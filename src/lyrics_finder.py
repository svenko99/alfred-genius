import os
import sys
import json
import requests
import datetime

DOWNLOAD_AND_DISPLAY_IMAGES = os.environ["DOWNLOAD_AND_DISPLAY_IMAGES"] == "1"
IMAGES_CACHE_DAYS = int(os.environ["IMAGES_CACHE_DAYS"])


def output_results(results):
    """Outputs the results in the Alfred json format."""
    return json.dumps({"items": results})


def create_alfred_item(
    title, subtitle=None, arg=None, quicklookurl=None, icon_path=None
):
    """Returns a dictionary with the given parameters."""
    return {
        "title": title,
        "subtitle": subtitle,
        "arg": arg,
        "quicklookurl": quicklookurl,
        "icon": {"path": icon_path},
    }


def download_image(url):
    """
    Downloads the image from the given url and returns the path to the file.
    If the file already exists, it returns the path to the existing file.
    """
    if os.path.exists(os.path.join("song_images", os.path.basename(url))):
        return os.path.join("song_images", os.path.basename(url))
    response = requests.get(url)
    if response.status_code == 200:
        directory = os.path.join(
            os.path.dirname(os.path.abspath(__file__)), "song_images"
        )
        os.makedirs(directory, exist_ok=True)
        file_path = os.path.join(directory, os.path.basename(url))
        with open(file_path, "wb") as file:
            file.write(response.content)
        return file_path
    return None


def delete_old_images():
    """Deletes the images that are older than IMAGES_CACHE_DAYS."""
    directory = os.path.join(os.path.dirname(os.path.abspath(__file__)), "song_images")
    for file in os.listdir(directory):
        file_path = os.path.join(directory, file)
        if os.path.isfile(file_path):
            file_age = (
                datetime.datetime.now()
                - datetime.datetime.fromtimestamp(os.path.getctime(file_path))
            ).days
            if file_age > IMAGES_CACHE_DAYS:
                os.remove(file_path)


def search_lyrics(query):
    """Searches for the given query and returns a list of results."""
    url = f"https://genius.com/api/search/lyric?q={query}"
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        hits = data["response"]["sections"][0]["hits"]
        results = []

        for hit in hits:
            song = hit["result"]
            title = song["full_title"]
            url = song["url"]
            snippet = hit["highlights"][0]["value"].replace("\n", ", ")
            image_url = song["header_image_thumbnail_url"]
            image_path = (
                download_image(image_url) if DOWNLOAD_AND_DISPLAY_IMAGES else "icon.png"
            )
            result = create_alfred_item(
                title=f"{title}",
                subtitle=snippet,
                arg=url,
                quicklookurl=url,
                icon_path=image_path,
            )
            results.append(result)

        return results

    return []


if __name__ == "__main__":
    delete_old_images()
    query = " ".join(sys.argv[1:])

    if results := search_lyrics(query):
        output = output_results(results)
    else:
        output = json.dumps({"items": [{"title": "No results found."}]})

    print(output)

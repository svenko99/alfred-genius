# 🎵 Genius Lyrics Finder Workflow for Alfred

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![macOS](https://svgshare.com/i/ZjP.svg)](https://svgshare.com/i/ZjP.svg)

## Introduction

The "Genius Lyrics Finder" is an Alfred workflow that allows you to quickly search for song lyrics using the Genius API. It provides a convenient way to find lyrics for your favorite songs right from your Alfred interface.

## Features

- **Quick and Easy Lyrics Search**: Simply type `lyrics` followed by the lyrics you're looking for, and the workflow will fetch the results.
- **Lyrics Results**: The workflow displays the song title, artist, a snippet of the lyrics, and a link to the full lyrics page on Genius.com.
- **Optional Image Download**: You can choose to download and display the song's header image as an icon in the workflow results.
- **Image Cache Management**: The workflow automatically deletes old header images from the cache to free up disk space, although image sizes are usually very small (150 KB).

## Installation

1. Download the "Genius Lyrics Finder" workflow from the [⤓ GitHub repository](https://github.com/svenko99/alfred-genius/releases/latest/download/Genius.Lyrics.Finder.alfredworkflow).
2. Double-click the downloaded file to install it in Alfred.

## Usage

1. In Alfred, type `lyrics` followed by the lyrics you want to search for. For example: `lyrics love me like you do`.
2. The workflow will fetch the lyrics results from Genius.com and display them in Alfred.
3. Click on a result to open the lyrics page on Genius.com in your browser.
4. To download and display the song's header image as an icon in the results, check `Download and display images` in `Configure Workflow...` in Alfred. Additionally, you can adjust the `Images cache days` setting to determine the number of days an image should be stored in the cache before being automatically removed.

	<img src="https://github.com/svenko99/alfred-genius/blob/main/images/example.gif" width=93% height=93%/>

## Acknowledgments

- The workflow utilizes the [Genius API](https://genius.com/developers) to search for song lyrics and retrieve the necessary data.

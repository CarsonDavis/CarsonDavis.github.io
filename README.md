# Writing Guide
I've put together a quick guide to the most common things I need to do on the blog.

## Post Header
Each post needs to have some stuff at the top. Not all of it is required. 

```
---
title: Fluorescent Rocks
date: 2020-01-02
last_modified_at: 2024-05-18
categories: []
tags: []
media_subpath: /Fluorescent+Rocks/
description: Details on my small collection of fluorescent rocks.
image: 20200213_002700.jpg
---
```
## Links
### Internal Links
`[Phone Meter Repair]({% link _posts/2018-06-24-phone_meter.md %})`
### Simple image links
`![20240516_225034](Fluorecent+Rocks.jpg)`

### Images Side by Side

```
<style>
    .grid-2x2 {
        display: grid;
        grid-template-columns: 1fr 1fr;
        grid-template-rows: auto auto;
        gap: 20px;
        justify-items: center;
    }
    .grid-3x2 {
        display: grid;
        grid-template-columns: 1fr 1fr 1fr;
        grid-template-rows: auto auto;
        gap: 20px;
        justify-items: center;
    }
    .grid-container {
        justify-items: center;
    }
    .grid-container img {
        width: auto;
        max-width: 100%;
        height: auto;
        object-fit: cover;
        display: block;
    }
    .grid-container .caption {
        text-align: center;
        align-self: start;
    }
</style>

<div class="grid-container grid-2x2">
    <div>
        <img src="image1.jpg" alt="image1">
    </div>
    <div>
        <img src="image2.jpg" alt="image2">
    </div>
    <div class="caption">
        <p>Caption 1</p>
    </div>
    <div class="caption">
        <p>Caption 2</p>
    </div>
</div>

<div class="grid-container grid-3x2">
    <div>
        <img src="rock.PNG" alt="white light">
    </div>
    <div>
        <img src="20200213_002157.jpg" alt="shortwave">
    </div>
    <div>
        <img src="20200213_003144.jpg" alt="shortwave">
    </div>
    <div class="caption">
        <p>white light</p>
    </div>
    <div class="caption">
        <p>shortwave</p>
    </div>
    <div class="caption">
        <p>shortwave</p>
    </div>
</div>
```


## Running and Debugging
The basic command I've been running is:
```
bundle exec jekyll serve --unpublished
```

However, if weird stuff is happening with the build, sometimes I'll burn the old site down and rebuild it.
```
rm -rf .jekyll-cache _site
bundle exec jekyll build --trace
```

And then I'll replicate the tests run on github actions.

```
 bundle exec htmlproofer ./_site --disable-external
```

## Getting Started on a New Computer

## Prerequisites

Follow the instructions in the [Jekyll Docs](https://jekyllrb.com/docs/installation/) to complete the installation of
the basic environment. [Git](https://git-scm.com/) also needs to be installed.

## Installation
You won't have any of the gems installed, so you'll need to run the following command to install them.
```
bundle install
```

## Usage

Please see the [theme's docs](https://github.com/cotes2020/jekyll-theme-chirpy#documentation).

## Images
### Converting to WebP
I've been using the `cwebp` command to convert images to webp format. You can install it with homebrew.
```
brew install webp
```

This command converts a jpeg to a webp file at 70% compression.
```
cwebp -q 70 0010_S2Ark7u.jpeg -o 0010_S2Ark7u.webp
```

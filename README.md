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
<div style="display: flex; justify-content: center; gap: 20px; align-items: center;">
  <div>
    <img src="20200206_214655.jpg" alt="white light" style="height: auto;">  
    <p style="text-align: center;">white light</p>   
  </div>
  <div>
    <img src="20200206_214647.jpg" alt="shortwave" style="height: auto;">
    <p style="text-align: center;">shortwave</p>   
  </div>
</div>
```

## Running and Debugging

## Getting Started on a New Computer

## Prerequisites

Follow the instructions in the [Jekyll Docs](https://jekyllrb.com/docs/installation/) to complete the installation of
the basic environment. [Git](https://git-scm.com/) also needs to be installed.

## Installation

Sign in to GitHub and [**use this template**][use-template] to generate a brand new repository and name it
`USERNAME.github.io`, where `USERNAME` represents your GitHub username.

Then clone it to your local machine and run:

```console
$ bundle
```

## Usage

Please see the [theme's docs](https://github.com/cotes2020/jekyll-theme-chirpy#documentation).

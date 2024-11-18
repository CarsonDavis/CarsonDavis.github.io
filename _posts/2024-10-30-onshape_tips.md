---
title: OnShape Tips
date: 2024-10-30
last_modified_at: 2024-11-02
categories: [bookbinding, projects log]
tags: []
description: A single post to collect all my bookbinding projects.
media_subpath: /bookbinding-projects/
image: header_image.webp
published: False
---
<style>
    .grid-2x2 {
        display: grid;
        grid-template-columns: 1fr 1fr;
        grid-template-rows: auto auto;
        column-gap: 20px; /* Keep horizontal gap */
        justify-items: center;
    }
    .grid-3x2 {
        display: grid;
        grid-template-columns: 1fr 1fr 1fr;
        grid-template-rows: auto auto;
        column-gap: 20px; /* Keep horizontal gap */
        justify-items: center;
    }
    .grid-container {
        justify-items: center;
    }
    .grid-container > div {
        display: flex;
        flex-direction: column;
        align-items: center;
        height: 100%; /* Ensure the div takes full height of the grid cell */
    }
    .grid-container .image-div {    
        justify-content: flex-end; 
    }
    .grid-container img {
        width: auto;
        max-width: 100%;
        height: auto;
        object-fit: cover;
        display: block;
        margin-bottom: 5px; /* Small margin to separate the image and caption */}
    .grid-container .caption {display: block;
        text-align: center;
        font-style: normal;
        font-size: 80%;
        padding: 0;
        color: #6d6c6c;
    }
</style>

## Introduction
I don't 3d model very often, and it seems like every time I want to do it I need to relearn the software and techniques. In this post I am going to document some of my most common operations, so that they are easy to find and reference in the future.

If you are forgetful or new to OnShape like me, I hope this post helps you as well!

## Constraints

## Drawing Constrained Lines
When drawing lines, you can ping them onto a line or point to automatically generate a constraint.

## Setting Variables
When dimensioning any area of a sketch, instead of typing a number you can type # and select create new variable. This will allow you to change the value of the variable in the Features Panel and have it update everywhere it is used in the model.

## Linking Variables to Text
- right click on the bottom of the text selection square and click Edit Text
- once the dialog box is open, right click on the text and click convert to expression
- instead of typing `4.25mm` type, you can type `toString(#trimming_length/mm)~"mm"` and it will automatically update to the correct value in the correct units with your added text of `mm`.

## Placing Text Within a Sketch
You'll need to decide if you are going to constrain the text within a certain height or width. Then you can draw two lines and pin the text midpoints to the lines. 
 
## Setting two Pieces to Match an Overall Length

## That Thing About Coplaner Lines or Something?

## Offset Tool
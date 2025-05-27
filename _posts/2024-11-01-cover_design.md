---
title: Book Cover Design
date: 2025-05-23
last_modified_at: 2025-05-26
categories: [bookbinding, cover design]
tags: []
description: Designing book covers in Affinity Design 2 and cutting with Silhouette Cameo.
media_subpath: /cover-design/
image: cover_design_post-cover_image-black_arrows.webp
published: True
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


## Overview

I've made around a half dozen covers in Affinity, and it feels like every time I walk away for more than a month all my hard-won knowledge evaporates, and I'm back to making rookie mistakes. How does the pen tool work again?

In this post, I've tried to consolidate a rough overview of my process, with some tips and tricks along the way...to hopefully finally break me out of the relearning cycle.

If you are _completely_ new to Affinity and Silhouette, it's probably a good idea to at least watch a couple tutorials online. I personally really enjoyed working through the videos by [Design Made Simple](https://www.youtube.com/watch?v=tAiAOprFNtU).


## Table of Contents

* [Overview](#overview)
* [Design Process](#design-process)
* [Setting Up Affinity](#setting-up-affinity)
* [Creating the Book Template](#creating-the-book-template)
* [Drawing](#drawing)
* [Export and Silhouette Cameo Preparation](#export-and-silhouette-cameo-preparation)
* [Troubleshooting Common Issues](#troubleshooting-common-issues)

## Design Process
Although I'm sure some people can just hop into Affinity and smash out a cover from scratch, I'm just a lowly engineer and often need a bit of inspiration. Sometimes I like to simply modify the original cover into something more vector friendly, like with Making of the Fittest. Sometimes I really will draw almost completly from scratch, like with Demon Haunted World. However, I especially like using AI image generation as a springboard to flesh out ideas - or even make basic assets I can trace into vectors, like with Empire of Cotton. 

If I had to outline my process, it would look something like this:
1. Brainstorm initial concepts
2. Use AI tools like ChatGPT for design ideation
3. Import reference materials and inspiration into Affinity
4. Create the cover

If you've never used a high-quality llm like OpenAi to get the creative juices flowing, I highly recommend it. You can prompt something like: "draw me a line art of a book cover for empire of cotton." ...which might be too complicated to cut with a silouette, so you can follow up with, "another one, simpler this time, with bold designs and clean lines."

<div class="grid-container grid-3x2">
    <div class="image-div">
        <img src="chatgpt_output.webp" alt="">
    </div>
    <div class="image-div">
        <img src="chatgpt_output_2.webp" alt="">
    </div>
    <div class="image-div">
        <img src="final_design_square.webp" alt="">
    </div>
    <div class="caption">initial ChatGPT design</div>
    <div class="caption">simpler ChatGPT design</div>
    <div class="caption">my final Affinity drawing</div>
</div>

This back and forth is excellent for helping me narrow down on the vibe that I want, and I can sometimes even get components I like enough to directly trace into vectors. You can see how helpful the two chatgpt covers were in pointing me towards my final design.


## Setting Up Affinity
When the design phase is over, it's time to get everything set up nicely within Affinity.

### Document Settings
I use a custom "Book Cover" preset with these values:
- Width: 350mm
- Height: 300mm
- DPI: 144
- Document Units: mm

>**Pro Tip:** These settings give enough room for a standard book and use convenient units for calipers. Save this as a preset to ensure consistency across projects.
{: .prompt-info }

### Workspace Organization

#### Artboards

Once I'm actually working in Affinity and creating different verions of the covers, I will create artboards. I copy and paste different major versions on each artboard, and this lets me easily make comparisons, create cut versions, etc.

![layout.webp](layout.webp)

Here you can see my multiple artboards for different versions, starting with the initial faithful vector conversion and then moving on to the modified final design.

<div class="grid-container grid-2x2">
    <div class="image-div">
        <img src="Screenshot_20241030_181734_Lightroom.jpg" alt="">
    </div>
    <div class="image-div">
        <img src="Screenshot_20241030_181837_Lightroom.jpg" alt="">
    </div>
    <div class="caption">front</div>
    <div class="caption">back</div>
</div>

And, of course, here is the final cover. 

#### Groups

Even when using artboards, you can be quickly overwhelmed by the number of curves and shapes. How you group items is a bit subjective, but I like to think about what objects I would want to edit or move together.

So I might have top level groups for:
  - Book Components (cover, spine, bands, etc)
  - Cut Components (design, art, title, etc)

And then within Cut Components I might have groups for
  - DNA
  - Title
  - Author Name
  - etc 

>**Grouping:** Entire groups can be hidden or locked together, making it easy to lock the book cover so you don't accidently move it, or to hide the book elements when exporting the text.
{: .prompt-info }

## Creating the Book Template
A fundamental challenge when making art for book covers is nailing the final sizing. You want the art you are designing to fit perfectly on the cover when you are finished. We accomplish that in a two step process. First we measure the book and draw it to the millimeter within Affinity. Then we export as PDF, which, believe it or not, is better than SVG at preserving the sizes on import into Silhouette.

### Measuring and Layout
1. Measure physical book dimensions precisely using calipers
2. Create two initial cover shapes. They'll be similar to this:
   - Main cover: ~ 150x220mm
   - Spine: ~ 25x220mm
3. Draw rectangles with a stroke width of 0 and a fill color to match your cover material

>**Measure What??** Don't include the gutter or the spine in your cover measurements. I only measure the surface of the board, since that's where the art will go. When in doubt, round down your measurement.
{: .prompt-info }

### Creating Spine Bands
1. Measure the width of your bands
2. Create a single rectangle for a band, in a slightly darker color than the cover
3. Position at top edge of the spine
4. Duplicate for additional bands
5. Click on them one after another and use the transform panel to reposition vertically

For example, one of my books had bands that were 5mm tall. Measuring from the top of the spine, they were 22, 47, 163, 189, 202 millimeters. 

>**Band Location:** When spacing spine bands, measure from the top of the spine to each band's top edge on the physical book. You can use math in the Transform panel to add your spine measurements to the existing Y location for perfect positioning. So in my example, +22, +47, etc.
{: .prompt-info }


## Drawing

### Border Creation
A lot of my covers feature a border of some kind around the perimeter, slightly inset from the edges. The contour tool can be great for this. The idea is that you make a copy of the book template and use the contor tool to decrease the size until it is the perfect border. Something like:
   - Inset: 7.5mm (this is effectively the distance from the edge)
   - Stroke width: 2.5-3pt
   - Fill: Transparent
   - Stroke color: Match your design scheme

>**Math Sucks:** Using the contour tool allows you to skip doing a bunch of math. If you want a border 7.5mm from the edge - use that as your inset. This saves you from calculating how big the border would need to be and carefully positioning it.
{: .prompt-info }

### Pen Tool and Node Manipulation

**Pen Tool Basics**

1. Press **P** to activate the Pen Tool.
2. Click to place **sharp nodes** (corner points) with straight segments between them.
3. Hold **Shift** while clicking or dragging to constrain new segments to 45° increments.

**Advanced Pen Tool**
1. Experiment with cap and join in the stroke menu
2. Create pressure profiles for variable width lines (this can really give your drawings more personality)

![line_width_2.webp](line_width_2.webp)

You can see that the left has a variable line width with round caps and the right has a constant line width with square caps. Neither is "correct" - you should experiment to see what works best on your cover.

**Converting to Curves**
After drawing a straight line, you often want to give it a curve. Of course this can be done by converting a node to smooth and using the handles, but I often find the following to be more intuitive:

1. Draw a straight line
2. Switch to the Node Tool (**A**).
3. Hover over a straight segment until you see the little squiggle cursor.
4. Click & drag that segment to pull it into a single-handle curve (creates one tangent handle).

**Smooth vs. Sharp Nodes**

* **Sharp nodes** have no handles and always form corners.
* **Smooth nodes** maintain C¹ continuity:

  1. Double-click an untouched node (in Node Tool) to convert it to Smooth.
  2. Two handles appear, linked 180° opposite—dragging one moves both, affecting both adjacent segments.

**Breaking Continuity**

* Hold **Alt** (Option on Mac) and drag **one** handle to move it independently (break the link).
* Add **Shift** to lock that handle’s movement to 45° increments.

**Adding & Removing Nodes**

* **Add a node**: While in the node tool, hover the mouse over a line until you see a squiggle then click and release.
* **Remove a handle**: Double-click a handle (or Alt-click) to delete it and restore a corner.

**Cheat Sheet**

| Action                          | Shortcut (Win)                       | Shortcut (Mac)                          |
| ------------------------------- | ------------------------------------ | --------------------------------------- |
| Activate Pen Tool               | `P`                                  | `P`                                     |
| Activate Node Tool              | `A`                                  | `A`                                     |
| Activate Move Tool              | `V`                                  | `V`                                     |
| Constrain line or handle to 45° | `Shift`                              | `Shift`                                 |
| Generate Curve                  | Hover for squiggle, click and drag   | Hover for squiggle, click and drag      |
| Convert node: Smooth ↔ Sharp    | Double-click node                    | Double-click node                       |
| Drag one handle independently   | `Alt` + drag                         | `Option` + drag                         |
| Remove a handle                 | Double-click handle (or `Alt`+click) | Double-click handle (or `Option`+click) |


### Tracing

1. **Import Reference** at \~50% opacity on its own layer. Lock the reference layer
2. **Map Major Points**: place a node at each key corner or curve start/end (avoid clicking mid-curve)
3. **Curve Segments**: hover for the squiggle, click & drag to shape.
4. **Refine Nodes**: switch to **A**, convert critical nodes to Smooth, tweak handles; use **Alt** to break continuity where necessary.
5. **Finalize**: adjust stroke weight, join segments, and clean up any stray nodes.
6. **Group Components**: group meaningful components so they can be moved and locked together

>**Node Placement:** I create a node at every major change in the drawing: new curve, new straight line, etc. I do _not_ click in the middle of existing curves. I create nodes at the beginning and end of a curve. 
{: .prompt-info }

>**Curve Dragging:** Creating smooth nodes and manipulating the handles directly isn't always needed. Instead, I hover until I see the squiggly and just drag the line to the correct curve. Only later will I manipulate node handles.
{: .prompt-info }


### Shapes
Shapes are the downfall of a new Affinity user. I don't want to tell you how long I struggled to wrap my head around consistent shape additions and subtractions. 

The idea is simple: you draw two shapes and then you can subtract one from the other, either by selecting and pressing the subtract button, or by using the shape builder tool. However, not every drawn item in Affinity can be combined, and there are a few gotchas to consider along the way.

The most important thing to know it that the only thing being subtracted are fills, _not_ strokes. When you expand something from curves, it will automatically be a closed shape made by vectors that have no stroke width. But if you have drawn shapes from scratch, it is possible they have a stroke width, which will wreck havoc on your shape subtraction.

**Guidelines**:
- all objects need to have fill (either native shapes or expanded strokes)
- native shapes should be drawn with no stroke, just fill

>**Shape Builder:** To use Shape Builder, first select all the shapes you want to subtract and add. Then open the Shape Builder and began drawing on the shapes you want to add, or holding alt and clicking the ones to remove.
{: .prompt-info }

<div class="grid-container grid-2x2">
    <div class="image-div">
        <img src="shapes_nodes.webp" alt="">
    </div>
    <div class="image-div">
        <img src="shapes_no_nodes.webp" alt="">
    </div>
    <div class="caption">nodes selected</div>
    <div class="caption">unselected</div>
</div>

Here's an actual problem I ran into while making the Empire of Cotton cover. I went to subtract the shapes, but got the result in the Fill has Stroke diagram. The left images show the nodes selected, so you can clearly see the vectors. Click on the images to enlarge.

- **Vectors**: The original shape I drew for the cover. Works great when you are still changing the sizes of everything.
- **Expanded**: The strokes are now expanded so that they can be subtracted.
- **Fill has Stroke**: Since the cotton bulb had a stroke, you can see that after subtraction the stroke followed into the cutouts, making them almost completely disappear.
- **No Stroke**: I've removed the stroke from the bulb and enlarged it to match the orignal size. Now the subtraction finally works as expected.

>**Too Late?** If you have already made a bunch of shapes with stroke widths, don't worry! 
- Duplicate the shape in a contrasting color.
- Remove the stroke, making it smaller. 
- Use the contor tool to increase the size until it matches the original.
{: .prompt-info }

<!-- ## Text and Typography
1. Use the Warp tool for curved text:
   - Easy method: Text Studio panel
   - Advanced method: Custom path warping
2. Convert text to curves before final export
3. Recommended fonts:
   - American Typewriter
   - Rockwell 4
   - STIX Two Text
   - Plantagenet Cherokee

## Text and Typography

### Text Basics in Affinity Designer
1. **Creating Text**  
   - Select the Text Tool (press **T**).  
   - Click once for **point text** (good for short labels) or click-and-drag for **frame text** (for blocks you’ll wrap or flow into).  
2. **Formatting**  
   - With your text selected, use the **Character** and **Paragraph** panels to set font family, size, line height, letter spacing, alignment, and more.  
   - Tip: Turn on **snap to baseline grid** (View → Show Grid → Baseline Grid) for perfect lines of type.  
3. **Converting to Curves**  
   - Once you’re happy, **right-click → Convert to Curves** to lock in your shapes before exporting or Boolean operations.

### Warping and Distorting Text
1. **Text on a Curve**  
   - Draw a path (Pen Tool **P**).  
   - Select your text, then **Text → Fit Text to Path** and adjust the offset in the context toolbar.  
2. **Envelope Warp (Mesh Warp)**  
   - Select your text (converted to curves), then **Layer → Convert to Curves** → **Layer → Warp Group → Convert to Mesh**.  
   - In the **Mesh Warp** panel, choose the number of rows/columns, then drag control points to distort.  
3. **Quad Warp**  
   - With curves selected, go **Layer → Convert to Curves**, then **Layer → Convert to Quad Warp**.  
   - Drag the corner handles to achieve perspective or fisheye effects.

If you deselect the warp group and lose you place, you can reselect the **group** and then switch over to the node tool.

### Links to Good Free & Paid Fonts
- **Google Fonts** (free):  
  https://fonts.google.com/  
- **Font Squirrel** (free):  
  https://www.fontsquirrel.com/  
- **MyFonts** (paid):  
  https://www.myfonts.com/  

### Some of My Goto Fonts

| Font Name                 | Use Case                                      |
| ------------------------- | --------------------------------------------- |
| **American Typewriter**   | Vintage/monospaced titles                     |
| **Rockwell 4**            | Bold, geometric headlines                     |
| **Plantagenet Cherokee**  | Elegant serifs for body copy                  |
| **STIX Two Text**         | Clean, academic designs                       |
| **Publico Text**          | High-readability book body text               |
| **Sama Tamil**            | When I need a distinctive display or script   | 

Where to download https://ng.maisfontes.com/bimbo-serif-main.font

List of good fonts
- American Typewriter
- AppleMyungjo
- Plantagenet Cherokee
- Publico Text
- Rockwell 4
- Sama Tamil
- STIX Two Text
- Trattatello

-->


## Export and Silhouette Cameo Preparation

### Add Layout Marks
When it comes time to actually position your art on the book, it's hugely helpful to have layout marks. I make them in Affinity, just by adding some dashes around my existing book template. But be careful - if you leave them when ironing, the HTV might adhere to the book. So I first color on the top of the transparency with marker before removing the HTV from underneath.

<div class="grid-container grid-3x2">
    <div class="image-div">
        <img src="layout_marks_affinity.webp" alt="">
    </div>
    <div class="image-div">
        <img src="layout_marks_printed.webp" alt="">
    </div>
    <div class="image-div">
        <img src="layout_marks_on_book.webp" alt="">
    </div>
    <div class="caption">in affinity</div>
    <div class="caption">cut on the sheet</div>
    <div class="caption">replaced with marker and on book</div>
</div>

### Exporting from Affinity
1. Hide the Book Components layer
2. Ensure all text is converted to curves and expanded
3. Ensure all shapes are converted to curves and expanded
4. Finalize any shape subtraction (see shapes section above)
5. Select final Artboard and export as PDF

### Silhouette Cameo Import Settings
1. Import as vector
2. Uncheck "Group objects"
3. Position with 10mm minimum margins
4. Mirror horizontally (Object → Mirror → Flip Horizontal)

### Critical Cutting Settings
- Text elements: Use outline cutting (if you didn't convert to curves)
- Solid shapes: Use center-line cutting
- Verify cut preview before proceeding
- Place material shiny side down

### Material Settings
For interested parties and my own reference, here settings that have worked in the past for me. However, I highly recommend testing first on a small scrap piece.

- Siser HTV Metal Bronze
  - Silhouette Settings: Heat Transfer, Reflective
  - Blade Depth 1, Force 10, Speed 6, Passes 1

>**Heating Disaster!** If you accidently heat for longer than the recommended time, you may see bubling on your HTV. In this case, DO NOT peel immediately as the glue will still be tacky. Instead, allow it to cool before peeling.
{: .prompt-info }

## Troubleshooting Common Issues

### Selection Troubleshooting

Sometimes, the object you are trying to select just won't seem to activate. 

If you are sure you have pressed V to enter the Move Tool, and you are clicking on a shape but nothing happens, it is probably either locked or within a group. You need to double click on groups to enter further within the structure so that you can then click on individual components.

### Vector Fill Problems
- Ensure objects have proper fill, not just strokes
- Use Layer → Expand Stroke when converting strokes to fills
- Select all objects before applying vector fills

### Text Cutting Issues
- Convert all text to curves before export
- Check for proper node reduction
- Verify cutting depth settings in Silhouette Studio

### Alignment Problems
- Use snap-to-grid for precise positioning
- Leverage alignment tools for consistent spacing
- Group related elements before final positioning

### Expand to Stroke Shennanigans

Occassionally line widths will suddenly become wonky after expand to stroke. I was once able to fix this problem by  changing the cap from circular to square extending beyond the point. 

I have also fixed this problem by opening the pressure menu in stroke and clicking reset. It turned out that in my supposedly "uniform" pressure curve, I actually had 3 points instead of 2.

### Shape Subtraction
Sometimes the shape builder tool just does some odd things. Often a close inspection will show that you had more nodes than necessary in your shape, or an internal node that was created during the conversion. 

When doing complicated subtraction, it's also very important to remember to have all the relevant shapes selected.


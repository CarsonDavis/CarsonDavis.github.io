---
title: Book Cover Design
date: 2025-05-23
last_modified_at: 2025-05-25
categories: [bookbinding, cover design]
tags: []
description: Designing book covers in Affinity Design 2 and cutting with Silhouette Cameo.
media_subpath: /cover-design/
image: cover_photo_2.webp
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


## Overview

I've made around a half dozen covers in Affinity, and it feels like every time I walk away for more than a month all my hard-won knowledge evaporates, and I'm back to making rookie mistakes. 

In this post, I've tried to consolidate a rough overview of my process, with some tips and tricks along the way, to finally break me out of the relearning cycle.

If you are completely new to Affinity and Silhouette, it's probably a good idea to at least watch a couple tutorials online. I personally really enjoyed working through the videos by [Design Made Simple](https://www.youtube.com/watch?v=tAiAOprFNtU).

<!-- ## Rough Overview
**Setup**
1. Brainstorm and design cover art with pen and paper and AI
2. Create a canvas in Affinity 
3. Carefully measure book and create template

**Art**
4. Draw the coverart, tracing from assets when it makes sense
5. Shape the title font

**Cutting**
6. Prepare document for cutting
7. Position and flip in Silhouette, then cut

**Application**
8. Peel and position HTV on cover
9. Heat press


| Stage           | Step | Task                                             |
| --------------- | ---- | ------------------------------------------------ |
| **Setup**       | 1    | Brainstorm cover art with pen and paper and AI   |
|                 | 2    | Create a canvas in Affinity                      |
|                 | 3    | Carefully measure book and create template       |
| **Art**         | 4    | Draw the cover art                               |
|                 | 5    | Shape the title font                             |
| **Cutting**     | 6    | Prepare document for cutting                     |
|                 | 7    | Position and flip in Silhouette, then cut        |
| **Application** | 8    | Peel and position HTV on cover                   |
|                 | 9    | Heat press                                       | -->
 

## Design Process
Although I'm sure some people can just hop in Affinity and smash out a cover from scratch, I'm just a lowly engineer and often need a bit of inspiration. Sometimes I like to simply modify the original cover into something more vector friendly, like with Making of the Fittest. Sometimes I really will draw almost completly from scratch, like with Demon Haunted World. However, I especially like using AI image generation as a springboard to flesh out ideas or even make basic assets I can trace into vectors, like with Empire of Cotton. 

If I had to outline my process, it would look something like this:
1. Brainstorm initial concepts
2. Use AI tools like ChatGPT for design ideation
3. Import reference materials and inspiration into Affinity
4. Create the cover


If you've never used a high-quality llm like OpenAi to get the creative juices flowing, I highly recommend it. You can prompt something like: "draw me a line art of a book cover for empire of cotton." ...which might be too complicated to cut with a silouette, so you can follow up with, "another one, simpler this time, with bold designs and clean lines"

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

This back and forth is excellent for helping me narrow down on the vibe that I want, and I can sometimes even get designs components I like enough to directly trace into vectors. You can see how helpful the two chatgpt covers were in pointing me towards my final design.


## Setting Up Affinity
When the design phase is over, it's time to get everything set up nicely within Affinity.

### Document Settings
I use a custom "Book Cover" preset that gives me enough room to work with and specifies the same units that I like using when measuring books.
- Width: 350mm
- Height: 300mm
- DPI: 144
- Document Units: mm

>**Pro Tip:** These settings provide ample workspace while maintaining print quality. Save this as a preset to ensure consistency across projects.
{: .prompt-info }

### Workspace Organization

#### Artboards

Once I'm actually working in Affinity and creating different verions of the covers, I will create arboards. I copy and paste different major versions on each artboard, and this lets me easily make comparisons, create print versions, etc.

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

And, of course, here we have the final cover. 

#### Groups

Even when using artboards, you can be quickly overwhelmed by the number of curves and shapes. I try to very deliberately name and group curves that I would later want to move or edit together. 

So I might have top level groups for:
  - Book Components (cover, spine, bands, etc)
  - Print Components (design, art, title, etc)

And then within Print Components I would have groups for
  - Title
  - Candle
  - Light Beams
  - etc 
2. Keep your layers panel organized with clear naming conventions
3. Save custom workspaces for different stages of the design process

>**Printing** Entire groups can be hidden or locked together, making it easy to lock the book cover so you don't accidently move it, or to hide the spine when exporting the text.
{: .prompt-info }

## Creating the Book Template

### Measuring and Layout
1. Measure physical book dimensions precisely using calipers
2. Create two initial cover shapes. They'll be similar to this:
   - Main cover: ~ 150x220mm
   - Spine: ~ 25x220mm

>**Measure What??** Don't include the gutter or the spine in your cover measurements. I only measure the surface of the board. 
{: .prompt-info }

### Creating Spine Bands
1. Design single band template
2. Position at spine top
3. Duplicate for additional bands
4. Use Transform panel for precise spacing
5. Measure from physical book for accuracy

>**Measurement Tip:** When spacing spine bands, measure from the top of the spine to each band's top edge on the physical book. Use these measurements in the Transform panel for perfect positioning.
{: .prompt-info }

### Border Creation
A lot of my covers feature a border of some kind around the perimeter, slightly inset from the edges. The contour tool can be great for this. Something like:
   - Inset: 7.5mm
   - Stroke width: 2.5-3pt
   - Fill: Transparent
   - Stroke color: Match your design scheme

Using the contour tool allows you to skip doing a bunch of math.

## Drawing
### Pen Tool and Node Manipulation

**Pen Tool Basics**

1. Press **P** to activate the Pen Tool.
2. Click to place **sharp nodes** (corner points) with straight segments between them.
3. Hold **Shift** while clicking or dragging to constrain new segments to 45° increments.

**Converting to Curves**

1. Switch to the Node Tool (**A**).
2. Hover over a straight segment until you see the little squiggle cursor.
3. Click & drag that segment to pull it into a single-handle curve (creates one tangent handle).

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

>**Curve Dragging:** Creating smooth nodes and manipulating the handles directly isn't always needed. Instead, I hover until I see the squiggly and just drag the line to the correct curve. Only later will manipulate node handles.
{: .prompt-info }


### Shapes
Shapes are the downfall of a new Affinity user. I don't want to tell you how long I struggled to wrap my head around consistent shape additions and subtractions. 

The idea is simple: you draw two shapes and then you can subtract one from the other, either by selecting and pressing the subtract button, or by using the shape builder tool. However, not every drawn item in Affinity can be combined, and there are a few gotchas to consider along the way.

The most important thing to know it that the only thing being subtracted are fills, _not_ strokes. When you expand something from curves, it will automatically be closed shape made by vectors that have no stroke width. But if you have drawn shapes from scratch, it is possible they have a stroke width which will wreck havoc on you shape subtraction.

**Guidelines**:
- all objects need to have fill (either native shapes or expanded strokes)
- native shapes should be drawn with no stroke, just fill


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


Here's an actual problem I ran into while making the Empire of Cotton cover. The left images show the nodes selected, so you can clearly see the vectors. Click on them to enlarge.

- **Vectors**: The original shape I drew for the cover. Works great when you are still changing the sizes of everything.
- **Expanded**: The strokes are now expanded so that they can be subtracted.
- **Fill has Stroke**: Since the bulb had a stroke, you can see that after subtraction it followed into the cutouts, making them almost completely disappear.
- **No Stroke**: I've removed the stroke from the bulb and enlarged it to match the orignal size. Now the subtraction finally works as expected.

>**Too Late?** If you have already made a bunch of shapes with stroke widths, don't worry! 
- Duplicate the shape in a contrasting color.
- Remove the stroke, making it smaller. 
- Use the contor tool to increase the size until it matches the original.
{: .prompt-info }


## Text and Typography
1. Use the Warp tool for curved text:
   - Easy method: Text Studio panel
   - Advanced method: Custom path warping
2. Convert text to curves before final export
3. Recommended fonts:
   - American Typewriter
   - Rockwell 4
   - STIX Two Text
   - Plantagenet Cherokee

## Export and Silhouette Cameo Preparation

### Add Layout Marks
Actually aligning the cover with the book can be a nightmare with no reference marks. I like to look at the exact dimensions of the front cover boards, not including the spine or the gap, and add indexing markers here.

### Exporting from Affinity
1. Hide Print Components layer
2. Ensure all text is converted to curves
3. Ensure all shapes are converted to curves
4. Finalize any shape subtraction (see shapes section above)
5. Export as PDF

### Silhouette Cameo Import Settings
1. Import as vector
2. Uncheck "Group objects"
3. Position with 10mm minimum margins
4. Mirror horizontally (Object → Mirror → Flip Horizontal)

### Critical Cutting Settings
- Text elements: Use outline cutting
- Solid shapes: Use center-line cutting
- Verify cut preview before proceeding
- Place material shiny side down

### Materials
- If you accidently heat for longer than the recommended time, you may see bubling on your HTV. In this case, DO NOT peel immediately. As the glue will still be tacky. Instead, allow it to cool before peeling. 

- Siser HTV Metal Bronze
  - Silhouette Settings: Heat Transfer, Reflective
  - Blade Depth 1, Force 10, Speed 6, Passes 1

## Troubleshooting Common Issues

### Selection Troubleshooting

Sometimes, the object you are trying to select just won't seem to activate. 

If you have pressed V to enter the Move Tool, and you are clicking on a shape but nothing happens, it is probably either locked or within a group. You need to double click on groups to enter further within the structure so that you can then click on individual components.

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

Another problem I've seen in this phase is that previously even and constant width strokes will suddenly become triangular after expand to stroke. I have been able to fix this by changing the cap fom circular to square extending beyond the point. This effect is also seen sometimes when importing an unexpanded curve into Silouhette. 

I have also fixed this problem by opening the pressure menu in stroke and clicking reset. It turned out that in my supposedly "uniform" pressure curve, I actually had 3 points instead of 2.

### Object Overlapping
So, often I have the problem that I used overlapping objects to hide areas of the stroke during drawing, and when I get to the cutting stage it wants to cut all those hidden object. Since I am always cutting out of one color, it seems like there should just be an easy way to select all gold and cut around it, but I haven't found this option in a way that works. 

Using Affinity Design's Select by fill color doesn't behave how I expected, and the exported selections still contain things not in the fill.

So, instead, what I do is go through the entire drawing and expand everything into real shapes, then use subtraction to cut away all the parts I was previously hiding with mere colors. 

- convert all objects to curves, Layer → Convert to Curves
- expand all strokes, Layer → Expand Stroke
  - this gives everything an external geometry instead of internal line
- any background color areas that were hiding parts of the foreground now need to be subtracted.
  - start at the lowest layer and select it, then the layer that is masking it
  - subtract
  - if weird stuff happens, one of your layers was not correctly expanded to strokes
Now is also the time to tidy up any of your overlaps. Once things are expanded to strokes, it becomes easier to manipulate every egde and corner. You might want to think about deleting some nodes, moving them around, or tweaking their handles. 
Sometimes wierd things happen when expanding, so always go back through your shapes and add and subtract them one by one until you get the finished item.


## Resource List

### Recommended Tutorials
1. Pen Tool Mastery
2. Vector Tracing Techniques
3. Typography in AD2
4. Silhouette Studio Advanced Cutting

### Useful Keyboard Shortcuts
- Ctrl + Alt + V: Paste inside
- Ctrl + J: Duplicate in place
- Hold Shift: Constrain proportions
- Hold Alt: Copy while dragging





# Notes
There are several things that i think i have specific tips on such as:
- using the text tool
- using warp to make nice shapes with text (there was an easy and a hard way iirc)
 
------------------

Selecting
click an object, go to the select menu, then select same
you can do by color, brush type, etc

Control + alt + v
paste drawing inside another drawing
double click to get inside of objects to select theem

Making Objects
When sizing an object, hold shift or control to lock the aspect ratio or scale from the middle
Hold shift key while rotating to lock to 15 degree increments


Brush Tool
take a shape and apply a brush to it
you can then change the size with brackets

Booleans
don’t forget these, they are very cool
divide, holy shmoly

Alighnment
use the menu to align stuff relative to the canvas
actually, you can do all kinds of alignments
use the magnet icon to snap shapes to each other


Hold control to duplicate

Image View

What does rasterizing the layer do??
an image layer is not editable as pixels, but rasterizing turns it into a pixel layer that you can edit

Selections
While making a shape selection, you can hold space to move the selection around. 
You can use selection brush tool. W on keyboard. Make the brush bigger and smaller. Zoom in and move with mouse and alt
After selecting, you can click the refine button and then paint with foreground and background

Tutorials
Unfinished Tutorials
Halftone Boom
Overlapping Letters Logo
Video Link
Download fonts from https://www.myfonts.com/products/condensed-regular-winner-394140
You just download it, double click it, and it gets installed
Layer -> convert to curves
this will turn the letters into vectors so we can play with them as if they were shaps
Sizing
if you draw the whole letter, it will fuck it up. So instead, you can use the nodes tool to only grab the top nodes and collapse them
Hold shift to stay in a straight line
Magic Letter Fuckery
grab the nubs of the E using shift and then nodes tool (A)
Grab transform from the top bar and hold control to size them at the same time
I’m guessing this is going to be great for messing with symmetric covers
Oh I see. it is treating the selection as a single shape, but doing the transform from both directions. Since they are nodes, it makes it seem line it is expanding
You can use this to widen individual parts of the letter. Just imagine it forming a square with your selection
Contour
You use the contour tool to make the duplicated letters bigger
then the shape builder to delete parts and then merge parts so you end up with the final shape
Lines Letter Logo
Video Link
make a letter with a bold font. I used Arial Black Bold
convert to curves
draw a line with the pen tool, holding shift to make it straight
increase the stroke width using the stroke tab on the far right
You can click the pressure button on the right, add a point, and then drag it to change it to an embiggining line!!!!!
magic copy
after copy and pasting and moving carefully with shift, you can press control j to duplicate in the same location each time. i had to try this a couple times, it didn’t work immediately. probably som OOO thing to figure out
use shapebuilder to minus the strokes, then delete or hide you letter layer
to add sexy colors, Layer, Geometry, Merge Curves (I have no idea how this is different from adding shapes or whatever)
Gradient, stroke, linear
Warped Text Logo
Video Link
When you are typing, you can hold down alt and then arrow to completely change the kerning of text. This is in the text, spacing menu
Don’t forget, you can hold control while sizing to do it from the center. This works with edge and corner sizing.
on the layer menu, you can turn on warp, then at the top, you can turn on snapping. i also had to turn on snap to object geometry
after setting first the corners and then the top, you can click on the nodes to gain access to the curve handle. you can then tweak all the node curve handles to get a nice circle
convert to curves and then warp with the fish eye

draw the shape you want to warp into. I start with a rectangle, then convert to curves, then warp the rectangle with the node tool
type the text and size it inside the box
convert the text to curves
select the text, go to the layer menu, and convert to quad warp
get the corners warps. then you can grab the center of one of the warp line as if you were using the node tool
Nature Sucks
video link
Line Joins
when making a shape and then editing the stroke, you can change how all the line connect by altering the join. In our case we went from a soft round to a miter 
Door Frame
To give ourselves a door frame, we can come over to the corners tool, select both corner nodes, and then fully round over the corner
Door Border
to make the border around the inner door, do a duplicate and then a contour, choosing the contour type of miter at the top of the screen so that you will still  have sharp corners
Spacing
the align menu has an align thing which will auto align the shape within the exterior of the are that they describe.
Shape Manipulation
After making a rectangle and rotating it, we can then convert it to curves and break the curves in order to get two V shapes. This is a useful way to break apart shapes when the shape builder minus tool is inconvienient
Vector Fill
I was having a really hard time with vector fill, and I believe the solution was to select all the objects prior to using the fill
Shield Letters
Building Shapes from lines
You can make lines between two points make making individual clicks with the pen tool 
after drawing some stuff with lines, you can use the shape builder to actually make the shapes as objects. In our case, we make 4 triangles by drawing lines through a square
Making the grid
as you drag copy elements by using alt, you can let go of alt to allow snapping
immediately press control j to copy the action
Making the shield
as you make the circles, don’t forget that you can still align horizontally by 3 spacings
use the intersection tool to create the shield

Repeat Objects Along A Path
Link
Build the shape
make a 10x14 square grid. 
select everything, enter the shapebuilder, then delete the stuff you don’t want
add the remaining stuff
make it black and then group it
Make a brush
with the shapes selected, export as png
use selection only. this should give you just the black with a transparent background in and around
make a brush category and then add a new textured intensity brush
change body from stretch to repeat by double clicking on the brush
using it
you can now use it as a stroke. 
remember that you can change the scale with object checkbox if desired

How to use the pencil tool
link
HOLY SHIT
stabilizer, rope mode
this is incredible, allows you to make these beautiful smooth lines with sharp corners
window mode
can’t really fully tell the difference between these two modes. Probably need to watch a dedicated tutorial on the subject
sculpt mode
this will let you continue lines after unclicking from a node, creating a single curve
pressure profiles
use this to change the thickness along the length of a stroke
HOLD DOWN COMMAND TO ENTER NODE TOOL
Stock Images
you can activate the stock window and download free vector and other images


Mastering the Pen Tool
after you draw with a pen, there are 3 kinds of nodes
sharp
the two handles on either side of the node adjust separately
enter by holding option, either while forming a node, or while adjusting a handle
smooth
the two handles on either side of the node adjust together
smart
pen modes:
pen mode
this is all the stuff that we have been talking about
smart mode
polygon mode
just draws straight lines between points that you can later come back and tweak
i had the best luck with this while doing the flame
every time there seems to be a fundamental change to the curve add a new break
click and hold, then you can set the contour of the curve by using the handles on the first point
you can click and drag at every step
hold option while adjusting a node and it will snap one side of it?


--------------------------------

here is a previous partial draft of the cover design post:

## Creating a New Documents
To get started, measure your book dimensions. Then create a new document in Affinity Design large enough to hold the book unfolded with some extra space. I use the following settings as a default.
- Width: 350mm
- Height: 300mm
- DPI: 144
- Document Units: mm

Measure the book cover, not the spine. Under measure if you need to.

Tip: If you are going to make a lot of book covers, it is worth making a custom preset. After going to File > New and setting the width, height, etc, you can then click the icon to create a new preset. 

## Create the Book Components
### Measure the Book
We want to draw the outline of the front, back, and spine. 

When a book is closed, you can see the side of the spine, the hinge gap, and the cover. We want to specifically measure only the area of the cover itself, where there is board underneath. Later, we will print indexing marks to make placing the vinyl easier. So we want to measure all the way to the edges of the cover, but not the hinge gap or the spine.

Similarly, measure the working area of the spine.

As an example, I measured a book that was:
- cover: 144x218
- spine: 29x218

Always use the exact measurement, but when in doubt, it is better to round down than up. This will keep you from making a design too big to fit on the actual book. 

### Draw the Covers and Spine
Select the rectangle tool and in the side panel change the stroke to transparent and the fill color to match your leather. Stokes are not considered part of the dimensions of a shape. 

Draw an arbitrary rectangle. 

With the rectangle still selected, you can change from the layers panel to the transform panel. Here you can change the dimensions of the rectangle to match the dimensions of the cover. Copy and paste this twice to make the spine and the back cover.

For the spine, change the width.

Tip: Keyboard shortcuts: You an press V on your keyboard to switch from drawing rectangles to the movement/selection cursor. With the rectangle selected, you can hold control and drag and a copy will be made.

### Align the Covers
- Select all three shapes
- Align Vertically: Align Top
- Align Horizontally: Space Horizontally
- You can play with the spacing and realign horizontally. Note that the two exterior shapes will stay in the same place, but the middle shape will move.

To align on the page, first make a group called 'Book Components' with the spine and covers. 
- First select the back rectangle
- Then select the group, Book Components
- Align Vertically: Align Middle
- Align Horizontally: Align Center

### Draw the Spine Bands
- Measure the height of a spine band
- measure the position of each spine band, starting from the top of the spine to the top of each band

In my case,  
- each band is 5mm tall
- and they are positioned at the following locations: 22, 47, 163, 189, 202

Copy and paste the spine, then edit it to be the height of a spine band and slightly darker than the cover color.
Copy and paste your new band for each band you need.

- if your bands are not already aligned at the top of the spine, do so
- click on each band and use the transform panel to add your measurements to the y position
- you can use math in the transform panel. For example, for my first band, I added *+22* to the existing y position: *41.3 mm+22*

Make sure that all the Book Components are in the Book Components group.



You should now have something that looks like my screenshot:

#

When making the bands, create a single band of the correct dimensions, slightly darker than the cover material. The position it at the very top of the spine and copy paste it for each band. Measure on the book from the top of the spine to the top of each band and use math in the transform panel to add the numbers to each band.



Tip: I don't like working in the white affinity background, so I usually make a rectangle the size of the document and fill it with a light grey that gently contrasts with the color of the leather I'm using for my book rectangles. After drawing this rectangle, you lock it in the panel so you can't accidently select it.

copy one of your covers and then use the contour tool to make the border. i've been doing it inset by 7.5mm. You will want to give it transparent fill but a colored stroke. I've been using 2.5-3 pt for the stroke width.


Hold alt and drag to copy the cover.

For some of my recent books, I have been making simplified vector versions of the original covers. Find a nice copy of the original cover online and paste it into your document at 50+ transparency. Then trace over it with the pen tool. You can use the contour tool to make the border.


Tips for using the pen tool

A to select and edit nodes
V to select shapes
P to select the pen tool
While using the pen tool, if an existing node is highlighted blue, you can continue from it. 
You can edit your curves by clicking a node and then moving the handles. You can also hover over a curve and see a wavy line and drag it to adjust the curve. You can add new nodes along the path of curves.




Once you make the band text, you can align vertically and distribute horizontally. You always want to select the bands first, and then the text.
 
I like to group everything into Book Components and Print Components, then hide the print components and export as PDF.

When bringing it into silhoutte, import it as vector but do <i>not</i> group. This will allow you to change the cut settings for the text vs the cover.

Arrange it in silhoutte and position it reasonably close to the top. I try to leave some space around the covers, because any excess plastic can be marked and used as a positioning aide. Try to leave at least 10 mm on all sides, since the inset is usually around 7.5mm.


Once it is placed, go to object, mirror, then flip horizontally. 

Don't cut off more than you need, just 20mm or so beyond the expected bottom. You are leaving some room for positioning and some room for the cutter to be misaligned.

The shiny side goes down


Where to download https://ng.maisfontes.com/bimbo-serif-main.font


List of good fonts


American Typewriter
AppleMyungjo
Plantagenet Cherokee
Publico Text
Rockwell 4
Sama Tamil
STIX Two Text
Trattatello









The post structure should be something like this:

- 

. make workspaces if needed for different iterations

main sections:
- why affinity design
    - single purchase: $69.99
    - affinity design 2 has really caught up to illustrator
- do you need silouette studio buisness edition?
    - no, you can use affinity design 2
    - i thought this was needed to get SVG import, but turns out PDF is the best
using affinity design...
- setting up the canvas. i used a 
- making an 
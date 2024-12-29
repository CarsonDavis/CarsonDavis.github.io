---
title: Cover Design
date: 2024-11-02
last_modified_at: 2024-11-02
categories: [bookbinding, projects log]
tags: []
description: Designing book covers in Affinity Design 2.
media_subpath: /cover-design/
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


# Comprehensive Guide to Book Cover Design with Affinity Designer 2 and Silhouette Cameo

## Overview

This guide walks through the complete process of designing and cutting book covers using Affinity Designer 2 (AD2) and Silhouette Cameo (SC). While the principles apply to other software like Adobe Illustrator or Cricut, specific tips and techniques focus on AD2 and SC workflows.

## Initial Setup

### Document Settings in Affinity Designer 2

Create a custom "Book Cover" preset with these specifications:
- Width: 350mm
- Height: 300mm
- DPI: 144
- Document Units: mm

>**Pro Tip:** These settings provide ample workspace while maintaining print quality. Always save this as a preset to ensure consistency across projects.
{: .prompt-info }

### Workspace Organization

For optimal workflow in AD2:
1. Create two main layer groups:
   - Book Components (visible elements)
   - Print Components (technical elements)
2. Keep your layers panel organized with clear naming conventions
3. Save custom workspaces for different stages of the design process

## Design Process

### 1. Design Conceptualization
1. Brainstorm initial concepts
2. Use AI tools like ChatGPT for design ideation
3. Gather reference materials and inspiration
4. Sketch rough layouts before moving to digital

### 2. Asset Collection and Preparation
1. Source assets from AD2 stock library
2. Import and organize external assets
3. Convert all assets to appropriate format (vector/raster)

### 3. Creating the Base Structure

#### Measuring and Layout
1. Measure physical book dimensions precisely using calipers
2. Create cover shapes:
   - Main cover: Usually 144x218mm
   - Spine: Typically 24x218mm
   - **Always measure the actual book and adjust accordingly**

#### Border Creation
1. Use the Contour tool for professional borders:
   - Inset: 7.5mm
   - Stroke width: 2.5-3pt
   - Fill: Transparent
   - Stroke color: Match your design scheme

>**Technical Note:** When creating borders, using the Contour tool rather than manual drawing ensures perfect alignment and consistent spacing.
{: .prompt-info }

### 4. Advanced Design Techniques

#### Using the Pen Tool
- Press 'A' to select/edit nodes
- Press 'V' to select shapes
- Press 'P' to activate pen tool
- Blue-highlighted nodes indicate connection points
- Hold Shift for straight lines
- Double-click curves for quick adjustments

#### Vector Tracing Tips
1. Import reference image at 50% opacity
2. Create new layer above
3. Trace key elements with pen tool
4. Use node tool (A) for refinements
5. Apply appropriate fills/strokes

#### Text and Typography
1. Use the Warp tool for curved text:
   - Easy method: Text Studio panel
   - Advanced method: Custom path warping
2. Convert text to curves before final export
3. Recommended fonts:
   - American Typewriter
   - Rockwell 4
   - STIX Two Text
   - Plantagenet Cherokee

### 5. Spine Design

#### Creating Spine Bands
1. Design single band template
2. Position at spine top
3. Duplicate for additional bands
4. Use Transform panel for precise spacing
5. Measure from physical book for accuracy

>**Measurement Tip:** When spacing spine bands, measure from the top of the spine to each band's top edge on the physical book. Use these measurements in the Transform panel for perfect positioning.
{: .prompt-info }

### 6. Export and Silhouette Cameo Preparation

#### Exporting from AD2
1. Hide Print Components layer
2. Export as PDF
3. Ensure all text is converted to curves
4. Verify vector integrity

#### Silhouette Cameo Import Settings
1. Import as vector
2. Uncheck "Group objects"
3. Position with 10mm minimum margins
4. Mirror horizontally (Object → Mirror → Flip Horizontal)

#### Critical Cutting Settings
- Text elements: Use outline cutting
- Solid shapes: Use center-line cutting
- Verify cut preview before proceeding
- Place material shiny side down

## Troubleshooting Common Issues

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

## Final Tips and Best Practices

1. Always work with backup copies
2. Test cut settings on scrap material
3. Maintain organized layer structure
4. Document successful settings for future reference
5. Regular saving and versioning

>**Workflow Tip:** Develop a consistent naming convention for your files and layers. This becomes crucial when working on multiple book covers or revisiting projects months later.
{: .prompt-info }


# Notes


I want to write a post on my processes for designing book covers using affinity design 2 and siloutte cameo.
the tutorial will be applicable to other software, such as illustrator or cricut, but will have many specific tips for AD2 and SC.

the overview of my process is something like this:
1. brainstorm ideas for the cover and go back and forth with chatgpt on possible designs
2. use any assets from GPT or the affinity design stock images that i can
3. make a document with my book preset
4. measure the book with calipers/ruler and draw the cover and spine
5. use the outline? tool to trace any art (need to give tips here)
6. add text
7. export as PDF
8. import into siloutte cameo

There are several things that i think i have specific tips on such as:
- using the pen tool
- using the contour tool
- using the shape builder tool
- using the text tool
- using warp to make nice shapes with text (there was an easy and a hard way iirc)
- using the stock images in affinity
- the exact document settings that I use
- how to organize the layers in affinity
- how to organize workspaces in affinity
- how to import the PDF into siloutte cameo (grouped or not grouped, etc)
- how you can change the text or lines so that they cut correctly in siloutte cameo...there is something special about whether it is rasterized or not that i think is in my notes
   - if it isn't, you have to treat it differently when you are in siloutte cameo, because some things will cut the outline, and others will cut the line in the middle
- tips on filling in shapes and good and bad ways to do it 
 
------------------

here is an example of how i do tips and formatting in other posts:

#### 6. **Scoop and Chill the Dough:**
1. Using a **¼-cup measure**, scoop dough portions onto a parchment-lined baking sheet.  
2. Cover tightly with plastic wrap and refrigerate for **12 to 48 hours**.  

>**Rest the Dough:** It doesn't need to be a baking sheet -- I shove mine into tubberware. But you must let them sit at least overnight. In my experience, the flavors continue to merge and the final texture improves for up to about 2 days.
{: .prompt-info }


#### 7. **Prepare the Oven and Bake:**
1. Preheat oven to **350°F**.  
2. Place **6–8 dough balls** on an aluminum foil-lined baking sheet.  
3. Bake for **15–18 minutes**.  
4. Let them crystalize! Rest them for about 3 minutes, and they will be warm, gooey, and perfectly crunchy. Eat them too soon and they will just be too hot and soft.

>**Baking:** Baking is maybe the most important part of any cookie. You can have the best recipe, but if you don't bake it right, it won't shine. I usually take them out around 15-16 minutes. The goal is some softness in the center but a nice crunch on the outside. The tops should have a nice golden brown color. If the cookie isn't the perfect mix of gooey and crunchy, then you need to adjust your baking times. 
{: .prompt-info }

--------------------------------

here are some notes that I took while learning affinity design and taking tutorials:
Cutting Objects
If you are going to subtract objects from each other, they need to have fill, not just curves. Its good to do it like this:
the base object should be crafted from the start with no stoke, just fill
if you are already far into your project, you can duplicate, remove stroke off one, and use the contour tool to increase the size to remake it like the original
if you need to subtract any strokes, you can Layer => Expand Stroke
this will convert a stroke to a fill
then arrange the objects in the layers panel, subtract on top, and 

sick t shirts guy
what the hell are artboards??


HOLY SHIT
incredible video of dude making a mushroom character in vector art with shading and stuff

Selecting
click an object, go to the select menu, then select same
you can do by color, brush type, etc

Control + alt + v
paste drawing inside another drawing
double click to get inside of objects to select theem

Making Objects
When sizing an object, hold shift or control to lock the aspect ratio or scale from the middle
Hold shift key while rotating to lock to 15 degree increments

Using the Pen Tool
You can hold shift to lock the line
You can drag while placing a point to make it curved

Pencil Tool
the pencil tool automatically makes curves that match a softened version of what you drew

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
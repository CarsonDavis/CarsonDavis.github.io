---
title: Troublesome Translations
date: 2025-03-10
last_modified_at: 2025-03-12
categories: [coding, ocr]
tags: []
description: Attempting to translate a 16th-century French text with OCR
media_subpath: /troublesome-translations/
image: cover_image.webp
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

## Background
### Martin Guerre
In 1548, Martin Guerre mysteriously disappeared from his small village in southwestern France, leaving behind his wife Bertrande and a young son. Eight years later, he finally returned, greeting everyone by name, reminiscing about old times, and getting back into the good graces of his wife and four sisters.

Perhaps some of the villagers occasionally thought that something was off about the long-lost Martin, but he was generally accepted back into village life, and over the next three years had two children with his beautiful wife, of which one survived. He began doing business around the village, and it seemed like he might actually be on track to make him and his wife Bertrande into wealthy merchants.

But then came his inheritance disputes with his uncle Pierre Guerre, and his world began to disintegrate. Pierre started telling anyone who would listen that the long-lost Martin was in fact an imposter. 

The following years were full of lies, murder plots, imprisonments of all the involved parties, and a dramatic ending. Thankfully, one of the judges who ruled over the subsequent court cases was so moved that in 1561 he wrote a book on the events, and the rest is history.

### Arrest Mémorable
I discovered this fabulous story when I read Natalie Davis's 1983 <i>The Return of Martin Guerre</i>. Natalie was a cross cutting historian who became obsessed with the story, and deeply researched everything she could, from the original writings about the court case to the land grants and small claims records in the surrounding towns. Her book is a short and excellent read, though I would recommend skipping the introduction, as it gives away the ending. 

But like I said, it's short, and it left me wanting to dig more into the details of the case. Thankfully the judge Jean de Coras wrote an entire book on it in 1561, full of interesting commentary and annotations. This commentary promises to give insight into how contemporary witnesses viewed the case and it's religious and moral ramification. (As a fascinating historical note, the Judge Jean de Coras was later murdered during the Saint Bartholomew's Day Massacre, along with as many as 30,000 other protestants by French Catholics.)

So off I went to find an english version...and nothing. As far as I can tell, there is no modern english printing. There is no historic english translation. There is nothing.

Well, almost. I looked and looked, and finally, I did find something in an old journal, <i>Translation of the main text of Coras, Arrest Memorable, by Jeannette K Ringold, in Triquarterly 55 (Fall 1982): 86-103.</i> Although you may have noticed the caveat in the title, the all-important word "main". Sadly the article only translates the main text, and not the annotations, which was the part I was most looking forward to. In fact, the translation is 13.5 pages long, while the original book is closer to 160.

That number exaggerates the loss a little, since one must make allowances for the fact that 1500s books simply didn't cram all that many words onto a page, but suffice to say, I was disappointed.

If I wanted to read the annotations, I would have to translate them myself.

## The Plan
If we're being perfectly honest, I may have just let this drop after finding the main text translation. After all, is it really worth the effort? But this is actually the <i>third</i> time this has happened to me in as many months, and I had begun to get fed up. I collect old books, and I've got two other annotated 1600s books on my shelves that I also haven't found any translation for. 

Thankfully we live in a remarkable age. Translations are as easy as asking ChatGPT, and Mistral literally just released a top-of-the-line OCR model just last week. Mistral's model is special in that it is supposed to be able to handle complicated documents with multiple columns and annotations, which is exactly what I need.

Why do I need OCR? Well, sadly, in addition to not being able to find an English translation, I also couldn't immediately find a French transcription. Thankfully, there are a couple of high quality scans, notably [this one](https://cudl.lib.cam.ac.uk/view/PR-MONTAIGNE-00001-00007-00022/7) from The Cambridge University Library.

<div class="grid-container grid-2x2">
    <div class="image-div">
        <img src="bleed_through.webp" alt="">
    </div>
    <div class="image-div">
        <img src="no_bleedthrough.webp" alt="">
    </div>
    <div class="caption">1561, with bleed through, https://www.digitale-sammlungen.de/en/view/bsb10163169?page=,1</div>
    <div class="caption">1572, less bleed through, https://cudl.lib.cam.ac.uk/view/PR-MONTAIGNE-00001-00007-00022/7</div>
</div>


You might notice that I have *not* linked the first edition. This is because all the first editions I've currently found have obvious bleed through from the other side of the page, which I was worried would hurt the OCR. 

So, the plan is:
1. Download all the images from the Cambridge University Library
2. Crop out the bad parts of the page and compress
3. OCR the text
4. Have an LLM fix any mistakes
5. Haven an LLM translate the text


## Downloading the Images
Downloading the images is hardly worth mentioning. This is the sort of task that in the olden days would have taken a grueling hour by hand, or maybe 30 minutes if you could write a script to do it. But in today's world, you can just ask an LLM, and you'll have the code faster than it took you to type the prompt.

```
i want a python script that downloads the images from an increasing sequende from 22 to 182

https://images.lib.cam.ac.uk//content/images/PR-MONTAIGNE-00001-00007-00022-000-00022.jpg
https://images.lib.cam.ac.uk//content/images/PR-MONTAIGNE-00001-00007-00022-000-00182.jpg
```
And just like that, we have some [downloading code](https://github.com/CarsonDavis/ocr_translation/blob/main/utils/downloader.py).

## Cropping and Compression
With the downloads finished and in a folder, you'd think it's time for OCR. However, each of the original page scans was a 2mb JPG with extra black text at the bottom and a quarter of the adjoining page either to the left or right. It's possible that I could have written some code to automatically crop out the bad parts of the page, but I didn't feel up to the task, so I put 10 images at a time into Affinity Design before cropping and compressing them.

I'm converting the original JPGs to 80% webp, which, after the crop, typically results in files over 10 times smaller with no loss in quality. Here is a comparison of the original and cropped images:

<div class="grid-container grid-2x2">
    <div class="image-div">
        <img src="00026_original.webp" alt="">
    </div>
    <div class="image-div">
        <img src="00026.webp" alt="">
    </div>
    <div class="caption">original image</div>
    <div class="caption">cropped</div>
</div>


## CODING!
Now for the rest of this, I finally wrote some code. Why? Well, there is no world where I want to be pasting hundreds of images and prompts into ChatGPT by hand and laboriously combining the results. God forbid I get halfway done and realize there was a better prompt I could have used. Or if next week a new model is released that I want to try.

So anyway, I wrote a little CLI in 4 parts: OCR, LLM Correction, LLM Translation, and one to run the full process. It's not the most elegant code I've ever written, but it works. Importantly, it lets me test out different prompts and models easily, and should allow me to easily add new models as they are released. 

If I end up frequently translating old documents, then I'll add a couple features, mainly: parallelization, pre-run cost estimation, and a general tightening up of the repository...but for now it's in a workable state.

I want this post to be focused more on an analysis of the results than the code itself, so if you'd like to take a look at the code or use it on your own projects, you can find it on [my github](https://github.com/CarsonDavis/ocr_translation). 

### OCR
OCR is the most important, and sadly the most difficult, part of the process. As impressive as Mistral is, cramped, 16th century French annotations are its downfall.

As far as I can tell there are several issues:
- separate column for annotations
- flowery typeface with ligatures
- the long s
- abbreviations
- floating annotation letters
- antiquated spellings

Take a look at this example where I've highlighted some potential difficulties

![annotation_information_ct.webp](annotation_information_ct.webp)
_I think that may be a [ct ligature](https://commons.wikimedia.org/wiki/File:Latin_ligatures_ct_and_st.svg) in the word fruit...although last time I checked there is no 'c' in fruit. Perhaps a typesetting error by the printer?_

To further beat a dead horse, let's take a look at that last paragraph. Notice the long s, the abbreviation for "et", the floating "b", the archaic spellings of "maſles" and "meſmes", the random ligatures, etc.

**Transcription:**  
*Auſsi quād les femmes sont nées, pour la meſme raiſon de leur foiblesſe & debilité, croiſſent & enuielilliſſent pluſtoſt que les maſles a. Dōt faut attribuer cela à la nature qui rend les femmes pluſtoſt aptes à engendrer, comme eſtāt plus freſles, & pluſtoſt creuës, & enuielillies b. à l’exemple de tout fruiſt, lequel de tā plus eſt petit & menu, de tant ſe meuriſt plus promptement, & avec plus grande celerité.*

---

**Modernized:**  
*Aussi, quand les femmes sont nées, pour la même raison de leur faiblesse et débilité, croissent et vieillissent plus tôt que les mâles a. Dont faut attribuer cela à la nature qui rend les femmes plutôt aptes à engendrer, comme étant plus frêles, et plutôt crevées, et vieillies b. à l’exemple de tout fruit, lequel de tant plus est petit et menu, de tant se mûrit plus promptement, et avec plus grande célérité.*

---

**English:**  
*Thus, when women are born, for the same reason of their weakness and frailty, they grow and age sooner than males a. This must be attributed to nature, which makes women more apt to procreate, as they are more delicate, and rather burst, and aged b. following the example of all fruit, which, the smaller and finer it is, the faster it ripens, and with greater speed.*

---

Suffice to say that both 16th century printing and 16th century ideas of gender and biology are a bit of a headache.

## LLM Fixing
I had this idea that instead of jumping straight from the OCR to the translation, I could instead let the LLM take a pass at fixing any mistakes in the OCR. Essentially I could give it a little bit of context that this was a 16th century French legal text with annotations and hope for the best...something like:

```
You will be given an OCR-generated transcription of the 16th-century French legal text **"Arrest mémorable du Parlement de Tolose"** by Jean de Coras, a detailed account of the Martin Guerre impostor case. This OCR transcription contains transcription errors such as incorrect character recognition, misplaced punctuation, and spacing mistakes.
**Your task is to:**

1. **Correct all transcription errors**, ensuring accuracy in spelling, punctuation, capitalization, and spacing.
2. **Preserve the original 16th-century French style and vocabulary**, maintaining archaic language and legal terms as faithfully as possible.
3. **Pay particular attention to annotations**, which often contain classical references (e.g., Homer, Virgil, Cicero, and biblical passages), ensuring these are accurately transcribed and coherent in the context of the overall narrative.
4. Note that the annotations are often referenced through out the text with single letters. These single letters are not mistakes if they line up with an annotation.
5. **Retain original formatting** (such as headings, numbered annotations, and paragraph structure) wherever possible.
6. Respond with absolutely nothing except the edited text. Do not make any comments.
```

![page_26_corrections.webp](page_26_corrections.webp)

What I've done here is put the original transcription on the left and the "corrected" transcription on the right. When a word or letter is highlighted in darker green or red, that means it was changed between versions.

So, on the page that we've been looking at so far, there are very few corrections. Mostly some small spacing changes and the occasional switch from the long s to the modern s.

![page_30_corrections.webp](page_30_corrections.webp)
However, page 30 is absolutely covered in changes. 

Right off the bat we see the troubling conversion of  `\& dim. pudëce:non gucres` to `et dissimulation de pudeur`. I can see where the LLM is coming from, but if you reference the [original page](https://made-by-carson-images.s3.us-east-1.amazonaws.com/troublesome-translations/00030.webp), what it really seems to say is `et d'impudece: non gueres`. However, scanning through the rest of the corrections, most of them hold up pretty well. 

So... *To Correct or Not to Correct?*

With this evidence, I'm not sure. If I get a bit of time, I'll pick maybe 3 sample pages and transcribe them fully by hand myself. Then I can test out a bunch of different OCR and correction pairings to see which have the greatest deviation from my hand transcription.


## Final Translations
The final translations are, at best, ok. The main text is typically very good, but the highly abbreviated and often truncated annotations are a bit of a mess. Thankfully, whenever an annotation is particularly long, as in page 30 above, the printer has placed it in the main body of the page. 

If you'd like to read the full translation, you can find it here.

![return_engraving.jpg](return_engraving.jpg)
_Engraving from 1871 in 'Histoire Des Cocus Celebres' by Henry de Kock_

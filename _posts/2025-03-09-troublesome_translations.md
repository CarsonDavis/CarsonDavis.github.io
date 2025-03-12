---
title: Troublesome Translations
date: 2025-03-10
last_modified_at: 2025-03-11
categories: [coding, ocr]
tags: []
description: Attempting to translate a 16th-century French text with OCR
media_subpath: /troublesome-translations/
image: 20250219_212247.webp
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

## Background
### Martin Guerre
In 1548, Martin Guerre mysteriously disappeared from his village of Artigat in southwestern France, leaving behind his wife Bertrande and a young son. Eight years later, he finally returned, greeting everyone by name, reminiscing about old times, and getting back into the good graces of his wife and sisters.

Perhaps of the villagers occasionally thought that something was off about the long-lost Martin, but he was generally accepted back into village life, and over the next three years had two children with his beautiful wife, of which one survived. He did business around the village and it seemed like he might be on track to make him and Bertrande wealthy.

But then he claimed his inheritance rights from his uncle Pierre Guerre, and his world began to disintegrate. Pierre started telling anyone who would listen that Martin was in fact an imposter. The following years were full of lies, murder plots, imprisonments of all the involved parties, and a dramatic ending.

One of the judges who ruled over the subsequent court cases was so moved that in 1561 he wrote a book on the events, and the rest is history.

### Arrest Mémorable
I discovered this fabulous story when I read Natalie Davis's 1983 <i>The Return of Martin Guerre</i>. She became obsessed with the story, and deeply researched everything she could, from the original writings about the court case to the land grants and small claims records in the surrounding towns. Her book is a short and excellent read, though I would recommend skipping the introduction, as it gives away the ending. 

But like I said, it's short, and it left me wanting to dig more into the details of the case. Thankfully the judge Jean de Coras wrote an entire book on it in 1561, full of interesting commentary and annotations. As a fascinating historical note, the Judge Jean de Coras was murdered during the Saint Bartholomew's Day Massacre 11 years later, along with as many as 30,000 other protestants by French Catholics.

So off I went to find an english version...and nothing. There is no modern english printing, and there is no historic english translation, there is nothing.

I looked and looked, and finally I found something in an old journal, <i>Translation of the main text of Coras, Arrest Memorable, by Jeannette K Ringold, in Triquarterly 55 (Fall 1982): 86-103.</i> You may have noticed the caveat in the title, the all important word "main". Sadly the article only translates the main text, and not the annotations, which was the part I was most looking forward to. In fact, the translation is 13.5 pages long, while the original book is 160.

That number exaggerates the loss a little, since one must make allowances for the fact that 1500s books simply didn't cram all that many words on to a page, but suffice to say, I was disappointed.

If I wanted to read the annotations, I would have to translate them myself. And so I set out to do just that.

## The Plan
If we are being perfectly honest, I may have just let this drop after finding the main text translation. After all, I don't even speak French. But this is actually the <i>third</i> time this has happened to me in as many months, and I had begun to get fed up. I've got two other annotated 1600s books on my shelves that I also haven't found any translation for. 

Thankfully we live in a remarkable age. Translations are as easy as asking ChatGPT, and Mistral literally just released a top of the line OCR model just last week. Mistral's model is special, in that it is supposed to be able to handle complicated documents with multiple columns and annotations, which is exactly what I need.

Why do I need OCR? Well, sadly, in addition to not being able to find an english translation, I also couldn't immediately find a French transcription. Although thankfully, there are a couple of high quality scans, notable [this one](https://cudl.lib.cam.ac.uk/view/PR-MONTAIGNE-00001-00007-00022/7) from The Cambridge University Library.

You might note that this is not the first edition, but all the first editions I've currently found have obvious bleed through from the other side of the page, which I was worried would hurt the OCR. 

So the plan is thus:
1. Download all the images from the Cambridge University Library
2. Crop out the bad parts of the page and compress
3. OCR the text
4. Have an LLM fix any mistakes
5. Haven an Llm translate the text

### Downloading the Images
Downloading the images is hardly worth mentioning. This is the sort of task that would have taken an easy hour by hand, or 30 minutes to write code for yourself. But in today's world, you can just ask an LLM to do it and you'll have the code faster than it took you to type the prompt.

```
i want a python script that downloads the images from an increasing sequende from 22 to 182

https://images.lib.cam.ac.uk//content/images/PR-MONTAIGNE-00001-00007-00022-000-00022.jpg
https://images.lib.cam.ac.uk//content/images/PR-MONTAIGNE-00001-00007-00022-000-00182.jpg
```

### Cropping and Compression
Each of the original page scans was a 2mb jpg with extra black text at the bottom and a quarter of the adjoining page either to the left or right. It's possible that I could have written some code to automatically crop out the bad parts of the page, but I didn't feel up to the task, so I put 10 images at a time into affinity design and cropped and compressed them.

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

### CODING!
Now for the rest of this, I did write a bit of code. Why? Well, there is no world where I want to be pasting hundreds of images and prompts into ChatGPT by hand and laboriously combining the results. God forbid I get halfway done and realize there was a better prompt I could have used. Or if next week a new model is released that I want to try.

So anyway, I wrote a little CLI in 4 parts: OCR, LLM Correction, LLM Translation, and one to run the full process. It's not the most elegant code I've ever written, but it works. Importantly, it lets me test out different prompts and models easily, and should allow me to easily add new models as they are released. If I end up frequently translating old documents, then I'll add a couple features, mainly: parallelization, pre-run cost estimation, and a general tightening up of the repository...but for now it's in a workable state.

I want this post to be focused more on an analysis of the results than the code itself, so if you'd like to take a look at the code or use it on your own projects, you can find it on my github here: https://github.com/CarsonDavis/ocr_translation. 

### OCR
OCR is the most important, and sadly the most difficult, part of the process. As impressive as Mistral is, cramped, 16th century French annotations are its downfall.

As far as I can tell there are several issues:
- flowery typeface
- abreviations
- floating letters






## Notes
then i open each one in affinity design and manually crop out the bad parts of the page, and save them as 80% webp, which typically give 100x smaller files (give total directory size comparison)

then i do the ocr

now, i needed to write a bit of a wrapper for the ocr api, because it wants to do a couple of things with images in the scans that i don't want.

so, the ocr tends to have some small mistakes. for instance, whenever there are fancy capitals, it reads them as an image, so `Au` becomes just `v`. This could cause issues in translation, so the first step is to let the llm fix any mistakes.

I tried both 4o mini and 4o for this, and mini didn't even realize mistakes were there, while 4o did a pretty good job.

In the translations stage, 4o also gave subjectively better translations.


## Cleaning Comparisons

### Original OCR
```
Glefe euló fomme $x x \cdot q$. t. Jean-André de defponfimo pub.rous alle. guans S. Gra. goire en fes dialogues.
b. S.Hiero- me en vne de fes epiftires $a$ dreffec adVit. talem.
$i$. Alberique. en fon diction naire, fur la diction dctu trimoniis 2. 2. 10. And. $\mathcal{G}$ Panor. ${ }^{2}$ a $e$ fint, ce font des exēples beaux, certes, \& memorables: $d u x$, cōf. 100. $a n z$ Decrer. $l$ Aa lius. des Rois cxis. de au a.cbat, $m$ 3. Hierome efcriuane ad Vitalem, $n$ e. cum age folica, de us aux Decretal. c. 99.40 . $e$ ego folis, en la diffinition ix du Decrei. c. ftatuiimus. Farage. dernier lxi. diftinition. ditintion. 9 Platon aus 6. liure de fo. Republique,
```

### Simple Prompt
#### Prompt
CLEANING_USER_PROMPT = (
    "I created the following French 1500s text with OCR, and it might have missed "
    "some characters or made minor mistakes. Correct anything you see wrong, and "
    "respond with only the corrected information. Maintain the markdown formatting "
    "of the original. The context here is that it is a "
)

#### Result
```
Glose sur la somme $x x \cdot q$. t. Jean-André de desponsimo pub.rous alléguant S. Grégoire en ses dialogues.
b. S. Jérôme en une de ses épîtres $a$ dressée ad Vitalem.
$i$. Albérique en son dictionnaire, sur la diction de matrimonii 2. 2. 10. And. $\mathcal{G}$ Panor. ${ }^{2}$ à $e$ fin, ce sont des exemples beaux, certes, \& mémorables : $d u x$, conf. 100. $a n z$ Decret. $l$ Alius, des Rois cxis. de au achat, $m$ 3. Jérôme écrivant ad Vitalem, $n$ e. cum age solica, deus aux Décrétales. c. 99.40. $e$ ego solis, en la définition ix du Décret. c. statuimus. Parage dernier lxi. distinction. 9 Platon au 6. livre de sa République,
```

### Context Prompt
#### Prompt
CLEANING_USER_PROMPT = """You will be given an OCR-generated transcription of the 16th-century French legal text **"Arrest mémorable du Parlement de Tolose"** by Jean de Coras, a detailed account of the Martin Guerre impostor case. This OCR transcription contains transcription errors such as incorrect character recognition, misplaced punctuation, and spacing mistakes.
**Your task is to:**

1. **Correct all transcription errors**, ensuring accuracy in spelling, punctuation, capitalization, and spacing.
2. **Preserve the original 16th-century French style and vocabulary**, maintaining archaic language and legal terms as faithfully as possible.
3. **Pay particular attention to annotations**, which often contain classical references (e.g., Homer, Virgil, Cicero, and biblical passages), ensuring these are accurately transcribed and coherent in the context of the overall narrative.
4. **Retain original formatting** (such as headings, numbered annotations, and paragraph structure) wherever possible.

Begin now.
"""

#### Result
```
Glose sur la somme $x x \cdot q$: t. Jean-André de desponsationibus publiés aux allégations S. Grégoire en ses dialogues.
b. S. Jérôme en une de ses épîtres $a$ adressée à Vitalem.
$i$. Albericus en son dictionnaire, sur la diction matrimonii 2. 2. 10. And. $\mathcal{G}$ Panor. ${ }^{2}$ a $e$ fin, ce sont des exemples beaux, certes, \& mémorables : $d u x$, conf. 100. $a n z$ Décrét. $l$ Aalius. des Rois exis. de au a. chat, $m$ 3. Jérôme écrivant à Vitalem, $n$ e. cum age solica, de us aux Décrétales. c. 99.40 . $e$ ego solis, en la définition ix du Décret. c. statuiimus. Paragraph. dernier lxi. distinction. ditinction. 9 Platon au 6. livre de sa République.
```



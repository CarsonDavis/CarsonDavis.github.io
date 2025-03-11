---
title: Troublesome Translations
date: 2025-03-10
last_modified_at: 2025-03-10
categories: [coding, ocr]
tags: []
description: Attempting to translate a 16th-century French text with OCR
media_subpath: /troublesome-translations/
image: 20250219_212247.webp
published: False
---

## Background
### Martin Guerre
In 1548, Martin Guerre mysteriously disappeared from his village of Artigat in southwestern France, leaving behind his wife Bertrande and a young son. Eight years later, he finally returned, greeting everyone by name, reminiscing about old times, and getting back into the good graces of his wife and sisters.

Perhaps of the villagers occasionally thought that something was off about the long-lost Martin, but he was generally accepted back into village life, and over the next three years had two children with his beautiful wife, of which one survived. He did business around the village and it seemed like he might be on track to make him and Bertrande wealthy.

But then he claimed his inheritance rights from his uncle Pierre Guerre, and his world began to disintegrate. Pierre started telling anyone who would listen that Martin was in fact an imposter. The following years were full of lies, murder plots, imprisonments of all the involved parties, and a dramatic ending.

One of the judges who ruled over the subsequent court cases was so moved that in 1561 he wrote a book on the events, and the rest is history.

### Arrest Mémorable
I discovered this fabulous story when I read Natalie Davis's 198? <i>The Return of Martin Guerre</i>. She became obsessed with the story, and deeply researched everything she could, from the original writings about the court case to the land grants and small claims records in the surrounding towns. Her book is a short and excellent read, though I would recommend skipping the introduction, as it gives away the ending. 

But like I said, it's short, and it left me wanting to dig more into the details of the case. Thankfully the judge Jean de Coras wrote an entire book on it in 156?, full of interesting commentary and annotations.

So off I went to find an english version...and nothing. There is no modern english printing, and there is no historic english translation, there is nothing.

I looked and looked, and finally I found something in an old journal, <i>Translation of the main text of Coras, Arrest Memorable, by Jeannette K Ringold, in Triquarterly 55 (Fall 1982): 86-103.</i> You may have noticed the caveat in the title, the all important word "main". Sadly the article only translates the main text, and not the annotations, which was the part I was most looking forward to. In fact, the translation is 13.5 pages long, while the original book is 160.

That number exaggerates the loss a little, since one must make allowances for the fact that 1500s books simply didn't cram all that many words on to a page, but suffice to say, I was disappointed.

If I wanted to read the annotations, I would have to translate them myself. And so I set out to do just that.

## The Plan
If we are being perfectly honest, I may have just let this drop after finding the main text translation. But this is actually the <i>third</i> time this has happened to me in as many months, and I had begun to get fed up. 

Thankfully we live in a remarkable age. Translations are as easy as asking ChatGPT and Mistral literally released a top of the line OCR model just last week. Mistral's model is special, in that it is supposed to be able to handle complicated documents with multiple columns and annotations, which is exactly what I need.

Sadly, in addition to not being able to find an english translation, I also couldn't immediately find a french transcription. Thankfully, there are a couple of high quality scans, notable [this one](https://cudl.lib.cam.ac.uk/view/PR-MONTAIGNE-00001-00007-00022/7) from The Cambridge University Library.



Several of the other scans I found had pretty major bleed through from the other side of the page, which I was worried would hurt the OCR. 

So first i download all of the images using a script that iterates through the numbers

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



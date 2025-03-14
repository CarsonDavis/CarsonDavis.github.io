---
title: "Manus AI: First Look"
date: 2025-03-13
last_modified_at: 2025-03-13
categories: [ai, manus]
tags: []
description: An initial exploration into Manus AI's capabilities
media_subpath: /manus-review/
image: 5a8697cc-d232-4ea7-84e2-d57fddc5a69a.webp
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

> This is an ongoing post that will continue to receive updates as my usage quota is refreshed.
{: .prompt-danger }

## Overview
Manus promises to be a general AI agent that can do your work while you relax. Check out their full pitch on the [Manus website](https://manus.im/). Essentially it takes your prompt, makes a todo list for itself, and then begins an agentic workflow -- searching the web, executing actions, writing documents, and anything else it needs to complete your task.

In theory, it sounds absolutely awesome.

## Caveats
So far, I've had it for exactly one day and was able to use it for two personal projects before meeting my quota. I'm writing this post so soon because I have several friends and coworkers on the wait list who want to know my initial impressions. 

So, this is NOT a comprehensive review based on extensive usage. I've had to live within their quota system and will update this post as I continue to use it.

I also only have limited experience with OpenAI's $200/month competitor model, so I won't be comparing the two. 

With that out of the way, let's get into the projects I've used Manus for so far.

## Camera Research Project
### Overview
I'm a big film photography nerd, and recently I've been trying to make a long post that documents some of my old film cameras. Sadly, it's taking forever, because in addition to covering my personal experience shooting each camera, I would also like to write intelligently about their historical context.

So for each camera, I spend hours reading articles, watching videos, and using LLMs to do general research and find additional source material. 

### The Prompt

```
ok, i want you to research the historical context of the leica iii c. what years it was manufactured, what was the price, who was the market, what was the critical reception, etc
```

Over the past two weeks of camera research, I've done similar prompts on OpenAI's 4o, 4.5, o1, o3-mini-high, DeepSeek's R1, and Claude's 3.7 with extended thinking, both with and without search enabled. 

So, I've got a good idea of how much detail and factual accuracy I can expect from each model. In general, these modern models do an acceptable job, especially when they are also able to search the web. However, I typically still need to actually read a bunch of source material to get the full picture.

### Results
Manus makes some big promises, so my hope is that it will slash my research time by finding the sources for me and synthesizing the information into a coherent report. Manus offers a replay feature, so you can directly view [the results](https://manus.im/share/nIOC4el3795v8dzWaCGDuk?replay=1). Visit the link and take a look at the results it compiled.

It did, in fact, generate a massive report detailing the Origins and Development, the Manufacturing, the Price History, the Target Market, the Critical Reception, the User Experience and Ergonomics, the Historical Significance and Cultural Impact, and Legacy and Continuing Relevance of the Leica iii a.

To put it briefly, it wildly outperformed everything else I've tried. 

I will say that there was one definite factual error in the report; the serial number information is incorrect. It pulled the number from [this table](https://www.cameraquest.com/ltmnum.htm), which to be fair, has probably confused its fair share of humans as well.

Overall, I'm very pleased with this specific research use case. It's the best LLM I've used for this task. For subjects which are reasonably well-documented online, Manus seems to be a big help in the initial research phase.

So let's try something harder.

## 16th Century Document Research
### Background
I've recently been a little obsessed with the 1560 legal case of Martin Guerre, and I've been trying to read the original source material. Despite there being several modern books and movies on the case, I couldn't find a full transcription or translation of the original *Arrest mémorable* by judge Jean de Coras that included the judge's annotations.

However, I'm on vacation right now, and Mistral just released a new "[document understanding API](https://mistral.ai/news/mistral-ocr)" which is supposed to have excellent OCR capabilities...so I figured I could have a bit of fun transcribing and translating the document myself.

I've made an [initial post](https://madebycarson.com/posts/troublesome_translations/) about my project if you'd like to see what I did, and read a little bit about why this case is so interesting.

However, I've had this nagging suspicion that maybe I just didn't look hard enough and there really were existing transcriptions or translations out there. So I decided to ask Manus to do some research for me.

### The Prompt
```
I'm researching the Arrest mémorable du Parlement de Tolose by Jean de Coras. I'd like you to find 3 things. First, a list of all the unique scans of the original book. Second, a french transcription of the book that includes the annotations. And finally, an english language translation of the full book, specifically one that includes the annotations. 
```

Basically, in this prompt I'm looking for three things:
1. Scans of the original book
2. A French transcription of the book
3. An English translation of the book

### Results
As before, you can watch a video of the results [here](https://manus.im/share/Hi7E3I27BigTKJf5V9gAyA?replay=1). Also like before, it compiled a really nice document with links, context, and summaries of the results. But let's look at exactly what it found.

**Scans**

Although it did technically find scans, I was not impressed. Two of the 4 scans it found are not actually scans of the original. And worse, the scans it found are a bit mediocre; it's missing both of the higher quality scans that I used in my own project. 

**Transcriptions**

Another failure. Sadly, it just listed some more scans, and the not textual transcriptions I wanted.

This may be due to the inherent ambiguity between a scan and transcription, so I followed up with the agent with a clarification, and it was able to reevaluate the results to conclude that no French transcriptions exist.

**Translations**

Here, it correctly identifies that there are no translations of the full work, while providing the partial translations that exist.

### Final Thoughts the Marin Guerre Research
I knew this would be a hard research task for it, since it was hard task for me. Whereas there is an ungodly wealth of information on the internet about the Leica iii camera, there is so little about the *Arrest mémorable du Parlement de Tolose* that I wrote a whole code library just to transcribe and translate it.

So, what was the point of this research task then?

Well, I've looked at this subject in some depth, and I know what kinds of sources are easily available on the internet. So as a benchmark, I wanted to see if Manus could find something I missed. It did not. In fact, it did far worse.

If I had used Manus exclusively instead of researching myself, I would have missed several important source documents, and would have had a significantly harder time with my OCR.

To its credit, it does make really nice reports with lots of detail, but for this use case I simply am not able to trust it to be comprehensive.

## Notes on Usability
So, other than specific projects, what is Manus like to use?

As an interface, it is wonderfully usable. Nothing is hard to figure out, and all the features are right where you expect them. At no point did I find myself hunting for the right button or wondering if I was going to lose my work.

It's got lots of nice little features, like you can interrupt the research mid task and it will change it's objective. You can also jump into it's computer and interact with it if you see it struggling (at one point I solved a captcha to let it into a site).

## Future Investigations
Sadly, this is all I can report for now, as I have reached my daily quota

As my quota refreshes, there are a few things I would like to try:
- interrupting the workflow to update its todo list or other documents
- action-based tasks, such as 'transcribe and translate the first 10 pages of Arrest mémorable', instead of just having it do research

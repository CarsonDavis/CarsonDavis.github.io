---
title: Lens Equivalence for the Unhinged Camera Collector
date: 2026-01-19
last_modified_at: 2026-01-19
categories: [photography, tools]
tags: []
media_subpath: /lens-calculator/
description: A calculator for comparing lenses across formats, built by someone with 120 cameras and zero web dev skills.
image: calculator-hero.webp
published: False
---

## The Myth

People on the internet will tell you that the Pentax 67 with a 105mm f/2.4 has some mystical quality that cannot be replicated on 35mm. They'll rave about "3D pop" and "medium format compression" and how the bokeh is somehow *more* than what you get on a smaller format. They will positively froth at the mouth while declaring that the look is impossible to achieve without shooting 6x7.

And look, it's a nice lens. I own one. I've shot many rolls through it.

But it's a 50mm f/1.2 equivalent on full frame. That's it. That's the whole secret.

The "compression" people attribute to medium format? That's not caused by the format or the focal length—it's caused by the distance between you and your subject. Since the 105mm on 6x7 frames the same as a 50mm on 35mm, you're standing at the same distance, which means the compression is identical. There is no magical medium format compression. There is no 3D pop that exists only on larger sensors. There is only math.

I got tired of explaining this at camera meetups, so I built a calculator.

## What It Does

**Live app:** [lens-calc.codebycarson.com](https://lens-calc.codebycarson.com/)

You tell it what you're shooting—format, focal length, aperture, subject distance—and it tells you exactly what you'd need on another format to get the same image. Not just the same framing, but the same depth of field and the same background blur.

![Calculator showing full frame 50mm f/1.4 compared to APS-C equivalent](calculator-ff-to-apsc.webp)
_Full frame 50mm f/1.4 → APS-C: you'd need a 33mm f/0.9 to match. Good luck finding that lens._

It computes:

- **Equivalent focal length** — same field of view
- **Equivalent aperture** — same depth of field and background blur
- **Depth of field** — the near and far limits of acceptable sharpness
- **Blur disc size** — how blurry the background actually gets

Most crop factor calculators only do the first one. They'll tell you a 50mm on APS-C "acts like" a 75mm on full frame, which is true for framing but tells you nothing about depth of field. And depth of field is the whole reason people buy fast lenses.

## Why I Needed This

I have an unhealthy number of cameras. Around 120 at last count, though I've lost track. And when you're constantly switching between formats—35mm one day, 6x7 the next, maybe some 6x6 on the weekend—you start to lose your intuition for what a given lens will actually *do*.

My Nikon FM2 with the 50mm f/1.4 is my desert island setup. It's the benchmark by which I judge everything else. But what if I want that same look on my Pentax 67? The calculator says I'd need roughly a 105mm at f/2.9. Not f/2.4, which is what the famous lens shoots wide open—that would actually give me *shallower* depth of field than my 35mm setup.

Or take my landscape kit. On the Pentax 67, I use the 45mm f/4, which I maintain is the sharpest lens I own. Incredible detail. But what's the 35mm equivalent? Turns out it's roughly a 21mm f/1.9—a lens that basically doesn't exist. The combination of that ultra-wide angle with that depth of field simply isn't available on smaller formats without focus stacking.

And then there's my Voigtländer Prominent. Gorgeous camera. 50mm f/1.5 Nokton lens. I desperately want to shoot it wide open in daylight, but the maximum shutter speed is 1/500s. Having a calculator that tells me "f/1.5 on a sunny day needs 1/4000s minimum" would have saved me several ruined rolls. (The calculator doesn't do exposure yet, but a man can dream.)

![Calculator showing 35mm to 6x7 comparison](calculator-35mm-to-67.webp)
_35mm 50mm f/1.4 → Pentax 67: the "equivalent" is 105mm f/2.9, not the famous f/2.4_

The Yashica D is another interesting case. It's a 6x6 TLR with an 80mm f/3.5 taking lens. What's that equivalent to on 35mm? About a 44mm f/1.9. So my cheap Yashica, which I bought for $276 in 2017, gives me roughly the same look as a Voigtländer 40mm f/1.2 that costs $1,100 today. The Yashica is heavier and slower to operate, sure, but the rendering is equivalent.

Understanding this stuff doesn't make medium format pointless—the bigger negatives still have more detail and less grain, and that matters. But it does let you make informed decisions instead of chasing myths.

## How I Built It

I have 120 film cameras and approximately zero web development skills. My day job involves Python and data pipelines, not React components. So I did what any reasonable person would do in 2025: I mass-delegated to [Claude Code](https://claude.ai/claude-code).

But here's the thing—I didn't just tell Claude "build me a lens calculator" and hope for the best. That's how you get vibe-coded garbage that looks impressive for five minutes and then falls apart when you actually try to use it.

Instead, I spent about 5 hours on upfront documentation and research before writing a single line of code. I had Claude scrape Wikipedia for the actual depth of field and circle of confusion equations. I had it research modern web development best practices. I wrote detailed requirements documents, architecture questionnaires, design system specs. By the time I said "okay, now build it," there was a 50-page paper trail of exactly what I wanted.

The implementation took about 2.5 hours.

My thesis: if the code is bad, that's not Claude's fault. It means the documentation or the context engineering was bad. As of early 2025, the limiting factor on AI-assisted coding is not the AI's ability to write code—it's your ability to specify what you want.

I call this the "no-writing approach." I didn't write the documentation myself either; I co-created it through conversation, asking questions, requesting research, iterating on drafts. The only thing I occasionally touched up was a requirements doc here or there, and anything beyond a few lines meant my original prompting was flawed.

If you want to see exactly how this worked, I documented the entire process: [how-i-built-this.md](https://github.com/CarsonDavis/lens-calculator/blob/main/how-i-built-this.md). Every phase, every chat log, every artifact. It's the closest thing I have to a tutorial on AI-assisted development that actually produces production-quality code.

## The Math

I'm not going to deep-dive into the equations here—you can read the [research docs](https://github.com/CarsonDavis/lens-calculator/tree/main/research/lens-equations) if you want the gory details. But the high-level summary:

**Crop factor** is the ratio of sensor diagonals. Full frame is 43.3mm diagonal; APS-C is about 28.2mm; the Pentax 67 is about 91mm. Divide and you get your multiplier.

**Equivalent focal length** is just focal length times crop factor. A 50mm on APS-C has a crop factor of ~1.5, so it frames like a 75mm on full frame.

**Equivalent aperture** is the part most calculators skip. To get the same depth of field, you multiply the f-number by the crop factor too. So that 50mm f/1.8 on APS-C? It has the depth of field of a 75mm f/2.7 on full frame. You're not getting full-frame bokeh with a crop sensor and the same f-number—the physics don't work that way.

**Blur disc** is how big an out-of-focus point becomes on the final image. This is what actually determines how "blurry" your background looks. It depends on focal length, aperture, subject distance, and background distance. The calculator handles all of this.

The tricky part is handling formats with different aspect ratios. Do you match by diagonal, width, height, or area? The calculator defaults to diagonal (the most common convention) but lets you change it.

Think of this as the choil shot of lens calculators. If you've read my [kitchen knives post]({% link _posts/2024-02-14-kitchen_knives.md %}), you know that a choil shot—the cross-sectional view of a blade—tells you more about how a knife will perform than any marketing copy ever could. This calculator is the choil shot for lens comparisons. It shows you what actually matters instead of what sounds impressive.

## Try It

**[lens-calc.codebycarson.com](https://lens-calc.codebycarson.com/)**

Plug in your own cameras. See what your vintage 50mm f/2 actually translates to on modern APS-C. Figure out whether that medium format lens you're lusting after will actually give you anything your current kit can't.

And the next time someone tells you their Fuji GFX has "medium format compression" that 35mm could never achieve, you can smile politely and explain that their 50mm f/3.5 is basically a 40mm f/2.8 on full frame.

They'll love you for it.

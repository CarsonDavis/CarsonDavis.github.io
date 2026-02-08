---
title: "Claude Code...But Not For Coding"
date: 2026-02-07
last_modified_at: 2026-02-07
categories: [ai]
tags: []
description: How I used an AI agent to rescue a year of book notes from my phone.
image: calculator-hero.webp
published: false
---

## AI Is Insane and You Have No Idea

Basically anyone that has Claude Code installed already gets it. AI is incredible, it's terrifying, it's changing everything, and it's probably gonna take all our jobs. But sometimes it seems like my regular friends' only exposure to AI is the Google search overview telling them they should put glue on their pizza to keep the cheese from falling off...and honestly, I can't blame anyone for being unimpressed by that.

Here's the thing: whatever free chatbot you're using doesn't represent the state of the art. Not even close. All it does is talk to you (and immediately forgets what you said two messages ago). The future isn't chatbots. It's *agents* — AI that actually does things on your computer. If I thought the average reader would be impressed by coding examples, I'd point you at my portfolio of projects built 100% with Claude Code. But this post is about something more ordinary.

This post is for the haters. The people still asking ChatGPT questions in a browser and wondering what the fuss is about. My dad, my friends who roll their eyes when I bring this up at dinner, anyone who's heard the hype and thought *yeah, okay, sure*. This is not about programming. This is about a completely ordinary, non-technical life problem that I solved in an afternoon because we are, and I cannot stress this enough, living in the actual future.

I know I sound like an AI shill. Bear with me. By the end of this, you'll at least understand why I won't shut up about it.

## 365 Books, Zero Memory

I read a lot. Like, 365 books in the last three calendar years a lot. I'm always listening — cooking, driving, walking the dog. If I'm doing something with my hands and not my brain, there's a book playing.

Here's the cruel irony of being a voracious reader: the books you love most are the ones you remember least. You inhale a great novel in one afternoon and it's gone. Meanwhile, the boring one that took you two weeks to slog through? Burned into your long-term memory forever. Your brain is basically a graveyard of mediocre fiction.

I try to combat this by being deliberate about writing reviews after I finish a book. Sit down, collect my thoughts, put something on paper while it's still fresh. It genuinely helps — the act of writing a review cements a book in my memory in a way that just reading it doesn't.

The problem is that I'm rarely near a computer when the thoughts are happening. I'd be out on a walk, listening to a book, and a thought would hit me — a reaction to a character, a quote I liked, something I wanted to remember for a review. So I developed a hack: pull out my phone, open Signal, and voice-text a note to myself. Quick and easy. I'd come back later and write the proper review. And from 2023-2024 I was doing great.

Then as it does, life happened. Work got busy, I started a side business, I made a bunch of cool projects. What I did not do was write reviews. In 2025 I read 107 books. I failed to write reviews for 61 of them.

## Trapped

So at some point (yesterday) I decided it was finally time to deal with this. Thankfully I have all those lovely notes, I'll just type them up real quick, right? Hell no. You think I'm gonna type xx notes by hand in the age of AI?

Step one: get the messages off my phone and onto my computer. How hard could that be?

I'll just export them. Signal has a backup feature. Ha. I've been hoarding Signal messages for a decade, and my backup is so big it broke the Signal backup utility over a year ago. 

That's fine, I'll sync to desktop. Eh, that's a 68GB transfer, and Signal's "Note to Self" has known sync bugs. Direct database access? Requires root. The `adb backup` command? Signal explicitly blocks it. I tried half a dozen approaches. Every single one failed.

Two years ago, this is where the story ends. Sucks to suck, maybe get a better note-taking system. Have fun reading 453 messages off your phone screen and typing them into a document by hand.

## Enter Claude

Let me briefly explain what Claude Code is for the non-technical reader, because this is important context. It's not a chatbot. You don't ask it a question and get a response. It's an *agent* — it reads files, writes code, runs programs, and interacts with your computer. Think less "ask it a question" and more "give it a task and watch it work."

I explained the problem. Three messages later, my phone is plugged into my computer, and Claude is remotely scrolling through my Signal messages, reading each one off the screen, and saving them to a file.

Let that sink in. 453 messages across 96 screens, extracted in about three minutes. It handled scroll overlap, truncated messages, timestamps — all the fiddly edge cases that would have made this a nightmare to build by hand. Look, I write software for a living. If I'd tried to build this myself, it would have been a week-long project. But this is the future, and I described the problem in English, and Claude just...did it.

## The Magic: Matching Notes to Books

Now I had 453 messages on my computer. Some were book notes. Some were grocery lists. Some were drafts to friends I never sent. Most had no indication of which book they belonged to. Claude read through them all and flagged the obvious junk — five minutes of spot-checking on my end instead of hours of reading — and I was left with 427 actual book notes. But now I had a different problem: which notes went with which book?

This sounds straightforward until you remember that most of my notes have no book title. They're voice-texted fragments from someone who was half occupied caramelizing onions. Half of them could be about any of dozens of books. And I personally couldn't remember — the whole reason I was *taking* notes was because I forget everything.

I handed Claude two files: the cleaned messages and a Goodreads CSV export of every book I've read — 630 titles. "Figure out which notes go with which book."

Here's where it gets insane. Look at what Claude matched:

| My voice-texted note | The book |
|---|---|
| "Several really emotional moments, like when the black guy announces he'll go to the same school" | *Playground* by Richard Powers |
| "Amy burned her book of stories that she had been writing 43 years" | *Little Women* by Louisa May Alcott |
| "Freedom to leave as a motivator towards democracy" / "Political instability in Mexico" | *Why Nations Fail* by Daron Acemoglu |
| "his time with the little people is just super boring" | *The Time Machine* by H.G. Wells |

These aren't keyword matches. There's no algorithm that connects "the black guy announces he'll go to the same school" to a Pulitzer Prize-winning novel by Richard Powers. Claude *knows* that book. It knows the scene. It knows "little people" means the Eloi in *The Time Machine*. 

Final tally: 41 books matched, roughly 340 messages organized, near-100% accuracy. For the last few ambiguous groups, I just pointed out the neighboring books in my reading order and Claude narrowed them down.

A year ago, I tried to build something like this. A Python framework that wrapped an LLM, broke books into chapters, cross-referenced themes and characters. Days of work. Buggy as hell. Maybe 80% accurate when I was done. This time, it was one prompt, ten minutes of my time, and it just worked.

## The Point

Here's the thing I want you to take away from this: I didn't write code. I didn't program anything. I had a messy phone and a bad memory, and I described the problem in plain English. That's it.

Everyone who uses a computer has their version of this. A folder of unsorted photos. A spreadsheet that needs cleaning. A decade of receipts. A year of notes trapped on a phone. These are the problems AI can solve for *regular people*, right now, today. Not in some hypothetical future — right now.

Next up: I'm building a proper note-taking app so this never happens again. But that's a post for another day. For now, I have 365 books to review, and thanks to Claude, I actually remember what I thought about them.

Well. 41 of them, at least.

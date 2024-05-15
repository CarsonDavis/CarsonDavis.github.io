---
title: Various Variacs
date: 2018-06-13
categories: [electronics, variacs]
tags: [electronics, tools, multimeter, antiques, variacs]
media_subpath: /variacs/
description: I analyze the specs and capabilities of my variacs.
---

I've managed to gather a few variacs, including some about which I know very little. In this post I'll go over some of my findings.
![Kve7Pwl](Kve7Pwl.jpeg)
![8u6wINV](8u6wINV.jpeg)

Powerstat Type 1226, input 230/115V, output 0-270V, 2.5KVA

Powerstat Type 116-B, input 120V, output 0-140V, 1.4KVA, 10A

Powerstat Type 20, input 115V, output 0-135V, 3A

General Radio Company W2-S12-2, input ?, output ?, current ?

## Powerstat Type 1226 Analysis
So, I recently got this giagantic variac, and I don't really know the specs. Lets start by doing some tests. Please note that I originally discussed this over on the EEVBlog, and there are some additional details on this post https://www.eevblog.com/forum/beginners/230v-variac-wiring-question/. 

![5kRJtjZ](5kRJtjZ.jpeg)

Right is the input from the small variac. Left is the output. This holds true for the wires as well as the multimeters.

![K1VRvkt](K1VRvkt.jpeg)

So it seems that when connected to 115, you can double your voltage. But when connected to 230, you just get the input voltage.
I tried feeding the 115V input 120+ volts and the variac started making a weird humming sound, so I stopped.

![z8Pti4R](z8Pti4R.jpeg)

A clearer illustration of what is happening. Note that the output isn't exactly 1:1 and 1:2. 
It is actually 1:1.16 and 1:2.32

![oF5D3US](oF5D3US.png)

Possibly the correct wiring diagram for my unit. However, as noted before, the X-1226 does not have the same ratings, and so might not be the same.
[UPDATE:] Based on my tests, it would appear that this wiring is almost right, but not quite. if posts 2 and 4 were switched, it would appear to describe my unit.


![xsjlIF1](xsjlIF1.png)

Documentation for my exact unit is thin on the ground, however I was able to find documentation for the X-1226. It seems to be an explosion proof variant of my model. I have a friend with an explosion proof Powerstat, and one of the immediately noticeable differences is the contained plug housing. The O models are oil-cooled, and are definitely not similar.

This X-1226 seems to have a few noticeable spec differences 

120in 280out instead of 115in 270out.

1.7KVA instead of 2.5KVA

6A instead of my guess of of 9.25A

So far the assumption has been that the Output Current Rating = Rated KVA/Max Output Voltage.
For the X-1226 that would mean (1700/280=6.07A). So that equation seems to be working as expected.

For the moment, that means we can probably calculate my rating as (2500/270=9.25A).

![BIVoc2I](BIVoc2I.png)

Here is the listed derating curve for the Powerstat. From the previous chart, we know that the unit is rated at 1.7KVA with 240in 280out. But with 120in 280out it drops to 0.71KVA. That gives an expected output current of (710/280=2.54A). That 2.54A number seems to line up pretty perfectly with the 280V number on the derating curve.

So if we make a bit of a leap, and assume that my unit has an identically scaled curve but with different values, what is my derated number? ((710/1700)*2500)/270=3.87A max output at 270 volts and 115 volts input. 

However, as you can see from the curve, in the same wiring configuration I can input 115 and output up to what looks like 150V (135V for mine) at the full 9.25 A.

It is also interesting to note that Powerstat does not fuse their inputs. They are only fusing the output to the listed number.

![72iQVK2](72iQVK2.png)

So I ran a few tests on my Variac, monitoring input and output voltage and current, and then calculating the power and efficiency.

There is some weird stuff going on at the beginning where power isn't being conserved. I suspect that this is due to an effect called AC Power Factor. It has to do with phase shifts and magic when you start involving magnetism. 

I wasn't willing to output more than the 100V and 6.5A on my test load because I wasn't super confident in my wire ratings, etc. However the Efficiency seemed to stabilize at around 85%. I suspect that efficiency might change once the variac starts outputting higher than input voltages. If anyone knows a simple way to output 280V at around 3A, let me know.

So from this we can assume that if the variac is inputting 120 and outputting 120, the input current will be 10.5A while the output current is 9A. So apparently the bottleneck of the wire is not actually 9A. It is 10.5A but there are power losses on the output side of the coil.

![qDCUaKr](qDCUaKr.png)
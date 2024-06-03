---
title: Guilty Grandmas
date: 2024-06-01
last_modified_at: 2024-06-02
categories: [machine leaning, metrics]
tags: []
description: Understanding precision, recall, and accuracy.
media_subpath: /ml-metrics/
image: cropped_grandmas.jpg
math: True
published: True
---

<!-- > This is an unfinished post that will receive additional content and editing in the future. 
{: .prompt-danger } -->

## The Madness of Machine Learning Metrics
If you are interested in machine learning, then you've seen the words precision, accuracy, and recall. Maybe you've heard of True Negatives and False Positives, and perhaps some misguided soul has tried to explain everything with a picture of arrows on a bullseye, which unfortunately has no bearing on the ML definitions. 

It took me the longest time to fully internalize these concepts, and I think that was in large part because of how they were explained to me. I don't want you to suffer like I did, so let's break everything down. 

## Guilty Grandmas
I think the first hurdle is wrapping your head around these obscure terms. What the heck is a false negative anyway? Let's use a real example to find out.

Let's say you are Chad, the local district judge. And on your docket today, you have 10 naughty grandmas. Actually, half of them are guilty and the other half are innocent, but you don't know that. You're just the anthropomorphization of a machine learning algorithm designed for comedic illustration.

There are only 4 possible types of convictions you can make:

- <strong>True Positive</strong>: Send a guilty grandma to jail.
- <strong>False Positive</strong>: Send an innocent grandma to jail.
- <strong>True Negative</strong>: Let an innocent grandma free.
- <strong>False Negative</strong>: Let a guilty grandma free.

## The Metrics
How can we evaluate your success at convicting grandmas? Well, two metrics in particular are often used to understand how a machine learning model performs. And interestingly, they are often at odds with one another. As you are in the final stages of training your model, you might have to ask yourself, would I rather optimize for high precision, or high recall?

### Precision
Did you convict any innocent grandmas? 

Well, technically precision asks the reverse, 'what percent of jailed grandmas were guilty?' But the idea of convicting innocents is more memorable. If you want to actually calculate precision, you can use:

$$
\frac{\text{True Positives}}{\text{True Positives} + \text{False Positives}}
$$

or, to put it more simply:

$$
\frac{\text{Jailed Grandmas who were Guilty}}{\text{Jailed Grandmas}}
$$

### Recall
Did you put all the guilty grandmas in jail?

$$
\frac{\text{True Positives}}{\text{True Positives} + \text{False Negatives}}
$$

or

$$
\frac{\text{Jailed Grandmas who were Guilty}}{\text{Guilty Grandmas}} 
$$


## The Balancing Act
As we've seen, often you have to choose whether to optimize for precision or recall. Let's take this to extremes.

### High Precision, Low Recall
So what would it mean for a model to be ultra high precision, but low recall? 

Essentially, whenever you do send a grandma to jail you are always right, but you miss a lot of actually guilty grandmas in the process.

On mobile you may need to scroll the table to the left or right. TP is short for True Positive, FN for False Negative, etc. A green x is a correct judgement and a red x is incorrect.

<!-- ![img](Screenshot+2024-06-01+113941.png) -->


<style>
    table {
        width: 100%;
        border-collapse: collapse;
        text-align: center;
        margin: auto;
    }
    th, td {
        border: 1px solid #4a4849;
        padding: 10px;
        text-align: center;
    }
    thead tr {
        background-color: #2d2d2d;
        color: #d3d3d3;
    }
    .header-row {
        background-color: #e76f51;  
    }
    .row-dark {
        background-color: #333;
    }
    .row-light {
        background-color: #4d4d4d;
    }
    .guilty {
        color: #e76f51;
    }
    .innocent {
        color: #118ab2;
    }
    .jail {
        background-color: #e76f51;
        color: #2d2d2d;
    }
    .true {
        background-color: #3c732e;
    }
    .false {
        background-color: #8c1936;
    }
</style>

<!-- ![img](high-precision.png) -->

<div style="display: flex; justify-content: center;">
    <table>
        <thead style="border: .5px solid #bf2673;">
            <tr>
                <th style="border: .5px solid #4f4f4f;" class="row-dark">Grandmas</th>
                <th class="row-dark">Guilty?</th>
                <th class="row-dark">Jail</th>
                <th class="row-dark" style="line-height: 1.2; text-align: center; border-left: 3px solid #4a4849">TP</th>
                <th class="row-dark" style="line-height: 1.2; text-align: center;">TN</th>
                <th class="row-dark" style="line-height: 1.2; text-align: center;">FP</th>
                <th class="row-dark" style="line-height: 1.2; text-align: center;">FN</th>
            </tr>
        </thead>
        <tbody>
            <tr class="row-dark">
                <td>Edith</td>
                <td class="guilty">guilty</td>
                <td class="jail">yes</td>
                <td class="true" style="border-left: 3px solid #4a4849">x</td>
                <td></td>
                <td></td>
                <td></td>
            </tr>
            <tr class="row-light">
                <td>Mabel</td>
                <td class="guilty">guilty</td>
                <td></td>
                <td style="border-left: 3px solid #4a4849"></td>
                <td></td>
                <td></td>
                <td class="false">x</td>
            </tr>
            <tr class="row-dark">
                <td>Florence</td>
                <td class="guilty">guilty</td>
                <td></td>
                <td style="border-left: 3px solid #4a4849"></td>
                <td></td>
                <td></td>
                <td class="false">x</td>
            </tr>
            <tr class="row-light">
                <td>Eleanor</td>
                <td class="guilty">guilty</td>
                <td></td>
                <td style="border-left: 3px solid #4a4849"></td>
                <td></td>
                <td></td>
                <td class="false">x</td>
            </tr>
            <tr class="row-dark">
                <td>Beatrice</td>
                <td class="guilty">guilty</td>
                <td></td>
                <td style="border-left: 3px solid #4a4849"></td>
                <td></td>
                <td></td>
                <td class="false">x</td>
            </tr>
            <tr class="row-light">
                <td>Agnes</td>
                <td class="innocent">innocent</td>
                <td></td>
                <td style="border-left: 3px solid #4a4849"></td>
                <td class="true">x</td>
                <td></td>
                <td></td>
            </tr>
            <tr class="row-dark">
                <td>Mildred</td>
                <td class="innocent">innocent</td>
                <td></td>
                <td style="border-left: 3px solid #4a4849"></td>
                <td class="true">x</td>
                <td></td>
                <td></td>
            </tr>
            <tr class="row-light">
                <td>Gertrude</td>
                <td class="innocent">innocent</td>
                <td></td>
                <td style="border-left: 3px solid #4a4849"></td>
                <td class="true">x</td>
                <td></td>
                <td></td>
            </tr>
            <tr class="row-dark">
                <td>Dorothy</td>
                <td class="innocent">innocent</td>
                <td></td>
                <td style="border-left: 3px solid #4a4849"></td>
                <td class="true">x</td>
                <td></td>
                <td></td>
            </tr>
            <tr class="row-light">
                <td>Gladys</td>
                <td class="innocent">innocent</td>
                <td></td>
                <td style="border-left: 3px solid #4a4849"></td>
                <td class="true">x</td>
                <td></td>
                <td></td>
            </tr>
        </tbody>
    </table>
</div>



- <strong>Precision</strong>: What percent of jailed grandmas were guilty? -- <strong>100%</strong>.
- <strong>Recall</strong>: What percent of guilty grandmas were jailed? -- <strong>20%</strong>.
- <strong>Accuracy</strong>: What percent of convictions were accurate? -- <strong>60%</strong>.

<!-- | Precision | 100% |
| Recall  |  20% |
| Accuracy |  60%  |
| F1 |  33%  | -->

### Low Precision, High Recall
What about low precision, high recall? 

Well here, the judge successfully condemns all the guilty people, but in the process condemns many innocents as well.

<!-- ![img](high-recall.png) -->

<div style="display: flex; justify-content: center;">
    <table>
        <thead style="border: .5px solid #bf2673;">
            <tr>
                <th style="border: .5px solid #4f4f4f;" class="row-dark">Grandmas</th>
                <th class="row-dark">Guilty?</th>
                <th class="row-dark">Jail</th>
                <th class="row-dark" style="line-height: 1.2; text-align: center; border-left: 3px solid #4a4849">TP</th>
                <th class="row-dark" style="line-height: 1.2; text-align: center;">TN</th>
                <th class="row-dark" style="line-height: 1.2; text-align: center;">FP</th>
                <th class="row-dark" style="line-height: 1.2; text-align: center;">FN</th>
            </tr>
        </thead>
        <tbody>
            <tr class="row-dark">
                <td>Edith</td>
                <td class="guilty">guilty</td>
                <td class="jail">yes</td>
                <td class="true" style="border-left: 3px solid #4a4849">x</td>
                <td></td>
                <td></td>
                <td></td>
            </tr>
            <tr class="row-light">
                <td>Mabel</td>
                <td class="guilty">guilty</td>
                <td class="jail">yes</td>
                <td  class="true" style="border-left: 3px solid #4a4849">x</td>
                <td></td>
                <td></td>
                <td></td>
            </tr>
            <tr class="row-dark">
                <td>Florence</td>
                <td class="guilty">guilty</td>
                <td class="jail">yes</td>
                <td  class="true" style="border-left: 3px solid #4a4849">x</td>
                <td></td>
                <td></td>
                <td></td>
            </tr>
            <tr class="row-light">
                <td>Eleanor</td>
                <td class="guilty">guilty</td>
                <td class="jail">yes</td>
                <td  class="true" style="border-left: 3px solid #4a4849">x</td>
                <td></td>
                <td></td>
                <td></td>
            </tr>
            <tr class="row-dark">
                <td>Beatrice</td>
                <td class="guilty">guilty</td>
                <td class="jail">yes</td>
                <td  class="true" style="border-left: 3px solid #4a4849">x</td>
                <td></td>
                <td></td>
                <td></td>
            </tr>
            <tr class="row-light">
                <td>Agnes</td>
                <td class="innocent">innocent</td>
                <td class="jail">yes</td>
                <td style="border-left: 3px solid #4a4849"></td>
                <td></td>
                <td class="false">x</td>
                <td></td>
            </tr>
            <tr class="row-dark">
                <td>Mildred</td>
                <td class="innocent">innocent</td>
                <td class="jail">yes</td>
                <td style="border-left: 3px solid #4a4849"></td>
                <td></td>
                <td class="false">x</td>
                <td></td>
            </tr>
            <tr class="row-light">
                <td>Gertrude</td>
                <td class="innocent">innocent</td>
                <td class="jail">yes</td>
                <td style="border-left: 3px solid #4a4849"></td>
                <td></td>
                <td class="false">x</td>
                <td></td>
            </tr>
            <tr class="row-dark">
                <td>Dorothy</td>
                <td class="innocent">innocent</td>
                <td class="jail">yes</td>
                <td style="border-left: 3px solid #4a4849"></td>
                <td></td>
                <td class="false">x</td>
                <td></td>
            </tr>
            <tr class="row-light">
                <td>Gladys</td>
                <td class="innocent">innocent</td>
                <td></td>
                <td style="border-left: 3px solid #4a4849"></td>
                <td class="true">x</td>
                <td></td>
                <td></td>
            </tr>
        </tbody>
    </table>
</div>

- <strong>Precision</strong>: What percent of jailed grandmas were guilty? -- <strong>56%</strong>.
- <strong>Recall</strong>: What percent of guilty grandmas were jailed? -- <strong>100%</strong>.
- <strong>Accuracy</strong>: What percent of convictions were accurate? -- <strong>60%</strong>.

## Meaningful Metrics Matter
Did scientists really need to come up with two new metrics no one has ever heard of just to explain how accurate a judge is?

### Accuracy
Well, you may have noticed that despite our two wildly different examples, accuracy was the exact same. 

Because accuracy doesn't care if a mistake means sending an innocent grandma to jail or letting a guilty grandma free. They are both the same mistake as far as accuracy is concerned. And in our examples the percent of the time the judge correctly decided whether a grandma was guilty or innocent was the same, 60%.

$$
\frac{\text{True Positives} + \text{True Negatives}}{\text{Total Number of Observations}}
$$

or

$$
\frac{\text{Correctly Sentenced Grandmas}}{\text{All Sentenced Grandmas}} 
$$


### To Visit or Not to Visit?
Ok sure, in my contrived example, these metrics seem really important, but what about in the real world?

Well let's say you've got a cough and you are about to visit your immunocompromised grandma in high security prison, so you take a COVID test. Thankfully, it says you are negative! But then you read the back of the box and you see that the test has 100% precision but only 20% recall. 

Can you really be certain you don't have COVID? Well that 100% precision means you could have been certain of a positive diagnosis...but since you had a negative result, and recall is only 20%, there is still a decent chance that you have COVID. 

Technically to know the exact percent, you would need to know your a priori probability of having COVID considering you have a cough, perhaps I'll write a follow-up post on this...but for now, maybe you shouldn't visit your guilty grandma after all.

<!-- ## What about F1??
I see lots of ML practitioners using the F1 score as a replacement for accuracy 

$$
\text{F1 Score} = 2 \cdot \frac{\text{Precision} \cdot \text{Recall}}{\text{Precision} + \text{Recall}}
$$
<br><br> -->

## Machine Learning
In truth, medical statistics has its own specialized metrics and terminology; they don't actually use the concepts of precision and recall. So for our final example let's look at a real-world machine learning problem.

At my work, we have created a curated Science Discovery Engine that contains, among other things, 52,000 Earth Science datasets. And we'd like a subset of these datasets to be available in a specialized portal dedicated to Environmental Justice. 

There are 8 possible types of EJ datasets (climate change, extreme heat, food availability, etc), so we plan to train a classification model to tag each of the 52,000 broader Earth Science datasets as either not-EJ, or with one or more of the 8 EJ indicators.

### High Precision, Low Recall
So what would the end user experience be like if we optimized the model for high precision but low recall?

This is the same as only sending guilty grandmas to jail, but missing many in the process. So we could be confident that only EJ content was on the portal, but we would also be missing lots of relevant content.

### High Recall, Low Precision
If we instead optimized for high recall, then this would be the same as convicting all the guilty grandmas, but putting innocent grandmas in jail in the process.

The portal would be guaranteed to contain all the EJ datasets from the broader corpus, but it would also have unrelated content polluting the results.

### What's Better?
Well it depends on the goal of the platform and the end user. If you want to ensure that every bit of relevant data is available, then you go with high recall. But if you want to guarantee that no unrelated datasets appear in the portal, then you should optimize for high precision.

<br><br>
> Cover image generated using DALL-E 3 
{: .prompt-info }
---
title: Guilty Grandmas
date: 2024-06-01
last_modified_at: 2024-06-02
categories: [machine leaning, metrics]
tags: []
description: Understanding precision, recall, accuracy, and F1.
media_subpath: /ml-metrics/
image: cropped_grandmas.jpg
math: True
published: True
---

> This is an unfinished post that will receive additional content and editing in the future. 
{: .prompt-danger }

## The Madness of Machine Learning Metrics
If you are interested in machine learning, then you've seen the words precision, accuracy, recall, and F1. Maybe you've heard of True Negatives and False Positives, and perhaps some misguided soul has tried to explain everything with some picture of arrows on a bullseye. 

It took me the longest time to full internalize these terms, and I think that was in large part because of how they were explained to me. I don't want you to suffer like I did. 

This post will attempt to give you an intuitive sense of what these metrics mean in the real world.

## Guilty Grandmas
I think the first hurdle is wrapping your head around these obscure terms. What the heck is a false negative anyway? Let's use a real example to find out.

Let's say you are Chad, the local district judge. And on your docket today, you have 10 naughty grandmas. Actually, half of them are guilty and the other half are innocent, but you don't know that. You're just the anthropomorphization of a machine learning algorithm designed for comedic illustration.

Anyway, when training a machine learning model, often you have to choose whether to have high recall or to have high precision. There is a balancing act between these two metrics.


## High Precision, Low Recall
So what would it mean for a model to be high precision, but low recall? 

Basically, when the judge does send a grandma to jail he always right, but he misses a lot of actually guilty grandmas in the process.

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

<div style="display: flex; justify-content: center;">
    <table>
        <thead style="border: .5px solid #bf2673;">
            <tr>
                <th style="border: .5px solid #4f4f4f;" class="row-dark">Grandmas</th>
                <th class="row-dark">Innocent?</th>
                <th class="row-dark">Jail</th>
                <th class="row-dark" style="line-height: 1.2; text-align: center; border-left: 3px solid #4a4849">True<br>Positive</th>
                <th class="row-dark" style="line-height: 1.2; text-align: center;">True<br>Negative</th>
                <th class="row-dark" style="line-height: 1.2; text-align: center;">False<br>Positive</th>
                <th class="row-dark" style="line-height: 1.2; text-align: center;">False<br>Negative</th>
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

<!-- <div style="display: flex; justify-content: center;">
    <table>
        <thead style="border: .5px solid #bf2673;">
            <tr>
                <th style="border: .5px solid #4f4f4f;" class="row-dark">Metric</th>
                <th class="row-dark">Score</th>
            </tr>
        </thead>
        <tbody>
            <tr class="row-dark">
                <td>Precision</td>
                <td>100%</td>
            </tr>
            <tr class="row-light">
                <td>Recall</td>
                <td>20%</td>
            </tr>
            <tr class="row-dark">
                <td>Accuracy</td>
                <td>60%</td>
            </tr>
            <tr class="row-light">
                <td>F1</td>
                <td>33%</td>
            </tr>
        </tbody>
    </table>
</div> -->

- <strong>Precision</strong>: What percent of jailed grandmas were guilty? -- <strong>100%</strong>.
- <strong>Recall</strong>: What percent of guilty grandmas were jailed? -- <strong>20%</strong>.
- <strong>Accuracy</strong>: What percent of convictions were accurate? -- <strong>60%</strong>.

<!-- | Precision | 100% |
| Recall  |  20% |
| Accuracy |  60%  |
| F1 |  33%  | -->

## Low Precision, High Recall
What about low precision, high recall? 

Well here, the judge successfully condemns all the guilty people, but in the process condemns many innocents as well.


<div style="display: flex; justify-content: center;">
    <table>
        <thead style="border: .5px solid #bf2673;">
            <tr>
                <th style="border: .5px solid #4f4f4f;" class="row-dark">Grandmas</th>
                <th class="row-dark">Innocent?</th>
                <th class="row-dark">Jail</th>
                <th class="row-dark" style="line-height: 1.2; text-align: center; border-left: 3px solid #4a4849">True<br>Positive</th>
                <th class="row-dark" style="line-height: 1.2; text-align: center;">True<br>Negative</th>
                <th class="row-dark" style="line-height: 1.2; text-align: center;">False<br>Positive</th>
                <th class="row-dark" style="line-height: 1.2; text-align: center;">False<br>Negative</th>
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
- <strong>Recall</strong>: What percent of guilty grandmas were jailed? -- <strong>20%</strong>.
- <strong>Accuracy</strong>: What percent of convictions were accurate? -- <strong>60%</strong>.
 
## Accuracy
Interestingly, the accuracy, or percent of the time the judge accurately decided whether a grandma was guilty or innocent, was the exact same in both examples, 60%. But obviously there is a massive difference between the two models.

## The Metrics
How did we actually calculate these numbers?

### Precision
Did you convict any innocent grandmas?

$$
\frac{\text{True Positives}}{\text{True Positives} + \text{False Positives}} =  \frac{\text{Jailed Grandmas who were Guilty}}{\text{Jailed Grandmas}} 
$$

### Recall
Did you put all the guilty grandmas in jail?

$$
\frac{\text{True Positives}}{\text{True Positives} + \text{False Negatives}} =  \frac{\text{Jailed Grandmas who were Guilty}}{\text{Guilty Grandmas}} 
$$

### Accuracy
What percent did you convict correctly?

$$
\frac{\text{True Positives} + \text{True Negatives}}{\text{Total Number of Observations}} =  \frac{\text{Correctly Sentenced Grandmas}}{\text{All Sentenced Grandmas}} 
$$


<!-- F1 scores are some ML bullshit

$$
\text{F1 Score} = 2 \cdot \frac{\text{Precision} \cdot \text{Recall}}{\text{Precision} + \text{Recall}}
$$ -->
<br><br>

> Cover image generated using DALL-E 3 
{: .prompt-info }
---
title: Machine Learning Metrics
date: 2024-05-31
last_modified_at: 2024-05-31
categories: [machine leaning, metrics]
tags: []
description: Quick explanation of precision, recall, accuracy, and F1.
published: False
math: True
---

## Dataset

Let's imagine we are building a machine learning model to classify earth science datasets into one of two categories: Extreme Heat or Flooding.

We've finished building our model and we are at the point of evaluating its performance. We have a small set of known datasets that we will use to see how well the model is doing.




$$
\text{Precision} = \frac{\text{True Positives}}{\text{True Positives} + \text{False Positives}}
$$
What percent of identified extreme heat events are actually extreme heat events?
When the model tells you something is true, how likely is it to actually be true?


$$
\text{Recall} = \frac{\text{True Positives}}{\text{True Positives} + \text{False Negatives}}
$$

$$
\text{Accuracy} = \frac{\text{True Positives} + \text{True Negatives}}{\text{Total Number of Observations}}
$$

$$
\text{F1 Score} = 2 \cdot \frac{\text{Precision} \cdot \text{Recall}}{\text{Precision} + \text{Recall}}
$$


<style>
    table {
        width: 50%;
        border-collapse: collapse;
        margin: 25px 0;
        font-size: 18px;
        text-align: left;
    }
    th, td {
        padding: 12px;
        border: 1px solid #ddd;
    }
    th {
        background-color: #f2f2f2;
    }
    .correct {
        background-color: #a8d5a2;
        color: white;
        text-align: center;
    }
    .incorrect {
        background-color: #f7b3b3;
        color: white;
        text-align: center;
    }
</style>

<table>
    <thead>
        <tr>
            <th>Datasets</th>
            <th>Actual</th>
            <th>Tagged as Heat</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Dataset 1</td>
            <td>Extreme Heat</td>
            <td class="correct">x</td>
        </tr>
        <tr>
            <td>Dataset 2</td>
            <td>Extreme Heat</td>
            <td class="correct">x</td>
        </tr>
        <tr>
            <td>Dataset 3</td>
            <td>Extreme Heat</td>
            <td class="correct">x</td>
        </tr>
        <tr>
            <td>Dataset 4</td>
            <td>Extreme Heat</td>
            <td class="correct">x</td>
        </tr>
        <tr>
            <td>Dataset 5</td>
            <td>Extreme Heat</td>
            <td></td>
        </tr>
        <tr>
            <td>Dataset 6</td>
            <td>Flood</td>
            <td class="incorrect">x</td>
        </tr>
        <tr>
            <td>Dataset 7</td>
            <td>Flood</td>
            <td class="incorrect">x</td>
        </tr>
        <tr>
            <td>Dataset 8</td>
            <td>Flood</td>
            <td></td>
        </tr>
        <tr>
            <td>Dataset 9</td>
            <td>Flood</td>
            <td></td>
        </tr>
        <tr>
            <td>Dataset 10</td>
            <td>Flood</td>
            <td></td>
        </tr>
    </tbody>
</table>

---
nav_title: Conversion Correlation
article_title: Conversion Correlation
alias: /conversion_correlation/
page_order: 3

page_type: reference
description: "This reference article explains the Conversion Correlation analysis on the Campaign Analytics page."
tool: 
  - Reports
  
---

# Conversion Correlation

> The Conversion Correlation analysis on the Campaign Analytics page gives you insight into what user attributes and behaviors help or hurt the outcomes you set for campaigns. 

## Overview

For every campaign, we check a list of attributes and user behaviors and compute whether they are statistically significantly associated with increases or decreases in each of the [conversion events](https://www.braze.com/docs/user_guide/engagement_tools/campaigns/testing_and_more/conversion_events/) you've chosen for the campaign. We also compute how much more or less likely users with the given attribute or behavior were to convert, and if it's significant, display that on the corresponding left or right side of the table. Users with each attribute or behavior of interest are compared to the rates for the entire campaign audience as a whole. Behaviors and attributes that have no significant correlation with conversion are simply not shown in the table.

__To run a Conversion Correlation Analysis:__<br> 
Use the dropdown to select the conversion event of interest.

![Conversion Correlation Table][1]

## What is checked?

We check the following attributes by treating them as categorical variables. In other words, a user either does or doesn't have each possible value of these attributes, and we test whether they affect the conversion rate.

-  Country
-  Language
-  Gender

We also check whether the following affect the rate of conversion:

- Performing any custom events
- Campaigns and Canvases received in the last 30 days (other than the campaign currently being assessed)

Finally, we check several behavioral variables that can take on multiple values. We split the following into 4 buckets or quartiles and then measure the association of being in that quartile with increases or decreases in conversion:

- Age
- Total dollars spent
- Number of sessions

## When can I check this analysis?

This analysis becomes available at least 24 hours after a campaign starts sending and only looks at sends that occurred in the last 30 days. If no behaviors or attributes significantly correlate with any of the campaign's conversion events, the dropdown will be disabled and a message will be displayed letting you know that's the case.

## How we check for significance

We check for statistical significance by using something called the [Wilson confidence interval](https://en.wikipedia.org/wiki/Binomial_proportion_confidence_interval#Wilson_score_interval). We determine at 95% confidence the rate at which the entire campaign audience converted. This is called the base rate. 

Then, for each of the variables, we also compute the rate at which users with that particular attribute or behavior of interest converted at 95% confidence. By dividing that by the base rate, we're able to measure the ratio. If it's much larger than 1, users with the attribute or behavior are more likely to convert. If it's much less, they're less likely. We display the value of the ratio itself in the table. The value is only displayed if it's far enough from 1 to be significant at the 95% confidence level.

[1]: {% image_buster /assets/img/convcorr.png %}

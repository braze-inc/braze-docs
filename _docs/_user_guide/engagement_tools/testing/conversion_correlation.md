---
nav_title: Conversion Correlation
alias: /conversion_correlation/
description: "This article covers explains the Conversion Correlation analysis on the Campaign Analytics page."
page_type: reference
page_order: 3
---

# Conversion Correlation

> The Conversion Correlation analysis on the Campaign Analytics page gives you insight into what user attributes and behaviors help or hurt the outcomes you set for campaigns. 

## How the Conversion Correlation Works

For every campaign, we check a list of attributes and user behaviors and compute whether they are stastically significantly associated with increases or decreases in each of the [conversion events](https://www.braze.com/docs/user_guide/engagement_tools/campaigns/testing_and_more/conversion_events/) you've chosen for the campaign. We also compute how much more or less likely users with the given attribute or behavior were to convert, and if it's significant, display that on the appropriate side of the table depending on whether the attribute or behavior is associated with increased or decreased conversion. Users with each attribute or behavior of interest are compared to the rates for the entire campaign audience as a whole.

# What is checked?

We check the following attributes by treating them as categorical variables. In other words, a user either does or doesn't have each possible value of these attributes, and we test whether they do affects the conversion rate.

-  Country
-  Language
-  Gender

We also check whether the following affect the rate of conversion:

- Having ever performed each of your top 10 most common custom events 
- Having received each of your top 10 highest volume campaigns in the last 30 days (other than the campaign currently being assessed)

Finally, we check several behavioral variables that can take on multiple values. We split the following into 4 buckets or quartiles and then measure the association of being in that quartile with increases or decreases in conversion:

- Age
- Total dollars spent
- Number of sessions

# How we check for significance

We check for statistical significance by using something called the [Wilson confidence interval](https://en.wikipedia.org/wiki/Binomial_proportion_confidence_interval#Wilson_score_interval). We determine at 95% confidence the rate at which the entire campaign audience converted. This is called the base rate. 

Then, for each of the variables we also compute the rate at which users with that particular attribute or behavior of interest converted at 95% confidence. By dividing that by the base rate, we're able to measure the ratio. If it's much larger than 1, users with the attribute or behavior are more likely to convert. If it's much less, they're less likely. We display the value of the ratio itself in the table. The value is only displayed if it's far enough from 1 to be significant at the 95% confidence level.

![Conversion Correlation Table][1]


[1]: {% image_buster /assets/img/convcorr.png %}
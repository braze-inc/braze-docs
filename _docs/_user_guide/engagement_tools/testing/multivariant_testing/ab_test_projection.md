---
nav_title: A/B Test Projection
article_title: A/B Test Projection
page_order: 20
page_type: reference
description: "This article explains how A/B Test Projection works."
---

# A/B Test Projection

A/B Test Projection uses neural networks and language models to predict which subject lines perform best. Our model has extracted linguistic features from winning A/B tests performed on Braze and used those statistical language patterns to teach AI what makes for better subject lines.

## Running a projection

In Campaign composition, insert your message variants along with their subject lines into the editor. When ready, go to step 3 of the campaign creation flow. In the A/B Testing panel of the Target Audience step, click **Run Projection**

<img width="518" alt="image" src="https://github.com/braze-inc/braze-docs/assets/17167198/8e74835c-76e4-4241-9763-c4f86a622c75">

A window will open where you will see the subject lines of any message variants you have already created. Optionally, you may insert up to 1 additional subject line as desired.

Click **Run Projection**

<img width="722" alt="image" src="https://github.com/braze-inc/braze-docs/assets/17167198/f9ad45a3-6565-467b-a7f6-35277bef7699">

The subject line our AI predicts to be best will be highlighted with a "Projected Winner" label.

### Data aggregation 

Note that this feature requires Data Aggregation be enabled in your Company Settings. That is because this feature learns from historical A/B tests carried out on Braze. In order to get the benefit of the feature, we ask you to allow the AI to learn from the language patterns of your A/B tests. If you'd like to opt out of data aggregation, you can do so in Company Settings. [Click here to learn more.
](braze.com/docs)

### How we use your data?

Keep in mind that the actual copy of your messages is never provided to the algorithm. We first extract the high level language patterns that predict winning messages. Then, those patterns are provided to the AI in order to teach it to discern what constitutes superior subject lines.

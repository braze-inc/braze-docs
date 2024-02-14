---
nav_title: A/B Test Projection
article_title: A/B Test Projection
page_order: 20
page_type: reference
description: "This article explains how A/B Test Projection works."
---

# A/B Test Projection

A/B Test Projection uses neural networks  to predict which subject lines perform best. Our model has extracted linguistic features from winning A/B tests performed on Braze and used those statistical language patterns to teach AI what makes for better subject lines.

## Running a projection

In Campaign composition, insert your message variants along with their subject lines into the editor. When ready, go to step 3 of the campaign creation flow. In the A/B Testing panel of the Target Audience step, click **Run Projection**

<img width="518" alt="image" src="https://github.com/braze-inc/braze-docs/assets/17167198/8e74835c-76e4-4241-9763-c4f86a622c75">

A window will open where you will see the subject lines of any message variants you have already created. Optionally, you may insert up to 8 additional subject lines by entering one manually into the box and running the projection.

Click **Run Projection**

<img width="722" alt="image" src="https://github.com/braze-inc/braze-docs/assets/17167198/f9ad45a3-6565-467b-a7f6-35277bef7699">

The subject line our AI predicts to be best will be highlighted with a "Projected Winner" label.


### How we use your data?

This feature learns from past A/B tests carried out on Braze. Keep in mind that the actual copy of your or any Braze customers' messages is never provided to the model. We first extract the high level language patterns that predict winning messages in A/B tests. Then, those patterns are provided to the AI in order to teach it to discern which linguistic features constitute superior subject lines.

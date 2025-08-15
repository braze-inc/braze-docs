---
nav_title: Ab test projection
article_title: A/B Test Projection
page_order: 20
hidden: true
page_type: reference
description: "This article explains how A/B test projection works, how to run a projection, and how Braze uses your data."
---

# A/B test projection

> A/B test projection uses neural networks to predict which subject lines perform best. Our model extracts linguistic features from winning A/B tests performed on Braze and uses those statistical language patterns to teach our AI what makes better subject lines.

{% alert important %} 
This feature is currently in early access. Contact your Braze customer success or account manager if you're interested in participating in the early access.
{% endalert %}

## Running a projection

In campaign composition, insert your message variants and their subject lines into the editor. When ready, go to the **Target Audience** step of the campaign creation flow. In the **A/B Testing** panel, select **Run Projection**.

<img width="518" alt="image" src="https://github.com/braze-inc/braze-docs/assets/17167198/8e74835c-76e4-4241-9763-c4f86a622c75">

A modal will open with the subject lines of any message variants you have already created. Optionally, you may insert additional subject lines (up to a maximum of ten) by manually entering one into the box and running the projection. Select **Run Projection**.

<img width="722" alt="image" src="https://github.com/braze-inc/braze-docs/assets/17167198/f9ad45a3-6565-467b-a7f6-35277bef7699">

The subject line our AI predicts to be best will be highlighted with a **Projected Winner** label.

{% alert note %}
For [quick push campaigns]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/quick_push/), A/B testing is supported when you select multiple platforms.
{% endalert %}

### How accurate are the projections?

In testing, we found the projections to be about 70% accurate when picking between pairs of messages in real A/B tests. Consider this when interpreting the messages the model projects to win.

### How do we use your data?

This feature learns from past A/B tests carried out on Braze. The actual copy of your or any Braze customers' messages is never provided to the model. We first extract the high-level language patterns that predict winning messages in A/B tests. Then, we provide those patterns to our AI to teach it to discern which linguistic features constitute superior subject lines.
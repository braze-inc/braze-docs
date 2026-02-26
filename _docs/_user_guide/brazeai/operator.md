---
nav_title: Operator
article_title: BrazeAI Operator
page_order: 7
layout: dev_guide
alias: /operator/
guide_top_header: "BrazeAI Operator"
guide_top_text: "BrazeAI Operator<sup>TM</sup> is an AI-powered assistant built into the dashboard. Operator helps get things done—answering questions, walking through setup, troubleshooting issues, and brainstorming ideas."
description: "This reference article covers BrazeAI Operator<sup>TM</sup>, an AI-powered assistant built into the Braze dashboard."

guide_featured_title: "Topics"
guide_featured_list:
- name: Getting Started
  link: /docs/user_guide/brazeai/operator/getting_started/
  image: /assets/img/braze_icons/book-open-01.svg
- name: Reviewing Actions
  link: /docs/user_guide/brazeai/operator/reviewing_actions/
  image: /assets/img/braze_icons/check-square-broken.svg
- name: Troubleshooting
  link: /docs/user_guide/brazeai/operator/troubleshooting/
  image: /assets/img/braze_icons/alert-circle.svg

---

## Data privacy and security

### HIPAA compliance

AI Operator utilizes multi-turn conversation technology that is currently ineligible for OpenAI's Zero Data Retention policy. AI Operator uses OpenAI's Modified Abuse Monitoring data retention policy, but AI Operator is not covered by the Business Associate Agreement (BAA) between Braze and OpenAI. Users should not prompt AI Operator to access Protected Health Information (PHI) stored in Braze or otherwise submit PHI to this feature.

### Model providers as sub-processors or third-party providers

When you use an integration with an LLM provider provided by Braze through the Braze Services ("Braze-provided LLM"), the providers of such Braze-provided LLM act as Braze Sub-processors, subject to the terms of the Data Processing Addendum (DPA) between you and Braze. BrazeAI Operator<sup>TM</sup> integrates with OpenAI.

### How data is used with OpenAI

To generate AI output through BrazeAI features that leverage OpenAI ("Output"), Braze will send certain information ("Input") to OpenAI. Input consists of your prompts, the content displayed in the dashboard, and workspace data relevant to your queries. Per [OpenAI's API platform commitments](https://openai.com/enterprise-privacy/), data sent to OpenAI's API via Braze is not used to train or improve OpenAI models. Between you and Braze, Output is your intellectual property. Braze will not assert any claims of copyright ownership on such Output. Braze makes no warranty of any kind with respect to any AI-generated content, including Output.

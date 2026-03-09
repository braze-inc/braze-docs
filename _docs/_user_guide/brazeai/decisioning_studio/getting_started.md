---
nav_title: Getting started
article_title: Getting Started with Decisioning Studio
layout: dev_guide_content_first
guide_top_header: "Getting Started with Decisioning Studio"
guide_top_text: "Before you create a decisioning agent, use these articles to guide your planning and understanding of Decisioning Studio."
page_order: 0
search_rank: 2
page_type: landing
description: "This section provides an introduction to Decisioning Studio, and how you can use it to design and deploy decisioning agents that optimize any business metric."

guide_featured_title: "Section articles"
guide_featured_list:
  - name: Design Your Agent
    link: /docs/user_guide/brazeai/decisioning_studio/designing_decisioning_agents/
    image: /assets/img/braze_icons/settings-01.svg
  - name: Prepare Your Data
    link: /docs/user_guide/brazeai/decisioning_studio/preparing_your_data/
    image: /assets/img/braze_icons/database-01.svg
  - name: Define Your Audience
    link: /docs/user_guide/brazeai/decisioning_studio/define_your_audience/
    image: /assets/img/braze_icons/users-01.svg
  - name: Set Up Orchestration
    link: /docs/user_guide/brazeai/decisioning_studio/set_up_orchestration/
    image: /assets/img/braze_icons/dataflow-04.svg

guide_menu_title: "Additional resources"
guide_menu_list:
  - name: About Decisioning Studio
    link: /docs/user_guide/brazeai/decisioning_studio/about/
    image: /assets/img/braze_icons/info-circle.svg
  - name: Decisioning Studio FAQ
    link: /docs/user_guide/brazeai/decisioning_studio/faq/
    image: /assets/img/braze_icons/annotation-question.svg
---

# Getting started with Decisioning Studio

> This reference gives an overview of the steps involved in setting up Decisioning Studio, including connecting data sources, setting up orchestration, and designing your decisioning agent.

BrazeAI Decisioning Studio™ allows you to design and deploy decisioning agents that optimize any business metric. A decisioning agent is a custom configuration tailored to meet a specific business goal.

{% alert tip %}
Your AI Expert Services team will support you in setting up Decisioning Studio for optimal performance.
{% endalert %}

## Key design decisions

Working with the AI Decisioning Services team, you'll make the following decisions:

| Decision | Description | Examples |
|----------|-------------|----------|
| **Success metric** | What will the agent maximize when personalizing customer engagement? | Revenue, LTV, ARPU, conversions, retention |
| **Audience** | For whom will the Decisioning Studio agent make customer engagement decisions? | All customers, loyalty members, at-risk subscribers |
| **Experiment groups** | How should Decisioning Studio's randomized controlled trials be structured? | Decisioning Studio, Random Control, BAU, Holdout |
| **Dimensions** | What decisions should the agent personalize? | Time of day, subject line, frequency, offers, channel |
| **Options** | What options does the agent have to work with? | Specific templates, offers, time windows |
| **Constraints** | What decisions should the agent *never* make? | Geographic restrictions, budget limits, eligibility rules |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

Each of these decisions has implications for how much incremental uplift the agent may be able to generate, and how quickly. Our AI Decisioning Services team will work with you to design an agent that generates maximum value while respecting all of your business rules.

![Decisioning Pro Diagram]({% image_buster /assets/img/decisioning_studio/decisioning_studio_pro_agent_design.png %})

## Decisioning Studio capabilities

| Capability | Details |
|------------|---------|
| **Any success metric** | Optimize for revenue, conversions, ARPU, LTV, or any business KPI |
| **Unlimited dimensions** | Personalize across offer, channel, timing, frequency, creative, and more |
| **Any CEP** | Native integrations with Braze, SFMC, Klaviyo + custom integrations for any platform |
| **AI Decisioning Services** | Dedicated support from Braze's data science team |
| **Advanced experiment design** | Fully customizable treatment groups and holdouts |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

## Best practices

A few best practices for designing Decisioning Studio agents:

1. **Maximize data richness**: The more information agents have about your customers, the better they will perform.
2. **Diversify actions**: The more diverse the set of actions the agent can take, the more it can personalize its strategy for each user.
3. **Minimize constraints**: The fewer constraints on your agents, the better. Constraints should be designed to respect business rules while freeing agent-led experimentation as much as possible.

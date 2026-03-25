---
nav_title: Get started
article_title: Get Started with Decisioning Studio
layout: dev_guide
guide_top_header: "Get Started with Decisioning Studio"
guide_top_text: ""
page_order: 0
search_rank: 2
page_type: landing
description: "This section provides an introduction to Decisioning Studio, and how you can use it to design and deploy decisioning agents that optimize any business metric."

guide_featured_title: "Section articles"
guide_featured_list:
  - name: Design Your Agent
    link: /docs/user_guide/brazeai/decisioning_studio/design_agents/
    image: /assets/img/braze_icons/settings-01.svg
  - name: Prepare Your Data
    link: /docs/user_guide/brazeai/decisioning_studio/prepare_data/
    image: /assets/img/braze_icons/database-01.svg
  - name: Define Your Audience
    link: /docs/user_guide/brazeai/decisioning_studio/audience/
    image: /assets/img/braze_icons/users-01.svg
  - name: Set Up Orchestration
    link: /docs/user_guide/brazeai/decisioning_studio/orchestration_setup/
    image: /assets/img/braze_icons/dataflow-04.svg

guide_menu_title: "Additional resources"
guide_menu_list:
  - name: About Decisioning Studio
    link: /docs/user_guide/brazeai/decisioning_studio/
    image: /assets/img/braze_icons/info-circle.svg
  - name: Decisioning Studio FAQ
    link: /docs/user_guide/brazeai/decisioning_studio/faq/
    image: /assets/img/braze_icons/annotation-question.svg
---

BrazeAI Decisioning Studio™ allows you to design and deploy decisioning agents that optimize any business metric.

This reference gives an overview of the steps involved in setting up Decisioning Studio, including designing your agent, configuring and connecting data sources, setting up orchestration, and evaluating performance.

## Key design decisions

Work with the AI Decisioning Services team to make the following decisions:

| Decision | Description | Examples |
|----------|-------------|----------|
| **Success metric** | What will the agent maximize when personalizing customer engagement? | Revenue, LTV, ARPU, conversions, retention |
| **Audience** | For whom will the Decisioning Studio agent make customer engagement decisions? | All customers, loyalty members, at-risk subscribers |
| **Experiment groups** | How should Decisioning Studio's randomized controlled trials be structured? | Decisioning Studio, Random Control, BAU, Holdout |
| **Dimensions** | What decisions should the agent personalize? | Time of day, subject line, frequency, offers, channel |
| **Options** | What options does the agent have to work with? | Specific templates, offers, time windows |
| **Constraints** | What decisions should the agent never make? | Geographic restrictions, budget limits, eligibility rules |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

Each of these decisions has implications for how much incremental uplift the agent may be able to generate, and how quickly. Our AI Decisioning Services team will work with you to design an agent that generates maximum value while respecting all of your business rules.

![Diagram showing how success metrics, audience, experiment groups, dimensions, options, and constraints feed into a Decisioning Studio agent design]({% image_buster /assets/img/decisioning_studio/decisioning_studio_pro_agent_design.png %})

## Decisioning Studio capabilities

| Capability | Details |
|------------|---------|
| **Any success metric** | Optimize for revenue, conversions, ARPU, LTV, or any business KPI |
| **Unlimited dimensions** | Personalize across offer, channel, timing, frequency, creative, and more |
| **Any CEP** | Native integrations with Braze, Salesforce Marketing Cloud, or custom integrations for any platform |
| **AI Decisioning Services** | Dedicated support from Braze's data science team |
| **Advanced experiment design** | Fully customizable treatment groups and holdouts |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

## Best practices

A few best practices for designing Decisioning Studio agents:

- **Maximize data richness**: The more information agents have about your customers, the better they will perform.
- **Diversify actions**: The more diverse the set of actions the agent can take, the more it can personalize its strategy for each user.
- **Minimize constraints**: The fewer constraints on your agents, the better. Constraints should be designed to respect business rules while freeing agent-led experimentation as much as possible.
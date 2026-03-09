---
nav_title: Getting started
article_title: Getting Started with Decisioning Studio
layout: dev_guide
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

## Setting up Decisioning Studio

To set up Decisioning Studio, you will complete the following steps:

### Step 1: Prepare your data

Connect customer profiles and engagement data so that the decisioning agents you create understand who each customer is and how they behave.

You typically only need to connect your data sources once, during the initial setup of Decisioning Studio. If you expand your use cases later, you may need to add new data sources.

{% alert tip %}
Any data already in the [Braze Data Platform]({{site.baseurl}}/user_guide/data/braze_data_platform) is automatically available to Decisioning Studio.
{% endalert %}

For detailed guidance, see [Preparing your data]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/preparing_your_data/).

### Step 2: Define your audience

Define the audience for your decisioning agent and configure treatment groups for randomized controlled trials.

For detailed guidance, see [Define your audience]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/define_your_audience/).

### Step 3: Set up orchestration

Integrate Decisioning Studio with your customer engagement platform (CEP) to allow your agents to orchestrate actions. The CEP is the platform used to deliver personalized experiences to your customers based on the agent's decisions.

You generally need to set up this orchestration only once.

For detailed guidance, see [Set up orchestration]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/set_up_orchestration/).

### Step 4: Design your agents

Configure your decisioning agents to define what outcomes you want to maximize and what actions the agent can take to achieve them. See [Designing Decisioning Agents]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/designing_decisioning_agents/) for detailed guidance on agent design.

### Step 5: Launch your decisioning agent

Launch your decisioning agent and let it continuously learn and optimize for your business outcomes.

For detailed guidance, see [Launch your agent]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/launch_your_agent/).

## Next steps

Now that you have a basic understanding of the key concepts of Decisioning Studio, you can start designing your decisioning agent.

- [Designing Decisioning Agents]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/designing_decisioning_agents/)

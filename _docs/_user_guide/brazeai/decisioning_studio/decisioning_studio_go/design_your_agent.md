---
nav_title: Design your agent
article_title: Design your agent
page_order: 3
description: "Learn how to design a BrazeAI Decisioning Studio Go agent, including audience definition, dimensions, and Go-specific limitations."
---

# Design your agent

> This article covers how to design your Decisioning Studio Go agent, including defining your audience, selecting dimensions, and understanding Go-specific capabilities and limitations.

For foundational concepts about decisioning agents—including success metrics, dimensions, action banks, and constraints—see [Designing Decisioning Agents]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/getting_started/designing_decisioning_agents/).

## Go vs. Pro capabilities

Decisioning Studio Go is a self-service platform with streamlined capabilities compared to Decisioning Studio Pro. Understanding these differences helps you design an effective agent within Go's scope.

| Capability | Decisioning Studio Go | Decisioning Studio Pro |
|-----------|----------------------|------------------------|
| **Success metric** | Clicks only | Any business metric (revenue, conversions, ARPU, etc.) |
| **Dimensions** | Limited action bank | Unlimited dimensions |
| **CEPs supported** | Braze, SFMC, Klaviyo | Any CEP (native + custom) |
| **Setup** | Self-service | AI Decisioning Services support |
| **Experiment groups** | Go + Random Control + optional BAU | Fully customizable |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

## Designing your Go agent

When designing a Decisioning Studio Go agent, you'll make decisions in the following areas:

### Step 1: Define your audience

Your audience is the set of customers the agent will engage. In Go, audiences are defined in your CEP:

{% tabs %}
{% tab Braze %}

**Defining audience in Braze:**

1. Create a segment in Braze that defines the customers you want the agent to target.
2. When configuring your experimenter in the Decisioning Studio Go portal, select this segment as your target audience.

{% alert tip %}
Consider creating a dedicated segment for your Decisioning Studio Go experimenter to keep your testing isolated and measurable.
{% endalert %}

{% endtab %}
{% tab Salesforce Marketing Cloud %}

**Defining audience in SFMC:**

1. Configure a Data Extension that contains your target audience.
2. Ensure this Data Extension is refreshed daily with the latest customer data.
3. Reference this Data Extension in the Decisioning Studio Go portal when configuring your experimenter.

{% endtab %}
{% tab Klaviyo %}

**Defining audience in Klaviyo:**

1. Create a segment in Klaviyo that defines your target audience.
2. When configuring your experimenter in the Decisioning Studio Go portal, select this segment.

{% endtab %}
{% endtabs %}

### Step 2: Select your dimensions

Dimensions are the "levers" the agent can pull to personalize the customer experience. In Go, the available dimensions include:

| Dimension | Description | Example |
|-----------|-------------|---------|
| **Email template** | Which email template to send | Template A vs. Template B vs. Template C |
| **Subject line** | The email subject line | "Don't miss out!" vs. "Just for you" |
| **Send time** | When to send the message | Morning vs. Afternoon vs. Evening |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

{% alert note %}
The specific dimensions available depend on your CEP and how your campaigns are configured. Work with the templates and content you've set up in your CEP.
{% endalert %}

### Step 3: Configure your action bank

The action bank defines the specific options the agent can choose from for each dimension. For example:

- **Email templates**: Select which templates the agent can use (these must be configured in your CEP first)
- **Subject lines**: Define the subject line variants the agent can test
- **Send times**: Specify the time windows the agent can choose from

### Step 4: Set up experiment groups

Decisioning Studio Go automatically creates experiment groups to measure performance:

| Group | Description |
|-------|-------------|
| **Decisioning Studio Go** | Customers who receive AI-optimized recommendations |
| **Random Control** | Customers who receive randomly selected options (baseline comparison) |
| **Business as Usual (optional)** | Customers who receive your existing campaign (if comparing against current performance) |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{% alert important %}
For an accurate comparison, ensure no customer can belong to more than one experiment group, and that customers are randomly assigned to groups without bias.
{% endalert %}

## Limitations to consider

When designing your Go agent, keep these limitations in mind:

- **Clicks only**: Go optimizes for click-through rates. If you need to optimize for revenue, conversions, or other business metrics, consider Decisioning Studio Pro.
- **Limited dimensions**: Go supports a predefined set of dimensions. For custom dimensions or complex personalization, consider Decisioning Studio Pro.
- **Three CEPs**: Go only integrates with Braze, Salesforce Marketing Cloud, and Klaviyo. For other platforms, consider Decisioning Studio Pro.

## Best practices

- **Start simple**: Begin with 2-3 templates or subject line variants. This gives the agent enough options to learn while keeping the experiment manageable.
- **Give it time**: The agent needs sufficient data to learn. Allow at least 2-4 weeks before drawing conclusions about performance.
- **Keep content varied**: Ensure your options are meaningfully different. Testing minor variations may not yield significant insights.
- **Monitor regularly**: Check the Decisioning Studio Go portal to monitor experiment progress and engagement metrics.

## Next steps

Once you've designed your agent and configured it in the Decisioning Studio Go portal, you're ready to launch:

- [Launch your agent]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/launch_your_agent/)


---
nav_title: Deploying agents
article_title: Deploying custom agents
description: "Learn how to put custom agents to use in Braze after you create them."
alias: /deploying-agents/
---

# Deploying custom agents

> Learn how to put custom agents to use in Canvas steps or catalog fields after you create them. For an introduction, see [Braze Agents]({{site.baseurl}}/user_guide/brazeai/agents/). 

{% alert important %}
Braze Agents are currently in beta. For help getting started, contact your customer success manager.
{% endalert %}

## Agent usage

In the **Agent Usage** section of your agent, you can reference and navigate to where the agent is being actively used in catalogs and Canvases.

![Agent Usage section that shows two active agents and one inactive agent for Canvases.]( {% image_buster /assets/img/ai_agent/agent_usage.png %} )

## Agents in Canvas  

You can use agents as steps in a journey to personalize messages or guide decisioning in real time. For detailed setup steps, refer to [Agent Step]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/agent_step/).

### Use cases

| Use case | Description |
| --- | --- |
| Lead scoring and qualification | Use an Agent step to evaluate incoming leads on a scale (for example, 1–10). Route users with a score above a threshold into nurture paths, while disqualifying low-fit leads. |
| Dynamic message personalization | Have an agent generate subject lines, product recommendations, or message copy based on user attributes or recent behaviors. The response can be inserted directly into a Message step. |
| Customer feedback handling | Pass customer comments to an agent to analyze sentiment and generate empathetic follow-up messages. For high-value users, the agent might escalate the response or include perks. |
| Intelligent routing | Use agent outputs (boolean or numeric) to split users into different Canvas paths. For example, classify users as “at risk” or “healthy” and adjust messaging cadence accordingly. |
| Survey or response interpretation | Let an agent parse open-ended survey responses or free-text fields, returning structured values (for example, categorizing intent or need) that drive downstream paths. |
| Multi-step reasoning | Configure an agent to combine context fields and make complex decisions, such as recommending the next-best action (email, SMS, or human outreach) based on multiple user attributes. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Agents in catalogs  

You can apply an agent to catalog fields so it automatically generates or calculates values for each row. The agent will also run on new rows that are added to the catalog in the future. 

### Use cases

| Use case | Description |
| --- | --- |
| Generate product descriptions | Automatically create short marketing copy for new catalog entries, for example by generating a catchy description from structured product data like name, category, and features. |
| Enrich product attributes | Fill in missing values such as color family, style, or season based on a product name and details. For example, if a product name is “Laguna Polarized Sunglasses,” the agent could assign the style as “sport” and the color family as “blue.” |
| Calculate derived fields | Use existing fields to generate new data, such as a “fit score” based on attributes or a “popularity tag” from sales and review counts. |
| Categorize or tag items | Assign tags for recommendation logic so personalization models can segment products more effectively. For example, tag products as “outdoor,” “festival-ready,” or “premium.” |
| Localize content | Translate catalog text into another language for global campaigns, or adjust tone and length for region-specific channels. For example, translate “Classic Clubmaster Sunglasses” into Spanish as “Gafas de sol Classic Clubmaster,” or shorten descriptions for SMS campaigns. |
| Summarize reviews or feedback | Summarize sentiment or feedback into a new field, such as assigning sentiment scores like Positive, Neutral, or Negative, or creating a short text summary like “Most customers mention great fit, but note slow shipping.” |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Steps

![An Agent step in a catalog field.]({% image_buster /assets/img/ai_agent/agent_in_catalog.png %}){: style="float:right;max-width:30%;margin-left:15px;"}

To add an agent to your catalog field:

1. In your catalog, add a new field.  
2. Select **Apply AI agent**.
3. Assign an agent to this field.  
4. Select which columns should be passed as input. If none are selected, the agent will have access to all columns in the catalog.  
5. Decide if the agent should recalculate fields when catalog rows are updated. If you do not select this option, the agent will only run once per row.
6. Select **Add fields** to deploy the agent and review cost estimations. The **Cost estimation** modal shows how many times the agent will run on this catalog, roughly equal to the total number of rows. To continue, select **Confirm**.

### How catalog agents run  

After launching, the agent runs and evaluates each row, taking the selected columns into its context to produce an output. Agents run on all new rows added after you deploy the agent. If you selected **Recalculate when catalog rows update**, all values for this field update if existing source fields change.

You can refresh and edit the fields in your catalog that use agents. To remove an agent from a column, unselect **Apply AI agent**. This reverts the column to a non-agentic column, and the fields retain the latest values the agent applied the last time it ran on the catalog.

![The option to select "Apply AI agent" for a catalog field.]({% image_buster /assets/img/ai_agent/edit_agent_column.png %}){: style="max-width:80%;"}

{% alert note %}
During the beta period, catalog agents are limited to processing input values up to 25 KB per row.
{% endalert %}

#### Define response fields

If your agent uses [fields]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents/#fields) as the output format, you can select the corresponding field from the agent for **Response Field** to use in the catalog field. 

Let's say you have an agent that adds product descriptions to a catalog with the following fields to structure the output format:

| Field name | Value |
| --- | --- |
| **description** | Text |
| **confidence_score_out_of_ten** | Number |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

You can add a field named **product_description** to a catalog and select **description** as the **Response Field** to populate the column with the agent's descriptions.

![The option to select "Apply AI agent" for a catalog field.]({% image_buster /assets/img/ai_agent/response_field.png %}){: style="max-width:80%;"}

You can also manually override the agentic cell by selecting **Edit Item** and updating the agentic description with your edits. To revert your edits back to the agentic description, select the refresh symbol in the cell.

### Error handling in catalogs  

- Failed catalog invocations do not retry.
- If the API call to the foundational model provider returns any error, such as an invalid API key error or a rate limit error, the field value does not update.
- You can review the agent's logs for details on failed runs.

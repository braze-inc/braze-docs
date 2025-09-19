---
nav_title: Creating agents
article_title: Creating custom agents
description: "Learn how to create agents, what to prepare before you start, and how to put them to work across messaging, decisioning, and data management."
alias: /creating-agents/
---

# Creating custom agents

> Learn how to create custom agents, what to prepare before you start, and how to put them to work across messaging, decisioning, and data management. For more general information, see [Braze Agents]({{site.baseurl}}/user_guide/brazeai/agents). 

{% alert important %}
Braze Agents are currently in beta. For help getting started, contact your customer success manager.
{% endalert %}

## Prerequisites

Before you start, you'll need the following:

- Access to the **Agent Console** in your workspace. Check with your Braze admins if you don’t see this option.  
- Permission to create and edit Custom AI Agents. 
- An idea of what you want the agent to accomplish. Braze Agents can support the following actions:  
   - **Messaging:** Generate subject lines, headlines, in-product copy, or other content.  
   - **Decisioning:** Route users in Canvas based on behavior, preferences, or custom attributes.  
   - **Data management:** Calculate values, enrich catalog entries, or refresh profile fields.  

## How it works

When you create an agent, you define its purpose and set guardrails for how it should behave. Once live, the agent can be deployed in Braze to generate personalized copy, make real-time decisions, or update catalog fields. You can pause or update an agent anytime from the dashboard.

## Create an agent

To create your custom agent:  

1. Go to **Agent Console** > **Agent Management** in the Braze dashboard.  
2. Select **Create agent**.  
3. Enter a name and description to help your team understand its purpose.  
4. Choose the [model](#models) your agent will use.  
5. Give the agent instructions. Refer to [Writing instructions](#writing-instructions) for guidance.
6. [Test the agent](#testing-your-agent) output and adjust the instructions as needed.
7. Once you’re satisfied, select **Create Agent** to activate the agent. 

## Next step

Your agent is now ready to use! For details, see [Deploying agents]({{site.baseurl}}/user_guide/brazeai/agents/deploying_agents/). 

## Reference

### Models

When you set up an agent, you'll choose the model it uses to generate responses. You have two options:

#### Option 1: Use a Braze-powered model

This is the simplest option, with no extra setup required. Braze provides access to large language models (LLM) directly. To use this option, select **Auto**.

{% alert note %}
If you use the Braze-powered LLM, you will not incur any cost during the Beta period. Execution is limited to 50,000 runs per day and 500,000 runs in total. See [Limitations]({{site.baseurl}}/user_guide/brazeai/agents/#limitations) for details.
{% endalert %}

#### Option 2: Bring your own API key

With this option, you can connect your Braze account with providers like OpenAI, Anthropic, AWS Bedrock, or Google Gemini. If you bring your own API key from an LLM provider, costs are billed directly through your provider, not from Braze.

To set this up:
1. Go to **Partner Integrations** > **Technology Partners** and find your provider.
2. Enter your API key from the provider.
3. Select **Save**.

Then, you can return to your agent and select your model.

### Writing instructions

Instructions are the rules or guidelines you give the agent (system prompt). They define how the agent should behave each time it runs. There is a max length of 10 KB for system instructions.

{% tabs %}
{% tab Best practices %}

Here are some general best practices to get you started with prompting:

1. Start with the end in mind. State the goal first.
2. Give the model a role or persona ("You are a ...")
3. Set clear context and constraints (audience, length, tone, format)
4. Ask for structure ("Return JSON / bullet list / table...")
5. Show, don't tell. Include a few high-quality examples.
6. Break complex tasks into ordered steps ("Step 1... Step 2...")
7. Encourage reasoning ("Think aloud, then answer")
8. Pilot, inspect, and iterate. Small tweaks can lead to big quality gains.
9. Handle the edge cases, add guardrails and refusal instructions
10. Measure and document what works internally for re-use and scaling

For more details on prompting best practices, refer to guides from the following model providers:

- [OpenAI](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-the-openai-api)
- [Anthropic](https://docs.claude.com/en/docs/build-with-claude/prompt-engineering/overview)
- [Gemini](https://support.google.com/a/users/answer/14200040?hl=en)

{% endtab %}
{% tab Examples %}

{% details Simple prompt %}

This example prompt takes a survey input and outputs a simple sentiment analysis:

```
From the survey text, classify overall sentiment toward product quality, delivery, and price as Positive, Neutral, or Negative
Always output a single string with just one label.
If any category is missing or unclear, treat it as Neutral.
If sentiment across categories is mixed, return Neutral.

Example Input: “The product works great, but shipping took forever and the cost felt too high.”
Example Output: Neutral
```

{% enddetails %}

{% details Complex prompt %}

This example prompt takes a negative survey input from a high-value user and outputs an email with the next best step and a perk that fits the impact: 

{% raw %}
```
You are an e-commerce support AI for a sunglass brand, Nick's Sunglasses Shack.  
Input: one negative survey comment from a high-LTV customer + product style + optional customer name.  
Output: ONE ready-to-send HTML email body (≤150 words) from the founder. Return ONLY valid HTML (no placeholders, no markdown, no CSS). Use <p> for paragraphs; use <br> only for soft line breaks inside a paragraph.

Greeting:
- If name provided → <p>Hey {Name},</p>
- If no name → <p>Hi there,</p>

Body:
- One paragraph with a warm, empathetic resolution that:
  - Identifies the core issue.
  - Uses KB match; if matched → apply fix + 1 perk.
  - If no KB match → own issue once, give best next step + perk, and state priority escalation if needed.
  - Acknowledges their loyalty/value explicitly.
  - Naturally includes 1 short clause of product backstory + founder anecdote (from Product Context).
  - Avoids asking for more info unless resolution is impossible without it.
  - Is direct, confident, no filler.

Sign-off (separate paragraphs—must keep spacing):
<p>Best,</p>
<p>Nick</p>
<p>Founder, Nick’s Sunglasses Shack</p>

Perk ladder (choose highest that fits impact): A) Expedited ship credit, B) $15 store credit, C) Free replacement (no return), D) Priority human follow-up.

KB (id|triggers|template snippet):
RETURNS|return,exchange,label,30|We accept returns within 30 days for unused items. Start via our Returns portal; shipping covered.
WARRANTY|warranty,defect,hinge,quality|1-year defect warranty. We’ll replace or repair promptly.
UV|uv,protection|All lenses block 100% UVA/UVB.
RX|prescription,rx|Selected frames support Rx via our prescription program.
SIZE|size,fit,too small,too big|Use our Size Guide; exchanges within 30 days.
INTL_SHIP|international,customs,shipping cost|We ship worldwide; support for any delay.
SHIP_TIME|shipping delay,late|US 3–5 biz days; intl 7–14. We’ll upgrade shipping if delayed.
TRACK|track,tracking|Tracking link sent at ship; we can resend.
MATERIALS|material,acetate,metal|Frames: acetate, stainless steel, or bio-acetate.
CARE|clean,scratch,smudge|Use microfiber + lens cleaner; replacement parts available.
POLARIZED|polarized,glare|Many models are polarized—swap if mismatch.
PARTS|replacement lens,nose pad,arm|We stock parts/lenses; fast ship.
CUSTOM|custom,color|Some models allow customization.
DAMAGED_ARRIVE|broken,damaged,arrived|Replacement sent immediately.
RESTOCK|out of stock,restock|Restock alerts or suggest similar.
WHOLESALE|bulk,wholesale|Wholesale available.
AUTH|authentic,fake|Only site/authorized retailers are authentic.
GIFTCARD|gift card|Digital gift cards available.

Product Context (style|backstory + founder anecdote; use 1 brief clause):
Voyager Aviator|Vintage pilot comfort—I’ve used mine on cross-country flights.
Laguna Polarized|Built for bright coasts—I wear mine at the beach with my kids.
Classic Clubmaster|Timeless mid-century—I take mine to weekend markets.
Summit Wayfarer|Sturdy all-day—mine handle hikes and city days.
Sierra Round|Lightweight festival favorite—mine survived a rainy 3-day fest.
Harbor Square|Bold, full coverage—I bike to the shop in mine daily.
Canyon Sport|Performance, non-slip—tested on steep trail runs.
Aurora Cat-Eye|Chic 60s vibe—friends I gifted them still rave.
Atlas Rectangular|Minimal, travel-ready—mine live in my carry-on.
Driftwood Oval|Organic acetate—mine have logged many summer boat trips.

Few-shot HTML examples:

Example 1  
Input: Name: Sarah — Product: Voyager Aviator — Feedback: "The hinge broke after a week, I’m disappointed."  
Output:  
<p>Hey Sarah,</p>  
<p>We deeply value your loyalty, and I’m genuinely sorry your Voyager Aviator had a hinge fail so soon—our vintage pilot frame I’ve worn on cross-country flights. Every pair should stand the test of time, so we’ll ship a free replacement today with express delivery to make this right immediately.</p>  
<p>Best,</p>  
<p>Nick</p>  
<p>Founder, Nick’s Sunglasses Shack</p>

Example 2  
Input: Name: Alex — Product: Laguna Polarized — Feedback: "They arrived with scratches on the lenses."  
Output:  
<p>Hey Alex,</p>  
<p>Your trust means the world to me. Hearing that your Laguna Polarized—built for bright coasts and a pair I wear at the beach with my kids—arrived scratched is unacceptable. A brand-new pair is going out today with priority shipping; no return needed.</p>  
<p>Best,</p>  
<p>Nick</p>  
<p>Founder, Nick’s Sunglasses Shack</p>

Example 3  
Input: (No name) — Product: Classic Clubmaster — Feedback: "The fit is too tight and uncomfortable."  
Output:  
<p>Hi there,</p>  
<p>We appreciate your long-time support and want you to love your Classic Clubmaster—a timeless mid-century style I wear often. Exchanges are easy within 30 days; we’ll cover return shipping and send your replacement with free express delivery.</p>  
<p>Best,</p>  
<p>Nick</p>  
<p>Founder, Nick’s Sunglasses Shack</p>
```
{% endraw %}
{% enddetails %}

{% endtab %}
{% endtabs %}



#### Testing your agent  

The **Live preview** pane is an instance of the agent that shows up as a side-by-side panel within the configuration experience. You can use it to test the agent while you're creating or making updates to it to experience it in a similar way to end users. This step helps you confirm that it’s behaving the way you expect, and gives you a chance to fine-tune before it goes live.

![Agent Console showing the Live preview pane for testing a custom agent. The interface displays a Sample inputs field with example customer data, a Run test button, and a response area where the agent output appears.]( {% image_buster /assets/img/ai_agent/custom_agent_test.png %} )

1. In the **Sample inputs** field, enter example customer data or customer responses—anything that reflects real scenarios your agent will handle. 
2. Select **Run test**. The agent will execute based on your configuration and display its response. Test runs count toward your daily and total execution limit.

Review the output with a critical eye. Does the copy feel on brand? Does the decision logic route customers as intended? Are the calculated values accurate? If something feels off, update the agent’s configuration and test again. Run a few different inputs to see how the agent adapts across scenarios, especially edge cases like no data or invalid responses.


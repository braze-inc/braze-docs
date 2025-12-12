---
nav_title: Survicate
article_title: Survicate
description: "This reference article outlines the partnership between Braze and Survicate, a customer feedback platform that helps you collect, analyze, and act on customer insights across multiple channels and throughout the user journey."
alias: /partners/survicate/
page_type: partner
search_tag: Partner

---

# Survicate

![An example of what a embedded HTML survey (first question) could look like in a Braze email.]({% image_buster /assets/img/survicate/survicate_asset_1.png %}){: style="float:right;max-width:40%;border:0; margin-left:8px;"}

> [Survicate](https://survicate.com/integrations/braze-survey/?utm_source=braze&utm_medium=integrations&utm_campaign=helpcenter) is a customer feedback platform that collects, analyzes, and acts on customer insights across multiple channels and throughout the user journey.  

_This integration is maintained by Survicate._

## About the integration

With the Braze and Survicate integration, you can embed surveys directly in Braze emails to increase response rates. Survey responses sync automatically with Braze user profiles as custom attributes or events. Real-time insights enable tracking and analysis of feedback alongside customer data to create targeted follow-ups.

## Use cases

Braze and Survicate work together to cover a range of feedback use cases, collecting actionable user insights and improving the customer experience:

- Measure customer satisfaction (such as CSAT, NPS, or CES)
- Collect product feedback
- Conduct user or market research
- Gather insights at critical stages of the customer journey
- Trigger personalized workflows and automate follow-up campaigns based on customer feedback

## Key features of the integration

The Survicate and Braze integration offers real-time data syncing, so the most up-to-date information from Survicate surveys is immediately available in Braze. Based on survey responses, you can use this data to take timely, personalized actions.

- **Send survey responses to Braze as custom user attributes**: Enrich Braze user profiles with data from survey responses.
- **Trigger custom events in Braze**: Use events based on survey answers to target specific groups or initiate follow-up campaigns.
- **Build detailed segments**: Create Braze segments using data from Survicate surveys to personalize your outreach further.

## Prerequisites

| Requirement | Description |
| ----------- | ----------- |
| Survicate account | You need a Survicate account to activate this integration. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integration

### Step 1: Create your survey in Survicate

1. In your Survicate panel, select **Create new survey**.
2. Choose your survey channel—**email, link, website, in-product, and mobile app surveys** are available. 
3. Design your survey from scratch, use the AI survey creator, or select from over 100 ready-to-use templates.

![Four options to create a survey: start from scratch, use a template, AI-assisted creation, and import questions.]({% image_buster /assets/img/survicate/survicate_asset_3.png %})

### Step 2: Identify respondents automatically with Braze emails

1. After your survey is ready, go to the **Configure** tab.
2. For *Identify respondents with*, select **Braze**. This automatically links responses to your Braze customer profiles, so there’s no need to ask for contact details in your survey.

![Braze is selected as the respondents.]({% image_buster /assets/img/survicate/survicate_asset_2.png %})

### Step 3: Connect the integration

1. Then, in the **Connect tab**, find Braze and select **Connect** to integrate. 
2. Insert your Braze account Workspace API Key and Braze Instance URL.

![Fields to enter the workspace API key and Braze instance URL.]({% image_buster /assets/img/survicate/image1.png %})

### Step 4: Share your survey

1. Next, in the **Share** tab, choose where you want to place your survey. Options include:
- **Direct link**: Copy the link to use in Braze as a button or hyperlink.
- **Embed first question**: Copy the HTML code to embed the first survey question directly in a Braze email body.
- **Launching a survey on your website or in-product**: Install the tracking code once, and set surveys live directly from the Survicate panel.

### Step 5: Add the survey to your Braze email campaign

1. In Braze, paste the survey link or HTML code into your email campaign’s content.
2. Start collecting feedback and track responses directly within Survicate.



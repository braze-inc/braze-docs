---
nav_title: Your Partner Page
page_order: 1

description: "This is the Google Search and SEO description that will appear, try to make this informative and concise, yet brief."
alias: /partners/your_partner_name/

page_type: partner
hidden: true
---

# [Partner Name]

> Welcome to the Partner Page Template! Here, you'll find everything you need to create your partner page. In this first section, you should describe the partner in the first paragraph in a sentence or two. Also, include a link to that partner's main site.

In the second paragraph, you should explore and explain the relationship between Braze and this partner. This paragraph should explain how Braze and this partner work together to tighten the bond between the Braze User and their customer. Explain the "elevation" that occurs when a Braze User integrates with or leverages this partner and their services.

## Requirements or Prerequisites

This section is all about what you need to integrate with the partner and start using their services. The best way to deliver this information is with a quick instructional paragraph that describes any non-technical important details of "need to know" information, like whether or not your integration will be subject to additional security checks or clearances. Then, you should use a chart to describe the technical requirements of the integration.

{% alert important %}
The requirements listed below are typical requirements you might need from Braze. We recommend using the attributed titling, origin, links, and phrasing as listed in the chart below. Be sure to adjust the description so that you know what each of these requirements is used to do.
{% endalert %}

| Requirement | Origin | Access | Description |
|---|---|---|---|
| Braze API Key | Braze | You will need to create a new API Key.<br><br>This can be created in the __Developer Console -> API Settings -> Create New API Key__ with __users.track__ permissions. | This description should tell you what to do with the Braze API Key. |
| Braze REST Endpoint | Braze | [Braze REST Endpoint List][1] | Your REST Endpoint URL. Your endpoint will depend on the Braze URL for your instance. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## [Type of Integration] Integration

This is where you break down the integration into steps. Do not just write endless paragraphs - these are technical documents that will be used by marketers and developers alike to get the integration up and running. Your only goal for this section is to write descriptive documentation that helps the Braze User get the job done. By 'Type of Integration' in the section title, we mean to indicate whether or not this is a Side-by-Side integration, server-to-server, or Out-of-the-Box. This enables you to have multiple Integration Sections if there is more than one way to integrate with this partner.

### Step 1: This Is a Short Description of Step One

Just break this down, including any code as necessary. Remember that you can offer several different sets of code - there's no need to only offer one way to integrate.

### Step 2: This Step Will Describe Images

You have the option to put images in your documentation, so we recommend you do and do so mindfully.

### Step 3: How Many Steps

Outline thorough usage of the integration - especially if it means inserting Liquid into our message composer.

## Customization

This is an __optional__ section. Here, you could outline any specific ways to customize your integration between the two partners.

## Using This Integration

This should describe how to use the integration - let your reader know if they need to push a few buttons or if they don't need to do anything at all after the integration.

### Step 1: This Is a Short Description of Step One

Just your typical step by step how to.

## Use Cases

This can be a critical part of your documentation. Though this is optional, this is a good place to outline typical or even novel use cases for the integration. This can be used as a way to sell or upsell the relationship - it provides context, ideas, and most importantly a way to visualize the capabilities of the integration.

[1]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints)

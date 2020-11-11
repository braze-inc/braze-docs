---
nav_title: Zendesk
page_order: 1

description: "Braze and Zendesk integration through webhooks. Send custom data from Braze to create a ticket in Zendesk Support Suite"
alias: /partners/zendesk/

page_type: partner
hidden: false
---

# Zendesk

[Zendesk Support Suite](https://www.zendesk.com/support-suite/) offers businesses to have natural conversations with their customers through an omnichannel support, whether it’s email, chat, voice or social messaging apps. ZSS values customer support through tracking and prioritising interactions, allowing businesses to have a unified view of the customer through pulling in previous history too. Powerful tools such as a streamlined ticketing system allows businesses to reach out directly to customers with a personalised approach. 

## Requirements

This section is all about what you need to integrate with the partner and start using their services. The best way to deliver this information is with a quick instructional paragraph that describes any non-technical important details of "need to know" information, like whether or not your integration will be subject to additional security checks or clearances. Then, you should use a chart to describe the technical requirements of the integration.


| Requirement | Origin | Access | Description |
|---|---|---|---|
| Zendesk Admin | Zendesk | You will need to create a Zendesk API token.| The Zendesk API token is necessary to be able to send requests from Braze to the Zendesk Ticket endpoint. |
| Braze REST Endpoint | Braze | [Braze REST Endpoint List][1] | Your REST Endpoint URL. Your endpoint will depend on the Braze URL for your instance. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Braze → Zendesk Integration
### Create tickets in Zendesk directly from Braze Campaign/Canvas

Using this webhook template, customers can easily automate the creation of support tickets as a result of a user’s journey or message engagement within Braze. For example, you may want to automatically create a support ticket when a user receives a Braze in-app message that asks “Do you like our app?” and the user clicks “No”, so that your support team can reach out and offer help to satisfy the customer. 


### Step 1: Create a Webhook

Just break this down, including any code as necessary. Remember that you can offer several different sets of code - there's no need to only offer one way to integrate.

### Step 2: This Step Will Describe Images

You have the option to put images in your documentation, so we recommend you do and do so mindfully.

### Step 3: How Many Steps

Outline thorough usage of the integration - especially if it means inserting liquid into our message composer.

## Customization

This is an __optional__ section. Here, you could outline any specific ways to customize your integration between the two partners.

## Using This Integration

This should describe how to use the integration - let your reader know if they need to push a few buttons or if they don't need to do anything at all after the integration.

### Step 1: This Is a Short Description of Step One

Just your typical step by step how to.

## Use Cases

This can be a critical part of your documentation. Though this is optional, this is a good place to outline typical or even novel use cases for the integration. This can be used as a way to sell or upsell the relationship - it provides context, ideas, and most importantly a way to visualize the capabilities of the integration.

[1]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints)

---
nav_title: Dixa
article_title: Dixa
description: "This article outlines the partnership between Braze and Dixa."
alias: /partners/dixa/
page_type: partner
search_tag: Partner

---

# Dixa

> [Dixa](https://www.dixa.com/) is a customer service platform designed to enhance support experiences by unifying communication channels such as chat, email, phone, and social media into a single interface. It helps businesses improve customer satisfaction and efficiency through intelligent routing, automation, and real-time performance insights.

The Braze and Dixa integration offers a better view on all your users by providing customer service agents with real-time Braze data.

## Prerequisites

Before you start, you'll need the following:

| Prerequisite          | Description                                                                                                                                                       |
|-----------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| A Dixa account        | A Dixa admin account is required to take advantage of this partnership.                                                                                           |
| A Braze REST API key  | A Braze REST API key with `users.export.ids` and `email.status` permissions.<br><br> This can be created in the Braze dashboard from **Settings** > **API Keys**. |
| A Braze REST endpoint | [Your REST endpoint URL]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). Your endpoint will depend on the Braze URL for your instance.              |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Use cases

Surface Braze data into the customer service agent view while communicating with your users on different communication channels, such as email, messenger, or chat.

## Integration

You must be a Dixa administrator to configure integrations within Dixa. For the Braze integration, in Dixa, go to **Settings** > **Integrations** > **Braze**.

![]({% image_buster /assets/img/dixa/dixa-create-integration.png %}){: style="width:450px;"}

### Step 1: Create the integration in Dixa

On the **Create Braze widget** page, fill in the following required fields to create the integration:

- **Widget name:** This is the name of the integration that will later be used in the conversation sidebar as the title.
- **API URL:** This is the Braze REST API endpoint URL for your instance.
- **API Key:** This is the Braze API key you created in the prerequisites.

### Step 2: Configure the integration

Next, configure the Braze and Dixa integration. Choose from the following options to adjust the view of the Braze widget in the conversation sidebar.

#### Show the widget in the conversation sidebar

This setting shows or hides the whole integration within the conversation sidebar in Dixa. 

If you're actively configuring the integration, we recommend turning this off while you fill in the required fields. When you're finished configuring, you can turn it on again and Dixa agents can use the integration.

#### Display customer details

Choose to show or hide the user's details. The details contain data about location, email, phone number, email subscription state, push notification subscription state, and the duration of the membership in Braze. 

#### Display the button to change the email subscription state

The buttons are based on one of the three subscription states from Braze: `subscribed`, `opted-in`, and `unsubscribed`. If a user is `subscribed`, the agent can choose to `opt-in` or `unsubscribe`. When a user is `opted-in` or `unsubscribed`, it's only possible to switch between the two.

#### Display a list of custom attributes

Choose to show or hide the user's custom Braze attributes.

#### Display a list of custom events

Choose to show or hide the user's custom Braze events.

#### Display a list of purchases

Choose to show or hide a list products purchased by the user. Here, you can see how many times it was purchased. To view the first and last purchase date, hover above the item. 

### Example integration

The following shows an example of the integration:

![The Braze and Dixa integration in Dixa that displays a user's email subscription state, custom attributes, custom events, and purchases.]({% image_buster /assets/img/dixa/dixa-braze-integration.png %}){: style="width:350px;"}


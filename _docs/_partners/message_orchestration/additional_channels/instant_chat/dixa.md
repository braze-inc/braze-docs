---
nav_title: Dixa
article_title: Dixa
description: "This article outlines the partnership between Braze and Dixa."
alias: /partners/dixa/
page_type: partner
search_tag: Partner

---

# Dixa

> Dixa is a customer service platform designed to enhance support experiences by unifying communication channels such as chat, email, phone, and social media into a single interface. It helps businesses improve customer satisfaction and efficiency through intelligent routing, automation, and real-time performance insights. [Visite us at dixa.com](https://www.dixa.com/)

The partnership between Dixa and Braze offers our customers a better 360 view on all end-customers by providing customer service agents with real-time Braze data.


## Prerequisites

Before you start, you'll need the following:

|Prerequisite|Description|
|---|---|
| A Dixa account | A Dixa admin account is required to take advantage of this partnership. |
| A Braze REST API key | A Braze REST API key with `users.export.ids` and `email.status` permissions.<br><br> This can be created in the Braze dashboard from **Settings** > **API Keys**. |
| A Braze REST endpoint | [Your REST endpoint URL]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). Your endpoint will depend on the Braze URL for your instance. |
{: .reset-td-br-1 .reset-td-br-2}

{% alert note %}
If you are using the [older navigation]({{site.baseurl}}/navigation), you can create an API key at **Developer Console** > **API Settings**.
{% endalert %}


## Use cases

Surface Braze data into the customer service agent view when they are communicating with end-customers on different communication channels (e.g. email, messenger, chat etc..).


## Integrating Dixa with Braze

You must be a Dixa (System-) Administrator to configure integrations within Dixa.

You will find the Braze integration in Dixa under _Settings > Integrations > Braze_.

![][1]{: style="width:450px;"}

### Step 1: Create the integration

On the _Create Braze widget_ page, you must fill in the following required fields in order to create the integration.

* `Widget name` This is the name of the integration that will later be used in the conversation sidebar as title.
* `API URL` This is the Braze REST API endpoint URL for your instance.
* `API Key` This is the Braze API key you created in the prerequisites.

### Step 2: Configure the integration

You have the following options to fine tune the view of the Braze widget in the conversation sidebar.

#### Show the widget in the conversation sidebar
This setting basically shows or hides the whole integration within Dixas conversation sidebar. If you are actively configuring the integration, we recommend turning this off while you fill in the required fields. You can toggle it on when everything is configured and agents can use the integration.

#### Display customer details
Choose to show or hide the customer's details. The details contain data about since when the customer is member in Braze, location, email, phone number, email subscription state, and push notification subscription state.

#### Display the button to change the email subscription state
The button/s are based on one of the three subscription states from Braze: `Subscribed`, `Opted-In`, and `Unsubscribed`. If a customer is `Subscribed`, the agent can choose to `Opt-In` or `Unsubscribe`. When a customer is `Opted-In` or `Unsubscribed`, it's only possible to switch between the two.

#### Display a list of custom attributes
Choose to show or hide the customer's custom Braze attributes.

#### Display a list of custom events
Choose to show or hide the customer's custom Braze events.

#### Display a list of purchases
Choose to show or hide a list products purchased by the customer. On the right side it shows how many times it was purchased. By hovering above the item, a first and last purchase date appears.


## The integration in action

![][2]{: style="width:350px;"}


[1]: {% image_buster /assets/img/dixa/dixa-create-integration.png %}
[2]: {% image_buster /assets/img/dixa/dixa-braze-integration.png %}

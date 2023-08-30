---
nav_title: Overview
article_title: Data Transformation Overview
page_order: 0
page_type: reference
description: "This reference article provides an overview of data transformation, frequently asked questions, and product limitations."
---

# Data transformation overview

> Data transformation allows you to build and manage webhook integrations to automate data flow from external platforms into Braze user profiles. This integrated user data can then power even more sophisticated marketing use cases.

Data transformation is a low-code solution, and you can be up and running in minutes, even if you have very little coding experience. This feature can help expedite your data integration and replace your team’s dependency on manual API calls, third-party integration tools, or even customer data platforms.

## How it works

Many modern-day platforms can send webhooks, real-time notifications, when something happens. Data transformation with Braze builds on these external webhooks by providing a Braze address to send those webhooks to.

To do this, you will have to write transformation code to map the contents of those incoming webhooks and create an output that matches Braze’s `/users/track` schema. You have full flexibility in what you want to use from the webhook, and how you want the data represented as Braze user attributes, events, and purchases. 

Lastly, you must enable your transformation and send webhooks from your external platform. Your transformation will apply to every webhook we receive, and your integration is complete.

{% details More on webhooks %}
Webhooks are real-time notifications sent via an HTTP POST request to a specific destination. Webhooks are often used to send data from one point to another, in which the webhook can pass through data about an action that has occurred and who is involved in that action.

For example, a survey platform can send a webhook to a destination of your choice whenever a survey response to an online form is received. Or, a customer service platform can send a webhook to a destination of its choice whenever a customer service ticket is created.
{% enddetails %}

## Limitations

The following table describes the usage limitations that apply for each version of data transformation.

| Limitation Area | Free Version | Data Transformation Pro |
|----|----|----|
| **Active transformations** | Up to 5 per company | Up to 55 per company |
| **Monthly incoming requests** | 300,000 incoming requests per minute | 10,300,000 incoming requests per minute |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

{% alert important %}
To request an upgrade to Data Transformation Pro, contact your Braze account manager or select the **Request Upgrade** button in the Braze dashboard.
{% endalert %}

### Rate limits

The rate limit for data transformation is 1,000 incoming requests per minute. If you have Data Transformation Pro and need a higher rate limit, contact your Braze account manager.

## Frequently asked questions

{% details What gets synced with data transformation? %}
Any data the external platform makes available in a webhook can be synced to Braze. The more an external platform sends via webhooks, the more options for choosing what gets synced.
{% enddetails %}

{% details I’m a marketer. Do I need developer resources to use data transformation? %}
While we would love for developers to use this feature as well, you don’t need to be one to use this! Marketers can also successfully set up transformations without developer resources.
{% enddetails %}

{% details Can I still use data transformation if my external platform only gives an email address as an identifier? %}
Yes. Data transformation early access users will also be granted early access to the [`/users/track` endpoint]({{site.baseurl}}/api/endpoints/user_data/post_user_track/#example-request-for-updating-a-user-profile-by-email-address) to update a user profile by email address.

Use `email` as your identifier property in the transformation code instead of `external_id` or `braze_id`. The example [transformation code](#example-transformation-code) uses this functionality.

{% alert note %}
Data transformation early access users who started before April 2023 may be familiar with a `get_user_by_email` function that helped with this use case. That function has been deprecated.
{% endalert %}
{% enddetails %}

{% details Does data transformation consume data points? %}
In most cases, yes. Data transformation eventually creates a `/users/track` call that writes the attributes, events, and purchases you want. These will consume data points in the same way as if the `/users/track` call was made independently. You have control over how many data points will be written based on how you write your transformation.
{% enddetails %}

{% details How can I get help setting up my use case or with my transformation code? %}
Contact your Braze account manager for additional assistance.
{% enddetails %}

[1]: {% image_buster /assets/img_archive/data_transformation1.png %}
[2]: {% image_buster /assets/img/data_transformation/data_transformation1.jpg %}
---
nav_title: Fresh Relevance
article_title: Fresh Relevance
description: "This reference article outlines the partnership between Braze and Fresh Relevance, a versatile personalization platform that allows you to include relevant products in your Braze campaigns and Canvases."
alias: /partners/fresh_relevance/
page_type: partner
search_tag: Partner

---

# Fresh Relevance

> [Fresh Relevance](https://www.freshrelevance.com/) is a versatile personalization solution that empowers commerce-driven businesses to create customized cross-channel experiences with ease. The platform saves you time, integrates with your tech stack, and empowers you to deliver conversion-boosting personalized customer experiences across your website, app, emails, SMS, and ads, without relying on your IT team.

The Braze and Fresh Relevance integration allows you to:
* Send advanced triggered email campaigns such as price drop, back in stock, multi-stage browse, or cart abandoned messages.
* Include personalized content in triggered emails, such as product recommendations based on the customer's browsed product or items within the same category.
* Personalize bulk email campaigns with AI-driven recommendations, countdown times, real-time weather forecasts, social media feeds, and more.
* Grow the email database with new contacts collected through data capture pop-ups.
* Identify website visitors that arrive from a Braze email link.

## Prerequisites

| Requirement | Description |
|-------------| ----------- |
| Fresh Relevance account  | A Fresh Relevance account is required to take advantage of this partnership. |
| Braze REST API key | A Braze REST API key with permissions sufficient for the endpoints listed below. <br><br> This can be created in the Braze dashboard from **Settings** > **API Keys**. |
| Braze REST endpoint | [Your REST endpoint URL]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). Your endpoint will depend on the Braze URL for your instance. |
| Braze campaign ID | The default Braze campaign that you want to use to send emails. |
{: .reset-td-br-1 .reset-td-br-2}

## Integration

To set up the integration in Fresh Relevance, you must create a Braze channel in **Messaging Channels** and use the channel in appropriate Fresh Relevance triggers or content as required. 

For step-by-step instructions, log in to Fresh Relevance and follow their [documentation](https://admin.freshrelevance.com/help/esp_instructions/?esp_class_name=EspBraze).

The Fresh Relevance system will communicate with Braze using the API key provided. A full integration makes use of the following Braze API endpoints:

* [`/users/alias/new`]({{site.baseurl}}/api/endpoints/user_data/post_user_alias/)
* [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)
* [`/campaigns/triggers/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/)
* [`/users/export/ids`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/)
* [`/subscription/status/get`]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_group_status/)
* [`/v2/subscription/status/set`]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status_v2/)


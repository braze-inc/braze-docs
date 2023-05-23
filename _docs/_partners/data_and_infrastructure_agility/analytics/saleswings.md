---
nav_title: SalesWings
article_title: SalesWings
page_order: 1

description: "This reference article outlines the partnership between Braze and SalesWings, an analytics platform, that helps you track scoring and grading, sales insights and alerts, marketing alignment, and attribution reporting."
alias: /partners/saleswings/

page_type: partner
search_tag: Partner
hidden: true
layout: dev_guide
---

# SalesWings

> [SalesWings][1], an analytics platform built for marketing and sales teams, helps you manage account website tracking, scoring and grading, sales insights and alerts, marketing alignment, and attribution reporting.

The Braze and SalesWings integration allows you to sync data across the two platforms as a [flexible way][3] to qualify leads with lead scoring and lead grading capabilities.

## Use cases

With the Braze and SalesWings integration, users can align different teams by qualifying leads and creating different visualizations to gain insights from the various messages they have created.

{% tabs %}
{% tab Visualize data %}
View qualified leads and accounts based on profile data by sending attribute data from Braze directly to SalesWings with key insights on detailed engagement with Braze emails, other marketing messaging, and message engagement.

{% endtab %}
{% tab Automated reporting %}
Build automated reporting with leads, contacts, accounts and opportunities, based on web engagement data and Braze campaign engagement. For instance, you can surface a list of hot leads to a sales team or representative, with everyone who clicked on a specific email campaign, or performed a specific action in your app, or on your website.

![Example dashboard linked to Braze email and marketing engagement within Salesforce, focusing on the impact of Braze campaigns on sales results and outcomes.]({{site.baseurl}}/assets/img/saleswings/saleswings_email_campaign_attribution_dashboard.png)

{% endtab %}
{% endtabs %}

## Prerequisites

| Requirement | Description |
| ----------- | ----------- |
| SalesWings account | A [SalesWings][1] account is required to take advantage of this partnership. |
| Braze REST API key | A Braze REST API key with `users.export.ids` permissions. <br><br> This can be created within the **Braze Dashboard > Developer Console > REST API Key > Create New API Key**. |
| Braze REST endpoint | [Your REST endpoint URL][2]. Your endpoint will depend on the Braze URL for your instance. |
| Segment.com account (optional) | If you are a Segment.com user, you can send all lead engagement and profile data along with identify events via Segment.com for lead profiling. |
{: .reset-td-br-1 .reset-td-br-2}

## Integration

### Requirements

In SalesWings, set up website tracking and identification of leads prior to integration.

### Step 1: Create your Braze API key

In Braze, go to the **Developer Console** and select the **API Settings** tab. Select **Create New API Key** and ensure the following permission is added: `users.export.ids`.  

![The SalesWings Braze Integration section with the Braze API endpoint field highlighted.][12]

### Step 2: Add key to SalesWings

Go to the [SalesWings Settings page][13] and expand the **Braze Integration** section.

![The Braze Integration section of the SalesWings Settings page.][14]

Copy the value of the **Identifier** column for the newly created key and paste into the **Braze API key** field of the SalesWings **Braze Integration** section.

Add your Braze API endpoint as described in [API and SDK endpoints article][16], and enter it in the **Braze API endpoint** field. Copy the value of the **REST Endpoint** column and enter it in the **Braze API endpoint** field in the SalesWings **Braze Integration** section.

Then, click **Save Changes** in the SalesWings settings.

## Using this integration 

To trigger lead scoring and the creation of sales insights, SalesWing must identify a lead on your website or app. This can occur in the following ways:

- **Form submissions:** When a lead, also known as the user, submits a web form, SalesWings will automatically identify all of your web form types (i.e. login, download, contact us, etc.), and resolve the identity of a lead when they submit a form. 
- **URL clicks with a Braze ID or external ID:** A lead clicks on a Braze marketing action, typically email clicks, banner clicks, or similar, leading to a page which you are tracking with SalesWings.
- **Sales email tracking via Gmail and Outlook plug-ins (optional):** If you decide to empower your sales representative with email tracking plugins, they can trigger full website tracking of leads by sending trackable links.
- **Segment.com identify event (optional):** If you are a Segment.com user, you can also resolve the identity of a lead with Segment.com integration.

### Identifying leads from URL clicks

You can identify leads automatically when they click on a "trackable" URL (e.g., via email blasts, banners with URLs). In order to make a URL trackable, there are two ways to modify your website URLs in your emails, banners, or SMS by adding the parameter and ID at the end of your links.

1. Appending `?braze_id=` followed by {% raw %}`{{${braze_id}}}`{% endraw %} 
  - **Link example:** {% raw %}`https://www.your-website.com?braze_id={{${braze_id}}}`{% endraw %}

2. Appending `?br_user_id=` followed by {% raw %}`{{${user_id}}}`{% endraw %}
  - **Link example:** {% raw %}`https://www.client-website.com?br_user_id={{${user_id}}}`{% endraw %}

The `braze_id` variable is set to an identifier of the user generated by Braze and is always available. The `br_user_id` variable is set to the identifier of the user in your system and may be missing in certain scenarios (e.g., for anonymous users created by the Braze SDK). If both `braze_id` and `br_user_id` are used in a link, SalesWings will only consider the `braze_id` parameter.

For configuration and further troubleshooting, contact the [SalesWings services team][1] for onboarding support.


[1]: https://www.saleswingsapp.com/?utm_source=braze&utm_campaign=technicaldocs
[2]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints
[3]: https://www.saleswingsapp.com/braze-lead-scoring-and-sales-insights?utm_source=braze&utm_campaign=technicaldocs
[4]: {% image_buster /assets/img/saleswings/example_lead_scoring_builder_braze_lead_scoring.png %}
[5]: {% image_buster /assets/img/saleswings/prioritized_lead_or_contact_list_braze_lead_scoring.png %}
[6]: {% image_buster /assets/img/saleswings/prioritized_account_list_braze_lead_scoring.png %}
[7]: {% image_buster /assets/img/saleswings/marketo_sales_insights_alternative_for_braze.png %}
[8]: {% image_buster /assets/img/saleswings/smart_watch_alerts.png %}
[9]: {% image_buster /assets/img/saleswings/saleswings_email_campaign_attribution_dashboard.png %}
[10]: https://www.saleswingsapp.com/schedule-a-demo?utm_source=braze&utm_campaign=technicaldocs
[11]: https://support.saleswingsapp.com/en/collections/3285135-1-implementing-saleswings-tracking-script
[12]: {% image_buster /assets/img/saleswings/creating_api_key_in_braze_lead_scoring.png %}
[13]: https://helium.saleswings.pro/settings
[14]: {% image_buster /assets/img/saleswings/saleswings_braze_lead_scoring_integration_settings.png %}
[15]: {% image_buster /assets/img/saleswings/braze_api_key_lead_scoring.png %}
[16]: https://www.braze.com/docs/user_guide/administrative/access_braze/sdk_endpoints
[17]: {% image_buster /assets/img/saleswings/braze_api_endpoint_for_lead_scoring.png %}
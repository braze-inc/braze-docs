---
nav_title: SalesWings
article_title: SalesWings
description: "This reference article outlines the partnership between Braze and SalesWings, an analytics platform, that helps you track scoring and grading, sales insights and alerts, marketing alignment, and B2B attribution reporting."
alias: /partners/saleswings/
page_type: partner
search_tag: Partner

---

# SalesWings

> [SalesWings][1] is a B2B SaaS lead profiling add-on, built for marketing and sales teams, which helps manage lead and account qualification through lead scoring and grading, sales insights and alerts, marketing alignment, and B2B attribution reporting, along with a tight Salesforce CRM integration.

SalesWings allows marketing teams and marketing operations managers to qualify leads and accounts for their sales teams, which is essential for sales and marketing alignment and sales efficiency. Furthermore, SalesWings together with braze provides you with the ability to surface a lead’s customer journey and braze marketing campaign engagement data to sales reps, allowing to increase lead qualification rates through more educated conversations.

## Prerequisites
 
| Requirement | Description |
| ----------- | ----------- |
| SalesWings account | A [SalesWings][1] account is required to take advantage of this partnership. |
| Braze REST API key | A Braze REST API key with `users.export.ids` permissions. <br><br> This can be created within the **Braze Dashboard > Developer Console > REST API Key > Create New API Key**. |
| Braze REST endpoint | [Your REST endpoint URL][2]. Your endpoint will depend on the Braze URL for your instance. |
| Segment.com account (optional) | If you are a Segment.com user, you can send all lead engagement and profile data and identify events via Segment.com for lead profiling. |
{: .reset-td-br-1 .reset-td-br-2}

## Use cases

{% tabs %}
{% tab Lead Scoring %}

SalesWings provides braze customers with [flexible way to qualify leads, contacts and accounts with state-of-the-art lead scoring](https://www.saleswingsapp.com/braze-lead-scoring-and-sales-insights?utm_source=braze&utm_campaign=technicaldocs) and lead grading capabilities. All your lead qualification data is natively pushed to Salesforce CRM, as well as other systems where you want to manage and report on leads, contacts, accounts and opportunities.

![Example of a simple, click-not-code lead scoring model in SalesWings]({% image_buster /assets/img/saleswings/example_lead_scoring_builder_braze_lead_scoring.png %})

_Example of a simple, click-not-code lead scoring model in SalesWings_
{% endtab %}
{% tab Sales and Marketing Alignment %}
SalesWings allows marketing teams to track, qualify and hand-off marketing-qualified leads to your sales teams. All SalesWings data is natively pushed to Salesforce, and can be leveraged to fine-tune any existing process, or create new processes via lists, reports, flows, and more.

![Example of how SalesWings lead scoring prioritizes a list of leads or contacts natively inside Salesforce]({% image_buster /assets/img/saleswings/prioritized_lead_or_contact_list_braze_lead_scoring.png %})

_Example of how SalesWings lead scoring prioritizes a list of leads or contacts natively inside Salesforce_

![Example of how SalesWings lead scoring prioritizes a list of accounts natively inside Salesforce]({% image_buster /assets/img/saleswings/prioritized_account_list_braze_lead_scoring.png %})

_Example of how SalesWings lead scoring prioritizes a list of accounts natively inside Salesforce_
{% endtab %}
{% tab Lead and Account Grading %}
SalesWings allows braze customers to qualify leads and accounts based on profile data (typically CRM data). This is also referred to as “lead grading”, “fit scoring” or “firmographic scoring”. Braze customers can send attribute data directly to SalesWings, and SalesWings has the ability to read any Salesforce CRM standard or custom objects data and records, for a holistic profile scoring.
{% endtab %}
{% tab Sales Insights for Sales Reps %}
SalesWings enables you to show your sales reps sales insights about their leads, contacts and accounts (Marketo Sales Insights alternative). Essentially, you can surface any braze and web engagement data to your sales team. The insights are natively embedded into Salesforce CRM, and can also be pushed to other CRM’s or systems, or via a braze email as a “sales alert”.

![Example of sales insights view for sales reps inside Salesforce (also available for other CRM systems)]({% image_buster /assets/img/saleswings/marketo_sales_insights_alternative_for_braze.png %})

_Example of sales insights view for sales reps inside Salesforce (also available for other CRM systems)_
{% endtab %}
{% tab Sales Alerts %}
SalesWings offers native email as well as Slack alerts, and you can set up report subscriptions in Salesforce that your sales team can access to get daily, weekly and monthly email reports. Furthermore, through a Zapier integration, you can build additional work-flows based on SalesWings lead qualification data.

![Example of sales alert via Slack channel]({% image_buster /assets/img/saleswings/smart_watch_alerts.png %})

_Example of sales alert via Slack channel_
{% endtab %}
{% tab Reporting in Salesforce CRM %}
Through SalesWings integration with Salesforce, you can build automated reporting with leads, contacts, accounts and opportunities, based on web engagement data and braze campaign engagement. For instance, you can surface a list of hot leads to a sales team / rep, with everyone who clicked on a specific email campaign, or performed a specific action in your app, or on your website.

![Example dashboard linked to braze email & marketing engagement within Salesforce, looking at impact of braze campaigns on sales results and outcomes]({% image_buster /assets/img/saleswings/saleswings_email_campaign_attribution_dashboard.png %})

_Example dashboard linked to braze email & marketing engagement within Salesforce, looking at impact of braze campaigns on sales results and outcomes_
{% endtab %}
{% endtabs %}

## Integration

### Step 1: SalesWings account and configuration

Please [schedule a demo][4] with the friendly SalesWings team to learn more about SalesWings.

### Step 2: Installing behavioral tracking on your website / app

Currently there are 2 ways for you to collect behavioral data in SalesWings for lead scoring and sales insights:
* [Deploy the SalesWings tracking Javascript][5] on the websites and apps where you want to track and identify leads
* Send behavioral lead activity data (and lead profile data) via SalesWings integration with Segment.com

### Step 3: Connecting SalesWings to braze

Go to the [**SalesWings Settings** page][6] and expand the **Braze Integration** section.

![The Braze Integration section of the SalesWings Settings page.][7]

Copy the value of the **Identifier** column for the newly created key and paste it into the **Braze API key** field of the SalesWings **Braze Integration** section.

Add your Braze API endpoint as described in [API and SDK endpoints article][8], and enter it in the **Braze API endpoint** field. Copy the value of the **REST Endpoint** column and enter it in the **Braze API endpoint** field in the SalesWings **Braze Integration** section.

Then, click **Save Changes** in the SalesWings settings.

### Step 4: Configuring SalesWings lead scoring for braze, CRM integration, and more

Please consult SalesWings services team for full on-boarding support via the [website][1].

## Using this integration 

To trigger lead scoring and the creation of sales insights, SalesWings must identify a user on your website or app. This can occur in the following ways:

- **Form submissions:** When a user submits a web form, SalesWings will automatically identify all of your web form types (i.e., login, download, contact us, etc.) and resolve the identity of a user when they submit a form. 
- **URL clicks with a Braze ID or external ID:** A user clicks on a Braze marketing action, typically email clicks, banner clicks, or similar, leading to a page you are tracking with SalesWings.
- **Sales email tracking via Gmail and Outlook plugins (optional):** If you decide to empower your sales representative with email tracking plugins, they can trigger full website tracking of users by sending trackable links.
- **Segment.com identify event (optional):** If you are a Segment.com user, you can also resolve the identity of a user with Segment.com integration.

### Identifying users from URL clicks

You can identify users automatically when they click on a trackable URL (e.g., email blasts, banners with URLs). To make a URL trackable, there are two ways to modify your website URLs in your emails, banners, or SMS by adding the parameter and ID at the end of your links.

1. Appending `?braze_id=` followed by {% raw %}`{{${braze_id}}}`{% endraw %} 
  - **Link example:** {% raw %}`https://www.your-website.com?braze_id={{${braze_id}}}`{% endraw %}<br><br>

2. Appending `?br_user_id=` followed by {% raw %}`{{${user_id}}}`{% endraw %}
  - **Link example:** {% raw %}`https://www.client-website.com?br_user_id={{${user_id}}}`{% endraw %}

The `braze_id` variable is set to an identifier of the user-generated by Braze and is always available. The `br_user_id` variable is set to the user's identifier in your system and may be missing in certain scenarios (e.g., for anonymous users created by the Braze SDK). If both `braze_id` and `br_user_id` are used in a link, SalesWings will only consider the `braze_id` parameter.

For configuration and further troubleshooting, contact the [SalesWings services team][1] for onboarding support.

[1]: https://www.saleswingsapp.com/?utm_source=braze&utm_campaign=technicaldocs
[2]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints
[3]: https://www.saleswingsapp.com/braze-lead-scoring-and-sales-insights?utm_source=braze&utm_campaign=technicaldocs
[4]: https://www.saleswingsapp.com/schedule-a-demo?utm_source=braze&utm_campaign=technicaldocs
[5]: https://support.saleswingsapp.com/en/collections/3285135-1-implementing-saleswings-tracking-script
[6]: https://helium.saleswings.pro/settings
[7]: {% image_buster /assets/img/saleswings/saleswings_braze_lead_scoring_integration_settings.png %}
[8]: {{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints

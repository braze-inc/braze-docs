---
nav_title: SalesWings
article_title: SalesWings
description: "This reference article outlines the partnership between Braze and SalesWings. SalesWings is a sales and marketing operations solution for Braze that helps you qualify leads and accounts, and provides sales insights and alerts inside CRM like Salesforce, as well as B2B attribution reporting. You can leverage interests and engagements inside Braze for personalization in Canvas and segmentation. SalesWings also provides a way to generate leads from a website, similar to Digioh."
alias: /partners/saleswings/
page_type: partner
search_tag: Partner

---

# SalesWings

> [SalesWings](https://www.saleswingsapp.com/?utm_source=braze&utm_campaign=technicaldocs) is a B2B SaaS sales and marketing operations solution that helps manage lead and account qualification through holistic lead scoring and grading and provides sales insights and alerts and B2B attribution reporting, along with a tight Salesforce CRM integration.  A website engagement add-on, similar to Digioh, allows you to generate leads on the website. You can leverage the interests and engagements inside Braze for personalization in Canvas and segmentation.

_This integration is maintained by SalesWings._

## About the integration

SalesWings allows marketing teams and marketing operations managers to qualify leads and accounts for their sales teams, essential for sales and marketing alignment and operational efficiency. Furthermore, SalesWings, together with Braze, can surface a lead’s and account’s full customer journey and Braze marketing campaign engagement data to sales representatives, allowing you to increase lead qualification rates through more educated conversations. SalesWings identifies needs and interests along with other signals, allowing the hand-off of qualified buyers to sales teams inside your CRM in an automated manner. You can use the identified needs, interests, and sales-readiness as Braze user attributes for personalization and segmentation.

## Prerequisites
 
| Requirement | Description |
| ----------- | ----------- |
| SalesWings account | A [SalesWings](https://www.saleswingsapp.com/?utm_source=braze&utm_campaign=technicaldocs) account is required to take advantage of this partnership. |
| Braze REST API key | A Braze REST API key with `users.export.ids` permissions (and `users.track` if using the SalesWings insights push feature). <br><br> This can be created in the Braze dashboard from **Settings** > **API Keys**. |
| Braze REST endpoint | [Your REST endpoint URL]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). Your endpoint will depend on the Braze URL for your instance. |
| Segment.com account (optional) | If you are a Segment.com user, you can send all lead engagement and profile data and identify events via Segment.com for lead profiling. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Use cases

{% tabs %}
{% tab Lead and Account Scoring %}

SalesWings provides Braze customers with [a flexible way to qualify leads, contacts, and accounts with state-of-the-art lead scoring](https://www.saleswingsapp.com/braze-lead-scoring-and-sales-insights?utm_source=braze&utm_campaign=technicaldocs) and lead grading capabilities. All your lead qualification data is natively pushed to Salesforce CRM and other systems where you want to manage and report on leads, contacts, accounts, and opportunities.

![Example of a simple, click-not-code lead scoring model in SalesWings]({% image_buster /assets/img/saleswings/example_lead_scoring_builder_braze_lead_scoring.png %})

_Example of a simple, click-not-code lead scoring model in SalesWings_
{% endtab %}
{% tab Sales and Marketing Alignment %}
SalesWings allows marketing teams to track, qualify and hand off marketing-qualified leads to your sales teams. All SalesWings data is natively pushed to Salesforce, and can be leveraged to fine-tune any existing process, or create new processes via lists, reports, flows, and more.

![Example of how SalesWings lead scoring prioritizes a list of leads or contacts natively inside Salesforce]({% image_buster /assets/img/saleswings/prioritized_lead_or_contact_list_braze_lead_scoring.png %})

_Example of how SalesWings lead scoring prioritizes a list of leads or contacts natively inside Salesforce_

![Example of how SalesWings lead scoring prioritizes a list of accounts natively inside Salesforce]({% image_buster /assets/img/saleswings/prioritized_account_list_braze_lead_scoring.png %})

_Example of how SalesWings lead scoring prioritizes a list of accounts natively inside Salesforce_
{% endtab %}
{% tab Lead and Account Grading %}
SalesWings allows Braze customers to qualify leads and accounts based on profile data (typically CRM data). This is also referred to as “lead grading”, “fit scoring,” or “firmographic scoring”. Braze customers can send attribute data directly to SalesWings, and SalesWings can read any Salesforce CRM standard or custom objects data and records for holistic profile scoring.
{% endtab %}
{% tab Sales Insights for Sales Reps %}
SalesWings enables you to show your sales reps sales insights about their leads, contacts, and accounts (Marketo Sales Insights alternative). Essentially, you can surface any Braze and web engagement data to your sales team. The insights are natively embedded into Salesforce CRM and can be pushed to other CRMs or systems or via a Braze email as a “sales alert”.

![Example of sales insights view for sales reps inside Salesforce (also available for other CRM systems)]({% image_buster /assets/img/saleswings/marketo_sales_insights_alternative_for_braze.png %})

_Example of sales insights view for sales reps inside Salesforce (also available for other CRM systems)_
{% endtab %}
{% tab Sales Alerts %}
SalesWings offers native email and Slack alerts, and you can set up report subscriptions in Salesforce that your sales team can access to get daily, weekly, and monthly email reports. Furthermore, through a Zapier integration, you can build additional workflows based on SalesWings lead qualification data.

![Example of sales alert via Slack channel]({% image_buster /assets/img/saleswings/smart_watch_alerts.png %})

_Example of sales alert via Slack channel_
{% endtab %}
{% tab Reporting in Salesforce CRM %}
Through the native SalesWings integration with Salesforce, you can build automated reporting with leads, contacts, accounts, and opportunities based on web engagement data and any Braze campaign engagement with a native Braze currents integration. For example, you can surface a list of hot leads to a sales team, with everyone who clicked on a specific email campaign or performed a specific action in your app or website.

![Example dashboard linked to Braze email & marketing engagement within Salesforce, looking at impact of Braze campaigns on sales results and outcomes]({% image_buster /assets/img/saleswings/saleswings_email_campaign_attribution_dashboard.png %})

_Example dashboard linked to Braze email & marketing engagement within Salesforce, looking at the impact of Braze campaigns on sales results and outcomes_
{% endtab %}
{% endtabs %}

## Integration

### Step 1: SalesWings account and configuration

[Schedule a demo](https://www.saleswingsapp.com/schedule-a-demo?utm_source=braze&utm_campaign=technicaldocs) with the friendly SalesWings team to learn more about SalesWings.

### Step 2: Installing behavioral tracking on your website or app

There are several ways for you to collect behavioral data in SalesWings for lead and account scoring, identifying buyer intent and sales insights:
* [Deploy the SalesWings tracking JavaScript](https://support.saleswingsapp.com/en/collections/3285135-1-implementing-saleswings-tracking-script) on the websites and apps where you want to track and identify leads
* Ingest Braze events along with event properties into SalesWings via Braze Currents
* Send behavioral lead activity data (and lead profile data) via [SalesWings integration with Segment](https://support.saleswingsapp.com/en/articles/9258905-segment-com-integration)
* Send data straight to the SalesWings [API](https://support.saleswingsapp.com/en/articles/6930889-using-saleswings-open-api-to-send-events-to-saleswings) from a third-party solution

### Step 3: Connecting SalesWings to Braze

Go to the [**SalesWings Integrations** page](https://helium.saleswings.pro/integrations) and expand the **Braze Integration** section.

![The Braze Integration section of the SalesWings Settings page.]({% image_buster /assets/img/saleswings/saleswings_braze_lead_scoring_integration_settings.png %})

Copy the value of the **Identifier** column for the newly created key and paste it into the **Braze API key** field of the SalesWings **Braze Integration** section.

Add your Braze API endpoint as described in [API and SDK endpoints article]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints), and enter it in the **Braze API endpoint** field. Copy the value of the **REST Endpoint** column and enter it in the **Braze API endpoint** field in the SalesWings **Braze Integration** section.

Then, select **Save**.

### Step 4: Enable SalesWings insights push to Braze (optional)

If you want to make SalesWings insights available on your Braze user profiles for segmentation, personalization, or Canvas journey orchestration, visit the [**SalesWings Integrations** page](https://helium.saleswings.pro/integrations) and expand the **Braze Integration** section.

Click **Start data push** under **SalesWings-to-Braze insights data push**.

### Step 5: Set up a custom Currents export to SalesWings (optional)

If you want to use [user behavior]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/customer_behavior_events) and [message engagement]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events) events for behavioral intelligence, lead and account scoring, produce sales insights, or generate reports in your CRM, go to the [**SalesWings Integrations** page](https://helium.saleswings.pro/integrations) and expand the **Braze Integration** section.

Select **Generate** under **Generate an API token to setup a Custom Currents Export**.

Then, [create a new Current]({{site.baseurl}}/user_guide/data/braze_currents/setting_up_currents) and select **Custom Currents Export** as the Current type.

In the **Credentials** section of the Current creation form, enter the API token you have generated on the [**SalesWings Integrations** page](https://helium.saleswings.pro/integrations) for **Bearer Token**, and `https://helium.saleswings.pro/api/braze/currents/events` for **Endpoint**.

### Step 6: Configuring SalesWings lead and account scoring for Braze, CRM integration, and more

Consult the SalesWings services team for full onboarding support via the [website](https://www.saleswingsapp.com/?utm_source=braze&utm_campaign=technicaldocs).

## Using this integration 

To trigger tie behavioral data and other data to leads and accounts, SalesWings must identify a user on your website or app, or through a third-party integration. This can occur in the following ways:

- **Form submissions:** When a user submits a web form, SalesWings will automatically identify all of your web form types (such as login, download, contact us, etc.) and resolve the identity of a user when they submit a form. 
- **URL clicks with a Braze ID or external ID:** A user clicks on a Braze marketing action, typically email clicks, banner clicks, or similar, leading to a page you are tracking with SalesWings.
- **Braze Currents events (optional):** If the Custom Currents export to SalesWings is configured, SalesWings will create an identified profile for every Braze user with an email that has events sent to the Current.
- **Sales email tracking via Gmail and Outlook plugins (optional):** If you decide to empower your sales representative with email tracking plugins, they can trigger full website tracking of users by sending trackable links.
- **Segment.com identify event (optional):** If you are a Segment.com user, you can also resolve the identity of a user with Segment.com integration.

### Identifying users from URL clicks

You can identify users automatically when they click on a trackable URL (for example, email blasts, banners with URLs). To make a URL trackable, there are two ways to modify your website URLs in your emails, banners, or SMS by adding the parameter and ID at the end of your links.

1. Appending `?braze_id=` followed by {% raw %}`{{${braze_id}}}`{% endraw %} 
  - **Link example:** {% raw %}`https://www.your-website.com?braze_id={{${braze_id}}}`{% endraw %}<br><br>

2. Appending `?br_user_id=` followed by {% raw %}`{{${user_id}}}`{% endraw %}
  - **Link example:** {% raw %}`https://www.client-website.com?br_user_id={{${user_id}}}`{% endraw %}

The `braze_id` variable is set to an identifier of the user-generated by Braze and is always available. The `br_user_id` variable is set to the user's identifier in your system and may be missing in certain scenarios (for example, for anonymous users created by the Braze SDK). If both `braze_id` and `br_user_id` are used in a link, SalesWings considers only the `braze_id` parameter.

### Pushing SalesWings insights to Braze

If you enable SalesWings insights push to Braze, SalesWings updates your Braze user profiles with the following [Custom Attributes]({{site.baseurl}}/user_guide/data/activation/custom_data/custom_attributes):

| Custom Attribute | Type | Description |
| ----------- | ----------- | ----------- |
| `sw_favorite` | boolean | Whether the lead was marked as a favorite in SalesWings or Salesforce CRM |
| `sw_last_active_at` | date | The moment of the lead's last activity on your website |
| `sw_lead_link_open` | string | The link to access a lead profile in SalesWings (without a SalesWings dashboard account) |
| `sw_lead_link_protected` | string | The link to access a lead profile in SalesWings (with a SalesWings dashboard account) |
| `sw_lead_owner` | string | The owner set for the lead in SalesWings or Salesforce CRM |
| `sw_lead_score` | float | The value of the main SalesWings lead score configured in the SalesWings [Rule Engine](https://helium.saleswings.pro/falcon) |
| `sw_predictive_score` | string | The value of SalesWings [predictive score](https://support.saleswingsapp.com/en/articles/581795-the-predictive-lead-score) that assesses the lead's engagement based on the number and recency of tracked activities. The possible values are `HOT`, `WARM`, `NORMAL`, `COLD` or `FROZEN` |
| `sw_salesforce_record_id` | string | The ID of the Lead or Contact record in Salesforce CRM |
| `sw_salesforce_record_url` | string | The URL of the Lead or Contact record in Salesforce CRM |
| `sw_session_count` | integer | The number of tracked sessions on your website for this lead |
| `sw_tags` | array of string | The needs and interests that SalesWings identified, represented as “tags”. The names of SalesWings tags configured in the SalesWings [Rule Engine](https://helium.saleswings.pro/falcon) that apply to this lead |
| Additional lead score attributes | float | One Custom Attribute for every additional lead score configured in the SalesWings [Rule Engine](https://helium.saleswings.pro/falcon). The attribute name is derived from the SalesWings score name, for example, a score named `Likeliness to meet` is sent as Custom Attribute `sw_likeliness_to_meet`. If you rename a score after the system creates it, SalesWings continues syncing with the initial Custom Attribute name. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

When the push is enabled, SalesWings immediately starts sending Custom Attributes to Braze as soon as underlying data points change in SalesWings lead profiles, and progressively syncs all existing leads even if they don't have new updates.

SalesWings updates every Braze user with an email that matches the SalesWings lead profile email address. If there are no matching users in Braze, SalesWings does not create a new one. 

### Using Braze Currents events in your CRM

If you connect a Braze Current to SalesWings, SalesWings will create identified lead profiles for every Braze user with an email and record supported Braze events as lead activity. In your CRM, all data can automatically be aggregated on the lead’s account level. The recorded activity and data could be further combined with the behavioral data collected with the SalesWings tracking script or Segment.com, or by sending other data to the SalesWings API, and then used to identify the needs and sales-readiness of your prospects for your lead and account management processes.

The following table shows the Braze event types supported by SalesWings and their representation in SalesWings lead activity history and rule engine:

| Event Category | Event Type | Event Name in SalesWings |
| ----------- | ----------- | ----------- |
| Canvas Events | Entries | `[Nurturing] Added by marketing team onto the journey $canvas_name` |
| Customer Behavior Events | Custom Events | `[Custom Event tracked] $name` |
| Customer Behavior Events | First Session | `[User Action] Today marks the user's first session` |
| Customer Behavior Events | Install Attribution | `[User Action] User installed app from $source` |
| Customer Behavior Events | Purchase Events | `[Purchase] Customer purchased $product_id for $price $currency` |
| Message Events | Content Card Click | `[Content Card engagement] Clicked on $campaign_name content card` |
| Message Events | Email Bounce | `[Alerting or negative] Email hard-bounced. This person's email appears to be no longer valid` |
| Message Events | Email Click | `[Email campaign engagement] Clicked in email $campaign_name on $url` |
| Message Events | Email Delivery | `[Nurturing] Received email $campaign_name` |
| Message Events | Email Open | `[Email campaign engagement] Opened email $campaign_name` |
| Message Events | Email Unsubscribe | `[Subscription status change] Unsubscribed from $campaign_name` |
| Message Events | In-App Message Click | `[In-app campaign engagement] Clicked on message $campaign_name` |
| Message Events | Push Open | `[Push notification engagement] Clicked on notification $campaign_name` |
| Message Events | SMS/MMS Inbound Received | `[SMS/mobile campaign engagement] We received a message from this person to our internal number $inbound_phone_number: $message_body` |
| Message Events | SMS/MMS Short Link Click | `[SMS/mobile campaign engagement] Clicked on $short_url` |
| Message Events | WhatsApp Inbound Received | `[WhatsApp engagement] We received a message from this person to our WhatsApp number $inbound_phone_number: $message_body` |
| Message Events | WhatsApp Read | `[WhatsApp engagement] Lead read our message from the $campaign_name campaign` |
| Subscriptions | Global Subscription State Change | `[Subscription status change] Global marketing subscription setting set to $subscription_status` |
| Subscriptions | Subscription Group State Change | `[Subscription status change] $subscription_status to/from $campaign_name` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

You can then configure **Custom Event** > **Event Name** and **Custom Event** > **Event Property** conditions for SalesWings tags and scores against the SalesWings event names from the table above. The list of event properties available for conditions is prefilled with some of the commonly used entries, and you can always add new ones in the **Event Property** section of the [Rule Engine configuration page](https://helium.saleswings.pro/falcon).

![Example of an Event Name condition.]({% image_buster /assets/img/saleswings/saleswings_braze_lead_scoring_custom_event_condition.png %})

For configuration and further troubleshooting, contact the [SalesWings services team](https://www.saleswingsapp.com/?utm_source=braze&utm_campaign=technicaldocs) for onboarding support.


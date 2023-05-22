---
nav_title: SalesWings
article_title: SalesWings
page_order: 1

description: "SalesWings enables braze customers with essential B2B functionality such as no-code lead scoring and grading, sales insights, and a Salesforce and CRM integration."
alias: /partners/saleswings/

page_type: partner
search_tag: Partner
hidden: true
layout: dev_guide
---

# SalesWings

> [SalesWings][1] upgrades braze with all essential B2B capabilities that you may be used to from B2B marketing automation platforms.
SalesWings is tightly integrated with braze and your CRM solution such as Salesforce Sales Cloud CRM, and delivers essential B2B capabilities including lead/account website tracking, lead scoring and grading, sales insights, sales alerts, sales and marketing alignment, and B2B attribution reporting.

## Prerequisites

| Requirement | Description |
| ----------- | ----------- |
| SalesWings account | A [SalesWings][1] account is required to take advantage of this partnership. |
| Braze REST API key | A Braze REST API key with `users.export.ids` permissions. <br><br> This can be created within the **Braze Dashboard > Developer Console > REST API Key > Create New API Key**. |
| Braze REST endpoint | [Your REST endpoint URL][2]. Your endpoint will depend on the Braze URL for your instance. |
| Segment.com account (OPTIONAL) | If you are a Segment.com user, you can send all lead engagement and profile data along with identify events via Segment.com for lead profiling. |
{: .reset-td-br-1 .reset-td-br-2}

## Use cases

### Lead scoring for braze | Lead and Account qualification for your sales team

SalesWings provides braze customers with a [user-friendly, powerful and flexible way to qualify leads with best-in-class lead scoring][3] and lead grading capabilities. SalesWings provides braze clients with a holistic approach to qualify leads and accounts, including predictive lead scoring, point-based behavioral lead scoring, as well as firmographic lead grading. All your lead qualification data is natively pushed to Salesforce CRM, braze (coming soon), as well as other systems where you want to manage and report on leads, contacts, accounts and opportunities.

![Example of simple, click-not-code lead scoring model in SalesWings.][4]
_Example of simple, click-not-code lead scoring model in SalesWings_

### Sales and marketing alignment challenges

SalesWings allows marketing teams to track, qualify and hand-off marketing-qualified leads to your sales teams. With a tight integration into Salesforce CRM and further lead management systems, you will be able to increase leads acceptance rates, lead qualification and conversion rates, up-selling and cross-selling and increase marketing-generated pipeline growth. All SalesWings data is natively pushed to Salesforce, and can be leveraged to fine-tune any existing process, or create new processes via lists, reports, flows, and more.

![Example of how SalesWings lead scoring prioritizes a list of leads or contacts natively inside Salesforce.][5]
_Example of how SalesWings lead scoring prioritizes a list of leads or contacts natively inside Salesforce_

![Example of how SalesWings lead scoring prioritizes a list of accounts natively inside Salesforce.][6]
_Example of how SalesWings lead scoring prioritizes a list of accounts natively inside Salesforce_

### Lead, Contact, Account and Opportunity grading

SalesWings allows braze customers to qualify leads and accounts based on profile data (typically CRM data). This is also referred to as “lead grading”, “fit scoring” or “firmographic scoring”. Braze customers can send attribute data directly to SalesWings, and SalesWings has the ability to read any Salesforce CRM standard or custom objects data and records, for a holistic profile scoring.

### Sales insights and intelligence for sales reps

SalesWings enables braze customers to show your sales reps intuitive sales insights about their leads, contacts and accounts. In a visual, intuitive and fully automated way, SalesWings summarises key insights such as a lead’s or account’s interests, sales readiness, detailed engagement with braze emails, other marketing campaigns and content, along with the full lead’s journey. Essentially, you can surface any braze and web engagement data to your sales team. The insights are natively embedded into Salesforce CRM, and can also be pushed to other CRM’s or systems, or via a braze email as a “sales alert”.

![Example of sales insights view for sales reps inside Salesforce (also available for other CRM systems).][7]
_Example of sales insights view for sales reps inside Salesforce (also available for other CRM systems)_

### Tactical sales tools like sales alerts

SalesWings incorporates a smart and holistic way to collaborate with your sales team in an effortless way. SalesWings has native email as well as Slack alerts, and you can set up report subscriptions in Salesforce that your sales team can access to get daily, weekly and monthly email reports. Furthermore, thanks to our Zapier integration, you can build additional work-flows based on SalesWings lead qualification data.

![Example of sales alert via Slack channel.][8]
_Example of sales alert via Slack channel_

### Reporting around campaigns and lead engagement with braze activities in Salesforce CRM

Through our Salesforce integration, you can build automated reporting with leads, contacts, accounts and opportunities, based on web engagement data and braze campaign engagement. For instance, you can surface a list of hot leads to a sales team / rep, with everyone who clicked on a specific email campaign, or performed a specific action in your app, or on your website.

![Example dashboard linked to braze email & marketing engagement within Salesforce, looking at impact of braze campaigns on sales results and outcomes.][9]
_Example dashboard linked to braze email & marketing engagement within Salesforce, looking at impact of braze campaigns on sales results and outcomes_

## Integration

The SalesWings B2B solution for braze requires the following elements:

1. A configured SalesWings account
2. A braze account, connected to SalesWings
3. Website tracking set up
4. Identification of leads set up

### Step 1: SalesWings account and configuration

Please [schedule a demo][10] with the friendly SalesWings team to learn more about SalesWings.

### Step 2: Installing behavioral tracking on your website / app

Currently there are 3 ways for you to collect behavioral data in SalesWings for lead scoring and sales insights.

1. [Deploy the SalesWings tracking Javascript][11] on the websites and web apps where you want to track and identify leads.
2. Send behavioral lead activity data (and lead profile data) via our Segment.com integration
3. (Coming soon) Send braze tracking data via currents to SalesWings

### Step 3: Connecting SalesWings to braze

Follow these instructions to connect your SalesWings project to braze:

1. Generate a new Braze API key for SalesWings:
  - Go to the **Developer Console** of your Braze Dashboard
  - In the **Rest API Keys** section, click on **Create New API Key**
  - Name it **“SalesWings”**
  - Select the single required permission: `users.export.ids`
  - Click on Save API Key
  - The key should become visible in the the Rest API Keys section
![Create braze API key for SalesWings][12]

2. Go to the [SalesWings Settings page][13]
3. Expand the **Braze Integration** section
![SalesWings braze integration settings][14]

4. Copy the value of the Identifier column for the newly created key and paste it in the Braze API key field of the SalesWings Braze Integration section
![braze API key for SalesWings][12]
![braze API key in SalesWings braze settings][15]

5. Find your Braze API endpoint as described at the [SDK Endpoints page][16] and enter it in the Braze API endpoint field. To find out your endpoint, locate the URL of your Braze dashboard in the URL column of the table and take the value of Rest Endpoint column of the corresponding row. For example, if your Braze dashboard URL is `https://dashboard-03.braze.com`, your Braze API endpoint should be `https://rest.iad-03.braze.com`.
6. Copy the value of the **REST ENDPOINT** column and enter it in the Braze API endpoint field of the SalesWings Braze Integration section
![braze API endpoint in SalesWings braze integration settings][17]

7. Click **Save Changes** in the SalesWings settings
8. SalesWings is now connected to braze 🎉

### Step 4: Identifying leads on your website / app

#### Ways to identify leads and trigger lead scoring with braze and SalesWings

To trigger lead scoring and the creation of sales insights, a lead must first be identified on your website or app by SalesWings - just like with other common B2B marketing automation solutions.
In order to identify leads on your website and initiate behavioral scoring, we have to first resolve their identity on the website. This can occur in 4 ways:

1. Form submissions
  - A lead (“user”) submits a web form: The SalesWings javascript will automatically identify all of your web forms (i.e. login, download, contact us etc), and resolve the identity of a lead (”user”) when they submit such a form. Key is that the web form has an “email” field, which is used as a key ID in SalesWings
2. Segment.com Identify event (optional)
  - If you are a Segment.com user, you can also resolve the identity of a lead with our Segment.com integration
3. Sales email tracking via Gmail and Outlook plugins (optional)
  - If you decide to empower your sales reps with our email tracking plugins, they are able to trigger full website tracking of leads by sending them trackable links.
4. URL link clicks with braze ID or external ID
  - A lead clicks on a braze marketing action, typically email clicks, banner clicks, or similar, leading to a page which you are tracking with the SalesWings tracking script
  - See guide below how to achieve this:

#### Identifying leads from URL clicks

You can identify leads automatically when they click on a “trackable” URL, for example via email blasts, banners with URL’s, or else.

In order to make a URL trackable:

1. Modify your URL links going to your website in your emails, banners, SMS, or other places
2. Add the following parameter and ID at the end of your links (just like UTM’s)

Option 1: **braze_id** parameter:
  - `?braze_id=` followed by the “Personalization” variable {% raw %}`{{${braze_id}}}`{% endraw %}
  - The variable here is the standard “braze ID”
  - Example of final link: {% raw %}`https://www.your-website.com?braze_id={{${braze_id}}}`{% endraw %}

Option 2: **br_user_id** parameter:
  - `?br_user_id=` followed by the “Personalization” variable {% raw %}`{{${user_id}}}`{% endraw %}
  - The variable here is your customizable “external ID”
  - Example of final link: {% raw %}`https://www.client-website.com?br_user_id={{${user_id}}}`{% endraw %}

The **braze_id** personalization variable is set to a permanent identifier of the user generated by braze and is always available. The **user_id** personalization variable is set to the identifier of the user in your system and might be missing in certain scenarios (e.g., for anonymous users created by braze SDK). If both **braze_id** and **br_user_id** are used in a link, SalesWings will consider only **braze_id** parameter.

### Step 5: Configuring SalesWings lead scoring for braze, CRM integration, and more

Please consult our services team for full on-boarding support via [our website][1].

## Troubleshooting

Please contact our services team for support via [our website chat][1].

---
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

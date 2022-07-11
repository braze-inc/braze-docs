---
nav_title: actionable.me
article_title: actionable.me
page_order: 1

description: "actionable.me is a proprietary software and processes to help you get the most out of your Braze investment right away."
alias: /partners/actionableme/

page_type: partner
search_tag: Partner
hidden: true

---

# actionable.me

> [actionable.me][2] is a standardized and automated approach to running CRM programs. We provide tools and processes designed to get Braze customers to value quickly, consistently and predictably. The platform has been built by the team at Massive Rocket (data & crm agency) on top of Braze technology.

Customer Engagement Platforms like Braze unlock significant growth and competitive differentiation opportunities for businesses. However, most companies plan and execute their CRM (CEM) activities manually, inefficiently and inconsistently. Braze + actionable.me will ensure you have a best in class customer engagement setup and the process to get your business to value systematically.

## Prerequisites

| Requirement | Description                                                                                                                                                                            |
| ----------- |----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| actionable.me account | actionable.me setup is required to take advantage of this partnership.                                                                                                                 |
| Braze REST API key | A Braze REST API key with permissions listed in the next section.<br><br> This can be created within the **Braze Dashboard > Developer Console > REST API Key > Create New API Key**. |
| Braze REST endpoint | [Your REST endpoint URL][1]. Your endpoint will depend on the Braze URL for your instance.                                                                                             |
{: .reset-td-br-1 .reset-td-br-2}

## Integration

To integrate Braze and actionable.me, the actionable.me platform must be configured and a Braze API key needs to be created in Braze and configured in the actionable.me dashboard .

### Step 1: Create your Braze API Key

In Braze, navigate to **Developer Console**, select the **REST API Keys** tab and generate your API key.

![generating_new_api_key][4]

When creating the API key, the following permissions are required:

```
campaigns.list
campaigns.data_series
campaigns.details
sends.data_series

segments.list
segments.data_series
segments.details

events.list
canvas.list
canvas.data_series
canvas.details
canvas.data_summary

kpi.mau.data_series
kpi.dau.data_series
kpi.new_users.data_series
kpi.uninstalls.data_series
```

To complete the integration, you will need to provide your Rest API Key and [REST endpoint URL][1] to your actionable.me operations team. actionable.me will then establish the connection and reach out to you once the setup is complete.

### Step 2: The actionable.me operations team will configure your integration

Your actionable.me operations team will configure the integration between actionable.me and Braze and be in touch to start sharing insights.

![integrating_your_api_key][5]

## Troubleshooting

Contact the **actionable.me or Massive Rocket team** for additional support: [info@massiverocket.com][3]

[1]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints
[2]: https://actionable.me
[3]: mailto:info@massiverocket.com
[4]: {% image_buster /assets/img/actionableme/image1.png %}
[5]: {% image_buster /assets/img/actionableme/image2.png %}

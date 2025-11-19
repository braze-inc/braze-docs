---
nav_title: actionable.me
article_title: actionable.me
description: "This reference article outlines the partnership between Braze and actionable.me, a proprietary software and processes, that allow you to get the most out of your Braze investment right away."
alias: /partners/actionableme/
page_type: partner
search_tag: Partner

---

# actionable.me

> [actionable.me](https://actionable.me), built by the team at Massive Rocket, a data and CRM agency, is a standardized and automated approach to running CRM programs, providing tools and processes designed to get Braze customers to value quickly, consistently, and predictably. 

_This integration is maintained by actionable.me._

## About the integration

The Braze and actionable.me integration allows you to deploy a service to monitor your progress in the utilization of Braze. Through a combination of tools and processes, they will rapidly benchmark your CRM performance, identify new opportunities and provide recommendations on how to perform better.

## Prerequisites

| Requirement | Description |
| --- | --- |
| actionable.me account | An actionable.me account is required to take advantage of this partnership. |
| Braze REST API key | A Braze REST API key with the permissions listed in the next section.<br><br> This can be created in the Braze dashboard from **Settings** > **API Keys**. |
| Braze REST endpoint | [Your REST endpoint URL]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). Your endpoint will depend on the Braze URL for your instance. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integration

To integrate Braze and actionable.me, the actionable.me platform must be configured, and a Braze API key needs to be created in Braze and configured in the actionable.me dashboard.

### Step 1: Create your Braze API Key

In Braze, navigate to **Settings** > **API Keys**. Select **Create New API Key** and ensure following permissions are added:

- `campaigns.list`
- `campaigns.data_series`
- `campaigns.details`
- `sends.data_series`
- `segments.list`
- `segments.data_series`
- `segments.details`
- `events.list`
- `canvas.list`
- `canvas.data_series`
- `canvas.details`
- `canvas.data_summary`
- `kpi.mau.data_series`
- `kpi.dau.data_series`
- `kpi.new_users.data_series`
- `kpi.uninstalls.data_series`

### Step 2: Provide information to the actionable.me team

To complete the integration, you must provide your REST API key and [REST endpoint URL]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints) to your actionable.me operations team. actionable.me will then establish the connection and contact you after the setup is complete and be in touch to start sharing insights.

![The actionable.me "add platform" page that the actionable.me operations team will configure.]({% image_buster /assets/img/actionableme/image2.png %})

## Troubleshooting

Contact the actionable.me or Massive Rocket team for additional support: [info@massiverocket.com](mailto:info@massiverocket.com)



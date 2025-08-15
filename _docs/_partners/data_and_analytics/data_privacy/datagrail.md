---
nav_title: Datagrail
article_title: DataGrail
description: "This reference article outlines the partnership between Braze and DataGrail, a privacy management platform, that allows you to detect consumer data collected and stored within Braze to quickly process DSRs."
alias: /partners/datagrail/
page_type: partner
search_tag: Partner

---

# DataGrail

> [DataGrail](https://www.datagrail.io/), a privacy management platform, helps build consumer trust and eliminate risky business. With continuous system detection and automated data subject request (DSR) fulfillment, DataGrail powers privacy programs, supporting compliance with evolving privacy laws and regulations, like GDPR, CCPA, and CPRA. 

_This integration is maintained by DataGrail._

## About the integration

The Braze and DataGrail integration allows you to detect consumer data collected and stored within Braze to quickly process DSRs (access, delete, and do-not-sell requests). Braze will be added to an accurate blueprint of where consumer data lives in your organization with automated data mapping — no more surveys or spreadsheets are needed to maintain a privacy framework or produce a record of processing activities (RoPA). 

## Prerequisites

| Requirements | Description |
|---|---|
| DataGrail account | A DataGrail account to take advantage of this partnership.<br>Contact your admin or email support@datagrail.io with any issues or questions regarding the integration. |
| Braze API key | A Braze REST API key with `events.list`, `users.export.ids`, `users.delete`, and `users.track` permissions.<br><br>This can be created in the Braze dashboard from **Settings** > **API Keys**. |
| Braze instance | Your Braze instance can be obtained from your Braze onboarding manager or can be found on the [API overview page]({{site.baseurl}}/api/basics/#endpoints). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integration

Login to the DataGrail portal and select **Connect** within the integration page for Braze. Next, enter your instance and Braze API Key and select **Connect Braze**.

If there are additional Braze accounts to integrate:
1. Select **Edit Connection** within the integration page for Braze.
2. From the dropdown, select **+Add New Connection**.
3. Under **Connection Name**, enter a new name to identify this separate account (for example, Braze Training Account).
4. Enter a separate Braze instance and API key for this new account.
5. Select **Connect**.

Email DataGrail at support@datagrail.io with any issues or questions regarding your integration.


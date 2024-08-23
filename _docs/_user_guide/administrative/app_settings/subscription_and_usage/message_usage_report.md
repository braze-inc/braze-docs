---
nav_title: Message Usage Report
article_title: Message Usage Report
page_order: 0
page_type: reference
description: "This reference article covers the Message Usage Report dashboard, where you can view real-time and self-service insights into your SMS and WhatsApp credit usage."
tool: Dashboard
hidden: true
permalink: /message_usage_report/
---

# Message usage report

> The **Message Usage Reporting** dashboard provides real-time, self-service insights into your SMS and WhatsApp credit usage for a comprehensive view of historical and current usage compared against contract allotments. These insights can reduce your confusion and help you make adjustments to prevent overage risks.

The **Message Usage Reporting** dashboard is divided into three sections:
- [Credit Usage Overview](#credit-usage-overview)
- [SMS/MMS](#smsmms) 
- [WhatsApp](#whatsapp)

## Credit Usage Overview

**Credit Usage Overview** provides an overview of usage across all channels that use credits. You can see how you're pacing against your overall credit allotment, and find details around your active contract and your contract period.

This page displays if you're on a message credits contract or if you've purchased WhatsApp. The channels that use message credits are shown in the **Credit contract overview**.

{% alert note %}
If you purchased WhatsApp but aren't on a message credits contract, you'll still see credit consumption for WhatsApp because that's how legacy WhatsApp contracts are billed. This differs from legacy SMS, which only consumes credits when you're on a message credits contract.
{% endalert %}

**Credit Usage Overview** data is limited to the contract period, which is displayed in the **Credit contract overview**. You can't filter on a date range outside of the **Credit period**.

### Credit Usage over Contract

The **Credit Usage over Contract** graph shows your usage over the selected period of time. The granularity of this chart depends on your selected time frame. Export export options by selecting the menu in the top right corner of the chart.

![Credit Consumption Overview dashboard with sections for credit usage, credit contract overview, and credit consumption over contract.][1]{: style="max-width:80%;"}

## SMS/MMS

**SMS/MMS Credit Consumption** shows the usage breakdown for the SMS/MMS channel. The columns in the data table vary depending on whether SMS/MMS is a credit channel. If SMS/MMS is a credit channel, additional **Credit ratio** and **Credits consumed** columns will be visible and indicate the respective country rate and consumed credits. Additionally, high-level tiles will indicate the total SMS and, when relevent, MMS consumption across the selected date range.

Filters are available allowing you to filter by **Country** or **SMS type**.

![SMS/MSS Credit Consumption with tiles for high-level data and a section for consumption by account.][2]{: style="max-width:80%;"}

Unlike the **Credit Usage Overview**, this section contains historical data from prior contract periods. 

{% alert note %}
It’s possible to select a date range that contains both non-credits and message credits usage. In this case, the consumption that occurred outside of message credits will display `—` (null) in the **Credit ratio** and **Credits consumed** columns.
{% endalert %}

![SMS/MMS Credit Consumption table with null values.][3]{: style="max-width:80%;"}

## WhatsApp

**WhatsApp Credit Consumption** shows the usage breakdown for the WhatsApp channel. The tiles display the total WhatsApp credit usage, which can be broken down in the **Consumption by account** section by applying filters to limit the data table results to a specific workspace.

### Filters

You can filter your data by:
- Country
- WhatsApp Business account
- Braze workspace
- Conversation category type
- Region

![WhatsApp Credit Consumption with a tile for total credits consumed and a consumption by account table.][4]{: style="max-width:80%;"}

## Things to know

{% alert important %}
The data shown in **Message Usage Reporting** is at the contract level and isn't scoped to an individual dashboard company or workspace. This data reflects usage from all workspaces within your dashboard, and potentially across all dashboards (if you have multiple).
{% endalert %}

- The underlying data is provided in a daily cadence, with the data tables refreshed at 3 am, 9 am, 12 pm, and 6 pm EST. 
- Braze follows standard rounding methodology: numbers are rounded up to the nearest tenth.

[1]: {% image_buster /assets/img/app_settings/credit_usage_over_contract1.png %}
[2]: {% image_buster /assets/img/app_settings/sms_credit_consumption2.png %}
[3]: {% image_buster /assets/img/app_settings/sms_table_null3.png %}
[4]: {% image_buster /assets/img/app_settings/whatsapp_credit_consumption4.png %}
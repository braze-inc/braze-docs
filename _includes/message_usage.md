# Message Usage dashboard

> The Message Usage dashboard provides self-service insights into your SMS and WhatsApp credit usage for a comprehensive view of historical and current usage compared against contract allotments. These insights can reduce your confusion and help you make adjustments to prevent overage risks.

The **Message Usage** dashboard is divided into three sections:
- [Credit Usage Overview](#credit-usage-overview)
- [SMS/MMS](#smsmms) 
- [WhatsApp](#whatsapp)

Access the dashboard by going to **Settings** > **Billing** > **Message Usage**.

## Message credits usage overview

**Message Credits Usage Overview** provides an overview of usage across all channels that use credits. You can see how you're pacing against your overall credit allotment, and find details about your active contract and your contract period.

This page displays if you're on a message credits contract or if you've purchased WhatsApp. The channels that use message credits are shown in the **Credits contract overview**.

{% alert note %}
If you purchased WhatsApp but aren't on a message credits contract, you'll still see credit consumption for WhatsApp because that's how legacy WhatsApp contracts are billed. This differs from legacy SMS, which only consumes credits when you're on a message credits contract.
{% endalert %}

**Message Credits Usage Overview** data is limited to the contract period, which is displayed in the **Credits contract overview**. You can't filter on a date range outside of the **Credits period**.

### Message credits usage over contract

The **Message Credits Usage over Contract** graph shows your usage over the selected period of time. The granularity of this chart depends on your selected time frame. Export export options by selecting the menu in the top right corner of the chart.

![Message Credits Usage Overview dashboard with sections for credit usage, credit contract overview, and credit consumption over contract.][1]{: style="max-width:70%;"}

## SMS and MMS

**SMS/MMS Credits Usage** shows the usage breakdown for the SMS/MMS channel. The columns in the data table vary depending on whether SMS/MMS is a credit channel. If SMS/MMS is a credit channel, additional **Credit ratio** and **Credits** columns will be visible and indicate the respective country rate and consumed credits. Additionally, high-level tiles will indicate the total SMS and, when relevent, MMS consumption across the selected date range.

Filters are available allowing you to filter by **Country** or **SMS type**.

![SMS/MSS Credits Usage with tiles for high-level data and a section for consumption by account.][2]{: style="max-width:70%;"}

Unlike the **Message Credits Usage Overview**, this section contains historical data from prior contract periods. 

{% alert note %}
It’s possible to select a date range that contains both non-credits and message credits usage. In this case, the consumption that occurred outside of message credits will display `—` (null) in the **Credit ratio** and **Credits** columns.
{% endalert %}

![SMS/MMS Credits Usage table with null values.][3]{: style="max-width:70%;"}

## WhatsApp

**WhatsApp Credits Usage** shows the usage breakdown for the WhatsApp channel. The tiles display the total WhatsApp credit usage, which can be broken down in the **Usage by account** section by applying filters to limit the data table results to a specific workspace.

### Filters

You can filter your data by:
- Country
- WhatsApp Business account
- Braze workspace
- Conversation category type
- Region

![WhatsApp Credits Usage with a tile for total credits consumed and a usage by account table.][4]{: style="max-width:70%;"}

## Things to know

{% alert important %}
The data shown in the **Message Usage** dashboard is at the contract level and isn't scoped to an individual dashboard company or workspace. This data reflects usage from all workspaces within your dashboard, and potentially across all dashboards (if you have multiple).
{% endalert %}

- The underlying data is provided in a daily cadence, with the data tables refreshed at 3 am, 9 am, 12 pm, and 6 pm EST. 
- Braze follows standard rounding methodology: numbers are rounded up to the nearest tenth.

[1]: {% image_buster /assets/img/app_settings/credit_usage_over_contract1.png %}
[2]: {% image_buster /assets/img/app_settings/sms_credit_consumption2.png %}
[3]: {% image_buster /assets/img/app_settings/sms_table_null3.png %}
[4]: {% image_buster /assets/img/app_settings/whatsapp_credit_consumption4.png %}
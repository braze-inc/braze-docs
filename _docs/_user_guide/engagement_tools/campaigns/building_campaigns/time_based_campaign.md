---
nav_title: Time-Based Functionalities for Campaigns
article_title: Time-Based Functionalities for Campaigns
page_order: 2
tool: Campaigns
page_type: reference
description: "This reference article covers time-based functionalities for Campaigns."

---
# Time-Based Functionalities for Campaigns

> This reference article covers time-based functionalities for campaigns to assist with strategies, troubleshooting, and to answer common questions.

## Scheduled Delivery

This section covers time-based scheduling and delivery options for [Scheduled Delivery]({{site.baseurl}}/user_guide/engagement_tools/campaigns/scheduling_and_organizing/delivery_types/scheduled_delivery/) campaigns.

### Send at a designated time

| Definition | Time Zone |
| ---------- | --------- |
| Send message at a designated time, on a specific calendar date. | Company's time zone. |
{: .reset-td-br-1 .reset-td-br-2}

![Send at a designated time][2]

### Intelligent Timing

| Definition | Time Zone |
| ---------- | --------- |
| User's optimal time. Each user will receive the campaign at the time they are most likely to engage. [Learn more]({{site.baseurl}}/user_guide/intelligence/intelligent_timing/). | If you select **a specific time** as your [fallback]({{site.baseurl}}/user_guide/intelligence/intelligent_timing/#fallback-options), this will be sent in the user's local time. |
{: .reset-td-br-1 .reset-td-br-2}

![Intelligent Timing][3]

### Send campaign to users in their local time zone

| Definition | Time Zone |
| ---------- | --------- |
| Allows you to deliver messages to a segment based on a user's individual time zone. [Learn more]({{site.baseurl}}/user_guide/engagement_tools/campaigns/faq/#what-does-local-time-zone-delivery-offer). | Users's local time. If a user's time zone isn't set, this will fall back to company time zone. |
{: .reset-td-br-1 .reset-td-br-2}

![Local time zone][4]

### Allow users to become re-eligible to receive campaign

| Definition | Time Zone |
| ---------- | --------- |
| After a user is messaged by this campaign, specify when they will become re-eligible to receive the campaign again. [Learn more]({{site.baseurl}}/user_guide/engagement_tools/campaigns/scheduling_and_organizing/delivery_types/reeligibility/#campaigns). | N/A |
{: .reset-td-br-1 .reset-td-br-2}

![Re-eligibility][5]

## Action-Based Delivery

This section covers the schedule delay and delivery options for [Action-Based Delivery]({{site.baseurl}}/user_guide/engagement_tools/campaigns/scheduling_and_organizing/delivery_types/triggered_delivery/) campaigns.

### Schedule Delay

{% alert important %}
In choosing your delay length, note that if you set a delay that is longer than the [Campaign Duration]({{site.baseurl}}/user_guide/engagement_tools/campaigns/scheduling_and_organizing/delivery_types/triggered_delivery/#step-4-assign-duration), no users will receive your campaign.
{% endalert %}

#### Send campaign immediately

| Definition | Time Zone |
| ---------- | --------- |
| Send message immediately after the user performs the trigger action. | N/A |
{: .reset-td-br-1 .reset-td-br-2}

![Send immediately][6]

#### Send campaign after X days

| Definition | Time Zone |
| ---------- | --------- |
| Send message after a delay. You can specify a delay in seconds, minutes, hours, days, or weeks. | N/A |
{: .reset-td-br-1 .reset-td-br-2}

![Send after X days][7]

#### Send campaign on the next [day of the week] at X time

| Definition | Time Zone |
| ---------- | --------- |
| Send message on the next specified day of the week, at a selected time of day. | Select between **user's local time** or **company time** |
{: .reset-td-br-1 .reset-td-br-2}

![Send on the next (day) at X time][8]

For example, suppose you select "Send on the next Saturday at 3:15pm". If a user performs the trigger event on a Saturday, they would receive that message on the next Saturday in 7 days. If they enter on a Friday, the next Saturday would be in 1 day.

#### Send in X calendar days at Y time

| Definition | Time Zone |
| ---------- | --------- |
| Send message in a specific number of days at a specified time. | Select between **user's local time** or **company time** |
{: .reset-td-br-1 .reset-td-br-2}

![Send in X days at Y time][9]

Braze calculates the delay as `day of the week` + `calendar days`, then adds the `time`. For example, suppose the user performs the trigger event on Monday at 9pm, and the schedule delay is set to "Send campaign in 1 day at 9am". That message will be delivered on Tuesday at 9am, because Braze calculates the delay as `Monday` + `1 calendar day`, then adds on `9am`.

### Quiet Hours

| Definition | Time Zone |
| ---------- | --------- |
| Prevent messages from being sent during specified hours. If a message triggers during Quiet Hours, you can choose between aborting the message, or sending at the next available time (i.e. Send at the end of your Quiet Hours). | User's local time. If a user's time zone isn't set, this will fall back to company time zone. |
{: .reset-td-br-1 .reset-td-br-2}

![Quiet Hours][10]

### Allow users to be re-eligible to receive campaign

| Definition | Time Zone |
| ---------- | --------- |
| After a user is messaged by this campaign, specify when they will become re-eligible to receive the campaign again. [Learn more]({{site.baseurl}}/user_guide/engagement_tools/campaigns/scheduling_and_organizing/delivery_types/reeligibility/#campaigns). | N/A |
{: .reset-td-br-1 .reset-td-br-2}

![Re-eligibility][5]

### Global Frequency Capping

| Definition | Time Zone |
| ---------- | --------- |
| Limit how many times each user should receive the campaign within a certain time frame, which can be measured in minutes, days, weeks (7 days), and months. [Learn more]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/rate-limiting/#frequency-capping). | User's local time. If a user's time zone isn't set, this will fall back to company time zone. |
{: .reset-td-br-1 .reset-td-br-2}

Frequency capping is based on calendar days, not a 24-hour period. This means that you could set up a frequency capping rule of sending no more than one campaign a day, but if a user receives a message at 11pm in their local time, they can still receive another message an hour later (on midnight the next calendar day).

## Conversion Deadline

| Definition | Time Zone |
| ---------- | --------- |
| The maximum amount of time that may pass between a user receiving a campaign and performing the assigned action for it to be considered a conversion. [Learn more]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/conversion_events/). | N/A |
{: .reset-td-br-1 .reset-td-br-2}



[2]: {% image_buster /assets/img_archive/time_designated.png %}
[3]: {% image_buster /assets/img_archive/time_intelligent_timing.png %}
[4]: {% image_buster /assets/img_archive/time_local.png %}
[5]: {% image_buster /assets/img_archive/time_reeligibility.png %}
[6]: {% image_buster /assets/img_archive/time_delay_immediately.png %}
[7]: {% image_buster /assets/img_archive/time_delay_after.png %}
[8]: {% image_buster /assets/img_archive/time_delay_on_the_next.png %}
[9]: {% image_buster /assets/img_archive/time_delay_in.png %}
[10]: {% image_buster /assets/img_archive/time_quiet_hours.png %}

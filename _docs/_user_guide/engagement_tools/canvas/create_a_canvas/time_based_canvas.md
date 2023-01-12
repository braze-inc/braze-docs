---
nav_title: Time-Based Functionalities for Canvas
article_title: Time-Based Functionalities for Canvas
page_order: 1
tools: Canvas
page_type: reference
description: "This reference article covers definitions, time zones, and examples of time-based functionalities for Canvas."

---

# Time-based functionalities for Canvas

> This reference article covers time-based functionalities for Canvas to assist with strategies, troubleshooting, and to answer common questions.

## Schedule delay

The following information applies to the original Canvas workflow. For time-based functionalities the for Canvas Flow workflow, check out the [Delay component]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/delay_step/).

### Send immediately

| Definition |  Time Zone |
| --- | --- |
| Send message immediately after the user receives the previous step, or if this is the first step, immediately after the user enters the Canvas. | N/A |
{: .reset-td-br-1 .reset-td-br-2}

![][1]

### Send after X days

| Definition |  Time Zone |
| --- | --- |
| Send message after a delay. You can specify a delay in seconds, minutes, hours, days, or weeks.  | N/A |
{: .reset-td-br-1 .reset-td-br-2}

![][2]

### Send on the next [day of the week] at X time

| Definition |  Time Zone |
| --- | --- |
| Send message on the next specified day of the week, at a selected time of day.  | Select between **user's local time** or **company time** |
{: .reset-td-br-1 .reset-td-br-2}

For example, suppose you select "Send on the next Saturday at 3:15 pm". If a user enters the Canvas on a Saturday, they would receive that message on the next Saturday in seven days. If they enter on a Friday, the next Saturday would be in one day.

![][3]

### Send in X calendar days at Y time

| Definition |  Time Zone |
| --- | --- |
| Send message in a specific number of days at a specified time. | Select between **user's local time** or **company time** |

Canvas calculates the delay as `day of the week` + `calendar days`, then adds the `time`. For example, suppose a Canvas component is sent on Monday at 9 pm, and the next step is scheduled to "Send in 1 day at 9 am". That message will be delivered on Tuesday at 9 am, because the Canvas calculates the delay as `Monday` + `1 calendar day`, then adds on `9 am`.

![][4]

### Intelligent Timing

| Definition | Time Zone |
| ---------- | ----- |
| [Intelligent Timing]({{site.baseurl}}/user_guide/intelligence/intelligent_timing/) calculates the optimal send time based on a statistical analysis of your user’s past interactions with your messaging (on a per channel basis) and app. | If you select **a specific time** as your [fallback]({{site.baseurl}}/user_guide/intelligence/intelligent_timing/#fallback-options), this will be sent in the user's local time. |
{: .reset-td-br-1 .reset-td-br-2}

![][5]

## Global frequency capping

| Definition | Time Zone |
| --- | --- |
| Limit how many times each user should receive the Canvas within a certain time frame, which can be measured in minutes, days, weeks (seven days), and months. | User's local time. If a user's time zone isn't set, this will fall back to company time zone. |
{: .reset-td-br-1 .reset-td-br-2}

[Frequency capping]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/rate-limiting/#frequency-capping) is based on calendar days, not a 24-hour period. This means that you could set up a frequency capping rule of sending no more than one campaign a day, but if a user receives a message at 11 pm in their local time, they can still receive another message an hour later (on midnight the next calendar day).

![Frequency Capping][6]

[1]: {% image_buster /assets/img_archive/schedule_delay_immediately.png %}
[2]: {% image_buster /assets/img_archive/schedule_delay_after.png %}
[3]: {% image_buster /assets/img_archive/schedule_delay_next.png %}
[4]: {% image_buster /assets/img_archive/schedule_delay_in.png %}
[5]: {% image_buster /assets/img_archive/schedule_delay_intelligent.png %}
[6]: {% image_buster /assets/img_archive/schedule_frequency_capping.png %}

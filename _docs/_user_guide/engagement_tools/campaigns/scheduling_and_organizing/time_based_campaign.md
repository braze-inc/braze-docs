---
nav_title: Time-Based Functionalities for Campaigns
platform: Campaigns
subplatform: Scheduling and Organizing
page_order: 0

tool: Campaigns
page_type: reference
description: "This reference article covers time-based functionalities for Campaigns."
---
# Time-Based Functionalities for Campaigns

> This document serves to inform you of the nuances of any time-related capabilities in Braze relating to campaigns to assist with customer questions/strategies, as well as with troubleshooting. It outlines the definition of that term or capability, the time zone it pertains to, if any, an example for clarity, and other additional caveats and notes.

Scheduled Delivery| Definition | Time Zone | Notes | 
----------------- | ---------- | --------- | ------- |
Send at a Designated Time | Calendar Day | Company's Time Zone | Excludes local time delivery |
Local Time Delivery | Allows you to deliver messages to a segment based on a user's individual time zone | User's Time Zone | We use the company's time zone if the user's time zone is not set|
Intelligent Timing | User's Optimal Time | Not Relevant | |
Re-eligibility | User is eligible again for the message in exactly x seconds | Not Relevant | If a user is re-eligible in 1 month, that's exactly 2592000 seconds, equal to approx 30 days |
Quiet Hours| Prevent messages from being sent during specified hours | User's Time Zone | We use the company's time zone if the user's time zone is not set|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}


Action-Based Delivery| Definition | Time Zone | Notes |
----------------- | ---------- | --------- | ------- |
Action-Based Delay<br>Send "in x days at y am/pm" | Day of week + 1 calendar day + that specific time (see example)<br><br>Using the "in" clause only allows the use of calendar days as a measurement of time | Company's Time Zone | Example:<br>If a trigger event is performed at 9 pm on Monday and the campaign is set up to send "in 1 day at 6 am", the user will receive the message on Tuesday at 6 am |
Action-Based Delay<br>Send "after x seconds/minutes/days/weeks" | The "after" clause allows the user to specify x seconds, minutes, hours, and days. | Not Relevant | If a Canvas step is sent after 1 day, then the user will receive the step exactly 24 hours after |
Global Frequency Capping | Calendar Day | User's Time Zone | We use the company's time zone if the user's time zone is not set <br><br> It's possible a user does not have to wait 24 hours to get another message, since it's based on calendar days and not a 24-hour period.<br><br>Example:<br>Set up a frequency capping rule in the users' time zone of "send no more than 1 campaign a day" <br> If a user receives a message at 11 pm in their local time zone, they can receive another message an hour later.  |
Send Message in x Day using Intelligent Timing | Calendar Day | Not Relevant | |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

Conversions| Definition | Time Zone |
----------------- | ---------- | --------- |
Conversion Event Deadline | Window begins when the user receives the campaign | Not Relevant |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}


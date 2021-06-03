---
nav_title: Time-Based Functionalities for Campaigns
platform: Campaigns
subplatform: Scheduling and Organizing
page_order: .9

tool: Campaigns
page_type: reference
description: "This reference article covers time-based functionalities for Campaigns."
---
# Time-Based Functionalities for Campaigns

> This document serves to inform you of the nuances of any time-related capabilities in Braze relating to campaigns to assist with customer questions/strategies, as well as with troubleshooting. It outlines the definition of that term or capability, the time zone it pertains to if any, an example for clarity, and other additional caveats and notes.

Scheduled Delivery| Definition | Time Zone | Example | Notes |
----------------- | ---------- | --------- | ------- | ----- |
Send at a designated time (except for Local Time Delivery) | Calendar Day | Company's Time Zone | | |
Local Time Delivery | Allows you to deliver messages to a segment based on a user's individual timezone | User's Time Zone | | We use Company's Time Zone if User's Time Zone is not Set|
Intelligent Timing | User's Optimal Time | Not Relevant | | |
Re-eligibility | User is eligible again for the message in exactly x seconds | Not Relevant | If a user is re-eligible in 1 month, that's exactly 2592000 seconds, equal to approx 30 days | |
Quiet Hours| Prevent messages from being sent during specified hours | User's Time Zone | | We use Company's Time Zone if User's Time Zone is not Set|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}


Action-Based Delivery| Definition | Time Zone | Example | Notes |
----------------- | ---------- | --------- | ------- | ----- |
Action-based Delay<br>Send "in x days at y am/pm" | Day of week + 1 calendar day + that specific time (see example) | Company's Time Zone | If a trigger event is performed at 9pm on Monday, and the campaign is set up to send “in 1 Day at 6am”. The user will receive the message on Tuesday at 6am | Using "in" clause only allows the use of calendar days as a measurement of time |
Action-based Delay<br>Send "after x seconds/minutes/days/weeks" | The 'after' clause allows the user to specify x seconds, minutes, hours and days. | Not Relevant | If Canvas step is sent after 1 day, then the user will receive the step exactly 24 hours after | |
Global Frequency Capping | Calendar Day | User's Time Zone | User Time Zone set up a frequency capping rule of send no more than 1 campaign a day <br><br> If a user receives a message at 11 pm in their local time zone, he/she can receive another message an hour later.  | We use Company's Time Zone if User's Time Zone is not Set <br><br> It's possible a user does not have to wait 24 hours to get another message, since it's based on calendar days and not a 24-hour period. |
Send Message in x Day using Intelligent Timing | Calendar Day | Not Relevant | | |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

Conversions| Definition | Time Zone | Example | Notes |
----------------- | ---------- | --------- | ------- | ----- |
Conversion Event Deadline | Window begins when the user receives the campaign | Not Relevant | | |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}


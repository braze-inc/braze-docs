---
nav_title: High Volume Sending
page_order: 4
description: "This reference article covers how Braze processes certain keywords for SMS, as well as best practices."
page_type: reference
tool:
  - Dashboard
  - Docs
  - Campaigns

platform:
  - iOS
  - Android

channel:
  - SMS
---

# High Volume Sending

Plan on doing some high volume sending? We have some best practices for you to ensure it runs smoothly.

- Adjust the delivery speed rate-limiting for your campaign/canvases as needed, based on target audience size. This will ensure that (1) you reach the send volume that you need and (2) Braze sends the messages at the rate that Twilio is expecting and can handle.
- Look to AE/leadership to assist with increased MPS rate discussions with Twilio.
Please note: higher throughput pricing needs to go through a deal desk.
- Ensure you are sticking to the 160 character limit, and aware of special characters double-counting (i.e. \ ^ &#126;). 
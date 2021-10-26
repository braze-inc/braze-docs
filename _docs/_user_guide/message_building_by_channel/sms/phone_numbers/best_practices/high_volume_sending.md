---
nav_title: High-Volume Sending
article_title: High-Volume SMS Sending
page_order: 4
description: "This reference article covers high-volume sending best practices for SMS messaging."
page_type: reference
channel:
  - SMS
  
---

# High-volume sending

Plan on doing some high-volume sending? We have some best practices for you to ensure it runs smoothly:

- Adjust the delivery speed rate limiting for your campaign/canvases as needed, based on target audience size. This will ensure that (1) you reach the send volume that you need and (2) Braze sends the messages at the rate that the phone numbers you have provisioned can handle
- Ensure you are sticking to the 160 character limit, and aware of special characters double-counting (i.e. \ ^ &#126;). Messages beyond 160 characters will result in multiple messages, effectively cutting your send speed in half.

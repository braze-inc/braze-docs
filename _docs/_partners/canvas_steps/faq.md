---
nav_title: FAQs
article_title: Frequently asked questions for audience sync
description: ""
page_order: 80
Tool:
  - Canvas

---

# Frequently asked questions

### How long does it take for my audiences to populate in my Audience Sync partner dashboard? 

The time it takes to populate an audience depends on the specific partner.

All networks will process the requests from Braze and attempt to match users. This process can typically take anywhere from 6-48 hours.

You can check the specific time range within the Troubleshooting section within the documentation for each Audience Sync partner. 

### What type of first-party data can I use in my Audience Sync?

The specific fields that are used for each partner may vary depending on the partner requirements. 

For example, when you configure an Audience Sync to Facebook, you will be able to use a wide variety of first-party fields like email, phone, first name, and last name whereas with Snapchat you will only be able to select either email, phone, or mobile advertiser ID. 

It is important to note that the user fields you can select to sync correlate with Braze standard attributes, along with the mobile advertising IDs. You will need to ensure that you are appropriately passing this data via our SDKs or APIs. 

### What occurs when my data is being processed to send to each Audience Sync partner?

The data that you select to send into your Audience Sync destination will be normalized. Each partner may have different specifications for data normalization based on their API requirements, so please review each partner specific endpoint for further details.

In addition, Braze will hash all data before syncing users with our Audience Sync partners, will ensure that all PII is hashed using SHA256.

### What are the most common errors that can occur when creating and managing my Audience Syncs?

Invalid Token: 

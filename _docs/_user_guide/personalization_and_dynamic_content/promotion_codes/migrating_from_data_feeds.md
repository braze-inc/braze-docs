---
nav_title: Migrating from data feeds
article_title: Migrating from Data Feeds to Promotion Codes
page_order: 10
description: "This reference article provides guidance on migrating from Data Feeds to promotion codes."
---

# Migrating from Data Feeds to promotion codes

{% alert note %}
Data Feeds is being deprecated. Braze recommends that customers who use Data Feeds move over to promotion code lists.
{% endalert %}

> This page guides you through migrating from Data Feeds to promotion codes. This is a straightforward process that involves manually creating promotion code lists with the information from your Data Feeds and updating your message references accordingly.

## Features and functionality

There are a few differences between promotion code lists and Data Feeds.

| Feature          | Promotion codes | Data Feeds   |
|------------------|-----------------|--------------|
| Descriptions     | Yes             | No           |
| Expiration Dates | Yes             | No           |
| Creation Method  | Uploading a CSV | Pasting text |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## How to migrate

To replace a Data Feed with a promotion code list, do the following: 

1. Go to **Data Settings** and select **Create Promotion Code List**.
2. [Set up your promotion code list]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/promotion_codes).
3. Navigate to your messages that previously referenced the Data Feed and update it to use the promotion code list.
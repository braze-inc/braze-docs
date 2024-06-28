---
nav_title: Migrating from Data Feeds to Promotion Codes
article_title: Migrating from Data Feeds to Promotion Codes
page_order: 0
description: "This reference article provides guidance on migrating from data feeds to promotion codes."
---

# Migrating from data feeds to promotion codes

{% alert note %}
Data feeds is being deprecated. Braze recommends that customers who use data feeds move over to our promotion codes.
{% endalert %}

> Migrating from data feeds to promotion codes takes time, but it's a straightforward process! This involves manually creating promotion code lists with the information from your data feeds and updating your message references accordingly.

There are two main differences between the promotion codes and data feeds:

- You can use descriptions and expiration dates with promotion codes, not with data feeds.
- You create promotion codes by uploading a CSV, whereas you create data feeds by pasting text.

## How to migrate

To replace a data feed with a promotion code list, do the following: 

1. Go to **Data Settings** and select **Create Promotion Code List**.
2. [Set up your promotion code]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/promotion_codes).
3. Navigate to your messages that previously referenced the data feed and update it to use the promotion code list.
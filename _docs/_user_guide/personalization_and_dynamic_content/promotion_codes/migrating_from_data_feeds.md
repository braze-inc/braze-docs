---
nav_title: Migrating from Data Feeds to Promotion Codes
article_title: Migrating from Data Feeds to Promotion Codes
page_order: 0
description: "This reference article provides guidance on migrating from Data Feeds to promotion codes."
---

# Migrating from Data Feeds to promotion codes

{% alert note %}
Data Feeds is being deprecated. Braze recommends that customers who use Data Feeds move over to our promotion codes.
{% endalert %}

> Migrating from Data Feeds to promotion codes takes time, but it's a straightforward process! This involves manually creating promotion code lists with the information from your Data Feeds and updating your message references accordingly.

There are two main differences between the promotion codes and Data Feeds:

- You can use descriptions and expiration dates with promotion codes, not with Data Feeds.
- You create promotion codes by uploading a CSV, whereas you create Data Feeds by pasting text.

## How to migrate

To replace a Data Feed with a promotion code list, do the following: 

1. Go to **Data Settings** and select **Create Promotion Code List**.
2. [Set up your promotion code]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/promotion_codes).
3. Navigate to your messages that previously referenced the Data Feed and update it to use the promotion code list.
---
nav_title: Catalog
article_title: Catalog
page_order: 2
description: "Learn how to use catalogs as a data source for personalizing your Braze messages with non-user data like product details, content feeds, and pricing."
---

# Catalog

> Reference non-user data in your messages by connecting to catalogs. Catalogs store structured datasets — such as product information, restaurant listings, or content feeds — that you can access through Liquid to personalize any message.

## How it works

{% raw %}
After importing data into a catalog (through CSV or API), reference catalog items in your messages using the `items` Liquid tag. For example, to pull a product name from a catalog called `products`:

```liquid
{% catalog_items products {{${product_id}}} %}
{{items[0].name}} is back in stock!
```
{% endraw %}

Catalogs support up to 1,000 fields per item and can store millions of rows, making them suitable for large product inventories and content libraries.

## Common use cases

| Use case | Description |
| --- | --- |
| Product details | Insert names, descriptions, prices, and images from a product catalog |
| Restaurant or store listings | Personalize messages with location-specific details |
| Content recommendations | Reference articles, videos, or other media items |
| Event information | Pull event dates, venues, and descriptions into messages |
| Tier-based offers | Match promotions to a user's membership level or segment |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Catalog triggers

Catalogs also power automated messaging through catalog triggers. Set up back-in-stock notifications and price drop notifications to automatically message users when catalog items change.

For more information, see [Catalog triggers]({{site.baseurl}}/user_guide/data/activation/catalogs/catalog_triggers/).

## Selections

Use selections to group catalog items by filters you define. For example, create a selection of items under $20 or items in a specific category, then reference the filtered set in your messages.

For more information, see [Selections]({{site.baseurl}}/user_guide/data/activation/catalogs/selections/).

## Getting started

To create and manage catalogs, see [Catalogs]({{site.baseurl}}/user_guide/data/activation/catalogs/). To learn how to reference catalog data in your messages, see [Using catalogs in a message]({{site.baseurl}}/user_guide/data/activation/catalogs/use/).

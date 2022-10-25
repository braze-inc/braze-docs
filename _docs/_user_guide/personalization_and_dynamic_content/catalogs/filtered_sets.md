---
nav_title: Filtered Sets
article_title: Filtered Sets
page_order: 2
description: "This reference article covers how to create and use filtered sets with your catalogs to reference data in your Braze campaigns."
---

# Filtered sets

Filtered sets are groups of data that can be used to personalize a message for each user in your campaign. After creating a [catalog]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalog/), you can further reference this data by incorporating filtered sets in your Braze campaigns.

{% alert important %}
Filtered sets are currently in early access. Contact your Braze account manager if you are interested in participating in the early access.
{% endalert %}

To create a filtered set, select your catalog and click **Create Filtered Set**. Select the catalog column from the **Filter Field** dropdown. Next, select the operator, and enter the attribute. Continue to add any additional filters as needed. Click **Create Filtered Set**, and the filtered set will display above the catalog data. Now, you can reference this filtered set in your messaging.

If you use any Liquid in catalogs, such as custom attributes and custom events, this can result in different results returned for each user in your filtered set.

![The Filtered Sets section in an example catalog "restaurants".][1]{: style="max-width:85%;"}

## Use case

Let's say we want to recommend autumn sale items from a popular clothing store to multiple customers. With filtered sets, you can set up information that is personalized to each customer. 

Using a catalog with the clothing store's information for clothing items, prices, and ratings, we can create a filtered set to recommend clothing items with ratings greater than four stars.

![An example of a filtered set for a clothing store with three filters: one that identifies an item price, an item, and the rating.][2]{: style="max-width:85%;"}

To use this catalog in a campaign, you can insert this filtered set using the **Add Personalization** modal in the message composition section of building a campaign. In our example, we've selected the catalog with store product information with the filtered set for fall sale favorites. 

![Personalization modal that shows the filtered set "Fall_Sale_Favorites" with three filter settings for price, sale, and rating.][4]{: style="max-width:60%;"}

Using the set personalization and a Content Card campaign, we can send three sale items with a rating greater than four stars for each customer at the clothing store.

![A Content Card for a test user with the title "Check out some fall favorites" followed by three recommended item names, sale prices, and ratings.][3]{: style="max-width:50%;"}

[1]: {% image_buster /assets/img_archive/catalog_filtered_sets1.png %}
[2]: {% image_buster /assets/img_archive/catalog_filtered_sets2.png %}
[3]: {% image_buster /assets/img_archive/catalog_filtered_sets3.png %}
[4]: {% image_buster /assets/img_archive/catalog_filtered_sets4.png %}
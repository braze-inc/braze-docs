---
nav_title: Filtered Sets
article_title: Filtered Sets
page_order: 2
description: "This reference article covers how to create and use filtered sets with your catalogs to reference data in your Braze campaigns."
---

# Filtered sets

After creating a [catalog]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalog/), you can further reference this data by incorporating filtered sets in your Braze campaigns. Filtered sets are groups of data that can be used to personalize a message for each user in your campaign.

{% alert important %}
Filtered sets are currently in early access. Contact your Braze account manager if you are interested in participating in the early access.
{% endalert %}

To create a filtered set, select your catalog and click **Create Filtered Set**. Select the catalog column from the **Filter Field** dropdown. Next, select the operator, and enter the attribute. Continnue to add any additional filters as needed. This filtered set will determine the information set up for each user. Click **Create Filtered Set**, and the filtered set will display above the catalog data.

![The Filtered Sets section in an example catalog "restaurants".][1]{: style="max-width:85%;"}

## Use case

Let's say we want to recommend meals from a popular restaurant to multiple customers. With filtered sets, you can set up information that is personalized to each customer. 

Using a catalog with the restaurant's information for menu items, prices, and product types, we can create a filtered set to recommend a meal based on the latest product type a customer has viewed.

![An example of a filtered set for a restaurant with two filters: one that identifies a meal recommendation, and one that identifies a customer's most recently viewed category.][2]{: style="max-width:85%;"}

Next, you can insert this filtered set using the **Add Personalization** modal for a Content Card campaign that returns the three meal recommendations for a customer:

![A Content Card for a test user with the title "Check out some new stuff" followed by three recommended meals and prices.][3]{: style="max-width:50%;"}

[1]: {% image_buster /assets/img_archive/catalog_filtered_sets1.png %}
[2]: {% image_buster /assets/img_archive/catalog_filtered_sets2.png %}
[3]: {% image_buster /assets/img_archive/catalog_filtered_sets3.png %}
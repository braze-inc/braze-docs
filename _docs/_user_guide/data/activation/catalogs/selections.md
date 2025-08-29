---
nav_title: Selections
article_title: Selections
page_order: 5
description: "This reference article covers how to create and use selections with your catalogs to reference data in your Braze campaigns."
---

# Selections

> Selections are groups of data that can be used to personalize a message for each user in your campaign. When you use a selection, you’re essentially setting up custom filters based on specific columns in your catalog. This could include filters for brand, size, location, date added, and more. It gives you control over what you’re showing to users by allowing you to define criteria that items must meet first.<br><br>This page covers how to create and use selections with your catalogs.

After creating a [catalog]({{site.baseurl}}/user_guide/data/activation/catalogs/), you can further reference your catalog data by incorporating selections in your Braze campaigns or recommendations.

![The Selections section in an example catalog.]({% image_buster /assets/img_archive/catalog_selections1.png %})

## Things to know

- You can create up to 30 selections per catalog.
- You can add up to 10 filters per selection.
- Selections are great for refining recommendations from Braze catalog data. If you're looking for inspiration, check out [About item recommendations]({{site.baseurl}}/user_guide/brazeai/recommendations/) for example use cases.

## Creating a selection

To create a selection, do the following.

1. Go to **Catalogs** and select your catalog from the list.
2. Select the **Selection** tab and click **Create Selection**.
3. Give your selection a name and optional description.
4. For **Filter Field**, select the catalog column you want to filter by. String fields with more than 1,000 characters can't be selected for filters.
5. Finish defining your filter criteria by selecting the relevant operator (for example, "equals" or "does not equal") and attribute.
6. In the **Sort type** section, determine how results are sorted. By default, results are returned in no particular order. To specify sorting by a specific field, turn off **Randomize Sort Order** and specify the **Sort Field** and **Sort Order** (ascending or descending).
7. In the **Results limit** section, enter the results (up to 50).
8. Select **Create Selection**.

### Test and preview

After creating a selection, you can use the **Preview for user** section to view what a selection would return for either a random user or a specific user. For selections that use personalization, you can only view the preview after selecting a user.

### Liquid in selection results

Using any Liquid in catalogs, such as custom attributes and custom events, can result in different results returned for each user in your selection. 

{% alert note %}
Connected Content Liquid isn't supported in these filter settings.
{% endalert %}

![Filter settings for catalog selection where the attribute is set to a Liquid custom attribute.]({% image_buster /assets/img_archive/catalog_selections7.png %})

## Using selections in messaging

After creating your selection, personalize your messages with Liquid to insert the filtered items from that catalog. You can have Braze generate the Liquid for you from the personalization window found in message composers:

1. In any message composers that support personalization, select <i class="fa-solid fa-circle-plus" style="color: #12aec5;" title="Add personalization"></i> to open the personalization window.
2. For **Personalization Type**, select **Catalog Items**.
3. Select your catalog name.
4. For **Item selection method**, select **Use a selection**.
4. Select your selection from the list.
5. For **Information to Display**, select which fields from the catalog should be included for each item.
6. Select the **Copy** icon and paste the Liquid wherever it needs to go in your message.

![The Add Personalization modal with the following selections: "Catalog Items" for "Personalization Type", "Games" for "Catalog Name", "Selections" for "Selection Type", "game_selection" for "Selection", and "title" and "description_en" for "Information to Display".]({% image_buster /assets/img_archive/catalog_selections6.png %}){: style="max-width:70%;"}

## Use case

Let's say you own a meal delivery service and want to send a personalized message to your users who have specific meal preferences based on their most recently viewed food category. 

Using a catalog with your meal delivery service's information for the meal name, price, image, and category of the meal, you can create a selection to recommend three meals based on a user's most recently viewed category.

![An example of a selection for a meal delivery service with two filters: one that identifies a product type as a meal, and one that identifies the category as the most recently viewed. The selection is set to randomize the order in which the three results are returned.]({% image_buster /assets/img_archive/catalog_selections2.png %}){: style="max-width:90%;"}

To use this catalog and selection in a campaign, use the **Add Personalization** modal in the message composition section of building a campaign. In this example, we've selected the catalog with your meal delivery service's information, and the selection for meal recommendations based on the most recently viewed category. This allows us to display the meal name and price. To further build your message, you can use the selection to also add an image of the first recommended meal.

![A Content Card with the header "You will LOVE these highly rated meals!" with the selection "recommendations_be_recent_category" in message composition section.]({% image_buster /assets/img_archive/catalog_selections3.png %}){: style="max-width:90%;"}

For example, say you have a user whose most recently viewed category is "Chicken". Using the set personalization and a Content Card campaign, you can send three meal recommendations that include chicken for this user.

![A Content Card with an image of char-grilled lemon chicken, and a list of three meal recommendations that include chicken based on the user's most recently viewed category.]({% image_buster /assets/img_archive/catalog_selections4.png %}){: style="max-width:90%;"}

Using the same personalization, you can also send three meal recommendations for a user whose most recently viewed category is "Beef".

![A Content Card with an image of beef stroganoff, and a list of two meal recommendations that include beef based on the user's most recently viewed category.]({% image_buster /assets/img_archive/catalog_selections5.png %}){: style="max-width:90%;"}



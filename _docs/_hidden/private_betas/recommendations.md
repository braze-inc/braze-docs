---
nav_title: Item Recommendations
article_title: Item Recommendations
permalink: "/recommendations/"
description: "This reference article covers how to create an Item Recommendation for most popular products."
hidden: true
---

# Item Recommendations

You can use Item Recommendations to calculate the most popular products or create personalized AI recommendations for a specific [catalog]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/). After you create your recommendation, you can use personalization to insert those products into your messages.

## Prerequisites

You must have at least one [catalog][catalog] to take advantage of Item Recommendations.
You must have purchase data on Braze (custom events or the purchase object) that includes a reference to unique product IDs stored in a catalog. 

## Creating an Item Recommendation

To create an item recommendation:

1. Go to **Analytics** > **Item Recommendation**.
2. Select **Create Prediction** > **Item Recommendation**.

You can also choose to create a recommendation straight from an individual catalog. From the **Catalogs** page, select your catalog and click **Create Recommendation**.

### Step 1: Add recommendation details

First, give your recommendation a name and optional description.

![][1]

### Step 2: Define your recommendation

Next, select the recommendation type. Both recommendation types use the last 6 months of purchase data.

- **Most popular:** Calculates the items from the catalog that are purchased most often by users in the entire workspace.
- **Personalized:** Uses transformers, a new kind of deep learning, to predict each individual user's next most likely set of items to purchase. We calculate up to 30 of the next most likely items ranked from most to least likely.

![][2-1]

If not already populated, select the [catalog][catalog] that this recommendation will pull items from.

#### Add a selection

If you'd like more control over your recommendation, choose a [selection]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/selections/) to apply custom filters. Selections filter recommendations by specific columns in your catalog (such as brand, size, or location). If your selection contains Liquid, it can't be used in your recommendation.

![][2-2]

{% alert tip %}
If you can't find your selection, make sure it's set up in your catalog first.
{% endalert %}

### Step 3: Select how you track user purchases

Next, select the option your company most frequently uses to track purchases. This can either be through purchase events (with the [Purchase Object]({{site.baseurl}}/api/objects_filters/purchase_object/)) or custom events.

If you choose **Custom Event**, select your event from the list.

![][3]

### Step 4: Choose the corresponding property name {#property-name}

To create a recommendation, you need to tell Braze which field of your purchase event (purchase object or custom event) has the unique indentifier that matches the `id` field of the catalog. Select this field for the **Property Name**.

The **Property Name** field will be pre-populated with a list of fields sent through the SDK to Braze. If enough data is provided, these properties will also be ranked in order of probability to be the correct property. Select the one that corresponds to the `id` field of the catalog.

![][4]

#### Requirements

There are some requirements for selecting your property:

- Must map to the `id` field of your selected catalog.
- **If you selected Purchase Object:** Must be the `product_id` or a field of your purchase event's `properties`. This field can be nested.
- **If you selected Custom Event:** Must be a field of your custom event's `properties`. This field can be nested.

### Step 5: Train the recommendation

When you're ready, select **Create Recommendation**. This process will take a few minutes to complete. You will receive an email update when the recommendation is successfully trained, or an explanation of why the creation may have failed.

You can find the recommendation on the **Predictions** page, where you can then edit or archive it as needed. Only one most popular products recommendation can be created per catalog.

## Using recommendations in messaging

![][10]{: style="max-width:30%;float:right;margin-left:15px;"}

After your recommendation finishes training you will receive an email letting you know it succeeded. Then, you can personalize your messages with Liquid to insert the most popular products in that catalog. The Liquid can be generated for you by the personalization window found in message composers:

1. In any message composers that support personalization, click <i class="fa-solid fa-circle-plus" style="color: #12aec5;" title="Add personalization"></i> to open the personalization window.
2. For **Personalization Type**, select **Item Recommendation**.
3. For **Item Recommendation Name**, select the recommendation you just created.
4. For **Number of Predicted Items**, enter how many top products you'd like to be inserted. For example, you can display the top three most purchased items.
5. For **Information to Display**, select which fields from the catalog should be included for each item. The values for these fields for each item will be drawn from the catalog associated with this recommendation.
6. Click the **Copy** icon and paste the Liquid wherever it needs to go in your message.

[1]: {% image_buster /assets/img/item_recs_1.png %}
[2-1]: {% image_buster /assets/img/item_recs_2-1.png %}
[2-2]: {% image_buster /assets/img/item_recs_2-2.png %}
[3]: {% image_buster /assets/img/item_recs_3.png %}
[4]: {% image_buster /assets/img/item_recs_4.png %}
[10]: {% image_buster /assets/img/add_personalization.png %}
[catalog]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/

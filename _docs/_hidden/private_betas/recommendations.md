---
nav_title: Item Recommendations
article_title: Item Recommendations
permalink: "/recommendations/"
description: "This reference article covers how to create an Item Recommendation for most popular products."
---

# Item Recommendations

You can use Item Recommendations to calculate the most popular products in a specific [catalog]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/). After you create your recommendation, you can use personalization to insert those top products into your messages.

{% alert important %}
Item Recommendations is currently in early access. Contact your Braze customer success manager if you're interested in participating in the early access.
{% endalert %}

## Prerequisites

You must have at least one [catalog]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/) to take advantage of Item Recommendations.

## Creating an Item Recommendation for most popular products

### Step 1: Create a new recommendation

From the **Predictions** page, select **Create Prediction** > **Item Recommendation**. You can also choose to create a recommendation straight from an individual catalog. From the **Catalogs** page, select your catalog and click **Create Recommendation**.

### Step 2: Specify catalog details

1. Enter a name and optional description for your recommendation.
2. If not already populated, select the catalog for which this recommendation will calculate the most popular products.
3. For the recommendation **Type**, select **Most popular**.
4. Select the [Product IDs](#product-ids).

![][1]{: style="max-width:80%;"}

#### Product IDs

To create a recommendation, you need to tell Braze where to find the product IDs in the purchase events. The unique values in the `id` field of the catalog must also be in the `product_id` field of the purchase events, or in the top-level fields of the `properties` of those events. The **Product IDs** field will be pre-populated with those fields sent through the SDK to Braze. Select the one that corresponds to the product IDs.

{% alert important %}
The product IDs must be in a top-level field of the properties of the purchase event. No nested properties or custom event fields are supported at this time.
{% endalert %}

### Step 3: Train the recommendation

When you're ready, select **Create Recommendation**. This process will take a few minutes to complete. You will receive an email update when the recommendation is successfully trained, or an explanation of why the creation may have failed.

You can find the recommendation on the **Predictions** page, where you can then edit or archive it as needed. Only one most popular products recommendation can be created per catalog.

## Using recommendations in messaging

![][2]{: style="max-width:30%;float:right;margin-left:15px;"}

After your recommendation finishes training, you can personalize your messages with Liquid to insert the most popular products in that catalog. The liquid can be generated for you by the personalization window found in message composers:

1. In any message composers that support personalization, click <i class="fa-solid fa-circle-plus" style="color: #12aec5;" title="Add personalization"></i> to open the personalization window.
2. For **Personalization Type**, select **Item Recommendation**.
3. For **Item Recommendation Name**, select the recommendation you just created.
4. For **Number of Predicted Items**, enter how many top products you'd like to be inserted. For example, you can display the top three most purchased items.
5. For **Information to Display**, select which fields from the catalog should be included for each item. This information corresponds to the columns in your uploaded CSV file used to generate your catalog.
6. Click **Copy** and paste the Liquid wherever it needs to go in your message.

[1]: {% image_buster /assets/img/most_popular_products.png %}
[2]: {% image_buster /assets/img/most_popular_products_personalize.png %}

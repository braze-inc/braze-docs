---
nav_title: Item Recommendations
article_title: Item Recommendations
permalink: "/recommendations/"
description: "This reference article covers how to create an Item Recommendation for most popular products."
hidden: true
---

# Item Recommendations

You can use Item Recommendations to calculate the most popular products or create personalized AI recommendations for a specific [catalog]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/). After you create your recommendation, you can use personalization to insert those products into your messages.

{% alert important %}
Most popular product recommendations is currently in early access.<br>
Personalized AI recommendations is currently in beta.<br><br>
Contact your Braze customer success manager if you're interested in participating in the early access or beta.
{% endalert %}

## Prerequisites

You must have at least one [catalog]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/) to take advantage of Item Recommendations.

## Creating an Item Recommendation

From the **Predictions** page, select **Create Prediction** > **Item Recommendation**.

{% alert note %}
If you are using our [updated navigation]({{site.baseurl}}/navigation), you can find **Predictions** under **Analytics** and **Catalogs** under **Data Settings**.
{% endalert %}

You can also choose to create a recommendation straight from an individual catalog. From the **Catalogs** page, select your catalog and click **Create Recommendation**.

### Step 1: Define your recommendation

1. Enter a name and optional description for your recommendation.
2. If not already populated, select the catalog for which this recommendation will calculate the most popular products.
3. Select the recommendation type:
   - **Most popular:** Calculates the items from the catalog that are purchased most often by users in the entire workspace.
   - **Personalized:** Uses transformers, a new kind of deep learning, to predict each individual user's next most likely set of items to purchase. We calculate up to 30 of the next most likely items ranked from most to least likely.

Both recommendation types use the last 6 months of purchase data.

![][1]

### Step 2: Select how you track user purchases

Next, select the option your company most frequently uses to track purchases. This can either be through purchase events (with the [Purchase Object]({{site.baseurl}}/api/objects_filters/purchase_object/)) or custom events.

If you choose **Custom Event**, select your event from the list.

![][2]

### Step 3: Choose the corresponding purchase ID {#product-ids}

To create a recommendation, you need to tell Braze where to find the purchase IDs in your event. The unique values in the `id` field of the catalog must also be in the `product_id` field of the purchase events, or in the top-level fields of the `properties` of those events. 

The **Purchase IDs** field will be pre-populated with those fields sent through the SDK to Braze. Select the one that corresponds to the product IDs.

![][3]

{% alert important %}
The product IDs must be in a top-level field of the properties of the purchase event. No nested properties are supported at this time.
{% endalert %}

### Step 4: Train the recommendation

When you're ready, select **Create Recommendation**. This process will take a few minutes to complete. You will receive an email update when the recommendation is successfully trained, or an explanation of why the creation may have failed.

You can find the recommendation on the **Predictions** page, where you can then edit or archive it as needed. Only one most popular products recommendation can be created per catalog.

## Using recommendations in messaging

![][4]{: style="max-width:30%;float:right;margin-left:15px;"}

After your recommendation finishes training, you can personalize your messages with Liquid to insert the most popular products in that catalog. The Liquid can be generated for you by the personalization window found in message composers:

1. In any message composers that support personalization, click <i class="fa-solid fa-circle-plus" style="color: #12aec5;" title="Add personalization"></i> to open the personalization window.
2. For **Personalization Type**, select **Item Recommendation**.
3. For **Item Recommendation Name**, select the recommendation you just created.
4. For **Number of Predicted Items**, enter how many top products you'd like to be inserted. For example, you can display the top three most purchased items.
5. For **Information to Display**, select which fields from the catalog should be included for each item. This information corresponds to the columns in your uploaded CSV file used to generate your catalog.
6. Click the **Copy** icon and paste the Liquid wherever it needs to go in your message.

[1]: {% image_buster /assets/img/item_recommendation_1.png %}
[2]: {% image_buster /assets/img/item_recommendation_2.png %}
[3]: {% image_buster /assets/img/item_recommendation_3.png %}
[4]: {% image_buster /assets/img/add_personalization.png %}

---
nav_title: AI Item Recommendations
article_title: AI Item Recommendations
page_order: 100
alias: "/recommendations/"
description: "This reference article covers how to create an AI Item Recommendation for items in a catalog."
---

# AI item recommendations

> Learn how to create an AI Item Recommendation for items in a catalog.

You can use AI item recommendations to calculate the most popular products or create personalized AI recommendations for a specific [catalog]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/). After you create your recommendation, you can use personalization to insert those products into your messages.

## Prerequisites

- You must have at least one [catalog][catalog] to use AI item recommendations.
- You must have purchase or event data on Braze (custom events or the purchase object) that includes a reference to unique product IDs stored in a catalog.

### Important notes

This article describes the free version of AI item recommendations. When using the free version:

- You can create one recommendation per [recommendation type](#recommendation-type) in a workspace.
- The items recommended to each user in a recommendation update once a week. The recommendation model itself will automatically update once a month.

## Creating an AI Item Recommendation

To create an item recommendation:

1. Go to **Analytics** > **AI Item Recommendation**.
2. Select **Create Prediction** > **AI Item Recommendation**.

You can also choose to create a recommendation straight from an individual catalog. Select your catalog from the **Catalogs** page and click **Create Recommendation**.

### Step 1: Add recommendation details

First, give your recommendation a name and optional description.

![][1]

### Step 2: Define your recommendation {#recommendation-type}

Next, select the recommendation type. Both recommendation types use the last 6 months of item interaction (purchase or custom event) data.

- **Most popular:** Calculates the items from the catalog that users interact with most often in the entire workspace. The interaction is defined by the event chosen in Step 3.
- **Personalized:** Uses transformers, a new kind of deep learning, to predict each user's next most likely set of items to purchase or interact with. The interaction is defined by the event chosen in Step 3. We calculate up to 30 of the next most likely items ranked from most to least likely.

<!--
**Most recent:** Surfaces each user's most recent purchases.
-->

![][2-1]

If not already populated, select the [catalog][catalog] that this recommendation will pull items from.

#### Add a selection

If you'd like more control over your recommendation, choose a [selection]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/selections/) to apply custom filters. Selections filter recommendations by specific columns in your catalog, such as brand, size, or location. If your selection contains Liquid, the selection can't be used in your recommendation.

![][2-2]

{% alert tip %}
If you can't find your selection, make sure it's set up in your catalog first.
{% endalert %}

### Step 3: Select the interaction to drive recommendations

Next, select the event you want this recommendation to optimize for. This event is usually a purchase, but it can also be any kind of interaction with an item.

You can optimize for:

- Purchase events with the [Purchase Object]({{site.baseurl}}/api/objects_filters/purchase_object/)
- Custom events that represent a purchase
- Custom events that represent any other item interaction (such as product views, clicks, or media plays)

If you choose **Custom Event**, select your event from the list.

![][3]

### Step 4: Choose the corresponding property name {#property-name}

To create a recommendation, you need to tell Braze which field of your interaction event (purchase object or custom event) has the unique indentifier that matches the `id` field of an item in the catalog. Not sure? See [heading name](#heading).

Select this field for the **Property Name**.

The **Property Name** field will be pre-populated with a list of fields sent through the SDK to Braze. If enough data is provided, these properties will also be ranked in order of probability to be the correct property. Select the one that corresponds to the `id` field of the catalog.

![][4]

#### Requirements

There are some requirements for selecting your property:

- Must map to the `id` field of your selected catalog.
- **If you selected Purchase Object:** Must be the `product_id` or a field of your interaction event's `properties`.
- **If you selected Custom Event:** Must be a field of your custom event's `properties`.
- The field can be nested
- The field can be in an array (of multiple catalog items within a single event). It will automatically be flattened.

#### Example mappings

The following example mappings both refer to this sample catalog:

<style type="text/css">
.tg td{word-break:normal;}
.tg th{word-break:normal;font-size: 14px; font-weight: bold; background-color: #f4f4f7; text-transform: lowercase; color: #212123; font-family: "Sailec W00 Bold",Arial,Helvetica,sans-serif;}
.tg .tg-0pky{border-color:inherit;text-align:left;vertical-align:top;word-break:normal}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-0pky">id</th>
    <th class="tg-0pky">title</th>
    <th class="tg-0pky">price</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-0pky">ADI-BL-7</td>
    <td class="tg-0pky">Adidas Black Size 7</td>
    <td class="tg-0pky">100.00 USD</td>
  </tr>
  <tr>
    <td class="tg-0pky">ADI-RD-8</td>
    <td class="tg-0pky">Adidas Red Size 8</td>
    <td class="tg-0pky">100.00 USD</td>
  </tr>
  <tr>
    <td class="tg-0pky">ADI-WH-9</td>
    <td class="tg-0pky">Adidas White Size 9</td>
    <td class="tg-0pky">100.00 USD</td>
  </tr>
  <tr>
    <td class="tg-0pky">ADI-PP-10</td>
    <td class="tg-0pky">Adidas Purple Size 10</td>
    <td class="tg-0pky">75.00 USD</td>
  </tr>
</tbody>
</table>

{% tabs %}
{% tab Custom event %}

Let's say you want to use the custom event `added_to_cart` so that you can recommend similar products before the customer checks out. The event `added_to_cart` has an event property of `product_sku`.

Then the `product_sku` property must include at least one of the values from the `id` column in the sample catalog: "ADI-BL-7", "ADI-RD-8", "ADI-WH-9", or "ADI-PP-10". You don't need events for every catalog item, but you need some of them so that the recommendation engine has enough content to work with.

##### Example custom event object

This event has `"product_sku": "ADI-BL-7"`, which matches the first item in the sample catalog.

```json
{
  "events" : [
    {
      "external_id" : "user1",
      "app_id" : "your-app-id",
      "name" : "added_to_cart",
      "time" : "2024-07-16T19:20:30+01:00",
      "properties" : {
        "product_sku": "ADI-BL-7"
      }
    }
  ]
}
```

{% endtab %}
{% tab Purchase object %}

A purchase object gets passed through the API when a purchase has been made.

In terms of mapping, a similar logic applies for purchase objects as it does for custom events, except you can choose between using the purchase object's `product_id` or a field in the `properties` object.

Remember, you don't need events for every catalog item, but you do need some of them so that the recommendation engine has enough content to work with.

##### Example purchase object mapped to product ID

This event has `"product_id": "ADI-BL-7`, which maps to the first item in the catalog.

```json
{
  "purchases": [
    {
      "external_id": "user1",
      "app_id": "11ae5b4b-2445-4440-a04f-bf537764c9ad",
      "product_id": "ADI-BL-7",
      "currency": "USD",
      "price": 100.00,
      "time": "2024-07-16T19:20:30+01:00",
      "properties": {
        "color": "black",
        "checkout_duration": 180,
        "size": "7",
        "brand": "Adidas"
      }
    }
  ]
}
```

##### Example purchase object mapped to a properties field

This event has a property of `"sku": "ADI-RD-8"`, which maps to the second item in the catalog.

```json
{
  "purchases": [
    {
      "external_id": "user1",
      "app_id": "11ae5b4b-2445-4440-a04f-bf537764c9ad",
      "product_id": "shoes",
      "currency": "USD",
      "price": 100.00,
      "time": "2024-07-16T19:20:30+01:00",
      "properties": {
        "sku": "ADI-RD-8",
        "color": "red",
        "checkout_duration": 180,
        "size": "8",
        "brand": "Adidas"
      }
    }
  ]
}
```

{% endtab %}
{% endtabs %}

### Step 5: Train the recommendation

When you're ready, select **Create Recommendation**. This process can take anywhere from 10 minutes to 36 hours to complete. You will receive an email update when the recommendation is successfully trained or an explanation of why the creation may have failed.

You can find the recommendation on the **Predictions** page, where you can then edit or archive it as needed. Recommendations will automatically retrain once every month.

## Analytics

You can view analytics for your recommendation to see which items users were recommended and how accurate the recommendation model was.

1. Go to **Analytics** > **Item Recommendation**.
2. Select your recommendation from the list.

At the top of the page, you can find statistics about your recommendation, such as precision and coverage.

![][5]

These metrics are defined in the following table. 

| Metric              | Description |
| ------------------- | ---------- |
| Precision           | The percentage of time the model correctly guessed the next item a user purchased. Precision is heavily dependent on your specific catalog size and mix, and should be used as a guide to understand how often the model is correct.<br><br>In past testing, we have seen models perform well with precision numbers ranging from 6-20%. This metric updates when the model next retrains.  |
| Coverage            | What percentage of available items in the catalog are recommended to at least one user. You can expect to see higher item coverage with personalized item recommendations over most popular ones. |
| Recommendation type | Percentage of users who will receive personalized recommendations versus the fallback of most popular items. The fallback is sent to users who don’t have enough data to generate a personalized recommendation. |
{: .reset-td-br-1 .reset-td-br-2}

The next section shows a breakdown of items in the catalog, split into two columns:

- **Personalized items:** This column lists each item in the catalog in order of most often to least often recommended to users. This column also shows how many users were assigned each item by the model.
- **Most Popular items:** This column lists each item in the catalog in order of popularity. Popularity here refers to items in the catalog that users interact with most often in the entire workspace.

![][6]

For your reference, the final section shows a summary of your chosen recommendation configuration, as well as when the recommendation was last updated.

![][7]{: style="max-width:45%" }

## Using recommendations in messaging

![][10]{: style="max-width:30%;float:right;margin-left:15px;"}

After your recommendation finishes training, you can personalize your messages with Liquid to insert the most popular products in that catalog. The Liquid can be generated for you by the personalization window found in message composers:

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
[5]: {% image_buster /assets/img/item_recs_analytics_1.png %}
[6]: {% image_buster /assets/img/item_recs_analytics_2.png %}
[7]: {% image_buster /assets/img/item_recs_analytics_3.png %}
[10]: {% image_buster /assets/img/add_personalization.png %}
[catalog]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/

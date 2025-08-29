---
nav_title: AI recommendations
article_title: Creating AI Item Recommendations
description: "This reference article covers how to create an AI item recommendation for items in a catalog."
page_order: 1
---

# Creating AI item recommendations

> Learn how to create an AI recommendation engine from items in your catalog.

## About AI item recommendations

Use AI item recommendations to calculate the most popular products or create personalized AI recommendations for a specific [catalog]({{site.baseurl}}/user_guide/data/activation/catalogs/). After creating your recommendation, you can use personalization to insert those products into your messages.

{% alert tip %}
[AI Personalized recommendations](#recommendation-types) work best with hundreds or thousands of items and typically at least 30,000 users with purchase or interaction data. This is only a rough guide and can vary. The other recommendation types can work with less data.
{% endalert %}

## Creating an AI item recommendation

### Prerequisites

Before you start, you'll need to complete the following:

- You must have at least one [catalog]({{site.baseurl}}/user_guide/data/activation/catalogs/) to use any of the recommendation types described below.
- You must have purchase or event data on Braze (custom events or the purchase object) that includes a reference to unique product IDs stored in a catalog.

### Step 1: Create a new recommendation

You can create an AI item recommendation from either place in the dashboard:

{% tabs local %}
{% tab From the navigation menu %}
1. Go to **Analytics** > **AI Item Recommendation**.
2. Select **Create Prediction** > **AI Item Recommendation**.
{% endtab %}

{% tab From a catalog %}
You can also choose to create a recommendation directly from an individual catalog. Select your catalog from the **Catalogs** page, then select **Create Recommendation**.
{% endtab %}
{% endtabs %}

### Step 2: Add recommendation details

Give your recommendation a name and optional description.

!["Recommendation details" step with the name and description fields.]({% image_buster /assets/img/item_recs_1.png %})

### Step 3: Define your recommendation {#recommendation-type}

Select a recommendation type. Each type uses the last six months of item interaction data, such as a purchase or custom event data. For more detailed information and uses cases for each, see [Types and Uses Cases]({{site.baseurl}}/user_guide/brazeai/recommendations/).

{% alert tip %}
When using **Most recent** or **AI Personalized**, users with insufficient data to create individualized recommendations will receive **Most popular** items as a fallback. The proportion of users receiving the **Most popular** fallback is displayed on the **Analytics** page.
{% endalert %}

#### Step 3.1: Exclude prior purchases or interactions (optional)

To avoid suggesting items that a user has already purchased or interacted with, select **Do not recommend items users have previously interacted with**. This option is only available when the recommendation **Type** is set to **AI Personalized**.

!["Define your recommendation" step with "AI Personalized" as the type and the "Do not recommend items users have previously interacted with" option selected.]({% image_buster /assets/img/item_recs_2-3.png %})

This setting prevents messages from reusing the items a user has already bought or interacted with, provided the recommendation has been updated recently. Items purchased or interacted with between recommendation updates may still appear. For the free version of item recommendations, updates happen weekly. For the pro version of AI item recommendations, updates happen every 24 hours.

For example, when using the pro version of AI item recommendations, if a user purchases something and then receives a marketing email within 30 minutes, the item they just purchased might not be excluded from the email in time. However, any messages sent after 24 hours won't include that item.

#### Step 3.2: Select a catalog

If not already populated, select the [catalog]({{site.baseurl}}/user_guide/data/activation/catalogs/) that this recommendation will pull items from.

#### Step 3.3: Add a selection (optional)

If you'd like more control over your recommendation, choose a [selection]({{site.baseurl}}/user_guide/data/activation/catalogs/selections/) to apply custom filters. Selections filter recommendations by specific columns in your catalog, such as brand, size, or location. Selections that contain Liquid can't be used in your recommendation.

![An example of the "in-stock" selection selected for the recommendation.]({% image_buster /assets/img/item_recs_2-2.png %})

{% alert tip %}
If you can't find your selection, make sure it's set up in your catalog first.
{% endalert %}

### Step 4: Select the interaction to drive recommendations

Select the event you want this recommendation to optimize for. This event is usually a purchase, but it can also be any interaction with an item.

You can optimize for:

- Purchase events with the [Purchase Object]({{site.baseurl}}/api/objects_filters/purchase_object/)
- Custom events that represent a purchase
- Custom events that represent any other item interaction (such as product views, clicks, or media plays)

If you choose **Custom Event**, select your event from the list.

![The "Completed Purchase" custom event selected as how events are currently tracked.]({% image_buster /assets/img/item_recs_3.png %})

### Step 5: Choose the corresponding property name {#property-name}

To create a recommendation, you need to tell Braze which field of your interaction event (purchase object or custom event) has the unique identifier that matches an item's `id` field in the catalog. Not sure? [View requirements](#requirements).

Select this field for the **Property Name**.

The **Property Name** field will pre-populate with a list of fields sent through the SDK to Braze. If enough data is provided, these properties will also be ranked in order of probability to be the correct property. Select the one that corresponds to the `id` field of the catalog.

![The property name "purchase_item" selected that corresponds to the item IDs in the catalog.]({% image_buster /assets/img/item_recs_4.png %})

#### Requirements {#requirements}

There are some requirements for selecting your property:

- Must map to the `id` field of your selected catalog.
- **If you selected Purchase Object:** Must be the `product_id` or a field of your interaction event's `properties`.
- **If you selected Custom Event:** Must be a field of your custom event's `properties`.
- Nested fields must be typed into the **Property Name** dropdown in dot notation with the format of `event_property.nested_property`. For example, if selecting the nested property `district_name` within the event property `location`, you would enter `location.district_name`.
- The field can be inside an array of products, or end with an array of IDs. In either case, each product ID will be treated as a separate, sequential event with the same timestamp.

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
  "events": [
    {
      "external_id": "user1",
      "app_id": "your-app-id",
      "name": "added_to_cart",
      "time": "2024-07-16T19:20:30+01:00",
      "properties": {
        "product_sku": "ADI-BL-7"
      }
    }
  ]
}
```

##### Example custom event object with an array of products

If your event properties contain multiple products in an array, each product ID will be treated as a separate, sequential event. This event can use the property `products.sku` to match the first and third items in the sample catalog.

```json
{
  "events": [
    {
      "external_id": "user1",
      "app_id": "your-app-id",
      "name": "added_to_cart",
      "time": "2024-07-16T19:20:30+01:00",
      "properties": {
        "transaction_id": "2ff3f9a9-8803-4c3a-91da-14adbf93dc99",
        "products": [
          { "sku": "ADI-BL-7" },
          { "sku": "ADI-WH-9" }
        ]
      }
    }
  ]
}
```

##### Example custom event object with a nested object containing a product ID array

If your product IDs are values in an array instead of objects, you can use the same notation and each product ID will be treated as a separate, sequential event. This can flexibly be combined with nested objects in the following event by configuring the property as `purchase.product_skus` to match the first and third items in the sample catalog.

```json
{
  "events": [
    {
      "external_id": "user1",
      "app_id": "your-app-id",
      "name": "added_to_cart",
      "time": "2024-07-16T19:20:30+01:00",
      "properties": {
        "transaction_id": "13791e08-7c22-4f6c-8cc6-832c76af3743",
        "purchase": {
          "product_skus": ["ADI-BL-7", "ADI-WH-9"]
        }
      }
    }
  ]
}
```

{% endtab %}
{% tab Purchase object %}

A purchase object is passed through the API when a purchase has been made.

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

### Step 6: Train the recommendation

When you're ready, select **Create Recommendation**. This process can take anywhere from 10 minutes to 36 hours to complete. You will receive an email update when the recommendation is successfully trained or an explanation of why the creation may have failed.

You can find the recommendation on the **Predictions** page, where you can then edit or archive it as needed. Recommendations will automatically retrain once every week (paid) or month (free).

## Plan-specific features

The following table describes the differences between the free and pro version of the AI Personalized, Popular, and Trending recommendation types:

| Area                   | Free version                          | Pro version            |
| :---------------------- | ------------------------------------- | :--------------------------------------- |
| User update frequency<sup>1</sup>   | Weekly                                | Daily                                    |
| Model retraining frequency  | Monthly                               | Weekly                                   |
| Maximum recommendation models | 1 model per type<sup>2</sup> | 100 models per type<sup>2</sup> |

<sup>1. This is the frequency at which user-specific item recommendations are updated (all models except Most Popular items, which updates when the model retrains). For example, if a user purchases an item recommended based on AI item recommendations, their recommended items will be updated according to this frequency</sup><br>
<sup>2. Available recommendation types are AI Personalized, Most recent, Most popular, and Trending.</sup>

## Frequently asked questions (FAQ) {#faq}

### What causes "Most popular" items to be mixed into other models' recommendations?

When our recommendation engine curates a list for you, it first prioritizes personalized selections based on the specific model you’ve chosen, like "Most recent" or "AI Personalized". If this model can’t fill the complete list of 30 recommendations for whatever reason, some of your most popular items among all users are then added to make sure each user always has a full set of recommendations.

This happens under a few specific conditions:

- The model finds fewer than 30 items that match your criteria.
- Relevant items are no longer available or in stock.
- Items don’t meet the current selection criteria, perhaps due to a change in stock or user preferences.

### Do existing recommendations train weekly after upgrading to Item Recommendations Pro?

Yes, but only after their next scheduled update. Existing recommendations don’t switch to weekly training and daily prediction immediately upon upgrading to Item Recommendations Pro. However, they will adopt the new schedule automatically at their next retraining cycle. For example, if a recommendation was last trained on February 1 and is set to retrain every 30 days, it will adopt the new weekly schedule after its next update on March 2.

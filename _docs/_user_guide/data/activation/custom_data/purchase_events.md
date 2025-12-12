---
nav_title: Purchase events
article_title: Purchase Events
page_order: 8
page_type: reference
description: "This reference article describes purchase events and properties, their usage, segmentation, where to view relevant analytics, and more."
search_rank: 3
---

# Purchase events

> This page covers purchase events and properties, their usage, segmentation, where to view relevant analytics, and more.

Purchase events are purchase actions taken by your users, and are used to record in-app purchases and establish the Lifetime Value (LTV) for each user profile. These events must be set up by your team. Logging purchase events allows you to add properties like quantity and type, helping you further target your users based on these properties.

## Logging purchase events

You can log purchases by passing a [purchase object]({{site.baseurl}}/api/objects_filters/purchase_object/) through the [`/users/track` endpoint]({{site.baseurl}}/api/endpoints/user_data/post_user_track/), or using one of our SDK libraries listed below.

The following lists methods across various platforms that are used to log purchases. Within these pages, you'll also find documentation on how to add properties and quantities to your purchase event. You can further target your users based on these properties.

- [Android and FireOS]({{site.baseurl}}/developer_guide/analytics/logging_purchases/?tab=android)
- [iOS]({{site.baseurl}}/developer_guide/analytics/logging_purchases/?tab=swift)
- [Web]({{site.baseurl}}/developer_guide/analytics/logging_purchases/?tab=web)
- [React Native]({{site.baseurl}}/developer_guide/platform_integration_guides/react_native/analytics/#logging-purchases)
- [Unity]({{site.baseurl}}/developer_guide/analytics/logging_purchases/?tab=unity)
- [.NET MAUI (formerly Xamarin)]({{site.baseurl}}/developer_guide/platform_integration_guides/xamarin/analytics/#logging-purchases)
- [Roku]({{site.baseurl}}/developer_guide/analytics/logging_purchases/?tab=roku)

## Viewing purchase data

After you have set up and begun logging purchase events, you can view this purchase data on a user's profile in the [Overview tab]({{site.baseurl}}/user_guide/engagement_tools/segments/using_user_search/#overview-tab).

## Using purchase data

There are several ways you can use purchase data in Braze:

- **[Segmentation](#purchase-event-segmentation):** Use purchase data to create segments of users based on their purchasing behavior.
- **[Personalization](#personalization):** Use purchase data to personalize messages to users.
- **[Trigger messages](#trigger-messages):** Set up messages to trigger based on purchase events.
- **[Analytics](#analytics):** Analyze your purchase data to gain insights into user behavior and the effectiveness of your marketing campaigns.

### Segmentation {#purchase-event-segmentation}

You can trigger any number or type of follow-up campaigns based on logged purchase events. For example, you can create a segment of users who made a purchase in the last 30 days, or a segment of users who have spent over a certain amount.

The following segmentation filters are available when targeting users:

- First Made Purchase
- First Purchase For App
- Last Purchased Product
- Money Spent
- Purchased Product
- Total Number of Purchases
- X Money Spent in Y Days
- X Product Purchased in Y Days
- X Purchase Property in Y Days
- X Purchases in Last Y Days

For details on each filter, refer to the [Segmentation filters]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/) glossary and filter by "Purchase behavior".

![Filtering for users who made exactly three purchases]({% image_buster /assets/img/purchase_filter_example.gif %}){: style="max-width:80%;"}

{% alert tip %} 
To segment on the number of times a specific purchase has occurred, record that purchase individually as an [incrementing custom attribute]({{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#custom-attribute-storage).
{% endalert %}

### Personalization

Like any other type of data you collect from your users, you can use purchase data to personalize your messaging through Liquid. For example, you can send a personalized email to a user recommending products similar to ones they just purchased.

Suppose you have a purchase event property called `last_purchased_product` that stores the name of the last product a user purchased. You can use this property to personalize an email message like this:

{% raw %}

```liquid
{% if ${last_purchased_product} == "Running Shoes" %}
  We hope you're enjoying your new running shoes! Based on your recent purchase, you might also like these running shorts and water bottles.
{% elsif ${last_purchased_product} == "Yoga Mat" %}
  We hope you're enjoying your new yoga mat! Based on your recent purchase, you might also like these yoga blocks and straps.
{% else %}
  Thank you for your recent purchase! We hope you're enjoying your new item.
{% endif %}
```

{% endraw %}

In this example, the message is personalized based on the `last_purchased_product` property. If the last product the user purchased was "Running Shoes", they receive a message recommending running shorts and water bottles. If the last product was "Yoga Mat", they receive a message recommending yoga blocks and straps. If the `last_purchased_product` is anything else, they receive a generic thank you message.

### Trigger messages

A common use case is to automatically send a message, such as an email, when a user makes a purchase. For example, you can send a thank you message or discount code for a future purchase.

To do so, create an action-based campaign or Canvas, then set the trigger action to **Make Purchase**. You can also specify additional conditions for the trigger, such as the product purchased or the purchase amount.

You can also personalize your triggered message with Liquid. In the following example, `${purchase_product_name}` is a custom attribute that you would replace with the actual attribute name that stores the name of the purchased product in your Braze setup.

{% raw %}

```liquid
Thank you for your purchase of ${purchase_product_name}! As a token of our appreciation, here's a discount code for your next purchase: SAVE10
```

{% endraw %}

### Analytics

In addition to tracking purchase metrics for segmentation, Braze also notes the number of purchases for each product and the revenue generated over time. This can be helpful to identify the most popular products or measure the impact of a promotional campaign on sales.

You can find this data on the [Revenue Report]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/exporting_revenue_data/#revenue-data) page.

### Understanding revenue calculations

<style>
    .no-split {
        word-break: keep-all;
    }
</style>

<table>
    <thead>
        <tr>
            <th>Metric</th>
            <th>Definition</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#lifetime-revenue">Lifetime Revenue</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Lifetime Revenue' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#lifetime-value-per-user">Lifetime Value Per User</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Lifetime Value Per User' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#average-daily-revenue">Average Daily Revenue</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Average Daily Revenue' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics#daily-purchases">Daily Purchases</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Daily Purchases' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#daily-revenue-per-user">Daily Revenue Per User</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Daily Revenue Per User' %}</td>
        </tr>
    </tbody>
</table>

#### Lifetime revenue calculation

Braze uses purchase events to calculate the lifetime revenue (also called lifetime value or LTV) of a user, which is a prediction of the net profit attributed to the entire future relationship with a customer. This can help you make informed decisions about customer acquisition and retention strategies.

$$\text{Average purchase value} = \frac{\text{Total spend in dollars}}{\text{Total number of purchase events}}$$  

There are two main places in Braze you can reference to understand your users' LTV:

- For overall metrics like *Lifetime revenue* and the *Lifetime value per user* for each app and site, refer to your [Revenue Report]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/exporting_revenue_data/#revenue-data).
- To understand a specific user's lifetime revenue, refer to their [user profile]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/#overview-tab).

##### Impact of refunds on lifetime revenue

When using purchase events to track purchase data, you should track refunds by logging a Braze purchase event with a negative `price` property. This approach maintains an accurate total for the lifetime revenue.

However, keep in mind the refund will count as an additional purchase event. Let's consider the following example. Sam makes their first purchase for $12 but returns part of the purchase for a refund of $5. Sam's profile would log:

- 1 purchase with a price of $12
- 1 purchase with a price of -$5
- Lifetime revenue of $7

While Sam would have two purchase events on their profile, in reality, they only made one purchase. This is important to consider if you have any segments or use cases built around the number of purchases a user has made. Constant refunds will inflate the purchase count on user's profile.

## Purchase event properties {#purchase-properties}

With purchase event properties, you can set properties on purchases that can be used to further qualify trigger conditions, increase personalization in messaging, and generate more sophisticated analytics through raw data export. Property value types (string, numeric, boolean, date) vary per platform and are often assigned as key-value pairs.

For example, if you have an eCommerce application and want to message a user after making a purchase, you could additionally improve your target audience and allow for increased campaign personalization by adding a purchase event property of `brand_name`.

**Example of triggering based on purchase event properties:**

![Action-based delivery settings to send a campaign to users who purchase headphones with a brand name equal to HeadphoneMart]({% image_buster /assets/img/purchase2.png %}){: style="max-width:80%;margin-left:15px;"}

Refer to [purchase properties object]({{site.baseurl}}/api/objects_filters/purchase_object/#purchase-properties-object) for more.

### Event property segmentation

Event property segmentation lets you target users based not only on custom events taken, but also on the properties associated with those events. This adds additional filtering options when segmenting purchase and custom events.

![]({% image_buster /assets/img/nested_object3.png %}){: style="max-width:80%;margin-left:15px;"}

These segmentation filters include:
- Has done the custom event with property Y with value V X times in the last Y days
- Has made any purchases with property Y with value V X times in the last Y days
- Adds 1-30 day segmentation on all purchases, events, and properties within purchases and events

Unlike with [Segment Extensions]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/), segments used are updated in real-time, support an unlimited amount of segments, offer a look back history of at most 30 days, and incur data points. Because of the additional data point charge, you must contact your Braze customer success manager to get event properties turned on for your custom events.

When approved, additional properties can be added in the dashboard under **Data Settings** > **Custom Events** by selecting **Manage Properties**. You can then use these event properties in the target step of the campaign or Canvas builder.

### Canvas entry properties and event properties

{% multi_lang_include canvas_entry_event_properties.md %}

### Log purchases at the order level

To log purchases at the order level instead of the product level, use the order name or order category as the `product_id`. Refer to our [purchase object specification]({{site.baseurl}}/api/objects_filters/purchase_object/#product-id-naming-conventions) to learn more. 

### Product ID naming conventions

At Braze, we offer some general naming conventions for the purchase object `product_id`. When choosing `product_id`, Braze suggests using simplistic names such as the product name or product category (instead of SKUs) with the intention of grouping all logged items by this `product_id`.

This makes products straightforward to identify for segmentation and triggering. 

## Blocklisting purchase events

You may occasionally identify purchase events that either log too many data points, are no longer useful to your marketing strategy, or were recorded in error. To stop this data from being sent to Braze, you can blocklist the custom data object while your engineering team works to remove it from the backend of your app or website.

In the Braze dashboard, you can manage blocklisting from **Data Settings** > **Products**. Check out [Managing custom data]({{site.baseurl}}/user_guide/data/custom_data/managing_custom_data/) to learn more.


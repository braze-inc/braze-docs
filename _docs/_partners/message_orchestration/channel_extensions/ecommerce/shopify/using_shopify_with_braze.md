---
nav_title: Using Shopify with Braze
article_title: "Using Shopify with Braze"
description: "This reference article outlines how to use the Shopify integration."
page_type: partner
search_tag: Partner
permalink: "/using_shopify_with_braze/"
page_order: 6
hidden: true
---

# Using Shopify with Braze

> This page shows you how you can use the Shopify integration in Braze, such as in your campaigns, Canvases, segments, and how to disable checkout notifications in Shopify.

## Prerequisites

Review [Shopify standard itegration]({{site.baseurl}}/shopify_standard_integration/) for instructions on integrating your Shopify store before proceeding with this article.

## Disable abandoned checkout notifications in Shopify 

As you implement your Shopify use cases in Braze, ensure that you disable Shopify’s Abandoned Checkout notification. This will help you avoid sending duplicate emails to your customers.

### Steps to Disable Emails in Shopify:

1. Log into your Shopify admin panel.
2. Go to **Settings** > **Notifications**.
3. Disable the relevant notifications, such as abandoned checkout emails by doing the following:
4. Select the **Edit** button for each notification and uncheck the option to send these emails.
5. Save your changes.

{% alert important %}
Disable these emails right before you enable the corresponding flows in Braze. This will help you avoid any gaps in communication and faciliate a seamless transition to sending notifications through Braze.
{% endalert %}

## Create your Canvas user journeys 

Canvas is a powerful tool designed to help marketers create personalized user journeys that engage customers at every stage of their shopping experience. With its flexible and intuitive interface, Canvas allows you to design, automate, and optimize customer interactions seamlessly. Whether you're looking to nurture leads, recover lost sales, or enhance customer loyalty, Braze Canvas provides the tools you need to create impactful marketing campaigns.

**Key features of Braze Canvas**

- **Flexibility:** Easily customize user journeys to fit your brand’s unique needs. Drag-and-drop functionality allows you to create complex workflows without any coding experience.
- **Real-time data integration:** Leverage real-time customer data to deliver personalized messages based on user behavior and preferences.
- **Multi-channel engagement:** Reach your customers through various channels, including email, SMS, and more.

#### Ecommerce Canvas Templates

Braze Canvas offers several pre-built templates tailored specifically for ecommerce marketers, making it easier to implement essential strategies. Here are some key templates you can use to enhance your customer journeys:

{% tabs %}
{% tab Abandoned browse %}
##### Abandoned browse

**Purpose:** Re-engage users who have browsed products but did not add them to their cart or place an order.

**Setup:** 

On the Canvas page, select **Use a Canvas Template** > **Braze templates** and then apply the **TEMPLATE_NAME** template. 

The following settings are pre-configured in your Canvas:
- Basics 
    - Canvas name: **CANVAS_NAME**
    - Conversion event: ecommerce.order placed
        - Conversion deadline: 3 days 
- Entry schedule 
    - Action-based when a user performs the ecommerce.product_viewed event
    - Start time is when you create the Canvas template 
- Target audience 
    - Entry audience 
        - Has used these apps **more than 0** times 
        - Email **is not blank**
    - Entry controls
        - Users are eligible to re-enter this Canvas. Only one user can enter this Canvas every day
    - Exit criteria 
        - Performs either ecommerce.cart_updated, ecommerce.checkout started, or ecommerce.order_placed
- Send settings 
    - Users who are subscribed or opted in 
- Delay step
    - 1 hour delay
- Message step 
    - Uses a Braze email template that you can modify with your team 
    - To personalize the product within your message, check out [Abandoned Cart and Abandoned Checkout product personalization](#abandoned-cart-checkout)
{% endtab %}

{% tab Abandoned cart %}
##### Abandoned cart

**Purpose:** Recover potential lost sales from customers who added products to their cart but did not continue to checkout or place an order. 

**Setup:** 

On the Canvas page, select **Use a Canvas Template** > **Braze templates** and then apply the **TEMPLATE_NAME** template. 

The following settings are pre-configured in your Canvas:
- Basics 
    - Canvas name: **CANVAS_NAME**
    - Conversion event: ecommerce.order_placed 
        - Conversion deadline: 3 days 
- Entry schedule 
    - Action-based trigger when a user performs the ecommerce.cart_updated event
    - Start time is when you create the Canvas template 
- Target Audience 
    - Entry audience 
        - Has used these apps **more than 0** times 
        - Email **is not blank**
    - Entry controls
        - Users are immediately re-eligible for Canvas entry
    - Exit criteria 
        - Performs either ecommerce.cart_updated, ecommerce.checkout started, or ecommerce.order_placed
- Send settings 
    - Users who are subscribed or opted in 
    - Delay step
        - 4 hour delay
- Message step 
    - Uses a Braze email template that you can modify with your team
    - To personalize products within your message, this use case uses a special shopping cart Liquid tag. For more information, check out [Abandoned Cart and Abandoned Checkout product personalization](#abandoned-cart-checkout)
{% endtab %}

{% tab Abandoned checkout %}
##### Abandoned checkout

**Purpose:** Target customers who started the checkout process but left before placing their order. 

**Setup:**

On the Canvas page, select **Use a Canvas Template** > **Braze templates** and then apply the **TEMPLATE_NAME** template. 

The following settings are pre-configured in your Canvas:

- Basics 
    - Canvas name: **CANVAS_NAME**
    - Conversion event: ecommerce.order_placed 
        - Conversion deadline: 3 days 
- Entry schedule 
    - Action-based trigger when a user performs the `ecommerce.checkout_started` event
    - Start time is when you create the Canvas template 
- Target audience 
    - Entry audience 
        - Has used these apps **more than 0** times 
        - Email **is not blank**
    - Entry controls
        - Users are immediately re-eligible for Canvas entry
        - Exit criteria 
            - Performs the ecommerce.order_placed events
- Send settings 
    - Users who are subscribed or opted in 
    - Delay step
        - 4 hour delay
- Message step 
    - Uses a Braze email template that you can modify with your team
    - To personalize products within your message, this use case uses a special shopping cart Liquid tag. For more information, check out [Abandoned Cart and Abandoned Checkout product personalization](#abandoned-cart-checkout)
{% endtab %}
{% tab Order confirmation %}
##### Order confirmation

**Purpose:** Confirm successful orders and enhance customer satisfaction.

**Setup:**

On the Canvas page, select **Use a Canvas Template** > **Braze templates** and then apply the **TEMPLATE_NAME** template. 

The following settings are pre-configured in your Canvas:

- Basics 
    - Canvas name: **CANVAS_NAME**
    - Conversion event: ecommerce.order_placed 
        - Conversion deadline: 3 days 
- Entry schedule 
    - Action-based trigger when a user performs the ecommerce.cart_updated event
    - Start time is when you create the Canvas template 
- Target audience 
    - Entry audience 
        - Has used these apps **more than 0** times 
        - Email **is not blank**
    - Entry controls
        - Users are immediately re-eligible for Canvas entry
        - Exit criteria 
            - Performs either ecommerce.cart_updated, ecommerce.checkout started, or ecommerce.order_placed
- Send settings 
    - Users who are subscribed or opted in 
- Message step 
    - Uses a Braze email template that you can modify with your team. 
    - To personalize products within your message, check out [Message personalization](#message-personalization)
{% endtab %}
{% tab Post-purchase retargeting %}

##### Post-purchase retargeting

**Purpose:** Engage customers after their purchase to encourage repeat business and build loyalty.

**Setup:**  

On the Canvas page, select **Use a Canvas Template** > **Braze templates** and then apply the **TEMPLATE_NAME** template. 

The following settings are pre-configured in your Canvas:
- Basics 
    - Canvas name: **CANVAS_NAME**
    - Conversion event: ecommerce.order_placed 
        - Conversion deadline: 3 days 
- Entry schedule 
    - Action-based trigger when a user performs the ecommerce.cart_updated event
    - Start time is when you create the Canvas template 
- Target audience 
    - Entry audience 
        - Has used these apps **more than 0** times 
        - Email **is not blank**
    - Entry controls
        - Users are immediately re-eligible for Canvas entry
    - Exit criteria 
        - Performs either ecommerce.cart_updated, ecommerce.checkout started, or ecommerce.order_placed
- Send settings 
    - Users who are subscribed or opted in 
    - Delay step
        - 7 days 
- Message step 
    - Uses a Braze email template that you can modify with your team. 
    - To personalize products within your message, check out  [Message personalization](#message-personalization)
{% endtab %}
{% endtabs %}

## Message Personalization 

[Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/) is a powerful templating language used by Braze that allows you to create dynamic and personalized content for your customers. By using Liquid tags, you can customize messages based on customer data, product information, and other variables, enhancing the shopping experience and driving engagement.

### Key features of Liquid

- **Dynamic content:** Insert customer-specific information such as names, order details, and preferences into your messages.
- **Conditional logic:** Use if/else statements to display different content based on specific conditions (such as customer location and purchase history).
- **Loops:** Iterate over collections of products or customer data to display lists or grids of items.

### Getting started with Liquid

To begin personalizing your messages using Liquid tags, you can refer to the following resources:

- [Shopify data]({{site.baseurl}}/shopify_features/shopify_data/) reference with pre-defined liquid tags
- [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/)

### Abandoned Cart and Abandoned Checkout product personalization {#abandoned-cart-checkout}

To dynamically add product information into your Abandoned Cart and Abandoned Checkout messages, you need to use the shopping cart Liquid tag like the one below.

{% raw %}
```json
INSERT EXAMPLE
```
{% endraw %}

{% alert tip %}
Use this shopping cart abort tag to avoid triggering a message to users without items in their cart.
{% endalert %}

## Segments

Use Braze [segments]({{site.baseurl}}/user_guide/engagement_tools/segments#about-braze-segments) to create targeted customer segments based on specific attributes and behaviors, and deliver personalized messaging and campaigns through your Shopify integration. With this powerful feature, you can effectively engage your customers by reaching the right audience with the right message at the right time.

For more information on getting started with segments, check out [About Braze segments]({{site.baseurl}}/user_guide/engagement_tools/segments#about-braze-segments).

### Shopify integration guidance  

To create a segment based on who has performed a supported event through the integration, you can use our Custom Event filters and specify the [specific event name]({{site.baseurl}}/shopify_features/?tab=shopify%20events&subtab=cart%20updated#supported-shopify-custom-attributes).

![Custom Events segment filters.][1]{: style="max-width:50%;"}

To create a segment based on attributes supported through the integration, you can use Custom Attribute filters and specify the [attribute name](). 

![Custom Attributes segment filters.][2]{: style="max-width:50%;"}

If you need to specify interactions with specific products, like who has placed an order for shoes, you can use one of the following options: 
- [Segment Extensions]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/#step-1-navigate-to-segment-extensions)
- [SQL Segment Extensions]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/#creating-sql-segment-extensions)

{% alert note %}
At this time, the Shopify integration doesn’t support populating the Braze [purchase event]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/purchase_events#purchase-events). As a result, purchase filters, Liquid tags, action-based triggered, and analytics should use the ecommerce.order_placed event. 
{% endalert %}

## Reporting 

Braze reporting features are designed to help you gain valuable insights into your customer engagement and marketing performance through your Shopify integration. You can track key metrics, analyze user behavior, and measure the effectiveness of your campaigns, all in one place.

### Shopify integration guidance  

To create a [Custom Events]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events#analytics) report based on who has performed a supported event through the integration, you can specify the specific [event name]({{site.baseurl}}).

To gain insights into the trends related to orders placed from your launched Canvases, you will need to set up a [Conversions Dashboard]({{site.baseurl}}/user_guide/data_and_analytics/analytics/conversions_dashboard#conversions-dashboard) and specify your Canvases.

For more advanced reporting use cases, you can use the Braze [Query Builder]({{site.baseurl}}/user_guide/data_and_analytics/query_builder/) to generate custom reports. 

{% alert note %}
At this time, the Shopify integration doesn’t support populating the Braze [purchase event]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/purchase_events#purchase-events). As a result, purchase filters, Liquid tags, action-based triggered, and analytics should use the ecommerce.order_placed event. 
{% endalert %}

[1]: {% image_buster /assets/img/Shopify/custom_events_segment.png %}
[2]: {% image_buster /assets/img/Shopify/custom_attributes_segment.png %}
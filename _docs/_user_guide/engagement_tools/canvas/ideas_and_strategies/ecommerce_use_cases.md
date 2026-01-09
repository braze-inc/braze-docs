---
nav_title: eCommerce use cases
article_title: eCommerce Use Cases
alias: /ecommerce_use_cases/
page_order: 4
description: "This reference article covers several pre-built Braze templates tailored specifically for eCommerce marketers, making it easier to implement essential strategies."
toc_headers: h2
---

# How to use eCommerce recommended events

> This page covers how and where you can use eCommerce recommended events across the platform, including how to use Braze eCommerce Canvas templates.

{% alert important %}
[eCommerce recommended events]({{site.baseurl}}/user_guide/data/custom_data/recommended_events/ecommerce_events/) are currently in early access. Contact your Braze customer success manager if you’re interested in participating in this early access. <br><br>If you’re using the new Shopify connector, eCommerce recommended events will automatically be available through the integration.
{% endalert %}

## Using a Canvas template

To use a Canvas template:
1. Go to **Messaging** > **Canvas**.
2. Select **Create Canvas** > **Use a Canvas Template**.
3. Browse the **Braze templates** tab for the template you want to use. You can preview a template by selecting its name.
4. Select **Apply Template** for the template you want to use.<br><br>!["Canvas templates" page opened to the "Braze templates" tab and showing a list of recently used templates and selectable Braze templates.]({% image_buster /assets/img_archive/apply_template.png %}){: style="max-width:80%;"}

## eCommerce Canvas templates

Braze offers four eCommerce Canvas templates.

{% multi_lang_include canvas/ecommerce_templates.md %}

## Message personalization

[Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/) is a powerful templating language used by Braze that allows you to create dynamic and personalized content for your customers. By using Liquid tags, you can customize messages based on customer data, product information, and other variables, enhancing the shopping experience and driving engagement.

### Key features of Liquid

- **Dynamic content:** Insert customer-specific information such as names, order details, and preferences into your messages.
- **Conditional logic:** Use if/else statements to display different content based on specific conditions (such as customer location and purchase history).
- **Loops:** Iterate over collections of products or customer data to display lists or grids of items.

### Getting started with Liquid

To begin personalizing your messages using Liquid tags, you can refer to the following resources:

- [Shopify data]({{site.baseurl}}/shopify_features/#shopify-data) reference with pre-defined liquid tags
- [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/)

## Segmentation

Use Braze segments to create targeted customer segments based on specific attributes and behaviors, and deliver personalized messaging and campaigns. With this powerful feature, you can effectively engage your customers by reaching the right audience with the right message at the right time.

For more information on getting started with segments, check out [About Braze segments]({{site.baseurl}}/user_guide/engagement_tools/segments#about-braze-segments).

### Recommended events

eCommerce events are based on [recommended events]({{site.baseurl}}/recommended_events/).
Because recommended events are more opinionated custom events, you can search for the recommended eCommerce event names by selecting any [custom event filter]({{site.baseurl}}/user_guide/data/custom_data/custom_events/#segmentation-filters).

### eCommerce filters

Segment your users with eCommerce filters, like **Ecommerce Source** and **Total Revenue**, by going to the **Ecommerce** section within the segmenter. 

For a list of eCommerce filters and their definitions, refer to [Segment filters]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/) and select the "eCommerce" search category.

![Segment filters dropdown with "Ecommerce" filters.]({% image_buster /assets/img_archive/ecommerce_filters.png %}){: style="max-width:50%"}

{% multi_lang_include alerts/important_alerts.md alert='Purchase event deprecation for eCommerce filters' %}

## Nested event properties

To segment by nested event properties, you can leverage [Segment Extensions]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/#why-use-segment-extensions). For example, you can use Segment Extensions to find who has bought the product “SKU-123” in the last 90 days.

## Analytics

### Custom events report

You can track eCommerce recommended event volume in the [Custom Events report]({{site.baseurl}}/user_guide/data/activation/custom_data/custom_events/#analytics). Filter by **Perform Custom Event**, then specify the [eCommerce recommended event name]({{site.baseurl}}/user_guide/data/activation/custom_data/recommended_events/ecommerce_events/#types-of-ecommerce-recommended-events) to view its performance over time.

![Custom Events chart displaying results for six selected events.]({% image_buster /assets/img/ecommerce/custom_events_chart.png %})

### Conversions report 

### Custom Events report

To create a [Custom Events report]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events#analytics) based on who has performed an event supported through the integration, you can specify the specific [event name]({{site.baseurl}}/shopify_data_features/).

### Dashboards

#### Conversions dashboard

To gain insights into the trends related to orders placed from your launched Canvases, set up a [Conversions dashboard]({{site.baseurl}}/user_guide/data_and_analytics/analytics/conversions_dashboard#conversions-dashboard) and specify your Canvases.

#### eCommerce revenue dashboard

To gain insights into revenue attributed to the last campaign or Canvas a user interacted with before placing an order, use the [eCommerce revenue dashboard]({{site.baseurl}}/ecommerce_revenue_dashboard/) and select a conversion window.

### Query Builder

### Revenue report 

To analyze data from these new events, go to the [Dashboard Builder]({{site.baseurl}}/user_guide/analytics/reporting/dashboard_builder/) and view the [**eCommerce Revenue - Last Touch Attribution** dashboard]({{site.baseurl}}/ecommerce_revenue_dashboard/).

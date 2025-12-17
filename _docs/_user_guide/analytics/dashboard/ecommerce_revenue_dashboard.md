---
nav_title: eCommerce revenue dashboard
article_title: eCommerce revenue dashboard
alias: "/ecommerce_revenue_dashboard/"
page_order: 6
description: "This article provides an overview of the eCommerce Revenue - Last Touch Attribution dashboard."
---

# eCommerce revenue dashboard

> The **eCommerce Revenue - Last Touch Attribution** dashboard tracks last-touch attributed revenue for campaigns and Canvases using [eCommerce recommended events]({{site.baseurl}}/ecommerce_events/). Use this dashboard to understand which messages drive revenue and to monitor overall eCommerce performance over time.

{% alert note %}
eCommerce recommended events are currently in early access. Contact your Braze customer success manager if you’re interested in participating in this early access. <br><br>If you're using the new [Shopify connector]({{site.baseurl}}/partners/ecommerce/shopify/multiple_stores/?tab=shopify%20connector), these recommended events will be automatically available through the integration. Otherwise, these events must be implemented before data appears in this dashboard.
{% endalert %}

To view your eCommerce revenue dashboard, go to **Analytics** > **Dashboard Builder**, then select **eCommerce Revenue - Last Touch Attribution**. This dashboard reports on revenue attributed to the last campaign or Canvas a user interacted with before placing an order, within the selected conversion window.

## Available metrics

| Metric | Definition |
| --- | --- |
| eCommerce Revenue | Total last-touch attributed revenue based on the selected date range and conversion window. |
| Daily Orders Placed | The average number of distinct orders placed per day. |
| Average Daily eCommerce Revenue | Average attributed revenue per day for the selected time period. |
| eCommerce Revenue Over Time | A time series of attributed revenue in the selected date range. |
| eCommerce Revenue by Campaign | Attributed revenue broken down by campaign. | 
| eCommerce Revenue by Canvas | Attributed revenue broken down by Canvas. |
{: .reset-td-br-1 .reset-td-br-2 role=“presentation”}

## Attribution model

The **eCommerce Revenue - Last Touch Attribution** dashboard uses last-touch attribution. This means revenue is attributed to the most recent Braze campaign or Canvas a user engaged with prior to placing an order.

{% alert important %}
Message interactions must have occurred within the selected conversion window. Orders without an eligible message interaction within the conversion window are not attributed.
{% endalert %}

## Included data

The **eCommerce Revenue - Last Touch Attribution** dashboard pulls in data from eCommerce recommended events:

- `ecommerce.product_viewed`
- `ecommerce.cart_updated`
- `ecommerce.checkout_started`
- `ecommerce.order_placed`
- `ecommerce.order_refunded`
- `ecommerce.order_cancelled`

Revenue and order counts use Braze standardized calculations.

| Metric | Calculation |
| --- | --- |
| Total Revenue | Sum of order placed values − Sum of refunded values |
| Total Orders | Distinct orders placed − Distinct orders cancelled |
{: .reset-td-br-1 .reset-td-br-2 role=“presentation”}

### Excluded data

Purchases logged using the legacy purchase event are not included.
The **eCommerce Revenue - Last Touch Attribution** dashboard currently does not support features tied to legacy purchase events, such as LTV or revenue reporting within campaigns or Canvases. 

## Currency handling

All revenue is displayed in USD. Non-USD currencies are converted to USD using the exchange rate on the date the event is reported. To prevent conversion, hardcode the currency to `USD` when sending events.

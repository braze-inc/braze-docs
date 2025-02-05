---
nav_title: Constructor
article_title: Constructor
description: "This reference article outlines the partnership between Braze and Constructor. This partnership allows you to leverage Constructor's Offsite Product Discovery to dynamically generate and deliver personalized product recommendations in Braze messages."
alias: /partners/constructor/
page_type: partner
search_tag: Partner
---

# Constructor

> [Constructor](https://constructor.com/) is a search and product discovery platform that uses AI and machine learning to deliver personalized search, recommendations, and browsing experiences for eCommerce and retail websites.

With the Braze and Constructor integration, you can use Constructor’s Offsite Product Discovery to dynamically generate and deliver personalized product recommendations in Braze messages.

## Use cases

- **Abandoned cart and post-order follow-ups**: Generate dynamic product recommendations based on user behavior and cart contents to send personalized abandoned cart reminders or post-order suggestions.
- **Similar product recommendations for abandoned cart items**: Suggest similar products to items left in a user’s cart to keep them engaged and offer alternatives.
- **Recently viewed item reminders**: Notify users about items they recently viewed but haven’t purchased yet, encouraging them to complete their purchase.
- **Promotion campaigns**: Deliver personalized promotional messages with curated product recommendations tailored to user preferences for seasonal sales or special offers.
- **Visually similar product suggestions**: Recommend visually similar items to those a user recently viewed, helping them discover related options they might prefer.

## Prerequisites

| Requirement | Description |
|-------------|-------------|
| Constructor Account | A Constructor account with its Offsite Discovery service enabled is required to take advantage of this partnership. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integration

Work with your Constructor onboarding team to complete the integration process. Make sure behavioral data from your website or other relevant data sources is available to enable personalized product recommendations. Your Constructor onboarding team will also help configure the necessary HTML snippets for use in Braze messages.

## Constructor's Offsite Discovery API URL

You can use Constructor's Offsite Discovery API URL to render product images and direct users to the appropriate product detail page. Below is a breakdown of the endpoint structure and an example of how to use it:

### Example

```html
<a href="https://offsite-discovery.cnstrc.com/v1/product/url?position=[position]&ui=[ui]&pod_id=[pod_id]&key=[key]&style_id=[style_id]&campaign_id=[campaign_id]" target="_blank">
  <img 
    src="https://offsite-discovery.cnstrc.com/v1/product/image?position=[position]&ui=[ui]&pod_id=[pod_id]&key=[key]&style_id=[style_id]&campaign_id=[campaign_id]"
    width="200" 
    border="0" 
    alt="Shop Now" 
  />
</a>
```

### Parameters

| Parameters | Description |
|-------------|-------------|
| `position` | Refers to the ranking of the specific recommended item within the suggested list (for example, `position = 2`). <br>![Position ranking of item.]({% image_buster /assets/img/constructor/constructor_position.png %}) |
| `ui` | Represents the user's identifier, crucial for personalizing recommendation results. Set the `ui` parameter as the customer’s `external_id` in Braze. If omitted, Constructor will return general recommendations instead of user-specific ones. |
| `pod_id` | Identifier for the pod containing strategy and searchandising rules for recommendations (for example, a pod with a bestseller strategy generates personalized bestseller). |
| `key` | The Constructor index key for this customer. |
| `style_id` | Determines which images are displayed for the product card. For example, different `style_ids` display unique product card images. |
| `campaign_id` | Unique ID for the email campaign. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Optional inputs

| Input | Description |
|-------------|-------------|
| `item_id` | Represents the seed item. Necessary for item-item based strategies, such as alternative, complementary, bundles. For example, the first item in an email is the seed item, with subsequent items as alternatives. |
| `num_results` | Number of products to be added to the email. The default is 10, up to 100. For example, `num_results = 3` means three recommendations are added. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }


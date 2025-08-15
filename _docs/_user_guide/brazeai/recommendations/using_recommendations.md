---
nav_title: Using recommendations
article_title: Using Item Recommendations In Your Messaging
description: "This article describes how to use item recommendations in your message."
page_order: 1.2
---

# Using item recommendations in your messaging

> After your recommendation is trained, you can use Liquid to fetch and display recommended items in your messages by working directly with the `product_recommendation` Liquid object.

{% alert tip %}
For a step-by-step walkthrough, check out our Braze Learning course: [Crafting Personalized Experiences with AI](https://learning.braze.com/ai-item-recommendations-use-case/1996254).
{% endalert %}

## Prerequisites

Before you can use recommendations in your messaging, you'll need to [create and train a recommendation engine]({{site.baseurl}}/user_guide/brazeai/recommendations/creating_recommendations/). Training can take anywhere between 10 minutes and 36 hours&#8212;you'll receive an email when it's finished or if an error has occurred.

## Using recommendations in your messaging

### Step 1: Add Liquid code

After your recommendation is finished training, you can personalize your messages with Liquid to insert the most popular products in that catalog.

{% tabs local %}
{% tab pre-formatted code %}
!["Add Personalization" modal with item recommendation as the personalization type.]({% image_buster /assets/img/add_personalization.png %}){: style="max-width:30%;float:right;margin-left:15px;"}

You can generate Liquid from the **Add personalization** section in your message composer:

1. In any message composers that support personalization, select <i class="fa-solid fa-circle-plus" style="color: #12aec5;" title="Add personalization"></i> to open the personalization window.
2. For **Personalization Type**, select **Item Recommendation**.
3. For **Item Recommendation Name**, select the recommendation you just created.
4. For **Number of Predicted Items**, enter how many top products you'd like to be inserted. For example, you can display the top three most purchased items.
5. For **Information to Display**, select which fields from the catalog should be included for each item. The values for these fields for each item will be drawn from the catalog associated with this recommendation.
6. Select the **Copy** icon and paste the Liquid wherever it needs to go in your message.
{% endtab %}

{% tab custom code %}
You can write custom Liquid code by referencing a catalog's `product_recommendation` object. It contains all the dynamically-generated product recommendation data for that catalog, structured as an array of objects, where each object represents a recommended item.

|Specification|Details|
|-------------|-------|
|**Structure**|Each item is accessed as `items[index]`, where index starts at 0 (for the first item) and increments for subsequent items.|
|**Catalog fields**|Each item in the array contains key-value pairs corresponding to fields (columns) in the catalog. For example, common catalog fields for product recommendations include:<br>- `name` or `title`<br>- `price`<br>- `image_url`|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

Use the `assign` tag to fetch the `product_recommendation` data and assign it to a variable.

{% raw %}
```liquid
{% assign items = {{product_recommendation.${recommendation_name}}} %}
```
{% endraw %}

Replace the following:

|Placeholder|Description|
|-----------|-----------|
|`recommendation_name`|The name of the AI recommendation you created in Braze.|
|`items`|The variable storing the recommended items array.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

Next, reference specific items and their fields using array indexing and dot notation:

{% raw %}
```liquid
{% assign items = {{product_recommendation.${recommendation_name}}} %}
{{ items[0].name }} for {{ items[0].price }}
```
{% endraw %}

To include multiple items, reference each item individually by its index. `.name` and `.price` pull the corresponding field from the catalog. 

{% raw %}
```liquid
{% assign items = {{product_recommendation.${recommendation_name}}} %}
{{ items[0].name }} for {{ items[0].price }}
{{ items[1].name }} for {{ items[1].price }}
{{ items[2].name }} for {{ items[2].price }}
```
{% endraw %}

AI recommendations return multiple products as an array, where `items[0]` is the first item, `items[1]` is the second, and so on. If a recommendation only returns one item, attempting to reference `items[1]` will result in an empty field.
{% endtab %}
{% endtabs %}

### Step 2: Reference an image (optional)

If the catalog your recommendation includes image links, you can reference them in your message. 

{% tabs %}
{% tab Drag-and-drop%}
In the email drag-and-drop editor, add an image block to your email, then select the image block to open **Image properties**.

![Image properties panel in the drag-and-drop editor]({% image_buster /assets/img/image_with_liquid.png %}){: style="max-width:45%"}

Toggle **Image with Liquid**, then add the following to the **Dynamic URL** field:

{% raw %}
```liquid
{% assign items = {{product_recommendation.${recommendation_name}}} %}
{{ items[0].image_url_field }}
```
{% endraw %}

Replace the following:

|Placeholder|Description|
|-----------|-----------|
|`recommendation_name`|The name of your recommendation.|
|`image_url_field`|The name of the field in your catalog that contains image URLs.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

To include a placeholder image in your preview and test emails, select **Choose image** then either choose an image from your media library or enter the URL of an image from your hosting site.
{% endtab %}

{% tab HTML %}
For HTML image references, set the image `src` attribute to the image URL field in the catalog. You might want to use another field, such as a product name or description, as the alt text.

{% raw %}
```html
{% assign items = {{product_recommendation.${recommendation_name}}} %}
<img src="{{ items[0].image_url_field }}" alt="{{ items[0].name }}">
```
{% endraw %}

Replace the following:

|Placeholder|Description|
|-----------|-----------|
|`recommendation_name`|The name of your recommendation.|
|`image_url_field`|The name of the field in your catalog that contains image URLs.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}
{% endtab %}
{% endtabs %}

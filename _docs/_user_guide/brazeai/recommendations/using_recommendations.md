---
nav_title: Using Item Recommendations
article_title: Using Item Recommendations In Your Messaging
description: "This article describes how to use item recommendations in your message."
page_order: 20
---

# Using item recommendations in your messaging

> After your recommendation is trained, you can use Liquid to fetch and display recommended items in your messages. The key here is working directly with the `product_recommendation` Liquid object. This article covers the `product_recommendation` Liquid object and includes a tutorial to help you put that knowledge into practice.

{% alert tip %}
This article describes the syntax of the Liquid object in detail. However, you can [insert pre-formatted variables]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/using_liquid/#inserting-pre-formatted-variables) with defaults through the **Add Personalization** modal located on the top-right of any templated text field.
{% endalert %}

For additional guidance on using AI item recommendations in Braze, check out our Braze Learning [Course on Crafting Personalized Experiences with AI][1]. This course covers industry use cases, step-by-step instructions, and an additional use case for creating an in-app message with AI-driven recommendations.

## Anatomy of the recommendation object

The `product_recommendation` object represents the set of items recommended by the model. It provides data directly from the associated catalog, structured as an array of objects, where each object represents a recommended item.

- **Structure:** Each item is accessed as `items[index]`, where index starts at 0 (for the first item) and increments for subsequent items.
- **Catalog fields:** Each item in the array contains key-value pairs corresponding to fields (columns) in the catalog. For example, common catalog fields for product recommendations include:
   - `name` or `title`
   - `price`
   - `image_url`

## Liquid tags

The `product_recommendation` object contains dynamically generated product recommendations. To access these in Liquid, you must first assign the data to a variable before using it in your message.

### Assigning recommendation data

Always start with the assign tag to fetch the `product_recommendation` data and store it in a variable.

{% raw %}

```liquid
{% assign items = {{product_recommendation.${RECOMMENDATION_NAME}}} %}
```

{% endraw %}

- `RECOMMENDATION_NAME`: Replace this with the name of the AI recommendation you created in Braze.
- `items`: The variable storing the recommended items array.

### Accessing individual items

After the recommendation data is assigned, you can reference specific items and their fields using array indexing and dot notation:

{% raw %}

```liquid
{% assign items = {{product_recommendation.${RECOMMENDATION_NAME}}} %}
{{ items[0].name }} for {{ items[0].price }}
```

{% endraw %}

To include multiple items, reference each item individually by its index. `.name` and `.price` pull the corresponding field from the catalog. 

{% raw %}

```liquid
{% assign items = {{product_recommendation.${RECOMMENDATION_NAME}}} %}
{{ items[0].name }} for {{ items[0].price }}
{{ items[1].name }} for {{ items[1].price }}
{{ items[2].name }} for {{ items[2].price }}
```

{% endraw %}

AI recommendations return multiple products as an array, where `items[0]` is the first item, `items[1]` is the second, and so on. If a recommendation only returns one item, attempting to reference `items[1]` will result in an empty field.

## Adding images

If the catalog your recommendation uses includes image links, you can reference those images in your message. 

{% tabs %}

{% tab Drag-and-drop%}
In composers with image fields, add the following Liquid to the respective field in the composer:

{% raw %}

```liquid
{% assign items = {{product_recommendation.${RECOMMENDATION_NAME}}} %}
{{ items[0].IMAGE_URL_FIELD }}
```

{% endraw %}

For the email drag-and-drop editor:

1. Add an image block to your email.
2. Select the image block (not the **Browse** button) to open the **Image properties** panel.
3. Turn on **Image with Liquid**. 
4. Paste the Liquid snippet to the **Dynamic URL** field.

{% raw %}

```liquid
{% assign items = {{product_recommendation.${RECOMMENDATION_NAME}}} %}
{{ items[0].IMAGE_URL_FIELD }}
```

{% endraw %}

![Image properties panel in the drag-and-drop editor]({% image_buster /assets/img/image_with_liquid.png %}){: style="max-width:60%"}

{:start="5"}

5. To include a placeholder image in your preview and test emails, press **Choose image** to add a placeholder image from the media library, or enter a URL where your image is hosted.

{% endtab %}

{% tab HTML %}

For HTML image references, set the image `src` attribute to the image URL field in the catalog. You might want to use another field, such as a product name or description, as the alt text.

{% raw %}

```html
{% assign items = {{product_recommendation.${RECOMMENDATION_NAME}}} %}
<img src="{{ items[0].IMAGE_URL_FIELD }}" alt="{{ items[0].name }}">
```

{% endraw %}

{% endtab %}

{% endtabs %}

-  Replace `MY_RECOMMENDATION_NAME` with the name of your recommendation
- Replace `IMAGE_URL_FIELD` with the name of the field in your catalog that contains image URLs.


## Tutorial: Create abandoned cart email

In this tutorial, you’ll learn how to create a dynamic email that recommends products to users based on their preferences or behavior using Braze AI item recommendations. 

Let's say you're a marketer at "Flash & Thread," an online clothing retailer. You want to re-engage customers who have left items in their carts and upsell additional products. Your goal is to create an email that displays the abandoned items and personalized recommendations.

### Step 1: Prepare your catalog

Your recommendation will pull items from a catalog. Follow the steps for Creating a catalog. Make sure your catalog includes these fields:

| Field | Data type | Description |
| --- | --- | --- |
| id | String | A unique identifier for each item in your catalog |
| name | String | The product name, like, “Striped Knit Sweater.” |
| price | Number | The product price, like, "49.99". |
| image_url | String | A URL pointing to the product image. Must be HTTPS-secured. If your images are hosted in the media library, hover over an asset to copy its URL. |
| category | String | The product category, like "Sweaters" or "Accessories." |
| color | String | A descriptive color for the product, like "Navy/Grey." |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


#### Example catalog

<style type="text/css">
.tg td{word-break:normal;}
.tg th{word-break:normal;font-size: 14px; font-weight: bold; background-color: #f4f4f7; text-transform: lowercase; color: #212123; font-family: "Sailec W00 Bold",Arial,Helvetica,sans-serif;}
.tg .tg-0pky{border-color:inherit;text-align:left;vertical-align:top;word-break:normal}
</style>

<table class="tg">
  <tr>
    <th>id</th>
    <th>name</th>
    <th>price</th>
    <th>image_url</th>
    <th>category</th>
    <th>color</th>
  </tr>
  <tr>
    <td>1001</td>
    <td>Striped Knit Sweater</td>
    <td>49.99</td>
    <td>https://{{media_library}}/images/67a41294f5eac400685ce908/original.png?1738805908</td>
    <td>Sweaters</td>
    <td>Navy/Grey</td>
  </tr>
  <tr>
    <td>1002</td>
    <td>Custom Yacht Club Shoes</td>
    <td>79.99</td>
    <td>https://{{media_library}}/images/67a4136fe5a7660068bbe046/original.png?1738806127</td>
    <td>Footwear</td>
    <td>Navy</td>
  </tr>
  <tr>
    <td>1003</td>
    <td>Back to Work Shoes</td>
    <td>89.99</td>
    <td>https://{{media_library}}/images/67a41370f542c1006798c26e/original.png?1738806128</td>
    <td>Footwear</td>
    <td>Pink/Gold</td>
  </tr>
  <tr>
    <td>1004</td>
    <td>End of Summer Hat</td>
    <td>29.99</td>
    <td>https://{{media_library}}/images/67a4136fbf6f620068511b67/original.png?1738806127</td>
    <td>Accessories</td>
    <td>White Floral</td>
  </tr>
</table>


### Step 2: Set up your recommendation

1. From your catalog, select **Create recommendation**.
2. Follow the steps for [Creating an AI item recommendation][3]. 
3. For the recommendation type, select **AI Personalized**.
4. Use the catalog you just created to train the recommendation. This might take some time—you'll get an email when the training is complete.

### Step 3: Create an email

When the recommendation has finished training, you can use it in your messaging.

1. Create an email with the drag-and-drop editor.
2. In the message body, add an image block wherever you want to pull in a recommendation from the catalog. 
3. Select the image block and turn on **Image with Liquid** in the **Image properties** panel. 
4. Paste this Liquid snippet in the Dynamic URL field.


{% raw %}

```liquid
{% assign items = {{product_recommendation.${abandoned_cart}}} %}
{{ items[0].image_url }}
```

{% endraw %}

{: start="5"}

5. Below the image, add a paragraph block. Here's where you'll add the product name and any supporting details. 
6. Paste the following Liquid snippet in the block. This pulls the name, category, color, and price of the first recommendation from the catalog, and adds them as separate lines. 

{% raw %}

```liquid
{% assign items = {{product_recommendation.${abandoned_cart}}} %}
{{ items[0].name }}
{{ items[0].category }}
{{ items[0].color }}
${{ items[0].price }}
```

{% endraw %}

{: start="7"}

7. For both snippets, replace `abandoned_cart` with your recommendation name in Braze.
8. Double-check that item field names (`{{ items[0].field_name }}`)  match column names in your catalog.
9. Increment the array by one each time you repeat the block to pull in the next recommended item from the catalog. For example, the array starts with `{{ items[0].name }}`, so the next item would be `{{ items[1].name }}`.

### Step 4: Preview your message

To see how your message looks like for a real user:

1. Go to the **Preview & Test** tab in your editor.
2. Select **Random User** from the dropdown.
3. Select **Get Random User** to fetch a user from your audience and preview how the email will appear with their data.

The preview will fully render Liquid, including AI recommendations, as long as the selected user has the required attributes or event data tied to the recommendation.

If the recommendation doesn't appear in the preview, check the following:

- The user has interacted with relevant products or events that trained the recommendation model
- The recommendation itself has been successfully trained
- The Liquid code correctly references the correct recommendation and fields



[1]: https://learning.braze.com/ai-item-recommendations-use-case/1996254
[2]: {% image_buster /assets/img/image_with_liquid.png %}
[3]: {{site.baseurl}}/user_guide/brazeai/recommendations/ai_item_recommendations#creating-an-ai-item-recommendation
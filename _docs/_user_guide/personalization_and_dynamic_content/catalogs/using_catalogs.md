---
nav_title: Using catalogs
article_title: Using Catalogs
page_order: 1.5
description: "This reference article covers how to use catalogs to reference non-user data in your Braze campaigns through Liquid."
---

# Using catalogs in a message

> After creating a catalog, you can reference non-user data in your Braze campaigns through [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid). You can use catalogs in all of your messaging channels, including anywhere in the drag-and-drop editor where Liquid is supported.

## Step 1: Add personalization type {#step-one-personalization}

In the message composer of your choice, select the <i class="fas fa-plus-circle"></i> plus icon to open the **Add Personalization** modal and select **Catalogs Items** for the **Personalization Type**. Then, select your **Catalog Name**. Using our previous example, we'll select the "Games" catalog.

![]({% image_buster /assets/img_archive/use_catalog_personalization.png %})

We can immediately see the following Liquid preview:

{% raw %}
```liquid
{% catalog_items Games %}
```
{% endraw %}

## Step 2: Select catalog items

Next, it's time to add your catalog items! Using the dropdown, select the catalog items and the information to display. This information corresponds to the columns in your uploaded CSV file used to generate your catalog.

For example, to reference the title and price of our Tales game, we could select the `id` for Tales (1234) as the catalog item and request `title` and `price` for the displayed information.

{% raw %}
```liquid
{% catalog_items Games 1234 %}
 
Get {{ items[0].title }} for just {{ items[0].price }}!
```
{% endraw %}

This renders as the following:

> Get Tales for just 7.49!

## Exporting catalogs

There are two ways you can export catalogs from the dashboard: 

- Hover over the catalog row in the **Catalogs** section. Then, select the **Export catalog** button.
- Select your catalog. Then, select the **Export catalog** button in the **Preview** tab of the catalog.

You'll receive an email to download the CSV file after initiating the export. You'll have up to four hours to retrieve this file.

## Additional use cases

### Multiple items

You aren't limited to just one item in a single message. You can use the **Add Personalization** modal to add up to three catalog items at a time. To add more items to your message, select **Add Personalization** in the message composer and select the additional catalog items and information to display.

Check out this example where we add the `id` of three games, Tales, Teslagrad, and Acaratus, for **Catalog Items** and select `title` for **Information to Display**.

![]({% image_buster /assets/img_archive/catalog_multiple_items.png %}){: style="max-width:70%" }

We can further personalize our message by adding some text around our Liquid:

{% raw %}
```liquid
Get the ultimate trio {% catalog_items games 1234 1235 1236 %}
{{ items[0].title }}, {{ items[1].title }}, and {{ items[2].title }} today!
```
{% endraw %}

This returns as the following:

```Get the ultimate trio Tales, Teslagrad, and Acaratus today!```

{% alert tip %}
Check out [selections]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/selections/) to create groups of data for more personalized messaging!
{% endalert %}

### Using Liquid `if` statements

You can use catalog items to create conditional statements. For example, you can trigger a certain message to display when a specific item is selected in your campaign.

To do this, you'll use a Liquid `if` statement, such as in this example:

{% raw %}
```liquid
{% catalog_selection_items item-list selections %} 
{% if items[0].venue_name.size > 10 %}
Message if the venue name's size is more than 10 characters. 
{% elsif items[0].venue_name.size < 10 %}
Message if the venue name's size is less than 10 characters. 
{% else %} 
{% abort_message(no venue_name) %} 
{% endif %}
```
{% endraw %}

In this example, different messages will display if the custom attribute `venue_name` has more than 10 characters or less than 10 characters. If `venue_name` is `blank`, nothing will display. 

Note that you must declare the catalog list and, if applicable, the selection before using `if` statements. In the example, `item-list` is the catalog list, and `selections` is the selection name.

### Using images {#using-images}

You can also reference images in the catalog to use in your messaging. To do so, use the `catalogs` tag and `item` object in the Liquid field for images.

For example, to add the `image_link` from our Games catalog to our promotional message for Tales, select the `id` for the **Catalog Items** field and `image_link` for the **Information to Display** field. This adds the following Liquid tags to our image field:

{% raw %}
```liquid
{% catalog_items Games 1234 %}

{{ items[0].image_link }}
```
{% endraw %}

![Content Card composer with catalog Liquid tag used in the image field.]({% image_buster /assets/img_archive/catalog_image_link1.png %})

Here's what this looks like when the Liquid is rendered:

![Example Content Card with catalog Liquid tags rendered.]({% image_buster /assets/img_archive/catalog_image_link2.png %}){: style="max-width:50%" }

### Templating catalog items

You can also use templating to dynamically pull catalog items based on custom attributes. For example, let's say a user has the custom attribute `wishlist`, which contains an array of game IDs from your catalog.

```json
{
    "attributes": [
        {
            "external_id": "user_id",
            "wishlist": ["1234", "1235"]
        }
    ]
}
```

{% alert note %}
JSON objects in catalogs are only ingested through the API. You can't upload a JSON object using a CSV file.
{% endalert %}

Using Liquid templating, you can dynamically pull out the wishlist IDs and then use them in your message. To do so, [assign a variable]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/using_liquid/#assigning-variables) to your custom attribute, then use the **Add Personalization** modal to pull a specific item from the array. Variables referenced as the catalog item ID must be wrapped in curly brackets to be referenced properly, such as `{{result}}`.

{% alert tip %}
Remember, arrays start at `0`, not `1`.
{% endalert %}

For example, to let a user know that Tales (an item in our catalog that they've wished for) is on sale, we can add the following to our message composer:

{% raw %}
```liquid
{% assign wishlist = {{custom_attribute.${wishlist}}}%}
{% catalog_items Games {{ wishlist[0] }} %}

Get {{ items[0].title }} now, for just {{ items[0].price }}!
```
{% endraw %}

Which will display as the following:
> Get Tales now, for just 7.49!

With templating, you can render a different catalog item for each user based on their individual custom attributes, event properties, or any other templatable field.

### Uploading a CSV

You can upload a CSV of new catalog items to add or catalog items to update. To delete a list of items, you can upload a CSV of item IDs to delete them.

### Using Liquid

You can also manually piece together catalogs with Liquid logic. However, note that if you type in an ID that doesn't exist, Braze will still return an items array without objects. We recommend that you include error handling, such as checking the size of the array and using an `if` statement to account for an empty array case.

{% alert note %}
Liquid currently can't be used inside catalogs. If Liquid personalization is listed inside a cell in your catalog, the dynamic value won't render and only the actual Liquid will display.
{% endalert %}

#### Templating catalog items including Liquid

Similar to [Connected Content]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content), you must use the `:rerender` flag in a Liquid tag to render a catalog item's Liquid content. Note that the `:rerender` flag is only one level deep, meaning it won't apply to any nested Liquid tag calls.

If a catalog item contains user profile fields (within a Liquid personalization tag), these values must be defined in Liquid earlier in the message and before the templating in order to render the Liquid properly. If the `:rerender` flag isn't provided, it will render the raw Liquid content.

For example, if a catalog named "Messages" has an item with this Liquid:

![]({% image_buster /assets/img_archive/catalog_liquid_templating.png %}){: style="max-width:80%;"}

To render the following Liquid content:

{% raw %}
```liquid
Hi ${first_name}

{% catalog_items Messages greet_msg :rerender %}
{{ items[0].Welcome_Message }}
```
{% endraw %}

This will display as the following:

{% raw %}
```
Hi Peter,

Welcome to our store, Peter!
```
{% endraw %}

{% alert note %}
Catalog Liquid tags can't be used recursively inside catalogs.
{% endalert %}


[1]: {% image_buster /assets/img_archive/use_catalog_personalization.png %}
[2]: {% image_buster /assets/img_archive/catalog_multiple_items.png %}

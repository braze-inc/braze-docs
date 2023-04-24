---
nav_title: Nested Custom Attributes
article_title: Nested Custom Attributes
alias: "/nested_custom_attribute_support/"
page_order: 1
page_type: reference
description: "This reference article covers using nested custom attributes as a data type for custom attributes, including limitations and usage examples."
---

# Nested custom attributes

You can use nested custom attributes to send objects as a new data type for custom attributes. This nested data allows you to create segments using information from a custom attribute object, and personalize your messages using a custom attribute object and Liquid.

Objects can contain existing [data types][1], such as:

- Numbers
- Strings
- Booleans
- Arrays
- Time
- Other objects
- [Arrays of objects]({{site.baseurl}}/array_of_objects/)

## Limitations

- Nested custom attributes are intended for custom attributes sent via the API. They are not supported for use with Braze SDKs.
- Partners do not support arrays of objects. We recommend against using this feature with app groups that have partner integrations enabled.
- Objects have a maximum size of 50KB.
- Key names and string values have a size limit of 255 characters.
- Key names cannot contain spaces.

## API request body

{% tabs %}
{% tab Create %}
The following is a `/users/track` example with a "Most Played Song" object. To capture the properties of the song, we'll send an API request that lists `most_played_song` as an object, along with a set of object properties.

```json
{
  "attributes": [
    {
      "external_id": "user_id",
      "most_played_song": {
        "song_name": "Solea",
        "artist_name": "Miles Davis",
        "album_name": "Sketches of Spain",
        "genre": "Jazz",
        "play_analytics": {
            "count": 1000,
            "top_10_listeners": true
        }
      }
    }
  ]
}
```

{% endtab %}
{% tab Update %}
To update an existing object, send a POST to `users/track` with the `_merge_objects` parameter in the request. This will deep merge your update with the existing object data. Deep merging ensures that all levels of an object are merged into another object instead of only the first level. In this example, we already have a `most_played_song` object in Braze, and now we're adding a new field, `year_released`, to the `most_played_song` object.

```json
{
  "attributes": [
    {
      "external_id": "user_id",
      "_merge_objects": true,
      "most_played_song": {
          "year_released": 1960
      }
    }
  ]
}
```

After this request is received, the custom attribute object will now look like the following:

```json
"most_played_song": {
  "song_name": "Solea",
  "artist_name" : "Miles Davis",
  "album_name": "Sketches of Spain",
  "year_released": 1960,
  "genre": "Jazz",
  "play_analytics": {
     "count": 1000,
     "top_10_listeners": true
  }
}
```

{% alert warning %}
You must set `_merge_objects` to true, or your objects will be overwritten. `_merge_objects` is false by default.
{% endalert %}

{% endtab %}
{% tab Delete %}
To delete a custom attribute object, send a POST to `users/track` with the custom attribute object set to `null`.

```json
{
  "attributes": [
    {
      "external_id": "user_id",
      "most_played_song": null
    }
  ]
}
```

{% endtab %}
{% endtabs %}

#### Capturing dates as object properties

To capture dates as object properties, you must use the `$time` key. In the following example, an "Important Dates" object is used to capture the set of object properties, `birthday` and `wedding_anniversary`. The value for these dates is an object with a `$time` key.

```json
{
  "attributes": [ 
    {
      "external_id": "time_with_nca_test",
      "important_dates": {
        "birthday": {"$time" : "1980-01-01T19:20:30Z"},
        "wedding_anniversary": {"$time" : "2020-05-28T19:20:30Z"}
      }
    }
  ]
}
```

Note that for nested custom attributes, if the year is less than 0 or greater than 3000, Braze does not these values on the user.

## Liquid templating

The following Liquid templating example shows how to reference the custom attribute object properties saved from the preceding API request and use them in your messaging.

Use the `custom_attribute` personalization tag and dot notation to access properties on an object. Specify the name of the object (and position in array if referencing an array of objects), followed by a dot (period), followed by the property name.

{% raw %}
`{{custom_attribute.${most_played_song}[0].artist_name}}` — "Miles Davis"
<br> `{{custom_attribute.${most_played_song}[0].song_name}}` — "Solea"
<br> `{{custom_attribute.${most_played_song}[0].play_analytics.count}}` — "1000"
{% endraw %}

![Using Liquid to template a song name and the number of times a listener has played that song into a message][5]

## Segmentation

You can build segments based on nested custom attributes to further target your users. To do so, filter your segment based on the custom attribute object, then specify the path to your property name and associated value you want to segment on. If you're not sure what that path looks like, you can [generate a schema](#generate-schema) and use the nested object explorer to have Braze populate that path for you.

After adding a path to your property, click **Validate** to verify that the value in the path field is valid.

![Filtering based on a most played song custom attribute where a listener has played a song over a specified number of times][6]

When working with nested custom attributes segmentation, you'll have access to a new comparator grouped by data type. For example, since `play_analytics.count` is a number, you can select a comparator under the **Number** category.

![A user choosing an operator based on the data type for the nested custom attribute][7]

### Multi-criteria segmentation

Use **Multi-Criteria Segmentation** to create a segment that matches multiple criteria within a single object. This qualifies the user into the segment if they have at least one object array that matches all the criteria specified. For example, users will only match this segment if their key is not blank, and if their number is more than 0.

![An example segment with the selected checkbox for Multi-Criteria Segmentation.][14]

### Generate a schema using the nested object explorer {#generate-schema}

You can generate a schema for your objects to build segment filters without needing to memorize nested object paths. To do so, perform the following steps.

#### Step 1: Generate a schema

For this example, suppose we have an `accounts` object array that we've just sent to Braze:

```json
"accounts": [
  {"type": "taxable",
  "balance": 22500,
  "active": true},
  {"type": "non-taxable",
  "balance": 0,
  "active": true},
 ]
```

In the Braze dashboard, navigate to **Manage Settings** > **Custom Attributes**. Search for your object or object array. In the **Attribute Name** column, click **Generate Schema**.

![][8]

{% alert tip %}
It may take a few minutes for your schema to generate depending on how much data you've sent us.
{% endalert %}

After the schema has been generated, a new <i class="fas fa-plus"></i> plus button appears in place of the **Generate Schema** button. You can click on it to see what Braze knows about this nested custom attribute. 

During schema generation, Braze looks at previous data sent and builds an ideal representation of your data for this attribute. Braze also analyzes and adds a data type for your nested values.

For our `accounts` object array, you can see that within the object array, there's an object that contains the following:

- A boolean type with a key of `active` (regardless of if the account is active or not)
- A number type with a key of `balance` (balance amount in the account)
- A string type with a key of `type` (non-taxable or taxable account)

![][10]{: style="max-width:50%" }

Now that we've analyzed and built a representation of the data, let's build a segment.

#### Step 2: Build a segment

Let's target customers who have a balance of less than 100 so that we can send them a message nudging them to make a deposit.

Create a segment and add the filter `Nested Custom Attribute`, then search for and select your object or object array. Here we've added the `accounts` object array. 

![][11]

Click the <i class="fas fa-plus"></i> plus button in the path field. This will bring up a representation of your object or object array. You can select any of the listed items and Braze will insert them into the path field for you. For our use case, we need to get the balance. Select the balance and the path (in this case, `[].balance`) is automatically populated in the path field.

![][12]{: style="max-width:70%" }

You can click **Validate** to verify that the contents of the path field is valid, then build the rest of the filter as needed. Here we've specified that the balance should be less than 100.

![][13]

That's it! You just created a segment using a nested custom attribute, all without needing to know how the data is structured. Braze's nested object explorer generated a visual representation of your data and allowed you to explore and select exactly what you needed to create a segment.

### Trigger nested custom attribute changes

You can trigger when a nested custom attribute object changes. This option is not available for changes to object arrays. If you don't see an option to view the path explorer, check that you've generated a schema. 

![][16]

For example, in the following action-based campaign, you can add a new trigger action for **Change Custom Attribute Value** to target users who have changed their neighborhood office preferences. 

![][15]

### Personalization

Using the **Add Personalization** modal, you can also insert nested custom attributes into your messaging. Select **Nested Custom Attributes** as the personalization type. Next, select the top-level attribute and attribute key. 

For example, in the personalization modal below, this inserts the nested custom attribute of a local neighborhood office based on a user's preferences.

![][9]{: style="max-width:70%" }

{% alert tip %}
Check that a schema has been generated if you don't see the option to insert nested custom attributes.
{% endalert %}

### Regenerate schemas {#regenerate-schema}

After a schema has been generated, it can be regenerated once every 24 hours. Locate your custom attribute and click the <i class="fas fa-plus"></i> plus button to view the current schema. Then click <i class="fas fa-arrows-rotate"></i> **Regenerate Schema**. This option will be disabled if it has been less than 24 hours since the schema was last regenerated.

## Data Points

Any key that is updated consumes a data point. For example, this object initialized in the user profile counts as seven (7) data points:

```json
{
  "attributes": [
    {
      "external_id": "user_id",
      "most_played_song": {
        "song_name": "Solea",
        "artist_name": "Miles Davis",
        "album_name": "Sketches of Spain",
        "year_released": 1960,
        "genre": "Jazz",
        "play_analytics": {
          "count": 1000,
          "top_10_listeners": true
        }
      }
    }
  ]
}
```

{% alert note %}
Updating a custom attribute object to `null` also consumes a data point.
{% endalert %}

[1]: {{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#custom-attribute-data-types
[4]: https://calendly.com/d/w9y6-qq9c/feedback-on-nested-custom-attributes?month=2021-07
[5]: {% image_buster /assets/img_archive/nca_liquid_2.png %} 
[6]: {% image_buster /assets/img_archive/nca_segmentation_2.png %}
[7]: {% image_buster /assets/img_archive/nca_comparator.png %}
[8]: {% image_buster /assets/img_archive/nca_generate_schema.png %}
[9]:{% image_buster /assets/img_archive/nca_personalization.png %}
[10]: {% image_buster /assets/img_archive/nca_schema.png %}
[11]: {% image_buster /assets/img_archive/nca_segment_schema.png %}
[12]: {% image_buster /assets/img_archive/nca_segment_schema2.png %}
[13]: {% image_buster /assets/img_archive/nca_segment_schema_3.png %}
[14]: {% image_buster /assets/img_archive/nca_multi_criteria.png %}
[15]: {% image_buster /assets/img_archive/nca_triggered_changes.png %}
[16]: {% image_buster /assets/img_archive/nca_triggered_changes2.png %}

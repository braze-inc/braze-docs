---
nav_title: Nested Custom Attribute Support
permalink: "/nested_custom_attribute_support/"
hidden: true
---
<br>
{% alert note %}
Nested custom attribute support is currently in beta. Please contact your Braze account manager if you are interested in participating in the beta.
{% endalert %}

# Nested Custom Attribute Support

Nested custom attribute support allows you to send objects as a new data type for custom attributes. This nested data allows you to create segments using information from a custom attribute object, and personalize your messages using a custom attribute object and Liquid.

Objects can contain existing [data types][1], such as:

- Numbers
- Strings
- Booleans
- Arrays
- Other objects

## Limitations

- Available on custom attributes sent via API only, the Braze SDKs are not yet supported.
- Partners do not yet support nested custom attributes. Until this is supported, we recommend against using this feature with app groups that have partner integrations enabled.
- Arrays of objects are not currently support, but they are coming soon. Looking for this feature? [Schedule a chat][4] with the product team.
- Objects have a maximum size of 50KB.
- Key names and string values have a size limit of 255 characters.

## Usage Examples

### API Request Body

{% tabs local %}
{% tab Create %}
Shown below is a `/users/track` example with a "Last Played Song" object. To capture the properties of the song, we'll send an API request that lists "last_played_song" as an object, along with a set of object properties.

```
{
  "attributes": [
    {
      "external_id": "user_id",
      "last_played_song" : {
          "song_name":"Solea",
          "artist_name" : "Miles Davis",
          "album_name": "Sketches of Spain",
          "genre" : "Jazz"
      }
    }
  ]
}
```

{% endtab %}
{% tab Update %}
To update an existing object, send a POST to `users/track` with the `_merge_objects` parameter in the request. This will deep merge your update with the existing object data. In this example, we already have a `last_played_song` object in Braze, and now we're adding a new field, `year_released`, to the `last_played_song` object.

```

{
  "attributes": [
    {
      "external_id": "user_id",
      "_merge_objects" : true,
      "last_played_song" : {
          "year_released" : 1960
      }
    }
  ]
}
```

After the above request is received, the custom attribute object will now look like this:

```
"last_played_song" : {
    "song_name":"Solea",
    "artist_name" : "Miles Davis",
    "album_name": "Sketches of Spain",
    "genre" : "Jazz",
    "year_released" : 1960
}
```

{% alert warning %}
You must set `_merge_objects` to true, or your objects will be overwritten. `_merge_objects` is false by default.
{% endalert %}

{% endtab %}
{% tab Delete %}
To delete a custom attribute object, send a POST to `users/track` with the custom attribute object set to `null`.

```
{
  "attributes": [
    {
      "external_id": "user_id",
      "last_played_song" : null
    }
  ]
}
```

{% endtab %}
{% endtabs %}

### Liquid Templating

The Liquid templating example below shows how to reference the custom attribute object properties saved from the above API request and use them in your messaging.

Use the `custom_attribute` personalization tag and dot notation to access properties on an object. Specify the name of the object, followed by a dot (period), followed by the property name.

{% raw %}
`{{custom_attribute.${most_played_song}.artist_name}}` — "Miles Davis"
<br> `{{custom_attribute.${most_played_song}.song_name}}` — "Solea"
<br> `{{custom_attribute.${most_played_song}.play_analytics.count}}` — "50"
{% endraw %}

![Last Played Push Notification Example][5]

### Segmentation

You can build Segments based on nested custom attributes to further target your users. To do so, filter your Segment based on the custom attribute object, then specify the property name and associated value you want to segment on.

![Last Played Song Segment][6]

## Data Points

Any key that is updated consumes a data point, including the initialization of a parent custom attribute object. For example, this object initialized in the user profile counts as five (5) data points:

```
{
  "attributes": [
    {
      "external_id": "user_id",
      "last_played_song" : {
          "song_name":"Solea",
          "artist_name" : "Miles Davis",
          "album_name": "Sketches of Spain",
          "genre" : "Jazz"
      }
    }
  ]
}
```

{% alert note %}
Updating a custom attribute object to `null` also consumes a data point.
{% endalert %}


[1]: {{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#custom-attribute-data-types
[2]: {% image_buster /assets/img_archive/nca_liquid.png %}
[3]: {% image_buster /assets/img_archive/nca_segmentation.png %}
[4]: https://calendly.com/d/w9y6-qq9c/feedback-on-nested-custom-attributes?month=2021-07
[5]: {% image_buster /assets/img_archive/nca_liquid_2.png %} 
[6]: {% image_buster /assets/img_archive/nca_segmentation_2.png %}
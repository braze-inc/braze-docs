---
nav_title: Array of objects
article_title: Array of Objects
alias: "/array_of_objects/"
page_order: 0
page_type: reference
description: "This reference article covers using an array of objects as a data type for custom attributes, including limitations and usage examples." 
---

# Array of objects

> This page covers how to use an array of objects to group related attributes. For example, you may have a group of pet objects, song objects, and account objects that all belong to one user. These arrays of objects can be used to personalize your messaging with Liquid, or create audience segments if any element within an object matches the criteria.

{% multi_lang_include nested_attribute_objects/supported_data_types.md %}

## Limitations

- Arrays of objects are intended for custom attributes sent through the API. CSV uploads are not supported. This is because commas in the CSV file will be interpreted as a column separator, and commas in values will cause parsing errors. 
- Arrays of objects have no limit on the number of items but do have a maximum size of 100&nbsp;KB.
- Not all Braze Partners support arrays of objects. Refer to the [Partner documentation]({{site.baseurl}}/partners/home) to confirm if the integration supports this feature.

Updating or removing items in an array requires identifying the item by key and value, so consider including a unique identifier for each item in the array. The uniqueness is scoped only to the array and is useful if you want to update and remove specific objects from your array. This is not enforced by Braze.

{% alert tip %}
For more information on using arrays of objects for user attributes objects, refer to [User attributes object]({{site.baseurl}}/api/objects_filters/user_attributes_object).
{% endalert %}

## API example

{% tabs local %}
{% tab Create %}

The following is a `/users/track` example with a `pets` array. To capture the properties of the pets, send an API request that lists `pets` as an array of objects. Note that each object has been assigned a unique `id` that can be referenced later when making updates.

```json
{
  "attributes": [
    {
      "external_id": "user_id",
      "pets": [
        {
          "id": 1,
          "type": "dog",
          "breed": "beagle",
          "name": "Gus"
        },
        {
          "id": 2,
          "type": "cat",
          "breed": "calico",
          "name": "Gerald"
        }
      ]
    }
  ]
}
```
{% endtab %}
{% tab Add %}

Add another item to the array using the `$add` operator. The following example shows adding three more pet objects to the user's `pets` array.

```json
{
  "attributes": [
    {
      "external_id": "user_id",
      "pets": {
        "$add": [
          {
            "id": 3,
            "type": "dog",
            "breed": "corgi",
            "name": "Doug"
          },
          {
            "id": 4,
            "type": "fish",
            "breed": "salmon",
            "name": "Larry"
          },
           {
            "id": 5,
            "type": "bird",
            "breed": "parakeet",
            "name": "Mary"
          }
        ]
      }
    }
  ]
}
```
{% endtab %}
{% tab Update %}

Update values for specific objects within an array using the `_merge_objects` parameter and the `$update` operator. Similar to updates to simple [nested custom attribute]({{site.baseurl}}/nested_custom_attribute_support/#api-request-body) objects, this performs a deep merge.

Note that `$update` can't be used to remove a nested property from an object inside an array. To do this, you'll need to remove the entire item from the array and then add the object without that specific key (using a combination of `$remove` and `$add`).

The following example shows updating the `breed` property to `goldfish` for the object with an `id` of `4`. This request example also updates the object with `id` equals `5` with a new `name` of `Annette`. Since the `_merge_objects` parameter is set to `true`, all other fields for these two objects remain the same.

```json
{
  "attributes": [
    {
      "external_id": "user_id",
      "_merge_objects": true,
      "pets": {
        "$update": [
          {
            "$identifier_key": "id",
            "$identifier_value": 4,
            "$new_object": {
              "breed": "goldfish"
            }
          },
          {
            "$identifier_key": "id",
            "$identifier_value": 5,
            "$new_object": {
              "name": "Annette"
            }
          }
        ]
      }
    }
  ]
}
```

{% alert warning %}
You must set `_merge_objects` to true, or your objects will be overwritten. `_merge_objects` is false by default.
{% endalert %}

{% endtab %}
{% tab Remove %}

Remove objects from an array using the `$remove` operator in combination with a matching key (`$identifier_key`) and value (`$identifier_value`).

The following example shows removing any object in the `pets` array that has an `id` with a value of `1`, an `id` with a value of `2`, and a `type` with a value of `dog`. If there are multiple objects with the `type` value of `dog`, all matching objects will be removed.

```json
{
  "attributes": [
    {
      "external_id": "user_id",
      "pets": {
        "$remove": [
          // Remove by ID
          {
            "$identifier_key": "id",
            "$identifier_value": 1
          },
          {
            "$identifier_key": "id",
            "$identifier_value": 2
          },
          // Remove any dog
          {
            "$identifier_key": "type",
            "$identifier_value": "dog"
          }
        ]
      }
    }
  ]
}
```
{% endtab %}
{% endtabs %}

### Timestamps

When including fields like timestamps in an array of objects, use the `$time` format instead of plain strings or Unix epoch integers.

```json
{
  "attributes": [
    {
      "external_id": "user123",
      "purchases": [
        {
          "item_name": "T-shirt",
          "price": 19.99,
          "purchase_time": {
            "$time": "2020-05-28"
          }
        }
      ]
    }
  ]
}
```

{% alert tip %}
For more information, see [Nested Custom Attributes]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/nested_custom_attribute_support).
{% endalert %}

## SDK example

{% tabs local %}
{% tab Android SDK %}
{% subtabs %}
{% subtab Create %}
```kotlin
val json = JSONArray()
    .put(JSONObject()
        .put("id", 1)
        .put("type", "dog")
        .put("breed", "beagle")
        .put("name", "Gus"))
    .put(JSONObject()
        .put("id", 2)
        .put("type", "cat")
        .put("breed", "calico")
        .put("name", "Gerald")
    )

braze.getCurrentUser { user ->
    user.setCustomUserAttribute("pets", json)
}
```
{% endsubtab %}

{% subtab Add %}
```kotlin
val json = JSONObject()
    .put("\$add", JSONArray()
        .put(JSONObject()
            .put("id", 3)
            .put("type", "dog")
            .put("breed", "corgi")
            .put("name", "Doug"))
        .put(JSONObject()
            .put("id", 4)
            .put("type", "fish")
            .put("breed", "salmon")
            .put("name", "Larry"))
        .put(JSONObject()
            .put("id", 5)
            .put("type", "bird")
            .put("breed", "parakeet")
            .put("name", "Mary")
        )
    )

braze.getCurrentUser { user ->
    user.setCustomUserAttribute("pets", json, true)
}
```
{% endsubtab %}

{% subtab Update %}
```kotlin
val json = JSONObject()
    .put("\$update", JSONArray()
        .put(JSONObject()
            .put("\$identifier_key", "id")
            .put("\$identifier_value", 4)
            .put("\$new_object", JSONObject()
                .put("breed", "goldfish")
            )
        )
        .put(JSONObject()
            .put("\$identifier_key", "id")
            .put("\$identifier_value", 5)
            .put("\$new_object", JSONObject()
                .put("name", "Annette")
            )
        )
    )

braze.getCurrentUser { user ->
    user.setCustomUserAttribute("pets", json, true)
}
```
{% endsubtab %}

{% subtab Delete %}
```kotlin
val json = JSONObject()
    .put("\$remove", JSONArray()
        .put(JSONObject()
            .put("\$identifier_key", "id")
            .put("\$identifier_value", 1)
        )
        .put(JSONObject()
            .put("\$identifier_key", "id")
            .put("\$identifier_value", 2)
        )
        .put(JSONObject()
            .put("\$identifier_key", "type")
            .put("\$identifier_value", "dog")
        )
    )

braze.getCurrentUser { user ->
    user.setCustomUserAttribute("pets", json, true)
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab Swift SDK %}
{% subtabs %}
{% subtab Create %}
```swift
let json: [[String: Any?]] = [
  [
    "id": 1,
    "type": "dog",
    "breed": "beagle",
    "name": "Gus"
  ],
  [
    "id": 2,
    "type": "cat",
    "breed": "calico",
    "name": "Gerald"
  ]
]

braze.user.setCustomAttribute(key: "pets", array: json)
```
{% endsubtab %}

{% subtab Add %}
```swift
let json: [String: Any?] = [
  "$add": [
    [
      "id": 3,
      "type": "dog",
      "breed": "corgi",
      "name": "Doug"
    ],
    [
      "id": 4,
      "type": "fish",
      "breed": "salmon",
      "name": "Larry"
    ],
    [
      "id": 5,
      "type": "bird",
      "breed": "parakeet",
      "name": "Mary"
    ]
  ]
]

braze.user.setCustomAttribute(key: "pets", dictionary: json, merge: true)
```
{% endsubtab %}

{% subtab Update %}
```swift
let json: [String: Any?] = [
  "$update": [
    [
      "$identifier_key": "id",
      "$identifier_value": 4,
      "$new_object": [
        "breed": "goldfish"
      ]
    ],
    [
      "$identifier_key": "id",
      "$identifier_value": 5,
      "$new_object": [
        "name": "Annette"
      ]
    ]
  ]
]

braze.user.setCustomAttribute(key: "pets", dictionary: json, merge: true)
```
{% endsubtab %}

{% subtab Delete %}
```swift
let json: [String: Any?] = [
  "$remove": [
    [
      "$identifier_key": "id",
      "$identifier_value": 1,
    ],
    [
      "$identifier_key": "id",
      "$identifier_value": 2,
    ],
    [
      "$identifier_key": "type",
      "$identifier_value": "dog",
    ]
  ]
]

braze.user.setCustomAttribute(key: "pets", dictionary: json, merge: true)
```
{% endsubtab %}
{% endsubtabs %}

{% alert important %}
Nested custom attributes are not supported for AppboyKit.
{% endalert %}
{% endtab %}

{% tab Web SDK %}
{% subtabs local %}
{% subtab Create %}
```javascript
import * as braze from "@braze/web-sdk";
const json = [{
  "id": 1,
  "type": "dog",
  "breed": "beagle",
  "name": "Gus"
}, {
  "id": 2,
  "type": "cat",
  "breed": "calico",
  "name": "Gerald"
}];
braze.getUser().setCustomUserAttribute("pets", json);
```
{% endsubtab %}

{% subtab Add %}
```javascript
import * as braze from "@braze/web-sdk";
const json = {
  "$add": [{
    "id":  3,
    "type":  "dog",
    "breed":  "corgi",
    "name":  "Doug",
  }, {
    "id":  4,
    "type":  "fish",
    "breed":  "salmon",
    "name":  "Larry",
  }, {
    "id":  5,
    "type":  "bird",
    "breed":  "parakeet",
    "name":  "Mary",
  }]
};
braze.getUser().setCustomUserAttribute("pets", json, true);
```
{% endsubtab %}

{% subtab Update %}
```javascript
import * as braze from "@braze/web-sdk";
const json = {
  "$update": [
    {
      "$identifier_key": "id",
      "$identifier_value": 4,
      "$new_object": {
        "breed": "goldfish"
      }
    },
    {
      "$identifier_key": "id",
      "$identifier_value": 5,
      "$new_object": {
        "name": "Annette"
      }
    }
  ]
};
braze.getUser().setCustomUserAttribute("pets", json, true);
```
{% endsubtab %}

{% subtab Delete %}
```javascript
import * as braze from "@braze/web-sdk";
const json = {
  "$remove": [
    {
      "$identifier_key": "id",
      "$identifier_value": 1,
    },
    {
      "$identifier_key": "id",
      "$identifier_value": 2,
    },
    {
      "$identifier_key": "type",
      "$identifier_value": "dog",
    }
  ]
};
braze.getUser().setCustomUserAttribute("pets", json, true);
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

## Liquid templating

You can use this `pets` array to personalize a message. The following Liquid templating example shows how to reference the custom attribute object properties saved from the preceding API request and use them in your messaging.

{% raw %}
```liquid
{% assign pets = {{custom_attribute.${pets}}} %} 
 
{% for pet in pets %}
I have a {{pet.type}} named {{pet.name}}! They are a {{pet.breed}}.
{% endfor %} 
```
{% endraw %}

In this scenario, you can use Liquid to loop through the `pets` array and print out a statement for each pet. [Assign a variable]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/using_liquid/#assigning-variables) to the `pets` custom attribute and use dot notation to access properties on an object. Specify the name of the object, followed by a period `.`, followed by the property name.

## Segmentation

When segmenting users based on arrays of objects, a user will qualify for the segment if any object in the array matches the criteria. 

Create a new segment and select **Nested Custom Attribute** as your filter. Then search for and select the name of your array of objects.

![Filter by array of objects.]({% image_buster /assets/img_archive/array_of_objects_segmenting_1.gif %})

Use dot notation to specify which field in the array of objects you want to use. Start the text field with an empty set of square brackets `[]` to tell Braze that you're looking inside an array of objects. After that, add a period `.`, followed by the name of the field you want to use.

For example, if you want to filter the `pets` array of objects based on the `type` field, enter `[].type` and choose which type of pet to filter for, such as `snake`.

![Filter by pet type equals snake.]({% image_buster /assets/img_archive/array_of_objects_segmenting_3.png %})

Or you might filter for pets that have a `type` of `dog`. Here a user has at least one dog so that user qualifies into the segment of "any user who has at least one pet of type dog".

![Filter by pet type equals dog.]({% image_buster /assets/img_archive/array_of_objects_segmenting_2.png %})

### Levels of nesting

You can create a segment with up to one level of array nesting (array within another array). For example, given the following attributes, you can make a segment for `pets[].name` contains `Gus`, but you can't make a segment for `pets[].nicknames[]` contains `Gugu`.

{% raw %}
```json
{
  "attributes": [
    {
      "external_id": "user_id",
      "pets": [
        {
          "id": 1,
          "type": "dog",
          "breed": "beagle",
          "name": "Gus",
          "nicknames": [
            "Gugu",
            "Gusto"
          ]
        },
        {
          "id": 2,
          "type": "cat",
          "breed": "calico",
          "name": "Gerald",
          "nicknames": [
            "GeGe",
            "Gerry"
          ]
        }
      ]
    }
  ]
}
```
{% endraw %}

## Data points

Data points are logged differently depending on whether you create, update, or remove a property.

{% tabs local %}
{% tab Create %}

Creating a new array logs one data point for each attribute in an object. This example logs eight data points—each pet object has four attributes and there are two objects.

```json
{
  "attributes": [
    {
      "external_id": "user_id",
      "pets": [
        {
          "id": 1,
          "type": "dog",
          "breed": "beagle",
          "name": "Gus"
        },
        {
          "id": 2,
          "type": "cat",
          "breed": "calico",
          "name": "Gerald"
        }
      ]
    }
  ]
}
```
{% endtab %}
{% tab Update %}

Updating an existing array logs one data point for each property added. This example logs two data points as it only updates one property in each of the two objects.

```json
{
  "attributes": [
    {
      "external_id": "user_id",
      "_merge_objects": true,
      "pets": {
        "$update": [
          {
            "$identifier_key": "id",
            "$identifier_value": 4,
            "$new_object": {
              "breed": "goldfish"
            }
          },
          {
            "$identifier_key": "id",
            "$identifier_value": 5,
            "$new_object": {
              "name": "Annette"
            }
          }
        ]
      }
    }
  ]
}
```
{% endtab %}
{% tab Remove %}

Removing an object from an array logs one data point for each removal criteria you send. This example logs three data points, even though you may be removing multiple dogs with this statement.

```json
{
  "attributes": [
    {
      "external_id": "user_id",
      "pets": {
        "$remove": [
          // Remove by ID
          {
            "$identifier_key": "id",
            "$identifier_value": 1
          },
          {
            "$identifier_key": "id",
            "$identifier_value": 2
          },
          // Remove any dog
          {
            "$identifier_key": "type",
            "$identifier_value": "dog"
          }
        ]
      }
    }
  ]
}
```
{% endtab %}
{% endtabs %}


---
nav_title: Array of Objects
permalink: "/array_of_objects/"
hidden: true
---
<br>
{% alert note %}
Support for this feature depends on [nested custom attributes]({{site.baseurl}}/nested_custom_attribute_support/), which is currently in beta. Please contact your Braze account manager if you are interested in participating in the beta.
{% endalert %}

# Array of Objects

When dealing with numerous custom attribute objects, use an array of objects to group related attributes. These arrays of objects can be used to personalize your messaging with Liquid, or create audience segments if any element within an object matches the criteria.

## Limitations

- Available on custom attributes sent via API only, not supported with Braze SDKs or CSV upload.
- Partners do not yet support arrays of objects. Until this is supported, we recommend against using this feature with app groups that have partner integrations enabled.
- Datetimes are not supported in objects. If datetimes are included in your objects, they are stored as strings.
- Arrays of objects have no limit on the number of items, but do have a maximum size of 50KB.

Updating or removing items in an array requires identifying the item by key and value. As such, consider including a unique identifier for each item in the array. The uniqueness is scoped only to the array, and is useful if you want to update and remove specific objects from your array. This is not enforced by Braze.

## Usage Examples

### API Request Body

{% tabs %}
{% tab Create %}

Shown below is a `/users/track` example with a `pets` array. To capture the properties of the pets, send an API request that lists `pets` as an array of objects. Note that each object has been assigned a unique `id` that can be referenced when making updates later.

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

Add another item to the array using the `$add` operator. The following example shows adding three more pet objects to the user's pets array.

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
        ]
      }
    }
  ]
}
```
{% endtab %}
{% tab Update %}

Update values for specific objects within an array using the `_merge_objects` parameter. Similar to updates to simple [nested custom attribute]({{site.baseurl}}/nested_custom_attribute_support/#api-request-body) objects, this performs a deep merge.

The following example shows updating the `breed` property to `goldfish` for the object with an `id` of `4`. This also updates the object with `id` equals `5` with a new `name` of `Annette`. Since the `_merge_objects` parameter is set to `true`, all other fields for these two objects remain the same.

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

The following example shows removing any object in the pets array that have an `id` with a value of `1`, an `id` with a value of `2`, and a `type` with a value of `dog`. If there are multiple objects with the `type` value of `dog`, all matching objects will be removed.

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

### Liquid Templating

You can use this pets array to personalize a message. The Liquid templating example below shows how to reference the custom attribute object properties saved from the above API request and use them in your messaging.

{% raw %}
```liquid
{% assign pets = {{custom_attribute.${pets}}} %} 
 
{% for pet in pets %}
I have a {{pet.type}} named {{pet.name}}! They are a {{pet.breed}}.
{% endfor %} 
```
{% endraw %}

In this scenario, you can use Liquid to loop through the pets array and print out a statement for each pet. [Assign a variable]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/using_liquid/#assigning-variables) to the `pets` custom attribute and use dot notation to access properties on an object. Specify the name of the object, followed by a period `.`, followed by the property name.

### Segmentation

When segmenting users based on arrays of objects, a user will qualify for the segment if any object in the array matches the criteria. 

Create a new segment and select **Nested Custom Attribute** as your filter. Then search for and select the name of your array of objects.

![Filter by array of objects][1]

Use dot notation to specify which field in the array of objects you want to use. Start the text field with an empty set of square brackets `[]` to tell Braze that you're looking inside an array of objects. After that, add a period `.`, followed by the name of the field you want to use.

For example, if you want to filter the pets array of objects based on the `type` field, enter `[].type` and choose which type of pet to filter for, such as `snake`.

![Filter by pet type equals snake][3]

Or you might filter for pets that have a `type` of `dog`. Here a user has at least one dog, so that user qualifies into the segment of "any user who has at least one pet of type dog".

![Filter by pet type equals dog][2]

## Data Points

Data points are consumed differently depending on whether you create, update, or remove a property.

{% tabs %}
{% tab Create %}

Creating a new array consumes one data point for each attribute in an object. This example costs eight data points—each pet object has four attributes and there are two objects.

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

Updating an existing array consumes one data point for each property added. This example costs two data points as it only updates one property in each of the two objects.

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

Removing an object from an array consumes one data point for each removal criteria you send. This example costs three data points, even though you may be removing multiple dogs with this statement.

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

[1]: {% image_buster /assets/img_archive/array_of_objects_segmenting_1.gif %}
[2]: {% image_buster /assets/img_archive/array_of_objects_segmenting_2.png %}
[3]: {% image_buster /assets/img_archive/array_of_objects_segmenting_3.png %}
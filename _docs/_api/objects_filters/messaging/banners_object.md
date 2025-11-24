---
nav_title: "Banners object"
article_title: Banners Messaging Object
page_order: 10
page_type: reference
channel: banners
description: "This reference article explains the different components of the Braze Banners object."

---

# Banners object

> The `banners` object contains banner information organized by placement ID. Each placement can contain a single banner with associated properties.

## Response structure

```json
{
  "banners": {
    "placement_1": {
      "banner": {
        "id": (string) the unique identifier for this banner instance,
        "placement_id": (string) the placement identifier where this banner appears,
        "is_test_send": (boolean) whether this is a test send,
        "is_control": (boolean) whether this banner is part of a control group,
        "html": (string) the HTML content of the banner,
        "expires_at": (integer) Unix timestamp when the banner expires, or -1 for no expiration,
        "properties": (object or null) additional custom properties for the banner
      }
    }
  }
}
```

## Banner properties

The `properties` object can contain custom key-value pairs with typed values. Each property has the following structure:

```json
{
  "property_name": {
    "type": (string) the data type - one of "string", "number", "boolean", "datetime", "jsonobject", or "image",
    "value": (varies) the property value, type depends on the "type" field
  }
}
```

### Supported property types

- **string**: Text value
- **number**: Numeric value
- **boolean**: True or false value
- **datetime**: Unix timestamp
- **jsonobject**: A nested JSON object
- **image**: URL to an image resource

## Example response

```json
{
  "banners": {
    "placement_1": {
      "banner": {
        "id": "NjYwYWY0ZjdlYjYzNTEzNGEwODcxNDIyXyRfY2M9OGU0NGY3MmUtZDdiMC0xZmFkLTM1ZjYtYTg2NGRmZjJmYTZlJmRpJmRtJm12PTY2MGFmNTQ1Zjg3NmVjMDA1NWJkNzc2MCZvZCZwaT13ZnMmdz02NjBhZjU0NWY4NzZlYzAwNTViZDc3NDUmd3A9MTcxOTQ5OTQxOSZ3dj02NjBhZjU0NWY4NzZlYzAwNTViZDc3OGE",
        "placement_id": "placement_1",
        "is_test_send": false,
        "is_control": false,
        "html": "<html></html>",
        "expires_at": 1719592613,
        "properties": {
          "years_until_next_overflow_bug": {
            "type": "number",
            "value": 14
          },
          "overflow_bug_date": {
            "type": "datetime",
            "value": 2147483648
          },
          "favourite_icecream": {
            "type": "string",
            "value": "vanilla"
          },
          "does_braze_have_overflow_bug": {
            "type": "boolean",
            "value": false
          },
          "movie_reviews": {
            "type": "jsonobject",
            "value": {
              "reviews": [
                {
                  "name": "Dune 2",
                  "comment": "it was really long"
                },
                {
                  "name": "Oppenheimer",
                  "comment": "it was really really long"
                }
              ]
            }
          },
          "logo": {
            "type": "image",
            "value": "https://somefakedomain.com/withsomefakeimage.jpg"
          }
        }
      }
    },
    "placement_2": {
      "banner": {
        "id": "NjYwYWY1MjY0ZGQxYzg0NDQ3YTk3Yzk1XyRfY2M9YTBjYTFlZDMtOWYyNy0wMTdhLTExZjAtNjI5YzBhZTNlNDI5JmRpJmRtJm12PTY2MGFmNTQ1Zjg3NmVjMDA1NWJkNzc2NCZvZCZwaT13ZnMmdz02NjBhZjU0NWY4NzZlYzAwNTViZDc3NDUmd3A9MTcxOTQ5OTQxOSZ3dj02NjBhZjU0NWY4NzZlYzAwNTViZDc3OGE",
        "is_test_send": false,
        "is_control": false,
        "html": "<html></html>",
        "expires_at": -1,
        "placement_id": "placement_2",
        "properties": null
      }
    },
    "placement_3": {
      "banner": {
        "id": "NjYwYWY1MzcwNGY2M2VjNmY2MWYzYmZkXyRfY2M9ODY4MmNmNWYtYTE4ZC01ZTJiLTdhYTctYmQ0YTgxMjY5N2IzJmRpJmRtJm12PTY2MGFmNTQ1Zjg3NmVjMDA1NWJkNzc2OCZvZCZwaT13ZnMmdz02NjBhZjU0NWY4NzZlYzAwNTViZDc3NDUmd3A9MTcxOTQ5OTQxOSZ3dj02NjBhZjU0NWY4NzZlYzAwNTViZDc3OGE",
        "placement_id": "placement_3",
        "is_test_send": false,
        "is_control": true,
        "html": "",
        "expires_at": -1,
        "properties": {
          "years_until_next_overflow_bug": {
            "type": "number",
            "value": 14
          },
          "overflow_bug_date": {
            "type": "datetime",
            "value": 2147483648
          },
          "favourite_icecream": {
            "type": "string",
            "value": "vanilla"
          },
          "does_braze_have_overflow_bug": {
            "type": "boolean",
            "value": false
          },
          "movie_reviews": {
            "type": "jsonobject",
            "value": {
              "reviews": [
                {
                  "name": "Dune 2",
                  "comment": "it was really long"
                },
                {
                  "name": "Oppenheimer",
                  "comment": "it was really really long"
                }
              ]
            }
          },
          "logo": {
            "type": "image",
            "value": "https://somefakedomain.com/withsomefakeimage.jpg"
          }
        }
      }
    }
  }
}
```

{% alert note %}
When `is_control` is `true`, the banner is part of a control group and the `html` field will typically be empty.
{% endalert %}

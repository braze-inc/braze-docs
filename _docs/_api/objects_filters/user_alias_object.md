---
nav_title: "User alias object"
article_title: API User Alias Object
page_order: 11
page_type: reference
description: "This reference article explains the different components of the user alias object."

---

# User alias object

> An alias serves as an alternative unique user identifier. By using a user alias object, you can set a consistent identifier for analytics that will follow a given user both before and after they have logged in to a mobile app or website. You can also use this object to add the identifiers used by a third-party vendor to your Braze users to more easily reconcile your data externally.

The user alias object consists of two parts: an `alias_name` for the identifier itself, and an `alias_label` indicating the type of alias. Users can have multiple aliases with different labels, but only one `alias_name` per `alias_label`.

This object is used frequently in all of our endpoints, and oftentimes within other objects.

## Object body

```json
{
  "user_alias" : {
    "alias_name" : (required, string),
    "alias_label" : (required, string)
  }
}
```

### Example

```json
{
  "user_alias": {
    "alias_name": "john_doe_123",
    "alias_label": "email_id"
  },
  "external_id": "user_456"
}
```
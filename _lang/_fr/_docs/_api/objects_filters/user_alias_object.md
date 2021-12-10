---
nav_title: "User Alias Object"
article_title: API User Alias Object
page_order: 11
page_type: reference
description: "This article explains the different components of the User Alias object."
---

# User alias object specification

An alias serves as an alternative unique user identifier. Use aliases to identify users along different dimensions than your core user ID:
- Set a consistent identifier for analytics that will follow a given user both before and after they have logged in to a mobile app or website.
- Add the identifiers used by a third-party vendor to your Braze users to more easily reconcile your data externally.

The User Alias Object consists of two parts: an `alias_name` for the identifier itself, and an `alias_label` indicating the type of alias. Users can have multiple aliases with _different_ labels, but only one `alias_name` per `alias_label`.

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

---
nav_title: "WhatsApp Object"
article_title: WhatsApp Messaging Object
page_order: 15
page_type: reference
channel: WhatsApp
description: "This reference article explains the different components of Braze's WhatsApp object."

---

# WhatsApp object

> The `whats_app` object allows you to modify or create WhatsApp messages via our [messaging endpoints]({{site.baseurl}}/api/endpoints/messaging).

## WhatsApp object

```json
{
    "app_id": (required, string) see App Identifier,
    "subscription_group_id": (required, string) the id of your subscription group,
    "message_variation_id": (optional, string) used when providing a campaign_id to specify which message variation this message should be tracked under,
    "template_name": (required, string) the WhatsApp template name for the message,
    "template_language_code": (required, string) the language code of the WhatsApp template for the message,
    "header_variables": (optional, header variables object) an object to specify header variable values for specified template_name, required if the header has variables; see object specification below,
    "body_variables": (optional, body variable object) an object to specify body variable values for specified template_name, required if the body has variables; see object specification below,
    "button_variables": (optional, button variables object) an object to specify button variable values for specified template_name, required if buttons have variables; see object specification below,
    "header_image_uri" :(optional, string) URI to the header image, if the header is of type IMAGE in specified template_name
}
```

- [App identifier]({{site.baseurl}}/api/identifier_types/)

## Header variables object

The `header_variables` object lets you specify values for header variables in the WhatsApp template. Each key is the WhatsApp template variable index (zero-indexed) to replace with the specified value.

```json
{
    "$TEMPLATE_VARIABLE_INDEX_0": "$TEMPLATE_VARIABLE_VALUE_0"
}
```
Currently, only zero or one header variables can be specified.


#### Example

```json
{
    "0": "Check it out!"
}
```

## Body variables object

The `body_variables` object lets you specify values for body variables in the WhatsApp template. Each key is the WhatsApp template variable index (zero-indexed) to replace with the specified value.
```json
{
    "$TEMPLATE_VARIABLE_INDEX_0": "$TEMPLATE_VARIABLE_VALUE_0",
    "$TEMPLATE_VARIABLE_INDEX_1": "$TEMPLATE_VARIABLE_VALUE_1"
}
```

#### Example

```json
{
    "0": "Check it out!",
    "1": "It's pretty neat."
}
```

## Button variables object

The `button_variables` object lets you specify values for button variables in the WhatsApp template. Each key is the WhatsApp template variable index (zero-indexed) to replace with the specified value.

```json
{
    "$TEMPLATE_VARIABLE_INDEX_1": "$TEMPLATE_VARIABLE_VALUE_1",
}
```

Currently, only one button variable can be specified, which is the path component of a call-to-action URL. The variable index must match the CTA URL button index in the template. For example, if your CTA button is the second button in your template, use variable index "1".

#### Example

```json
{
    "1": "/marketing/promotion123"
}
```

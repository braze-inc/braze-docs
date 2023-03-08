---
nav_title: "WhatsApp Object"
article_title: WhatsApp Messaging Object
page_order: 15
page_type: reference
channel: WhatsApp
description: "This reference article explains the different components of Braze's WhatsApp object."

---
# WhatsApp object specification

The `whats_app` object allows you to modify or create WhatsApp messages via our [messaging endpoints]({{site.baseurl}}/api/endpoints/messaging).

```json
{
    "app_id": (required, string) see App Identifier,
    "subscription_group_id": (required, string) the id of your subscription group,
    "message_variation_id": (optional, string) used when providing a campaign_id to specify which message variation this message should be tracked under,
    "template_name": (required, string) the WhatsApp template name for the message,
    "template_language_code": (required, string) the language code of the WhatsApp template for the message,
    "header_variables": (optional, object) an object to specify header variable values for specified template_name, required if header has variables; see header_variables specification below,
    "body_variables": (optional, object) an object to specify body variable values for specified template_name, required if body has variables; see body_variables specification below,
    "button_variables": (optional, object) an object to specify button variable values for specified template_name, required if buttons have variables; see button_variables specification below,
    "header_image_uri" :(optional, string) URI to header image, if header is of type IMAGE in specified template_name
}
```

- [App Identifier]({{site.baseurl}}/api/api_key#the-app-identifier-api-key)
- [header_variables](#header_variables-object-specification)
- [body_variables](#body_variables-object-specification)
- [button_variables](#button_variables-object-specification)

## header_variables object specification

The `header_variables` object allows you to specify values for header variables in the specified WhatsApp template. Each key is the WhatsApp template variable index to replace with the specified value. **These are zero-indexed**.

**Currently, only zero or one header variables can be specified**

```json
{
    "$TEMPLATE_VARIABLE_INDEX_0": "$TEMPLATE_VARIABLE_VALUE_0"
}
```

### Example

```json
{
    "0": "Check it out!"
}
```

## body_variables object specification

The `body_variables` object allows you to specify values for body variables in the specified WhatsApp template. Each key is the WhatsApp template variable index to replace with the specified value. **These are zero-indexed**.

```json
{
    "$TEMPLATE_VARIABLE_INDEX_0": "$TEMPLATE_VARIABLE_VALUE_0",
    "$TEMPLATE_VARIABLE_INDEX_1": "$TEMPLATE_VARIABLE_VALUE_1"
}
```

### Example

```json
{
    "0": "Check it out!",
    "1": "It's pretty neat."
}
```

## button_variables object specification

The `button_variables` object allows you to specify values for button variables in the specified WhatsApp template. Each key is the WhatsApp template variable index to replace with the specified value. **These are zero-indexed**.

**Currently, only one button variable can be specified, which is the path component of a CTA URL. The variable index key must match the CTA URL button index in the message template**

```json
{
    "$TEMPLATE_VARIABLE_INDEX_1": "$TEMPLATE_VARIABLE_VALUE_1",
}
```

### Example

```json
{
    "1": "/marketing/promotion123"
}
```

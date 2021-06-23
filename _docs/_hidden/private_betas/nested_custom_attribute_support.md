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

Nested custom attribute support allows you to send objects as a new data type for custom attributes. Objects can contain existing data types, such as:

- Numbers
- Strings
- Booleans
- Arrays
- Other objects

This nested data allows you to create segments using information from a custom attribute object, and personalize your API-triggered messages using a custom attribute object and Liquid.

## Limitations

- Available on custom attributes sent via API only, the Braze SDKs are not yet supported.
- Partners do not yet support nested custom attributes. Until this is supported, we recommend against using this feature with app groups that have partner integrations enabled.
- Arrays do not currently support objects. 
- Objects have a maximum size of 50KB.
- Key names and string values have a size limit of 255 characters.

## Data Points

> Add information on how data points are logged. Tabs or dropdowns?

## Usage Examples

### API Request Body

> **Create:** Add a `/users/track` example.

> **Read:** Reference custom attributes page.

> **Update:** Add merge objects example

> **Delete:** set to `null`

### Liquid Templating

> Add Betterment example from Mo in Sweeney.

### Segmentation

> Add simple example with JMES path. Call out the comparator.



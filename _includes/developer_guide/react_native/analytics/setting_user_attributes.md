{% multi_lang_include developer_guide/prerequisites/react_native.md %}

## Logging custom attributes

Braze provides methods for assigning attributes to users. You'll be able to filter and segment your users according to these attributes on the dashboard.

### Default user attributes

To set user attributes automatically collected by Braze, you can use setter methods that come with the SDK.

```javascript
Braze.setFirstName("Name");
```

The following attributes are supported:

- First Name
- Last Name
- Gender
- Date of Birth
- Home City
- Country
- Phone Number
- Language
- Email

All string values such as first name, last name, country, and home city are limited to 255 characters.

### Custom user attributes

In addition to our predefined user attribute methods, Braze also provides [custom attributes]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#custom-attribute-data-types) to track data from your applications. 

```javascript
Braze.setCustomUserAttribute("attribute_key", "attribute_value", function(){
    // optional onResult callback
});
```

#### Unsetting custom attributes

```javascript
Braze.unsetCustomUserAttribute("attribute_key", function(){
    // optional onResult callback
});
```

#### Custom Attribute Arrays

```javascript

// Adds a string to a custom attribute string array, or creates that array if one doesn't exist.
Braze.addToCustomUserAttributeArray("my-attribute-array", "new or existing value", optionalCallback);

// Removes a string from a custom attribute string array.


Braze.removeFromCustomUserAttributeArray("my-attribute-array", "existing value", optionalCallback);
```

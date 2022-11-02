---
nav_title: Sheetlabs
article_title: Sheetlabs
page_order: 1

description: "This article outlines the partnership between Braze and Sheetlabs, a service that lets you personalise your marketing campaigns with data sourced from spreadsheets."
alias: /partners/sheetlabs/

page_type: partner
search_tag: Partner
hidden: true

---

# Sheetlabs

> [Sheetlabs][1] is a platform that allows you to turn spreadsheets into powerful, well-documented APIs. You can import data from Google Sheets or Excel, turn it into an API, and then use that API in other applications, such as Braze.

APIs created with Sheetlabs may be used inside your Braze marketing campaigns, through Braze's [Connected Content][2] functionality. This is commonly used to provide a bridge between a Google Spreadsheet, which is updated directly by the marketing team, and Braze's templates. This allows you to achieve more with Braze templates, such as translations, or larger sets of custom attributes.

## Prerequisites

| Requirement | Description |
| ----------- | ----------- |
| Sheetlabs account | A Sheetlabs account is required to take advantage of this partnership. You can create one for free on [https://sheetlabs.com][1] |
{: .reset-td-br-1 .reset-td-br-2}

## Use cases

Braze customers are currently using Sheetlabs to achieve the following use cases:

1. **Separating marketer access from Braze campaign acess**: Some teams wish to avoid giving all staff access to configure Braze templates and content directly. Instead, they want staff to update marketing content in a spreadsheet. Sheetlabs provides the bridge between spreadsheets and Braze, and it can be updated in realtime too.
2. **Translations**: Braze templates do not natively support translations. If you wish to support multiple languages, then you have to create multiple templates. By using Sheetlabs in conjunction with Braze, you can have a single Braze template that is translated into multiple languages.
3. **Extending custom attributes**: Braze has a limit on the number of custom attributes that can be configured. By using Sheetlabs in conjunction with Braze, you can overcome such limits.

More details around these use cases can be found on the [Sheetlabs documentation][3] site.

## Integration

### Step 1: Create a Sheetlabs account

Sheetlabs offers a generous free usage tier. You can create an account now and try this out. No credit card or sales contact is required.

### Step 2: Import your spreadsheet into Sheetlabs

You can either upload an Excel spreadsheet or you can link your Google account and import a Google Sheet. You may also opt to keep your Google Sheet in sync, which means that Sheetlabs will automatically fetch the latest data from your Google Sheet when it changes.

Make sure you include the Braze user ID in your spreadsheet, or something else that you can use as a lookup later on.

### Step 3: Create an API in Sheetlabs

Now you can create your API in Sheetlabs. Go to APIs and then Create API. Give your API a name. You will probably want to allow queries via a lookup field from your spreadsheet, such as the Braze user ID.

At this point, you should be able to access your API via a link like [https://sheetlabs.com/ACME/email1_translations?country=en][4].

### Step 4: Use the API in your Liquid template in Braze

Now that your API is accessible, you can use it via Braze's Connected Content feature. Here is an example of what a translations template might look like:

{% raw %}
```js
{% connected_content https://sheetlabs.com/ACME/email1_translations?country={{${country}}} :save translations %}

{{translations[0].greeting}} {{${first_name}}},

{{translations[0].message_body}}
```
{% endraw %}

And you're done!

## Further reading

The [Sheetlabs documentation portal][3] provides more examples and advice for integrating with Braze.


[1]: https://sheetlabs.com/
[2]: https://www.braze.com/docs/user_guide/personalization_and_dynamic_content/connected_content/about_connected_content/
[3]: https://app.sheetlabs.com/docs/producers/braze/
[4]: https://sheetlabs.com/ACME/email1_translations?country=en

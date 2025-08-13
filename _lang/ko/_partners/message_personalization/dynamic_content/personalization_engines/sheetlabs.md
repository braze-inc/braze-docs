---
nav_title: Sheetlabs
article_title: Sheetlabs
description: "This reference article outlines the partnership between Braze and Sheetlabs, a service that lets you personalize your marketing campaigns with data sourced from spreadsheets."
alias: /partners/sheetlabs/
page_type: partner
search_tag: Partner
---

# Sheetlabs

> [Sheetlabs](https://sheetlabs.com/) is a platform that allows you to turn spreadsheets into powerful, well-documented APIs. You can import data from Google Sheets or Excel, turn it into an API, and then use that API in other applications, such as Braze.
_This integration is maintained by Sheetlabs._

## About the integration

The Sheetlabs and Braze integration allows you to leverage [Connected Content]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/about_connected_content/) to include Sheetlabs APIs inside your Braze marketing campaigns. This is commonly used to provide a bridge between a Google Spreadsheet (which is updated directly by the marketing team) and Braze templates. This allows you to achieve more with Braze templates, such as translations or larger sets of custom attributes.

## Prerequisites

| Requirement | Description |
| ----------- | ----------- |
| Sheetlabs account | A [Sheetlabs account](https://sheetlabs.com/) is required to take advantage of this partnership. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Use cases

The Braze and Sheetlabs integration allows you to achieve the following use cases:

1. **Separating marketer access from Braze campaign access**: Some teams wish to avoid giving all staff access to configure Braze templates and content directly. Instead, they want staff to update marketing content in a spreadsheet. Sheetlabs provides the bridge between spreadsheets and Braze and can be updated in real-time.
2. **Translations**: Braze templates do not natively support translations. If you wish to support multiple languages, you must create multiple templates. By using Sheetlabs in conjunction with Braze, you can have a single Braze template that is translated into multiple languages.
3. **Extending custom attributes**: Braze provides a certain number of custom attributes that can be configured. By using Sheetlabs in conjunction with Braze, you can add additional custom attributes beyond this initial allotment.

Refer to [Sheetlabs](https://app.sheetlabs.com/docs/producers/braze/) for more information on these use cases.

## Integration

### Step 1: Import your spreadsheet into Sheetlabs

In Sheetlabs, upload an Excel spreadsheet, or link your Google account and import a Google Sheet. 

- To import an Excel spreadsheet, click **Data Tables** in the menu bar, and then **Import from CSV/Excel**.
- To import from Google Sheets, click **Data Tables** in the menu bar, and then **Import from Google**. You will then need to provide your Google login credentials and import the sheet.

You may also opt to keep your Google Sheet in sync, which means that Sheetlabs will automatically fetch the latest data from your Google Sheet when it changes.

Make sure you include the Braze user ID in your spreadsheet or something else that you can use as a lookup later on.

### Step 2: Create an API in Sheetlabs

Next, in Sheetlabs, go to **APIs > Create API**, and give your API a name. You will likely want to allow queries via a lookup field from your spreadsheet, such as the Braze user ID.

At this point, you should be able to access your API with a link like:<br> [`https://sheetlabs.com/ACME/email1_translations?country=en`](https://sheetlabs.com/ACME/email1_translations?country=en).

### Step 3: Use the API in Braze Connected Content

Now that your API is accessible, you can use it in your Connected Content calls. Here is an example of what a translations template might look like:

{% raw %}
```js
{% connected_content https://sheetlabs.com/ACME/email1_translations?country={{${country}}} :save translations %}

{{translations[0].greeting}} {{${first_name}}},

{{translations[0].message_body}}
```
{% endraw %}
{% alert tip %}
For more examples and advice on integrating with Sheetlabs, refer to [Sheetlabs documentation](https://app.sheetlabs.com/docs/producers/braze/).
{% endalert %}

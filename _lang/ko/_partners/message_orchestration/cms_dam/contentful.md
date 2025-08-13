---
nav_title: Contentful
article_title: Contentful
description: "This reference article outlines the partnership between Braze and Contentful, a content management system that allows you to dynamically use Connected Content to pull content from Contentful into your Braze campaigns."
alias: /partners/contentful/
page_type: partner
search_tag: Partner
---

# Contentful

>[Contentful](https://www.contentful.com/) is a headless content management system that lets you create, manage, and distribute content to any platform. Unlike a content management system (CMS), Contentful allows you to create your content model so you can decide which content you want to manage.<br><br>This page provides a step-by-step guide to configure Braze Connected Content to fetch data from Contentful's Content Delivery API. 

After you're integrated, you can use Contentful's RESTful APIs to deliver your content across multiple channels, such as websites, mobile apps (iOS, Android, and Windows), or many other platforms. You can also dynamically pull content from Contentful for use in your Braze campaigns.

## Prerequisites

Before you start, you'll need the following:

| Prerequisite          | Description                        |
|-----------------------|------------------------------------|
| A Contentful account | You need a Contentful account with access to the Content Delivery API. |
| A Braze account | You need a Braze account with access to the Connected Content feature. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integration

### Step 1: Get your Contentful API credentials

1. [Log into Contentful](https://app.contentful.com/login) with your credentials.
2. Create or retrieve API access tokens in the Contentful dashboard by going to **Settings** > **API keys**. If you don't already have an API key, create a new one:<br>2.1 Select **Add API key**.<br>2.2 Enter the required details and select the appropriate environment.<br>2.3 Select **Save** and note the **Space ID** and **Content Delivery API - access token**.
3. Identify the content model you want to access through the Contentful API.

### Step 2: Configure Braze Connected Content

1. [Log into Braze](https://dashboard.braze.com/sign_in) with your credentials.
2. In the Braze dashboard, go to **Templates** > **Content Blocks** > **Create Content Block** > **HTML Content Block**.
3. Create a Connected Content request to Contentful's [Contentful Content Delivery API URL](https://www.contentful.com/developers/docs/references/content-delivery-api/#/reference/links). An example Contentful Content Delivery API URL is ```https://cdn.contentful.com/spaces/{space_id}/environments/{environment_id}/entries```.<br><br> Retrieving different assets requires including specific variables. The example Connected Content URL request targets Contentful's [Entry](https://www.contentful.com/developers/docs/references/content-delivery-api/#/reference/entries/entry/get-a-single-entry/console) endpoint. This endpoint needs variables like `{space_id}` and `{environment_id}`, or `{entry_id}` and `{access_token}`. These can be taken from your Contentful instance. In this example Content Block, the variables must be replaced with your Contentful Space ID and Environment ID.<br><br>The example Content Delivery API URL uses only one of Contentful's available endpoints. Different use cases may be achieved by leveraging different URLs. For example, the [Image API](https://www.contentful.com/developers/docs/references/images-api/) can be used to capture images stored in Contentful. For more information, review [Content Delivery API](https://www.contentful.com/developers/docs/references/content-delivery-api/).

{% alert note %}
Different endpoints may require new variables, for instance the Images API requires an `{asset_id}`, `{unique_id},` and `{name}`. For further guidance, contact Contentful.
{% endalert %}

{% raw %}
```json
        {% assign space_id = "YOUR-CONTENTFUL-SPACE-ID"}
        {% assign environment_id = "YOUR-CONTENTFUL-ENVIRONMENT-ID"}
        {% assign entry_id = "YOUR-CONTENTFUL-ENTRY-ID"}
        {% assign access_token = "YOUR-CONTENTFUL-ACCESS-TOKEN"}
         {% connected_content https://cdn.contentful.com/spaces/{space_id}/environments/{environment_id}/entries/{entry_id}?access_token={access_token}
         :method get
         :headers {
             "Authorization": "YOUR_CONTENTFUL_ACCESS_TOKEN"
                 }
               :content_type application/json
               :save response %}
```
{% endraw %}

{: start="4"}
4\. Use "Test Endpoint" to test that Braze can successfully connect to the Contentful API and retrieve the desired data.
5\. Select **Done** to save your Content Block.
6\. Give your Content Block a descriptive name, such as "Contentful API", then select **Launch Content Block**.

### Step 3: Use Connected Content in campaigns and Canvasses

1. In Braze, create a new campaign or edit an existing one.
2. Use the Connected Content block to insert data fetched from Contentful. Use the data paths you defined during the configuration to dynamically populate campaign content.<br><br>
- **Response path:** After including the Content Block in a Braze Campaign or Canvas, the response becomes available when you insert the variable `{response}` into your message.<br><br>JSON dot notation allows you to specify what part of the response body from Contentful you want to include in your message. This will vary based on your use case. For example, you can use the title value ({% raw %}```liquid{{response.items[0].fields.title}}```{% endraw %}) from Contentful's Entry endpoint and receive a response like this:

{% raw %}
```json
   {
  "fields": {
    "title": {
      "en-US": "Hello!"
    },
    "body": {
      "en-US": "This is a sample message!"
    }
  },
  "metadata": {
    "tags": [
      {
        "sys": {
          "type": "Link",
          "linkType": "Tag",
          "id": "nyCampaign"
        }
      }
    ]
  },
  "sys": {
    "id": "5KsDBWseXY6QegucYAoacS",
    "type": "Entry",
    "version": 1,
    "space": {
      "sys": {
        "type": "Link",
        "linkType": "Space",
        "id": "yadj1kx9rmg0"
      }
    },
    "contentType": {
      "sys": {
        "type": "Link",
        "linkType": "ContentType",
        "id": "hfM9RCJIk0wIm06WkEOQY"
      }
    },
    "createdAt": "2016-12-20T10:43:35.772Z",
    "updatedAt": "2016-12-20T10:43:35.772Z",
    "revision": 1
  }
}
```
{% endraw %}

{: start="3" }
3\. Preview and test your campaign to confirm that the Connected Content data displays correctly.
4\. After you're satisfied with the setup, launch your campaign.

## Troubleshooting

### API response

Make sure that your Contentful API credentials and endpoint URL are correct. Check for any error messages in Braze that might indicate issues with the API call.

### Data mapping

Verify that the response path mappings are correctly configured and that the API response structure matches your expectations.

## Additional resources

- [Contentful Content Delivery API documentation](https://www.contentful.com/developers/docs/references/content-delivery-api/)
- [Braze Connected Content]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/)
- [Braze Content Blocks]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/content_blocks/)

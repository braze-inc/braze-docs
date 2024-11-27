---
nav_title: Contentful
article_title: Contentful
description: "How Connected Content allows dynamic content to be retrieved from Contentful to Braze."
alias: /partners/contentful/
page_type: partner
search_tag: Partner
layout: dev_guide
---

<!-- In most cases, the ARTICLE_TITLE will be your company name. If your tool requires several seperate pages on Braze Docs, you can add a relevant page descriptor to your title, such as "MyCompany Analytics." -->
# Contentful

<!-- The description starts with a '>' character and contains an introduction to your company, a link to your main site, and a consice overview of your integration. In a following paragraph, highlight the the relationship between your company and Braze and how this partnership helps your customers. 

I've added this, taken from the ISV Profile survey you filled in for us, but please feel free to replace this with whatever you think would be most appropriate for our customer facing docs.

Matt toldme on 29/10 that this was fine for the moment-->
>[Contentful](https://www.contentful.com/) is a headless content management system. Our platform lets you create, manage and distribute content to any platform. Unlike a CMS, we give you total freedom to create your own content model so you can decide which content you want to manage. We provide you RESTful APIs so you can deliver your content across multiple channels such as websites, mobile apps (iOS, Android and Windows Phone) or any other platform you can imagine (from Google Glass to infinity). 

This documentation provides a step-by-step guide to configure Braze Connected Content to fetch data from Contentful's Content Delivery API. This integration allows you to pull content dynamically from Contentful and use it in your Braze campaigns.

## Prerequisites

Before you start, you'll need the following:

| Prerequisite          | Description                                                                                                                                |
|-----------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| A Contentful account | Ensure you have a Contentful account with access to the Content Delivery API. |
| A Braze Account | Ensure you have a Braze account with access to the Connected Content feature. 
{: .reset-td-br-1 .reset-td-br-2}


{% alert note %}
If you are using the [older navigation]({{site.baseurl}}/navigation), you can create an API key at **Developer Console** > **API Settings**.
{% endalert %}


<!-- Create step-by-step instructions for integrating your tool with Braze. It's important to be concise and only outline the minimum neccesary steps. -->
## Integration

### Step 1: Obtain Contentful API Credentials

1. **Login to Contentful:**
   - Go to the [Contentful login page](https://app.contentful.com/login) and log in with your credentials.

2. **Create or Retrieve API Access Tokens:**
   - Navigate to the "API keys" section under the "Settings" in the Contentful dashboard.
   - If you do not already have an API key, create a new one:
     - Click on "Add API key."
     - Fill in the required details and select the appropriate environment.
     - Click "Save" and note down the "Space ID" and "Content Delivery API - access token."

3. **Identify the Content Model:**
   - Identify the content model you wish to access via the Contentful API.


### Step 2: Configure Braze Connected Content
<!-- I've replaced the login link you provided with this dashboard.braze link 

Also reviewing your original submission, I decided to pretty heavily re-write the below, as it looks like you may have gotten a bit mixed up between the creation of a Content Block and a Connected Content call. I inferred from later steps that you meant to talk about the creation of a content block that contained the connected content call 

Update 31/10/2024 Looking more closely at their documentation I'm afraid I don't think this documentation is clear enough - leveraging their endpoint requires a highly customized api url each time, and the one they gave as an example only contains the basics of a response - namely the space id and Environment id. I think I need to change it to a more specific endpoint so I can give what i think is a more practical example of how to handle a response, but I'll need them to review. 

They also spoke before about a likely value getting pulled in might be "entry by" but I can't see any value like that in any of the endpoints. -->
1. **Login to Braze:**
   - Go to the [Braze login page](https://dashboard.braze.com/sign_in) and log in with your credentials.

2. **Navigate to Content Blocks:**
   - In the Braze dashboard, go to **Templates ** > **Content Blocks** > **Create Content Block** > **HTML Content Block**

3. **Create a Connected Content Request to Contentful's [Contentful Content Delivery API URL](https://www.contentful.com/developers/docs/references/content-delivery-api/#/reference/links)**
     <!-- I'm concerned that this section of the article might be a bit too open ended. We should be trying to help the customer build a multi-purpose connected content call. If, on the back of the use cases you've seen, you expect customers to leverage endpoints other than the Content Delivery API, you might want to add more detail explaining the different url options and what kind of data they return here.
     
     Update 29/10. Matt and ben Golden agreed that we could change this further. We should add a note saying that users can swap out the url so users can access other Contentful endpoints. Looking at the image url, it does require more parameters than space id and environment id, so I need to tell the customer to talk to contentful for more guidance - need to give matt and ben a heads up on that. 
     
     We should also seperate a new paragraph talking about how the content block will give you a response - and how that response is handled is up to  -->
   - **Compose Connected Content Request:** 
  - The Contentful Content Delivery API URL is typically formatted as:
       ```
       https://cdn.contentful.com/spaces/{space_id}/environments/{environment_id}/entries
       ```
     - Retrieving different assets requires including specific variables, for more information, please review Contentful's documentation
     - In this example of a Connected Content request, we'll target Contentful's ["Entry"](https://www.contentful.com/developers/docs/references/content-delivery-api/#/reference/entries/entry/get-a-single-entry/console) endpoint. For this endpoint, we'll need variables like `{space_id}` and `{environment_id}`, `{entry_id}` and `{access_token}.`. These can be taken from your Contentful instance. 
     - In our Content Block, we must replace the variables with your Contentful Space ID and Environment ID.
     - The Content Delivery API URL shown above is but one of Contentful's available endpoints. Different use cases may be achieved by leveraging different URLs, for example the [Image API](https://www.contentful.com/developers/docs/references/images-api/) can be used to capture images stored in Contentful. 
     
     {% alert note %}Note: Different endpoints may require new variables, for instance the Images API requires an `{asset_id}` and `{unique_id}` and `{name}`. For further guidance, contact Contentful {% endalert %}

```
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

4. **Test the Endpoint:**
   - Use the "Test Endpoint" feature to ensure that Braze can successfully connect to the Contentful API and retrieve the desired data.

5. **Save the Content Block:**
   - Once you have tested the endpoint and confirmed that it works, click "Done." 
6. **Give your Content Block a descriptive name**
   - For example, "Contentful API". Then click "Launch Content Block"

<!-- Does this need to specify Campaigns, do you not advise customers request data in Canvasses? If not, I can update this section to focus on about using connected content Liquid tags anywhere they're needed. This could maybe include the alert above not necessarily having to hard cose the response in the content block? 

Update 29/10 There's no need for this to specify Campaign-->

### Step 3: Use Connected Content in Campaigns & Canvasses

1. **Create or Edit a Campaign:**
   - Go to "Campaigns" in the Braze dashboard and create a new campaign or edit an existing one.

2. **Incorporate Content Block:**
   - When designing your campaign content, use the Connected Content Block to insert data fetched from Contentful. Use the data paths you defined during the configuration to dynamically populate campaign content.

   <!-- I'm thinking of adding a reccomendation here for customers to consider either directly putting a fixed response in the Content Block, or to leverage the response as they need it in their messaging . Update 29/10 Update Ben shared a response body with me with a good example of how customers will probably want to use the response body-->
      **Configure Response Mapping:**
     - **Response Path:** After including the Content Block in a Braze Campaign or Canvas, the response will be available by inserting the variable `{response}` in your message. 

     JSON dot notation allows you to specify what part of the response body from Contentful you want to include in your message. This will vary based on your use case, but for example, you may wish to leverage the title value which is available from Contentful's Entry endpoint. Responses from the Entry endpoint are structured as follows

```json
   {
  "fields": {
    "title": {
      "en-US": "Hello, World!"
    },
    "body": {
      "en-US": "Bacon is healthy!"
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


In your message copy, to leverage the title field, you should print the variable like so:

**{{response.items[0].fields.title}}** 
     
3. **Preview and Test:**
   - Preview and test your campaign to ensure that the Connected Content data is being correctly displayed.

4. **Launch Campaign:**
   - Once satisfied with the setup, launch your campaign.

## Troubleshooting

- **API Response Issues:** Ensure that your Contentful API credentials and endpoint URL are correct. Check for any error messages in Braze that might indicate issues with the API call.
- **Data Mapping Problems:** Verify that the response path mappings are correctly configured and that the API response structure matches your expectations.

## Additional Resources

- [Contentful Content Delivery API Documentation](https://www.contentful.com/developers/docs/references/content-delivery-api/)
- [Braze Connected Content Documentation](https://www.braze.com/docs/developer_guide/connected_content/)
- [Braze Content Blocks](https://www.braze.com/docs/user_guide/engagement_tools/templates_and_media/content_blocks)

---

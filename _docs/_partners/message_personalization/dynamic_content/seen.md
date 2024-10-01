---
nav_title: SEEN
article_title: SEEN
description: "SEEN’s personalized videos has helped companies reach unmatched attention and engagement, throughout their customer journey."
alias: /partners/seen/
page_type: partner
search_tag: Partner
layout: dev_guide
---

<!-- In most cases, the ARTICLE_TITLE will be your company name. If your tool requires several seperate pages on Braze Docs, you can add a relevant page descriptor to your title, such as "MyCompany Analytics." -->
# SEEN

<!-- The description starts with a '>' character and contains an introduction to your company, a link to your main site, and a consice overview of your integration. In a following paragraph, highlight the the relationship between your company and Braze and how this partnership helps your customers. -->
> SEEN’s personalized videos has helped companies reach unmatched attention and engagement, throughout their customer journey. Personalize videos with SEEN in three simple steps: 1. Design a video around your data. 2. Personalize it at scale in the cloud. 3. Distribute it where it works best.


<!-- Most partner integrations will require the following prerequisites. However, you may add additional prerequisites as needed. -->
## Prerequisites

Before you start, you'll need the following:

| Prerequisite          | Description                                                                                                                                |
|-----------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| A SEEN campaign   | A SEEN campaign is required to take advantage of this partnership.                                                                     |
| Data source   | You'll need to send data to SEEN to personalise your videos. Make sure you have all relevant data available in Braze, and that you pass data with **braze_id** as the identifier.                                                                   |


<!-- An optional section you can use to outline the typical or atypical use cases for your integration. -->
## Use cases

SEEN offers automated video personalization across the entire the customer journey. Common uses include Onboarding, Loyalty, Sign-ups/Conversion & Win-back/Anti-churn.

<!-- Create step-by-step instructions for integrating your tool with Braze. It's important to be concise and only outline the minimum neccesary steps. -->
## Integration

In the following example, we will be sending users data to SEEN for video generation, and receiving a unique landing page link and a unique, personalised thumbnail back to Braze for distribution. This example uses a POST webhook to send data to SEEN, and data transformation to receive the data back to Braze.

### Step 1: CREATE A WEBHOOK CAMPAIGN TO SEND DATA TO SEEN

Create a new [Webhook Campaign](https://www.braze.com/docs/user_guide/message_building_by_channel/webhooks) in Braze.

Give your campaign a name, and follow these steps to compose your webhook:

- **Webhook URL**: ht<span>tps://api.seen.io/v1/campaigns/{campaign_slug}/receivers/</span>
    - You will receive your campaign_slug from SEEN to call the correct endpoint.
- **HTTP Method**: POST
- **Request body**: Raw Text
    - You can use the code below as a starting point. Use [SEEN's documentation](https://docs.seen.io/api-documentation/ntRoJJ3rXoHzFXhA94JiHB/overview/tvy2F5tS3JRM7DfcHwz5fK#request-content) as a reference for the payload structure.
```json
[
    {
    "first_name":"{{${first_name}}}",
    "last_name":"{{${last_name}}}",
    "email":"{{${email_address}}}",
    "customer_id":"{{${braze_id}}}"
    }
]
```
>Remember to modify the payload depending on the personalisations in your film.
- **Request headers**:
    - Authorization → Token {token}
    - Content-Type → application/json
>You will receive your Authentication Token from SEEN.
- You can now test the webhook with a user by switching to the “Test” tab.
- If everything works as intended, you can proceed to finish the webhook setup.

<!-- Use the "Make a post request", "Default behavior," and "Rate limit" sections to outline how users can make a POST request. If this information isn't required for your integration, you can remove these sections. -->
### Step 2: CREATE DATA TRANSFORMATION TO RECEIVE DATA FROM SEEN

- Create new [Custom Attribute](https://www.braze.com/docs/user_guide/data_and_analytics/custom_data/custom_attributes/#managing-custom-attributes) fields for “landing_page_url” and “email_thumbnail_url”. These are the two attributes we will be using in this example.
- Open [“Data Transformation”](https://www.braze.com/docs/user_guide/data_and_analytics/data_transformation/creating_a_transformation/#prerequisites) tool under “Data Settings”, and click on “Create transformation”.
- Give your transformation a name, and choose:
    - “Start from scratch”
    - Destination → POST: Track users
- **Share your Webhook URL with SEEN.**
- You can use the code below as the starting point for the transformation:
```javascript
let brazecall = {
  "attributes": [
    {
      "braze_id": payload.customer_id,
      "_update_existing_only": true,
      "landing_page_url": payload.landing_page_url,
      "email_thumbnail_url": payload.email_thumbnail_url
    }
  ]
};
return brazecall;
```
>If you want to include other data, make sure to include those as well. Remember to discuss with SEEN as well so that the callback payload includes all needed fields.
- Send a test payload to the provided endpoint. If you want to use the callback payload defined in [our documentation](https://docs.seen.io/api-documentation/ntRoJJ3rXoHzFXhA94JiHB/callbacks/k9DEbcgkq3Vr2pxbHyPQbp), you can send this yourself via [Postman](https://www.postman.com/) or another similar service:
```json
{
        "customer_id": "101",
        "campaign_slug": "onboarding",
        "landing_page_url": "your.subdomain.com/v/12345",
        "video_url": "https://motions.seen.io/298abdcf-1f0f-46e7-9c26-a35b4c1e83cc/d3c1dffdf063986ad521a63e3e68fd7d1100c90a/output.m3u8",
        "thumbnail_url": "https://motions.seen.io/298abdcf-1f0f-46e7-9c26-a35b4c1e83cc/d3c1dffdf063986ad521a63e3e68fd7d1100c90a/thumbnail.jpg",
        "email_thumbnail_url": "https://motions.seen.io/298abdcf-1f0f-46e7-9c26-a35b4c1e83cc/d3c1dffdf063986ad521a63e3e68fd7d1100c90a/email_thumbnail.jpg"
       
}
```
- Click “Validate” to make sure everything works as intended.
- If everything worked as intended, click “Save” and “Activate”.

#### Rate limit

The SEEN API currently accepts 1000 calls per hour.

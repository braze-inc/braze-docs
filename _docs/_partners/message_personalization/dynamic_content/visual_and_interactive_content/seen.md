---
nav_title: SEEN
article_title: SEEN
description: "This reference article outlines the partnership between Braze and SEEN, a platform to design personalized videos to increase engagement throughout the customer journey."
alias: /partners/seen/
page_type: partner
search_tag: Partner
---

# SEEN

> [SEEN](https://seen.io/) is a personalization video platform that allows companies to create and build videos around their customers to deliver a more engaging experience. With SEEN, you can design a video around your data, personalize it at scale in the cloud, then distribute it where it works best.

## Use cases

SEEN offers automated video personalization across the entire customer journey. Common uses include onboarding, loyalty, sign-ups and conversion, and win-back and anti-churn.

## Prerequisites

Before you start, you'll need the following:

| Prerequisite          | Description                                                                                                                                |
|-----------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| A SEEN campaign   | A SEEN campaign is required to take advantage of this partnership.                                                                     |
| Data source   | You'll need to send data to SEEN to personalize your videos. Make sure you have all relevant data available in Braze, and that you pass data with **braze_id** as the identifier. |
| Braze Data Transformation Webhook URL   | Braze Data Transformation will be used to reformat the incoming data from SEEN so it can be accepted by Braze’s /users/track endpoint. |

## Rate limit

The SEEN API currently accepts 1,000 calls per hour.

## Integrating SEEN with Braze

In the following example, we'll send users' data to SEEN for video generation, and receive a unique landing page link and a unique, personalized thumbnail back to Braze for distribution. This example uses a POST webhook to send data to SEEN, and data transformation to receive the data back to Braze. If you have multiple video campaigns with SEEN, repeat the process to connect Braze with all video campaigns.

{% alert tip %}
If you experience any issues, reach out to your SEEN customer success manager for assistance.
{% endalert %}

### Step 1: Create a webhook campaign

Create a new [webhook campaign]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks) in Braze. Give your campaign a name, then refer to the following table to compose your webhook:

{% raw %}
<table>
  <thead>
    <tr>
      <th><strong>Field</strong></th>
      <th><strong>Details</strong></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Webhook URL</strong></td>
      <td>Use the following webhook URL. You will receive your <code>campaign_slug</code> from SEEN to call the correct endpoint.<br><br><code>https://api.seen.io/v1/campaigns/{campaign_slug}/receivers/</code></td>
    </tr>
    <tr>
      <td><strong>HTTP Method</strong></td>
      <td>Use the <code>POST</code> method.</td>
    </tr>
    <tr>
      <td><strong>Request body</strong></td>
      <td>Enter your request body in raw text similar to the following.<br><br><pre><code>[
    {
    "first_name":"{{${first_name}}}",
    "last_name":"{{${last_name}}}",
    "email":"{{${email_address}}}",
    "customer_id":"{{${braze_id}}}"
    }
]</code></pre><br>For more information, see <a href="https://docs.seen.io/api-documentation/ntRoJJ3rXoHzFXhA94JiHB/overview/tvy2F5tS3JRM7DfcHwz5fK#request-content">SEEN API</a>.</td>
    </tr>
    <tr>
      <td><strong>Request headers</strong></td>
      <td>Use the following information to fill out your request headers:<br>- <strong>Authorization:</strong> <code>Token {token}</code><br>- <strong>Content-Type:</strong> <code>application/json</code><br><br>You will receive your Authentication Token from SEEN.</td>
    </tr>
  </tbody>
</table>
{% endraw %}
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

You can now test the webhook with a user by switching to the **Test** tab.

If everything works as intended, go to Braze, then set the rate at which the campaign sends to 10 **messages per minute**. This way you won't exceed the SEEN's rate limit of 1,000 calls per hour.

### Step 2: Create data transformation

1. Create new [custom attribute]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#managing-custom-attributes) fields for `landing_page_url` and `email_thumbnail_url`. These are the two attributes we will be using in this example.
2. Open [Data Transformation]({{site.baseurl}}/user_guide/data_and_analytics/data_transformation/creating_a_transformation/#prerequisites) under **Data Settings**, and select **Create transformation**.
3. Give your transformation a name, then choose **Start from scratch** and set **Destination** to **POST: Track users**.
4. Select **Share your Webhook URL with SEEN**.
5. You can use the code below as the starting point for the transformation:

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
{% alert note %}
If you want to include other data, make sure to include those as well. Remember to discuss with SEEN as well so that the callback payload includes all needed fields.
{% endalert %}

{: start="6"}
6. Send a test payload to the provided endpoint. If you want to use the callback payload defined in the [SEEN documentation](https://docs.seen.io/api-documentation/ntRoJJ3rXoHzFXhA94JiHB/callbacks/k9DEbcgkq3Vr2pxbHyPQbp), you can send this yourself with [Postman](https://www.postman.com/) or another similar service:

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

{: start="7"}
7. Select **Validate** to make sure everything works as intended.
8. Select **Save** and **Activate**.

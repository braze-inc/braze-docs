---
nav_title: Wyng
article_title: Wyng
description: "This reference article outlines the partnership between Braze and Wyng, a zero-party data platform used to collect, use, and integrate customer preferences and attributes via micro-experiences, customer preference portals, and an API platform."
alias: /partners/wyng/
page_type: partner
search_tag: Partner
---

# Wyng

> [Wyng](https://wyng.com/) provides tools to build interactive digital experiences (quizzes, preference centers, promotions) that engage consumers at key moments, collect preferences and other zero-party data, and personalize in real time.

_This integration is maintained by Wyng._

## About the integration

The Braze and Wyng integration allows you to leverage zero-party data earned via Wyng experiences to personalize interactions in Braze Campaigns and Braze Canvas. Wyng can also power a preference center, so consumers can control the data and preferences (including communication preferences) they share with your brand.

## Prerequisites

| Requirement | Description |
| ----------- | ----------- |
| Wyng account | A Wyng account is required to take advantage of this partnership. |
| Braze REST API key | A Braze REST API key with `users.track` permissions. <br><br> This can be created in the Braze dashboard from **Settings** > **API Keys**. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integration

### Step 1: Connect the Braze integration

In Wyng, go to [**Integrations**](https://wyng.com/dashboard/integrations/) and select the **Add** tab. Next, hover over **Braze** and click **Connect** for the integration.

![The Braze partner tile in the Wyng platform.]({% image_buster /assets/img/wyng/2.png %}){: style="max-width:80%;"}

### Step 2: Configure the Braze connector

1. In the configuration window that opens, provide your Braze REST API key.
![An image of the what the credentials prompt looks like.]({% image_buster /assets/img/wyng/4.png %}){: style="max-width:80%;"}<br><br>
2. Next, use the dropdown to select the Wyng campaign you would like to share with Braze.![An image of the Braze connector prompting you to select an existing Wyng campaign you would like to share with Braze.]({% image_buster /assets/img/wyng/5.png %}){: style="max-width:80%;"}<br><br>
3. Next, you must set up subscriptions, attribute and event objects, and custom events.<br><br>
- **Subscriptions setup (required)**<br>
To subscribe users to subscription groups, click **Add Subscription** and add your subscription group name and ID. To add multiple group names and IDs, click the **Add Subscription** button again.<br>![An image prompting you for a subscription group name and ID.]({% image_buster /assets/img/wyng/8.png %}){: style="max-width:80%;"}<br><br>
- **User track setup**<br>
Click **Add custom property** to add attribute and event object pairs to send to the `/users/track` endpoint. Use this to add hard-coded attribute values for each data transaction sent for the integration. To add multiple properties, click the **Add custom property** button again.<br>![An image prompting you to add attribute custom properties.]({% image_buster /assets/img/wyng/9.png %}){: style="max-width:80%;"}<br><br>
- **Send custom event**<br>
Optionally, you can enable **Sending custom event**. If enabled, you should include the event name and corresponding app ID.<br>![An image prompting you to send custom events, if needed.]({% image_buster /assets/img/wyng/10.png %}){: style="max-width:80%;"}<br><br>
4. Lastly, you must map Wyng fields to Braze API fields based on your use case. Click **Select a field** to choose fields to map, and afterwards, **Save** your integration. When saved, these mapped fields can be found under **Integrations > Manage**.
![An example of the different Wyng fields you can map to certain Braze fields.]({% image_buster /assets/img/wyng/11.png %}){: style="max-width:80%;"}
![A list of available sync fields.]({% image_buster /assets/img/wyng/12.png %}){: style="max-width:80%;margin-top:2px"}

### Step 3: Test your integration

In Wyng, test submitting the form in your Wyng campaign. You can also submit it in the preview campaign if you do not want to add a record to the main production campaign. You should see a successful transaction in the **Integration** dashboard.

## Using this integration

Once the data connector is in place, any fields created in Wyng and added to Braze can be used just like any other data field to trigger campaigns, segment audiences, or feed personalized content.

Applications are broad, and specific questions can be addressed to [contact@wyng.com](mailto:contact@wyng.com) or your specific account manager.

## Troubleshooting

### Failed submission

In the case of a failed submission, when sending data to Braze, click on the **View Log** link to review the failed submission and the associated error message.

![The "View Log" link found under the actions header.]({% image_buster /assets/img/wyng/14.png %}){: style="max-width:80%;"}

The log page will show the failed submission, retry count, data from the submission, error, and a link to re-push the submission.

![An example of what a failed submission will show.]({% image_buster /assets/img/wyng/15.jpg %}){: style="max-width:80%;"}

The **View Error** section will show the error code and some additional information about the cause of the error. You can then cross-reference the error code with Braze to determine the cause.

![An example error log shown in the Wyng platform.]({% image_buster /assets/img/wyng/16.jpg %}){: style="max-width:80%;"}

If you have any additional questions, contact Wyng support ([support@wyng.com](mailto:contact@wyng.com)) for assistance.



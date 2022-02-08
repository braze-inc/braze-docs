---
nav_title: Wyng
article_title: Wyng
page_order: 1

description: "This article outlines the partnership between Braze and Wyng, a zero-party data platform, that makes it easy to collect, use, and integrate customer preferences and attributes via micro-experiences, customer preference portals, and an API platform."
alias: /partners/wyng/

page_type: partner
search_tag: Partner

---

# Wyng

> [Wyng][0], a zero-party data platform, makes it easy to collect, use, and integrate customer preferences and attributes via micro-experiences, customer preference portals, and an API platform.

The Braze and Wyng integration allows you to leverage Wyng experiences to deliver personalization in Braze campaigns and Canvases. Wyng also includes a customer preference portal so users can control the data and preferences they share with a brand.

## Prerequisites

| Requirement | Description |
| ----------- | ----------- |
| Wyng account | A Wyng account is required to take advantage of this partnership. |
| Braze REST API key | A Braze REST API key with `users.track` permissions. <br><br> This can be created within the __Braze Dashboard -> Developer Console -> REST API Key -> Create New API Key__ |
{: .reset-td-br-1 .reset-td-br-2}

## Integration

### Step 1: Connect the Braze integration

In Wyng, go to [**Integrations**][1] and select the **Add** tab. Next, hover over **Braze** and click **Connect** for the integration.

![Select the Braze tile][2]{: style="max-width:80%;"}

### Step 2: Configure the Braze connector

1. In the configuration window that opens, provide your Braze REST API key.
![Enter Braze API key][4]{: style="max-width:80%;"}<br><br>
2. Next, use the dropdown to select the Wyng campaign you would like to share with Braze.![Select a Wyng campaign][5]{: style="max-width:80%;"}<br><br>
3. Next, you must set up subscriptions, attribute and event objects, and custom events.<br><br>
- **Subscriptions setup (required)**<br>
To subscribe users to subscription groups, click **Add Subscription** and add your subscription group name and id. To add multiple group names and ids, click the **Add Subscription** button again.<br>![Add subscription group name and ID][8]{: style="max-width:80%;"}<br><br>
- **User track setup**<br>
Click **Add custom property** to add attribute and event object pairs to send to the users/track endpoint. Use this to add hardcoded attribute values for each data transaction sent for the integration. To add multiple properties, click the **Add custom property** button again.<br>![Add attribute custom properties][9]{: style="max-width:80%;"}<br><br>
- **Send custom event**<br>
Optionally, you can enable **Sending custom event**. If enabled, you should include the event name and corresponding app ID.<br>![Add custom events][10]{: style="max-width:80%;"}<br><br>
4. Lastly, you must map Wyng fields to Braze API fields based on your use case. Click **Select a field** to choose fields to map, and afterwards, **Save** your integration. Once saved, these mapped fields can be found under **Integrations > Manage**.
![Map Wyng form fields to Braze API fields][11]{: style="max-width:80%;"}
![Select a mapped field from the dropdown][12]{: style="max-width:80%;margin-top:2px"}

### Step 3: Test your integration

In Wyng, test submitting the form in your Wyng campaign. You can also submit it in the preview campaign if you do not want to add a record to the main production campaign. You should see a successful transaction in the **Integration** dashboard.

## Using this integration

Once the data connector is in place, any fields created in Wyng and added to Braze can be used just like any other data field to trigger campaigns, segment audiences, or feed personalized content.

Applications are broad, and specific questions can be addressed to [contact@wyng.com][13] or your specific account manager.

## Troubleshooting

### Failed submission

In the case of a failed submission, when sending data to Braze, click on the **View Log** link to review the failed submission and the associated error message.

![List active integrations][14]{: style="max-width:80%;"}

The log page will show the failed submission, retry count, data from the submission, error, and a link to re-push the submission.

![View submission log][15]{: style="max-width:80%;"}

The **View Error** section will show the error code and some additional information about the cause of the error. You can then cross-reference the error code with Braze to determine the cause.

![View error log][16]{: style="max-width:80%;"}

If you have any additional questions, please reach out to Wyng support ([support@wyng.com][13]) for assistance.

[0]: https://wyng.com/
[1]: https://wyng.com/dashboard/integrations/
[2]: {% image_buster /assets/img/wyng/2.png %}
[3]: {% image_buster /assets/img/wyng/3.png %}
[4]: {% image_buster /assets/img/wyng/4.png %}
[5]: {% image_buster /assets/img/wyng/5.png %}
[6]: {% image_buster /assets/img/wyng/6.png %}
[7]: https://www.braze.com/docs/api/basics/
[8]: {% image_buster /assets/img/wyng/8.png %}
[9]: {% image_buster /assets/img/wyng/9.png %}
[10]: {% image_buster /assets/img/wyng/10.png %}
[11]: {% image_buster /assets/img/wyng/11.png %}
[12]: {% image_buster /assets/img/wyng/12.png %}
[13]: mailto:contact@wyng.com
[14]: {% image_buster /assets/img/wyng/14.png %}
[15]: {% image_buster /assets/img/wyng/15.jpg %}
[16]: {% image_buster /assets/img/wyng/16.jpg %}
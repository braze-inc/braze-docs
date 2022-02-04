---
nav_title: Wyng
article_title: Wyng
page_order: 1

description: "The Wyng zero-party data platform makes it easy to collect, use, and integrate customer preferences and attributes via microexperiences, customer preference portals, and an API platform."
alias: /partners/message_personalization/dynamic_content/wyng

page_type: partner
search_tag: Partner
hidden: true

---

# Wyng

> The [Wyng][0] zero-party data platform makes it easy to collect, use, and integrate customer preferences and attributes via microexperiences, customer preference portals, and an API platform.

Expand Braze’s capabilities to build customer experiences that collect and use zero-party data to deliver personalization. Wyng also includes a customer preference portal where customers can control the data and preferences they share with a brand.

## Prerequisites

| Requirement | Description |
| ----------- | ----------- |
| Wyng account | A Wyng account is required to take advantage of this partnership. |
| Braze REST API key | A Braze REST API Key with `users.track` permissions. <br><br> This can be created within the __Braze Dashboard -> Developer Console -> REST API Key -> Create New API Key__ |
{: .reset-td-br-1 .reset-td-br-2}

## Use cases

Customers using Wyng can flow data from any Wyng experiences to Braze.
To try the connector in Wyng, go to the Integrations tab (More > Integrations) and click on **Add** to find the Braze connector.

## Integration

Here's how you can integrate your Wyng campaign form with Braze.

### Step 1: Select the integration

Go to [Integrations][1] and select the **Add** tab.

!["Select the Braze tile"][2]{: style="max-width:60%;display:block;"}

### Step 2: Connect the Braze integration
Hover over Braze and click **Connect** for the integration.

!["Connect the Braze integration"][3]{: style="max-width:60%;display:block;"}

### Step 3: Configure the Braze connector

The four-step integration configuration set up starts now.

1. Step 1 requires API Key. For help with the API key, please refer to [this section of the Braze documentation][7].
  !["Enter Braze API Key"][4]{: style="max-width:60%;display:block;margin:5px 0 10px 15px;"}
2. Under Step 2, you select the Wyng campaign you need the integration for. The dropdown "Select a Wyng campaign" will list all the campaigns under the property.
  !["Select a Wyng campaign"][5]{: style="max-width:60%;display:block;margin:5px 0 10px 15px;"}
3. Step 3 includes setting up Subscriptions, Attributes & event objects, and Custom event.
  !["Set-up Subscription"][6]{: style="max-width:60%;display:block;margin:5px 0 10px 15px;"}
  **Subscriptions setup**<br>
  Click the **Add Subscription** button to add the subscription group name and id. Using this users can be subscribed to subscription groups. Adding a subscription is mandatory to be able to proceed to the next step.
  !["Add subscription group name and ID"][8]{: style="max-width:60%;display:block;margin:5px 0 10px 15px;"}
  You can add multiple group names and ids by clicking on the Add Subscription button.<br>
  **User Track setup**<br>
  Click the **Add custom property** button to add attribute and event object pairs to be sent to the User Track endpoint. This can be used to add attribute values that are hardcoded for each data transaction sent for the integration.
  !["Add attribute custom properties"][9]{: style="max-width:60%;display:block;margin:5px 0 10px 15px;"}
  Similar to subscription, you can add multiple group names and ids by clicking on the **Add custom property** button.<br>
  **Send custom event**<br>
  Optionally you can enable **Sending custom event**. If enabled, you should include event name and corresponding app ID.
  !["Add custom events"][10]{: style="max-width:60%;display:block;margin:5px 0 10px 15px;"}
4. Step 4, the last step includes mapping Wyng form fields to the Braze API fields.
  !["Map Wyng form fields to Braze API fields"][11]{: style="max-width:60%;display:block;margin:5px 0 10px 15px;"}
  Click **Select a field** dropdown to choose the field to map.
  !["Select a mapped field from the dropdown"][12]{: style="max-width:60%;display:block;margin:5px 0 10px 15px;"}
  Click **Save** button on the bottom right to save your integration. Once saved, it will appear under **Integrations > Manage**.

### Step 4: Test your integration

Test submitting the form in your Wyng campaign. You can submit in the preview campaign if you do not want to add a record in the main production campaign. You should see a successful transaction in the Integration dashboard.

## Using this integration

Once the data connector is in place, any fields created in Wyng and added to Braze can be used just like any other data field - to trigger campaigns, segment audiences, or feed personalized content.

Applications are broad, and specific questions can be addressed to [contact@wyng.com][13] or your specific account manager.

## Troubleshooting

### Failed Submission:

In the case of a failed submission when sending data to Braze click on the “View Log” Link to review the failed submission and the associated error message.
!["List active integrations"][14]{: style="max-width:60%;display:block;margin:5px 0 10px 15px;"}
The log page will show the failed submission, retry count, data from the submission, error, and a link to re-push the submission.
!["View submission log"][15]{: style="max-width:60%;display:block;margin:5px 0 10px 15px;"}
The **View Error** section will show the error code and some additional information about the cause of the error. You can then cross reference the error code with Braze to determine the cause.
!["View error log"][16]{: style="max-width:60%;display:block;margin:5px 0 10px 15px;"}
If you have any additional questions please reach out to Wyng support ([support@wyng.com][17]) for assistance

[0]: https://wyng.com/
[1]: https://wyng.com/dashboard/integrations/
[2]: {% image_buster /assets/img/wyng/2.jpeg %}
[3]: {% image_buster /assets/img/wyng/3.jpeg %}
[4]: {% image_buster /assets/img/wyng/4.jpeg %}
[5]: {% image_buster /assets/img/wyng/5.jpeg %}
[6]: {% image_buster /assets/img/wyng/6.jpeg %}
[7]: https://www.braze.com/docs/api/basics/
[8]: {% image_buster /assets/img/wyng/8.jpeg %}
[9]: {% image_buster /assets/img/wyng/9.jpeg %}
[10]: {% image_buster /assets/img/wyng/10.jpeg %}
[11]: {% image_buster /assets/img/wyng/11.jpeg %}
[12]: {% image_buster /assets/img/wyng/12.jpeg %}
[13]: mailto:contact@wyng.com
[14]: {% image_buster /assets/img/wyng/14.jpg %}
[15]: {% image_buster /assets/img/wyng/15.jpg %}
[16]: {% image_buster /assets/img/wyng/16.jpg %}
[17]: mailto:support@wyng.com
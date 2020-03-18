---
nav_title: PassKit
alias: /partners/passkit/

description: "This article outlines the partnership between Braze and Passkit, enables you to extend your mobile reach by integrating Apple Wallet and Google Pay passes into your customers experience."
page_type: partner

---

# PassKit

> PassKit enables you to extend your mobile reach by integrating Apple Wallet and Google Pay passes into your customers experience. Easily create, manage, distribute and analyze the performance of digital coupons, loyalty cards, membership cards, tickets and much more; without your customers needing another app.

Deliver seamless, connected online to offline customer experiences with Braze and PassKit. Increase engagement with and measure engagement of your online campaigns by instantly delivering Apple Wallet and Google Pay passes. Analyze usage and make real time adjustments to increase in-store traffic by triggering location based messages and personalized, dynamic updates to your customers mobile wallet.

{% alert important %}
This partnership is in early access beta. All features may not perform as exactly described. Please reach out to your Braze Account Manager for more information.
{% endalert %}

## Pre-Requisites

| Requirement    | Origin                                                | Description                                                             |
| -------------- | ----------------------------------------------------- | ----------------------------------------------------------------------- |
| PassKit Account | PassKit | You will need to have a PassKit account and a PassKit account manager.|
| PassKit SDK integration | Client | You will need to integrate the PassKit SDK. Working with your PassKit account manager, they will be able to assist in consulting and building templates, Apple Wallet templates, and Google Pay templates. |
| Custom API Proxy | PassKit | This is required for basic authentication within the HTTP header of your webhook requests. |
| userDefinedID | Client | In order to appropriately update custom events and custom attributes to your users between PassKit and Braze, you will need to set the Braze external ID as the userDefinedID.|
| Braze API Key | Braze | You will need to create a new API Key can be created in the Developer Console -> API Settings -> +Create New API Key with *users.track* permissions. The Braze API key will need to be provided to your Rokt account manager.|
| [Braze REST Endpoint]({{ site.baseurl }}/api/basics?redirected=true#endpoints) | Braze | Your REST Endpoint URL will need to be provided to your PassKit account manager to pass subscriber data into Braze.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

## API Integration

To further enrich your customers’ mobile wallet experiences, you can work with your PassKit account manager to pass data into Braze through Braze’s [Users Track Endpoint]({{ site.baseurl }}/api/endpoints/user_data/#user-track-endpoint). Examples of data to share from PassKit includes:

- Pass Issue: when a customer clicks on a pass link and is first shown a pass.
- Pass Installs: when the customer adds/saves the pass to their wallet app.
- Pass updates: when a pass is updated.
- Pass delete: when a customer deletes the pass from their wallet app.

Once the data is passed into Braze, you can build audiences, personalize content via liquid, and trigger campaigns or Cavanses once these actions have been performed.

In order to pass data from PassKit, please ensure that you have:
- Set your Braze external ID as PassKit’s userDefinedID.
- Provide your PassKit account manager with a Braze API Key.
- Provide your PassKit account manager with a Braze REST Endpoint.

## Using PassKit in Your Braze Campaigns & Canvases

Within Braze, you can setup a webhook campaign or a webhook within a Canvas to either:

- Create a new pass.
- Update an existing pass.

Before you get started, here are the common JSON Payload Parameters that you can include within your Create and Update webhooks to PassKit.

| Data              | Type             | Description      |
| ----------------  | ---------------- | ---------------- |
| `campaignName` <br> _Required._ | string | This is the name of the campaign you created. For more detail, please see [Create Campaign](https://dev.passkit.net/v3/#create-a-campaign). This value cannot be changed after a pass created. |
| `templateName` <br> _Required._ | string | Required. This is the name of the template you created. For more detail, please see [Create Template](https://dev.passkit.net/v3/#create-a-template).|
| `dynamicData` | object | A key pair value JSON object. This is the user’s unique data. For example, customer name, date of birth, membership number. etc. The data will not show on the pass until it is defined in the template. See the example json for an example of the format. |
| `dynamicImages` | object | This is used to define a dynamic image for a pass, like a profile image on a membership pass. The value is the image path from Images Upload Endpoint. Please also see the sections Passbook Image Types and Dynamic Image Keys for more information regarding pass images. |
| `userDefinedId` | string | This allows a unique Id to be added to the pass record that can provide easy compatible with an existing system using unique customer identifiers (e.g. membership numbers). You can retrieve pass data by using this endpoint via [userDefinedId](https://dev.passkit.net/v3/#retrieve-a-pass-with-user-defined-id) and campaignName instead of pass ID. This value must be unique within a campaign, and once this value is set, it cannot be changed. <br> For the Braze integration, we would recommend using the [Braze external ID]({{ site.baseurl }}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/#identified-user-profiles). |
| `recoveryEmail` | string | The user’s email address. If this parameter is used, the user will receive an email containing a link to the pass. |
| `isVoided` | bool | When this field set to true, the pass will be voided. When the pass is voided the barcode will be greyed out and beacon and location notification will be turned off. Default value is false. |
| `isRedeemed` | bool | When this field set to true, the pass will be marked as redeemed. Default value is false. |
| `isInvalid` | bool | When this field set to true, the pass is invalidated The barcode, beacon and location messages will be removed and the pass can no longer be communicated with. Once a pass is set as invalidated, it cannot be changed. Default is false. |
| `expiryDate` | ISO8601 datetime | This is the pass expiry date. After the expiry date, the pass is automatically voided (see isVoided). This value will override the template and campaign end date value. |
| `passbook` | object | This is where the Apple Wallet (Passbook) specific parameters are defined. Please see [Passbook](https://dev.passkit.net/v3/#passbook). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}


### Create a New Pass via Webhook

##### Step 1: Create a Webhook Template in Braze

You can create this from the `Templates & Media` section, or create a new Webhook Campaign or Canvas in Braze.

Passkit IMage 1

Once you have selected the `PassKit - Create Pass` webhook template, you should see the following in the composer:

- `Webhook URL`: https://braze.passkitapi.com/v1/passes
- `Request Body`: Raw Text
- `HTTP Method`: POST

##### Step 2: Fill Out Your Template

Here is a generic template that can help you get started in building your pass. Your can add / edit the JSON Payload parameters and liquid to fit your use case. If you have worked with your PassKit account manager on customized templates or images, they will be able to help you add the appropriate JSON payload parameters for your campaign.

{% raw %}
```javascript
{% assign templateName= "example_templateName" %}
{% assign campaignName = "example_campaignName" %}
{% capture name %}{{${first_name} | default: "Friend" }}{% endcapture %}
{% capture membership_status %}{{custom_attribute.${memebership_status} | default: "General" }}{% endcapture %}
{% capture weekend_coupon %}Weekend123{% endcapture %}
{
  "campaignName": "campaignName",
  "templateName": "templateName",
  "userDefinedId": "{{${user_id}}}",
  "expiryDate": "2016-04-11T12:59:40Z",
  "dynamicData": {
    "name": "{{name}}",
    "membership": "{{membership_status}}",
    "coupon": "{{weekend_coupon}}",
  },
  "passbook": {
    "relevantDate": "2019-29-09T12:59:40Z"
  }
}

```
{% endraw %}

##### Step 3: Fill Out Your Request Headers & Select HTTP Method

| HTTP Header       | Definition       |
| ----------------  | ---------------- |
| Authorization  | Basic {{ '[INSERT_YOUR_API_PROXY]' | base64_encode }} |
| Content-Type  | application/json |
{: .reset-td-br-1 .reset-td-br-2}

Ensure that your `HTTP Method` is set to **Post**.

##### Step 4: Preview Your Request

You will see that your raw text automatically highlights if it is an applicable Braze tag.

You should be able to preview your request in the left-hand panel, or navigate to the `Test` tab, where you can select a random user, an existing user, or customize your own to test your webhook.

{% alert important %}
Remember to save your template before leaving the page!
{% endalert %}


#### Update a Pass via Webhook

##### Step 1: Create a Webhook Template in Braze

You can create this from the `Templates & Media` section, or create a new Webhook Campaign or Canvas in Braze.

Once you have selected the `PassKit - Update Pass` webhook template, you should see the following in the composer:

{% raw %}
- `Webhook URL`: https://braze.passkitapi.com/v1/passes/{insert_campaign_name}/{{${user_id}}}
  - _Note: You will need to manually input your campaign name within the URL._
- `Request Body`: Raw Text
- `HTTP Method`: PUT
{% endraw %}

##### Step 2: Fill Out Your Template

To setup the webhook, fill out the details of the new event within the Request Body.

{% raw %}
```javascript
{% assign templateName= "example_templateName" %}
{% assign campaignName = "example_campaignName" %}
{% capture name %}{{${first_name} | default: "Friend" }}{% endcapture %}
{% capture membership_status %}{{custom_attribute.${memebership_status} | default: "General" }}{% endcapture %}
{% capture weekend_coupon %}Weekend1234{% endcapture %}
{
  "campaignName": "campaignName",
  "templateName": "templateName",
  "userDefinedId": "{{${user_id}}}",
  "expiryDate": "2016-04-11T12:59:40Z",
  "dynamicData": {
    "name": "{{name}}",
    "membership": "{{membership_status}}",
    "coupon": "{{weekend_coupon}}",
  },
  "passbook": {
    "relevantDate": "2019-29-09T12:59:40Z"
  }
}
```
{% endraw %}

##### Step 3: Fill Out Your Request Headers & Select HTTP Method

| HTTP Header       | Definition       |
| ----------------  | ---------------- |
| Authorization  | Basic {{ '[INSERT_YOUR_API_PROXY]' | base64_encode }}|
| Content-Type  | application/json |
| Cache-Control | no-cache |
{: .reset-td-br-1 .reset-td-br-2}

Ensure that your `HTTP Method` is set to **PUT**.

##### Step 4: Preview Your Request

You will see that your raw text automatically highlights if it is an applicable Braze tag.

You should be able to preview your request in the left-hand panel, or navigate to the `Test` tab, where you can select a random user, an existing user, or customize your own to test your webhook.

{% alert important %}
Remember to save your template before leaving the page!
{% endalert %}

### Publish Passes via Connected Content

In addition to creating and updating passes, you can also retrieve the pass URL and other metadata via Braze’s Connected Content in order to incorporate personalized pass details and URL within your messaging campaigns.

{% raw %}
```liquid
{% connected_content https://braze.passkitapi.com/v1/passes/{{/{{${user_id}}} :basic_auth [Insert_Credentials] :save passes %}{{passes.url}}
```
{% endraw %}

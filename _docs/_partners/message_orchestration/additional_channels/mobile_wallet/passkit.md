---
nav_title: PassKit
alias: /partners/passkit/

description: "This article outlines the partnership between Braze and Passkit. This partnership enables you to extend your mobile reach by integrating Apple Wallet and Google Pay passes into your customers experience."
page_type: partner

---

{% alert important %}
This partnership is in early access beta. All features may not perform as exactly described. Please reach out to your Braze Account Manager for more information.
{% endalert %}

# PassKit

> PassKit enables you to extend your mobile reach by integrating Apple Wallet and Google Pay passes into your customer's experience. Easily create, manage, distribute, and analyze the performance of digital coupons, loyalty cards, membership cards, tickets, and much more; without your customers needing another app.

Deliver seamless, connected online to offline customer experiences with Braze and PassKit. Increase and measure the engagement of your online campaigns by instantly delivering Apple Wallet and Google Pay passes. Analyze usage and make real-time adjustments to increase in-store traffic by triggering location-based messages and personalized, dynamic updates to your customer's mobile wallet.

## Prerequisites

| Requirement | Origin | Description |
| ----------- | ------ | ----------- |
| PassKit Account | PassKit | You will need to have a PassKit account and a PassKit account manager.|
| userDefinedID | Client | To appropriately update custom events and custom attributes to your users between PassKit and Braze, you will need to set the Braze external ID as the userDefinedID. This userDefinedID will be used when making API calls to the PassKit Endpoints. |
| Braze API Key | Braze | You will need to create a new API Key.<br><br>This can be created in the __Developer Console -> API Settings -> Create New API Key__ with __users.track__ permissions. |
| [Braze REST Endpoint][6] | Braze | Your REST Endpoint URL. Your endpoint will depend on the Braze URL for your instance. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

## API Integration

To further enrich your customers’ mobile wallet experiences, from within your PassKit dashboard you can opt to pass data into Braze through Braze’s [Users Track Endpoint][7]. 

Examples of data to share from PassKit includes:
- __Pass Created__: when a customer clicks on a pass link and is first shown a pass.
- __Pass Installs__: when the customer adds/saves the pass to their wallet app.
- __Pass Updates__: when a pass is updated.
- __Pass Delete__: when a customer deletes the pass from their wallet app.

Once the data is passed into Braze, you can build audiences, personalize content via Liquid, and trigger campaigns or Cavanses once these actions have been performed.

### Connect PassKit to Braze

To pass data from PassKit, please ensure that you have set your Braze external ID as PassKit’s externalId.

1. Within Settings, under Integrations within your PassKit Pass Project or Program click Connect under the Braze Tab.<br>![Settings Button][5]{: style="max-width:60%"}
2. Fill out your Braze API Key, Endpoint URL, and provide a name for your connector.
3. Toggle Enable Integration, and whichever events you want in Braze to trigger or personalize your messages with.<br>![Connect to Braze][4]{: style="max-width:50%"}

## Create Pass using a SmartPass Link

Within Braze, you can setup a SmartPass Link to generate a unique URL for your customers to install their pass on either Android or iOS.

### Prerequisites

| Requirement | Origin | Description | Example | 
| ----------- | ------ | ----------- | ------- |
| __PassKit URL__ | PassKit | Your PassKit URL is a unique URL for your passkit program.  <br><br>Each program has a unique URL, and you can find it under the __Distribution__ tab of your PassKit Program/Project. | https://pub1.pskt.io/c/ww0jir |
| __PassKit Secret__| PassKit | Along with the URL, you will need to have the PassKit Key for this program handy.  <br><br>This can be found on the same page as your PassKit URL. | 5AuNonZoFHejGXmHNATz4l |
| __Program (or Project) ID__| PassKit | Your PassKit Program ID will be required to create the SmartPass URL. <br><br>You can find it under the __Settings__ tab of your project or program. | 1x3j9vWjSGx2UwUblYlcue |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

### PassKit Integrations

For more information on creating encrypted SmartPass Links, check out this [PassKit Article][8].

To begin creating a SmartPass URL, you should create this encryption within a Braze [Content Block][9]. Creating it this way will allow you to re-use the block for future passes and coupons. 

#### Step 1: Define your Pass Data Payload
First, you must define the coupon or member payload. 

There are many different components you can include in your payload, but here as two important ones to note:

| Component | Required | Type | Description |
| --------- | -------- | ---- | ----------- |
|`person.externalId​` | Required | String | Set as the Braze External ID, this is crucial for the callbacks from PassKit back to Braze to work, allowing Braze users to have coupons for multiple offers in one campaign. Not enforced as unique. |
| `members.member.externalId​` | Optional | String | Set as the Braze External ID, you may use your External ID to update the membership pass. Setting this field enforces the user as unique within the membership program.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

For a full list of available fields, their types, and helpful descriptions have a look at the [PassKit Github Documentation][10].

Example Payload
{% raw %}
```liquid
{
  "members.member.externalId": "{{${user_id}}}",
  "members.member.points": "100",
  "members.tier.name": "current_customer",
  "person.displayName": "{{${first_name}}} {{${last_name}}}",
  "person.externalId": "{{${user_id}}}",
  "universal.expiryDate": "{{ "now" | date: "%s" | plus: 31622400 | date: "%FT%TZ" }}"
}
```
{% endraw %}

#### Step 2: Create and Encode an Undefined Payload Variable

First, create and name a new content block by navigating to `Templates & Media` within the Braze Dashboard. Here you can find the Content Block Library tab, select `Create Content Block` to get started.

Next, you must define your __Content Block Liquid Tag__. After saving this content block, this Liquid tag can now be referenced when composing messages. In this example, we have assigned the Liquid tag as {% raw %}`{{content_blocks.${passKit_SmartPass_url}}}`{% endraw %}. 

Within this content block, we will not directly include the payload written above, but reference it in a {% raw %}`{{passData}}`{% endraw %} variable. The first code snippet you must add to your content block captures a Base64 encoding of the {% raw %}`{{passData}}`{% endraw %} variable.
{% raw %}
```liquid
{% capture base64JsonPayload %}{{passdata|base64_encode}}{% endcapture %}
```
{% endraw %}

#### Step 3: Create Your Encryption Signature using a SHA1 HMAC Hash

Next, you will be creating your encryption signature using a [SHA1 HMAC][16] hash of the project URL and the payload. 

The second code snippet you must add to your content block captures the URL to be used for hashing.
{% raw %}
```liquid
{% capture url %}{{projectUrl}}?data={{base64JsonPayload}}{% endcapture %}
```
{% endraw %}

Next, you must generate a signature using this hash and your `Project Secret`. This can be done by including a third code snippet, shown below. 
{% raw %}
```liquid
{% capture sig %}{{url | hmac_sha1: "Project_Secret"}}{% endcapture %}
```
{% endraw %}

Finally, append the signature to the full URL using the fifth code snippet, shown below.
{% raw %}
```liquid
{% capture longUrl %}{{projectUrl}}?data={{base64JsonPayload}}&sig={{sig}}{% endcapture %}
```
{% endraw %}

#### Step 4: Print Your URL

Lastly, make sure you call your final URL so that it prints your SmartPass URL within your message.
{% raw %}
```liquid
{{longURL}}
```
{% endraw %}

At this point you will have created a content block that looks something like this:

{% raw %}
```liquid
{% capture base64JsonPayload %}{{passdata|base64_encode}}{% endcapture %}

{% capture url %}{{projectUrl}}?data={{base64JsonPayload}}{% endcapture %}

{% capture sig %}{{url | hmac_sha1: "Project_Secret"}}{% endcapture %}

{% capture longUrl %}{{projectUrl}}?data={{base64JsonPayload}}&sig={{sig}}&utm_source=braze&utm_campaign={{campaign.${name}}}{% endcapture %}{% capture longUrl %}{{longUrl | url_encode}}{% endcapture %}

{{longURL}}
```
{% endraw %}

In this example, UTM parameters have been added to track the source of these installs back to Braze and this campaign.

{% alert important %}
Remember to save your content block before leaving the page!
{% endalert %}

#### Step 5: Putting it All Together

Once this content block has been made it can be reused again in the future. 

You may notice there are two variables left undefined in the above content block.<br> 
{% raw %}`{{passData}}`{% endraw %} - Your JSON pass data payload defined in [step 1](#passkit-integrations) <br>
{% raw %}`{{projectUrl}}`{% endraw %} - Your project or program's URL which you find on the distribution tab of your Passkit project.

This decision was purposeful and ensures the reusability of the content block. Because these variables are only referenced, not created within the content block, it allows for these variables to change without remaking the content block. 

For example, maybe you want to change the introductory offer to include more initial points in your loyalty program, or perhaps you want to create a secondary member card or coupon. These scenarios would require different Passkit projectURLs or different pass payload which you would define per campaign in Braze.  

### Composing the Message Body

In your message body, you’ll want to capture both of these variables and then call your content block. 
Capture your minified JSON payload from [step 1](#passkit-integrations) above:

__1.__ Assign the Project URL
{% raw %}
```liquid
{% assign projectUrl = "https://pub1.pskt.io/c/ww0jir" %}
```
{% endraw %}

__2.__ Capture the JSON created in Step 1.
{% raw %}
```liquid
{% capture passData %}{"members.member.externalId": "{{${user_id}}}","members.member.points": "100","members.tier.name": "current_customer","person.displayName": "{{${first_name}}} {{${last_name}}}","person.externalId": "{{${user_id}}}","universal.expiryDate": "{{ "now" | date: "%s" | plus: 31622400 | date: "%FT%TZ" }}"}{% endcapture %}
```
{% endraw %}

__3.__ Reference the content block you just made. 
{% raw %}
```liquid
{{content_block.${passkit_SmartPass_url}}}
```
{% endraw %}

Your Message Body should look something like this:
![Message Body][1]{: style="max-width:70%"}

The output URL for the sample above is:
![Output URL][2]{: style="max-width:70%"}

That looks long doesn’t it? The reason for this is due to it containing all the pass data in addition to incorporating best in class security to ensure data integrity and no tempering via URL modification. If using SMS to distribute this URL, you may want to run it through a link shortening process such as [bit.ly][3]. This can be done through a Connected Content call to a bit.ly endpoint!

## Update Pass Using the PassKit Webhook

Within Braze, you can setup a webhook campaign or a webhook within a Canvas to update an existing pass based on your user's behavior. Check out the links below for information on useful PassKit Endpoints. 
- [Member Projects][12]
- [Coupon Projects][13]
- [Flights Projects][14]

### Prerequisites
Before you get started, here are the common JSON Payload Parameters that you can include within your Create and Update webhooks to PassKit.

| Data | Type | Description |
| ---- | ---- | ----------- |
| `externalId` | String | This allows a unique Id to be added to the pass record that can provide compatibility with an existing system using unique customer identifiers (e.g. membership numbers). You can retrieve pass data by using this endpoint via userDefinedId and campaignName instead of pass ID. This value must be unique within a campaign, and once this value is set, it cannot be changed.<br><br>For the Braze integration, we would recommend using the Braze external ID: {% raw %}{{${user_id}}}{% endraw %} |
| `campaignId` (coupon) <br><br> `programId` (membership) | String | This is the ID for the campaign/program template you created in PassKit. To find this, head to the __Settings__ tab in your PassKit pass project. |
| `expiryDate` | IO8601 DateTime | This is the pass expiry date. After the expiry date, the pass is automatically voided (see isVoided). This value will override the template and campaign end date value. |
| `status` | String | This is the current status of a coupon, such as “REDEEMED” or “UNREDEEMED”. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

### Webhook Integration

#### Step 1: Create a Webhook Template in Braze

You can create this from the `Templates & Media` section, or create a new Webhook Campaign or Canvas in Braze. Next, select the PassKit - Update Pass webhook template, you should see the following in the composer:

__Webhook URL__ (Compose Tab): https://api-pub1.passkit.io/coupon/singleUse/coupon<br>
__Request Body__ (Compose Tab): application/json<br>
__HTTP Method__ (Settings Tab): PUT

#### Step 2: Fill Out Your Template
To set up the webhook, fill out the details of the new event within the Request Body:
{% raw %}
```liquid
{
  “externalId”: “{{${user_id}}}”,
  “campaignId”: “ 2xa1lRy8dBz4eEElBfmIz8”,
  “expiryDate”: “2020-05-10T00:00:00Z”
}
```
{% endraw %}

#### Step 3: Fill Out Your Request Headers

| HTTP Header       | Definition       |
| ----------------  | ---------------- |
| Authorization  | Bearer [INSERT_YOUR_LONG_LIVED_TOKEN] |
| Content-Type  | application/json |
{: .reset-td-br-1 .reset-td-br-2}

Ensure that your `HTTP Method` is set to **PUT**.

__Retrieve Your PassKit Long Lived Token__<br>
To retrieve your token, navigate to your PassKit Project/Program within the PassKit Admit Account. From here, go to Integrations within Settings, and select "Love Lived Integration Token" from the left-hand sidebar. Here, you find your long lived token. 

#### Step 4: Preview Your Request

You will see that your raw text automatically highlights if it is an applicable Braze tag.

You can preview your request in the left-hand panel or navigate to the `Test` tab, where you can select a random user, an existing user, or customize your own to test your webhook.

{% alert important %}
Remember to save your template before leaving the page!
{% endalert %}

## Retrieve Pass Details via Connected Content

In addition to creating and updating passes, you can also retrieve your users’ pass metadata via Braze’s Connected Content in order to incorporate personalized pass details within your messaging campaigns. For more information on how to run Connected Content calls, check out our [documentation][15]. 

__PassKit Connected Content Call__

{% raw %}
```liquid
{% connected_content  https://api-pub1.passkit.io/coupon/singleUse/coupon/externalId/{{${user_id}}} :headers {"Authorization": "Bearer [INSERT_YOUR_LONG_LIVED_TOKEN]","Content-Type": "application/json"} :save passes %}

{{passes.status}} 
```
{% endraw %}

__Liquid Example Responses:__

{% tabs local %}
{% tab {{passes.redemptionDetails}} %}

```json
{
    "redemptionDate": null,
    "redemptionCode": "",
    "lat": 0,
    "lon": 0,
    "alt": 0,
    "redemptionSource": "",
    "redemptionReference": "",
    "transactionReference": "",
    "transactionAmount": 0
}
```

{% endtab %}
{% tab {{passes.status}} %}
```
UNREDEEMED 
```
{% endtab %}
{% endtabs %}

[1]: {% image_buster /assets/img/passkit/passkit1.png %}
[2]: {% image_buster /assets/img/passkit/passkit2.png %}
[3]: https://dev.bitly.com/v4/#operation/createFullBitlink
[4]: {% image_buster /assets/img/passkit/passkit4.png %}
[5]: {% image_buster /assets/img/passkit/passkit5.png %}
[6]: {{site.baseurl}}/api/basics?redirected=true#endpoints
[7]: {{site.baseurl}}/api/endpoints/user_data/#user-track-endpoint
[8]: https://help.passkit.com/en/articles/3742778-hashed-smartpass-links
[9]: {{site.baseurl}}/user_guide/engagement_tools/templates_and_media/content_blocks/#content-blocks
[10]: https://github.com/PassKit/smart-pass-link-from-csv-generator
[12]: https://docs.passkit.io/protocols/member/
[13]: https://docs.passkit.io/protocols/coupon/
[14]: https://docs.passkit.io/protocols/boarding/
[15]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/making_an_api_call/
[16]: https://en.wikipedia.org/wiki/HMAC

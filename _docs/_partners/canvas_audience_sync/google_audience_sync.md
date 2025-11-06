---
nav_title: Google
article_title: Canvas Audience Sync to Google
alias: /google_audience_sync/
description: "This reference article will cover how to use Braze Audience Sync to Google, to deliver advertisements based upon behavioral triggers, segmentation, and more."
Tool:
  - Canvas
page_order: 3

---

# Audience Sync to Google

{% alert important %}
Google is updating its [EU User Consent Policy](https://www.google.com/about/company/user-consent-policy/) in response to changes to the [Digital Markets Act (DMA)](https://ads-developers.googleblog.com/2023/10/updates-to-customer-match-conversion.html), which is in effect as of March 6, 2024. This new change requires advertisers to disclose certain information to their EEA, UK, and Switzerland end users, as well as obtain necessary consent from them. Review the following documentation to learn more.
{% endalert %}

The Braze Audience Sync to Google integration enables brands to extend the reach of their cross-channel customer journeys to Google Search, Google Shopping, Gmail, YouTube, and Google Display. Using your first-party customer data, you can securely deliver ads based on dynamic behavioral triggers, segmentation, and more. Any criteria you'd typically use to trigger a message (for example, push, email, or SMS) as part of a Braze Canvas can be used to trigger an ad to that user with Google's [Customer Match](https://support.google.com/google-ads/answer/6379332?hl=en).

{% alert note %}
The Braze Audience Sync to Google integration is supported for Google Ads, not Google Ads Manager.
{% endalert %}

Google Ads no longer generates similar audiences, also known as "lookalike audiences," for targeting and reporting. Refer to [Google Ads documentation](https://support.google.com/google-ads/answer/12463119?) to learn more.

**Common use cases for syncing Custom Audiences include:**
- Targeting high-value users via multiple channels to drive purchases or engagement.
- Retargeting users who are less responsive to other marketing channels.
- Creating suppression audiences to prevent users from receiving advertisements when they're already loyal consumers of your brand.

{% alert note %}
This feature lets brands control what specific first-party data is shared with Google. At Braze, the integrations with which you can and cannot share your first-party data are given the utmost consideration. Learn more about our [Braze data privacy policy](https://www.braze.com/privacy).
{% endalert %}

## Prerequisites

Make sure the following items are created and completed before setting up your Google Audience step in Canvas.

| Requirement | Origin | Description |
| ----------- | ------ | ----------- |
| Google Ads Account | [Google](https://support.google.com/google-ads/answer/6366720?hl=en) | An active Google ads account for your brand.<br><br>If you're looking to share an audience across multiple managed accounts, you can upload your audiences into your [manager account](https://support.google.com/google-ads/answer/6139186). |
| Google Ads Terms and Google Ads Policies | [Google](https://support.google.com/adspolicy/answer/54818?hl=en) | You must accept and ensure you comply with [Google’s Ad Terms](https://payments.google.com/u/0/paymentsinfofinder?hostOrigin=aHR0cHM6Ly9wYXltZW50cy5nb29nbGUuY29tOjQ0Mw..&sri=-40) and [Google’s Ad Policies](https://support.google.com/adspolicy/answer/6008942?sjid=15557182366992806023-NC), which include the [EU User Consent Policy](https://www.google.com/about/company/user-consent-policy/), as applicable to you, in your use of Braze Audience Sync.<br><br>Consult with your Legal Team on Google’s new EU User Consent Policy to ensure you are collecting appropriate consent in order to use Google Ads’ services for your EEA, UK, and Switzerland end users. |
| Google Customer Match | [Google](https://support.google.com/google-ads/answer/6299717) |  Customer Match is not available for all advertisers.<br><br>**To use Customer Match, your account must have:**<br>• A good history of policy compliance<br>• A good payment history<br>• At least 90 days history in Google Ads<br>• More than USD 50,000 total lifetime spend. For advertisers whose accounts are managed in currencies other than USD, your spend amount will be converted to USD using the average monthly conversion rate for that currency.<br><br>If your account does not meet these criteria, then your account is currently ineligible to use Customer Match.<br><br>Connect with your Google Ads representative for more guidance on Customer Match availability for your account. |
| Google Consent Signals | [Google](https://support.google.com/google-ads/answer/14310715) |  If you want to serve ads to EEA end users using Google’s Customer Match service, you’ll need to pass Braze the following custom attributes (boolean) as part of Google’s  EU User Consent Policy. More details can be found under [Collecting consent for EEA, UK, and Switzerland end users](#collecting-consent-for-eea-uk-and-switzerland-end-users): <br> - `$google_ad_user_data` <br> - `$google_ad_personalization` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### Required SDK versions

When using Braze SDKs to collect consent signals, ensure you meet the following minimum versions:

{% sdk_min_versions swift:7.6.0 android:1.3.2 web:3.0.0 %}

### Collecting consent for EEA, UK, and Switzerland end users

Google’s EU User Consent Policy requires advertisers to disclose the following to their EEA, UK, and Switzerland end users, as well as obtain their consent for such:

* The use of cookies or other local storage where legally required; and
* The collection, sharing, and use of their personal data for the personalization of ads.

This does not affect US end users or any other end users located outside of the EEA, the UK, or Switzerland. Consult with your legal team on Google’s new EU User Consent Policy to ensure you are collecting appropriate consent in order to use Google Ads’ services for your EEA, UK, and Switzerland end users.

Under the Digital Markets Act (DMA) requirements in effect as of March 6, 2024, advertisers must pass consent for EEA, UK, and Switzerland end users when sharing data with Google. As part of this change, you can collect both consent signals in Braze as the following boolean custom attributes:

* `$google_ad_user_data`
* `$google_ad_personalization`

Braze will sync the data from these custom attributes to the appropriate [consent fields in Google](https://support.google.com/google-ads/answer/14310715#:~:text=These%20consent%20fields%20are%3A).

#### Managing revoked consent

To keep your audience lists up-to-date in the event an EEA end user has been added to the audience list, and then has subsequently retracted any of the two consents (`$google_ad_user_data` or `$google_ad_personalization`), you must set up a Canvas to remove users from the existing audience lists using an Audience Sync step.

{% alert note %}
If an EEA previously provided consent for both signals, that data will continue to be used for Google’s Customer Match until that list expires, or that consent status is explicitly updated via Google Audience Sync, or both.
{% endalert %}

#### Tips

* Send the value as a boolean type, not a string type.
* Prefix the dollar sign ($) for the attribute name. Braze uses a dollar sign at the start of an attribute name to dictate this is a special and reserved key.
* Enter the attribute name in lowercase.
* While you can't explicitly set a user as unspecified, if you send a `null` or `nil` value or any value that isn't `true` or `false`, Braze will pass this user to Google as `UNSPECIFIED`.
* New users added or updated without specifying either consent attribute will be synced to Google with those consent attributes marked as unspecified.

If you attempt to sync an EEA user without the necessary consent fields and granted status, Google will reject this and not serve ads to this user. In addition, if an ad is served to an EEA user without their explicit consent, you may be liable and could be at financial risk. To avoid this, we suggest sending campaigns with segment filters that only include EEA, UK, and Switzerland users with `true` Google consent attributes. For more details regarding the EU User Consent Policy for Customer Match upload partners, see Google’s [FAQs](https://support.google.com/google-ads/answer/14310715).

### Setting up your Canvas

After you have synced to Braze, the following consent attributes will be available on your user profiles and for segmentation:

- `$google_ad_user_data`
- `$google_ad_personalization`

In any Canvas where you're targeting EEA, UK, and Switzerland end users using a Google Audience Sync to add users to an audience, you need to exclude these users whenever both consent attributes are any value that isn't `true`. This can be achieved by segmenting these users when the consent values are set to `true`. This also ensures that the more accurate analytics of users are synced, since we know Google will reject these users from the audiences. Note that if you're using Google Audience Sync to remove users from an audience, consent attributes are not required.

## Integration

### Step 1: Connect Google account

To get started, go to **Partner Integrations** > **Technology Partners** > **Google Ads** and select **Connect Google Ads**. You'll be prompted with a modal to select the email associated with your Google Ads account and then grant Braze access to your Google Ads account.

After successfully connecting your Google Ads account, you'll be taken back to your Google Ads partner page. You'll then be prompted to select which ad accounts you want to access in the Braze workspace.

![A GIF that shows the workflow of a successful Google Ads account connection to Braze.]({% image_buster /assets/img/google_sync/googlesync.gif %}){: style="max-width:85%;"}

#### Export iOS IDFA or Google Advertising IDs

If you plan to export iOS IDFA or Google Advertising IDs in your audience sync, Google requires your iOS app ID and Android app ID within the requests. Under Google Audience Sync, select **Add Mobile Advertising IDs**, input your iOS app ID and Android app ID (app package name), and save each.

<br><br>
![The updated Google Ads technology page showing the Ad accounts connected, allowing you to re-sync accounts and add mobile advertising IDs.]({% image_buster /assets/img/google_sync/google_sync5.png %}){: style="max-width:75%;"}
<br><br>

If you have multiple apps in a single workspace, you can input any of your app IDs in the setup because mobile ad IDs for your users will be the same across multiple apps. This is because both the Android GAID and iOS IDFA are universal ad identifiers on the device and are not app-specific. To sync mobile ad IDs for users from a specific app, you can use segment filters ("Last Used Specific App" or Most Recent App Version") to target these users.

### Step 2: Add a Google Audience step in Canvas

Add a component in your Canvas, then select **Audience Sync**.

![The menu to select a Canvas component in the editor.]({% image_buster /assets/img/audience_sync/audience_sync3.png %}){: style="max-width:35%;"} ![The Audience Sync step added to the user journey.]({% image_buster /assets/img/audience_sync/audience_sync5.png %}){: style="max-width:28%;"}

### Step 3: Sync setup

1. Select **Custom Audience** to open the component editor.
2. Select **Google** as the Audience Sync partner.

![The Audience Sync step settings with the option to select a partner to start the sync.]({% image_buster /assets/img/audience_sync/audience_sync4.png %}){: style="max-width:80%;"}

{: start="3"}
3. Select the desired Google ad account. 
4. In the **Choose a New or Existing Audience** dropdown, enter the name of a new or existing audience. 

{% tabs %}
{% tab Create a New Audience %}

1. Enter a name for the new custom audience.
2. Select **Add Users to Audience**.
3. Select the first-party user field data to send to your audience. You can choose either:

- **Customer Contact Info**: Contains your users' email or phone numbers, or both, if they exist in Braze. Google requires this to be a single field to sync instead of separate identifiers. You can still use this single field if you only have one of the identifiers.
- **Mobile Advertiser ID**: Select either iOS IDFA or Android GAID. Due to Google’s Customer Match requirements, you can't have both mobile advertiser IDs in the same customer lists.

{: start="4"}
4. Next, save your audience by selecting the **Create Audience** button at the bottom of the step editor.

![Expanded view of the Custom Audience Canvas component. Here, the desired Ad account is selected, a new audience is created, and the "customer contact info" checkbox is selected.]({% image_buster /assets/img/audience_sync/g_sync.png %})

Users will be notified at the top of the step editor if the audience is created successfully or if errors arise during this process. Users can reference this audience for user removal later in the Canvas journey because the audience was created in draft mode. 

![An alert that appears after a new audience is created in the Canvas component.]({% image_buster /assets/img/audience_sync/g_sync3.png %})

When you launch a Canvas with a new audience, Braze will create a new custom audience upon launching the Canvas and subsequently sync users in near real-time as they enter the Google Audience step. 

{% alert important %}
Given Google's Customer Match requirements, you cannot have customer contact information and mobile advertiser IDs in the same customer lists. Google Customer Match will then use this information to determine who is targetable within Google Search, Google Display, YouTube, and Gmail. For more details around Google Customer Match requirements, review their [documentation](https://support.google.com/google-ads/answer/7474166?hl=en&ref_topic=6296507).
{% endalert %}
{% endtab %}
{% tab Sync with an Existing Audience %}

Braze also offers the ability to add or remove users from existing Google customer lists to ensure that these audiences are up-to-date. To sync with an existing audience:

1. Select an existing custom audience to sync.
2. Choose whether you want to **Add to the audience** or **Remove from the audience**.
3. Braze will add or remove users in near real-time as they enter the Google Audience step. 
4. After configuring your Google Audience step, select **Done**. Your Google Audience step will include details about the new audience.

![Expanded view of the Custom Audience Canvas component. Here, the desired Ad account and existing audience are selected, as well as the "Add user to Audience" radio button.]({% image_buster /assets/img/audience_sync/g_sync2.png %})

{% endtab %}
{% endtabs %}

### Step 4: Launch Canvas

Complete the remainder of your user journey within Canvas and then launch! If you have opted to create a new audience, Braze will create the audience within Google and then add users as they reach this step in your Canvas. If you have selected to add or remove users from an existing audience, Braze will either add or remove users when they reach this step in their user journey.

Users will then advance to the next component of the Canvas if there is one or exit the Canvas if it is the last step of the user journey. 

## User syncing and rate limit considerations

As users reach the Audience Sync component, Braze will sync these users in near real-time while respecting Google Ads API rate limits. What this means in practice is that Braze will try to batch and process as many users every 5 seconds before sending these users to Google. 

Once a customer is close to reaching the Google Ads API rate limit, Google will provide feedback to Braze around retry recommendations. If a Braze customer reaches their rate limit, Braze the Canvas will retry the sync for up to &#126;13 hours. If the sync is not possible, these users are listed under the Users Errored metric.

## Understanding analytics 

The following table includes metrics and descriptions to help you better understand analytics from your Audience Sync step.

| Metric | Description |
| ------ | ----------- |
| *Entered* | Number of users who entered this step to be synced to Google. |
| *Proceeded to Next Step* | How many users advanced to the next component, if there is one. All users will auto-advance. If this is the last step in the Canvas branch, this metric will be 0. |
| *Users Synced* | Number of users who have successfully been synced to Google. |
| *User Not Synced* | Number of users that have not been synced due to missing fields to match or the consent attribute was set to `false`. |
| *Users Errored* | Number of users who were not synced to Google due to an error, after &#126;13 hours of retries. For specific errors, like Google Ads API service disruptions, Canvas will retry the sync for up to &#126;13 hours. If the sync is still not possible at that point, the *User Not Synced* will be populated. |
| *Users Pending* | Number of users currently being processed by Braze to sync to Google. |
| *Exited Canvas* | Number of users who have exited the Canvas. This occurs when the last step in a Canvas is a Google step. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Frequently asked questions

### Why can I not select multiple fields to match in my Google Audience Step configuration?

Google Customer Match has strict requirements around how these audiences are formatted and what customer information is included. Specifically, mobile advertiser IDs need to be uploaded separately from customer contact information (such as email and phone number). For more details, refer to [Google's Customer Match documentation](https://support.google.com/google-ads/answer/7659867?hl=en#undefined).

### How long will it take for my audiences to sync in Google?

It can take anywhere between 6 to 12 hours for an audience to be synced into Google. 

### I've synced an audience, so why is the audience size in Google zero?

For privacy purposes, the user list size will show zero until the list has at least 1,000 members. After that, the size will be rounded to the two most significant digits.

### I've synced an audience into Google, but my ads are not serving.

Check that your audiences contain at least 5,000 users so that ads can start serving.

### How do I resolve the "Mobile App IDs Deleted" error?

If you're syncing audiences to Google, this error will trigger if you have selected to sync mobile identifiers as part of your syncs but deleted your mobile app IDs from the Google partner page. To resolve this issue, make sure you've added the appropriate mobile app IDs for iOS and Android to the Google partner page.



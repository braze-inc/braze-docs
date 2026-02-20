---
nav_title: Linkrunner
article_title: Linkrunner
alias: /partners/linkrunner/
description: "This reference article outlines the partnership between Braze and Linkrunner, a mobile attribution and analytics platform that lets you import attribution data to better understand your user acquisition campaigns."
page_type: partner
search_tag: Partner

---

# Linkrunner

> [Linkrunner](https://linkrunner.io/) is a mobile attribution and analytics platform that helps you track and analyze your user acquisition campaigns.

_This integration is maintained by Linkrunner._

## About the integration

The Braze and Linkrunner integration lets you import attribution data to better understand which campaigns are driving user acquisition and engagement.

## Prerequisites

The following is required before you begin:

| Requirement | Description |
|---|---|
| Linkrunner account | A Linkrunner account is required to take advantage of this partnership. |
| iOS or Android app | This integration supports iOS and Android apps. Depending on your platform, code snippets may be required in your application. |
| Linkrunner SDK | In addition to the required Braze SDK, you must install the [Linkrunner SDK](https://docs.linkrunner.io/introduction). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integration

### Step 1: Map user IDs

If you use the Braze SDK `changeUser` function, pass the same user ID in the `userData` parameter of the Linkrunner SDK `signup` function.

If you don't use `changeUser`, pass the `brazeDeviceId` in the `userData` parameter of the Linkrunner SDK `signup` function. Get the `brazeDeviceId` from the Braze SDK.

{% tabs local %}
{% tab Android (Kotlin) %}
```kotlin
val userData = UserDataRequest(
    id = "123", // Your user ID
    // ...other user fields
    brazeDeviceId = "BRAZE_DEVICE_ID", // Braze device ID from the Braze SDK (Required if you are not using the changeUser function)
)

LinkRunner.getInstance().signup(userData = userData)
```
{% endtab %}

{% tab iOS (Swift) %}
```swift
let userData = UserData(
    id: "123", // Your user ID
    // ...other user fields
    brazeDeviceId: "BRAZE_DEVICE_ID" // Braze Device ID from the Braze SDK (Required if you are not using the changeUser function)
)

try await LinkrunnerSDK.shared.signup(userData: userData)
```
{% endtab %}
{% endtabs %}

### Step 2: Create API key in Braze

In your Braze dashboard, go to **Settings** > **Setup and Testing** > **APIs and Identifiers** > **API Keys**.

1. Select **Create API Key**.
2. Under **User Data**, select the following permissions:
   - `users.track`
   - `users.export.ids`
3. Save the API key.
4. Copy the API key and REST endpoint.

![This image shows the API Keys page in Braze where you can create and manage API keys, including the data import key and REST endpoint needed for the Linkrunner integration.]({% image_buster /assets/img/attribution/linkrunner/1.png %})

### Step 3: Configure Braze in Linkrunner's dashboard

1. In Linkrunner, go to **Integrations** in the left-hand panel.
2. Under **Analytics**, select **Configure** for Braze.
3. Enter the API key and REST endpoint you copied in Step 2.

For more information, see [Linkrunner's documentation](https://docs.linkrunner.io/analytics-integrations/braze).

### Step 4: View user attribution data

Linkrunner sends `lr_campaign` and `lr_ad_network` as custom attributes. View this data in the **Custom Attributes** section of the user profile in the Braze dashboard.

## Facebook and X (formerly Twitter) attribution data

Attribution data for Facebook and X (formerly Twitter) campaigns is not available through our partners. These media sources do not permit their partners to share attribution data with third parties, and, therefore, our partners cannot send that data to Braze.
---
nav_title: Linkrunner
article_title: Linkrunner
alias: /partners/linkrunner/
description: "This reference article outlines the partnership between Braze and Linkrunner, a mobile attribution platform that lets you import attribution data to better understand your user acquisition campaigns."
page_type: partner
search_tag: Partner

---

# Linkrunner

> [Linkrunner](https://linkrunner.io/) is a mobile attribution and analytics platform that helps you track and analyze your user acquisition campaigns.

The Braze and Linkrunner integration lets you import attribution data to better understand which campaigns are driving user acquisition and engagement.

## Prerequisites

| Requirement | Description |
|---|---|
| Linkrunner account | A Linkrunner account is required to take advantage of this partnership. |
| iOS or Android app | This integration supports iOS and Android apps. Depending on your platform, code snippets may be required in your application. |
| Linkrunner SDK | In addition to the required Braze SDK, you must install the [Linkrunner SDK](https://docs.linkrunner.io/introduction). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integration

### Step 1: Map identifier

If you are using the `changeUser` function of the Braze SDK, you need to pass the same user ID in the `userData` parameter of the `signup` function of the Linkrunner SDK.

If you are not using the `changeUser` function, you need to pass the `brazeDeviceId` in the `userData` parameter of the `signup` function of the Linkrunner SDK. You can get the `brazeDeviceId` from the Braze SDK.

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

In your Braze dashboard, navigate to **Settings** > **Setup and Testing** > **APIs and Identifiers** > **API Keys**.

1. Click **Create API Key**.
2. Under permissions, select the following under **User Data**:
   - `users.track`
   - `users.export.ids`
3. Save the API key.
4. Copy the API Key and REST endpoint.

![The Braze API Keys page showing where to create and manage API keys.]({% image_buster /assets/img/attribution/linkrunner/1.png %})

### Step 3: Configure Braze in Linkrunner's dashboard

1. In Linkrunner, navigate to **Integrations** from the left-hand panel.
2. Under **Analytics**, click **Configure** for Braze.
3. Provide the API Key and REST Endpoint you copied earlier.

Additional information on these instructions is available in [Linkrunner's documentation](https://docs.linkrunner.io/analytics-integrations/braze).

### Step 4: Viewing user attribution data

Linkrunner will send `lr_campaign` and `lr_ad_network` as custom attributes. The data will be visible in the **Custom Attributes** section of the user profile in the Braze dashboard.

---
nav_title: Odicci
article_title: Odicci
description: "Step-by-step guide to integrating Odicci with Braze for personalized marketing campaigns"
alias: /partners/odicci/
page_type: partner
search_tag: Partner
---

# Integrating Odicci with Braze

> Learn how to integrate Braze with [Odicci](https://www.odicci.com/), a platform that empowers businesses to acquire, engage and retain customers through loyalty driven omnichannel experiences.

{% alert tip %}
Refer to the [Odicci Help Center](https://help.odicci.com) for additional resources and FAQs.
{% endalert %}

## 사용 사례

You can connect the Odicci platform with Braze for seamless data sharing and campaign management, which includes:

- Automatically sending audience data collected in Odicci experiences to Braze.
- Triggering personalized marketing campaigns based on user interactions.
- Mapping fields between Odicci and Braze to ensure accurate data synchronization.

## 예시

A retailer uses Odicci’s gamified experiences to collect email addresses for a marketing campaign.

1. A customer completes a game in Odicci, providing their email address.
2. Odicci automatically syncs this data to Braze.
3. Braze triggers a personalized "Thank You" email and includes a discount code.

## Prerequisites

시작하기 전에 다음이 필요합니다:

| 전제 조건             | 설명                                                               |
|---------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| An Odicci account            | An Odicci account with access to the **Integrations** section is required to take advantage of this partnership.|
| Braze REST API 키        | A Braze REST API key with the `users.track` and 'campaigns.list' permissions. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integrating Odicci

### 1단계: Enable the Integration in Odicci

1. Log in to your Odicci account.
2. Navigate to the **Settings > Integrations** section.
3. Find the **Braze** integration and click **Connect**.

   ![Connect Braze Integration]({% image_buster /assets/img/odicci/braze_connect.png %})

4. Enter your Braze REST API Key into the provided field.
5. Save the settings to activate the integration at the account level.

### 2단계: Obtain Your Braze REST API Key

1. Log in to your Braze account.
2. Go to **Developer Console > REST API Keys**.
3. Create a new API Key or copy an existing one with the `users.track` permission.

### 3단계: Activate the Integration at the Experience Level

1. Create or open an **Experience** in Odicci Studio.
2. Navigate to **Studio > Settings > Integrations**.
3. Locate the **Braze** checkbox and tick it to activate the integration for the experience.
4. 변경 사항을 저장합니다.

### 4단계: Map Fields

1. After activating the integration, remain in the **Studio > Settings > Integrations** section.
2. Map the fields from your Odicci experience (e.g., `Email`, `Name`) to their corresponding fields in Braze.
3. Save your configuration.

   ![Field Mapping Configuration]({% image_buster /assets/img/odicci/braze_field_mapping.png %})

### 5단계: Test the Integration

1. Run the experience in Odicci to collect test data.
2. Verify that the data syncs correctly to Braze by checking the Braze dashboard or data logs.
3. Ensure the mapped fields are correctly populated in Braze.

## 문제 해결

If you experience issues with the integration, consider the following solutions. For further assistance, contact [Odicci Support](https://help.odicci.com).

### API Key Not Valid

Double-check your Braze API Key and ensure it has the necessary permissions. Then, re-enter the API Key in the Odicci integration settings.

### Data Not Syncing

Verify that the fields in the **Field Mapping** section are correctly configured. Then, ensure the API Key has permissions for user data imports.

### Campaign Not Triggering

Check the Braze campaign settings to ensure the correct audience or trigger conditions are set.

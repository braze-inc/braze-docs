---
nav_title: Merkury
article_title: Merkury
description: "This reference article outlines the partnership between Braze and Merkury, an enterprise identity platform for your apps, that allows you to leverages the `MerkuryID` to increase site visitor recognition rates for Braze customers."
page_type: partner
search_tag: Partner

---

# Merkury

> [Merkury](https://merkury.merkleinc.com/) is Merkle’s enterprise identity platform that helps brands maximize consumer engagement, experience, and revenue through first-party cookieless identity capabilities. The `MerkuryID` unifies a brand’s known and unknown customer and prospects records, site/app visits, and consumer data to a single, persistent person ID.

_This integration is maintained by Merkury._

## About the integration

The Braze and Merkury integration allows you to leverages the `MerkuryID` to increase site visitor recognition rates for Braze customers. 브랜드 이메일 가입자인 방문자를 인식하면 Merkury는 가입자의 이메일 주소를 포함하도록 Braze 프로필을 업데이트합니다. The increased recognition capabilities of `MerkuryID` improves engagement and personalization opportunities and immediately increases site abandonment email send quantities and associated revenue. 

## Prerequisites

| Requirement | Description |
| --- | --- |
| Merkle account | A Merkle account is required to take advantage of this partnership. |
| Merkle Client ID | Obtain your Client ID from your Merkle representative. |
| Merkury tag | Place Merkle's Merkury tag on your website. |
| Braze REST and SDK endpoint | Your REST or SDK endpoint URL. Your endpoint will depend on the [Braze URL for your instance]({{site.baseurl}}/api/basics/#endpoints). |
| Braze REST API key | A Braze REST API key with `users.track, users.export.ids, users.export.segment, and segments.list` permissions. <br><br>This can be created within **Braze Dashboard > Developer Console > REST API Key > Create New API Key**. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% alert important %}
The Merkury identity connector requests to Braze operate within Braze API rate limit specifications. Contact Braze or your Merkle account manager if you have any questions.<br><br>자격을 갖춘 세션이 끝날 때 Merkury는 최소 한 번의 요청을 보냅니다.
{% endalert %}

## Side-by-side SDK integration

Uses Merkle's client-side Merkury tag to capture Braze devices and forwards them to the Merkury identity connector endpoint for identification.

### Step 1: Setup Braze web SDK tag

You must have the [Braze Web SDK]({{site.baseurl}}/developer_guide/platform_integration_guides/web/initial_sdk_setup/#install-gtm) deployed on your website to use this integration.

### Step 2: Deploy Merkle's Merkury tag

웹사이트에 머큐리 태그를 배포하여 웹사이트에서 머큐리 ID 커넥터를 사용할 수 있도록 합니다. Merkle 계정 매니저가 자세한 지침이 담긴 가이드를 제공해 드릴 것입니다.

### 3단계: Create custom attributes

Merkury 아이덴티티 커넥터는 다음 필드를 채우며, 이 필드는 Braze에서 [커스텀 속성으로]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes#custom-attributes) 만들어야 합니다.

| Attribute name | Data type | Description |
| --- | --- | --- |
| `hmid` | String | Merkle's Merkury ID |
| `confidence_score` | Number | How confident Merkury was able to identify (1-8, lower is better) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### Step 4: Provide Merkle with user email universe

Merkle recommends a segmentation export of your permissible email universe. This can be followed up with daily exports of active permissible users.

The following fields are required:

- `braze_id`
- `external_id`
- email address

See your Braze representative for further information.


---
nav_title: Antavo
article_title: Antavo Loyalty Cloud
description: "This reference article outlines the partnership between Braze and Antavo, a next-gen loyalty program that goes beyond rewarding purchases."
alias: /partners/antavo/
page_type: partner
search_tag: Partner
---

# Antavo Loyalty Cloud

> [Antavo](https://antavo.com/) is an enterprise-grade SaaS loyalty technology provider that builds comprehensive loyalty programs to foster brand love and change customer behavior.

_This integration is maintained by Antavo._

## About the integration

The Antavo and Braze integration allows you to use loyalty program-related data to build personalized campaigns to enhance the customer experience. Antavo supports loyalty data synchronization between the two platforms—this is a one-way data synchronization only, from Antavo to Braze. The integration supports the `external_id` Braze field, which Antavo uses to synchronize the loyalty member ID.

## Prerequisites

| Requirement          | Description                                                                                                                                                                   |
| -------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------  |
| Antavo account       | An [Antavo](https://antavo.com/) account with the Braze integration enabled is required to take advantage of this partnership.                                                |
| Braze REST API key   | A Braze REST API key with the following permissions: `users.track`, `events.list`, `events.data_series`, and `events.get`.<br><br>This can be created in the Braze dashboard from **Settings** > **API Keys**.  |
| Braze REST endpoint  | [Your REST endpoint URL]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). Your endpoint will depend on the Braze URL for your instance.                |
| Braze app identifier | Your app identifier key. <br><br>To locate this key in the Braze dashboard, go to **Settings** > **API Keys** and find the **Identification** section. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integration

### Step 1: Connect Braze in Antavo

In Antavo, go to **Modules** > **Braze** and click **Configure**. When first navigating to the Braze integration configuration page in Antavo, the interface will prompt you to connect the two systems.

Provide the following credentials:

- **Instance URL:** The Braze REST endpoint of the instance you are provisioned to.
- **API Token (Identifier):** The Braze REST API key that Antavo should use when sending requests to Braze.
- **App Identifier:** The Braze app identifier.

자격 증명을 입력한 후 **연결**을 클릭합니다.

![인스턴스 URL, API 토큰 및 앱 식별자를 사용하여 Antavo에서 Braze 화면을 연결합니다.]({% image_buster /assets/img/antavo/connect_braze.png %})

### 2단계: Configure field mapping

After the connection is established, you’ll be redirected to the **Sync Fields** page automatically in Antavo to configure the field synchronization between the two systems.   You can reach this page at any time through **Modules** > **Braze**.

To configure field mapping in Antavo:

1. Click **Add new field** <i class="fas fa-plus" alt=""></i>.
2. Use the dropdown field to select the Antavo **Loyalty field** that you want to synchronize to Braze.
3. Enter the **Remote field** that represents the equivalent custom attribute in Braze to which the data will be populated.  

{% alert note %}
You can find your list of custom attributes in Braze under **Data Settings** > **Custom Attributes**. If the field you enter is not defined in Braze, a new field will automatically be generated with the first sync.
{% endalert %}

{:start="4"}
4\. 필드 페어링을 추가하려면 1~3단계를 반복합니다.
5\. To remove a field from the list of synchronized data, click <i class="fa-solid fa-rectangle-xmark" title="Delete"></i> at the end of the row.
6\. Click **Save**.

Antavo에서 구성된 필드의 값이 변경되면 해당 단일 값의 동기화가 트리거될 뿐만 아니라 필드 매핑에 추가된 모든 필드가 요청에 포함됩니다.

![Antavo의 필드 동기화 페이지.]({% image_buster /assets/img/antavo/data_field_mapping.png %})

{% alert important %}
데이터 포인트 사용량을 최소화하려면 Braze 내에서 작업할 필드만 매핑하는 것이 좋습니다.
{% endalert %}

#### Supported data types

이 통합은 숫자(정수, 플로트), 문자열, 배열, 부울, 오브젝트, 오브젝트 배열, 날짜 등 모든 Braze 커스텀 속성 [데이터 유형]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#custom-attribute-storage)을 지원합니다.

![다양한 커스텀 속성을 보여주는 Braze 프로필.]({% image_buster /assets/img/antavo/braze_profile.png %})

데이터 필드는 구성된 필드 매핑에 따라 채워집니다.

## Triggers

In addition to configuring field mapping, the integration provides further capabilities through features built into Antavo’s [Workflows](https://antavo.atlassian.net/wiki/spaces/AUM/pages/581402629) tool. All Braze custom attribute [data types]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#custom-attribute-storage) and custom event property [data types]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events#expected-format) can be synchronized through workflows as well.

### Synchronizing loyalty data occasionally

Use this option if the data is not stored in loyalty fields in Antavo or if the data is not added to the list of mapped fields. The synchronization of requested data is triggered when the configured workflow criteria are met.

Visit the step-by-step guide to learn how to configure the synchronization of [loyalty data related to the last purchase](https://antavo.atlassian.net/wiki/spaces/AUM/pages/812056598/Braze#Use-case----Sync-data-related-to-the-customer%E2%80%99s-last-purchase).

### Synchronizing loyalty program events

Use events synchronized from Antavo to enter loyalty members in action-based Braze Canvases. The integration can synchronize any Antavo event (including purchase events) that appears in Braze as custom events.

Visit the step-by-step guide to learn how to configure the synchronization of the [loyalty program enrollment event](https://antavo.atlassian.net/wiki/spaces/AUM/pages/812056598/Braze#Use-case----Welcome-to-the-loyalty-program!) and the synchronization of the [loyalty program benefit earning event](https://antavo.atlassian.net/wiki/spaces/AUM/pages/812056598/Braze#Use-case----Welcome-to-the-loyalty-program!).



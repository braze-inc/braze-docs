---
nav_title: 재적격성
article_title: 재적격성
page_order: 8
page_type: reference
description: "이 참조 문서에서는 캠페인 및 캔버스에 대한 재자격에 대해 정의합니다."
tool:
    - Campaigns
    - Canvas
toc_headers: h2
---

# 캠페인 및 캔버스 재자격 부여

> 반복 또는 트리거 캠페인 또는 캔버스를 예약할 때 사용자가 해당 캠페인에 다시 참여할 수 있도록 허용하는 옵션이 있습니다. 재자격은 사용자가 트리거에 따라 캠페인이나 캔버스에 여러 번 참가할 수 있음을 의미합니다.

## How it works

재인증은 별도로 설정해야 하므로 사용자가 여러 번 재인증하더라도 기본적으로 Braze는 사용자에게 한 번만 메시지를 보냅니다. 이 기능을 켜면 자격을 갖춘 회원은 캠페인 또는 캔버스의 첫 번째 인스턴스를 받은 후 다시 메시지를 받을 수 있습니다. 사용자가 궁극적으로 다시 자격을 얻을 수 있는 시점을 명시할 수 있습니다.

## 다시 자격 설정하기

{% tabs local %}
{% tab 캠페인 %}
캠페인에 대한 재수신 자격을 설정하려면 **전달 관리** 섹션에서 **사용자가 캠페인 수신 자격을 다시 얻도록 허용** 확인란을 선택합니다. 캠페인에 대한 자격을 다시 얻을 수 있는 최대 기간은 720일입니다.

재자격이 설정된 트리거 캠페인의 경우, 트리거 이벤트를 완료했음에도 불구하고 [실제로 캠페인 메시지를 받지 못한]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/#why-did-a-user-not-receive-my-triggered-campaign) 사용자는 다음에 트리거 이벤트를 완료할 때 자동으로 메시지를 받을 자격을 얻게 됩니다. 이는 캠페인 참여가 아닌 메시지 수신을 기준으로 재자격이 부여되기 때문입니다. 사용자가 트리거된 캠페인에 다시 참여할 수 있도록 하면 단순히 메시지를 트리거하는 것이 아니라 실제로 메시지를 두 번 이상 수신할 수 있게 됩니다.

또한 0분의 재자격으로 즉시 메시지를 보내려는 경우, 사용자가 이전 버전의 캠페인이나 캔버스를 어떻게 수신했는지에 관계없이 항상 바로 예약을 시도합니다.

#### API로 트리거된 캠페인의 재적격성

사용자가 API로 트리거된 캠페인을 받는 횟수는 재적격성 설정을 사용하여 제한할 수 있습니다. 이것은 사용자가 API 트리거가 몇 번 실행되든 상관없이 캠페인을 한 번만 또는 주어진 기간 내에 한 번만 받게 됨을 의미합니다.

예를 들어 API 트리거 캠페인을 사용하여 사용자가 최근에 본 항목에 대한 캠페인을 보낸다고 가정해 보겠습니다. 이 경우, 캠페인이 하루에 최대 한 개의 메시지를 보내도록 제한할 수 있으며, 각 항목에 대해 API 트리거를 실행하는 동안 그들이 본 항목의 수에 관계없이 메시지를 보낼 수 있습니다. 반면, API로 트리거된 캠페인이 트랜잭션인 경우, 지연 시간을 0분으로 설정하여 사용자가 트랜잭션을 할 때마다 캠페인을 받을 수 있도록 해야 합니다.
{% endtab %}

{% tab 캔버스 %}
캔버스에 대한 재참가 자격을 설정하려면 **항목 제어** 섹션에서 **사용자가 이 캔버스에 다시 입장할 수 있도록 허용을** 선택합니다. 사용자가 캔버스의 최대 기간 이후 또는 지정된 기간 이후에 다시 입장할 수 있도록 허용할지 여부를 선택할 수 있습니다.

캔버스 배리언트에 대한 재자격은 메시지 수신이 아닌 캔버스 항목에 연결됩니다. 캔버스에 입장한 후 메시지를 받지 못한 사용자는 재참가 자격을 설정하지 않는 한 캔버스에 다시 입장할 수 없습니다.

### 예시

예를 들어 이메일 주소가 없는 사용자가 사용자 여정의 한 단계가 포함된 매일 반복되는 캔버스에 들어간다고 가정해 보겠습니다. 이 단계에는 이메일 메시지만 포함되어 있으므로 사용자는 참여를 얻지 못합니다. 이 사용자는 캔버스의 재인증이 켜져 있지 않으면 캔버스에 다시 입장할 수 없습니다. 

재참가 자격이 없는 활성 반복 또는 트리거된 캔버스가 있고 사용자가 메시지를 받을 때까지 캔버스에 재참가하도록 하려면 캔버스에서 메시지를 받은 고객을 제외하는 필터를 입력 기준에 추가하여 사용자가 재참가할 수 있도록 허용하는 것이 좋습니다.

캔버스의 재사용 자격이 캔버스 기간보다 짧게 설정되어 있으면 사용자가 캔버스에 두 번 이상 입장할 수 있으며, 이는 특히 지연 시간이 긴 인앱 메시지를 사용하는 캔버스의 경우 오해의 소지가 있는 동작으로 이어질 수 있습니다. 동일한 세션 시작 시 여러 개의 캔버스 인앱 메시지가 트리거될 수 있으므로 특정 구성요소가 다른 구성요소보다 빠르게 렌더링되는 경우 사용자는 동일한 메시지를 반복해서 수신하는 경험을 할 수 있습니다.
{% endtab %}
{% endtabs %}

## 자격 재취득 지연 계산

캠페인과 캔버스 모두에 대한 재자격은 달력 일수가 아닌 초 단위로 계산됩니다. 즉, 하루는 사용자가 메시지를 받은 시점부터 24시간(또는 86,400초)이 아니라 다음 날 자정까지로 계산됩니다. 마찬가지로 한 달은 정확히 2,592,000초로 계산되며, 이는 약 30일에 해당합니다.

### 예시

다음 시나리오를 생각해 보세요:

* 캠페인은 매월 15일에 발송되도록 설정되어 있으며, 재신청 자격은 30일로 설정되어 있습니다.
* 2월 15일부터 3월 15일까지는 30일이 채 되지 않습니다. 

즉, 2월 15일에 캠페인을 받은 사용자는 3월 15일에 발송되는 캠페인에 참여할 수 없습니다. 캠페인이 매일 오전 8시에 발송되도록 설정되어 있고 재적격 기간이 1일인 경우 메시지 발송에 지연 시간이 있는 경우, 오전 8시 30분에 캠페인을 받은 사용자는 다음 날 오전 8시에는 아직 재적격이 되지 않습니다.

## 다변량 테스트

다변량 테스트의 경우, Braze는 다음 규칙을 사용하여 모든 캠페인, 트리거된 인앱 메시지 및 캔버스에 대한 변형 재적격성을 결정합니다:

- 배리언트 비율을 변경하지 않으면 각 사용자는 재자격이 부여될 때마다 항상 동일한 캠페인 배리언트, 트리거된 인앱 메시지 또는 캔버스 항목을 입력하게 됩니다.
- 이형 상품 비율이 변경되면 사용자는 다른 이형 상품으로 재분배될 수 있습니다.
- 배리언트 비율이 변경되지 않으면 대조군은 일관성을 유지하며, 이전에 메시지를 받은 사용자는 나중에 메시지를 보낼 때 대조군에 들어가지 않으며 대조군에 속한 사용자도 메시지를 받지 않습니다.


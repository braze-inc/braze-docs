---
nav_title: Punchh
article_title: Punchh
page_order: 1
description: "이 참조 문서에서는 로열티 및 인게이지먼트 플랫폼인 Punchh와 Braze 간의 파트너십을 간략히 설명합니다. 이를 통해 두 플랫폼 사이에서 데이터를 동기화할 수 있습니다. Braze에 게시된 데이터는 세분화에 사용할 수 있으며, Braze에서 설정한 웹훅 템플릿을 통해 사용자 데이터를 Punchh로 다시 동기화할 수 있습니다."
page_type: partner
search_tag: Partner

---

# Punchh

> [Punchh](https://punchh.com/)는 업계 최고의 로열티 및 참여 플랫폼으로, 브랜드가 매장 내 및 디지털 방식으로 옴니채널 고객 로열티 프로그램을 제공할 수 있도록 합니다. 

_This integration is maintained by Punchh._

## 통합 정보

Braze와 Punchh 통합을 통해 두 플랫폼 간에 선물 및 로열티 목적으로 데이터를 동기화할 수 있습니다. Braze에 게시된 데이터는 세분화에 사용할 수 있으며 Braze 웹훅을 통해 사용자 데이터를 Punchh로 다시 동기화할 수 있습니다.

## 어떤 이점이 있나요?

- 실시간으로 Punchh에서 Braze로 로열티 데이터를 수집합니다. 
- Braze의 강력한 오디언스 데이터를 활용하고 계층화하여 의미 있고 동적인 크로스채널 경험(앱, 모바일, 웹, 이메일 및 SMS)을 전달합니다.
  - 고객이 이메일을 열었습니까? 고객이 매장 근처에서 앱을 열었나요?
- Braze를 통해 전송되는 트랜잭션 이메일의 모양과 느낌을 표준화합니다.
- 진행하면서 A/B 테스트 및 최적화를 진행할 수 있는 여정을 생성합니다.

## 전제 조건

| 요구 사항 | 설명 |
|---|---|
| Punchh 계정 | 이 파트너십을 활용하려면 활성화된 Punchh 계정이 필요합니다. |
| Braze REST API 키 | `users.track` 권한이 있는 Braze REST API 키. <br><br> 이는 **설정** > **API 키**에서 Braze 대시보드에서 생성할 수 있습니다. |
| Braze REST 엔드포인트 | [당신의 REST 엔드포인트 URL][6].] 사용자의 엔드포인트는 인스턴스를 위한 Braze URL에 따라 달라집니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 기타 고려사항

#### 통합하기 전에

- Braze 통합을 활용할 때 Punchh와 Braze에서 각각 하나씩 두 개의 캠페인이 필요합니다. 예를 들어, 캠페인에 오퍼를 첨부하여 전송하는 경우, 기프트 캠페인은 Punchh 내에서 구성되며, Braze에서 알림을 전송할 수 있습니다.
- 게스트는 이미 Punchh 및 Braze에 존재해야 합니다. Punchh는 이미 로열티 고객이 아닌 고객을 필터링합니다.

#### 중요한 참고 사항

- Punchh는 고객이 데이터 포인트 초과량을 방지하기 위해 Braze로의 기본 사용자 속성 전송을 비활성화할 수 있는 기능을 추가했습니다. 이것은 어댑터 설정 중에 구성됩니다.
- 반복 캠페인에서 커스텀 세그먼트를 사용하는 경우, 캠페인이 실행될 때마다 ID가 변경되므로 캠페인 ID 대신 캠페인 이름을 사용해야 합니다.
- 각 Punchh 기프트 캠페인 내에서 사용할 수 있는 커뮤니케이션 채널에는 리치 메시지, 푸시 알림, SMS 및 이메일이 포함됩니다.
- 사용자가 Braze에서 Punchh 커스텀 세그먼트로 전송된 후에는 제거할 수 없습니다. 새로운 게스트만 기존 커스텀 세그먼트에 추가할 수 있습니다. 기존 Punchh 커스텀 세그먼트에서 게스트를 제거해야 하는 경우, 사용자를 새 Punchh 커스텀 세그먼트로 보내기 위해 Braze에서 새로운 웹훅 캠페인을 생성해야 합니다.

## 통합

Punchh는 Braze 고객이 다음 Punchh API 엔드포인트를 사용하여 Punchh 플랫폼에 외부 ID를 추가할 수 있도록 여러 엔드포인트를 제공합니다. 외부 ID가 추가된 후 Punchh에서 어댑터를 생성하고 Braze 자격 증명을 제공한 다음, 동기화할 이벤트를 선택합니다. 다음으로, Punchh 세그먼트 ID를 사용하여 Punchh 웹훅을 빌드해 캔버스 여정에서 고객 동기화를 트리거할 수 있습니다.

Note that the Punchh `user_id` and Braze `external_id` need to be available in either platform for the integration to sync properly. 
- Events sent from Punchh to Braze will include the Braze `external_id` as the identifier. If Punchh is configured to use the `external_source_id`, that value will be set as the Braze `external_id`. Otherwise, the integration will default to setting the Punchh `user_id` as the Braze `external_id`.
- To send webhooks from Braze to Punchh, the Punchh `user_id` must be available on the Braze user profile. If Punchh `user_id` is not used as the Braze `external_id`, it should be set as a custom attribute "punchh_user_id". 

### 1단계: Set up external ID ingestion endpoints (optional)

Braze의 외부 ID는 신규 및 기존 Punchh 사용자에 대해 다음 엔드포인트를 사용하여 추가할 수 있습니다.

{% alert important %}
`external_source` 및 `external_source_id` 필드 값은 Punchh에서 고유해야 하며 기존 프로필에 연결되어 있지 않아야 합니다.
{% endalert %}

1. 새로운 Punchh 사용자<br>
`external_source` 및 `external_source_id` 필드를 사용하여 Punchh 가입 엔드포인트로 Punchh에 새 사용자를 생성합니다. Punchh는 다음 가입 엔드포인트 중 하나를 통해 고객 프로필과 함께 외부 식별자를 보낼 수 있도록 합니다:
- [모바일 가입 API](https://developers.punchh.com/docs/dev-portal-mobile/2e67abf6f8e12-sign-up-register)
- [SSO 가입 API](https://developers.punchh.com/docs/dev-portal-online-ordering/58f18dfdd2a3d-signup-with-email-and-password)<br><br>
2. 기존 Punchh 사용자 <br>
기존 Punchh 사용자에 대한 `external_source_id`를 업데이트합니다. Punchh는 사용자 API 업데이트 엔드포인트를 통해 프로필에 외부 식별자를 추가할 수 있습니다: 
- [모바일 사용자 업데이트](https://developers.punchh.com/docs/dev-portal-mobile/c9b928e35a6f3-update-user-profile)
- [SSO 사용자 업데이트](https://developers.punchh.com/docs/dev-portal-online-ordering/eef4eef6c97a0-update-user-information)
- [대시보드 사용자 업데이트](https://developers.punchh.com/docs/dev-portal-platform-functions/6351feaf591aa-update-a-user)
<br><br>
{% tabs 로컬 %}
{% tab 사용자 가입 API 예제 %}
이 예제에서는 가입 시 고객 프로필과 함께 외부 식별자를 보낼 수 있습니다. `external_source`를 '고객_id'로, `external_source_id`를 '111111111111111111'의 문자열 데이터 유형으로 전송하면 됩니다.

```json
curl --location --request POST 'https://server_name_goes_here.punchh.com/api2/mobile/users' \
--header 'Content-Type: application/json' \
--header 'x-pch-digest: SIGNATURE' \
--header 'Accept-Timezone: Etc/UTC' \
--header 'Accept: application/json' \
--header 'Accept-Language: en' \
--data-raw '{
    "client":"CLIENT",
    "user" : {
      "email": "test@example.com",
      "password": "PASSWORD",
      "first_name":"FIRST_NAME",
      "last_name":"LAST_NAME",
      "terms_and_conditions":"true",
      "anniversary":"2014-02-02",
      "zip_code":"94497",
      "birthday":"2004-02-02",
      "external_source":"customer_id",
      "external_source_id":"111111111111111111"
      }
}'
```
{% endtab %}
{% tab 사용자 업데이트 API 예제 %}
이 예제에서는 고객 프로필로 외부 식별자를 업데이트할 수 있습니다. `external_source`를 '고객_id'로, `external_source_id`를 '111111111111111111'의 문자열 데이터 유형으로 전송하면 됩니다.

```json
curl --location --request PUT 'https://server_name_goes_here.punchh.com/api2/mobile/users' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'Accept-Language: en' \
--header 'x-pch-digest: SIGNATURE' \
--header 'Authorization: Bearer ACCESS_TOKEN' \
--data-raw '{
    "client":"CLIENT",
    "user": {
        "external_source":"customer_id",
        "external_source_id":"111111111111111111"
    }
}'
```
{% endtab %}
{% endtabs %}

{% alert note %}
**플랫폼 구성:** Punchh에서 외부 식별자를 활성화하려면 Punchh 대시보드에서 **Cockpit** > **대시보드** > **External User Identifier**로 이동합니다.
{% endalert %}

### 2단계: Braze 어댑터 설정 in Punchh

#### 동기화할 수 있는 이벤트 {#available-events-to-sync}

1. **손님:** 가입, 게스트 프로필 업데이트, 비활성화 또는 삭제 시 트리거됨
2. **로열티 체크인:** 영수증에서 바코드를 스캔하여 로열티 거래 또는 적립이 발생한 경우
3. **기프트 체크인:** 캠페인에서 포인트가 기프트로 제공될 때 트리거됨
4. **사용:** Punchh 쿠폰을 제외하고 리워드 사용 시 트리거됨(해당 쿠폰은 발급 및 사용과 같은 쿠폰 이벤트로 별도로 발송됨)
5. **리워드:** 캠페인, 활동, 포인트에서 리워드로 전환 또는 관리자 기프트에서 기프트로 제공된 리워드로 트리거됨
6. **트랜잭션 알림:** 펀치 시스템 내에서 사용자의 거래 활동(예: 포인트 만료)에 따라 트리거됨
7. **마케팅 Notifications:** 연관된 사용자 세그먼트에 대해 Punchh에서 다양한 캠페인 설정을 기반으로 트리거됨

{% alert note %}
이러한 사용 가능한 이벤트에 대한 샘플 페이로드의 형태는 Punchh 설명서를 참조하세요.
{% endalert %}

귀하의 Punchh 구현 매니저와 협력하여 이 어댑터를 설정하십시오.

Braze와 Punchh 통합을 설정하려면 다음을 수행하십시오:

1. Punchh 대시보드에서 **Cockpit** > **대시보드** > **주요 기능** > **웹훅 관리 활성화**로 이동하여 **웹훅 관리 활성화**를 토글합니다.<br><br>
2. 다음으로, 어댑터를 활성화하려면 **설정** > **웹훅 매니저** > **구성** > **어댑터 탭 표시**로 이동하여 **어댑터 탭 표시**를 토글하십시오.<br><br>
3. **웹훅 매니저**에서 **설정** 탭으로 이동하고, **어댑터** 탭을 선택한 다음, **어댑터 생성**을 클릭합니다. <br><br>![][1]<br><br>
4. 어댑터 이름, 설명 및 관리자 이메일을 입력하세요. **Braze**를 어댑터로 선택하고 Braze REST API 엔드포인트와 Braze API 키를 제공하세요.<br><br>
5. 다음으로, 활성화하려는 사용 가능한 이벤트를 선택하십시오. 이러한 이벤트 목록은 [동기화할 수 있는 이벤트](#available-events-to-sync)에서 찾을 수 있습니다.<br><br>![][3]<br><br>
6. **제출**을 클릭하여 웹훅을 활성화합니다.

## Braze에서 Punchh 웹훅 만들기

Braze는 Punchh 커스텀 세그먼트를 활용하여 웹훅을 통해 사용자를 Punchh 세그먼트에 추가할 수 있습니다.

1. Punchh에서 커스텀 세그먼트를 만들고 아래에 표시된 대로 Punchh 세그먼트 대시보드 URL에 있는 `custom_segment_id`을(를) 기록하십시오. 클래식 또는 베타 세그먼트 빌더를 사용할 수 있습니다. 그러나 클래식은 결국 지원 중단될 예정이므로 베타가 권장됩니다.<br><br>Punchh 플랫폼에서 **Guest** > **세그먼트** > **커스텀 목록** > **새 커스텀 목록**으로 이동합니다.<br><br>![][8]<br><br>

2. 사용자를 커스텀 세그먼트에 웹훅 URL로 추가하는 경우 Braze에서 Punchh 엔드포인트를 사용하여 웹훅 캠페인을 생성합니다. 이때 URL에서 가져온 `custom_segment_id` 및 `user_id`를 키-값 페어로 제공할 수 있습니다.<br><br>![][4]<br><br>

3. 이 웹훅은 단일 캠페인으로 설정하거나 캔버스 내 단계로 설정할 수 있습니다. 또는 이 특정 Punchh 세그먼트에 사용자를 추가하는 웹훅이 여러 캠페인 또는 캔버스에서 사용될 경우 [템플릿]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/webhook_template#creating-a-webhook-template)으로 설정할 수 있습니다.<br><br>
웹훅 내의 `user_id` 키는 Punchh 사용자 ID에 매핑됩니다. 이 식별자는 사용자를 Punchh 커스텀 세그먼트에 추가하기 위해 Braze에서 생성된 모든 웹훅에 추가되어야 합니다. `punch_user_id` 커스텀 속성은 [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/using_liquid/#pre-formatted-variables)를 사용하여 `user_id` 키의 값으로 동적으로 채워질 수 있습니다. 모든 템플릿 텍스트 필드의 오른쪽 상단에 있는 파란색 '더하기' 아이콘을 사용하여 `punchh_user_id` 커스텀 속성 변수를 삽입할 수 있습니다.<br><br>![][10]{: style="max-width:65%;"}<br><br>![][11]{: style="max-width:65%;"}<br><br>

4. 웹훅이 저장된 후에는 아래와 같이 사용자를 동기화하는 데 사용할 수 있습니다. 예를 들어, 이 Braze 웹훅 캠페인이 시작될 때 136명의 게스트가 Punch 커스텀 세그먼트에 추가됩니다.<br><br>![Braze와 Punchh 통합으로 인해 저장된 웹훅을 사용하여 사용자를 동기화하는 예시입니다.][7]

웹훅이 Braze에서 사용되는 방법에 대한 자세한 내용은 [웹훅 만들기]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/)을 확인하세요. 

## 사용 사례 캠페인

### 캠페인 및 캔버스 구성

#### 트리거링

Punchh 이벤트에 의해 Braze로 전송되는 Braze 메시징의 사용 사례는 보상 이벤트 또는 게스트 이벤트와 같은 [액션 기반 캠페인]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery#action-based-delivery) 또는 관련 Punchh 이벤트에 의해 트리거되는 Canvases로 생성될 수 있습니다.

트리거를 추가하면 Braze에서 생성된 이벤트 목록이 표시됩니다. 이벤트를 기록한 사용자에게 전송할 캠페인 또는 캔버스를 트리거해야 하는 이벤트를 선택하세요.

![][12]

속성 필터를 추가하여 트리거 이벤트를 추가로 필터링할 수 있습니다. 예를 들어, 메시지는 고객이 승인된 이벤트 속성이 `true`인 "checkins_gift" 이벤트를 트리거할 때만 트리거되어야 합니다. 이것은 모든 사용 사례에 적용되지 않을 수 있는 선택적 기능입니다. 

#### 세분화

많은 경우에, Punchh 이벤트에 의해 트리거되는 Braze 캠페인과 캔버스는 이러한 이벤트를 트리거하는 사용자의 세분화가 Punchh 내에서 결정되기 때문에 '모든 사용자' 오디언스로 설정될 수 있습니다. 그러나 이벤트에 의해 트리거된 Braze 메시징을 받을 사용자 오디언스를 더욱 세분화하려는 고객은 캠페인 작성기의 **타겟 오디언스** 섹션 또는 캔버스 작성기의 **엔트리 오디언스**에 추가 필터와 세그먼트를 추가하여 이를 수행할 수 있습니다. 

### 사용 사례

{% tabs 로컬 %}
{% tab 가입 %}
#### 가입 캠페인

오퍼가 첨부된 가입 캠페인에 대한 Braze 구성을 활용할 때, Punchh 내에서 가입 기프트 캠페인을 구성하고 Braze에서 환영 메시지를 구성해야 합니다. 

Punchh는 가입 캠페인에 실행 지연을 추가할 것을 권장합니다. 그러면 Braze에서 먼저 게스트 이벤트를 기반으로 환영 메시지를 트리거할 수 있습니다. 사용자에게 기프트가 전달되었음을 알리는 후속 메시지를 보내려면 리워드 이벤트를 기반으로 트리거할 수 있습니다.

가입 캠페인의 경우, 세그먼트에 대해 모든 가입을 사용할 수 있으므로 커스텀 Braze 세그먼트는 필요하지 않습니다.

Punchh 구성 필요:
- 캠페인: 가입 
- 세그먼트: 모두 등록되었습니다
- 리워드: 고객 선택 사항
필요한 이벤트:
- 리워드 이벤트
- 게스트 이벤트
고려 사항:
- 실행 지연, 손님에게 5-10분 지연을 추가하도록 권장합니다

![사용자 세그먼트는 펀치에서 구성되며, 게스트는 로열티 프로그램에 가입합니다. 이후 게스트 이벤트(트리거된 경우) 및 Braze 메시징 캠페인이 트리거됩니다. 다음으로, Punchh 가입 기프트 캠페인은 10분 후에 트리거되어 리워드 이벤트와 선택적 후속 메시지를 트리거합니다.]({% image_buster /assets/img/punchh/usecase3.png %})

{% endtab %}
{% tab 대량 오퍼 %}
#### 대량 오퍼 캠페인

기프트를 위한 대량 제공 캠페인을 사용할 때, Punchh 내에서 대량 제공 캠페인을 구성하고 Braze에서 메시징 캠페인을 구성해야 합니다.

Punchh 플랫폼에서 게스트에게 기프트를 제공하기 전에 Braze에서 커뮤니케이션을 전송하거나 캠페인에 대한 Braze 세그먼트를 활용하려는 경우 Punchh 기프트 캠페인을 위해 [커스텀 Punchh 세그먼트]({{site.baseurl}}/partners/message_orchestration/channel_extensions/loyalty/punchh/#step-3-create-punchh-webhook-in-braze)가 필요합니다. 

Braze에서 이 오퍼를 받을 사용자 세그먼트를 생성하는 것은 Punchh에서 사용할 수 없는 속성을 사용할 때만 권장됩니다. 그렇지 않으면 Punchh 세분화를 사용할 수 있으며, Braze 메시징 캠페인은 사용자가 보상을 받을 때(보상 이벤트가 Punchh에 의해 트리거됨) 트리거되는 액션 기반 캠페인으로 생성됩니다.

Punchh 구성 필요:
- 캠페인: 대량 오퍼
- 세그먼트: 커스텀 목록 또는 고객 선택
- 리워드: 고객 선택 사항

**세분화 및 선물 제공을 위해 Punchh를 사용하고, 메시징을 위해 Braze를 사용:**<br>
예를 들어, $2 할인 리워드는 Punchh 내에서 구성 가능한 세그먼트에 전송되며 메시징은 Braze를 통해 전송됩니다.<br>
![사용자 세그먼트는 Punchh에서 구성할 수 있으며, 사용자는 Punchh 대량 제공 캠페인을 통해 선물을 받습니다. 다음으로, 리워드 이벤트가 트리거되고 다음으로, Braze 메시징 캠페인이 트리거됩니다.]({% image_buster /assets/img/punchh/usecase6.png %}){: style="max-width:80%;"}

**기프트에 Braze 세분화 및 메시징과 Punchh 사용:**<br>
예를 들어, Punchh에서 사용할 수 없는 속성을 가진 세그먼트에 보낸 $2 할인 리워드와 메시징이 이에 해당합니다.<br>
![사용자 세그먼트는 Braze에서 구성할 수 있습니다. 그런 다음, Braze 대 Braze 세그먼트에서 메시지를 보낼 수 있습니다. 다음으로, 사용자는 세그먼트 및 사용자 ID와 함께 Braze 웹훅을 통해 Punchh 커스텀 세그먼트로 전송됩니다. 이후 사용자는 커스텀 세그먼트를 사용한 Punchh 대량 제공 캠페인을 통해 선물을 받습니다. 이후 보상 이벤트가 트리거됩니다.]({% image_buster /assets/img/punchh/usecase5.png %}){: style="max-width:80%;"}

**기프트나 메시징 또는 둘 다에 Braze 세분화 및 Punchh 사용:**<br>
예를 들어, $2 할인 리워드는 Punchh에서 사용할 수 없는 속성을 가진 세그먼트에 전송되지만, 메시징이 필요하지 않거나 메시징이 Punchh를 통해 전송될 수 있습니다(모든 게스트가 Punchh에 있어야 함).<br>
![사용자 세그먼트는 Braze에서 구성할 수 있으며, 사용자는 Braze 웹훅을 통해 세그먼트 및 사용자 ID와 함께 Punchh 커스텀 세그먼트로 전송됩니다. 이후 사용자는 커스텀 세그먼트를 사용한 Punchh 대량 제공 캠페인을 통해 선물을 받습니다. 이후 보상 이벤트가 트리거됩니다.]({% image_buster /assets/img/punchh/usecase4.png %})

{% endtab %}
{% tab 반복 대량 오퍼 %}
#### 반복 대량 오퍼 캠페인

선물 제공을 위한 반복적인 대량 제공 캠페인을 사용할 때, Punchh 내에서 대량 제공 캠페인을 구성하고 Braze에서 메시징 캠페인을 설정해야 합니다. Punchh 커스텀 세그먼트는 고객이 Braze 세분화를 사용하려는 경우 필요합니다(단, Punchh에서 사용할 수 없는 속성을 사용하는 경우에만 권장됨). 그렇지 않으면 Punchh 세분화를 사용할 수 있으며, 리워드 이벤트를 기반으로 Braze 메시징 캠페인이 트리거됩니다.

Punchh 구성 필요:
- 캠페인: 반복 대량 오퍼
- 세그먼트: 커스텀 목록 또는 고객 선택
- 리워드: 고객 선택 사항
고려 사항:
- 캠페인 ID와 캠페인 이름은 이벤트에서 이벤트 속성정보로 Braze에 전송됩니다. 캠페인을 수신하는 오디언스를 추가로 필터링하기 위해 캠페인 식별자를 Braze에서 사용하려는 경우 캠페인 ID는 매일 변경되므로 캠페인 이름을 사용해야 합니다.

{% endtab %}
{% tab 체크인 후 오퍼 알림 %}
#### 알림을 포함한 체크인 후 오퍼 캠페인

포스트 체크인 오퍼 캠페인을 이용할 때, Braze는 선물에 관한 알림을 보내며, 게스트가 체크인할 때 Punchh 포스트 체크인 캠페인에서 선물을 받게 됩니다. 따라서, 체크인 후 오퍼 캠페인은 Punchh 내에서 구성해야 하며, Braze에서 메시징 캠페인(캠페인에 대해 고객에게 알리는 경우)을 구성해야 합니다.

Punchh 구성 필요:
- 캠페인: 체크인 후 제공
- 세그먼트: 커스텀 목록
- 리워드: 고객 선택 사항

예를 들어, Punchh에서 사용할 수 없는 속성을 가진 세그먼트에 더블 포인트를 위해 이번 주말에 방문하라는 이메일을 손님에게 알리는 것입니다. Punchh는 자격을 갖춘 체크인 후 이 세그먼트에 포인트를 제공하고 Braze에서 선택적으로 메시징을 제공합니다. 

![사용자 세그먼트는 Braze에서 구성되며, 메시지는 체크인 캠페인 후 Braze에서 전송됩니다. 다음으로, 자격을 갖춘 사용자는 세그먼트 및 사용자 ID와 함께 Braze 웹훅을 통해 Punchh 커스텀 세그먼트로 전송됩니다. 마지막으로, 커스텀 세그먼트에서 자격을 갖춘 사용자가 체크인하고 체크인 후 캠페인을 통해 기프트와 선택적 메시지를 수신합니다.]({% image_buster /assets/img/punchh/update7.png %})

{% endtab %}
{% tab 알림 없이 체크인 후 오퍼 %}
#### 알림 없이 체크인 후 오퍼 캠페인

고객에게 먼저 알리지 않는 체크인 후 캠페인을 활용할 때, 캠페인은 기프트(선택적 메시징)를 제공하고 Braze 내에서 모든 알림을 트리거합니다. 따라서 체크인 후 오퍼 캠페인은 Punchh 내에서 구성해야 합니다. 그러나 커스텀 목록은 필요하지 않습니다. 대신 Punchh 내에서 원하는 세그먼트를 선택할 수 있습니다. 

Punchh 구성 필요:
- 캠페인: 체크인 후 제공
- 세그먼트: 고객 선택 사항
- 리워드: 고객 선택 사항

예를 들어, 깜짝 놀라게 하고 기쁘게 하는 Braze 캠페인은 Punchh에서 사용할 수 있는 세그먼트에 발송되어 방문해 주신 고객에게 감사드리며 다음 방문 시 $2 할인을 제공합니다.

![자격을 갖춘 사용자 세그먼트는 Punchh 내에서 구성할 수 있으며, 자격을 갖춘 사용자는 Punchh의 체크인 후 캠페인를 통해 기프트를 받습니다. 이후 리워드 이벤트가 트리거되고 리콜 메시지가 발송되어 Braze에서 보낸 리워드를 게스트에게 알립니다.]({% image_buster /assets/img/punchh/usecase2.png %})

{% endtab %}
{% tab 기념일 %}
#### 기념일 캠페인 

기념일 캠페인을 활용할 때, 사용자는 먼저 Punchh 캠페인에서 기념일 기프트를 받습니다. 이 기프트 증정(리워드 이벤트)은 Braze 내에서 메시징 캠페인을 트리거하여 사용자에게 기프트 증정을 알립니다. 따라서 커스텀 목록은 필요하지 않습니다. 대신 Punchh 내에서 세그먼트 및 기념일 설정을 선택할 수 있습니다.

Punchh 구성 필요:
- 캠페인: 기념일 캠페인
- 세그먼트: 고객 선택 사항
- 리워드: 고객 선택 사항
고려 사항:
- 가입 달 기프트
- 유효 기간(생일 리워드는 얼마나 유효한가요?)
- 반복 캠페인, 일정 필요 

![선택적 세그먼트를 Punchh 내에서 생성할 수 있으며, 자격을 갖춘 사용자는 Punchh 기념일 캠페인을 통해 리워드를 받습니다. 이후 리워드 이벤트가 트리거되고 리콜 메시지가 발송되어 Braze에서 보낸 리워드를 게스트에게 알립니다.]({% image_buster /assets/img/punchh/usecase1.png %})

{% endtab %}
{% tab 리콜 %}
#### 리콜 캠페인

비활동을 기준으로 사용자를 타겟팅할 때 리콜 캠페인을 사용할 수 있습니다. 고객은 Punchh 내에서 세그먼트 및 캠페인을 생성할 수 있지만 메시징에는 Braze를 사용할 수 있습니다.

Braze에서 생성된 세분화를 사용하려면 비활성화를 기반으로 한 [커스텀 Punchh 세그먼트]({{site.baseurl}}/partners/message_orchestration/channel_extensions/loyalty/punchh/#step-3-create-punchh-webhook-in-braze)를 반복적인 대량 제공 캠페인에 첨부할 수 있습니다.

Punchh 구성 필요:
- 캠페인: 리콜 캠페인
- 세그먼트: 고객 선택 사항
- 리워드: 고객 선택 사항
고려 사항:
- 캠페인은 일정에 따라 실행됩니다

![선택적 세그먼트를 Punchh 내에서 생성할 수 있으며, 자격을 갖춘 사용자는 Punchh 리콜 캠페인을 통해 보상을 받습니다. 이후 리워드 이벤트가 트리거되고 리콜 메시지가 발송되어 Braze에서 보낸 리워드를 게스트에게 알립니다.]({% image_buster /assets/img/punchh/usecase.png %})

{% endtab %}
{% endtabs %}


[1]: {% image_buster /assets/img/punchh/punchh1.png %}
[2]: {% image_buster /assets/img/punchh/punchh2.png %}
[3]: {% image_buster /assets/img/punchh/punchh3.png %}
[4]: {% image_buster /assets/img/punchh/punchh4.png %}
[5]: {% image_buster /assets/img/punchh/punchh5.png %}
[7]: {% image_buster /assets/img/punchh/punchh6.png %}
[6]: {{site.baseurl}}/api/basics/#endpoints
[8]: {% image_buster /assets/img/punchh/update1.png %}
[9]: {% image_buster /assets/img/punchh/update2.png %}
[10]: {% image_buster /assets/img/punchh/update3.png %}
[11]: {% image_buster /assets/img/punchh/update4.png %}
[12]: {% image_buster /assets/img/punchh/update5.png %}
[13]: {% image_buster /assets/img/punchh/update6.png %}
[14]: {% image_buster /assets/img/punchh/update7.png %}

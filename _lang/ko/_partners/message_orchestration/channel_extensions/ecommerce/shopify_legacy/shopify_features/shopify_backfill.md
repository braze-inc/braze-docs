---
nav_title: "Shopify 히스토리컬 백필"
article_title: "Shopify 히스토리컬 백필"
alias: "/shopify_historical_backfill_legacy/"
description: "이 참조 문서에서는 위험 및 지원되는 데이터를 포함하여 Shopify의 과거 데이터 백필 설정 방법을 간략히 설명합니다."
page_type: partner
search_tag: Partner
page_order: 1
---

# Shopify 히스토리컬 백필 

> Shopify Historical Backfill 기능을 통해 브랜드는 고객 및 구매 데이터를 자동화되고 원활한 방식으로 동기화할 수 있어 가장 가치 있는 세그먼트 중 하나인 구매자와 즉시 소통을 시작할 수 있습니다. 

백필의 일환으로 Braze가 Shopify 통합 연결 이전 90일 동안의 모든 고객, 주문 및 구매 이벤트를 가져올 수 있도록 합니다. 이 기능은 다음 섹션에서 설명된 함의를 고려하여 실행 중인 활성 메시지가 없는 신규 고객에게 적합합니다. 이 기능은 데이터 포인트 사용량에도 포함됩니다.

## 위험

이 기능은 역사적 데이터와 이벤트를 가져와서 영향을 받는 캠페인이나 캔버스에 대해 사용자들이 관련 없고 시기적절하지 않은 메시지를 받는 등의 의도치 않은 결과를 초래할 수 있습니다. 다음 트리거 이벤트를 사용하는 캠페인 및 캔버스는 이 기능이 동기화하는 모든 Shopify 데이터를 사용하는 경우 영향을 받을 수 있습니다:
- 사용자 지정 속성 값 변경
- 전환 이벤트 수행
- 캠페인에 대한 예외 이벤트 수행
- 구독 상태 업데이트
- 구독 그룹 상태 업데이트
- 이메일 주소 추가
- 구매*
- 커스텀 이벤트 수행*

{% alert important %}
Shopify 과거 백필의 데이터를 사용하여 위 이벤트를 트리거할 수 있는 메시지가 있는지 현재 활성 캠페인과 캔버스를 감사하는 것이 좋습니다. 

- '구매' 및 '커스텀 이벤트 수행'의 경우 [시작 시간 지속 시간]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/#step-4-assign-duration)을 Shopify 스토어가 Braze에 연결된 이후의 모든 날짜 및 시간으로 업데이트할 수 있습니다. 이 새로운 시작 시간 이전의 모든 과거 이벤트는 메시지를 트리거하지 않습니다. 
- 위의 다른 모든 이벤트의 경우, 백필을 활성화하기 전에 [일시적으로 중지]({{site.baseurl}}/user_guide/engagement_tools/campaigns/managing_campaigns/change_your_campaign_after_launch/#stopping-your-campaign)하여 메시지가 전송되지 않도록 보장할 수 있습니다.
{% endalert %}

## Shopify 히스토리컬 백필 설정

### 전제 조건

백필을 켜기 전에 다음 이벤트를 활성화해야 합니다. 그렇지 않으면 해당 데이터를 가져오지 않습니다.

- `shopify_created_order`
- Braze 구매 이벤트 

위의 이벤트는 [이벤트 선택]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/setting_up_shopify/#event-selection) 중에 Shopify를 설정하는 동안 활성화할 수 있습니다.

{% alert important %}
통합에서 백필 기능은 한 번만 활성화할 수 있습니다.
{% endalert %}

### 1단계: Shopify 백필 프로세스를 시작합니다

Shopify 파트너 페이지에서 **데이터 백필 시작**을 선택합니다. 기존 Shopify 고객의 경우, Braze가 데이터 백필을 시작하기 전에 모든 과거 주문 이벤트를 수집할 수 있도록 액세스 권한을 다시 부여해야 합니다.

![][3]{: style="max-width:75%;"}

### 2단계: Shopify 데이터의 백필 토글

다음으로, 설정 작성기가 나타나고, 선택적으로 Shopify 과거 데이터 백필을 활성화할 수 있습니다. 이 백필의 일환으로, Braze는 기본적으로 Shopify 통합 이전의 마지막 90일 동안 다음 Shopify 데이터만 동기화합니다.
- 주문 생성 이벤트
- Braze 구매 이벤트
- 고객 데이터

어떤 특정 고객 데이터가 백필되고 있는지 확인하려면 [지원되는 Shopify 고객 데이터](#supported-shopify-customer-data) 섹션을 방문할 수 있습니다.

{% alert note %}
이 기능은 백필 중에 생성된 신규 사용자에 대해 이메일 및 SMS 가입 상태만 동기화합니다. 기존 사용자의 현재 상태를 덮어쓰지 않도록 Braze에서 기존 사용자의 구독 상태를 동기화하지 않습니다.<br><br>현재 동작에 대한 피드백이 있는 경우 **대시보드**의 **리소스** 아래 **제품 로드맵**으로 나열된 제품 포털을 통해 제출합니다. [업데이트된 탐색]({{site.baseurl}}/user_guide/administrative/access_braze/navigation/)을 사용하는 경우 **커뮤니티** > **제품 로드맵**을 선택합니다.
{% endalert %}

**다음**을(를) 누르면 백필이 활성화되어 과거 데이터를 동기화하기 시작합니다. 과거 백필은 **한 번**만 완료할 수 있으므로 데이터 동기화가 완료된 후에는 이 가져오기를 다시 실행할 수 없습니다.

![][1]{: style="max-width:75%;"}

### 3단계: 백필 진행 중

대시보드 알림을 수신하며, 상태가 '진행 중'으로 표시되어 백필이 시작되었음을 나타냅니다. 백필이 완료되는 데 걸리는 시간은 Braze가 Shopify에서 동기화해야 하는 고객 및 주문 수에 따라 달라집니다. 이 시간 동안 이 페이지를 떠나 백필 완료 시점을 알리는 대시보드 알림 또는 이메일을 기다릴 수 있습니다.

![][2]{: style="max-width:75%;"}

### 4단계: 백필 완료
Shopify 백필이 완료된 후 대시보드 알림과 이메일을 받습니다. Shopify 파트너 페이지는 과거 백필 아래에서 상태를 '완료'로 업데이트합니다.

## 지원되는 Shopify 고객 데이터

### Shopify 커스텀 속성

| 속성 이름 | 설명 |
| --- | --- |
| `shopify_order_count` | 이 커스텀 속성은 이 고객이 Shopify에서 완료한 총 주문 수에 해당합니다. 이것은 이 프로세스의 일부로 백필된 사용자만 사용할 수 있습니다. |
| `shopify_total_spent` | 이 커스텀 속성은 Shopify에서 이 고객이 지출한 총 금액에 해당합니다. 이것은 이 프로세스의 일부로 백필된 사용자만 사용할 수 있습니다. |
| `shopify_tags` | 이 속성은 Shopify 관리자에 의해 설정된 [고객 태그](https://help.shopify.com/en/manual/shopify-admin/productivity-tools/using-tags#tag-types)에 해당합니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 }

### Shopify 표준 속성
- 이메일
- 이름
- 성
- 전화
- 도시
- 국가

[1]: {% image_buster /assets/img/Shopify/backfill1.jpg %}
[2]: {% image_buster /assets/img/Shopify/backfill2.png %}
[3]: {% image_buster /assets/img/Shopify/backfill3.png %} 

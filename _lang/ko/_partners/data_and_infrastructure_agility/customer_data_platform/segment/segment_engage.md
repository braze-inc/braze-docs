---
nav_title: Segment Engage
article_title: Segment Engage
page_order: 3
alias: /partners/segment_personas/
alias: /partners/segment_engage/
alias: /partners/data_and_infrastructure_agility/customer_data_platform/segment/segment_personas/

description: "이 참조 문서에서는 마케팅 스택의 소스 간에 정보를 수집하고 라우팅하는 고객 데이터 플랫폼인 Braze와 Segment 간의 파트너십에 대해 간략하게 설명합니다."
page_type: partner
search_tag: Partner

---

# Segment Engage

> [Segment](https://segment.com)는 고객 데이터를 수집, 정리 및 활성화하는 데 도움이 되는 고객 데이터 플랫폼입니다. 이 참조 문서에서는 [Braze와 Segment Engage](https://segment.com/docs/destinations/braze/#Engage) 간의 연결에 대한 개요와 함께 적절한 구현 및 사용을 위한 요구 사항과 프로세스를 설명합니다.

브레이즈와 세그먼트의 통합을 통해 세그먼트에 내장된 오디언스 빌더인 [Engage를](https://segment.com/docs/engage/) 사용하여 다양한 소스에서 이미 수집한 데이터를 기반으로 사용자 세그먼트를 생성할 수 있습니다. 그런 다음, 이 오디언스는 캠페인 및 캔버스 리타겟팅에 사용할 Braze 세그먼트를 만드는 데 사용할 수 있는 커스텀 [속성]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/) 또는 [커스텀 이벤트]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#custom-events)를 통해 고객 프로필에 표시하거나 코호트로 Braze와 동기화됩니다.

## 전제 조건

| 요구 사항 | 설명 |
| ----------- | ----------- |
| Segment 계정 | 이 파트너십을 이용하려면 [세그먼트 계정이](https://app.segment.com/login) 필요합니다. |
| Braze 클라우드 대상 | Segment 통합에서 이미 [Braze를 대상으로 설정]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/segment/segment/#connection-settings/)해야 합니다.<br><br>여기에는 [연결 설정]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/segment/segment/#connection-settings)에서 올바른 Braze 데이터 센터 및 REST API 키를 제공하는 것이 포함됩니다. |
| Braze 데이터 가져오기 키 | Engage 오디언스를 코호트로 Braze와 동기화하려면 데이터 가져오기 키를 생성해야 합니다.<br><br>코호트 가져오기는 얼리 액세스에서 제공되며, 이 기능을 이용하려면 Braze 고객 성공 매니저에게 문의하세요. |

{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 코호트 대상 통합

### 1단계: Engage 오디언스 생성
1. Segment에서 Engage의 **오디언스** 탭으로 이동하고 **새로 만들기**를 클릭합니다.
2. 오디언스를 생성합니다. 페이지 상단 모서리에 번개 모양이 표시되어 오디언스가 실시간으로 업데이트되는지 여부를 알 수 있습니다.
3. 다음으로, Braze를 대상으로 선택합니다.
4. **검토 및 생성**을 클릭하여 오디언스를 미리 봅니다. 기본적으로 Segment는 모든 과거 데이터를 쿼리하여 계산된 특성 및 오디언스의 현재 값을 설정합니다. 이 데이터를 생략하려면 **과거 백필**을 선택 취소합니다.

### 2단계: 코호트 데이터 가져오기 키 캡처

Braze에서 **파트너 통합** > **기술 파트너**로 이동하여 **Segment**를 선택합니다.

여기에서 REST 엔드포인트를 찾아 Braze 데이터 가져오기 키를 생성합니다. 키가 생성된 후에는 새 키를 만들거나 기존 키를 무효화할 수 있습니다.

### 3단계: Braze 코호트 대상 연결
코호트 대상 설정에 관한 [Segment의 지침](https://segment.com/docs/connections/destinations/catalog/actions-braze-cohorts/#getting-started)에 따라 Engage 오디언스를 Braze에 코호트로 동기화합니다.

### 4단계: 참여 오디언스에서 Braze 세그먼트 만들기
Braze에서 **세그먼트**로 이동하고 새 세그먼트를 생성한 후 **Segment 코호트**를 필터로 선택합니다. 여기에서 포함할 Segment 코호트를 선택할 수 있습니다. 세그먼트 코호트 세그먼트가 생성된 후에는 캠페인 또는 캔버스를 만들 때 오디언스 필터로 선택할 수 있습니다.

![][1]

## 클라우드 모드 통합

### 1단계: 세그먼트 계산된 특성 또는 대상 만들기

1. Segment에서 **Engage**의 **오디언스** 또는 **계산된 특성** 탭으로 이동하고 **새로 만들기**를 클릭합니다.
2. 계산된 특성 또는 오디언스를 만듭니다. 페이지 상단에 번개 아이콘이 나타나고 계산이 실시간으로 업데이트되는지 여부를 알려줍니다.
3. 다음으로, 대상으로 **Braze**를 선택합니다. 
4. **검토 및 생성**을 클릭하여 오디언스를 미리 봅니다. 기본적으로 Segment는 모든 과거 데이터를 쿼리하여 계산된 특성 및 오디언스의 현재 값을 설정합니다. 이 데이터를 생략하려면 **과거 백필**을 선택 취소합니다.
5. 계산된 특성 또는 오디언스 설정에서 데이터를 Braze로 전송할 방식에 따라 연결 설정을 조정합니다.

#### 계산된 특성 및 대상

[계산된 특성과](https://segment.com/docs/engage/audiences/computed-traits/) [오디언스는](https://segment.com/docs/Engage/audiences/) 사용자 지정 속성 또는 사용자 지정 이벤트로 Braze에 전송할 수 있습니다.
- `identify` 호출을 사용하여 전송된 특성 및 오디언스는 Braze에 사용자 지정 속성으로 표시됩니다.
- `track` 호출을 사용하여 전송된 특성 및 오디언스는 Braze에 사용자 지정 이벤트로 표시됩니다.

계산된 특성을 Braze 대상에 연결할 때 사용할 방법을 선택하거나 둘 다 사용하도록 선택할 수 있습니다.

{% tabs %}
{% tab 식별 %}

계산된 특성과 오디언스를 `identify` 호출로 Braze에 전송하여 Braze에서 커스텀 속성을 생성할 수 있습니다. 

예를 들어, '마지막으로 조회한 제품 항목'에 대한 Engage의 계산된 특성이 있는 경우 **커스텀 속성** 아래의 Braze 고객 프로필에서 `last_product_viewed_item`을 찾을 수 있습니다. 대신 Engage 오디언스인 경우, `true`로 설정된 **커스텀 속성** 아래에 오디언스가 표시됩니다.

| 계산된 특성 | 오디언스 |
| -------------- | --------- |
| ![고객 프로필 내 커스텀 속성 섹션에서 'last_product_viewed_item'이 'Sweater'로 나열됩니다.]({% image_buster /assets/img/segment/last_viewed-id-braze.png %}) | ![사용자 프로필 내 사용자 지정 속성 섹션에 "dormant_shopper"가 "true"로 나열됩니다.]({% image_buster /assets/img/segment/dormant-identify-braze.png %}) |

{% endtab %}
{% tab 추적 %}

계산된 특성과 오디언스를 `track` 호출로 Braze에 전송하여 Braze에서 커스텀 이벤트를 생성할 수 있습니다. 

계속해서 이전 예제에서, 사용자에게 '마지막으로 조회한 제품 항목'에 대한 계산된 특성이 있는 경우 **커스텀 이벤트** 아래에 해당 수와 가장 최근 타임스탬프가 포함된 `Trait Computed`로 Braze 고객 프로필에 표시됩니다. 대신 Engage 오디언스인 경우 `true`로 설정된 **커스텀 속성** 아래에 오디언스, 수 및 가장 최근 타임스탬프가 표시됩니다.

| 계산된 특성 | 오디언스 |
| -------------- | --------- |
| ![고객 프로필 내 커스텀 이벤트 섹션에는 '계산된 특성' '1'시간이 나열되며 마지막 시간은 '20시간 전'입니다.]({% image_buster /assets/img/segment/last_viewed-track-braze.png %}) | ![고객 프로필 내 커스텀 속성 섹션에는 '진입한 오디언스' '1'시간이 나열되며, 마지막 시간은 '3월 9일 오전 1시 45분'입니다.]({% image_buster /assets/img/segment/dormant-track-braze.png %}) |

{% endtab %}
{% endtabs %}

### 2단계: Braze에서 사용자 세분화

Braze에서 이러한 사용자의 세그먼트를 만들려면 **참여** 아래의 **세그먼트로** 이동하여 새 세그먼트를 만들고 세그먼트의 이름을 지정합니다. 다음으로, 사용한 통화를 기준으로 합니다:
- **식별**: 필터로 **사용자 지정 속성을** 선택하고 사용자 지정 속성을 찾습니다. 그런 다음, '일치 정규식' 옵션(특성) 또는 '같음' 옵션(오디언스)을 사용하여 적절한 변수를 입력합니다.
- **추적**: 필터로 **사용자 지정 이벤트를** 선택하고 사용자 지정 이벤트를 찾습니다. 그런 다음, '초과', '미만' 또는 '정확히' 옵션을 사용하여 원하는 값을 삽입합니다. 이는 세그먼트를 어떻게 정의할 것인지에 따라 달라집니다.

저장한 후에는 사용자 타겟팅 단계에서 캔버스 또는 캠페인을 생성하는 동안 이 세그먼트를 참조할 수 있습니다.

## 동기화 시간

Braze와 Segment Engage 연결의 기본 설정은 `Realtime`이지만, 메시지 전송 시 오디언스 규모를 제한하는 시간 기반 필터를 포함하여 페르소나를 실시간으로 동기화할 수 없도록 하는 일부 필터가 있습니다.

## 세그먼트 디버거 테스트

Segment의 대시보드는 고객이 '소스'의 데이터가 예상대로 '대상'으로 전송되는지 테스트하도록 지원하는 '디버거' 기능을 제공합니다.

이 기능은 Braze [`/users/track` 엔드포인트]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)에 연결되므로 식별된 사용자(이미 Braze 고객 프로필에 대한 사용자 ID가 있는 사용자)에 대해서만 사용할 수 있습니다.

이 기능은 Braze 병렬 통합에서 작동하지 않습니다. 올바른 Braze REST API 정보를 입력하지 않으면 서버 데이터가 전송되지 않습니다.

[1]: {% image_buster /assets/img/segment/segment3.png %}
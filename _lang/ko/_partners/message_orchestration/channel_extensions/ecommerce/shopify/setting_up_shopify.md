---
nav_title: Shopify 설정
article_title: "Shopify 설정"
description: "이 참조 문서에서는 Braze 웹 SDK에 통합한 후 Shopify를 설정하는 방법을 간략하게 설명합니다."
page_type: partner
search_tag: Partner
alias: "/shopify_subscription_states/"
alias: "/setting_up_shopify/"
page_order: 2
---

# Braze에서 Shopify 설정

> 이 문서에서는 Braze와의 Shopify 통합 설정을 완료하는 방법을 간략하게 설명합니다. Shopify 웹사이트에 [Braze Web SDK를 구현한]({{site.baseurl}}//partners/message_orchestration/channel_extensions/ecommerce/shopify/getting_started_shopify/#implement-web-sdk) 후 다음 지침을 따르십시오.

## Braze에서 Shopify 통합 설정

### 1단계: Shopify 스토어 연결

Braze에서 **파트너 통합** > **기술 파트너로** 이동한 다음 "Shopify"를 검색합니다.

{% alert note %}
이전 탐색을 사용하는 경우 **통합**에서 **기술 파트너**를 찾을 수 있습니다.
{% endalert %}

Shopify 파트너 페이지에서 **Shopify 앱스토어로 이동을** 선택하여 통합 프로세스를 시작합니다.

![]({% image_buster /assets/img/Shopify/shop_setup_1.png %}){: style="max-width:70%"}

그러면 Braze 앱을 설치할 수 있는 Shopify 앱 스토어로 이동합니다.

{% alert note %}
Shopify 계정이 두 개 이상의 스토어와 연결된 경우 페이지 오른쪽 상단의 스토어 아이콘을 선택하고 **스토어 전환을** 선택하여 로그인 중인 스토어를 전환할 수 있습니다.
{% endalert %}

![]({% image_buster /assets/img/Shopify/switch_stores.png %}){: style="max-width:30%"}

원하는 스토어를 선택한 후 Braze 앱 페이지에서 **설치를** 선택합니다. 

![]({% image_buster /assets/img/Shopify/braze_install.png %}){: style="max-width:70%"}

Braze 앱을 설치하면 Shopify에 연결할 작업 공간을 확인하기 위해 Braze로 리디렉션됩니다. 

![]({% image_buster /assets/img/Shopify/confirm_workspace.png %}){: style="max-width:50%"}

올바른 작업 공간에 있는지 확인한 후 **설정 시작을** 선택하여 Shopify 통합 구성을 완료할 수 있습니다.

![]({% image_buster /assets/img/Shopify/begin_setup.png %}){: style="max-width:70%"}

{% alert note %}
현재 워크스페이스당 하나의 스토어만 연결할 수 있습니다. 워크스페이스에 연결하려는 Shopify 스토어가 여러 개 있는 경우 Shopify의 여러 스토어 베타에 대한 자세한 내용은 고객 성공 매니저에게 문의하세요.
{% endalert %}

### 2단계: 이벤트 및 과거 백필 선택

Shopify 스토어를 연결한 후 2단계로 진행하여 통합의 일부로 포함할 이벤트를 선택합니다. 하나 이상의 이벤트를 선택해야 합니다.

![]({% image_buster /assets/img/Shopify/shopify_step_2_events.png %}){: style="max-width:70%"}

**제품 조회**, **제품 클릭** 또는 **장바구니 이탈** 이벤트를 선택하려면 추적에 Braze 웹 SDK가 필요합니다. [Shopify ScriptTag]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/getting_started_shopify/?tab=shopify%20scripttag#supported-features)를 통해 또는 Shopify 사이트 [`theme.liquid`]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/getting_started_shopify/?tab=theme.liquid#supported-features)에 직접 Braze 웹 SDK를 구현하는 경우 Braze는 자동으로 추적 스크립트를 생성하여 사이트에 로드합니다. [헤드리스 Shopify 사이트]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/getting_started_shopify/#implement-web-sdk)에 대해 웹 SDK를 구현하는 경우 이러한 이벤트에 대한 추적을 수동으로 켜야 합니다. 

#### 기록 데이터 다시 채우기(선택 사항)

선택적으로 설치 전 지난 90일 동안의 구매 백필을 활성화할 수 있습니다. 과거 고객 및 구매 데이터를 자동으로 동기화하여 즉시 고객을 타겟팅하고 참여를 유도할 수 있습니다. 자세한 내용은 Shopify 과거 백필을 확인합니다.

![]({% image_buster /assets/img/Shopify/shop_setup_4.png %}){: style="max-width:70%"}

{% alert warning %}
주문 생성 이벤트 및 Braze 구매 이벤트를 가져오기 위한 백필의 경우 통합의 일부로 포함할 **주문 생성** 및 **Braze 구매 이벤트**를 선택해야 합니다.
{% endalert %}

### 3단계: 구독자 수집(선택 사항)

Shopify 통합을 사용하면 Shopify 스토어에서 Braze로 이메일 및 SMS 가입자를 수집할 수 있습니다. 자세한 내용은 [Shopify 가입자 동기화를]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/shopify_features/shopify_user_identity/#syncing-shopify-subscribers) 참조하십시오.

![]({% image_buster /assets/img/Shopify/shopify_step_3_email.png %}){: style="max-width:70%"}

### 4단계: Shopify 제품 동기화 설정(선택 사항)

선택적으로 Shopify 스토어에서 Braze 카탈로그로 제품을 거의 실시간으로 동기화하여 제품 데이터를 가져오는 프로세스를 자동화하여 메시지를 더욱 심층적으로 개인화할 수 있습니다. 자세한 내용은 [Shopify 제품 동기화를]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/shopify_features/shopify_catalogs/) 확인하십시오.

![]({% image_buster /assets/img/Shopify/shopify_step_4_catalog.png %}){: style="max-width:70%"}

### 5단계: 인브라우저 메시징 사용 

이 기능을 사용하도록 설정하면 선택적으로 브라우저 내 메시지에 대해 Shopify 스토어에서 추가 채널을 사용할 수 있습니다. 이를 통해 슬라이드업, Modal, 전체 화면, 간단한 설문조사 및 커스텀 HTML과 같은 기본 메시지 유형을 사용할 수 있습니다.

![]({% image_buster /assets/img/Shopify/shopify_step_5_channels.png %}){: style="max-width:70%"}

인브라우저 메시지를 활성화하는 경우, 추적을 위해 Braze 웹 SDK를 구현해야 합니다. [Shopify ScriptTag]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/getting_started_shopify/?tab=shopify%20scripttag#supported-features)를 통해 또는 Shopify 사이트 [`theme.liquid`]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/getting_started_shopify/?tab=theme.liquid#supported-features)에 직접 Braze 웹 SDK를 구현하는 경우 Braze는 자동으로 기본 인브라우저 메시지 구현을 생성하여 사이트에 로드합니다. [헤드리스 Shopify 사이트]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/getting_started_shopify/#implement-web-sdk)에 대해 웹 SDK를 구현하거나 인브라우저 메시지에 대한 사용자 지정을 추가하려는 경우 [개발자 가이드](/developer_guide/platform_integration_guides/web/in-app_messaging/integration/)를 사용하여 인브라우저 메시지를 사이트에 수동으로 추가해야 합니다. 

### 6단계: 설정 완료

설정을 구성한 후 **설정 완료**를 선택합니다.

![]({% image_buster /assets/img/Shopify/finish_setup.png %}){: style="max-width:70%"}

끝입니다! '연결 보류 중' 상태가 '연결됨'으로 업데이트되고 연결이 설정된 시점의 타임스탬프가 표시됩니다. 또한 페이지에서 각 Shopify 기능이 성공적으로 활성화되었는지 확인할 수 있습니다. 

![]({% image_buster /assets/img/Shopify/shopify_connected_store.png %}){: style="max-width:70%"}

### 고급 설정(선택 사항) 

#### 중단된 카트 및 중단된 결제 지연 업데이트

기본적으로 Braze는 `shopify_abandoned_checkout` 및 `shopify_abandoned_cart` 이벤트가 트리거되는 지연 시간을 비활동 상태 1시간으로 자동 설정합니다. 드롭다운을 선택한 다음 Shopify 파트너 페이지에서 **지연 설정을** 선택하여 각 이벤트에 대한 **중단된 카트 지연** 및 **중단된 결제 지연을** 5분에서 최대 24시간까지 설정할 수 있습니다.

![]({% image_buster /assets/img/Shopify/shop_setup_advanced_abandonment.png %}){: style="max-width:30%"}

#### 선호하는 제품 식별자 설정

Shopify 통합 설정에 Braze 구매 이벤트를 포함한 경우 기본적으로 Braze는 Braze 구매 이벤트 내에서 사용되는 `product_id`로 Shopify 제품 ID를 설정합니다. 이 정보는 Y일 이내에 구매한 제품을 필터링하거나 Liquid를 사용하여 메시지의 콘텐츠를 개인화할 때 사용됩니다.

또한 Shopify 제품 ID 대신, Shopify에서 SKU 또는 제품 제목을 설정하도록 선택할 수도 있습니다.

![]({% image_buster /assets/img/Shopify/shop_setup_advanced_productid.png %}){: style="max-width:30%"}

## 문제 해결

{% details Shopify 앱 설치가 아직 보류 중인 이유는 무엇인가요? %}
다음 이유 중 하나로 인해 설치가 보류 중일 수 있습니다:
 - Braze가 Shopify 웹훅을 설정하는 경우
 - Braze가 Shopify와 통신하는 경우


앱 설치가 1시간 동안 보류 중인 경우 Braze는 설치에 실패하고 설정을 재시도하라는 프롬프트가 표시됩니다.<br><br>
![Shopify]({% image_buster /assets/img/Shopify/shopify_integration8.png %}){: style="max-width:70%;"}
{% enddetails %}


{% details Shopify 앱 설치가 실패한 이유는 무엇인가요? %}
다음 이유 중 하나로 인해 설치가 실패했을 수 있습니다:
 - Braze를 Shopify에 연결할 수 없음
 - Braze가 요청을 처리하지 못했습니다.
 - Shopify 액세스 토큰이 유효하지 않습니다.
 - Shopify 관리자 페이지에서 Braze Shopify 앱이 삭제되었습니다.


이 경우 **재시도 설정**을 선택하고 설치 프로세스를 다시 시작할 수 있습니다.<br><br>
![Shopify]({% image_buster /assets/img/Shopify/shopify_integration16.png %}){: style="max-width:70%;"}
{% enddetails %}


{% details 내 Shopify 스토어에서 Braze 애플리케이션을 제거하려면 어떻게 합니까? %}

Shopify 스토어에서 Braze를 제거하는 두 가지 방법이 있습니다.

1. Shopify 파트너 페이지에서 **연결 해제를** 선택합니다.<br><br> ![연결 해제 링크가 있는 '통합 연결 해제' 섹션(]({% image_buster /assets/img/Shopify/disconnect_integration.png %}){: style="max-width:70%;"}

2. **앱** 아래에 있는 Shopify 관리자 페이지로 이동합니다. 그러면 Braze 애플리케이션을 삭제할 수 있는 옵션이 표시됩니다.<br><br> ![Braze 앱을 삭제할 것인지 확인하는 모달이 표시됩니다.]({% image_buster /assets/img/Shopify/shopify_integration12.png %}){: style="max-width:70%;"}
{% enddetails %}

{% details 사용자를 조정하는 데 어려움을 겪고 있습니다. 그 이유는 무엇일까요? %}

사용자 조정에 필요한 지원 유형은 웹 SDK를 구현한 방법에 따라 결정됩니다. 자세한 내용은 [Shopify 시작하기]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/getting_started_shopify/)를 참조하세요. 

- Shopify 헤드리스 사이트를 사용하는 경우 [헤드리스 구현]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/getting_started_shopify/?tab=headless%20shopify%20site#supported-features)을 확인하여 결제 사용자 조정을 활성화했는지 확인합니다.
- 이메일이나 전화번호가 동일한 사용자 프로필이 중복되는 경우, 다음 Braze 도구를 사용하여 중복된 프로필을 하나의 프로필로 병합할 수 있습니다: 
    - [`users/merge`]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/) 엔드포인트
    - [대량 병합]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/duplicate_users#bulk-merging)
- ScriptTag 통합을 사용하고 Shopify 스토어에서 장바구니를 건너뛰는 '지금 구매' 옵션을 제공하는 경우, Shopify에서 스크립트 태그를 통해 장바구니를 건너뛰는 사용자에게 이벤트를 매핑하기 위해 `device_id`를 검색할 수 없으므로 Braze에서 사용자를 조정하는 데 어려움을 겪을 수 있습니다.

{% enddetails %}
---
nav_title: 통합 개요
article_title: 통합 개요
page_order: 2
description: "이 문서에서는 온보딩 프로세스에 대한 기본적인 개요를 제공합니다."
platform:
  - iOS
  - Android
  - Web
  - React Native
  - Flutter
  - Cordova
  - Roku
  - Swift
  - Unity
---

# [![Braze 학습 과정]](https://learning.braze.com/sdk-integration-basics)({% image_buster /assets/img/bl_icon3.png %}){: style="float:right;width:120px;border:0;" class="noimgborder"}시작하기: 통합 개요

> 이 문서에서는 온보딩 프로세스에 대한 기본적인 개요를 제공합니다.

!['가치 실현 시간'을 중심으로 발견, 통합, 품질 보증, 유지 관리 등 네 개의 원으로 구성된 벤 다이어그램]({% image_buster /assets/img/getting-started/getting-started-integrate-flower.png %}){: style="max-width:50%;float:right;margin-left:15px;border:none;"} 

기술 리소스는 Braze를 기술 스택에 통합하여 팀의 역량을 강화할 수 있습니다. 온보딩은 크게 네 단계로 나뉩니다:
* [발견 및 계획](#discovery): 팀과 협력하여 범위를 조정하고, 데이터 및 캠페인의 구조를 계획하며, 적절한 워크스페이스 구조를 구축합니다. 
* [통합](#integration): SDK와 API를 통합하고, 메시징 채널을 활성화하며, 데이터 가져오기 및 내보내기를 설정하여 계획을 실행합니다. 
* [품질 보증](#qa): Braze 플랫폼과 앱 또는 사이트 간의 데이터 및 메시징 루프가 예상대로 작동하는지 확인합니다.
* [유지 관리](#maintenance): 마케팅 팀에 Braze를 넘긴 후에도 모든 것이 원활하게 운영되도록 계속 관리해야 합니다.

<br>
{% alert tip %}
저희는 모든 조직이 각기 다른 요구사항을 가지고 있다는 것을 알고 있으며, Braze는 특정 요구사항에 맞는 다양한 사용자 지정 옵션을 제공할 수 있도록 제작되었습니다. 통합 시간은 사용 사례에 따라 달라질 수 있습니다. 
{% endalert %}

## 검색 및 계획 {#discovery}

이 단계에서는 팀과 협력하여 온보딩 작업의 범위를 정하고 공통의 목표에 맞춰 모든 이해관계자를 조율할 수 있도록 합니다. 

팀은 사용 사례에 대한 포괄적인 계획을 세우고 이를 위해 정확한 데이터를 바탕으로 모든 것이 예상대로 구축될 수 있도록 보장합니다. 이 단계에는 프로젝트 리드, CRM 리드, 프론트엔드 및 백엔드 엔지니어링, 제품 소유자, 마케터가 참여합니다. 

검색 및 계획 단계에는 평균적으로 약 6주가 소요됩니다. 엔지니어링 리드는 이 단계에서 일주일에 2~4시간 정도 시간을 소비하리라 예상됩니다. 제품을 개발하는 개발자는 검색 및 계획 단계에서 일주일에 10~20시간을 Braze에 투자하리라 예상됩니다. 

{% alert tip %}
회사의 온보딩 기간에 Braze는 기술 개요 세션을 진행합니다. 엔지니어는 이 세션에 참석할 것을 적극 권장합니다. 기술 개요 세션에서는 플랫폼 아키텍처의 확장성에 대한 대화를 나누고, 비슷한 규모의 기업이 유사한 사용 사례로 어떻게 성공했는지 실제 사례를 확인할 수 있습니다.
{% endalert %}

![이메일, 장바구니, 이미지, 지리적 위치 등 다양한 채널에 대한 아이콘]({% image_buster /assets/img/getting-started/data-graphic-2.png %}){: style="max-width:40%;float:right;margin-left:15px;"} 

### 캠페인 계획

CRM 팀은 가까운 시일 내에 출시할 메시징 사용 사례를 계획합니다. 여기에는 다음이 포함됩니다:
* [채널]({{site.baseurl}}/user_guide/message_building_by_channel) (예: 푸시 알림 또는 인앱 메시지)
* [배송 방법]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types) (예: 예약 배송 또는 작업 기반 배송)
* [타겟 오디언스]({{site.baseurl}}/user_guide/engagement_tools/segments)
* [성공 지표]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events/)

예를 들어, 어제 첫 세션을 로그인한 고객 세그먼트에 매일 오전 10시에 이메일을 보내는 새로운 고객 캠페인이 있을 수 있습니다. 전환 이벤트(성공 지표)가 세션을 로깅하고 있습니다.

<br>
{% alert important %}
캠페인 계획 단계가 완료될 때까지 통합을 시작할 수 없습니다. 이 단계에서는 통합 단계에서 구성해야 하는 Braze의 구성요소와 조각을 결정합니다.
{% endalert %}

### 데이터 요구 사항 만들기

그런 다음, CRM 팀은 계획한 캠페인을 시작하는 데 필요한 데이터를 정의하여 데이터 요구 사항을 만들어야 합니다. 

이름, 이메일, 생년월일, 국가 등과 같은 많은 일반적인 유형의 사용자 속성은 Braze SDK가 통합된 후 자동으로 추적됩니다. 다른 유형의 데이터는 사용자 지정 데이터로 정의해야 합니다.

개발자는 팀과 협력하여 추적할 추가적인 커스텀 데이터를 정의할 수 있습니다. 사용자 지정 데이터는 사용자 기반을 분류하고 세분화하는 방식에 영향을 미칩니다. 성장 스택 전반에 걸쳐 이벤트 분류를 설정하여 데이터가 Braze로 송수신될 때 시스템과 호환되도록 데이터를 구조화할 수 있습니다.

{% alert tip %}
여러 도구에서 데이터 명명법을 일관되게 유지하세요. 예를 들어, 데이터 웨어하우스에서 '구매 기간 한정 혜택'을 특정 방식으로 기록할 수 있습니다. 이 형식에 맞게 Braze에서 사용자 지정 이벤트가 필요한지 결정해야 합니다.
{% endalert %}

[데이터 및 커스텀 데이터 자동 수집]({{site.baseurl}}/developer_guide/analytics/)에 대해 자세히 알아보세요.

### 사용자 지정 계획

원하는 사용자 지정에 대해 마케터와 상의합니다. 예를 들어 기본 Braze 콘텐츠 카드를 구현하고 싶으신가요? 브랜드 지침에 맞게 모양과 느낌을 약간 조정하고 싶으신가요? 컴포넌트에 대한 완전히 새로운 UI를 개발하고 Braze가 그 분석을 추적하도록 하고 싶으신가요? 사용자 지정 수준에는 다양한 수준의 범위가 필요합니다.

### 대시보드 액세스 권한 얻기

Braze 대시보드는 웹 UI 인터페이스입니다. 마케터는 대시보드를 사용하여 업무를 수행하고 콘텐츠를 제작합니다. 개발자는 대시보드를 사용하여 API 키 및 푸시 알림 자격 증명과 같은 앱 통합을 위한 설정을 관리합니다.

팀 관리자가 대시보드에 사용자로 본인 및 Braze에 액세스해야 하는 다른 모든 팀원을 추가해야 합니다.

### 워크스페이스 및 API 키

팀 관리자는 다른 [작업 공간도]({{site.baseurl}}/user_guide/administrative/app_settings/workspaces/) 만들 수 있습니다. 워크스페이스는 사용자, 세그먼트, API 키와 같은 데이터를 한 곳에 그룹화합니다. 모범 사례로 동일한 앱의 서로 다른 버전 또는 매우 유사한 앱을 하나의 워크스페이스에 모으는 방식만 제안합니다. 

중요한 점은 워크스페이스가 여러 플랫폼(예: iOS 및 Android)에 대한 API 키를 제공한다는 점입니다. 연관된 API 키를 사용하여 SDK 데이터를 특정 워크스페이스에 연결할 수 있습니다. 워크스페이스로 이동하여 각 앱의 API 키에 액세스합니다. 각 API 키에 범위를 지정한 작업을 수행할 수 있는 올바른 권한이 있는지 확인합니다. 자세한 내용은 [API 프로비저닝 문서]({{site.baseurl}}/api/basics/#rest-api-key)를 참조하세요.

{% alert important %}
개발과 프로덕션을 위해 서로 다른 환경을 설정하는 것이 중요합니다. 테스트 환경을 설정하면 온보딩 및 QA 과정에서 실제 비용의 지출을 방지할 수 있습니다. 테스트 환경을 구축하려면 테스트 워크스페이스를 설정하고 프로덕션 워크스페이스에 테스트 데이터를 채우지 않도록 해당 API 키를 사용해야 합니다.
{% endalert %}  

## 통합 {#integration}

![데이터 소스에서 사용자 디바이스로의 정보 흐름을 나타내는 추상 피라미드 그래픽입니다.]({% image_buster /assets/img/getting-started/data-graphic.png %}){: style="max-width:45%;float:right;margin-left:15px;"} 

Braze는 iOS 앱, Android 앱, 웹 앱 등을 지원합니다. React Native 또는 Unity와 같은 크로스플랫폼 래퍼 SDK를 사용할 수도 있습니다. 일반적으로 1~6주 정도면 고객은 통합을 마칠 수 있습니다. 많은 고객이 폭넓은 기술력과 대역폭에 따라 단 한 명의 엔지니어와 함께 Braze를 통합니다. 전적으로 구체적인 통합 범위와 팀이 Braze 프로젝트에 얼마나 많은 시간을 할애하는지에 따라 달라집니다. 

이에 익숙한 개발자가 필요합니다:
* 앱 또는 사이트의 네이티브 레이어에서 작업하기
* REST API를 호출하는 프로세스 생성
* 통합 테스트 
* JSON 웹 토큰 인증
* 일반적인 데이터 관리 기술
* DNS 레코드 설정

### CDP 통합 파트너

많은 고객이 통합 파트너로 고객 데이터 플랫폼(CDP)과도 통합할 수 있는 기회로 활용하고자 Braze 온보딩을 사용합니다. Braze는 데이터 추적 및 분석을 제공하며, CDP는 추가적인 데이터 라우팅 및 오케스트레이션을 제공할 수 있습니다. Braze는 [엠파티클]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/mparticle/mparticle/), [세그먼트]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/segment/segment/) 등 다양한 CDP와 원활하게 통합할 수 있습니다. 

CDP와 병렬 통합을 수행하는 경우, CDP의 SDK에서 Braze SDK로 호출을 매핑합니다. 특히 다음을 수행합니다.
* `changeUser`([Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/change-user.html), [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/changeuser(userid:sdkauthsignature:fileid:line:)/), [웹](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#changeuser))에 식별 호출을 매핑하고 속성을 설정합니다.
* `requestImmediateDataFlush`([Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/request-immediate-data-flush.html?query=abstract%20fun%20requestImmediateDataFlush()), [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/requestimmediatedataflush()), [웹](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#requestimmediatedataflush))에 데이터 플러시 호출을 매핑합니다.
* 사용자 지정 이벤트 또는 구매를 기록합니다.

선택한 플랫폼에 따라 Braze SDK와 선택한 CDP 간의 통합 예제를 사용할 수 있습니다. 자세한 내용은 [CDP 기술 파트너 목록을]({{site.baseurl}}/partners/data_and_analytics/) 참조하세요. 

### Braze SDK 통합

Braze SDK는 사용자 데이터를 수집하여 통합 고객 프로필에 동기화하고, 푸시 알림, 인앱 메시지, 콘텐츠 카드와 같은 메시징 채널을 지원하는 두 가지 중요한 기능을 제공합니다. 

{% alert tip %}
앱 또는 사이트에 완전히 통합된 Braze SDK는 완벽하게 구현된 수준의 정교한 마케팅을 제공합니다. Braze SDK 통합을 연기하면 설명서에 나온 일부 기능을 사용할 수 없습니다.
{% endalert %}

SDK를 구현하는 동안 다음을 수행합니다.

* 지원하려는 각 플랫폼에 대한 SDK 통합 코드를 작성합니다.
* 각 플랫폼에 대한 메시징 채널을 활성화하여 이메일, SMS, 푸시 알림 및 기타 채널에서 고객과의 상호 작용 데이터를 Braze SDK가 추적하도록 합니다.
* 계획된 UI 컴포넌트 커스터마이징(예: 커스텀 콘텐츠 카드)을 생성합니다. 완전한 커스텀 콘텐츠의 경우 SDK의 자동 데이터 수집이 새 구성요소를 인식하지 못하므로 분석을 기록해야 합니다. 기본 구성 요소에 이 구현을 패턴화할 수 있습니다.

### Braze API 사용

Braze를 사용하는 동안 여러 시점에 다양한 작업을 위해 REST API를 사용합니다. Braze API는 다음과 같은 경우에 유용합니다:

1. 기록 데이터 가져오기
2. Braze에서 트리거되지 않는 지속적인 업데이트. 예를 들어, 사용자가 앱에 로그인하지 않고도 사용자 프로필이 VIP로 업그레이드되는 경우 API는 이 정보를 Braze에 전달해야 합니다.

[Braze API]({{site.baseurl}}/api/basics) 시작하기.

{% alert important %}
API를 사용하는 동안 요청을 배치로 처리하고 델타 값만 전송해야 합니다. Braze는 전송되는 모든 속성을 다시 작성합니다. 값이 변경되지 않은 사용자 지정 속성은 업데이트하지 마세요.
{% endalert %}

### 제품 분석 설정

Braze는 기본적으로 데이터를 다룹니다. Braze의 데이터는 사용자 프로필에 저장됩니다. 

데이터 포인트는 마케터가 단순히 모을 수 있는 '모든' 데이터나 아니라 올바른 데이터를 수집할 수 있도록 지원하는 구조입니다. [데이터 포인트에]({{site.baseurl}}/user_guide/data/data_points/) 익숙해지세요.

### 레거시 사용자 데이터 마이그레이션

Braze [`/users/track endpoint`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) 를 사용하여 Braze 외부에 기록된 과거 데이터를 마이그레이션할 수 있습니다. 일반적으로 가져오는 데이터의 예로, 푸시 토큰과 과거 구매 내역이 있습니다. 이 엔드포인트는 일회성 가져오기 또는 정기적인 배치 업데이트에 사용할 수 있습니다. 

대시보드에 한 번의 [CSV 업로드를]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import#importing-a-csv) 통해 사용자를 가져오고 고객 속성 값을 업데이트할 수도 있습니다. CSV 업로드는 마케터에게 유용한 반면, REST API를 사용하면 더 큰 유연성을 확보할 수 있습니다.

### 세션 추적 설정

Braze SDK는 '세션 열기' 및 '세션 닫기' 데이터 포인트를 생성합니다. Braze SDK는 정기적으로 데이터를 플러시하기도 합니다. 세션 추적 기본값은 이 링크를 참조하세요([Android]({{site.baseurl}}/developer_guide/analytics/tracking_sessions/?tab=android), [iOS]({{site.baseurl}}/developer_guide/analytics/tracking_sessions/?tab=swift), [웹]({{site.baseurl}}/developer_guide/analytics/tracking_sessions/?tab=web)). 모두 사용자 지정할 수 있습니다.

### 사용자 지정 이벤트, 속성 및 구매 이벤트 추적하기

팀과 협력하여 커스텀 이벤트, 사용자 속성, 구매 이벤트 등 계획한 데이터 스키마를 설정합니다. [커스텀 데이터 스키마]({{site.baseurl}}/user_guide/data/custom_data/custom_events/)는 대시보드를 사용하여 입력되며 SDK 통합 중에 구현한 내용과 정확히 일치해야 합니다.

{% alert tip %}
Braze에서 `external_id`라고 하는 사용자 ID는 알려진 모든 사용자에 대해 설정해야 합니다. 사용자가 앱을 열었을 때 변경되지 않고 액세스할 수 있어야 여러 기기와 플랫폼에서 사용자를 추적할 수 있습니다. 모범 사례는 [사용자 수명 주기]({{site.baseurl}}/user_guide/data/user_data_collection/user_profile_lifecycle/) 문서를 참조하세요.
{% endalert %}

### 기타 도구

사용 사례에 따라 설정해야 하는 다른 도구가 있을 수 있습니다. 예를 들어 사용자 스토리를 구현하기 위해 [지오펜스]({{site.baseurl}}/user_guide/engagement_tools/locations_and_geofences#about-locations-and-geofences/)와 같은 툴을 구성해야 할 수 있습니다. 필수 통합 단계를 완료한 후 이러한 추가 툴을 설정할 수 있는 능력이 있는 고객이 가장 성공적인 것으로 나타났습니다.

## 품질 보증 {#qa}
통합을 실행할 때 설정한 모든 기능이 예상대로 작동하는지 확인하기 위해 품질 보증을 제공합니다. 이 QA는 데이터 수집과 메시지 채널이라는 두 가지 일반적인 범주로 분류됩니다.

{% alert important %}
QA를 시작하기 전에 프로덕션 및 테스트 환경이 설정되어 있는지 확인하세요.
{% endalert %}

| **QA 데이터 수집**  | **QA 메시징**                                              |
|---------------------------|---------------------------------------------------------------|
| 데이터 수집, 저장, 내보내기 방식에 대한 품질 보증을 수행합니다. | 사용자에게 메시지가 올바르게 전송되고 있는지, 모두 잘 보이는지 확인할 수 있습니다. |
| 테스트를 실행하여 데이터가 제대로 저장되었는지 확인합니다. | 사용자 세그먼트를 만듭니다. |
| 세션 데이터가 Braze 내에서 의도한 워크스페이스에 올바르게 기여하는지 확인합니다. | 캠페인과 캔버스를 성공적으로 시작합니다. |
| 세션 시작과 종료가 기록되고 있는지 확인합니다. | 올바른 캠페인이 올바른 사용자 세그먼트에 표시되고 있는지 확인합니다. |
| 사용자 속성 정보가 사용자 프로필에 대해 올바르게 기록되었는지 확인합니다. | 푸시 토큰이 올바르게 등록되었는지 확인합니다. |
| 사용자 프로필에 대해 사용자 지정 데이터가 올바르게 기록되고 있는지 테스트합니다. | 푸시 토큰이 올바르게 제거되었는지 확인합니다. |
| 익명 사용자 프로필을 만듭니다. | 푸시 캠페인이 디바이스에 올바르게 전송되고 참여가 기록되는지 테스트합니다. |
| `changeUser()` 메서드가 호출될 때 익명 고객 프로필이 알려진 고객 프로필이 되는지 확인합니다. | 인앱 메시지가 전달되고 지표가 기록되는지 테스트합니다. |
|                           | 콘텐츠 카드가 전달되고 지표가 기록되는지 테스트합니다. |
|                           | 커넥티드 콘텐츠 활성화(예: AccuWeather). |
|                           | 모든 메시지 채널 통합이 제대로 작동하는지 확인합니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

{% alert note %}
SDK 통합에 대한 QA를 수행하는 동안 [SDK 디버거를]({{site.baseurl}}/developer_guide/sdk_integration/debugging) 사용하면 앱에 대한 자세한 로깅을 켜지 않고도 문제를 해결할 수 있습니다.
{% endalert %}

### 마케터에게 Braze 전달

플랫폼이나 사이트를 통합한 후에는 마케팅 팀을 참여시켜 플랫폼의 소유권을 넘겨주는 것이 좋습니다. 이 프로세스는 회사마다 다르지만 다음과 같은 사항이 포함될 수 있습니다:

* 복잡한 [리퀴드 로직]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid#about-liquid) 구성
* [이메일 IP 온난화]({{site.baseurl}}/user_guide/message_building_by_channel/email/email_setup/ip_warming/) 지원
* 다른 이해관계자가 추적되는 데이터의 종류를 이해하는지 확인

### 미래를 위한 개발

코드베이스를 상속받았는데 초기 개발자의 생각을 전혀 짐작할 수 없었던 적이 있나요? 코드를 작성하고 완전히 이해했다가 1년 후에 다시 돌아왔을 때 완전히 당황한 적이 있나요? 

Braze를 온보딩할 때 데이터, 고객 프로필, 범위 내 통합과 범위 외 통합, 사용자 지정 작동 방식 등에 관해 내린 종합적인 결정을 되새기면 다시금 명확해질 수 있습니다. 팀이 Braze를 확장하려고 하거나 다른 기술 리소스가 Braze 프로젝트에 할당되면 이러한 정보가 모호해집니다.

기술 개요 세션에서 학습한 정보를 확고히 할 수 있는 리소스를 만드세요. 이 리소스는 팀에 새로 합류하는 개발자의 온보딩 시간을 줄이는 데 도움이 됩니다. 또는 현재 Braze 구현을 확장해야 할 때 스스로에게 상기시키는 역할을 하기도 합니다. 

## 유지 관리 {#maintenance}

마케터에게 인계한 후에는 유지 관리를 위한 리소스 역할을 계속 수행합니다. Braze SDK에 영향을 줄 수 있는 iOS 및 Android 업데이트에 주의를 기울이고 서드파티 공급자가 최신 상태인지 확인해야 합니다. 

Braze [GitHub](https://github.com/braze-inc/)를 통해 Braze 플랫폼의 업데이트를 추적합니다. 때때로 관리자가 긴급 업데이트 및 버그 수정에 대한 이메일을 Braze에서 직접 받기도 합니다. 

## SDK 속도 제한 

### 월간 활성 사용자 CY 24-25 

월간 활성 사용자 - CY 24-25를 구매한 고객의 경우, Braze는 세션, 사용자 속성, 이벤트 및 기타 사용자 프로필 데이터를 업데이트하기 위해 SDK에서 사용하는 API 요청에 대해 서버 측 속도 제한을 적용합니다. 이는 플랫폼의 안정성을 보장하고 빠르고 안정적인 서비스를 유지하기 위한 것입니다. 

* 시간당 요금 한도는 계정의 예상 SDK 트래픽에 따라 설정되며, 이는 구매한 월간 활성 사용자 수(MAU), 업종, 계절성 또는 기타 요인에 따라 달라질 수 있습니다. 시간당 요금 한도에 도달하면 Braze는 다음 시간까지 요청을 스로틀링합니다.
* 모든 속도 제한 요청은 SDK에 의해 자동으로 재시도됩니다.
* SDK 요청은 구현에서 수집된 사용자 지정 데이터의 양과 상관관계가 있습니다. 시간당 요금 한도에 지속적으로 근접하거나 한도에 도달했다면 고려해 보세요:
    * 과도한 데이터 수집을 줄이기 위해 SDK 통합을 검토합니다.
    * 마케팅 사용 사례에 필수적이지 않은 사용자 지정 데이터를 차단합니다.
* 버스트 속도 제한은 매우 짧은 시간(즉, 몇 초 이내)에 많은 양의 요청이 도착할 때 적용되는 단기간의 속도 제한입니다. 버스트 제한이 발생하면 조치를 취할 필요가 없으며, SDK가 곧 다시 시도합니다.

### 요금 한도 찾기

예상 SDK 처리량을 기준으로 현재 제한을 찾으려면 **설정** > **API 및 식별자** > **API 및 SDK 제한으로** 이동하세요.

사용 내역을 보려면 **설정** > **API 및 식별자** > **API 및 SDK 대시보드로** 이동하세요.

### 변경 사항 및 지원

Braze는 시스템 안정성을 보호하거나 계정의 데이터 처리량을 늘리기 위해 속도 제한을 변경할 수 있습니다. 요금 제한 및 요금 제한이 비즈니스에 미치는 영향에 대한 질문이나 우려 사항은 Braze 지원팀 또는 고객 성공 관리자에게 문의하세요.

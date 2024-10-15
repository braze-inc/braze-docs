---
nav_title: 릴리스 정보
article_title: 릴리스 정보
page_order: 4
layout: dev_guide
guide_top_header: "릴리스 정보"
guide_top_text: "여기에서 Braze 플랫폼의 모든 업데이트를 확인할 수 있으며, <a href='/docs/help/release_notes/#most-recent'>가장 최근의 플랫폼 업데이트</a>는 다음과 같습니다."
page_type: landing
search_rank: 1
description: "이 랜딩 페이지에서는 Braze 릴리즈 노트를 확인할 수 있습니다. 여기에서 Braze 플랫폼과 SDK에 대한 모든 업데이트, 더 이상 사용되지 않는 기능 목록을 확인할 수 있습니다."

guide_featured_title: "릴리스 노트"
guide_featured_list:
  - name: 2024
    link: /docs/help/release_notes/2024/
    image: /assets/img/braze_icons/calendar-check-02.svg
  - name: 2023
    link: /docs/help/release_notes/2023/
    image: /assets/img/braze_icons/calendar-check-02.svg
  - name: 2022
    link: /docs/help/release_notes/2022/
    image: /assets/img/braze_icons/calendar-check-02.svg
  - name: 2021
    link: /docs/help/release_notes/2021/
    image: /assets/img/braze_icons/calendar-check-02.svg
  - name: 2020
    link: /docs/help/release_notes/2020/
    image: /assets/img/braze_icons/calendar-check-02.svg
  - name: 2019
    link: /docs/help/release_notes/2019/
    image: /assets/img/braze_icons/calendar-check-02.svg
  - name: 2018
    link: /docs/help/release_notes/2018/
    image: /assets/img/braze_icons/calendar-check-02.svg
  - name: 2017
    link: /docs/help/release_notes/2017/
    image: /assets/img/braze_icons/calendar-check-02.svg
  - name: 2016
    link: /docs/help/release_notes/2016/
    image: /assets/img/braze_icons/calendar-check-02.svg
  - name: 사용 중단
    link: /docs/help/release_notes/deprecations/
    image: /assets/img/braze_icons/calendar-minus-01.svg
  - name: SDK 변경 로그
    link: /docs/developer_guide/platform_integration_guides/sdk_changelogs/
    image: /assets/img/braze_icons/file-code-01.svg

---

# 최신 Braze 릴리즈 노트 {#most-recent}

> Braze는 주요 제품 출시에 맞춰 한 달 주기로 제품 업데이트에 대한 정보를 공개하지만 매주 기타 개선 사항이 업데이트됩니다.
> <br>
> <br>
> 이 섹션에 나열된 업데이트에 대한 자세한 내용은 계정 관리자에게 문의하거나 [지원 티켓을 개설하세요]({{site.baseurl}}/help/support/). 또한 [SDK 체인지로그에서]({{site.baseurl}}/developer_guide/platform_integration_guides/sdk_changelogs/) 월별 SDK 릴리스, 업데이트 및 개선 사항에 대한 자세한 정보를 확인할 수 있습니다.

## 2024년 7월 23일 출시

### Braze 문서 업데이트

#### Diátaxis 및 Braze 문서

현재 [Diátaxis](https://diataxis.fr/)라는 프레임워크를 사용하여 설명서 표준화하는 작업을 진행 중입니다. 작가와 기여자가 이 새로운 프레임워크에 맞는 콘텐츠를 만들 수 있도록 [각 콘텐츠 유형에 맞는 템플릿을 만들었습니다]({{site.baseurl}}/contributing/content_types).

#### Braze 문서를 위한 새로운 풀-리퀘스트 템플릿

시간을 들여 풀 리퀘스트(PR) 템플릿을 개선하여 더 쉽고 혼란스럽지 않게 [Braze 설명서에 기여하실]({{site.baseurl}}/contributing/home/) 수 있도록 했습니다. 그래도 개선의 여지가 있다고 생각되면 PR을 개설하거나 [이슈를 제출하세요](https://github.com/braze-inc/braze-docs/issues/new?assignees=&labels=enhancement&projects=&template=request_a_feature.md&title=). 모든 게 더 쉬워졌습니다!
 
### 데이터 유연성

#### 사용자 지정 이벤트 및 속성 내보내기

{% multi_lang_include release_type.md release="일반 사용 가능" %}

[`/custom_attributes`]({{site.baseurl}}/api/endpoints/export/custom_attributes/get_custom_attributes) 및 [`/events`]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events_data) API 엔드포인트를 통한 내보내기는 더 이상 얼리 액세스로 제공되지 않습니다.

#### 사용자를 위한 새로운 커런츠 권한

사용자를 위한 두 가지 새로운 권한 설정이 있습니다: **전류 통합 보기** 및 **전류 통합 편집하기**. [여기에서]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions) 사용자 권한에 대해 자세히 알아보세요. 

#### Snowflake 데이터 유지 정책 업데이트
 
8월 27일부터 2년이 지난 모든 Snowflake 보안 데이터 공유 이벤트 데이터에서 개인 식별 정보(PII)가 삭제됩니다. Snowflake를 사용하는 경우 유지 정책이 적용되기 전에 Snowflake 계정에 사본을 저장하여 환경의 전체 이벤트 데이터를 유지하도록 선택할 수 있습니다. 자세히 알아보려면 [Snowflake 데이터 유지]({{site.baseurl}}/partners/data_and_infrastructure_agility/data_warehouses/snowflake/data_retention/)를 참조하세요.
 
### 창의력 발휘

#### 여러 페이지로 구성된 인앱 메시지

{% multi_lang_include release_type.md release="일반 사용 가능" %}

인앱 메시지에 페이지를 추가하면 온보딩 흐름이나 환영 여정과 같은 순차적인 흐름을 통해 사용자를 안내할 수 있습니다. 자세한 내용은 [드래그 앤 드롭으로 인앱 메시지 만들기]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/create#multi-page)를 참조하세요.

#### Liquid를 사용한 링크 단축

{% multi_lang_include release_type.md release="일반 사용 가능" %}

[Liquid를 사용하여 URL을 개인화]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/link_shortening/#enabling-link-shortening)하면 SMS 메시지에 포함된 URL을 자동으로 단축하고 클릭률 분석을 수집할 수 있습니다. 사용해 보려면 [링크 단축을]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/link_shortening/) 참조하세요.

#### 카탈로그용 API 예제

배열 필드를 사용하는 `/catalogs` 엔드포인트에 대한 예제를 추가했습니다. 예시를 보려면 다음을 확인하세요:

- [여러 카탈로그 항목 편집]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/patch_catalog_items_bulk)
- [여러 카탈로그 항목 만들기]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/post_create_catalog_items_bulk)
- [카탈로그 항목 업데이트]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/put_update_catalog_items)
- [카탈로그 항목 편집]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/patch_catalog_item)
- [카탈로그 항목 생성]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/post_create_catalog_item)
- [카탈로그 항목 업데이트]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/put_update_catalog_item)
- [카탈로그 만들기]({{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/post_create_catalog)
 
### 강력한 채널

### 여러 개의 WhatsApp 비즈니스 계정

{% multi_lang_include release_type.md release="일반 사용 가능" %}

이제 각 워크스페이스에 여러 개의 WhatsApp 비즈니스 계정과 구독 그룹(및 전화번호)을 추가할 수 있습니다. 자세한 내용은 [다중 WhatsApp 비즈니스 계정]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/multiple_subscription_groups)을 참조하세요. 

#### SMS 지리적 허용

SMS 지리적 권한은 SMS 메시지를 보낼 수 있는 국가에 대한 제어를 적용하여 보안을 강화하고 사기성 SMS 트래픽으로부터 보호합니다. SMS 메시지를 승인된 지역으로만 보낼 수 있도록 국가 허용 목록을 지정하는 방법을 알아보려면 [SMS 국가 허용 목록 구성하기를]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_geographic_permissions/#configuring-your-sms-country-allowlist) 참조하세요.

#### LINE과 Braze

{% multi_lang_include release_type.md release="베타" %}

[LINE](https://www.lycbiz.com/sites/default/files/media/jp/download/LINE%20Business%20Guide_202310-202403.pdf)은 일본에서 가장 인기 있는 메시징 앱으로, 월간 활성 사용자가 9,500만 명이 넘습니다. LINE 계정을 Braze와 통합하여 자사 및 타사 고객 데이터를 활용하여 고객의 선호도, 행동, 크로스채널 상호 작용을 기반으로 적합한 고객에게 매력적인 LINE 메시지를 보낼 수 있습니다. 시작하려면 [LINE]({{site.baseurl}}/line)을 참조하세요.

#### Shopify: 가격 인하 및 재입고

{% multi_lang_include release_type.md release="조기 액세스" %}

이제 Shopify를 사용하면 [가격 인하]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/price_drop_notifications) 및 [품절 품목에]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/back_in_stock_notifications) 대한 사용자 지정 알림을 생성할 수 있습니다.

 
### AI 및 ML 자동화
 
#### 중복 사용자에 대한 규칙 기반 병합

이전에는 Braze에서 중복 사용자를 개별적으로 또는 일괄적으로 찾아서 병합할 수 있었습니다. 이제 중복 확인 방법을 제어하는 규칙을 만들어 가장 관련성이 높은 사용자를 유지하도록 할 수 있습니다. 자세히 알아보려면 [규칙 기반 병합]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/duplicate_users/#rules-based-merging)을 참조하세요.

#### AI Liquid 어시스턴트

{% multi_lang_include release_type.md release="베타" %}

Sage AI Liquid 어시스턴트는 메시지 콘텐츠를 개인화하는 데 필요한 Liquid를 생성하는 것을 돕는 Sage AI 기반의 채팅 도우미입니다. 템플릿에서 Liquid를 생성하고, 개인화된 Liquid 제안을 받고, Sage AI의 지원을 받아 기존 Liquid를 최적화할 수 있습니다. AI Liquid 도우미는 사용된 Liquid를 설명하는 주석도 제공하므로 Liquid에 대한 이해를 높이고 직접 작성하는 방법을 배울 수 있습니다.

시작하려면 [AI Liquid 어시스턴트]({{site.baseurl}}/user_guide/sage_ai/generative_ai/ai_liquid)를 참조하세요.
 
### SDK
 
#### Android SDK 로그

앱에서 더 쉽게 읽고 사용할 수 있도록 [Braze Android SDK의 로깅 설명서]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/additional_customization_and_configuration/#logging)를 개편했습니다. 또한 각 로그 수준에 대한 설명도 추가했습니다.

#### iOS SDK 포그라운드 푸시 알림

이제 Braze iOS SDK의 `subscribeToUpdates` 메서드가 포그라운드 푸시 알림 수신 여부를 감지할 수 있습니다. 자세히 알아보려면 [iOS 푸시 알림 통합]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration)을 참조하세요.
 
#### Xamarin 문서 업데이트
 
[버전 4.0.0](https://github.com/braze-inc/braze-xamarin-sdk/releases/tag/4.0.0)부터 Braze Xamarin SDK는 Swift SDK 바인딩을 사용하므로 코드 스니펫과 참조 자료를 업데이트했습니다. 또한 읽고 이해하기 쉽도록 섹션을 재구성했습니다. 자세한 내용은 [Xamarin 문서를]({{site.baseurl}}/developer_guide/platform_integration_guides/xamarin/initial_sdk_setup) 참조하세요.

#### SDK 업데이트

다음 SDK 업데이트가 릴리스되었습니다. 주요 업데이트는 아래에 나열되어 있으며, 그 외의 모든 업데이트는 해당 SDK 체인지로그를 확인하면 확인할 수 있습니다.
 
- [Swift SDK 9.3.1](https://github.com/braze-inc/braze-swift-sdk/releases/tag/9.3.1)
- [웹 SDK 5.3.2](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md#532)
    - 5.2.0에서 외부 스크립트가 동기식으로 로드될 때 HTML 인앱 메시지가 잘못 렌더링될 수 있는 회귀 현상을 수정했습니다.
- [웹 SDK 5.4.0](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md#540)

## 2024년 6월 25일 출시

### 일본어 문서

이제 Braze Docs에서 일본어를 지원합니다!

![일본어 인터페이스가 표시된 Braze Docs 사이트]({% image_buster /assets/img/braze-docs-japan.png %}){: style="max-width:70%;"}
 
### 데이터 유연성

#### API 트리거 캠페인용 첨부 파일

{% multi_lang_include release_type.md release="일반 사용 가능" %}

이제 [`/campaigns/trigger/send` 엔드포인트]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns)에서 첨부 파일을 지원합니다(`/messages/send` 엔드포인트에서 이메일의 첨부 파일을 지원하는 것과 유사). 

#### 추가 데이터 웨어하우스 지원

{% multi_lang_include release_type.md release="조기 액세스" %}

이제 Braze [클라우드 데이터 수집(CDI)]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/connected_sources)은 BigQuery, Databricks Redshift 및 Snowflake를 지원합니다.

#### WhatsApp 전화번호 마이그레이션

메타의 임베디드 가입을 사용하여 WhatsApp 비즈니스 계정 간에 WhatsApp 전화번호를 마이그레이션하세요. [WhatsApp 전화번호 마이그레이션]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/phone_number_migration)에 대해 자세히 알아보세요.
 
### 창의력 발휘

#### 기기별 참여

{% multi_lang_include release_type.md release="일반 사용 가능" %}

새로운 **디바이스별 참여도** 보고서에서는 사용자가 이메일에 참여하는 데 사용하는 디바이스에 대한 분석 정보를 제공합니다. 이 데이터는 모바일, 데스크톱, 태블릿 및 기타 기기 유형에서 이메일 인게이지먼트를 추적합니다. [보고서와 이메일 성능 대시보드]({{site.baseurl}}/user_guide/data_and_analytics/analytics/email_performance_dashboard)에 대해 자세히 알아보세요.

#### 캔버스 흐름의 WhatsApp 및 SMS Liquid 속성

{% multi_lang_include release_type.md release="일반 사용 가능" %}

[캔버스 플로우에 WhatsApp 및 SMS Liquid 속성]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties)에 대한 지원을 추가했습니다. 이제 행동 경로 단계에 "SMS 인바운드 메시지 보내기" 또는 "WhatsApp 인바운드 메시지 보내기" 트리거가 포함된 경우 후속 캔버스 단계에 SMS 또는 WhatsApp Liquid 속성정보를 포함할 수 있습니다. 이는 캔버스 플로우에서 이벤트 속성정보가 작동하는 방식을 반영합니다. 이렇게 하면 메시지를 활용하여 사용자 프로필 및 대화 메시지에 대한 퍼스트 파티 데이터를 저장하고 참조할 수 있습니다.
 
#### 반복 캔버스의 개인화된 경로

{% multi_lang_include release_type.md release="조기 액세스" %}

캔버스에서 개인화된 경로를 사용하면 전환 가능성에 따라 개별 사용자에 대한 캔버스 여정의 모든 지점을 개인화할 수 있습니다. 이제 반복 캔버스에 개인화된 경로를 사용할 수 있습니다. [개인화된 이형]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step/personalized_paths) 상품에 대해 자세히 알아보세요.

#### 세그먼트 문제 해결

세그먼트로 작업하시나요? 다음은 몇 가지 [문제 해결 단계 및 유의해야 할 사항]({{site.baseurl}}/user_guide/engagement_tools/segments/troubleshooting)입니다.

#### 리퀴드 하이라이트

접근성 가이드라인을 더 잘 지원하기 위해 [Liquid에서 사용하는 색상 코딩을]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid) 개선했습니다.

![]({% image_buster /assets/img/liquid_color_code.png %})
 
### 강력한 채널

#### SMS 지리적 권한

{% multi_lang_include release_type.md release="조기 액세스" %}

SMS 지리적 권한은 SMS 메시지를 보낼 수 있는 국가에 대한 제어를 적용하여 보안을 강화하고 사기성 SMS 트래픽으로부터 보호합니다. 이제 관리자는 허용 국가 목록을 지정하여 SMS 메시지가 승인된 지역으로만 전송되도록 할 수 있습니다. 자세한 내용은 [SMS 지리적 권한에서]({{site.baseurl}}/sms_geographic_permissions) 확인하세요. 

![가장 일반적인 국가가 상단에 표시되는 '국가 허용 목록' 드롭다운.]({% image_buster /assets/img/sms/allowlist_dropdown.png %}){: style="max-width:80%;"}

#### SMS/MMS 모범 사례

수신 거부 모니터링 및 트래픽 펌핑에 대한 권장 사항을 포함하여 [Braze를 사용한 SMS/MMS 모범 사례에]({{site.baseurl}}/user_guide/message_building_by_channel/sms/best_practices/best_practices) 대해 자세히 알아보세요. 

#### 푸시 수신 거부 추적 기술

새로운 [도움말 문서]({{site.baseurl}}/help/help_articles/push/push_unsubscribes)에서 푸시 수신 거부 추적 기술에 대한 몇 가지 팁을 확인하세요.

#### Shopify `checkout.liquid` 사용 중단

Shopify `checkout.liquid`에 대한 지원은 2024년 8월에 지원 중단이 시작되어 2025년 8월에 종료됩니다. Braze가 [이 전환을 어떻게 처리할지]({{site.baseurl}}/help/release_notes/deprecations/shopify_checkout) 자세히 알아보세요. 

### SDK 업데이트
 
다음 SDK 업데이트가 릴리스되었습니다. 주요 업데이트는 아래에 나열되어 있으며, 그 외의 모든 업데이트는 해당 SDK 체인지로그를 확인하면 확인할 수 있습니다.
 
- [Swift SDK 9.3.0](https://github.com/braze-inc/braze-swift-sdk/releases/tag/9.3.0)
    - 기존 기능 플래그 API를 더 이상 사용하지 않으며, 향후 버전에서 제거될 예정입니다.
        - `Braze.FeatureFlag.jsonStringProperty(key:)` 는 더 이상 사용되지 않습니다.
        - `Braze.FeatureFlag.jsonObjectProperty(key:)`는 `Braze.FeatureFlag.jsonProperty(key:)`를 위해 더 이상 사용되지 않습니다.
- [Roku SDK 2.2.0](https://github.com/braze-inc/braze-roku-sdk/blob/main/CHANGELOG.md)
- [Braze Expo 플러그인 2.1.2](https://github.com/braze-inc/braze-expo-plugin/blob/main/CHANGELOG.md)

#### tvOS 문서

몇 달 전, 실수로 [tvOS 콘텐츠 카드]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/content_cards/tvos) 및 [인앱 메시징]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/in-app_messaging/customization/tvos)에 대한 설명서가 더 이상 사용되지 않게 되었습니다. 이 설명서는 이제 Braze 문서의 Swift 섹션에 다시 게시되었습니다.

{% alert note %}
Braze 설명서의 [기여자]({{site.baseurl}}/contributing/home)는 이제 사이트가 Ruby 3.3.0에서 실행된다는 점에 유의하세요. 필요에 따라 Ruby 버전을 업그레이드하세요.
{% endalert %}

## 2024년 5월 28일 출시

### 문서 사이트의 시각적 업데이트

문서 웹사이트가 멋지게 바뀐 것을 눈치채셨을 것입니다! 새롭고 활기찬 Braze의 브랜드 아이덴티티를 반영하여 개편했습니다. 새 브랜드에 대한 비하인드 스토리는 [새 브랜드 공개에서 자세히 알아보세요: Braze 수석 크리에이티브 디렉터 그렉 에르델레이와의 대화](https://www.braze.com/resources/articles/unveiling-our-new-brand-a-conversation-with-braze-executive-creative-director-greg-erdelyi).

### 포르투갈어 및 스페인어 지원

{% multi_lang_include release_type.md release="일반 사용 가능" %}

이제 Braze를 포르투갈어와 스페인어로 이용할 수 있습니다. Braze 대시보드가 표시되는 언어를 변경하려면 [언어 설정]({{site.baseurl}}/user_guide/administrative/access_braze/language/)을 참조하세요.

### 강력한 채널

#### 다국어 설정

{% multi_lang_include release_type.md release="일반 사용 가능" %}

[다국어 설정]({{site.baseurl}}/multi_language_support/)을 조정하면 하나의 이메일 메시지 내에서 서로 다른 언어와 위치의 사용자를 대상으로 서로 다른 메시지를 보낼 수 있습니다. 다국어 지원을 편집하고 관리하려면 "다국어 설정 관리" 사용자 권한이 있어야 합니다. 메시지에 로캘을 추가하려면 캠페인을 편집할 수 있는 권한이 필요합니다.

#### 메시지 수준의 원클릭 목록-수신 취소 헤더

{% multi_lang_include release_type.md release="일반 사용 가능" %}

목록 수신 거부 헤더([RFC 8058](https://datatracker.ietf.org/doc/html/rfc8058))의 원클릭 수신 거부 기능은 수신자가 이메일을 쉽게 수신 거부할 수 있는 방법을 제공합니다. 이 헤더 설정을 이메일의 메시지 수준에서 적용하도록 조정할 수 있습니다. 이 설정에 대한 자세한 내용은 [워크스페이스의 이메일 수신 거부 헤더]({{site.baseurl}}/user_guide/administrative/app_settings/email_settings/#email-unsubscribe-header-in-workspaces)를 참조하세요.

#### 이메일 살균 정보

Braze가 이메일 메시지에서 특정 유형의 JavaScript를 감지할 때 발생하는 프로세스에 대해 자세히 알아보려면 새로운 [위생 처리]({{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices/sanitization) 문서를 참조하세요. 주요 목적은 악의적인 공격자가 다른 Braze 대시보드 사용자의 세션 데이터에 액세스하는 것을 방지하는 것입니다.

#### 콘텐츠 블록의 포함 횟수

활성 캠페인 또는 캔버스에 콘텐츠 블록을 추가한 후 콘텐츠 블록을 마우스로 가리키고 <i class="fa fa-eye preview-icon"></i> **미리보기** 아이콘을 선택하면 콘텐츠 블록 라이브러리에서 [이 콘텐츠 블록을 미리 볼]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/content_blocks/) 수 있습니다.

#### 캔버스 상태

Braze 대시보드에서 캔버스는 상태별로 그룹화되어 있습니다. 다양한 [캔버스 상태와]({{site.baseurl}}/user_guide/engagement_tools/canvas/get_started/canvas_status) 그 의미에 대한 [설명을]({{site.baseurl}}/user_guide/engagement_tools/canvas/get_started/canvas_status) 확인하세요.

### AI 및 ML 자동화

#### AI 카피라이팅 어시스턴트를 위한 브랜드 가이드라인

{% multi_lang_include release_type.md release="일반 사용 가능" %}

이제 [브랜드 가이드라인]({{site.baseurl}}/user_guide/sage_ai/generative_ai/ai_copywriting/brand_guidelines/)을 생성하고 적용하여 AI 카피라이팅 어시스턴트가 생성한 카피 스타일을 브랜드에 맞게 맞춤 설정할 수 있습니다. 다양한 시나리오에 대해 여러 가지 가이드라인을 설정하여 항상 상황에 맞는 어조를 유지할 수 있습니다.
 
### 새로운 Braze 파트너십

#### Adikteev - 애널리틱스

Braze와 [Adikteev의]({{site.baseurl}}/partners/data_and_infrastructure_agility/analytics/adikteev/) 통합을 통해 Braze CRM 캠페인 내에서 Adikteev의 이탈 예측 기술을 활용하여 고위험 사용자 세그먼트를 우선적으로 타겟팅함으로써 사용자 유지율을 높일 수 있습니다.
 
#### Celebrus - 애널리틱스
 
Braze와 [Celebrus]({{site.baseurl}}/partners/data_and_infrastructure_agility/analytics/celebrus) 통합은 웹 및 모바일 앱 채널 전반에서 Braze SDK와 원활하게 통합되어 채널 활동 데이터로 Braze의 인구를 늘리는 데 도움이 됩니다. 여기에는 지정된 기간 동안 디지털 자산 전반의 방문자 트래픽에 대한 포괄적인 인사이트가 포함됩니다.
 
#### IAM Studio - 메시지 템플릿
 
Braze와 [IAM Studio의]({{site.baseurl}}/partners/message_orchestration/channel_extensions/email_templates/iam_studio/) 통합을 통해 이미지 교체, 텍스트 수정, 딥링크 설정, 사용자 지정 속성 및 이벤트 설정을 제공하는 사용자 지정 가능한 인앱 메시지 템플릿을 Braze 인앱 메시지에 쉽게 삽입할 수 있습니다. IAM Studio를 사용하면 메시지 제작 시간을 단축하고 콘텐츠 기획에 더 많은 시간을 할애할 수 있습니다.
 
#### Regal - 인스턴트 채팅

Braze와 [Regal]({{site.baseurl}}/partners/message_orchestration/additional_channels/messaging/regal/)을 통합하면 모든 고객 터치포인트에서 보다 일관되고 개인화된 경험을 제공할 수 있습니다.

#### Treasure Data - 코호트 가져오기
 
Braze와 [Treasure Data]({{site.baseurl}}/partners/data_and_infrastructure_agility/cohort_import/treasuredata/) 통합을 통해 사용자 코호트를 Treasure Data에서 Braze로 가져올 수 있으므로, 웨어하우스에만 존재할 수 있는 데이터를 기반으로 타겟팅 캠페인을 보낼 수 있습니다.
 
#### Zapier - 워크플로 자동화
 
Braze와 [Zapier의]({{site.baseurl}}/partners/data_and_infrastructure_agility/workflow_automation/zapier/) 파트너십은 Braze API와 Braze 웹훅을 활용하여 타사 애플리케이션과 연결하여 다양한 작업을 자동화합니다.

### SDK 업데이트
 
다음 SDK 업데이트가 릴리스되었습니다. 주요 업데이트는 아래에 나열되어 있으며, 그 외의 모든 업데이트는 해당 SDK 체인지로그를 확인하면 확인할 수 있습니다.

- [Android SDK 31.0.0](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md)
- [Braze 세그먼트 Swift 플러그인 3.0.0](https://github.com/braze-inc/braze-segment-swift/blob/main/CHANGELOG.md#300)
    - 9.2.0+ SemVer 버전 이상의 릴리스가 필요하도록 Braze Swift SDK 바인딩을 업데이트합니다.
        - 이를 통해 9.2.0부터 10.0.0까지 모든 버전의 Braze SDK와 호환됩니다(단, 10.0.0은 포함되지 않음).
        - 잠재적인 변경 사항에 대한 자세한 내용은 [7.0.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#700), [8.0.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#800) 및 [9.0.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#900)의 체인지로그 항목을 참조하세요.
    - 이제 푸시 알림을 지원하려면 앱 수명 주기 초기에 애플리케이션의 `AppDelegate.application(_:didFinishLaunchingWithOptions:)` 메서드에서 정적 메서드 `BrazeDestination.prepareForDelayedInitialization()`을 호출해야 합니다.
- [Cordova SDK 9.0.0-9.2.0](https://github.com/braze-inc/braze-cordova-sdk/blob/master/CHANGELOG.md)
    - [Braze Swift SDK 7.7.0에서 9.0.0으로](https://github.com/braze-inc/braze-swift-sdk/compare/7.7.0...9.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed) 네이티브 iOS 브릿지를 업데이트했습니다.
- [Expo 플러그인 2.1.1](https://github.com/braze-inc/braze-expo-plugin/blob/main/CHANGELOG.md#211)
- [Flutter SDK 10.1.0](https://pub.dev/packages/braze_plugin/changelog)
- [React Native SDK 11.0.0](https://github.com/braze-inc/braze-react-native-sdk/blob/11.0.0/CHANGELOG.md)
- [Swift SDK 9.1.0-9.2.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#920)
- Unity 6.0.0
    - [Braze Swift SDK 7.7.0에서 9.0.0으로](https://github.com/braze-inc/braze-swift-sdk/compare/7.7.0...9.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed) 네이티브 iOS 브릿지를 업데이트했습니다.
    - 네이티브 Android 브릿지를 [Braze Android SDK 29.0.1에서 30.3.0으로](https://github.com/braze-inc/braze-android-sdk/compare/v29.0.1...v30.3.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed) 업데이트했습니다.
- [웹 SDK 5.3.1](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md)
- Xamarin SDK 버전 5.0.0
    - [Braze Swift SDK 8.4.0에서 9.0.0으로](https://github.com/braze-inc/braze-swift-sdk/compare/8.4.0...9.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed) iOS 바인딩을 업데이트했습니다.

## 2024년 4월 30일 출시

### 프로모션 코드 목록을 생성하거나 업데이트할 수 있는 권한

2024년 4월부터 사용자는 프로모션 코드 목록을 만들거나 업데이트하려면 '캠페인, 캔버스, 카드, 세그먼트, 미디어 라이브러리에 액세스' 권한이 필요합니다. 권한 이름과 설명에 대한 목록은 [제한된 권한 및 팀 역할 권한 관리하기]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#managing-limited-and-team-role-permissions)를 참조하세요.

### 데이터 유연성

#### SAML 적시 프로비저닝

{% multi_lang_include release_type.md release="조기 액세스" %}

[적시 프로비저닝은 SAML SSO와 함께 작동하여 새로운 대시보드 사용자가 처음 로그인할 때 Braze 계정을 만들 수 있도록 합니다. 따라서 관리자가 새 대시보드 사용자의 계정을 수동으로 만들고, 권한을 선택하고, 워크스페이스에 할당하고, 사용자가 계정을 활성화할 때까지 기다릴 필요가 없습니다.

#### 권한 집합 및 역할

[권한 세트]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#permission-sets-and-roles)를 사용하여 특정 주제 영역 또는 작업과 관련된 권한을 묶을 수 있습니다. 이러한 권한 집합은 여러 워크스페이스에서 동일한 액세스 권한이 필요한 대시보드 사용자에게 적용할 수 있습니다.

#### 클라우드 데이터 수집 세그먼트

Braze [클라우드 데이터 수집 세그먼트를]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/cdi_segments) 사용하면 CDI 연결을 통해 제공되는 데이터를 사용하여 자체 데이터 웨어하우스에 직접 쿼리하는 SQL을 작성하고, Braze 내에서 타겟팅할 수 있는 사용자 그룹을 만들 수 있습니다.

### 창의력 발휘

### 쿼리 빌더 템플릿

{% multi_lang_include release_type.md release="일반 사용 가능" %}

쿼리 빌더 템플릿을 사용하면 Snowflake의 Braze 데이터를 사용하여 보고서를 만들 수 있습니다. [쿼리 빌더]({{site.baseurl}}/user_guide/data_and_analytics/query_builder/) 템플릿에 액세스하려면 보고서를 만들 때 **쿼리 템플릿**을 선택합니다. 모든 템플릿은 최대 최근 60일까지의 데이터를 표시하지만 편집기에서 해당 값과 다른 값을 직접 편집할 수 있습니다.

### 세그먼트별 성능 데이터

{% multi_lang_include release_type.md release="일반 사용 가능" %}

캠페인, 배리언트, 캔버스 및 세그먼트별 캔버스 단계에 대한 쿼리 빌더 보고서 템플릿에서 [성과 데이터]({{site.baseurl}}/user_guide/data_and_analytics/reporting/viewing_and_understanding_segment_data/#performance-data-by-segment)를 세그먼트별로 분류할 수 있습니다.

### 강력한 채널

#### SMS 메시징을 위한 자동 링크 단축

{% multi_lang_include release_type.md release="일반 사용 가능" %}

[자동 링크 단축을]({{site.baseurl}}/user_guide/message_building_by_channel/sms/keywords/keyword_handling/?tab=manage%20responses#managing-keywords-and-auto-responses) 사용하여 응답에서 정적 URL을 자동으로 단축할 수 있습니다. 이렇게 하면 문자 카운터가 단축된 URL의 예상 길이를 표시하도록 업데이트되므로 응답을 구체화하는 데 도움이 될 수 있습니다.

### 새로운 Braze 파트너십

#### Friendbuy - 로열티

Braze와 [Friendbuy의]({{site.baseurl}}/partners/message_orchestration/channel_extensions/loyalty/friendbuy/) 통합을 활용하여 이메일 및 SMS 기능을 확장하는 동시에 추천 및 로열티 프로그램 커뮤니케이션을 손쉽게 자동화할 수 있습니다. Braze는 Friendbuy를 통해 수집된 모든 옵트인 전화번호에 대한 고객 프로필을 생성합니다.

### NiftyImages - 동적 콘텐츠

Braze와 [NiftyImages]({{site.baseurl}}/partners/message_personalization/dynamic_content/niftyimages/)의 파트너십을 통해 기존 Braze 개인화된 태그를 NiftyImages URL에 매핑하여 이메일 캠페인을 위한 역동적인 개인화 이미지를 만들 수 있습니다.

### SDK 업데이트

다음 SDK 업데이트가 릴리스되었습니다. 주요 업데이트는 아래에 나열되어 있으며, 그 외의 모든 업데이트는 해당 SDK 체인지로그를 확인하면 확인할 수 있습니다.

- [Android SDK 30.4.0](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md)
- [Braze 세그먼트 Swift 플러그인 2.4.0](https://github.com/braze-inc/braze-segment-swift/blob/main/CHANGELOG.md#240)
- [Flutter SDK 9.0.0](https://pub.dev/packages/braze_plugin/changelog)
    - 네이티브 iOS 브릿지를 [Braze Swift SDK 7.7.0에서 8.4.0으로](https://github.com/braze-inc/braze-swift-sdk/compare/7.7.0...8.4.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed) 업데이트합니다.
        - 최소 iOS 배포 대상이 12.0으로 업데이트되었습니다.
    - 네이티브 Android 브릿지를 [Braze Android SDK 29.0.1에서 30.3.0으로](https://github.com/braze-inc/braze-android-sdk/compare/v29.0.1...v30.3.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed) 업데이트합니다.
    - 지원되는 최소 Dart 버전은 2.15.0입니다.
- [React Native SDK 9.2.0](https://github.com/braze-inc/braze-react-native-sdk/blob/master/CHANGELOG.md)
- [Swift SDK 8.3.0-8.4.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md)
- [Swift SDK 9.0.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md)
    - BrazeKit 개인정보 매니페스트에서 기본 개인정보 추적 도메인을 제거합니다.
        - Braze [데이터 추적 기술 기능]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/privacy_manifest/)을 사용하는 경우, 앱 수준의 개인정보 매니페스트에 추적 기술 엔드포인트를 수동으로 추가해야 합니다.
        - 통합 지침은 업데이트된 [튜토리얼](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/e1-privacy-tracking)을 참조하세요.
    - 더 이상 사용되지 않는 `BrazeDelegate.braze(_:sdkAuthenticationFailedWithError) method in favor of BrazeSDKAuthDelegate.braze(_:sdkAuthenticationFailedWithError)` 을 제거합니다.
        - 이 방법은 원래 [릴리스 5.14.0](https://github.com/braze-inc/braze-swift-sdk/releases/tag/5.14.0)에서 더 이상 사용되지 않았습니다.
        - 새 델리게이트 메서드로 전환하지 않으면 컴파일러 오류가 트리거되지 않고 정의한 `BrazeDelegate.braze(_:sdkAuthenticationFailedWithError)` 메서드가 호출되지 않을 뿐입니다.
- [Xamarin SDK 버전 4.0.3](https://github.com/braze-inc/braze-xamarin-sdk/blob/master/CHANGELOG.md#403)

## 2024년 4월 2일 출시

### WhatsApp

#### 여러 비즈니스 계정

이제 각 워크스페이스에 여러 개의 WhatsApp 비즈니스 계정과 구독 그룹을 추가할 수 있습니다. 전체 안내는 [여러 개의 WhatsApp 비즈니스 계정 및 전화번호]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/multiple_subscription_groups/)를 참조하세요.

#### 읽기 속도

WhatsApp은 인도의 소비자들을 시작으로 보다 가치 있는 경험을 제공하고 기업의 마케팅 대화 참여를 극대화하기 위해 새로운 접근 방식을 테스트하고 있습니다. 여기에는 특정 기간 동안 특정 비즈니스에서 개인이 받는 마케팅 대화 수를 제한하는 것이 포함될 수 있으며, 읽을 가능성이 적은 소수의 대화부터 시작합니다. 자세한 내용은 [메타 리소스를]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/meta_resources/) 참조하세요.

### 데이터 유연성

#### Amazon S3 버킷을 Braze에 동기화하기

{% multi_lang_include release_type.md release="조기 액세스" %}

이제 S3용 클라우드 데이터 수집을 사용하여 AWS 계정에 있는 하나 이상의 S3 버킷을 Braze와 직접 통합할 수 있습니다. 새 파일이 S3에 게시되면 SQS에 메시지가 게시되고 Braze 클라우드 데이터 수집이 해당 새 파일을 받습니다. 자세한 내용은 [파일 스토리지 통합]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/file_integrations/)을 참조하세요.

#### Shopify OAuth

{% multi_lang_include release_type.md release="일반 사용 가능" %}

Shopify는 모든 규모의 소매 비즈니스를 시작, 성장, 마케팅 및 관리할 수 있는 신뢰할 수 있는 도구를 제공하는 선도적인 글로벌 상거래 기업입니다. 이제 Braze용 Shopify를 설정할 때 [워크스페이스에 OAuth를 사용하도록]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/setting_up_shopify/) 설정할 수 있습니다.

#### iOS용 Expo 푸시 알림 사용

React Native와 함께 Expo를 사용하여 iOS 앱에 리치 푸시 알림 및 푸시 스토리를 통합하는 [방법을 추가했습니다]({{site.baseurl}}/developer_guide/platform_integration_guides/react_native/push_notifications/?tab=expo).

#### iOS 라이브 활동 원격 시작

이제 [`/messages/live_activity/start`]({{site.baseurl}}/api/endpoints/messaging/live_activity/start/) 엔드포인트를 사용하여 iOS에서 라이브 활동을 원격으로 시작할 수 있습니다. 전체 안내는 [라이브 활동: ]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/live_activities/live_activities/#step-2-start-the-activity) 활동 시작을 참고하세요.

### AI 및 ML 자동화

#### 항목 추천

{% multi_lang_include release_type.md release="조기 액세스" %}

이제 Braze의 Sage AI를 사용하면 가장 인기 있는 제품을 계산하거나 특정 카탈로그에 대한 개인화된 AI 추천을 생성할 수 있습니다. 자세한 내용은 [항목 추천 정보를]({{site.baseurl}}/user_guide/sage_ai/recommendations/about_item_recommendations/) 참조하세요.

#### QA 인앱 메시지 콘텐츠

{% multi_lang_include release_type.md release="일반 사용 가능" %}

이전에는 Braze 대시보드에서 Sage AI를 사용하여 SMS 및 푸시 알림 콘텐츠에 대한 품질 보증을 수행할 수 있었습니다. 이제 [인앱 메시지 콘텐츠도 QA할]({{site.baseurl}}/user_guide/sage_ai/generative_ai/ai_content_qa/) 수 있습니다.

### 새로운 Braze 파트너십

#### 인구조사 - 코호트 가져오기

이제 Snowflake, BigQuery와 같은 클라우드 데이터 웨어하우스를 Braze에 연결하는 데이터 활성화 플랫폼인 [Census로 코호트 사용자를 가져올]({{site.baseurl}}/partners/data_and_infrastructure_agility/cohort_import/census/) 수 있습니다. 마케팅 팀은 퍼스트 파티 데이터를 활용하여 동적 오디언스 세그먼트를 구축하고, 고객 속성을 동기화하여 캠페인을 맞춤화하며, Braze의 모든 데이터를 최신 상태로 유지할 수 있습니다.

### SDK 업데이트

다음 SDK 업데이트가 릴리스되었습니다. 주요 업데이트는 아래에 나열되어 있으며, 그 외의 모든 업데이트는 해당 SDK 체인지로그를 확인하면 확인할 수 있습니다.

- [React Native 9.1.0](https://github.com/braze-inc/braze-react-native-sdk/blob/master/CHANGELOG.md)
  - React Native 최소 버전을 0.71.0으로 업데이트했습니다.
  - iOS 최소 버전을 12.0으로 업데이트했습니다.
  - Braze Swift SDK 8.1.0을 사용하도록 iOS 바인딩을 업데이트했습니다.
  - Braze Android SDK 30.1.1을 사용하도록 Android 바인딩을 업데이트했습니다.

## 2024년 3월 5일 출시

### Google EU 사용자 동의 정책

Google은 2024년 3월 6일부터 시행되는 [디지털 시장법(DMA)](https://ads-developers.googleblog.com/2023/10/updates-to-customer-match-conversion.html) 개정 사항에 따라 [EU 사용자 동의 정책](https://www.google.com/about/company/user-consent-policy/)을 업데이트하고 있습니다. 이 새로운 변경 사항에 따라 광고주는 EEA 및 영국 최종 사용자에게 특정 정보를 공개하고 해당 사용자로부터 필요한 동의를 얻어야 합니다. 곧 변경될 사항의 일환으로, [Braze에서 두 동의 신호를 모두 커스텀 속성으로 수집]({{site.baseurl}}/partners/canvas_steps/google_audience_sync/#collecting-consent-for-eea-and-uk-end-users)할 수 있습니다. Braze는 이러한 커스텀 속성의 데이터를 Google의 적절한 동의 필드에 동기화합니다.

### 데이터 유연성

#### 중복 사용자 병합

{% multi_lang_include release_type.md release="조기 액세스" %}

이제 Braze 대시보드에서 [중복 사용자를 검색하고 병합하여]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/duplicate_users) 캠페인과 캔버스의 효과를 극대화할 수 있습니다. 사용자 프로필을 개별적으로 병합하거나 식별자가 일치하는 모든 프로필을 가장 최근에 업데이트된 사용자 프로필로 병합하는 일괄 병합을 수행할 수 있습니다.

#### 보관된 콘텐츠 검색

이제 Braze 대시보드에서 **아카이브된 콘텐츠 표시**를 선택하여 [검색 결과에 아카이브된 콘텐츠]({{site.baseurl}}/user_guide/administrative/access_braze/global_search/#filter-for-archived-content)를 포함할 수 있습니다.

#### AWS S3 및 Google Cloud Storage에 대한 메시지 아카이빙 지원

[메시지 보관을]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/message_archiving/) 사용하여 보관 또는 규정 준수 목적으로 사용자에게 보낸 메시지의 사본을 AWS S3 버킷, Azure Blob Storage 컨테이너 또는 Google Cloud Storage 버킷에 저장할 수 있습니다.

#### SQL 테이블 참조

쿼리 빌더에서 또는 SQL 세그먼트 확장을 생성할 때 쿼리할 수 있는 테이블과 열을 보려면 [SQL 테이블 참조]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/sql_segments_tables/)를 방문하세요.

### 창의력 발휘

#### AI 카피라이팅을 위한 톤 제어

이제 AI 카피라이팅 어시스턴트로 생성된 카피의 스타일을 결정하기 위해 [메시지 톤]({{site.baseurl}}/user_guide/sage_ai/generative_ai/ai_copywriting/#steps)을 선택할 수 있습니다.

### 강력한 채널

#### 카드 생성

카드 [생성]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/create/card_creation/) 시기를 지정하여 Braze가 새 콘텐츠 카드 캠페인 및 캔버스 단계에 대한 오디언스 자격 및 개인화를 평가하는 시기를 선택할 수 있습니다. 

#### 사용자 경로 미리보기

{% multi_lang_include release_type.md release="일반 사용 가능" %}

사용자가 받게 될 메시지와 타이밍을 미리 보는 등 사용자를 위해 만든 캔버스 여정을 경험해 보세요. 이러한 [테스트 실행]({{site.baseurl}}/preview_user_paths/)은 캔버스를 보내기 전에 메시지가 올바른 오디언스에게 전송되는지 확인하는 품질 보증 역할을 합니다.

#### 빠른 푸시 캠페인

{% multi_lang_include release_type.md release="일반 사용 가능" %}

Braze에서 푸시 캠페인을 만들 때 여러 플랫폼과 기기를 선택하여 [퀵 푸시]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/quick_push/)라는 단일 편집 환경에서 모든 플랫폼에 하나의 메시지를 작성할 수 있습니다. 이 기능은 캠페인에만 사용할 수 있습니다.

#### 사용자 지정 List-Unsubscribe 헤더

{% multi_lang_include release_type.md release="일반 사용 가능" %}

이메일 메시징에 [커스텀 목록 수신 거부 헤더]({{site.baseurl}}/user_guide/administrative/app_settings/email_settings/#custom-list-unsubscribe-header)를 추가하면 수신자가 수신 거부할 수 있습니다. 이렇게 하면 직접 구성한 원클릭 수신 거부 엔드포인트와 선택 사항인 "mailto:"를 추가할 수 있습니다. 원클릭 수신 거부 HTTP는 대량 발신자에 대한 Yahoo 및 Gmail의 요구 사항이므로 Braze는 커스텀 목록 수신 거부 헤더를 지원하기 위해 URL을 입력해야 합니다.

#### 인앱 메시지를 위한 여러 페이지

{% multi_lang_include release_type.md release="조기 액세스" %}

[인앱 메시지에 페이지를 추가하면]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/create/#multi-page) 온보딩 흐름이나 환영 여정과 같은 순차적인 흐름을 통해 사용자를 안내할 수 있습니다. **빌드** 탭의 **페이지** 섹션에서 페이지를 관리할 수 있습니다.

#### 실험 경로에 대한 경로 무작위화

실험 경로 단계의 [경로 할당을 항상 무작위로 지정]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step)하려면 단계의 **실험 경로에서 무작위 경로를** 선택합니다. 이 옵션은 위닝 또는 개인화된 경로를 사용할 때는 사용할 수 없습니다.

#### 이메일 캡처 양식

[이메일 캡처 메시지를]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/customize/email_capture_form/) 사용하면 사이트 사용자에게 이메일 주소를 제출하라는 메시지를 쉽게 보낼 수 있으며, 이후에는 모든 메시징 캠페인에서 사용할 수 있도록 사용자 프로필에서 해당 주소를 사용할 수 있습니다.

### SDK 업데이트
 
다음 SDK 업데이트가 릴리스되었습니다. 주요 업데이트는 아래에 나열되어 있으며, 그 외의 모든 업데이트는 해당 SDK 체인지로그를 확인하면 확인할 수 있습니다.

- [AppboyKit iOS SDK 4.7.0](https://github.com/Appboy/appboy-ios-sdk/releases/tag/4.7.0)
    - 이는 2024년 3월 1일([Swift SDK](https://github.com/braze-inc/braze-swift-sdk/) 사용을 위해) 서비스 종료 이전에 Objective-C SDK의 마지막 릴리스가 될 것입니다.
    - SDWebImage의 최소 요구 버전을 5.8.2에서 5.18.7로 업데이트합니다. 이 버전에는 [개인정보에 영향을 미치는 SDK 목록](https://developer.apple.com/support/third-party-SDK-requirements/)에 표시되는 SDWebImage에 대한 개인정보 매니페스트가 포함되어 있습니다.
- [Flutter SDK 8.1.0](https://pub.dev/packages/braze_plugin/changelog)
- [Unity 5.2.0](https://github.com/braze-inc/braze-unity-sdk/blob/master/CHANGELOG.md)
- [React Native SDK 8.4.0](https://github.com/braze-inc/braze-react-native-sdk/blob/8.4.0/CHANGELOG.md)
- [Xamarin SDK 버전 4.0.2](https://github.com/braze-inc/braze-xamarin-sdk/blob/master/CHANGELOG.md)
- [Swift SDK 7.7.0-8.0.1](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#801)
- [Android SDK 30.1.0-30.2.0](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md)
- [웹 SDK 5.1.1](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md)
- [Cordova SDK 8.0.0-Cordova SDK 8.1.0](https://github.com/braze-inc/braze-cordova-sdk/blob/master/CHANGELOG.md)
    - 네이티브 Android 브릿지를 [Braze Android SDK 27.0.1에서 30.0.0으로](https://github.com/braze-inc/braze-android-sdk/compare/v27.0.0...v30.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed) 업데이트했습니다.
    - [Braze Swift SDK 6.6.0에서 7.6.0으로](https://github.com/braze-inc/braze-swift-sdk/compare/6.6.0...7.6.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed) 네이티브 iOS 브릿지를 업데이트했습니다.
    - `Banner` 콘텐츠 카드 유형 이름을 `ImageOnly` 으로 변경했습니다:
        - `ContentCardTypes.BANNER`부터 `ContentCardTypes.IMAGE_ONLY`까지
        - Android에서 프로젝트의 XML 파일에 콘텐츠 카드용 배너라는 단어가 포함된 경우 `image_only`로 대체해야 합니다.
    - `BrazePlugin.getFeatureFlag(id)`는 이제 기능 플래그가 존재하지 않으면 `null`을 반환합니다.
    - `BrazePlugin.subscribeToFeatureFlagsUpdates(function)`는 새로 고침 요청이 성공 또는 실패로 완료된 경우와 현재 세션에서 이전에 캐시된 데이터가 있는 경우 최초 구독 시에만 트리거됩니다.
    - 더 이상 사용되지 않는 메서드 `registerAppboyPushMessages` 를 제거했습니다. 대신 `setRegisteredPushToken` 을 사용하세요.

## 2024년 2월 6일 출시

### Braze 프라이버시 매니페스트

Braze는 신고된 추적 기술 데이터를 전용 `-tracking` 엔드포인트로 자동 리라우팅하는 유연한 새 API와 함께 자체 개인정보처리방침을 공개했습니다. 자세한 내용은 [Braze 개인정보취급방침]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/privacy_manifest)을 참조하세요.

### Google EU 사용자 동의 정책

Google은 2024년 3월 6일부터 시행되는 [디지털 시장법(DMA)](https://ads-developers.googleblog.com/2023/10/updates-to-customer-match-conversion.html)의 변경사항에 따라 [EU 사용자 동의 정책](https://www.google.com/about/company/user-consent-policy/)을 업데이트합니다. 이 새로운 변경 사항에 따라 광고주는 EEA 및 영국 최종 사용자에게 특정 정보를 공개하고 해당 사용자로부터 필요한 동의를 얻어야 합니다. 곧 변경될 사항의 일환으로, [Braze에서 두 동의 신호를 모두 커스텀 속성으로 수집]({{site.baseurl}}/partners/canvas_steps/google_audience_sync/#collecting-consent-for-eea-and-uk-end-users)할 수 있습니다. Braze는 이러한 커스텀 속성의 데이터를 Google의 적절한 동의 필드에 동기화합니다.

### 데이터 유연성

#### Google 파이어베이스 클라우드 메시징(FCM) API

{% multi_lang_include release_type.md release="일반 사용 가능" %}

이제 [더 이상 사용되지 않는 Google의 클라우드 메시징 API에서 완전히 지원되는 Firebase 클라우드 메시징(FCM) API로 마이그레이션할]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/migrating_to_firebase_cloud_messaging/) 수 있습니다. 

#### Braze 클라우드 데이터 수집(CDI) 엔드포인트

{% multi_lang_include release_type.md release="일반 사용 가능" %}

Braze CDI 엔드포인트를 사용하려면
- [기존 연동 목록을 반환합니다]({{site.baseurl}}/api/endpoints/cdi/get_integration_list/).
- 지정된 통합에 대한 [과거 동기화 상태 목록을 반환합니다]({{site.baseurl}}/api/endpoints/cdi/get_job_sync_status/).
- 지정된 통합에 대한 [동기화를 트리거합니다]({{site.baseurl}}/api/endpoints/cdi/post_job_sync/).

#### Databricks용 Braze 클라우드 데이터 수집(CDI) 지원

이제 [Databricks 데이터 소스에서]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/sync_catalogs_data/#step-2-integrate-cloud-data-ingestion-with-catalog-data) 카탈로그에 대한 Braze CDI 지원을 사용할 수 있습니다.

#### 수동 Swift SDK 통합

통합 가이드에 [수동 통합]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/installation_methods/manual_integration) 문서를 추가하여 패키지 관리자를 사용하지 않고 Swift SDK를 수동으로 통합하는 방법을 설명했습니다.

#### 사용 중단

2024년 1월 11일, Braze는 Windows 앱과 Baidu 앱에서 메시지 서비스 및 데이터 수집을 중단했습니다.

### 창의력 발휘

#### SQL 세그먼트 확장 사용 사례

[SQL 세그먼트 확장 사용 사례]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/use_cases) 라이브러리에는 자체 SQL 쿼리를 만들 때 영감을 얻기 위해 사용할 수 있는 SQL 세그먼트 확장에 대한 테스트된 쿼리가 포함되어 있습니다.

### 강력한 채널

#### 사용자 지정 코드 블록

{% multi_lang_include release_type.md release="일반 사용 가능" %}

[사용자 지정 코드 블록을]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/editor_blocks/#custom-code) 사용하면 인앱 메시지에 HTML, CSS 및 JavaScript를 추가, 편집 또는 삭제할 수 있습니다.

#### 푸시 알림의 페이로드 크기 줄이기

새로운 도움말 문서 [알림 페이로드 크기]({{site.baseurl}}/help/help_articles/push/reducing_payload_size#reducing-push-notification-payload-size)에서는 푸시 페이로드 크기 제한으로 인해 캠페인 또는 캔버스 단계를 시작할 수 없는 경우 푸시 알림의 페이로드 크기를 줄일 수 있는 몇 가지 팁을 제공합니다.

#### 캠페인 또는 캔버스에 BCC 주소 추가하기

{% multi_lang_include release_type.md release="일반 사용 가능" %}

이메일 메시지에 숨은 참조 [주소를]({{site.baseurl}}/user_guide/administrative/app_settings/email_settings/?tab=bcc%20address#outbound-email-settings) 추가할 수 있습니다. 이렇게 하면 사용자가 받은 메시지의 동일한 사본이 사용자의 BCC 받은편지함으로 전송됩니다. 이를 통해 규정 준수 요구 사항이나 고객 지원 문제를 위해 사용자에게 보낸 메시지의 사본을 보관할 수 있습니다.

#### 이메일의 원클릭 수신 거부 링크

[목록 수신 거부 헤더]({{site.baseurl}}/user_guide/administrative/app_settings/email_settings/#list-unsubscribe-header)를 사용하면 메시지 본문이 아닌 사서함 UI 내에 수신 **거부** 버튼을 표시하여 수신자가 클릭 한 번으로 마케팅 이메일의 수신을 거부할 수 있습니다.

### 새로운 Braze 파트너십

#### Criteo - 캔버스 오디언스 동기화

브랜드는 [Braze 오디언스 싱크 투 Criteo]({{site.baseurl}}/partners/canvas_steps/criteo_audience_sync/)를 사용하여 자체 Braze 통합의 사용자 데이터를 Criteo 고객 목록에 추가하여 행동 트리거, 세분화 등을 기반으로 광고를 게재할 수 있습니다. 사용자 데이터를 기반으로 Braze 캔버스에서 메시지(푸시, 이메일, SMS, 웹훅 등)를 트리거하는 데 일반적으로 사용하는 모든 기준을 이제 Criteo 고객 목록에서 해당 사용자에게 광고를 트리거하는 데 사용할 수 있습니다.

#### 이동식 잉크 - 동적 콘텐츠

[무버블 잉크]({{site.baseurl}}/partners/message_personalization/dynamic_content/movable_ink#movable-ink) 고객 데이터 API 통합을 통해 마케터는 Braze에 저장된 고객 이벤트 데이터를 활성화하여 무버블 잉크 내에서 개인화된 콘텐츠를 생성할 수 있습니다.

#### 스쿠버 애널리틱스 - 분석

[Scuba 분석]({{site.baseurl}}/partners/data_and_infrastructure_agility/analytics/scuba#scuba-analytics)은 고속 시계열 데이터를 위해 설계된 풀스택 머신 러닝 기반 데이터 협업 플랫폼입니다. Scuba를 사용하면 사용자(액터라고도 함)를 선택적으로 내보내고 Braze 플랫폼에 로드할 수 있습니다. Scuba에서는 커스텀 액터 속성을 사용하여 행동 추세를 분석하고, 다양한 플랫폼에서 데이터를 활성화하고, 머신 러닝을 사용하여 예측 모델링을 수행합니다.

### SDK 업데이트
 
다음 SDK 업데이트가 릴리스되었습니다. 주요 업데이트는 아래에 나열되어 있으며, 그 외의 모든 업데이트는 해당 SDK 체인지로그를 확인하면 확인할 수 있습니다.
 
- [Expo 플러그인 2.0.0](https://github.com/braze-inc/braze-expo-plugin/blob/main/CHANGELOG.md)
    - [엑스포 SDK 50 요구 사항](https://expo.dev/changelog/2024/01-18-sdk-50)에 따라 iOS 최소 플랫폼 버전을 `13.4`로 상향 조정합니다.
    - 이 버전은 Expo SDK 50을 완벽하게 지원하려면 Braze React Native SDK 버전 [8.3.0 이상](https://github.com/braze-inc/braze-react-native-sdk/releases/tag/8.3.0)이 필요합니다.
- [React Native SDK 8.3.0](https://github.com/braze-inc/braze-react-native-sdk/blob/8.3.0/CHANGELOG.md)
- [Unity SDK 5.1.0](https://github.com/braze-inc/braze-unity-sdk/blob/master/CHANGELOG.md)
- [Android SDK 30.0.0](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md)
    - 인앱 메시지에 사용되는 웹뷰가 `WebViewAssetLoader`를 사용하도록 업데이트되었습니다.
        - `WebSettings.allowFileAccess`는 이제 `InAppMessageHtmlBaseView` 및 `BrazeWebViewActivity`에서 false로 설정됩니다.
        - 직접 `InAppMessageWebViewClient` 또는 `InAppMessageHtmlBaseView` 을 사용하는 경우 원본 클래스와 비교하여 구현이 에셋을 올바르게 로드하고 있는지 확인하세요.
        - 사용자 정의 클래스를 사용하지 않는 경우 모든 것이 이전과 동일하게 작동합니다.
- [Braze Swift SDK 6.6.2](https://github.com/braze-inc/braze-swift-sdk/blob/6.6.2/CHANGELOG.md)
- [Braze Swift SDK 7.6.0](https://github.com/braze-inc/braze-swift-sdk/releases/tag/7.6.0)
- [Xamarin SDK 버전 3.0.0](https://github.com/braze-inc/braze-xamarin-sdk/blob/master/CHANGELOG.md)
    - NuGet 패키지의 이름이 `AppboyPlatformXamariniOSBinding`에서 [`BrazePlatform.BrazeiOSBinding`](https://www.nuget.org/packages/BrazePlatform.BrazeiOSBinding/)으로 변경되었습니다.
        - 업데이트된 패키지를 사용하려면 `AppboyPlatformXamariniOSBinding;` 사용 인스턴스를 Braze 사용으로 바꾸세요
    - 이 버전에서는 .NET 6+를 사용해야 하며 Xamarin 프레임워크를 사용하는 프로젝트에 대한 지원이 제거됩니다. Xamarin 지원 종료에 대한 [Microsoft의 정책](https://dotnet.microsoft.com/en-us/platform/support/policy/xamarin)을 참조하세요.
    - Android 바인딩을 [Braze Android SDK 26.3.2에서 29.0.1로](https://github.com/braze-inc/braze-android-sdk/compare/v26.3.1...v29.0.1#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed) 업데이트했습니다.
- [Xamarin SDK 4.0.0](https://github.com/braze-inc/braze-xamarin-sdk/blob/master/CHANGELOG.md)
    - 이 버전에서는 iOS 바인딩이 [Braze Swift SDK를](https://github.com/braze-inc/braze-swift-sdk/) 사용하도록 업데이트됩니다. 대부분의 iOS 공용 API가 변경되었으므로, 대체 사용에 대한 안내는 [마이그레이션 가이드](https://braze-inc.github.io/braze-swift-sdk/documentation/braze/appboy-migration-guide/) (Swift)를 참조하세요. 기존 공개 API를 계속 사용할 수 있도록 호환성 바인딩을 제공합니다.
        - 이제 iOS 바인딩은 여러 모듈로 구성됩니다:
            - **BrazeKit:** 분석 및 푸시 알림을 지원하는 기본 SDK 라이브러리(nuget: [Braze.iOS.BrazeKit](https://www.nuget.org/packages/Braze.iOS.BrazeKit)).
            - BrazeUI: 인앱 메시지 및 콘텐츠 카드를 위한 Braze 제공 사용자 인터페이스 라이브러리(nuget: [Braze.iOS.BrazeUI](https://www.nuget.org/packages/Braze.iOS.BrazeUI)).
            - BrazeLocation: 위치 분석 및 지오펜스 모니터링을 지원하는 위치 라이브러리(nuget: [Braze.iOS.BrazeLocation](https://www.nuget.org/packages/Braze.iOS.BrazeLocation)).
            - BrazeKitCompat: 4.0.0 이전 API를 지원하는 호환성 라이브러리(nuget: [Braze.iOS.BrazeKitCompat](https://www.nuget.org/packages/Braze.iOS.BrazeKitCompat)).
            - BrazeUICompat: 4.0.0 이전 UI API를 지원하는 호환성 라이브러리(nuget: [Braze.iOS.BrazeUICompat](https://www.nuget.org/packages/Braze.iOS.BrazeUICompat)).
        - 새로운 통합에 대해서는 BrazeiOSMauiSampleApp을, 호환성 모듈의 사용법에 대해서는 BrazeiOSMauiCompatSampleApp을 참조하세요.
    - [Braze Swift SDK 7.6.0](https://github.com/braze-inc/braze-swift-sdk/releases/tag/7.6.0)에 대한 iOS 바인딩을 업데이트했습니다.
    - iOS 바인딩을 사용하려면 Xcode 15와의 호환성을 위해 .NET 7을 사용해야 합니다.
- [Xamarin SDK 4.0.1](https://github.com/braze-inc/braze-xamarin-sdk/blob/master/CHANGELOG.md)

## 2024년 1월 9일 출시

### 업데이트된 Shopify 통합 문서

다음을 포함하여 Braze와 Shopify 통합 설명서의 섹션을 업데이트했습니다:

- [Shopify 시작하기]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/getting_started_shopify/)
- [Braze에서 Shopify 설정]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/setting_up_shopify/)
- [Shopify 사용자 ID 관리]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/shopify_features/shopify_user_identity/)

### 데이터 유연성

#### 카탈로그의 재고 부족 알림

{% multi_lang_include release_type.md release="조기 액세스" %}

카탈로그와 캔버스를 통한 [품절 알림을]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/back_in_stock_notifications/) 조합하여 품목의 품절 시 고객에게 알릴 수 있습니다. 고객이 선택한 커스텀 이벤트를 수행할 때마다 아이템이 보충될 때마다 자동으로 알림을 받도록 구독할 수 있습니다.

#### 카탈로그 세그먼트

{% multi_lang_include release_type.md release="조기 액세스" %}

[카탈로그 세그먼트는]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/catalog_segments/) SQL 세그먼트 확장의 카탈로그 데이터를 기반으로 하는 사용자 대상입니다. 이러한 SQL 세그먼트 확장은 세그먼트에서 참조한 다음 캠페인 및 캔버스에서 타겟팅할 수 있습니다. 카탈로그 세그먼트는 SQL을 사용하여 카탈로그의 데이터와 사용자 지정 이벤트 또는 구매의 데이터를 조인합니다. 이렇게 하려면 카탈로그와 커스텀 이벤트 또는 구매에 공통 식별자 필드가 있어야 합니다.

#### Firebase Cloud 메시징 API로 마이그레이션하기

{% multi_lang_include release_type.md release="조기 액세스" %}

더 이상 사용되지 않는 Google의 클라우드 메시징 API에서 완전히 지원되는 Firebase 클라우드 메시징(FCM) API로 [마이그레이션하는 방법을]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/migrating_to_firebase_cloud_messaging/) 알아보세요.

### SDK 업데이트

다음 SDK 업데이트가 릴리스되었습니다. 주요 업데이트는 아래에 나열되어 있으며, 그 외의 모든 업데이트는 해당 SDK 체인지로그를 확인하면 확인할 수 있습니다.

- [Swift SDK 7.5.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md)
    - Braze의 데이터 수집 정책을 설명하기 위해 `BrazeKit` 및 `BrazeLocation`에 대한 개인정보처리방침을 추가합니다. 자세한 내용은 Apple의 개인정보처리방침 [설명서](https://developer.apple.com/documentation/bundleresources/privacy_manifest_files/describing_data_use_in_privacy_manifests)를 참조하세요. 데이터 수집 관행을 관리하기 위한 더 많은 구성은 향후 릴리스에서 제공될 예정입니다.
    - 7.1.0에 도입된 XC프레임워크의 코드 서명 관련 문제를 수정합니다.
- [웹 SDK v5.1.0](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md)
- [Unity SDK 5.0.0](https://github.com/braze-inc/braze-unity-sdk/blob/master/CHANGELOG.md)
    - Braze Swift SDK 6.1.0에서 7.4.0으로 네이티브 iOS 브릿지를 업데이트했습니다.
        - 이제 iOS 리포지토리 링크는 이 [리포지토리](https://github.com/braze-inc/braze-swift-sdk-prebuilt-dynamic)에서 미리 빌드된 동적 XC프레임웍스를 가리킵니다.
    - 네이티브 Android 브릿지를 Braze Android SDK 27.0.1에서 29.0.1로 업데이트했습니다.
    - `AppboyBinding.GetFeatureFlag(string id)`는 이제 기능 플래그가 존재하지 않으면 `null`을 반환합니다.
    - `FEATURE_FLAGS_UPDATED`는 새로 고침 요청이 성공 또는 실패로 완료된 경우와 현재 세션에서 이전에 캐시된 데이터가 있는 경우 최초 구독 시에만 트리거됩니다.
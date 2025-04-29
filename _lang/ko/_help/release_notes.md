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
  - name: 2025
    link: /docs/help/release_notes/2025/
    image: /assets/img/braze_icons/calendar-check-02.svg
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
    link: /docs/developer_guide/changelogs/
    image: /assets/img/braze_icons/file-code-01.svg

---

# 최신 Braze 릴리즈 노트 {#most-recent}

> Braze는 주요 제품 출시에 맞춰 한 달 주기로 제품 업데이트에 대한 정보를 공개하지만 매주 기타 개선 사항이 업데이트됩니다.
> <br>
> <br>

> 이 섹션에 나열된 업데이트에 대한 자세한 내용은 계정 관리자에게 문의하거나 [지원 티켓을 개설하세요]({{site.baseurl}}/user_guide/administrative/access_braze/support/). 또한 [SDK 체인지로그에서]({{site.baseurl}}/developer_guide/changelogs) 월별 SDK 릴리스, 업데이트 및 개선 사항에 대한 자세한 정보를 확인할 수 있습니다.
 
## 2025년 4월 1일 출시

### Braze 탐색 업데이트

Braze의 업데이트된 탐색은 장치 간 기능 및 콘텐츠에 효율적으로 접근할 수 있도록 설계되었습니다. 탐색 버전 간 전환 옵션은 더 이상 제공되지 않습니다. 전용 [Navigating Braze]({{site.baseurl}}/user_guide/administrative/access_braze/navigation) 기사에서 자세히 알아보세요.

### 개발자 가이드 정리

이전에는 많은 플랫폼 수준 작업이 여러 페이지에 걸쳐 분산되어 있었으며, 예를 들어 Swift SDK 통합이 6페이지에 걸쳐 나뉘어 있었습니다. 또한, 공유 기능이 각 플랫폼에 대해 개별적으로 문서화되어 있어, "푸시 알림 설정"과 같은 주제를 검색하면 10개의 다른 페이지가 반환되었습니다.

**이전:**

![플랫폼 통합 가이드 섹션에 위치한 이전 Swift 문서입니다.]({% image_buster /assets/img/before_swift.png %})

이제 플랫폼 수준 작업이 단일 페이지로 통합되었으며, 공유 SDK 기능이 이제 같은 페이지에 존재합니다(새로운 SDK 탭 기능의 도움으로). 예를 들어, 이제 Braze SDK 통합을 위한 단일 페이지가 있으며, 페이지 상단의 탭을 선택하여 플랫폼 간 전환할 수 있습니다. 그럴 경우, 페이지 내 목차도 현재 선택된 탭을 반영하도록 업데이트됩니다.

**이후:**

![SDK 통합 기사에서 Swift 탭에 위치한 업데이트된 Swift 문서입니다.]({% image_buster /assets/img/after_swift.png %})

![SDK 통합 기사에서 Android 탭에 위치한 업데이트된 Android 문서입니다.]({% image_buster /assets/img/after_android.png %})

### Braze 설명서에 기여하기

모르셨다면, 우리의 문서는 완전히 오픈 소스입니다! 우리의 [기여 가이드]({{site.baseurl}}/contributing/home)에서 방법을 배울 수 있습니다. 이번 달에는 [섹션을 자동 확장하도록 강제하기]({{site.baseurl}}/contributing/content_management/sections#forcing-auto-expand) 및 [API 생성 콘텐츠 렌더링]({{site.baseurl}}/contributing/generating_a_preview#step-2-start-a-local-server)와 같은 일부 사이트 기능을 문서화했습니다.

### 데이터 유연성

#### Canvas 항목 속성 업데이트

캔버스 항목 속성이 이제 [캔버스 컨텍스트 변수]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties)의 일부입니다. 각 컨텍스트 변수에는 이름, 데이터 유형, Liquid를 포함할 수 있는 값이 포함됩니다. 자세한 내용은 [컨텍스트 구성 요소]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context)를 참조하십시오.

#### 전화번호 필터에 대한 세분화 필터 업데이트

세분화 필터가 두 개의 전화번호 필터에 대한 변경 사항을 반영하도록 업데이트되었습니다:

- [형식이 없는 전화번호]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters#unformatted-phone-number) (이전 **전화번호**): 형식이 없는 전화번호로 사용자를 세분화합니다.
- [전화번호]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters#phone-number) (이전 **발신 전화번호**): 형식이 지정된 전화번호 필드로 사용자를 세분화합니다.

#### 커스텀 데이터 삭제

타겟팅 캠페인과 세그먼트를 구축하다 보면 더 이상 맞춤 이벤트나 맞춤 속성이 필요하지 않을 수 있습니다. 이제 [이 커스텀 데이터]({{site.baseurl}}/user_guide/data/custom_data/managing_custom_data#deleting-custom-data)를 삭제하고 앱에서 참조를 제거할 수 있습니다.

#### 이메일 주소 및 전화번호로 사용자 가져오기

이제 이메일 주소 또는 전화번호를 사용하여 [사용자를 가져올 수<1> 있으며 외부 ID 또는 사용자 별칭을 생략할 수 있습니다.

#### 서비스 제공자 주도 로그인 문제 해결

서비스 제공자(SP) 주도 로그인에는 이제 SAML 및 단일 로그인 문제를 해결하는 데 도움이 되는 [문제 해결 섹션]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/set_up/#troubleshooting)이 있습니다.

#### 사용자 가져오기 문제 해결

[사용자 가져오기 문제 해결 섹션]({{site.baseurl}}/user_guide/data/user_data_collection/user_import#troubleshooting)에는 가져온 CSV 파일에서 누락된 행을 문제 해결하는 방법을 포함하여 새롭고 업데이트된 항목이 있습니다.

#### 세그먼트 확장에 대한 자주 묻는 질문

세그먼트 확장에 대한 [자주 묻는 질문]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/#frequently-asked-questions)을 확인하십시오. 여기에는 여러 커스텀 이벤트를 사용하는 세그먼트 확장을 만드는 방법이 포함됩니다.

#### 개인화된 및 확장된 지연

{% multi_lang_include release_type.md release="조기 액세스" %}

사용자를 위한 [개인화된 지연]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/delay_step#personalized-delays)을 설정하고 이를 사용하여 지연할 컨텍스트 변수를 선택하는 컨텍스트 단계와 함께 사용할 수 있습니다.

이제 지연 단계를 최대 2년까지 연장할 수 있습니다. 예를 들어, 앱의 새로운 사용자를 온보딩하는 경우, 세션을 시작하지 않은 사용자에게 메시지 단계를 보내기 전에 2개월의 연장된 지연을 추가할 수 있습니다.

#### Snowflake의 기본 사용자 프로필 속성

{% multi_lang_include release_type.md release="베타" %}

이제 Snowflake에 [기본 사용자 프로필 속성]({{site.baseurl}}/partners/data_and_infrastructure_agility/data_warehouses/snowflake/user_attributes)이 세 개 있습니다. 각 뷰는 고유한 성능 고려 사항을 가진 특정 사용 사례를 위해 설계되었습니다. 예를 들어, 사용자 프로필의 기본 속성에 대한 주기적인 스냅샷을 제공받을 수 있습니다.

### 강력한 채널

#### 메시징 기본 사항

[메시징 기본 사항]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals)은 캠페인 및 캔버스에 대한 공유 개념과 용어를 포함하는 참여 도구의 새로운 섹션으로, 메시지 아카이빙 및 현지화와 같은 내용을 다룹니다.

#### WhatsApp 커스텀 도메인

이제 하나 이상의 WhatsApp 구독 그룹에 [커스텀 도메인]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/custom_domains/)을 할당할 수 있습니다.

#### 캔버스를 위한 트리거된 인앱 메시지

이제 세션 시작 시 또는 커스텀 이벤트 및 구매에 의해 트리거될 [인앱 메시지의 트리거]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_by_channel/in-app_messages_in_canvas)를 선택할 수 있습니다. 모든 지연이 지나고 오디언스 옵션이 확인되면, 사용자가 메시지 단계에 도달할 때 인앱 메시지가 활성화됩니다. 사용자가 세션을 시작하고 인앱 메시지의 트리거 이벤트를 수행하면, 사용자는 인앱 메시지를 보게 됩니다. 

#### 캔버스의 입장 볼륨 제한

선택한 주기(일일, 캔버스의 전체 기간 또는 캔버스가 예약될 때마다)에 따라 이 캔버스에 잠재적으로 들어갈 수 있는 사람 수를 제한할 수 있습니다. 예를 들어, [입장 제어를 설정]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas?tab=action-based%20delivery#step-2c-set-your-target-entry-audience)하여 캔버스가 하루에 5,000명에게만 전송되도록 할 수 있습니다.

#### 새로운 사용 사례: 예약 알림 이메일 시스템

Braze 기능을 사용하여 [예약 알림 이메일 메시징 서비스]({{site.baseurl}}/user_guide/engagement_tools/canvas/ideas_and_strategies/booking_use_case)를 구축하는 방법을 알아보세요. 이 서비스는 사용자가 약속을 예약할 수 있도록 하며, 다가오는 약속에 대한 알림을 사용자에게 메시지로 보냅니다. 이 사용 사례는 이메일 메시지를 사용하지만, 사용자 프로필에 대한 단일 업데이트를 기반으로 모든 채널 또는 여러 채널에서 메시지를 보낼 수 있습니다.

#### 특정 링크에 대한 클릭 추적

특정 링크에 대한 클릭 추적을 [끄려면 클릭 추적]({{site.baseurl}}/user_guide/message_building_by_channel/email/universal_links#turning-off-click-tracking-on-a-link-to-link-basis) HTML 편집기에서 이메일 메시지에 HTML 코드를 추가하거나 드래그 앤 드롭 편집기의 구성 요소에 추가하면 됩니다.

#### 동적 Apple 푸시 알림 서비스 게이트웨이 관리

[동적 APNs 게이트웨이 관리]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift#swift_dynamic-apns-gateway-management)은 올바른 APNs 환경을 자동으로 감지하여 iOS 푸시 알림의 신뢰성과 효율성을 향상시킵니다. 이전에는 푸시 알림을 위해 APNs 환경(개발 또는 프로덕션)을 수동으로 선택해야 했으며, 이로 인해 때때로 잘못된 게이트웨이 구성, 전달 실패 및 BadDeviceToken 오류가 발생했습니다.

#### 배너 카드에 대한 Flutter 지원

{% multi_lang_include release_type.md release="조기 액세스" %}

배너 카드는 이제 Flutter를 지원합니다. 또한 모든 배너 카드 문서가 더 쉽게 사용할 수 있도록 개편되었습니다. 시작하려면 다음 기사를 확인하세요:

- [배너 카드에 대한 설명]({{site.baseurl}}/developer_guide/banner_cards)
- [배너 카드 캠페인 만들기]({{site.baseurl}}/developer_guide/banner_cards/creating_campaigns)
- [앱에 배너 카드 삽입하기]({{site.baseurl}}/developer_guide/banner_cards/embedding_cards)

#### WhatsApp 클릭 추적

{% multi_lang_include release_type.md release="조기 액세스" %}

[클릭 추적]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/click_tracking/)을 통해 누군가 WhatsApp 메시지의 링크를 탭할 때를 측정할 수 있으며, 어떤 콘텐츠가 참여를 유도하는지 명확하게 파악할 수 있습니다. Braze는 URL을 단축하고, 백그라운드에서 추적을 추가하며, 클릭 이벤트가 발생할 때 이를 기록합니다.

#### 푸시에 대한 자주 묻는 질문

푸시 캠페인을 설정할 때 발생하는 가장 자주 묻는 질문을 다룬 새로운 [푸시 FAQ]({{site.baseurl}}/user_guide/message_building_by_channel/push/faq) 기사를 확인하세요.

#### 푸시 문제 해결

[푸시 문제 해결]({{site.baseurl}}/user_guide/message_building_by_channel/push/troubleshooting)은 푸시 알림과 관련된 전달 문제를 해결하는 데 도움이 되는 여러 단계를 제공합니다. 예를 들어, 푸시 알림과 관련된 전달 문제를 겪고 있다면, 문제를 해결하기 위해 취할 수 있는 단계를 정리했습니다.

### 새로운 Braze 파트너십

#### Movable Ink 다빈치 - 동적 콘텐츠

Braze와 Movable Ink [다빈치]({{site.baseurl}}/partners/movable_ink_da_vinci) 통합은 브랜드가 다빈치의 AI 기반 콘텐츠 결정 엔진을 활용하여 매우 개인화된 메시징을 제공할 수 있도록 합니다. 다빈치는 각 사용자에게 가장 관련성 높은 콘텐츠를 선별하고 Braze를 통해 메시지를 원활하게 배포합니다.

### SDK 업데이트

다음 SDK 업데이트가 릴리스되었습니다. 주요 업데이트는 아래에 나열되어 있으며, 그 외의 모든 업데이트는 해당 SDK 체인지로그를 확인하면 확인할 수 있습니다.

- [Flutter SDK 13.0.0](https://pub.dev/packages/braze_plugin/changelog)
    - 네이티브 Android 브리지를 [Braze Android SDK 33.0.0에서 35.0.0](https://github.com/braze-inc/braze-android-sdk/compare/v33.0.0...v35.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed)으로 업데이트합니다.
        - 필요한 최소 Android SDK 버전은 25입니다. 자세한 내용은 [여기](https://github.com/braze-inc/braze-android-sdk?tab=readme-ov-file#version-information)를 참조하세요.
- [Swift SDK v11.8.0-11.9.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md)
- [Web SDK v5.8.0](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md)

## 2025년 3월 4일 출시

### 연기

Braze는 소프트 바운스의 정의를 업데이트했으며, 2025년 2월 25일 오전 10시 EST부터 [연기]({{site.baseurl}}/user_guide/message_building_by_channel/email/reporting_and_analytics/email_reporting/#email-performance)라는 새로운 이벤트를 전송합니다.

Sendgrid 고객의 경우, 소프트 바운스 이벤트와 연기 이벤트를 분리하는 변경을 했습니다. 우리는 연기된 이벤트를 소프트 바운스 이벤트로 계산합니다. 이는 Currents, Query Builder, SQL Extension, Snowflake 데이터 공유 또는 우리의 트랜잭션 이메일 제품을 사용하는 모든 Sendgrid 고객에게 영향을 미칩니다.

#### 이전 동작

2025년 2월 25일 이전에는 캠페인 또는 캔버스의 이메일 주소에 대한 연기된 이벤트가 매번 소프트 바운스 이벤트를 기록합니다. 결과적으로, 연기는 소프트 바운스 데이터의 일부로 포함됩니다. 이로 인해 사용자 또는 캠페인이 예상보다 더 많은 소프트 바운스 이벤트를 보고할 수 있습니다. 

#### 새로운 동작

2025년 2월 25일부터 지연된 이벤트는 매번 소프트 바운스 이벤트를 기록하지 않습니다. 대신, 이메일 주소에 대해 전송당 한 번만 소프트 바운스 이벤트를 기록하며, 이메일이 몇 번 재시도되거나 지연되었는지에 관계없이 기록됩니다.

#### 이것이 의미하는 바

2025년 2월 25일부터 소프트 바운스 이벤트의 양이 크게 감소하는 것을 알 수 있으며, 이로 인해 다음과 같은 잠재적인 변화가 발생할 수 있습니다:

- 쿼리 빌더를 사용하여 작성된 모든 보고서에서 소프트 바운스 감소
- 소프트 바운스가 X회 발생한 사용자를 타겟팅하는 경우 SQL 확장을 사용하여 세그먼트 크기가 작아짐
- 커런츠 및 스노우플레이크의 모든 기능을 사용하여 전달된 소프트 바운스 이벤트 수 감소
- 트랜잭션 이메일 제품의 소프트 바운스 수 감소

스파크포스트 고객의 경우 소프트 바운스 이벤트 데이터에 영향이 없으며, 대신 커런츠와 스노우플레이크에서 새로운 이메일 이벤트인 지연을 받기 시작합니다.

### 개발자 가이드 정리

여러 SDK에서 공유되는 동일한 콘텐츠가 문서 사이트의 새로운 SDK 탭 기능을 사용하여 통합되기 시작했습니다. 이번 달 [SDK 통합]({{site.baseurl}}/developer_guide/sdk_integration/), [SDK 초기화]({{site.baseurl}}/developer_guide/sdk_initialization/), 및 [콘텐츠 카드]({{site.baseurl}}/developer_guide/content_cards/)가 결합되었습니다. 앞으로 몇 달 동안 더 많은 업데이트를 기대해 주세요.

### 데이터 유연성
 
#### 사용자 프로필에 대한 브레이즈 ID

이제 사용자 프로필에는 [브레이즈 ID]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles#user-profiles)가 포함됩니다. 사용자 프로필을 검색할 때 이를 사용할 수 있습니다.

#### 연기

브레이즈는 소프트 바운스의 정의를 업데이트했으며, 이메일이 즉시 전달되지 않았을 때 새로운 이벤트인 [지연]({{site.baseurl}}/user_guide/message_building_by_channel/email/reporting_and_analytics/email_reporting#email-performance)을 전송하고 있습니다. 이는 이메일이 일시적인 전달 실패 후 최대 72시간 동안 재전송되어 성공적인 전달 가능성을 극대화하기 위한 것입니다.

#### 스노우플레이크 엔티티 관계
 
스노우플레이크와 브레이즈 엔티티 관계에 대한 [원시 테이블 스키마](https://www.braze.com/docs/assets/download_file/data-sharing-raw-table-schemas.txt)를 새로운 [사용자 친화적인 문서 페이지](https://www.braze.com/docs/partners/data_and_infrastructure_agility/data_warehouses/snowflake/entity_relationships)에 매핑했습니다. 각 채널에 속하는 `USER_MESSAGES` 테이블의 세부 사항과 각 테이블의 기본 키, 외래 키 및 고유 키에 대한 설명이 포함되어 있습니다.

#### 외부 ID에 대한 아이덴티티 관리

이메일 주소 또는 해시된 이메일 주소를 Braze 외부 ID로 사용하면 데이터 소스 전반에 걸쳐 아이덴티티 관리를 간소화할 수 있지만, 사용자 개인 정보 및 데이터 보안에 대한 [잠재적 위험]({{site.baseurl}}/user_guide/data/user_data_collection/user_profile_lifecycle/#identified-user-profiles)을 고려하는 것이 중요합니다.
 
### 창의력 발휘

#### Liquid 튜토리얼

다음 시나리오에서 연산자를 사용하는 방법에 대한 [Liquid 튜토리얼]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/operators/#tutorials) 세 개가 추가되었습니다.

<table border="1">
  <tr>
    <td>정수 커스텀 속성이 있는 메시지 선택하기.</td>
    <td><img src="{% image_buster /assets/img/release_notes/2025_05_04/integer.png %}" alt="정수 커스텀 속성이 있는 메시지를 보여주는 Braze의 작성 단계." /></td>
  </tr>
  <tr>
    <td>문자열 커스텀 속성이 있는 메시지 선택하기.</td>
    <td><img src="{% image_buster /assets/img/release_notes/2025_05_04/string.png %}" alt="문자열 커스텀 속성이 있는 메시지를 보여주는 Braze의 작성 단계." /></td>
  </tr>
  <tr>
    <td>위치에 따라 메시지 중단하기.</td>
    <td><img src="{% image_buster /assets/img/release_notes/2025_05_04/location.png %}" alt="위치에 따라 중단되는 메시지를 보여주는 Braze의 작성 단계." /></td>
  </tr>
</table>
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

#### 캔버스의 컨텍스트 단계
 
{% multi_lang_include release_type.md release="조기 액세스" %}
 
사용자가 캔버스를 이동하는 동안 그 사용자의 컨텍스트(또는 그 사용자의 행동에 대한 통찰력)를 나타내는 변수 집합을 생성하거나 업데이트하기 위해 [컨텍스트 단계]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context)를 사용하세요.

#### 개인화된 지연

{% multi_lang_include release_type.md release="조기 액세스" %}

지연 단계에서 **개인화된 지연** 토글을 선택하여 사용자에 대한 [개인화된 지연]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/delay_step/#personalized-delays)을 설정할 수 있습니다. 컨텍스트 단계와 함께 사용하여 지연할 컨텍스트 변수를 선택할 수 있습니다.

캔버스 사용자 여정에서 지연 단계를 설정할 때 이제 최대 2년까지 지연을 생성할 수 있습니다.

#### 자동 동기화 되돌리기

[이메일 메시지 작성 중]({{site.baseurl}}/user_guide/message_building_by_channel/email/html_editor/creating_an_email_campaign/#step-3-compose-your-email)에 Plaintext 탭에서 Regenerate from HTML 아이콘을 선택하여 자동 동기화로 되돌릴 수 있으며, 이 아이콘은 일반 텍스트가 동기화되지 않을 때만 나타납니다.

![Braze에서 자동 동기화를 위한 되돌리기 버튼.]({% image_buster /assets/img/release_notes/2025_05_04/regenerate_from_html.png %})
 
### 강력한 채널

#### 안드로이드 라이브 업데이트

라이브 업데이트는 공식적으로 Android 16까지 사용할 수 없지만, 우리의 Android용 라이브 업데이트 페이지는 그 동작을 에뮬레이트하는 방법을 보여주므로, Swift Braze SDK의 라이브 활동과 유사한 대화형 잠금 화면 알림을 표시할 수 있습니다.
공식 라이브 업데이트와 달리, 이 기능은 이전 Android 버전에서도 구현할 수 있습니다. 작업 공간 간에 기능 플래그가 있는 캠페인을 복사하는 중입니다.

#### 이제 작업 공간 간에 기능 플래그가 있는 캠페인을 복사할 수 있습니다.

이를 위해서는 대상 작업 공간에 원래 캠페인에서 참조된 기능 플래그와 일치하는 ID로 구성된 기능 플래그 실험이 설정되어 있는지 확인하십시오. 새로운 WhatsApp 메시지 유형이 지원됩니다.

#### WhatsApp 메시지는 이제 비디오, 오디오 및 문서 아웃바운드 메시지를 지원합니다.

오른쪽에서 왼쪽으로 읽는 메시지 Contact your Braze account manager if you're interested in participating in the early access.

#### 오른쪽에서 왼쪽으로 읽는 메시지 만들기는 오른쪽에서 왼쪽으로 읽는 언어로 메시지를 작성하는 모범 사례를 다루어 메시지가 가능한 한 정확하게 표시되도록 합니다.

[메시징에서 항목 추천 사용]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/right_to_left_messages/)은  Liquid 객체를 다루며, 해당 지식을 실제로 적용하는 데 도움이 되는 튜토리얼을 포함합니다.
 
### AI 및 ML 자동화
 
#### 항목 추천

이메일 사랑 - 채널 확장

### 새로운 Braze 파트너십
 
#### Braze와 Email Love 파트너십은 Email Love의 Braze로 내보내기 기능과 Braze API를 활용하여 이메일 템플릿을 Braze에 원활하게 업로드합니다.
 
VWO - A/B 테스트

#### Braze와 VWO 통합을 통해 VWO 실험 데이터를 활용하여 타겟 세그먼트를 만들고 개인화된 캠페인을 제공할 수 있습니다.
 
React Native 최소 요구 사항 버전을 [0.71.0]({{site.baseurl}}/partners/data_and_infrastructure_agility/ab_testing/vwo)으로 증가시킵니다.
 
### SDK 업데이트
 
다음 SDK 업데이트가 릴리스되었습니다. 주요 업데이트는 아래에 나열되어 있으며, 그 외의 모든 업데이트는 해당 SDK 체인지로그를 확인하면 확인할 수 있습니다.
 
- [React Native](https://github.com/braze-inc/braze-react-native-sdk/blob/master/CHANGELOG.md)
    - 자세한 내용은 React 작업 그룹의 릴리스 지원 정책을 참조하십시오. 최소 요구 iOS 버전을 12.0으로 증가시킵니다.
    - 네이티브 iOS 버전 바인딩을 Braze Swift SDK 7.5.0에서 8.1.0으로 업데이트합니다.
    - 네이티브 Android 버전 바인딩을 [Braze Android SDK 29.0.1에서 30.1.1](https://github.com/braze-inc/braze-swift-sdk/compare/7.5.0...8.1.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed)으로 업데이트합니다.
    - 라이브 업데이트는 공식적으로 [Android 16](https://github.com/braze-inc/braze-android-sdk/compare/v29.0.1...v30.1.1#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed)까지 사용할 수 없지만, 우리의 Android용 라이브 업데이트 페이지는 그 동작을 에뮬레이트하는 방법을 보여주므로, Swift Braze SDK의 라이브 활동과 유사한 대화형 잠금 화면 알림을 표시할 수 있습니다.

## 2025년 2월 4일 출시

### Braze 문서 개선

#### 기여 가이드
최근 [기여 가이드]({{site.baseurl}}/contributing/your_first_contribution)에 대한 업데이트로 비기술 사용자가 Braze 문서에 기여하기가 더 쉬워졌습니다.

#### 데이터 및 분석 개편
원하는 정보를 더 쉽게 찾을 수 있도록 "데이터 및 분석" 아래에 있던 기사를 [데이터]({{site.baseurl}}/user_guide/data)와 [분석]({{site.baseurl}}/user_guide/analytics)으로 분리했습니다. 

#### 개발자 가이드
모든 문서에 대한 대규모 정리를 진행했으며, [Braze 개발자 가이드]({{site.baseurl}}/developer_guide/home)에 있는 여러 페이지에 나뉘어 있던 "사용 방법"을 하나의 페이지로 통합했습니다.

모든 Braze SDK에 대한 참조 문서와 리포지토리를 나열한 새로운 [SDK 참조 페이지]({{site.baseurl}}/developer_guide/references)도 있습니다.

##### 언리얼 엔진 Braze SDK
Unreal Engine Braze SDK GitHub 리포지토리 README의 모든 콘텐츠를 [Braze 문서의 전용 섹션]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=unreal%20engine)으로 마이그레이션하고 재작성했습니다.

### 데이터 유연성

#### API 사용량 대시보드

{% multi_lang_include release_type.md release="일반 사용 가능" %}

[API 사용 대시보드]({{site.baseurl}}/user_guide/analytics/dashboard/api_usage_dashboard)를 통해 Braze로 들어오는 REST API 트래픽을 모니터링하여 REST API 사용 내에서의 트렌드를 이해하고 잠재적인 문제를 해결할 수 있습니다.

#### 커스텀 속성에 태그 추가

{% multi_lang_include release_type.md release="일반 사용 가능" %}

"이벤트, 속성, 구매 관리" 권한이 있는 경우 생성 후 [커스텀 속성에 태그를 추가할 수 있습니다.]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes#adding-tags) 그런 다음 태그를 사용하여 속성 목록을 필터링할 수 있습니다.

#### 카탈로그 선택 및 비동기 카탈로그 필드 엔드포인트 

{% multi_lang_include release_type.md release="일반 사용 가능" %}

다음 엔드포인트가 이제 일반적으로 사용 가능합니다:
* [게시: 카탈로그 필드 생성]({{site.baseurl}}/api/endpoints/catalogs/catalog_fields/asynchronous/post_create_catalog_fields)
* [삭제: 카탈로그 필드 삭제]({{site.baseurl}}/api/endpoints/catalogs/catalog_fields/asynchronous/delete_catalog_field)
* [삭제: 카탈로그 선택 삭제]({{site.baseurl}}/api/endpoints/catalogs/catalog_selections/asynchronous/delete_catalog_selection)
* [게시: 카탈로그 선택 생성]({{site.baseurl}}/api/endpoints/catalogs/catalog_selections/asynchronous/post_create_catalog_selections)

#### 이메일 주소를 사용하여 캠페인 또는 캔버스를 트리거하기

{% multi_lang_include release_type.md release="일반 사용 가능" %}

이제 이메일 주소로 수신자를 지정하여 [캠페인]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/targeting_users) 및 [캔버스]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/?tab=target%20audience#step-2c-set-your-target-entry-audience)를 트리거할 수 있습니다.

#### API를 통해 전화번호를 사용하여 사용자를 식별합니다.

{% multi_lang_include release_type.md release="일반 사용 가능" %}

이제 별칭 및 이메일 주소 외에도 전화번호를 사용하여 [`/users/identify` API 엔드포인트]({{site.baseurl}}/api/endpoints/user_data/post_user_identify)를 통해 사용자를 식별할 수 있습니다.

#### SAML 추적 가져오기
SAML SSO에 대한 문제를 보다 효율적으로 해결하는 데 도움이 되는 [ SAML 추적을 얻는 방법에 대한 단계]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/set_up#obtaining-a-saml-trace)을 추가했습니다.
 
#### 지역별 데이터 센터
Braze가 새로운 지역을 서비스하기 위해 성장함에 따라, 운영 접근 방식을 명확히 하기 위해 [Braze 데이터 센터에 대한 기사]({{site.baseurl}}/user_guide/data/data_centers)를 추가했습니다.
 
### 창의력 발휘
 
#### 가격 인하 알림 및 재고 복귀 알림

{% multi_lang_include release_type.md release="일반 사용 가능" %}

이제 캔버스와 카탈로그를 통해 [재고 복귀 알림]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/catalog_triggers/back_in_stock_notifications)을 설정하여 고객에게 품목이 재고에 다시 들어왔음을 알릴 수 있습니다.

가격 인하 알림을 설정하여 품목의 가격이 하락했을 때 고객에게 알리기 위해 [가격 인하 알림]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/catalog_triggers/price_drop_notifications)을 생성할 수도 있습니다.

#### 선택 미리보기 

{% multi_lang_include release_type.md release="일반 사용 가능" %}

선택을 생성한 후, 무작위 사용자 또는 특정 사용자에 대해 [선택이 반환할 내용을 보기]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/selections/#test-and-preview)할 수 있습니다.

#### Liquid를 포함한 카탈로그 항목 템플릿 

{% multi_lang_include release_type.md release="일반 사용 가능" %}

Liquid를 포함하는 [템플릿 카탈로그 항목]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/using_catalogs/#using-liquid)을 만들 수 있습니다.

#### 캔버스 템플릿
우리는 [선호도 설문조사로 온보딩 사용자]({{site.baseurl}}/user_guide/engagement_tools/canvas/get_started/braze_templates/preference_survey) 및 [더블 옵트인으로 이메일 가입 생성]({{site.baseurl}}/user_guide/engagement_tools/canvas/get_started/braze_templates/email_signup)을 위한 새로운 캔버스 템플릿을 추가했습니다.

#### B2B를 위한 Salesforce Sales Cloud로 리드 관리
B2B 마케터가 Braze를 사용하는 한 가지 방법은 Salesforce Sales Cloud와의 통합을 통해서입니다. 이 [사용 사례]({{site.baseurl}}/user_guide/getting_started/b2b_use_cases/b2b_salesforce_sales_cloud)를 구현하는 방법에 대해 더 읽어보세요.
 
### 강력한 채널

#### 억제 목록

{% multi_lang_include release_type.md release="베타" %}
 
[억제 목록]({{site.baseurl}}/user_guide/engagement_tools/segments/suppression_lists)은 메시지를 절대 받지 않을 사용자 그룹을 지정합니다. 관리자는 세분화와 동일한 방식으로 사용자 그룹을 좁히기 위해 세그먼트 필터로 억제 목록을 생성할 수 있습니다.

### 새로운 Braze 파트너십

#### 생성자 - 동적 콘텐츠
[Constructor]({{site.baseurl}}/partners/message_personalization/dynamic_content/constructor)는 AI와 머신 러닝을 사용하여 전자상거래 및 소매 웹사이트를 위한 개인화된 검색, 추천 및 탐색 경험을 제공하는 검색 및 제품 발견 플랫폼입니다.
 
#### Trustpilot - 동적 콘텐츠
[Trustpilot]({{site.baseurl}}/partners/message_personalization/dynamic_content/trustpilot)는 고객이 피드백을 공유하고 리뷰를 관리하고 응답할 수 있도록 하는 온라인 리뷰 플랫폼입니다.

### SDK 업데이트
 
다음 SDK 업데이트가 릴리스되었습니다. 주요 업데이트는 아래에 나열되어 있으며, 그 외의 모든 업데이트는 해당 SDK 체인지로그를 확인하면 확인할 수 있습니다.
 
- [Braze Android SDK 34.0.0](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#3400)
    - 최소 SDK 버전을 21(Lollipop)에서 25(Nougat)로 업데이트했습니다.

## 2025년 1월 7일 출시

### 창의력 발휘

#### 앱 내 메시지 템플릿

드래그 앤 드롭 앱 내 메시지를 위한 [템플릿]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/)을 추가했습니다.

#### B2B Salesforce Sales Cloud 리드 관리

[Salesforce Sales Cloud로 리드 관리]({{site.baseurl}}/user_guide/getting_started/b2b_use_cases/b2b_salesforce_sales_cloud/)는 커뮤니티 제출 통합을 통해 Salesforce Sales Cloud에서 리드를 생성하고 업데이트하는 방법을 보여줍니다.

### 강력한 채널

#### 캔버스 템플릿

이중 옵트인으로 [이메일 가입]({{site.baseurl}}/user_guide/engagement_tools/canvas/get_started/braze_templates/email_signup/) 및 [선호도 설문조사로 온보딩]({{site.baseurl}}/user_guide/engagement_tools/canvas/get_started/braze_templates/preference_survey/)을 위한 Braze Canvas 템플릿을 추가했습니다.

#### WhatsApp 옵트인 정책 변경

메타는 최근 [옵트인 정책을](https://developers.facebook.com/docs/whatsapp/overview/getting-opt-in/) 업데이트했습니다. 추가 정보는 [WhatsApp 제품 업데이트]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/meta_resources/)를 참조하세요.

#### 이메일 드래그 앤 드롭 편집기의 콘텐츠 블록에 대한 너비 도구

드래그 앤 드롭 이메일 편집기에서 콘텐츠 블록의 [너비를 조정할 수 있습니다]({{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/dnd_content_blocks/#using-the-editor-to-add-a-content-block). 기본값 너비는 100%입니다.

### 데이터 유연성

#### 소프트 바운스된 세그먼트 필터

Y일 동안 소프트 바운스 횟수별로 사용자를 세분화하세요. 자세한 내용은 [세분화 필터 용어집]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters#soft-bounced)을 참조하세요.

#### 익명 사용자 개요

[익명 사용자]({{site.baseurl}}/user_guide/data/user_data_collection/user_profile_lifecycle/anonymous_users/)는 익명 사용자 및 사용자 별칭에 대한 개요를 제공하며, 그들의 중요성과 메시지에서 어떻게 활용할 수 있는지를 설명합니다.

#### 글로벌 컨트롤 그룹 멤버십

개별 사용자의 프로필의 **참여** 탭으로 이동하여 [글로벌 컨트롤 그룹 멤버십]({{site.baseurl}}/user_guide/engagement_tools/testing/global_control_group/#view-whether-a-user-is-in-a-global-control-group)을 **기타** 섹션으로 스크롤하여 볼 수 있습니다.

### 새로운 Braze 파트너십

#### Justuno - 리드 캡처

[Justuno]({{site.baseurl}}/partners/data_and_infrastructure_agility/leads_capture/justuno/)는 동적 세그먼트를 통해 모든 청중을 위한 완전히 최적화된 방문자 경험을 생성할 수 있게 해주며, 가장 진보된 타겟팅을 제공하여 사이트 속도나 개발 작업에 영향을 주지 않습니다.

#### Odicci - 고객 데이터 플랫폼

Braze를 [Odicci]({{site.baseurl}}/partners/message_personalization/dynamic_content/odicci/)와 통합하여, 기업이 로열티 기반의 옴니채널 경험을 통해 고객을 획득하고, 참여시키며, 유지할 수 있도록 합니다.

#### Optimizely - A/B 테스트

Braze와 [Optimizely]({{site.baseurl}}/partners/data_and_infrastructure_agility/ab_testing/optimizely/) 통합은 양방향 통합으로, 다음을 가능하게 합니다:

- Braze 고객 세그먼트와 이벤트를 매일 밤 Optimizely 데이터 플랫폼(ODP)과 동기화하여 Optimizely 고객 프로필, 보고서 및 세분화를 풍부하게 합니다.
- Braze에서 Optimizely의 보고 도구로 Braze Currents 이벤트를 전송합니다.
- ODP 고객 데이터와 이벤트를 Braze와 동기화하여 Braze 고객 데이터를 풍부하게 하고 ODP의 고객 이벤트에 따라 Braze 메시징을 트리거합니다.

## 2024년 12월 10일 출시

### IP 주소별 SDK 사용자 위치

2024년 11월 26일부터 Braze는 첫 번째 SDK 세션이 시작될 때부터 IP 주소를 사용하여 지리적으로 위치한 국가의 사용자 위치를 감지합니다. Braze는 IP 주소를 사용하여 SDK를 통해 생성된 사용자 프로필의 국가 값을 설정하며, 첫 번째 세션 중과 이후에도 IP 기반 국가 설정을 사용할 수 있습니다. 자세한 내용은 [위치 추적을]({{site.baseurl}}/user_guide/engagement_tools/locations_and_geofences/location_tracking/) 참조하세요.

### 고급 액세스 설정

[향상된 액세스]({{site.baseurl}}/user_guide/administrative/app_settings/company_settings/security_settings/#elevated-access) 권한은 Braze 대시보드의 민감한 작업에 대한 보안을 한층 더 강화합니다. 활성화된 경우, 사용자는 세그먼트를 내보내거나 API 키를 보기 전에 계정을 다시 인증해야 합니다. 상승된 액세스를 사용하려면 **설정** > **관리자 설정** > **보안 설정으로** 이동하여 이 기능을 켜세요.

### 개인 식별 정보(PII) 보기 권한

관리자의 경우, 사용자가 Liquid 변수를 사용하여 사용자 속성에 액세스하는 메시지 미리 보기의 대시보드에서 회사에서 정의한 [PII를 볼 수 있도록 허용할]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#list-of-permissions) 수 있습니다. 

워크스페이스의 경우, 사용자가 대시보드에서 회사에서 정의한 대로 PII를 볼 수 있도록 허용하거나 사용자 프로필을 보되 회사에서 PII로 식별한 필드를 삭제할 수 있습니다.

### 데이터 유연성

#### 데이터 레이크 스키마

원시 테이블 스키마에 다음 스키마가 추가되었습니다:
- `USERS_CANVASSTEP_PROGRESSION_SHARED`: 캔버스에서 사용자에 대한 진행 이벤트
- `CHANGELOGS_GLOBALCONTROLGROUP_SHARED`: 현재 및 이전 글로벌 컨트롤 그룹에 있는 임의의 버킷 번호 식별하기
- `USERS_MESSAGES_FEATUREFLAG_IMPRESSION_SHARED`: 사용자가 기능 플래그를 볼 때의 노출 이벤트

#### 계정 기반 세분화

B2B 데이터 모델을 설정하는 방식에 따라 두 가지 방법으로 [B2B(기업 간) 계정 기반 세분화를]({{site.baseurl}}/user_guide/getting_started/b2b_use_cases/account_based_segmentation/) 수행할 수 있습니다:

- 비즈니스 개체에 카탈로그를 사용하는 경우
- 비즈니스 개체에 연결된 소스를 사용하는 경우

#### 세분화 필터

세분화 [필터의]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters) 전체 목록과 설명은 세분화 필터를 참조하세요.

##### 다음에서 생성된 사용자 프로필

사용자 프로필이 생성된 시점을 기준으로 사용자를 세분화합니다. 사용자가 CSV 또는 API를 통해 추가된 경우 이 필터는 사용자가 추가된 날짜를 반영합니다. 사용자가 CSV 또는 API로 추가되지 않았고 SDK에서 첫 번째 세션을 추적하는 경우 이 필터는 첫 번째 세션의 날짜를 반영합니다.

##### 전화번호 보내기

e.164 전화번호 필드로 사용자를 세분화합니다. 이 필터와 함께 정규식을 사용하여 특정 국가 코드가 포함된 전화번호를 기준으로 세분화할 수 있습니다.

### 새로운 Braze 파트너십

#### Narvar - 전자상거래

Braze와 [Narvar의](https://corp.narvar.com/) 통합을 통해 브랜드는 Narvar의 알림 이벤트를 활용하여 Braze에서 직접 메시지를 트리거함으로써 고객에게 적시에 업데이트된 정보를 제공할 수 있습니다.

#### 전류용 Zeotap - 고객 데이터 플랫폼

Braze와 [Zeotap의](https://zeotap.com/) 통합을 통해 Zeotap 고객 세그먼트를 Braze 사용자 프로필에 동기화하여 캠페인의 규모와 도달 범위를 확장할 수 있습니다. [Currents를]({{site.baseurl}}/user_guide/data/braze_currents/) 사용하면 데이터를 Zeotap에 연결하여 전체 성장 스택에서 실행 가능한 데이터로 만들 수도 있습니다.

#### 알림 - 동적 콘텐츠

브라즈와 [노티파이의](https://notifyai.io/) 통합을 통해 마케터는 다양한 플랫폼에서 효과적으로 참여를 유도할 수 있습니다. 기존 마케팅 방식에 의존하는 대신, Braze API로 트리거되는 캠페인은 Notify의 기능을 활용하여 이메일, SMS, 푸시 알림 등 여러 채널을 통해 개인화된 메시지를 전달할 수 있습니다.

#### Contentful - 동적 콘텐츠

브레이즈와 [콘텐츠풀의](https://www.contentful.com/) 통합을 통해 커넥티드 콘텐츠를 동적으로 사용하여 콘텐츠풀의 콘텐츠를 브레이즈 캠페인으로 가져올 수 있습니다.

#### 아웃그로우 - 리드 캡처 

브레이즈와 [아웃그로우의](https://outgrow.co/) 통합을 통해 아웃그로우의 사용자 데이터를 자동으로 브레이즈로 전송하여 고도로 개인화된 타겟팅 캠페인을 진행할 수 있습니다.

### SDK 업데이트

다음 SDK 업데이트가 릴리스되었습니다. 주요 업데이트는 아래에 나열되어 있으며, 그 외의 모든 업데이트는 해당 SDK 체인지로그를 확인하면 확인할 수 있습니다.

- [웹 SDK 5.6.1](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md)
- [Flutter SDK 12.0.0](https://github.com/braze-inc/braze-flutter-sdk/releases/tag/12.0.0)
    - [브레이즈 스위프트 SDK 10.3.1에서 11.3.0으로](https://github.com/braze-inc/braze-swift-sdk/compare/10.3.1...11.3.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed) 네이티브 iOS 브릿지 업데이트
    - 네이티브 안드로이드 브릿지를 [Braze 안드로이드 SDK 32.1.0에서 33.1.0으로](https://github.com/braze-inc/braze-android-sdk/compare/v32.1.0...v33.1.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed) 업데이트합니다.
- [Swift SDK 11.0.1](https://github.com/braze-inc/braze-swift-sdk/blob/11.0.1/CHANGELOG.md)

## 2024년 11월 12일 출시
 
### 데이터 유연성
 
#### 속도 제한 `/users/track`

[`/users/track` 엔드포인트의]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) 속도 제한이 3초당 3,000으로 업데이트되었습니다.
 
### 창의력 발휘

#### 캔버스 사용 사례

브레이즈 캔버스를 활용할 수 있는 다양한 방법을 보여주는 몇 가지 사용 사례를 정리해 보았습니다. 영감을 얻고 싶다면 아래에서 사용 사례를 선택하여 시작하세요.

- [포기된 장바구니]({{site.baseurl}}/user_guide/engagement_tools/canvas/get_started/braze_templates/abandoned_cart/)
- [재고 있음]({{site.baseurl}}/user_guide/engagement_tools/canvas/get_started/braze_templates/back_in_stock/)
- [기능 채택]({{site.baseurl}}/user_guide/engagement_tools/canvas/get_started/braze_templates/feature_adoption/)
- [휴면 사용자]({{site.baseurl}}/user_guide/engagement_tools/canvas/get_started/braze_templates/lapsed_user/)
- [온보딩]({{site.baseurl}}/user_guide/engagement_tools/canvas/get_started/braze_templates/onboarding/)
- [구매 후 피드백]({{site.baseurl}}/user_guide/engagement_tools/canvas/get_started/braze_templates/post_purchase_feedback/)

### 강력한 채널

#### LINE

{% multi_lang_include release_type.md release="일반 사용 가능" %}

이제 Braze의 LINE 연동이 정식 출시되었습니다! LINE은 일본에서 가장 인기 있는 메시징 앱으로, 월간 활성 사용자가 9,500만 명이 넘습니다. 메시징 외에도 LINE은 사용자에게 소셜 미디어, 게임, 쇼핑 및 결제를 위한 "올인원" 플랫폼을 제공합니다.

시작하려면 [LINE 문서를]({{site.baseurl}}/user_guide/message_building_by_channel/line/) 참조하세요.
 
#### LinkedIn 잠재고객 동기화

{% multi_lang_include release_type.md release="베타" %}

이제 최고의 소셜 및 광고 기술로 캠페인의 도달 범위를 확장하는 데 도움이 되는 도구인 [Braze Audience Sync와]({{site.baseurl}}/partners/canvas_steps/) 함께 LinkedIn을 사용할 수 있습니다. 베타 버전에 참여하려면 Braze 성공 관리자에게 문의하세요.
 
### 개발자 가이드 개선
 
현재 [Braze 개발자 가이드를]({{site.baseurl}}/developer_guide/home/) 대대적으로 개선하는 작업을 진행 중입니다. 첫 번째 단계로 탐색을 간소화하고 중첩된 섹션의 수를 줄였습니다. 

|이전|이후|
|------|-----|
|!["브레이즈 개발자 가이드의 이전 탐색."]({% image_buster /assets/img/release_notes/developer_guide_improvements/old_navigation.png %})|!["Braze 개발자 가이드의 새로운 내비게이션."]({% image_buster /assets/img/release_notes/developer_guide_improvements/new_navigation.png %})|

### 새로운 Braze 파트너십
 
#### 내 엽서

선도적인 글로벌 엽서 앱인 [MyPostcard를](https://www.mypostcard.com/) 사용하면 다이렉트 메일 캠페인을 쉽게 실행하여 고객과 원활하고 수익성 있는 방식으로 소통할 수 있습니다. 시작하려면 [내 엽서를 Braze와 통합하기를]({{site.baseurl}}/partners/message_orchestration/additional_channels/direct_mail/mypostcard/) 참조하세요.
 
### SDK 업데이트
 
다음 SDK 업데이트가 릴리스되었습니다. 주요 업데이트는 아래에 나열되어 있으며, 그 외의 모든 업데이트는 해당 SDK 체인지로그를 확인하면 확인할 수 있습니다.
 
- [엑스포 플러그인 3.0.0](https://github.com/braze-inc/braze-expo-plugin/blob/main/CHANGELOG.md)
    - 이 버전을 사용하려면 Braze React Native SDK 13.1.0이 필요합니다.
    - BrazeReactUtils.populateInitialUrl 의 iOS BrazeAppDelegate 메서드 호출을 BrazeReactUtils.populateInitialPayload 로 바꿉니다.
        - 이 업데이트는 애플리케이션이 종료된 상태에서 알림을 클릭하면 푸시 열기 이벤트가 트리거되지 않던 문제를 해결합니다.
        - 이 업데이트를 완전히 활용하려면 자바스크립트 코드에서 Braze.getInitialURL 호출을 모두 Braze.getInitialPushPayload 로 바꾸세요. 이제 초기 URL은 초기 푸시 페이로드의 URL 속성을 통해 액세스할 수 있습니다.
- [브레이즈 세그먼트 스위프트 플러그인 5.0.0](https://github.com/braze-inc/braze-segment-swift/blob/main/CHANGELOG.md)
    - 11.1.1+ SemVer 종파의 릴리스가 필요하도록 Braze Swift SDK 바인딩을 업데이트합니다.
    - 이를 통해 11.1.1부터 12.0.0까지 모든 버전의 Braze SDK와 호환됩니다.
    - 잠재적인 변경 사항에 대한 자세한 내용은 11.1.1의 변경 로그 항목을 참조하세요.

## 2024년 10월 15일 출시

### 데이터 유연성

#### 캠페인 및 캔버스

캠페인 및 캔버스를 생성하는 동안 [정확한 통계 계산을]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/#statistics-for-segment-size) 선택하여 기본 추정치 대신 타겟 오디언스에서 도달 가능한 정확한 사용자 수를 계산할 수 있습니다.

#### API Android 개체

[`android_priority` 매개변수는]({{site.baseurl}}/api/objects_filters/messaging/android_object/#additional-parameter-details) "normal" 또는 "high" 값을 사용하여 FCM 발신자 우선순위를 지정할 수 있습니다. 기본적으로 알림 메시지는 높은 우선순위로 전송되고 데이터 메시지는 일반 우선순위로 전송됩니다.

다양한 값이 배달에 미치는 영향에 대한 자세한 내용은 [Android 메시지 우선순위를](https://firebase.google.com/docs/cloud-messaging/android/message-priority/) 참조하세요.

#### SDK

앱에서 자세한 로깅을 활성화하지 않고도 [Braze SDK에 내장된 디버거를]({{site.baseurl}}/developer_guide/debugging/) 사용하여 SDK 기반 채널의 문제를 해결할 수 있습니다.

#### 라이브 활동

스위프트 라이브 활동에 대한 [자주 묻는 질문과]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/live_activities/faq/) 답변에 몇 가지 새로운 질문과 답변이 추가되었습니다.

#### 사용자 지정 이벤트

이제 배열 또는 개체 값을 포함하는 [이벤트 속성 개체는]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#custom-event-properties) 최대 100KB의 이벤트 속성 페이로드를 가질 수 있습니다.

#### 무작위 버킷 번호

A/B 테스트 또는 캠페인의 특정 사용자 그룹 타겟팅을 위해 [무작위 버킷 번호로 무작위 오디언스 재입력을]({{site.baseurl}}/user_guide/engagement_tools/testing/random_bucket_numbers/#random-audience-re-entry-using-random-bucket-numbers) 사용하세요.

#### 세그먼트 확장

세그먼트 확장을 새로 고칠 빈도(매일, 매주 또는 매월)와 새로 고침할 특정 시간을 선택하여 [반복되는 일정에 따라 세그먼트 확장을]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/#setting-up-a-recurring-refresh) 새로 고칠 수 있습니다.

### 강력한 채널

#### SMS

Google 애널리틱스와 같은 타사 분석 도구에서 캠페인의 성과를 추적할 수 있도록 SMS 메시지에서 UTM 매개변수를 사용하는 방법을 설명하기 위해 [UTM 매개변수 추가]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/link_shortening/#using-link-shortening) 하기 기능을 추가했습니다.

#### 랜딩 페이지

[자체 도메인을 Braze 작업 영역에 연결하여]({{site.baseurl}}/user_guide/engagement_tools/landing_pages/customizing_urls/) 브랜드에 맞게 랜딩 페이지 URL을 사용자 지정하세요.

#### LINE과 Braze

{% multi_lang_include release_type.md release="베타" %}

새로운 문서를 추가했습니다:

- LINE [메시지 유형은]({{site.baseurl}}/line/create/message_types/) 작성할 수 있는 LINE 메시지 유형과 그 특징 및 제한 사항을 다루며, LINE 베타 컬렉션의 일부입니다.
- [사용자 계정 연동을]({{site.baseurl}}/line/line_setup/#user-account-linking) 통해 사용자는 LINE 계정을 앱의 사용자 계정과 연결할 수 있습니다. 그런 다음, 예를 들어 {% raw %}`{{line_id}}`{% endraw %} 과 같은 Braze의 Liquid를 사용하여 사용자의 LINE ID를 웹사이트나 앱에 전달하는 사용자 맞춤 URL을 생성하고, 이를 알려진 사용자와 연결할 수 있습니다.

#### WhatsApp 및 Braze

이제 [WhatsApp 비즈니스 계정(WABA)]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/#step-2-whatsapp-setup) 을 여러 비즈니스 솔루션 제공업체와 공유할 수 있습니다.

### 새로운 Braze 파트너십

#### 미래 국가 - 동적 콘텐츠

브레이즈와 [퓨처 앤썸의]({{site.baseurl}}/partners/message_personalization/dynamic_content/future_anthem/) 파트너십은 Amplifier AI를 활용하여 콘텐츠 개인화, 실시간 경험, 역동적인 오디언스를 제공합니다. Amplifier AI는 스포츠, 카지노, 복권 전반에 걸쳐 작동하며, 좋아하는 게임, 참여 점수, 다음 예상 베팅 등 업계별 플레이어 속성을 통해 Braze 플레이어 프로필을 향상시킬 수 있습니다.

### 설정

#### 구분 기호 필드 수준 암호화

{% multi_lang_include release_type.md release="일반 사용 가능" %}

[식별자 필드 수준 암호화를]({{site.baseurl}}/user_guide/analytics/field_level_encryption/) 사용하면 AWS 키 관리 서비스(KMS)로 이메일 주소를 원활하게 암호화하여 Braze에서 공유되는 개인 식별 정보(PII)를 최소화할 수 있습니다. 암호화는 민감한 데이터를 읽을 수 없는 암호화된 정보인 암호 텍스트로 대체합니다.

### SDK 업데이트

다음 SDK 업데이트가 릴리스되었습니다. 주요 업데이트는 아래에 나열되어 있으며, 그 외의 모든 업데이트는 해당 SDK 체인지로그를 확인하면 확인할 수 있습니다.

- [Swift SDK 10.3.1](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#1110)
- [Swift SDK 11.0.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#1110)
    - [Swift 6 엄격한 동시성 검사](https://developer.apple.com/documentation/swift/adoptingswift6) 지원 추가
        - 이제 관련 공용 Braze 클래스와 데이터 유형은 `Sendable` 프로토콜을 준수하며 동시성 컨텍스트에서 안전하게 사용할 수 있습니다.
        - 이제 메인 스레드 전용 API는 `@MainActor` 속성으로 표시됩니다.
        - 컴파일러에서 생성되는 경고 수를 최소화하면서 이러한 기능을 활용하려면 Xcode 16.0 이상을 사용하는 것이 좋습니다. 이전 버전의 Xcode를 계속 사용할 수 있지만 일부 기능에서 경고가 발생할 수 있습니다.
    - 푸시 알림 지원을 수동으로 통합하는 경우 경고를 방지하기 위해 `@preconcurrency` 속성을 사용하도록 `UNUserNotificationCenterDelegate` 준수를 업데이트해야 할 수 있습니다.
        - 프로토콜 준수에 `@preconcurrency` 속성을 적용하는 것은 Xcode 16.0 이상에서만 사용할 수 있습니다. [여기에서](https://github.com/braze-inc/braze-swift-sdk/tree/main/Examples/Swift/Sources/PushNotifications-Manual) 샘플 통합 코드를 참조하세요.
- [React Native SDK 13.0.0](https://github.com/braze-inc/braze-react-native-sdk/blob/master/CHANGELOG.md#1300)
    - 기본 Android 버전 바인딩을 [Braze Android SDK 31.1.0에서 32.1.0으로](https://github.com/braze-inc/braze-android-sdk/compare/v31.1.0...v32.1.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed) 업데이트합니다.
    - [브라즈 스위프트 SDK 10.3.0에서 11.0.0으로](https://github.com/braze-inc/braze-swift-sdk/compare/10.3.0...11.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed) 기본 iOS 버전 바인딩을 업데이트합니다.
- [Flutter SDK 11.1.0](https://pub.dev/packages/braze_plugin/changelog#1110)
- [Swift SDK 11.1.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#1110)
- [Android SDK 33.0.0](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#3300)
    - Kotlin을 1.8에서 Kotlin 2.0으로 업데이트했습니다.
- [웹 SDK 5.5.0](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md#550)

## 2024년 9월 17일 출시

### 데이터 유연성

#### S3용 Braze 클라우드 데이터 수집

[S3용 클라우드 데이터 수집(CDI)]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/file_storage_integrations/#aws-definitions) 을 사용하여 AWS 계정에 있는 하나 이상의 S3 버킷을 Braze와 직접 통합할 수 있습니다. 새 파일이 S3에 게시되면 SQS에 메시지가 게시되고 Braze 클라우드 데이터 수집이 해당 새 파일을 받습니다.

#### 월간 활성 사용자 CY 24-25

월간 활성 사용자 - CY 24-25를 구매한 고객의 경우, Braze는 `/users/track` 엔드포인트에서 다양한 요금 한도를 관리합니다. 자세한 내용은 [POST를 참조하세요: 사용자 추적]({{site.baseurl}}/api/endpoints/user_data/post_user_track/#monthly-active-users-cy-24-25). 

### 창의력 발휘

#### Liquid를 포함한 카탈로그 항목 템플릿

{% multi_lang_include release_type.md release="조기 액세스" %}

Liquid 태그에 `:rerender` 플래그를 사용하여 [카탈로그 항목의 Liquid 콘텐츠를 렌더링합니다]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/catalog/#using-liquid). 예를 들어 다음과 같은 리퀴드 콘텐츠를 렌더링하는 경우입니다:

{% raw %}
```liquid
Hi ${first_name}
{% catalog_items Messages greet_msg :rerender %}
{{ items[0].Welcome_Message }}
```
{% endraw %}

다음과 같이 표시됩니다:

{% raw %}
```
Hi Peter,
Welcome to our store, Peter!
```
{% endraw %}

### 강력한 채널

#### WhatsApp 응답 메시지

{% multi_lang_include release_type.md release="일반 사용 가능" %}

[응답 메시지를]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/create#response-messages) 사용하여 사용자의 인바운드 WhatsApp 메시지에 답장할 수 있습니다. 이 메시지는 작성 경험 중에 Braze에서 앱 내에서 작성되며 언제든지 편집할 수 있습니다. Liquid을 사용하여 응답 메시지 언어를 적절한 사용자에게 맞출 수 있습니다.

#### 캔버스 템플릿

{% multi_lang_include release_type.md release="일반 사용 가능" %}

캔버스 [템플릿을]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_templates/) 만들어 캔버스 전반에서 특정 목표에 맞게 쉽게 사용자 지정할 수 있는 일관된 프레임워크를 만들어 메시지를 구체화할 수 있습니다.

#### 랜딩 페이지

{% multi_lang_include release_type.md release="베타" %}

브레이즈 [랜딩 페이지는]({{site.baseurl}}/user_guide/engagement_tools/landing_pages) 사용자 확보 및 참여 전략을 추진할 수 있는 독립형 웹페이지입니다.

#### 마지막으로 본 이후 변경 사항

각 개요 페이지(예: [이메일 캠페인의]({{site.baseurl}}/user_guide/message_building_by_channel/email/reporting_and_analytics/email_reporting#changes-since-last-viewed) 개요 페이지)에서 *마지막으로 본 이후 변경사항* 지표를 참조하여 다른 팀원들이 [캔버스]({{site.baseurl}}/user_guide/engagement_tools/canvas/testing_canvases/measuring_and_testing_with_canvas_analytics/#changes-since-last-viewed), 캠페인 및 [세그먼트에]({{site.baseurl}}/user_guide/engagement_tools/segments/managing_segments/#changes-since-last-viewed) 업데이트한 횟수를 확인할 수 있습니다. 

#### 웹훅 및 커넥티드 콘텐츠 요청 문제 해결하기 

[이 문서에서는]({{site.baseurl}}/help/help_articles/api/webhook_connected_content_errors) 웹훅 및 커넥티드 콘텐츠 오류 코드를 해결하는 방법과 오류의 유형 및 해결 단계를 설명합니다.

### 새로운 Braze 파트너십

#### 인박스 몬스터 - 분석

[인박스 몬스터는]({{site.baseurl}}/partners/data_and_infrastructure_agility/analytics/inbox_monster/) 기업 브랜드가 모든 이메일을 수신할 수 있도록 도와주는 받은 편지함 신호 플랫폼입니다. 전달성, 크리에이티브 렌더링 및 SMS 모니터링을 위한 통합 솔루션 제품군으로, 최신 고객 관계 관리(CRM) 팀의 역량을 강화하고 이메일 전송에 대한 두려움을 없애줍니다.

#### SessionM - 로열티

[세션엠은]({{site.baseurl}}/partners/message_orchestration/channel_extensions/loyalty/sessionm/) 고객 참여 및 로열티 플랫폼으로, 마케터가 타겟팅된 아웃리치를 통해 참여도와 수익성을 높일 수 있도록 캠페인 관리 기능과 로열티 관리 솔루션을 제공합니다.

### AI 및 ML 자동화

#### 인기 있는 아이템 추천

"AI 개인화된" 모델 외에도, [AI 항목 추천]({{site.baseurl}}/user_guide/sage_ai/recommendations/about_item_recommendations/#trending) 기능에는 "트렌딩" 추천 모델도 포함되어 있습니다. 이 모델은 최근 사용자 상호작용에서 가장 긍정적인 모멘텀을 보인 항목들을 특징으로 합니다.

### 설정

#### 역할

{% multi_lang_include release_type.md release="일반 사용 가능" %}

[역할은]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#creating-a-role) 개별 사용자 지정 권한과 워크스페이스 액세스 제어를 함께 묶어 보다 체계적으로 관리할 수 있도록 해줍니다. 이는 하나의 대시보드에 여러 브랜드나 로컬 워크스페이스가 있는 경우 특히 유용합니다. 역할을 사용하면 대시보드 사용자를 올바른 워크스페이스에 추가하고 관련 권한을 직접 부여할 수 있습니다. 

#### 보안 이벤트 보고서

다운로드한 보안 보고서 이벤트에 표시될 수 있는 [보안 이벤트의]({{site.baseurl}}/user_guide/administrative/app_settings/company_settings/security_settings/#downloading-a-security-event-report) 전체 목록을 추가했습니다.

#### 메시지 사용량 보고서

{% multi_lang_include release_type.md release="조기 액세스" %}

[메시지 사용량 대시보드에서는]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_campaign_analytics/message_usage/) SMS 및 WhatsApp 크레딧 사용량에 대한 셀프 서비스 인사이트를 제공하여 계약 할당량과 비교한 과거 및 현재 사용량을 종합적으로 볼 수 있습니다. 이러한 인사이트를 통해 혼란을 줄이고 초과 위험을 방지하기 위한 조정에 도움을 받을 수 있습니다.

### SDK

#### 브레이즈 스위프트 SDK의 초기화가 지연되었습니다.

[지연 초기화를]({{site.baseurl}}/developer_guide/sdk_initalization/?sdktab=swift) 설정하여 푸시 알림 처리를 유지하면서 Braze Swift SDK를 비동기적으로 초기화할 수 있습니다. 서버에서 구성 데이터를 가져오거나 사용자 동의를 기다리는 등 SDK를 초기화하기 전에 다른 서비스를 설정해야 할 때 유용할 수 있습니다.

### SDK 업데이트

다음 SDK 업데이트가 릴리스되었습니다. 주요 업데이트는 아래에 나열되어 있으며, 그 외의 모든 업데이트는 해당 SDK 체인지로그를 확인하면 확인할 수 있습니다.

- [Android SDK 32.1.0](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#3210)
- [세그먼트 Kotlin SDK 2.0.0](https://github.com/braze-inc/braze-segment-kotlin/blob/main/CHANGELOG.md#200)
- [Swift SDK 10.1.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#1010)
- [React Native SDK 12.1.0](https://github.com/braze-inc/braze-react-native-sdk/blob/master/CHANGELOG.md#1210)
- [Cordova SDK 10.0.0](https://github.com/braze-inc/braze-cordova-sdk/blob/master/CHANGELOG.md#1000)
    - 이 버전을 사용하려면 이제 Cordova Android 13.0.0이 필요합니다.
    - 프로젝트 종속성 요구 사항의 전체 목록은 [코르도바 릴리스 공지를](https://cordova.apache.org/announcements/2024/05/23/cordova-android-13.0.0.html) 참조하세요.- 네이티브 안드로이드 브릿지를 [Braze 안드로이드 SDK 30.3.0에서 32.1.0으로](https://github.com/braze-inc/braze-android-sdk/compare/v30.3.0...v32.1.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed) 업데이트했습니다.
    - [브레이즈 스위프트 SDK 9.2.0에서 10.1.0으로](https://github.com/braze-inc/braze-swift-sdk/compare/9.2.0...10.1.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed) 네이티브 iOS 브릿지를 업데이트했습니다.
- [Swift SDK 10.2.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#1020)
- [Unity 7.0.0](https://github.com/braze-inc/braze-unity-sdk/blob/master/CHANGELOG.md#700)
    - 네이티브 안드로이드 브릿지를 [Braze 안드로이드 SDK 30.3.0에서 32.1.0으로](https://github.com/braze-inc/braze-android-sdk/compare/v30.3.0...v32.1.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed) 업데이트했습니다.
    - [브레이즈 스위프트 SDK 9.0.0에서 10.1.0으로](https://github.com/braze-inc/braze-swift-sdk/compare/9.0.0...10.1.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed) 네이티브 iOS 브릿지를 업데이트했습니다.
- [브레이즈 세그먼트 스위프트 플러그인 4.0.0](https://github.com/braze-inc/braze-segment-swift/blob/main/CHANGELOG.md#400)
    - 브레이즈 스위프트 SDK 바인딩을 업데이트하여 `10.2.0+` SemVer 디노미네이션의 릴리스가 필요하도록 합니다.
        - 이를 통해 `10.2.0` 에서 `11.0.0` 까지의 모든 버전의 Braze SDK와 호환이 가능합니다.
        - 변경 로그 항목을 참조하세요. [`10.0.0`](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#1000) 의 변경 로그 항목을 참조하세요.
- [Flutter SDK 11.0.0](https://pub.dev/packages/braze_plugin/changelog#1100)
    - 네이티브 안드로이드 브릿지를 [Braze 안드로이드 SDK 30.4.0에서 32.1.0으로](https://github.com/braze-inc/braze-android-sdk/compare/v30.4.0...v32.1.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed) 업데이트합니다.
        - 호출된 후에도 외부 구독(예: `subscribeToContentCards()`)을 유지하도록 Android에서 `wipeData()` 의 동작을 변경합니다.
    - 네이티브 iOS 브릿지를 [Braze Swift SDK 9.0.0에서 10.2.0으로](https://github.com/braze-inc/braze-swift-sdk/compare/9.0.0...10.2.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed) 업데이트합니다.
- [Swift SDK 10.3.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#1030)
- [Unity 7.1.0](https://github.com/braze-inc/braze-unity-sdk/blob/master/CHANGELOG.md#710)
- [React Native SDK 12.2.0](https://github.com/braze-inc/braze-react-native-sdk/blob/master/CHANGELOG.md#1220)

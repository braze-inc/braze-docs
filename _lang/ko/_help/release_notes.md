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

## 2024년 11월 12일 출시
 
### 데이터 유연성
 
#### `/users/track`에 대한 속도 제한

[`/users/track` 엔드포인트]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)의 속도 제한이 3초당 3,000으로 업데이트되었습니다.
 
### 창의력 발휘

#### 캔버스 사용 사례

우리는 Braze Canvas를 활용할 수 있는 다양한 방법을 보여주는 몇 가지 사용 사례를 모았습니다. 영감을 찾고 있다면, 시작하기 위해 아래의 사용 사례를 선택하세요.

- [포기된 장바구니]({{site.baseurl}}/user_guide/engagement_tools/canvas/get_started/braze_templates/abandoned_cart/)
- 재입고됨
- [기능 채택]({{site.baseurl}}/user_guide/engagement_tools/canvas/get_started/braze_templates/feature_adoption/)
- [소멸된 사용자]({{site.baseurl}}/user_guide/engagement_tools/canvas/get_started/braze_templates/lapsed_user/)
- [온보딩]({{site.baseurl}}/user_guide/engagement_tools/canvas/get_started/braze_templates/onboarding/)
- 구매 후 피드백

### 강력한 채널

#### LINE

{% multi_lang_include release_type.md release="일반 사용 가능" %}

브레이즈의 LINE 통합이 이제 일반적으로 제공됩니다! 라인은 일본에서 가장 인기 있는 메시징 앱으로, 월 9,500만 명 이상의 활성 사용자를 보유하고 있습니다. 메시징 외에도 LINE은 사용자에게 소셜 미디어, 게임, 쇼핑 및 결제를 위한 "올인원" 플랫폼을 제공합니다.

시작하려면 [LINE 설명서]({{site.baseurl}}/user_guide/message_building_by_channel/line/)을(를) 참조하세요.
 
#### 링크드인 오디언스 동기화

{% multi_lang_include release_type.md release="베타" %}

이제 [Braze Audience Sync]({{site.baseurl}}/partners/canvas_steps/)를 사용하여 LinkedIn을 사용할 수 있습니다. 이 도구는 캠페인의 도달 범위를 많은 주요 소셜 및 광고 기술로 확장하는 데 도움을 줍니다. 베타에 참여하려면 Braze 성공 매니저에게 연락하세요.
 
### 개발자 가이드 개선
 
우리는 [Braze Developer Guide]({{site.baseurl}}/developer_guide/home/)에 대한 주요 개선 작업을 진행 중입니다. 첫 번째 단계로, 우리는 탐색을 단순화하고 중첩 섹션의 수를 줄였습니다. 

|이전|이후|
|------|-----|
|!["브레이즈 개발자 가이드의 오래된 내비게이션."]({% image_buster /assets/img/release_notes/developer_guide_improvements/old_navigation.png %})|!["브레이즈 개발자 가이드의 새로운 내비게이션입니다."]({% image_buster /assets/img/release_notes/developer_guide_improvements/new_navigation.png %})|

### 새로운 Braze 파트너십
 
#### 내 엽서

[마이포스트카드](https://www.mypostcard.com/)는 선도적인 글로벌 포스트카드 앱으로, 귀하가 손쉽게 다이렉트 메일 캠페인을 실행할 수 있도록 지원하며, 고객과 연결하는 원활하고 수익성 있는 방법을 제공합니다. 시작하려면 [MyPostcard를 Braze와 통합하기]({{site.baseurl}}/partners/message_orchestration/additional_channels/direct_mail/mypostcard/)를 참조하세요.
 
### SDK 업데이트
 
다음 SDK 업데이트가 릴리스되었습니다. 주요 업데이트는 아래에 나열되어 있으며, 그 외의 모든 업데이트는 해당 SDK 체인지로그를 확인하면 확인할 수 있습니다.
 
- [엑스포 플러그인 3.0.0](https://github.com/braze-inc/braze-expo-plugin/blob/main/CHANGELOG.md)
    - 이 버전은 Braze React Native 소프트웨어 개발 키트의 13.1.0이 필요합니다.
    - BrazeReactUtils.populateInitialUrl의 iOS BrazeAppDelegate 메서드 호출을 BrazeReactUtils.populateInitialPayload로 교체합니다.
        - 이 업데이트는 애플리케이션이 종료된 상태일 때 알림을 클릭할 때 푸시 열린 이벤트가 트리거되지 않는 문제를 해결합니다.
        - 이 업데이트를 완전히 활용하려면 JavaScript 코드에서 Braze.getInitialURL의 모든 호출을 Braze.getInitialPushPayload로 교체하십시오. 초기 URL은 이제 초기 푸시 페이로드의 url 속성을 통해 접근할 수 있습니다.
- [Braze 세그먼트 Swift Plugin 5.0.0](https://github.com/braze-inc/braze-segment-swift/blob/main/CHANGELOG.md)
    - Braze Swift SDK 바인딩을 11.1.1+ SemVer 명칭의 릴리스를 요구하도록 업데이트합니다.
    - 이것은 11.1.1 버전부터 12.0.0 미만의 모든 Braze SDK 버전과의 호환성을 허용합니다.
    - 11.1.1의 체인지로그 항목을 참조하여 잠재적인 중단 변경 사항에 대한 자세한 정보를 확인하십시오.

## 2024년 10월 15일 출시

### 데이터 유연성

#### 캠페인 및 캔버스

캠페인과 캔버스를 생성하는 동안 기본 추정치 대신 [정확한 통계 계산]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/#statistics-for-segment-size)을 선택하여 목표 오디언스에서 도달 가능한 사용자 수를 정확하게 계산할 수 있습니다.

#### API Android 객체

[`android_priority` 매개변수]({{site.baseurl}}/api/objects_filters/messaging/android_object/#additional-parameter-details)는 FCM 발신자 우선 순위를 지정하기 위해 "normal" 또는 "high" 값을 허용합니다. 기본값으로 알림 메시지는 높은 우선 순위로 전송되며, 데이터 메시지는 일반 우선 순위로 전송됩니다.

더 많은 정보는 다양한 값이 전달에 미치는 영향을 보려면 [Android 메시지 우선순위](https://firebase.google.com/docs/cloud-messaging/android/message-priority/)를 참조하세요.

#### SDK

[Braze SDK의 내장 디버거]({{site.baseurl}}/developer_guide/platform_wide/debugging/)를 사용하여 앱에서 자세한 로깅을 활성화할 필요 없이 SDK 기반 채널의 문제를 해결하세요.

#### 라이브 활동

Swift Live Activities에 대한 [자주 묻는 질문]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/live_activities/faq/)을 몇 가지 새로운 질문과 답변으로 업데이트했습니다.

#### 사용자 지정 이벤트

[이벤트 속성정보 객체]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#custom-event-properties) 배열 또는 객체 값을 포함하는 [이벤트 속성정보]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#custom-event-properties) 페이로드는 이제 최대 100 KB까지 가질 수 있습니다.

#### 무작위 버킷 번호

[무작위 오디언스 재진입과 무작위 버킷 번호]({{site.baseurl}}/user_guide/engagement_tools/testing/random_bucket_numbers/#random-audience-re-entry-using-random-bucket-numbers)를 A/B 테스트 또는 특정 사용자 그룹을 타겟팅하는 데 사용하세요.

#### 세그먼트 확장

당신은 [새로고침 세그먼트 확장]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/#setting-up-a-recurring-refresh)을(를) 주기적으로 설정하여 선택한 빈도(매일, 매주 또는 매월)와 새로고침이 발생할 특정 시간을 지정할 수 있습니다.

### 강력한 채널

#### SMS

우리는 [UTM 매개변수 추가]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/link_shortening/#using-link-shortening)를 추가하여 SMS 메시지에서 UTM 매개변수를 사용하는 방법을 보여주었습니다. 이를 통해 Google Analytics와 같은 타사 분석 도구에서 캠페인의 성과를 추적할 수 있습니다.

#### 랜딩 페이지

[자신의 도메인]({{site.baseurl}}/user_guide/engagement_tools/landing_pages/connect_domain/)을 Braze 작업 공간에 연결하여 브랜드에 맞게 랜딩 페이지 URL을 사용자 정의하세요.

#### LINE과 Braze

{% multi_lang_include release_type.md release="베타" %}

우리는 새로운 설명서를 추가했습니다:

- [LINE 메시지 유형]({{site.baseurl}}/line/create/message_types/)는 작성할 수 있는 LINE 메시지 유형, 포함된 측면 및 제한 사항을 다루며, LINE 베타 컬렉션의 일부입니다.
- [사용자 계정 연결]({{site.baseurl}}/line/line_setup/#user-account-linking)을 통해 사용자는 LINE 계정을 귀하의 앱 사용자 계정에 연결할 수 있습니다. 그런 다음 {% raw %}`{{line_id}}`{% endraw %}와 같은 Braze에서 Liquid를 사용하여 사용자의 LINE ID를 귀하의 웹사이트나 앱으로 전달하는 개인화된 URL을 생성할 수 있으며, 이는 알려진 사용자와 연결될 수 있습니다.

#### WhatsApp과 Braze

[WhatsApp 비즈니스 계정 (WABA)]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/#step-2-whatsapp-setup) 이제 여러 비즈니스 솔루션 제공업체와 공유할 수 있습니다.

### 새로운 Braze 파트너십

#### 미래의 앤섬 - 동적 콘텐츠

브레이즈와 [Future Anthem]({{site.baseurl}}/partners/message_personalization/dynamic_content/future_anthem/) 파트너십은 Amplifier AI를 활용하여 콘텐츠 개인화, 실시간 경험 및 동적 청중을 제공합니다. 앰프리파이어 AI는 스포츠, 카지노 및 복권 전반에 걸쳐 작동하여 업계별 플레이어 속성(예: 좋아하는 게임, 참여 점수, 예상 다음 베팅 등)으로 Braze 플레이어 프로필을 향상시킬 수 있습니다.

### 설정

#### 식별자 필드 수준 암호화

{% multi_lang_include release_type.md release="일반 사용 가능" %}

[식별자 필드 수준 암호화]({{site.baseurl}}/user_guide/data_and_analytics/field_level_encryption/)을 사용하여, AWS 키 관리 서비스(KMS)로 이메일 주소를 원활하게 암호화하여 Braze에서 공유되는 개인 식별 정보(PII)를 최소화할 수 있습니다. 암호화는 민감한 데이터를 읽을 수 없는 암호화된 정보인 암호 텍스트로 대체합니다.

### SDK 업데이트

다음 SDK 업데이트가 릴리스되었습니다. 주요 업데이트는 아래에 나열되어 있으며, 그 외의 모든 업데이트는 해당 SDK 체인지로그를 확인하면 확인할 수 있습니다.

- [스위프트 소프트웨어 개발 키트 10.3.1](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#1110)
- [스위프트 소프트웨어 개발 키트 11.0.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#1110)
    - Swift 6의 엄격한 동시성 검사를 위한 지원을 추가합니다.
        - 관련된 공용 Braze 클래스와 데이터 유형은 이제 `Sendable` 프로토콜을 준수하며 동시성 컨텍스트에서 안전하게 사용할 수 있습니다.
        - 메인 스레드 전용 API는 이제 `@MainActor` 속성으로 표시됩니다.
        - 이러한 기능을 활용하면서 컴파일러가 생성하는 경고의 수를 최소화하려면 Xcode 16.0 이상을 사용하는 것이 좋습니다. 이전 버전의 Xcode는 여전히 사용할 수 있지만 일부 기능은 경고를 생성할 수 있습니다.
    - 푸시 알림 지원을 수동으로 통합할 때, 경고를 방지하기 위해 `UNUserNotificationCenterDelegate` 준수를 업데이트하고 `@preconcurrency` 속성을 사용해야 할 수 있습니다.
        - 프로토콜 준수에 `@preconcurrency` 속성을 적용하는 것은 Xcode 16.0 이상에서만 가능합니다. 샘플 통합 코드 [여기](https://github.com/braze-inc/braze-swift-sdk/tree/main/Examples/Swift/Sources/PushNotifications-Manual)를 참조하세요.
- [React Native 소프트웨어 개발 키트 13.0.0](https://github.com/braze-inc/braze-react-native-sdk/blob/master/CHANGELOG.md#1300)
    - 네이티브 Android 버전 바인딩을 [Braze Android SDK 31.1.0 to 32.1.0](https://github.com/braze-inc/braze-android-sdk/compare/v31.1.0...v32.1.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed)에서 업데이트합니다.
    - 네이티브 iOS 버전 바인딩을 [Braze Swift SDK 10.3.0 to 11.0.0](https://github.com/braze-inc/braze-swift-sdk/compare/10.3.0...11.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed) 업데이트합니다.
- [Flutter 소프트웨어 개발 키트 11.1.0](https://pub.dev/packages/braze_plugin/changelog#1110)
- [스위프트 소프트웨어 개발 키트 11.1.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#1110)
- [안드로이드 소프트웨어 개발 키트 33.0.0](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#3300)
    - Kotlin을 1.8에서 Kotlin 2.0으로 업데이트했습니다.
- [웹 소프트웨어 개발 키트 5.5.0](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md#550)

## 2024년 9월 17일 출시

### 데이터 유연성

#### 브레이즈 클라우드 데이터 수집을 위한 S3

[클라우드 데이터 수집 (CDI) for S3]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/file_storage_integrations/#aws-definitions)를 사용하여 AWS 계정의 하나 이상의 S3 버킷을 Braze와 직접 통합할 수 있습니다. 새 파일이 S3에 게시되면 SQS에 메시지가 게시되고 Braze 클라우드 데이터 수집이 해당하는 새 파일을 받습니다.

#### 요금 한도 증가

요청 유형 [/users/export/ids]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier)의 비율 제한이 분당 2,500 요청으로 증가했습니다.

#### 2024-2025년 월간 활성 사용자

월간 활성 사용자 - CY 24-25를 구매한 고객을 위해, Braze는 `/users/track` 엔드포인트에서 서로 다른 속도 제한을 관리합니다. 자세한 내용은 [POST를 참조하십시오. 사용자 추적]({{site.baseurl}}/api/endpoints/user_data/post_user_track/#monthly-active-users-cy-24-25). 

### 창의력 발휘

#### Liquid를 포함한 카탈로그 항목 템플릿

{% multi_lang_include release_type.md release="조기 액세스" %}

Liquid 태그에서 `:rerender` 플래그를 사용하여 [카탈로그 항목의 Liquid 콘텐츠]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/catalog/#using-liquid)를 렌더링합니다. 예를 들어, 다음 Liquid 콘텐츠를 렌더링하면:

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

사용자는 [응답 메시지]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/create#response-messages)를 사용하여 인바운드 WhatsApp 메시지에 응답할 수 있습니다. 이 메시지는 작성 경험 중에 Braze에서 앱 내에서 작성되며 언제든지 편집할 수 있습니다. Liquid을 사용하여 응답 메시지 언어를 적절한 사용자에게 맞출 수 있습니다.

#### 캔버스 템플릿

{% multi_lang_include release_type.md release="일반 사용 가능" %}

[캔버스 템플릿]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_templates/)을 만들어 메시징을 다듬어 특정 목표에 맞게 쉽게 사용자 정의할 수 있는 일관된 프레임워크를 만들 수 있습니다.

#### 랜딩 페이지

{% multi_lang_include release_type.md release="베타" %}

브레이즈 [랜딩 페이지]({{site.baseurl}}/user_guide/engagement_tools/landing_pages)는 사용자 확보 및 참여 전략을 추진할 수 있는 독립적인 웹페이지입니다.

#### 마지막으로 본 이후의 변경 사항

당신은 팀의 다른 구성원이 [캔버스]({{site.baseurl}}/user_guide/engagement_tools/canvas/testing_canvases/measuring_and_testing_with_canvas_analytics/#changes-since-last-viewed), 캠페인 및 [세그먼트]({{site.baseurl}}/user_guide/engagement_tools/segments/managing_segments/#changes-since-last-viewed)에 대한 업데이트 수를 *마지막으로 본 이후의 변경 사항* 지표를 참조하여 각 개요 페이지(예: [이메일 캠페인]({{site.baseurl}}/user_guide/message_building_by_channel/email/reporting_and_analytics/email_reporting#changes-since-last-viewed)의 개요 페이지)에서 확인할 수 있습니다. 

#### 문제 해결 웹훅 및 연결된 콘텐츠 요청 

[이 기사]({{site.baseurl}}/help/help_articles/api/webhook_connected_content_errors)는 웹훅 및 연결된 콘텐츠 오류 코드 문제를 해결하는 방법을 다루며, 오류가 무엇인지와 이를 해결하기 위한 단계가 포함되어 있습니다.

### 새로운 Braze 파트너십

#### 받은편지함 몬스터 - 분석

[받은편지함 몬스터]({{site.baseurl}}/partners/data_and_infrastructure_agility/analytics/inbox_monster/)는 기업 브랜드가 모든 발신을 수신할 수 있도록 돕는 받은편지함 신호 플랫폼입니다. 전달 가능성, 창의적인 렌더링 및 SMS 모니터링을 위한 통합 솔루션 모음으로, 현대 고객 관계 관리(CRM) 팀을 지원하고 발송에 대한 두려움을 없애줍니다.

#### SessionM - 로열티

[SessionM]({{site.baseurl}}/partners/message_orchestration/channel_extensions/loyalty/sessionm/)는 고객 참여 및 로열티 플랫폼으로, 캠페인 관리 기능과 로열티 관리 솔루션을 제공하여 마케터가 참여도와 수익성을 높이기 위한 목표 지향적인 아웃리치를 촉진하도록 돕습니다.

### AI 및 ML 자동화

#### 트렌드 아이템 추천

"AI 개인화된" 모델 외에도, [AI 항목 추천]({{site.baseurl}}/user_guide/sage_ai/recommendations/about_item_recommendations/#trending) 기능에는 "트렌딩" 추천 모델도 포함되어 있습니다. 이 모델은 최근 사용자 상호작용에서 가장 긍정적인 모멘텀을 보인 항목들을 특징으로 합니다.

### 설정

#### 역할

{% multi_lang_include release_type.md release="일반 사용 가능" %}

[역할]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#creating-a-role)은 개별 커스텀 권한을 작업 공간 접근 제어와 함께 묶어 더 많은 구조를 허용합니다. 이는 하나의 대시보드에 여러 브랜드나 로컬 워크스페이스가 있는 경우 특히 유용합니다. 역할을 사용하면 대시보드 사용자를 올바른 워크스페이스에 추가하고 관련 권한을 직접 부여할 수 있습니다. 

#### 보안 사건 보고서

다운로드한 보안 보고서 이벤트에 나타날 수 있는 [보안 이벤트]({{site.baseurl}}/user_guide/administrative/app_settings/company_settings/security_settings/#downloading-a-security-event-report)의 전체 목록을 추가했습니다.

#### 메시지 사용 보고서

{% multi_lang_include release_type.md release="조기 액세스" %}

[메시지 사용 대시보드]({{site.baseurl}}/message_usage/)는 SMS 및 WhatsApp 크레딧 사용에 대한 셀프 서비스 통찰력을 제공하여 계약 할당량에 대한 과거 및 현재 사용을 종합적으로 볼 수 있습니다. 이러한 통찰력은 혼란을 줄이고 초과 위험을 방지하기 위한 조정을 하는 데 도움을 줄 수 있습니다.

### SDK

#### 지연 초기화 for the Braze Swift 소프트웨어 개발 키트

[지연 초기화]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/advanced_use_cases/delayed_initialization/)을 설정하여 Braze Swift SDK를 비동기적으로 초기화하면서 푸시 알림 처리가 유지되도록 합니다. 이것은 SDK를 초기화하기 전에 서버에서 구성 데이터를 가져오거나 사용자 동의를 기다리는 것과 같은 다른 서비스를 설정해야 할 때 유용할 수 있습니다.

### SDK 업데이트

다음 SDK 업데이트가 릴리스되었습니다. 주요 업데이트는 아래에 나열되어 있으며, 그 외의 모든 업데이트는 해당 SDK 체인지로그를 확인하면 확인할 수 있습니다.

- [안드로이드 소프트웨어 개발 키트 32.1.0](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#3210)
- [세그먼트 Kotlin 소프트웨어 개발 키트 2.0.0](https://github.com/braze-inc/braze-segment-kotlin/blob/main/CHANGELOG.md#200)
- [스위프트 소프트웨어 개발 키트 10.1.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#1010)
- [React Native 소프트웨어 개발 키트 12.1.0](https://github.com/braze-inc/braze-react-native-sdk/blob/master/CHANGELOG.md#1210)
- [Cordova 소프트웨어 개발 키트 10.0.0](https://github.com/braze-inc/braze-cordova-sdk/blob/master/CHANGELOG.md#1000)
    - 이 버전은 이제 Cordova Android 13.0.0을 요구합니다.
    - [코르도바 릴리스 발표](https://cordova.apache.org/announcements/2024/05/23/cordova-android-13.0.0.html)를 참조하여 프로젝트 의존성 요구 사항의 전체 목록을 확인하십시오.- 네이티브 안드로이드 브리지를 [브레이즈 안드로이드 SDK 30.3.0에서 32.1.0으로](https://github.com/braze-inc/braze-android-sdk/compare/v30.3.0...v32.1.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed) 업데이트했습니다.
    - 네이티브 iOS 브리지를 [Braze Swift SDK 9.2.0에서 10.1.0](https://github.com/braze-inc/braze-swift-sdk/compare/9.2.0...10.1.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed)으로 업데이트했습니다.
- [스위프트 소프트웨어 개발 키트 10.2.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#1020)
- [Unity 7.0.0](https://github.com/braze-inc/braze-unity-sdk/blob/master/CHANGELOG.md#700)
    - 네이티브 Android 브리지를 [Braze Android SDK 30.3.0에서 32.1.0](https://github.com/braze-inc/braze-android-sdk/compare/v30.3.0...v32.1.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed)으로 업데이트했습니다.
    - 네이티브 iOS 브리지를 [Braze Swift SDK 9.0.0에서 10.1.0](https://github.com/braze-inc/braze-swift-sdk/compare/9.0.0...10.1.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed)으로 업데이트했습니다.
- [Braze 세그먼트 Swift Plugin 4.0.0](https://github.com/braze-inc/braze-segment-swift/blob/main/CHANGELOG.md#400)
    - 업데이트는 Braze Swift SDK 바인딩을 `10.2.0+` SemVer 명칭의 릴리스를 요구하도록 변경합니다.
        - 이것은 `10.2.0`부터 `11.0.0`까지의 모든 버전의 Braze SDK와의 호환성을 허용합니다.
        - [`10.0.0`](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#1000)에 대한 잠재적인 중단 변경 사항에 대한 자세한 내용은 체인지로그 항목을 참조하십시오.
- [Flutter 소프트웨어 개발 키트 11.0.0](https://pub.dev/packages/braze_plugin/changelog#1100)
    - 네이티브 Android 브리지를 [Braze Android SDK 30.4.0에서 32.1.0으로](https://github.com/braze-inc/braze-android-sdk/compare/v30.4.0...v32.1.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed) 업데이트합니다.
        - Android에서 `wipeData()`의 동작을 변경하여 호출된 후 외부 구독(예: `subscribeToContentCards()`)을 유지하도록 합니다.
    - 네이티브 iOS 브리지를 [Braze Swift SDK 9.0.0에서 10.2.0](https://github.com/braze-inc/braze-swift-sdk/compare/9.0.0...10.2.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed)으로 업데이트합니다.
- [스위프트 소프트웨어 개발 키트 10.3.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#1030)
- [Unity 7.1.0](https://github.com/braze-inc/braze-unity-sdk/blob/master/CHANGELOG.md#710)
- [React Native 소프트웨어 개발 키트 12.2.0](https://github.com/braze-inc/braze-react-native-sdk/blob/master/CHANGELOG.md#1220)

## 2024년 8월 20일 출시

### 새로운 사용 사례

#### 카탈로그

모든 유형의 데이터를 카탈로그로 가져올 수 있습니다. 일반적으로 데이터는 제품, 할인, 프로모션, 이벤트 등과 같은 오퍼링에 대한 메타데이터입니다. 우리의 [사용 사례]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs)를 읽고 이 데이터를 사용하여 사용자에게 매우 관련성 높은 메시징을 타겟팅하는 방법을 알아보세요.

#### Intelligence Suite

Intelligence Suite는 사용자 기록과 캠페인 및 캔버스 성과를 분석하는 강력한 기능을 제공하며, 참여, 시청률 및 전환을 증가시키기 위해 자동으로 조정합니다. 이러한 기능이 다양한 산업에 어떻게 도움이 되는지에 대한 몇 가지 예를 보려면 [사용 사례]({{site.baseurl}}/user_guide/brazeai/intelligence)를 확인하세요.

### 홈 대시보드 업데이트

당신은 [중단한 곳에서 계속할 수 있습니다]({{site.baseurl}}/user_guide/data_and_analytics/analytics/home_dashboard/#pick-up-where-you-left-off) Braze 대시보드에서 최근에 편집하거나 생성한 파일에 쉽게 접근할 수 있습니다. 이 섹션은 Braze 대시보드의 **홈** 페이지 상단에 나타납니다.

### 데이터 유연성

#### 데이터 변환 템플릿 및 새로운 대상

{% multi_lang_include release_type.md release="일반 사용 가능" %}

구축 당신의 데이터 변환을 사용하여 우리의 전용 [템플릿 라이브러리]({{site.baseurl}}/user_guide/data_and_analytics/data_transformation/creating_a_transformation#step-2-create-a-transformation) 특정 외부 플랫폼을 시작하는 데 도움을 주기 위해, 기본값 코드 대신. 이제 **POST를 선택할 수 있습니다: 즉시 메시지를 API Only**를 통해 대상에 전송하여 소스 플랫폼에서 웹후크를 변환하여 사용자에게 즉시 메시지를 전송합니다.

#### 대량으로 사용자 병합

{% multi_lang_include release_type.md release="일반 사용 가능" %}

사용자 프로필이 중복되는 경우, 이러한 사용자를 [대량 병합]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/duplicate_users#bulk-merging)하여 데이터를 간소화할 수 있습니다.

#### 사용자 지정 속성 내보내기

{% multi_lang_include release_type.md release="일반 사용 가능" %}

당신은 [커스텀 속성 목록을 내보낼 수 있습니다]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#exporting-data) CSV 파일로 **모두 내보내기**를 선택하여 **커스텀 속성** 페이지에서. CSV 파일이 생성되고 다운로드 링크가 이메일로 전송됩니다.

#### 커런츠 IP 허용 목록

브레이징은 나열된 IP에서 커런츠 데이터를 전송하며, 이는 [허용 목록 추가]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/setting_up_currents)에 선택된 모든 API 키에 자동으로 동적으로 추가됩니다.

### 강력한 채널

#### 새 세그먼트 빌더 경험

{% multi_lang_include release_type.md release="일반 사용 가능" %}

구축 a 세그먼트 using our [updated experience]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment). 세그먼트는 데이터가 변경됨에 따라 실시간으로 업데이트되며, 타겟팅 및 메시징 목적에 맞게 필요한 만큼의 세그먼트를 생성할 수 있습니다.

#### 세그먼트별 측정기준

캠페인, 캔버스, 변형 및 단계를 세그먼트별로 성능 측정기준을 분류하기 위해 [쿼리 빌더]({{site.baseurl}}/user_guide/data_and_analytics/query_builder/) 보고서 템플릿을 사용하십시오.

#### 전화번호 획득

WhatsApp 메시징 채널을 사용하려면 [Cloud API](https://developers.facebook.com/docs/whatsapp/cloud-api/phone-numbers) 또는 [On-Premises API](https://developers.facebook.com/docs/whatsapp/on-premises/phone-numbers)에 대한 WhatsApp의 요구 사항을 충족하는 전화번호가 필요합니다. 

전화번호는 직접 획득해야 하며, Braze는 번호를 제공하지 않습니다. 귀하의 비즈니스 전화 제공업체를 통해 SIM 카드가 있는 물리적 전화를 구입하거나 당사의 파트너 중 한 명을 사용할 수 있습니다: Twilio 또는 Infoblip. **Twilio 또는 Infobip 계정이 있어야 합니다. 이 작업은 Braze를 통해 수행할 수 없습니다.**

### 새로운 Braze 파트너십

#### Zendesk Chat - 인스턴트 채팅

Braze와 [Zendesk Chat]({{site.baseurl}}/partners/zendesk_chat/) 통합은 각 플랫폼의 웹후크를 사용하여 양방향 SMS 대화를 설정합니다. 사용자가 지원을 요청하면 Zendesk에 티켓이 생성됩니다. 에이전트 응답은 API 트리거 SMS 캠페인을 통해 Braze로 전달되며, 사용자 회신은 Zendesk로 다시 전송됩니다.

### SDK 업데이트

다음 SDK 업데이트가 릴리스되었습니다. 주요 업데이트는 아래에 나열되어 있으며, 그 외의 모든 업데이트는 해당 SDK 체인지로그를 확인하면 확인할 수 있습니다.

- [안드로이드 소프트웨어 개발 키트 32.0.0](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md)
- [스위프트 소프트웨어 개발 키트 10.0.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md)
    - 푸시 이벤트에 [`Braze.Notifications.subscribeToUpdates(payloadTypes:_:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/notifications-swift.class/subscribetoupdates(payloadtypes:_:)) 구독할 때 다음과 같은 변경 사항이 적용되었습니다.
        - 이 `update` 클로저는 이제 기본적으로 "푸시 열림" 및 "푸시 수신" 이벤트에 의해 트리거됩니다. 이전에는 "푸시 열림" 이벤트에 의해서만 트리거되었습니다.
            - "푸시 열림" 이벤트에만 계속 구독하려면 매개변수 `payloadTypes`에 `[.opened]`을 전달하세요. 대안으로, `update` 클로저를 구현하여 `Braze.Notifications.Payload`에서 `type`가 `.opened`인지 확인하십시오.
        - 푸시 알림을 수신할 때 `content-available: true`와 함께, [`Braze.Notifications.Payload.type`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/notifications-swift.class/payload/type)는 이제 `.received` 대신 `.opened`가 됩니다.
    - 다음의 더 이상 사용되지 않는 API를 사용 불가능으로 표시합니다:
        - `Braze.Configuration.Api.Flavor`
        - `Braze.Configuration.Api.flavor`
        - `Braze.Configuration.Api.SdkMetadata`
        - `Braze.Configuration.Api.addSdkMetadata(_:)`
        - `Braze.ContentCard.ClickAction.uri(_:useWebview:)`
        - `Braze.ContentCard.ClickAction.uri`
        - `Braze.InAppMessage.ClickAction.uri(_:useWebview:)`
        - `Braze.InAppMessage.ClickAction.uri`
        - `Braze.InAppMessage.ModalImage.imageUri`
        - `Braze.InAppMessage.Full.imageUri`
        - `Braze.InAppMessage.FullImage.imageUri`
        - `Braze.InAppMessage.Themes.default`
        - `Braze.deviceId(queue:completion:)`
        - `Braze._objc_deviceId(completion:)`
        - `Braze.deviceId()`
        - `Braze.User.setCustomAttributeArray(key:array:fileID:line:)`
        - `Braze.User.addToCustomAttributeArray(key:value:fileID:line:)`
        - `Braze.User.removeFromCustomAttributeArray(key:value:fileID:line:)`
        - `Braze.User._objc_addToCustomAttributeArray(key:value:)`
        - `Braze.User._objc_removeFromCustomAttributeArray(key:value:)`
        - `gifViewProvider`
        - `GifViewProvider.default`
    - 더 이상 사용되지 않는 API를 제거합니다.
        - `Braze.Configuration.DeviceProperty.pushDisplayOptions`
        - `Braze.InAppMessageRaw.Context.Error.extraProcessClickAction`
    - 구식 `BrazeLocation` 클래스를 `BrazeLocationProvider`로 대체합니다.
- [Xamarin 소프트웨어 개발 키트 Version 6.0.0](https://github.com/braze-inc/braze-xamarin-sdk/blob/master/CHANGELOG.md)
    - iOS 및 Android 바인딩에 대한 .NET 8.0 지원이 추가되었습니다. .NET 7.0은 지원 종료에 도달했습니다.
        - 이것은 .NET 7.0에 대한 지원을 제거합니다.
    - [Braze Android 30.4.0 to 32.0.0](https://github.com/braze-inc/braze-android-sdk/compare/v30.4.0...v32.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed) 안드로이드 바인딩을 업데이트했습니다.
    - [브레이즈 스위프트 소프트웨어 개발 키트 9.0.0 to 10.0.0](https://github.com/braze-inc/braze-swift-sdk/compare/9.0.0...10.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed)
        - 푸시 알림 이벤트에 가입할 때, 구독은 iOS에서 "푸시 수신"과 "푸시 열기" 모두에 대해 트리거되며, "푸시 열기" 이벤트에 대해서만 트리거되지 않습니다.
- [React Native 소프트웨어 개발 키트 12.0.0](https://github.com/braze-inc/braze-react-native-sdk/blob/12.0.0/CHANGELOG.md)
    - 네이티브 iOS 버전 바인딩을 [Braze Swift SDK 9.0.0 to 10.0.0](https://github.com/braze-inc/braze-swift-sdk/compare/9.0.0...10.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed) 업데이트합니다.
        - 푸시 알림 이벤트에 가입할 때, 구독은 `push_received` 및 `push_opened`에 대해 iOS에서 트리거되며, `push_opened` 이벤트에 대해서만 트리거되지 않습니다.

## 2024년 7월 23일 출시

### Braze 문서 업데이트

#### Diátaxis 및 Braze 문서

현재 [Diátaxis](https://diataxis.fr/)라는 프레임워크를 사용하여 설명서 표준화하는 작업을 진행 중입니다. 작가와 기여자들이 이 새로운 프레임워크에 맞는 콘텐츠를 만들 수 있도록, 우리는 [각 콘텐츠 유형에 대한 템플릿]({{site.baseurl}}/contributing/content_types)을 만들었습니다.

#### Braze 문서를 위한 새로운 풀-리퀘스트 템플릿

시간을 들여 풀 리퀘스트(PR) 템플릿을 개선하여 더 쉽고 혼란스럽지 않게 [Braze 설명서에 기여하실]({{site.baseurl}}/contributing/home/) 수 있도록 했습니다. 그래도 개선의 여지가 있다고 생각되면 PR을 개설하거나 [이슈를 제출하세요](https://github.com/braze-inc/braze-docs/issues/new?assignees=&labels=enhancement&projects=&template=request_a_feature.md&title=). 모든 게 더 쉬워졌습니다!
 
### 데이터 유연성

#### 사용자 지정 이벤트 및 속성 내보내기

{% multi_lang_include release_type.md release="일반 사용 가능" %}

이제 [`/custom_attributes`]({{site.baseurl}}/api/endpoints/export/custom_attributes/get_custom_attributes) 및 [`/events`]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events_data) 엔드포인트를 사용하여 커스텀 이벤트 및 커스텀 속성을 내보낼 수 있습니다.

#### 사용자를 위한 새로운 커런츠 권한

사용자를 위한 두 가지 새로운 권한 설정이 있습니다: **전류 통합 보기** 및 **전류 통합 편집하기**. 사용자 권한 [user permissions]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions)에 대해 자세히 알아보세요. 

#### Snowflake 데이터 유지 정책 업데이트
 
2024년 8월 27일부터 개인 식별 정보(PII)는 2년 이상 된 모든 Snowflake Secure Data Sharing 이벤트 데이터에서 제거됩니다. Snowflake를 사용하는 경우 유지 정책이 적용되기 전에 Snowflake 계정에 사본을 저장하여 환경의 전체 이벤트 데이터를 유지하도록 선택할 수 있습니다. [스노우플레이크 데이터 보존]({{site.baseurl}}/partners/data_and_infrastructure_agility/data_warehouses/snowflake/data_retention/)
 
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

AI Liquid Assistant는 BrazeAI<sup>TM</sup>로 구동되는 채팅 어시스턴트로, 메시지 콘텐츠를 개인화하는 데 필요한 Liquid를 생성하는 데 도움을 줍니다. 템플릿에서 Liquid를 생성하고, 개인화된 Liquid 제안을 받으며, BrazeAI<sup>TM</sup>의 지원으로 기존 Liquid를 최적화할 수 있습니다. AI Liquid 도우미는 사용된 Liquid를 설명하는 주석도 제공하므로 Liquid에 대한 이해를 높이고 직접 작성하는 방법을 배울 수 있습니다.

시작하려면 [AI Liquid 어시스턴트]({{site.baseurl}}/user_guide/brazeai/generative_ai/ai_liquid)를 참조하세요.
 
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

이제 [브랜드 가이드라인]({{site.baseurl}}/user_guide/brazeai/generative_ai/ai_copywriting/brand_guidelines/)을 생성하고 적용하여 AI 카피라이팅 어시스턴트가 생성한 카피 스타일을 브랜드에 맞게 맞춤 설정할 수 있습니다. 다양한 시나리오에 대해 여러 가지 가이드라인을 설정하여 항상 상황에 맞는 어조를 유지할 수 있습니다.
 
### 새로운 Braze 파트너십

#### Adikteev - 애널리틱스

Braze와 [Adikteev의]({{site.baseurl}}/partners/data_and_infrastructure_agility/analytics/adikteev/) 통합을 통해 Braze CRM 캠페인 내에서 Adikteev의 이탈 예측 기술을 활용하여 고위험 사용자 세그먼트를 우선적으로 타겟팅함으로써 사용자 유지율을 높일 수 있습니다.
 
#### Celebrus - 애널리틱스
 
Braze와 [Celebrus]({{site.baseurl}}/partners/data_and_infrastructure_agility/analytics/celebrus) 통합은 웹 및 모바일 앱 채널 전반에서 Braze SDK와 원활하게 통합되어 채널 활동 데이터로 Braze의 인구를 늘리는 데 도움이 됩니다. 여기에는 지정된 기간 동안 디지털 자산 전반의 방문자 트래픽에 대한 포괄적인 인사이트가 포함됩니다.
 
#### IAM Studio - 메시지 템플릿
 
Braze와 [IAM Studio]({{site.baseurl}}/partners/message_orchestration/channel_extensions/email_templates/iam_studio/) 통합을 통해 Braze 인앱 메시지에 맞춤형 인앱 메시지 템플릿을 쉽게 삽입할 수 있으며, 이미지 교체, 텍스트 수정, 딥링크 설정, 커스텀 속성 및 이벤트 설정을 제공합니다. IAM Studio를 사용하면 메시지 제작 시간을 줄이고 콘텐츠 계획에 더 많은 시간을 할애할 수 있습니다.
 
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

[적시 프로비저닝]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/saml_jit)은 SAML SSO와 함께 작동하여 새로운 대시보드 사용자가 처음 로그인할 때 Braze 계정을 만들 수 있도록 합니다. 따라서 관리자가 새 대시보드 사용자의 계정을 수동으로 만들고, 권한을 선택하고, 워크스페이스에 할당하고, 사용자가 계정을 활성화할 때까지 기다릴 필요가 없습니다.

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

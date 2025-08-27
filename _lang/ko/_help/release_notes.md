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

> Braze는 주요 제품 출시에 맞춰 한 달 주기로 제품 업데이트에 대한 정보를 공개하지만 매주 기타 개선 사항이 업데이트됩니다.<br><br>이 섹션에 나열된 업데이트에 대한 자세한 내용은 계정 관리자에게 문의하거나 [지원 티켓을 개설하세요]({{site.baseurl}}/user_guide/administrative/access_braze/support/). 또한 [SDK 체인지로그에서]({{site.baseurl}}/developer_guide/changelogs) 월별 SDK 릴리스, 업데이트 및 개선 사항에 대한 자세한 정보를 확인할 수 있습니다.

## 2025년 6월 24일 출시

### Braze의 OfferFit

[OfferFit](https://www.offerfit.ai/)은 A/B 테스트를 AI 의사결정으로 대체하여 모든 것을 개인화하고, 모든 지표를 극대화합니다: 클릭이 아닌 수익을 유도합니다. OfferFit을 사용하면 모든 비즈니스 KPI를 최적화할 수 있습니다. 샘플 사용 사례 및 주요 기능에 대한 전용 섹션 [Braze의 OfferFit]({{site.baseurl}}/user_guide/offerfit)을 참조하십시오.

### 새로운 SDK 튜토리얼

각 Braze SDK 튜토리얼은 전체 샘플 코드와 함께 단계별 지침을 제공합니다. 시작하려면 아래에서 튜토리얼을 선택하십시오:

- [배너 표시하기]({{site.baseurl}}/developer_guide/banners/tutorial_displaying_banners)
- [인앱 메시지 스타일 사용자 정의하기]({{site.baseurl}}/developer_guide/in_app_messages/tutorials/customizing_message_styling)
- [인앱 메시지 조건부 표시하기]({{site.baseurl}}/developer_guide/in_app_messages/tutorials/conditionally_displaying_messages)
- [트리거된 인앱 메시지 연기하기]({{site.baseurl}}/developer_guide/in_app_messages/tutorials/deferring_triggered_messages)

### 데이터 유연성

#### SAML 즉시 프로비저닝

{% multi_lang_include release_type.md release="일반 사용 가능" %}

새 대시보드 사용자가 첫 로그인 시 Braze 계정을 생성할 수 있도록 [SAML 즉시 프로비저닝]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/saml_jit)을 사용하십시오. 따라서 관리자가 새 대시보드 사용자의 계정을 수동으로 만들고, 권한을 선택하고, 워크스페이스에 할당하고, 사용자가 계정을 활성화할 때까지 기다릴 필요가 없습니다.

#### 선택당 필터

이제 [선택]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/selections)당 최대 10개의 필터를 추가할 수 있습니다.

#### 카탈로그 저장

무료 버전의 [카탈로그]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/catalog/#catalog-storage) 저장 용량은 최대 100MB입니다. 100MB 이하인 한 무제한 항목을 가질 수 있습니다.

#### 클라우드 데이터 수집과 동기화된 행 수

기본적으로 클라우드 데이터 수집의 경우 각 실행은 최대 5억 개의 행을 동기화할 수 있습니다. 5억 개 이상의 새로운 행이 있는 동기화는 중단됩니다.

자세한 내용은 [클라우드 데이터 수집 제품 제한 사항]({{site.baseurl}}/user_guide/data/cloud_ingestion/overview/#product-limitations)을 참조하십시오.

### 강력한 채널

#### 받은편지함 비전에서 접근성 테스트

{% multi_lang_include release_type.md release="일반 사용 가능" %}

받은편지함 비전에서 [접근성 테스트]({{site.baseurl}}/user_guide/message_building_by_channel/email/inbox_vision/#accessibility-testing)를 사용하여 이메일에 존재할 수 있는 접근성 문제를 강조 표시합니다. 

접근성 테스트는 이메일 콘텐츠를 [웹 콘텐츠 접근성 지침](https://www.w3.org/WAI/standards-guidelines/wcag/) (WCAG) 2.2 AA 요구 사항에 대해 분석합니다. 이것은 어떤 요소가 접근성 기준을 충족하지 못하는지에 대한 통찰력을 제공할 수 있습니다.

#### WhatsApp 클릭 추적

{% multi_lang_include release_type.md release="일반 사용 가능" %}

응답 및 템플릿 메시지 모두에서 [클릭 추적]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/click_tracking)을 활성화하여 WhatsApp 성과 보고서에서 클릭 데이터를 확인하고 클릭한 사용자에 따라 세그먼트할 수 있습니다.

#### WhatsApp용 비디오

{% multi_lang_include release_type.md release="일반 사용 가능" %}

아웃바운드 WhatsApp 메시지의 본문 텍스트 내에 [비디오를 삽입할 수 있습니다.]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/create/#supported-whatsapp-features) 이 파일은 URL을 통해 호스팅되거나 [Braze 미디어 라이브러리]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/media_library)에 있어야 합니다.

### 새로운 Braze 파트너십

#### Stripe - 전자상거래

Braze와 [Stripe]({{site.baseurl}}/partners/stripe) 통합을 통해 Stripe 이벤트(예: 체험 시작, 구독 활성화, 구독 취소 등)에 따라 Braze에서 메시징을 트리거할 수 있습니다.

### SDK 업데이트

다음 SDK 업데이트가 릴리스되었습니다. 주요 업데이트는 아래에 나열되어 있으며, 그 외의 모든 업데이트는 해당 SDK 체인지로그를 확인하면 확인할 수 있습니다.

- [React Native SDK 15.0.1](https://github.com/braze-inc/braze-react-native-sdk/blob/master/CHANGELOG.md)
- [Flutter SDK 14.0.1-14.0.2](https://pub.dev/packages/braze_plugin/changelog)
- [Cordova SDK 12.0.0](https://github.com/braze-inc/braze-cordova-sdk/blob/master/CHANGELOG.md#1200)
    - 네이티브 Android 브리지를 [Braze Android SDK 35.0.0에서 36.0.0으로 업데이트했습니다.](https://github.com/braze-inc/braze-android-sdk/compare/v35.0.0...v36.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed)
    - 네이티브 iOS 브리지를 [Braze Swift SDK 11.6.1에서 12.0.0으로 업데이트했습니다.](https://github.com/braze-inc/braze-swift-sdk/compare/11.6.1...12.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed)
- [세그먼트 Kotlin 4.0.0-4.0.1](https://github.com/braze-inc/braze-segment-kotlin/blob/4.0.0/CHANGELOG.md#400)
    - Braze Android SDK를 [35.0.0에서 36.0.0으로 업데이트했습니다.](https://github.com/braze-inc/braze-android-sdk/compare/v35.0.0...v36.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed)

## 2025년 5월 27일 출시

### 데이터 유연성

#### 작업 공간 간 캔버스 복사

{% multi_lang_include release_type.md release="일반 사용 가능" %}

이제 작업 공간 간에 캔버스를 복사할 수 있습니다. 이렇게 하면 다른 작업 공간의 캔버스를 복사하여 메시지 작성을 시작할 수 있습니다. 복사되는 내용에 대한 자세한 정보는 [작업 공간 간 캠페인 및 캔버스 복사]({{site.baseurl}}/copying_to_workspaces/)를 참조하십시오.

#### 승인 워크플로우를 위한 메시징 규칙 

{% multi_lang_include release_type.md release="일반 사용 가능" %}

승인 워크플로우에서 [메시징 규칙]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/approvals/messaging_rules)을 사용하여 추가 승인이 필요하기 전에 도달 가능한 사용자 수를 제한할 수 있습니다. 이렇게 하면 더 큰 오디언스를 타겟팅하기 전에 캠페인과 캔버스를 검토할 수 있습니다.

#### Snowflake 및 Braze에 대한 엔터티 관계 다이어그램

올해 초, 우리는 Snowflake와 Braze 간에 공유되는 데이터에 대한 엔터티 관계 테이블을 만들었습니다. 이번 달에는 각 테이블의 세부 정보를 팬, 잡고, 확대할 수 있는 [새로운 인터랙티브 다이어그램]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/entity_relationships/)을 추가하여 데이터가 Braze와 어떻게 상호작용하는지 더 잘 이해할 수 있습니다.

### 창의력 발휘

#### 추천 이벤트

{% multi_lang_include release_type.md release="조기 액세스" %}

[추천 이벤트]({{site.baseurl}}/user_guide/data/custom_data/recommended_events)는 가장 일반적인 전자상거래 사용 사례에 매핑됩니다. 추천 이벤트를 사용하면 고객 생애주기에 매핑된 미리 만들어진 캔버스 템플릿, 보고 대시보드 등을 잠금 해제할 수 있습니다.

### 강력한 채널

#### 배너 채널

{% multi_lang_include release_type.md release="일반 사용 가능" %}

[배너]({{site.baseurl}}/user_guide/message_building_by_channel/banners)를 사용하면 사용자에게 개인화된 메시지를 생성할 수 있으며, 이메일이나 푸시 알림과 같은 다른 채널의 도달 범위를 확장할 수 있습니다. 배너를 앱이나 웹사이트에 직접 삽입할 수 있어 사용자가 자연스럽게 느끼는 경험을 통해 참여할 수 있습니다.

#### 풍부한 커뮤니케이션 서비스(RCS) 채널

{% multi_lang_include release_type.md release="일반 사용 가능" %}

[풍부한 커뮤니케이션 서비스(RCS)]({{site.baseurl}}/about_rcs/)는 브랜드가 정보 제공뿐만 아니라 훨씬 더 매력적인 메시지를 전달할 수 있도록 전통적인 SMS를 향상시킵니다. 이제 Android와 iOS 모두에서 지원되는 RCS는 고품질 미디어, 인터랙티브 버튼 및 브랜드 발신자 프로필과 같은 기능을 사용자의 사전 설치된 메시징 앱에 직접 제공합니다. 별도의 앱을 다운로드할 필요가 없습니다.

#### 푸시 설정 페이지

{% multi_lang_include release_type.md release="일반 사용 가능" %}

푸시 알림의 주요 설정을 구성하려면 [**푸시 설정** 페이지]({{site.baseurl}}/user_guide/administrative/app_settings/push_settings)를 사용하십시오. 여기에는 푸시 유지 시간(TTL) 및 Android 캠페인에 대한 기본 FCM 우선 순위가 포함됩니다. 이 설정은 푸시 알림의 전달 및 효과를 최적화하여 사용자에게 더 나은 경험을 보장합니다.

#### 인앱 메시지 캠페인을 위한 프로모션 코드

{% multi_lang_include release_type.md release="조기 액세스" %}

인앱 메시지 캠페인에 [프로모션 코드]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/promotion_codes)를 사용하려면 메시지 본문에 [프로모션 코드 목록 스니펫]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/promotion_codes#creating-a-promotion-code-list)을 삽입하면 됩니다.

#### 웹훅 오류 처리 및 속도 제한

[웹훅에 대한 정보]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/understanding_webhooks/#webhook-error-handling-and-rate-limiting)에는 Braze가 웹훅 오류 및 속도 제한을 처리하는 방법을 설명하는 새로운 섹션이 있습니다.

#### 인앱 메시지 로케일

[로케일 추가]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/using_locales) 후, 단일 인앱 메시지 내에서 다양한 언어로 사용자에게 타겟팅할 수 있습니다.

#### Amazon SES를 이메일 발송 제공업체(ESP)로 사용하기

이제 Amazon SES를 ESP로 사용할 수 있으며, SendGrid 및 SparkPost를 사용하는 것과 유사합니다. 링크 간 SSL 설정 및 클릭 추적의 미세한 차이에 대해서는 [Braze의 SSL]({{site.baseurl}}/user_guide/message_building_by_channel/email/email_setup/ssl#what-is-a-cdn-and-why-do-i-need-it) 및 [유니버설 링크 및 앱 링크]({{site.baseurl}}/user_guide/message_building_by_channel/email/universal_links#turning-off-click-tracking-on-a-link-to-link-basis)를 참조하십시오.

### 새로운 Braze 파트너십

#### Eagle Eye - 로열티

Braze와 [Eagle Eye]({{site.baseurl}}/partners/eagle_eye/)의 양방향 통합을 통해 로열티 및 프로모션 데이터를 Braze에서 직접 활성화할 수 있으며, 마케터는 포인트 잔액, 프로모션 및 보상 활동과 같은 실시간 데이터를 사용하여 고객 참여를 개인화할 수 있습니다.

#### Eppo - A/B 테스트

Braze와 [Eppo]({{site.baseurl}}/partners/eppo/)의 통합을 통해 Braze에서 A/B 테스트를 설정하고 Eppo에서 결과를 분석하여 통찰력을 발견하고 메시지 성과를 매출 또는 유지와 같은 장기 비즈니스 지표에 연결할 수 있습니다.

#### Mention Me - 추천

함께, [Mention Me](https://www.mention-me.com/)와 Braze는 프리미엄 고객을 유치하고 변함없는 브랜드 로열티를 조성하는 관문이 될 수 있습니다. 1자체 추천 데이터를 Braze에 원활하게 통합함으로써 브랜드 팬을 겨냥한 매우 개인화된 옴니채널 경험을 제공할 수 있습니다. 시작하려면 [기술 파트너를 참조하십시오: Mention Me]({{site.baseurl}}/partners/mention_me).

#### Shopify - 전자상거래

여러 Shopify 스토어 도메인을 [단일 작업 공간에 연결]({{site.baseurl}}/shopify_connecting_multiple_stores/)하여 모든 시장에서 고객을 포괄적으로 볼 수 있습니다. 하나의 작업 공간에서 지역 매장 간의 노력을 중복하지 않고 자동화 프로그램과 여정을 구축하고 시작합니다.

### 기타

#### Braze에서 접근 가능한 메시지 구축으로 업데이트되었습니다.

우리는 [Braze에서 접근 가능한 메시지 구축]({{site.baseurl}}/help/accessibility/) 기사를 더 명확하고 구체적인 접근 가능한 메시지 생성에 대한 지침으로 업데이트했습니다. 이 기사는 이제 콘텐츠 구조, 대체 텍스트, 버튼 및 색상 대비에 대한 확장된 모범 사례와 사용자 정의 HTML 메시지에 대한 ARIA 처리에 대한 새로운 섹션을 포함합니다. 

이 업데이트는 Braze에서 더 접근 가능한 메시징 경험을 지원하기 위한 우리의 광범위한 노력의 일환입니다. 우리는 접근성이 진화하는 분야라는 것을 알고 있으며, 우리가 배우는 내용을 계속 공유할 것입니다.

{% multi_lang_include accessibility/feedback.md %}

### SDK 업데이트

다음 SDK 업데이트가 릴리스되었습니다. 주요 업데이트는 아래에 나열되어 있으며, 그 외의 모든 업데이트는 해당 SDK 체인지로그를 확인하면 확인할 수 있습니다.

- [안드로이드 SDK 36.0.0](https://pub.dev/packages/braze_plugin/changelog)
    - 이 릴리스는 Braze Android SDK의 최소 Android SDK 버전을 API 21에서 API 25로 증가시킨 것을 34.0.0에서 되돌립니다. 이로 인해 SDK는 다시 API 21을 지원하는 앱에 컴파일될 수 있습니다. 우리가 컴파일할 수 있는 기능을 다시 도입하고 있지만, < API 25에 대한 공식 지원을 재도입하지 않으며, 해당 버전에서 실행되는 장치에서 SDK가 의도한 대로 작동할 것이라고 보장할 수 없습니다.
    - 앱이 해당 버전을 지원하는 경우 다음을 수행해야 합니다:
        - 해당 API 버전의 실제 장치(에뮬레이터가 아님)에서 SDK 통합이 의도한 대로 작동하는지 확인하십시오.
        - 예상되는 동작을 검증할 수 없는 경우 [disableSDK](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/disable-sdk.html)를 호출하거나 해당 버전에서 SDK를 초기화하지 않아야 합니다. 그렇지 않으면 최종 사용자의 장치에서 의도하지 않은 부작용이나 성능 저하를 초래할 수 있습니다.
    - 인앱 메시지가 메인 스레드에서 읽기를 유발하는 문제를 수정했습니다.
    `BrazeInAppMessageManager.displayInAppMessage`는 이제 Kotlin 중단 함수입니다.
        - 이 함수를 직접 호출하지 않는 경우 변경할 필요가 없습니다.
    - AndroidX Compose BOM이 Jetpack Compose API의 업데이트를 처리하기 위해 2025.04.01로 업데이트되었습니다.
- [React Native SDK 15.0.0](https://github.com/braze-inc/braze-react-native-sdk/blob/master/CHANGELOG.md)
    - Braze Android SDK 35.0.0에서 36.0.0으로 네이티브 Android 브리지를 업데이트합니다.
    - Braze Swift SDK 11.9.0에서 12.0.0으로 네이티브 iOS 버전 바인딩을 업데이트합니다.
    - iOS에서 PushNotificationEvent.timestamp의 단위 표현을 밀리초로 업데이트합니다.
        - 이전에는 이 값이 iOS에서 초로 표현되었습니다. 이제 기존 Android 구현과 일치합니다.
- [Web SDK 5.9.0](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md)
- [Flutter SDK 14.0.0 5.9.0](https://pub.dev/packages/braze_plugin/changelog)
    - 이 릴리스는 Braze Android SDK의 최소 Android SDK 버전을 API 21에서 API 25로 증가시킨 것을 34.0.0에서 되돌립니다. 이로 인해 SDK는 다시 API 21을 지원하는 앱에 컴파일될 수 있습니다. 그러나 < API 25에 대한 공식 지원을 재도입하지 않습니다. 자세한 내용은 [여기](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#3600)를 참조하세요.
    - Braze Android SDK 35.0.0에서 36.0.0으로 네이티브 Android 브리지를 업데이트합니다.
    - Braze Swift SDK 11.9.0에서 12.0.0으로 네이티브 iOS 브리지를 업데이트합니다.

## 2025년 4월 29일 출시

### Braze 접근 문제 해결

[Troubleshooting Braze Access]({{site.baseurl}}/user_guide/administrative/access_braze/troubleshooting/)는 계정 잠금이나 예상대로 작동하지 않는 Braze 대시보드와 같은 Braze에 접근할 때 발생할 수 있는 문제를 탐색하는 데 도움을 줍니다.

### 데이터 유연성

#### 커런츠 자주 묻는 질문

새로운 [자주 묻는 질문]({{site.baseurl}}/user_guide/data/braze_currents/faq/) 페이지에서 커런츠에 대한 자주 묻는 질문에 대한 답변을 찾을 수 있습니다.

#### 익명 사용자

익명 사용자에 대한 새로운 세부정보는 [익명 사용자]({{site.baseurl}}/user_guide/data/user_data_collection/user_profile_lifecycle/anonymous_users/)의 다음 섹션에서 확인하세요.
- [How it works]({{site.baseurl}}/user_guide/data/user_data_collection/user_profile_lifecycle/anonymous_users/#how-it-works) 
- [사용자 별칭 할당]({{site.baseurl}}/user_guide/data/user_data_collection/user_profile_lifecycle/anonymous_users/#assigning-user-aliases)

#### 캠페인 초안

[초안 저장]({{site.baseurl}}/user_guide/engagement_tools/campaigns/managing_campaigns/change_your_campaign_after_launch/#campaign-drafts)은 활성 캠페인에 대한 대규모 변경을 수행하는 데 도움이 될 수 있습니다. 초안을 생성함으로써 다음 출시 전에 계획된 변경 사항을 시험해 볼 수 있습니다.

#### 사용자 식별 및 병합

사용자를 [식별]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/)하거나 [병합]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/)할 때, 이제 `least_recently_updated` 매개변수를 `prioritization` 배열에서 사용하여 가장 최근에 업데이트되지 않은 사용자를 우선시할 수 있습니다.

#### 예약된 사용자 병합

[예약된 병합]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/duplicate_users/#scheduled-merging)을 사용하면 미리 구성된 규칙을 사용하여 사용자 프로필의 병합을 매일 자동화할 수 있습니다. Braze will notify the admins of your workspace 24 hours before the scheduled merge occurs, providing a reminder and time to review the configuration.

#### 수신자 객체

이제 `braze_id`을 [수신자 객체]({{site.baseurl}}/api/objects_filters/recipient_object/)에 포함할 수 있으며, 이를 통해 우리의 엔드포인트에서 정보를 요청하거나 작성할 수 있습니다.

#### 새 데이터 센터

Braze는 두 개의 새로운 [데이터 센터]({{site.baseurl}}/user_guide/data/data_centers/)을 출시했습니다: US-10 및 ID-01. Braze 계정을 설정할 때 지역별 데이터 센터에 가입할 수 있습니다. 

### 창의력 발휘

#### 랜딩 페이지 템플릿

다음 캠페인을 위한 템플릿을 만들기 위해 [랜딩 페이지 템플릿]({{site.baseurl}}/user_guide/engagement_tools/landing_pages/creating_pages/#using-landing-page-templates)을 사용하세요. 이 템플릿은 랜딩 페이지 편집기와 대시보드의 **템플릿** 섹션에서 접근하고 관리할 수 있습니다.

#### 랜딩 페이지 양식 필드

랜딩 페이지를 사용자 정의할 때, 양식 필드가 [필수 또는 선택]({{site.baseurl}}/user_guide/engagement_tools/landing_pages/creating_pages/#step-3-customize-the-page)인지 선택할 수 있습니다. 필수 필드는 양식이 제출되기 전에 작성해야 합니다. 선택 필드는 사용자가 비워두거나 선택하지 않을 수 있습니다.

#### 캔버스 미리 구축된 템플릿

Braze Canvas는 전자상거래 마케터를 위해 특별히 맞춤화된 여러 [미리 구축된 템플릿]({{site.baseurl}}/user_guide/engagement_tools/canvas/ideas_and_strategies/ecommerce_use_cases/)을 제공하여 필수 전략을 구현하기 쉽게 만듭니다. 이 페이지는 고객 여정을 향상시키기 위해 사용할 수 있는 몇 가지 주요 템플릿을 제공합니다.

### 강력한 채널

#### WhatsApp 비디오

{% multi_lang_include release_type.md release="조기 액세스" %}

[WhatsApp 비디오 파일]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/create#outbound-messages)은 이제 URL 또는 Braze 미디어 라이브러리를 통해 호스팅할 수 있습니다.

#### WhatsApp 목록 메시지

[목록 메시지]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/message_processing/user_messages#list-messages/)는 클릭 가능한 옵션 목록과 함께 본문 메시지로 표시됩니다. 각 목록은 여러 섹션을 가질 수 있으며, 각 목록은 최대 10개의 행을 가질 수 있습니다.

#### 미리보기 링크 복사

HTML에서 **미리보기 링크 복사**를 사용하고 [이메일 메시지]({{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/overview/#step-3-add-your-sending-information), [이메일 템플릿]({{site.baseurl}}/user_guide/message_building_by_channel/email/templates/email_template/#step-5-preview-and-test-your-message), 및 [콘텐츠 블록]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/content_blocks/)을 드래그 앤 드롭하여 랜덤 사용자에게 콘텐츠가 어떻게 보일지를 보여주는 공유 가능한 링크를 생성하세요.

#### 푸시 등록 다이어그램

사용자 가이드에서 푸시 알림 문서를 개편하고 [푸시 등록이 대규모에서 어떻게 보이는지]({{site.baseurl}}/user_guide/message_building_by_channel/push/push_registration/#what-does-this-look-like-on-a-broader-scale)를 시각화하는 데 도움이 되는 새로운 다이어그램을 추가했습니다.

### 새로운 Braze 파트너십

#### 업데이트된 파트너 카테고리

내비게이션 경험을 개선하기 위해 [기술 파트너 섹션]({{site.baseurl}}/partners/home/)을 새로운 카테고리와 하위 카테고리로 업데이트했습니다.

#### Shopify (새 버전) - 전자상거래

Shopify 통합의 새 버전은 Shopify 스토어의 유형과 초기 통합 설정에 사용된 외부 ID에 따라 4월부터 단계적으로 출시될 예정입니다.

**통합의 이전 버전은 2025년 8월 28일에 사용 중단됩니다. 2025년 8월 28일 이전에 통합의 최신 버전으로 업데이트해야 합니다.**

새로운 Braze 고객: 2025년 4월부터 Braze는 새로운 온보딩 및 기존 고객 업그레이드를 위해 새로운 Shopify 커넥터를 점진적으로 출시할 예정입니다. 새로운 표준 통합에 대해 더 알아보려면 [Shopify 표준 통합]({{site.baseurl}}/shopify_standard_integration/)을 참조하세요.

#### 단어만 - 동적 콘텐츠

[단어만]({{site.baseurl}}/partners/just_words/)은 라이프사이클 마케팅 채널에서 메시징을 대규모로 하이퍼 개인화하여 수백 가지 변형을 동적으로 테스트하고 성과가 저조한 콘텐츠를 자동으로 새로 고침할 수 있도록 합니다.

#### 탭카트 - 전자상거래

[탭카트]({{site.baseurl}}/partners/ecommerce/tapcart/)는 Shopify 기반 브랜드를 위한 선도적인 모바일 상거래 플랫폼으로, 상인들이 고객이 좋아하는 개인화되고 매력적인 쇼핑 경험을 제공하는 맞춤형 모바일 앱을 만들 수 있도록 합니다.

### SDK

#### Braze SDK 버전 관리

이제 Braze SDK의 [버전 관리]({{site.baseurl}}/developer_guide/sdk_integration/version_management/)에 대해 배울 수 있으므로 앱이 최신 기능 및 품질 개선 사항으로 최신 상태를 유지할 수 있습니다.

#### SDK 문서 감사

현재 모든 [개발자를 위한 SDK 콘텐츠]({{site.baseurl}}/developer_guide/)를 감사하여 모든 코드 샘플이 유용하고 정확한지 확인하고 있습니다. 지금까지 Android 및 Swift 문서에 다양한 업데이트를 했으며, 더 많은 업데이트가 진행 중입니다.

### Braze 설명서에 기여하기

#### Braze 기여자를 위한 오프라인 지원

Braze 문서 기여자라면 이제 로컬 문서 사이트를 완전히 오프라인에서 생성할 수 있습니다. 시작하려면 [Braze 문서 기여하기]({{site.baseurl}}/contributing/home/)를 참조하세요.

#### Braze 문서 포크 문제 해결

포크에서 리포지토리를 타겟팅하는 데 문제가 있는 Braze 문서 기여자를 위해 [문제 해결 단계]({{site.baseurl}}/contributing/troubleshooting/#missing-base-repository)를 만들어 다시 정상 궤도로 돌아갈 수 있도록 도와드립니다.

### SDK 업데이트

다음 SDK 업데이트가 릴리스되었습니다. 주요 업데이트는 아래에 나열되어 있으며, 그 외의 모든 업데이트는 해당 SDK 체인지로그를 확인하면 확인할 수 있습니다.

- [Braze Unity SDK 8.0.0](https://github.com/braze-inc/braze-unity-sdk/blob/master/CHANGELOG.md#710)
    - 네이티브 iOS 브리지를 [Braze Swift SDK 10.3.0에서 11.9.0](https://github.com/braze-inc/braze-swift-sdk/compare/10.3.0...11.9.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed)으로 업데이트했습니다.
    - 네이티브 Android 브리지를 [Braze Android SDK 32.1.0에서 35.0.0](https://github.com/braze-inc/braze-android-sdk/compare/v32.1.0...v35.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed)으로 업데이트했습니다.
        - 필수 Android SDK 버전은 25입니다. 자세한 내용은 [여기](https://github.com/braze-inc/braze-android-sdk?tab=readme-ov-file#version-information)를 참조하세요.
- [Braze Segment Kotlin 3.0.0](https://github.com/braze-inc/braze-segment-kotlin/blob/main/CHANGELOG.md)
    - Braze Android SDK를 [32.1.0에서 35.0.0](https://github.com/braze-inc/braze-android-sdk/compare/v32.1.0...v35.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed)으로 업데이트했습니다.
        - 필수 Android SDK 버전은 25입니다. 자세한 내용은 [여기](https://github.com/braze-inc/braze-android-sdk?tab=readme-ov-file#version-information)를 참조하세요.
- [Braze Swift SDK 12.0.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#1200)
    - 배포된 정적 XCFrameworks는 이제 외부 리소스 번들에 의존하는 대신 리소스를 직접 포함합니다.
        - 정적 XCFrameworks를 수동으로 통합할 때는 대상의 *일반 설정*의 *프레임워크, 라이브러리 및 포함된 콘텐츠* 섹션에서 각 XCFramework에 대해 *포함 및 서명* 옵션을 선택해야 합니다.
        - Swift Package Manager 또는 CocoaPods 통합에 대한 변경 사항은 필요하지 않습니다.
- [Braze 세그먼트 Swift 6.0.0](https://github.com/braze-inc/braze-segment-swift/blob/main/CHANGELOG.md)
    - Braze Swift SDK 바인딩을 업데이트하여 `12.0.0`+ SemVer 명명법의 릴리스를 요구합니다.
        - 이를 통해 `12.0.0` 에서 `13.0.0` 까지의 모든 버전의 Braze SDK와 호환이 가능합니다.
        - 변경 로그 항목을 참조하세요. [`12.0.0`](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#1200) 의 변경 로그 항목을 참조하세요.

## 2025년 4월 1일 릴리스

### Braze 내비게이션 업데이트

Braze의 업데이트된 내비게이션은 여러 장치에서 기능과 콘텐츠에 효율적으로 접근할 수 있도록 설계되었습니다. 내비게이션 버전 간 전환 옵션은 더 이상 제공되지 않습니다. 전용 [Braze 탐색하기]({{site.baseurl}}/user_guide/administrative/access_braze/navigation) 기사에서 자세히 알아보세요.

### 개발자 가이드 정리

이전에는 많은 플랫폼 수준 작업이 여러 페이지에 걸쳐 분할되어 있었으며, Swift SDK 통합은 여섯 페이지에 걸쳐 분할되어 있었습니다. 또한, 공유 기능은 각 플랫폼에 대해 개별적으로 문서화되어 있어, "푸시 알림 설정"과 같은 주제를 검색하면 10개의 다른 페이지가 반환되었습니다.

**이전:**

![플랫폼 통합 가이드 섹션에 위치한 이전 Swift 문서입니다.]({% image_buster /assets/img/before_swift.png %})

이제 플랫폼 수준 작업이 단일 페이지로 통합되었으며, 공유 SDK 기능이 이제 같은 페이지에 존재합니다(새로운 SDK 탭 기능의 도움으로). 예를 들어, 이제 Braze SDK 통합을 위한 단일 페이지가 있으며, 페이지 상단의 탭을 선택하여 플랫폼 간 전환할 수 있습니다. 그럴 경우, 페이지 내 목차도 현재 선택된 탭을 반영하도록 업데이트됩니다.

**후:**

![SDK 통합 기사에서 Swift 탭에 위치한 업데이트된 Swift 문서입니다.]({% image_buster /assets/img/after_swift.png %})

![SDK 통합 기사에서 Android 탭에 위치한 업데이트된 Android 문서입니다.]({% image_buster /assets/img/after_android.png %})

### Braze 설명서에 기여하기

모르셨다면, 우리의 문서는 완전히 오픈 소스입니다! 우리의 [기여 가이드]({{site.baseurl}}/contributing/home)에서 방법을 배울 수 있습니다. 이번 달에는 [섹션을 자동 확장하도록 강제하기]({{site.baseurl}}/contributing/content_management/sections#forcing-auto-expand)와 [API 생성 콘텐츠 렌더링]({{site.baseurl}}/contributing/generating_a_preview#step-2-start-a-local-server)과 같은 사이트 기능을 문서화했습니다.

### 데이터 유연성

#### 캔버스 항목 속성 업데이트

캔버스 항목 속성은 이제 [캔버스 컨텍스트 변수]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties)의 일부입니다. 각 컨텍스트 변수에는 이름, 데이터 유형, Liquid를 포함할 수 있는 값이 포함됩니다. 자세한 내용은 [컨텍스트 구성 요소]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context)를 참조하십시오.

#### 전화번호 필터에 대한 세분화 필터 업데이트

세분화 필터는 두 개의 전화번호 필터에 대한 변경 사항을 반영하도록 업데이트되었습니다:

- [형식이 없는 전화번호]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters#unformatted-phone-number) (이전의 **전화번호**): 형식이 없는 전화번호로 사용자를 세분화합니다.
- [전화번호]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters#phone-number) (이전의 **발신 전화번호**): E.164 형식의 전화번호 필드로 사용자를 세분화합니다.

#### 사용자 정의 데이터 삭제

타겟팅 캠페인과 세그먼트를 구축하다 보면 더 이상 맞춤 이벤트나 맞춤 속성이 필요하지 않을 수 있습니다. 이제 [이 사용자 정의 데이터]({{site.baseurl}}/user_guide/data/custom_data/managing_custom_data#deleting-custom-data)를 삭제하고 앱에서 참조를 제거할 수 있습니다.

#### 이메일 주소와 전화번호로 사용자 가져오기

이제 이메일 주소나 전화번호를 사용하여 [사용자를 가져올]({{site.baseurl}}/user_guide/data/user_data_collection/user_import/#importing-with-email-addresses-and-phone-numbers) 수 있으며 외부 ID나 사용자 별칭을 생략할 수 있습니다.

#### 서비스 제공자 주도 로그인 문제 해결

서비스 제공자(SP) 주도 로그인에는 이제 SAML 및 단일 로그인 문제를 해결하는 데 도움이 되는 [문제 해결 섹션]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/set_up/#troubleshooting)이 있습니다.

#### 사용자 가져오기 문제 해결

[사용자 가져오기 문제 해결 섹션]({{site.baseurl}}/user_guide/data/user_data_collection/user_import#troubleshooting)에는 가져온 CSV 파일에서 누락된 행을 문제 해결하는 방법을 포함하여 새로운 항목과 업데이트된 항목이 있습니다.

#### 세그먼트 확장에 대한 자주 묻는 질문

세그먼트 확장에 대한 [자주 묻는 질문]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/#frequently-asked-questions)을 확인해 보세요. 여러 커스텀 이벤트를 사용하는 세그먼트 확장을 만드는 방법도 포함되어 있습니다.

#### 개인화된 및 확장된 지연

{% multi_lang_include release_type.md release="조기 액세스" %}

사용자를 위한 [개인화된 지연]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/delay_step#personalized-delays)을 설정하고 이를 Context 단계와 함께 사용하여 지연할 컨텍스트 변수를 선택할 수 있습니다.

이제 지연 단계를 최대 2년까지 연장할 수 있습니다. 예를 들어, 앱의 새로운 사용자를 온보딩하는 경우, 세션을 시작하지 않은 사용자에게 알림 메시지를 보내기 전에 2개월의 연장된 지연을 추가할 수 있습니다.

#### Snowflake의 기본 사용자 프로필 속성

{% multi_lang_include release_type.md release="베타" %}

이제 Snowflake에 세 가지 [기본 사용자 프로필 속성]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/user_attributes/)이 있습니다. 각 뷰는 특정 사용 사례에 맞게 설계되었으며, 고유한 성능 고려 사항이 있습니다. 예를 들어, 사용자 프로필의 기본 속성에 대한 주기적인 스냅샷을 제공받을 수 있습니다.

### 강력한 채널

#### 메시징 기본 사항

[메시징 기본 사항]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals)은 캠페인 및 캔버스에 대한 공유 개념과 용어를 포함하는 Engagement Tools의 새로운 섹션입니다. 메시지 아카이빙 및 현지화와 같은 내용이 포함됩니다.

#### WhatsApp 커스텀 도메인

이제 하나 이상의 WhatsApp 구독 그룹에 [커스텀 도메인]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/custom_domains/)을 할당할 수 있습니다.

#### 캔버스를 위한 트리거된 인앱 메시지

이제 세션 시작 시 또는 커스텀 이벤트 및 구매에 의해 트리거될 [인앱 메시지의 트리거]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_by_channel/in-app_messages_in_canvas)를 선택할 수 있습니다. 모든 지연이 지나고 오디언스 옵션이 확인되면, 사용자가 메시지 단계에 도달할 때 인앱 메시지가 활성화됩니다. 사용자가 세션을 시작하고 인앱 메시지의 트리거 이벤트를 수행하면, 사용자는 인앱 메시지를 보게 됩니다. 

#### 캔버스의 입장량 제한

선택한 주기(일일, 캔버스의 전체 수명 또는 캔버스가 예약될 때마다)에 따라 이 캔버스에 들어갈 수 있는 사람 수를 제한할 수 있습니다. 예를 들어, [입장 제어 설정]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas?tab=action-based%20delivery#step-2c-set-your-target-entry-audience)을 통해 캔버스가 하루에 5,000명에게만 전송되도록 할 수 있습니다.

#### 새로운 사용 사례: 예약 알림 이메일 시스템

Braze 기능을 사용하여 [예약 알림 이메일 메시징 서비스를 구축하는 방법]({{site.baseurl}}/user_guide/engagement_tools/canvas/ideas_and_strategies/booking_use_case)을 알아보세요. 이 서비스는 사용자가 약속을 예약할 수 있게 하며, 다가오는 약속에 대한 알림 메시지를 사용자에게 보냅니다. 이 사용 사례는 이메일 메시지를 사용하지만, 사용자 프로필에 대한 단일 업데이트를 기반으로 모든 채널 또는 여러 채널에서 메시지를 보낼 수 있습니다.

#### 특정 링크에 대한 클릭 추적

HTML 편집기에서 이메일 메시지에 HTML 코드를 추가하거나 드래그 앤 드롭 편집기의 구성 요소에 추가하여 특정 링크에 대한 클릭 추적을 [끄는 방법]({{site.baseurl}}/user_guide/message_building_by_channel/email/universal_links#turning-off-click-tracking-on-a-link-to-link-basis)을 설정할 수 있습니다.

#### 동적 Apple 푸시 알림 서비스 게이트웨이 관리

[동적 APNs 게이트웨이 관리]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift#swift_dynamic-apns-gateway-management)은 올바른 APNs 환경을 자동으로 감지하여 iOS 푸시 알림의 신뢰성과 효율성을 향상시킵니다. 이전에는 푸시 알림을 위해 APNs 환경(개발 또는 프로덕션)을 수동으로 선택해야 했으며, 이로 인해 잘못된 게이트웨이 구성, 전달 실패 및 BadDeviceToken 오류가 발생할 수 있었습니다.

#### 배너에 대한 Flutter 지원

{% multi_lang_include release_type.md release="조기 액세스" %}

배너는 이제 Flutter를 지원합니다. 또한 모든 배너 문서가 더 쉽게 사용할 수 있도록 개편되었습니다. 시작하려면 다음 기사를 확인하세요:

- [배너에 대하여]({{site.baseurl}}/developer_guide/banners/)
- [배너 캠페인 만들기]({{site.baseurl}}/user_guide/message_building_by_channel/banners/creating_campaigns/)
- [앱에 배너 삽입하기]({{site.baseurl}}/developer_guide/banners/creating_placements/)

#### WhatsApp 클릭 추적

{% multi_lang_include release_type.md release="조기 액세스" %}

[클릭 추적]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/click_tracking/)은 누군가 WhatsApp 메시지의 링크를 탭할 때를 측정할 수 있게 해주며, 어떤 콘텐츠가 참여를 유도하는지 명확하게 보여줍니다. Braze는 URL을 단축하고, 백그라운드에서 추적을 추가하며, 클릭 이벤트가 발생할 때 이를 기록합니다.

#### 푸시에 대한 자주 묻는 질문

푸시 캠페인을 설정할 때 발생하는 가장 자주 묻는 질문을 다룬 [푸시 FAQ]({{site.baseurl}}/user_guide/message_building_by_channel/push/faq) 기사를 확인해 보세요.

#### 푸시 문제 해결

[푸시 문제 해결]({{site.baseurl}}/user_guide/message_building_by_channel/push/troubleshooting)은 푸시 알림의 전달 문제를 해결하는 데 도움이 되는 여러 단계를 제공합니다. 예를 들어, 푸시 알림의 전달 문제를 겪고 있다면, 문제를 해결하기 위해 취할 수 있는 단계를 정리했습니다.

### 새로운 Braze 파트너십

#### Movable Ink 다빈치 - 동적 콘텐츠

Braze와 Movable Ink [다빈치]({{site.baseurl}}/partners/movable_ink_da_vinci) 통합은 브랜드가 다빈치의 AI 기반 콘텐츠 결정 엔진을 활용하여 매우 개인화된 메시지를 전달할 수 있도록 합니다. 다빈치는 각 사용자에게 가장 관련성 높은 콘텐츠를 선별하고 Braze를 통해 메시지를 원활하게 배포합니다.

### SDK 업데이트

다음 SDK 업데이트가 릴리스되었습니다. 주요 업데이트는 아래에 나열되어 있으며, 그 외의 모든 업데이트는 해당 SDK 체인지로그를 확인하면 확인할 수 있습니다.

- [Flutter SDK 13.0.0](https://pub.dev/packages/braze_plugin/changelog)
    - 네이티브 Android 브리지를 [Braze Android SDK 33.0.0에서 35.0.0으로](https://github.com/braze-inc/braze-android-sdk/compare/v33.0.0...v35.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed) 업데이트합니다.
        - 필수 Android SDK 버전은 25입니다. 자세한 내용은 [여기](https://github.com/braze-inc/braze-android-sdk?tab=readme-ov-file#version-information)를 참조하세요.
- [Swift SDK v11.8.0-11.9.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md)
- [Web SDK v5.8.0](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md)

## 2025년 3월 4일 출시

### 연기

Braze는 소프트 바운스의 정의를 업데이트했으며, 2025년 2월 25일 오전 10시 EST부터 [연기]({{site.baseurl}}/user_guide/message_building_by_channel/email/reporting_and_analytics/email_reporting/#email-performance)라는 새로운 이벤트를 전송합니다.

Sendgrid 고객을 위해, 우리는 소프트 바운스 이벤트에서 연기 이벤트를 분리하는 변경을 했습니다. 우리는 연기된 이벤트를 소프트 바운스 이벤트로 계산합니다. 이는 Currents, Query Builder, SQL Extension, Snowflake 데이터 공유 또는 우리의 트랜잭션 이메일 제품을 사용하는 모든 Sendgrid 고객에게 영향을 미칩니다.

#### 이전 동작

2025년 2월 25일 이전에 캠페인 또는 캔버스의 이메일 주소에 대한 연기된 이벤트는 매번 소프트 바운스 이벤트를 기록합니다. 결과적으로, 연기는 소프트 바운스 데이터의 일부로 포함됩니다. 이로 인해 사용자 또는 캠페인이 예상보다 더 많은 소프트 바운스 이벤트를 보고할 수 있습니다. 

#### 새로운 행동

2025년 2월 25일부터, 지연된 이벤트는 매번 소프트 바운스 이벤트를 기록하지 않습니다. 대신, 이메일 주소당 한 번의 소프트 바운스 이벤트만 기록하며, 이메일이 몇 번 재시도되거나 지연되었는지에 관계없이 기록됩니다.

#### 이것이 의미하는 바

2025년 2월 25일부터 소프트 바운스 이벤트의 양이 크게 감소하는 것을 알 수 있으며, 이는 다음과 같은 잠재적인 변화를 초래합니다:

- 쿼리 빌더를 사용하여 작성된 모든 보고서에서 소프트 바운스 감소
- Y 기간 동안 X회 소프트 바운스를 경험한 사용자를 타겟팅하는 경우 SQL 확장을 사용하여 더 작은 세그먼트 크기
- 커런츠 및 스노우플레이크의 모든 기능을 사용하여 전달된 소프트 바운스 이벤트 수 감소
- 트랜잭션 이메일 제품의 소프트 바운스 수 감소

스파크포스트 고객의 경우, 소프트 바운스 이벤트 데이터에 영향이 없으며, 대신 커런츠와 스노우플레이크에서 새로운 이메일 이벤트인 지연을 받기 시작합니다.

### 개발자 가이드 정리

여러 SDK에서 공유되는 동일한 콘텐츠가 문서 사이트의 새로운 SDK 탭 기능을 사용하여 통합되기 시작했습니다. 이번 달 [SDK 통합]({{site.baseurl}}/developer_guide/sdk_integration/), [SDK 초기화]({{site.baseurl}}/developer_guide/sdk_initialization/), 및 [콘텐츠 카드]({{site.baseurl}}/developer_guide/content_cards/)가 결합되었습니다. 앞으로 몇 달 동안 더 많은 업데이트를 기대해 주세요.

### 데이터 유연성
 
#### 사용자 프로필에 대한 브레이즈 ID

이제 사용자 프로필에는 [브레이즈 ID]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles#user-profiles)가 포함됩니다. 사용자 프로필을 검색할 때 이를 사용할 수 있습니다.

#### 연기

브레이즈는 소프트 바운스의 정의를 업데이트했으며, 이메일이 즉시 전달되지 않았을 때 새로운 이벤트인 [지연]({{site.baseurl}}/user_guide/message_building_by_channel/email/reporting_and_analytics/email_reporting#email-performance)을 전송하고 있습니다. 이는 브레이즈가 이 임시 전달 실패 후 최대 72시간 동안 이메일을 재시도하여 성공적인 전달 가능성을 극대화하기 위해 특정 캠페인에 대한 시도가 중단되기 전에 발생합니다.

#### 스노우플레이크 엔티티 관계
 
우리는 스노우플레이크와 브레이즈 엔티티 관계에 대한 [원시 테이블 스키마](https://www.braze.com/docs/assets/download_file/data-sharing-raw-table-schemas.txt)를 새로운 [사용자 친화적인 문서 페이지](https://www.braze.com/docs/partners/data_and_infrastructure_agility/data_warehouses/snowflake/entity_relationships)에 매핑했습니다. 각 채널에 속하는 `USER_MESSAGES` 테이블의 세부 사항과 각 테이블의 기본 키, 외래 키 및 기본 키에 대한 설명이 포함되어 있습니다.

#### 외부 ID에 대한 아이덴티티 관리

이메일 주소 또는 해시된 이메일 주소를 Braze 외부 ID로 사용하면 데이터 소스 전반에 걸쳐 아이덴티티 관리를 단순화할 수 있지만, 사용자 개인 정보 및 데이터 보안에 대한 [잠재적 위험]({{site.baseurl}}/user_guide/data/user_data_collection/user_profile_lifecycle/#identified-user-profiles)을 고려하는 것이 중요합니다.
 
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

지연 단계에서 **지연 개인화** 토글을 선택하여 사용자에 대한 [개인화된 지연]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/delay_step/#personalized-delays)을 설정할 수 있습니다. 컨텍스트 변수를 선택하여 지연할 때 이와 함께 컨텍스트 단계를 사용할 수 있습니다.

캔버스 사용자 여정에서 지연 단계를 설정할 때 이제 최대 2년까지 지연을 생성할 수 있습니다.

#### 자동 동기화 되돌리기

[이메일 메시지 작성 중]({{site.baseurl}}/user_guide/message_building_by_channel/email/html_editor/creating_an_email_campaign/#step-3-compose-your-email)에는 일반 텍스트 탭에서 HTML에서 다시 생성 아이콘을 선택하여 자동 동기화로 되돌릴 수 있으며, 이는 일반 텍스트가 동기화되지 않을 때만 나타납니다.

![Braze에서 자동 동기화를 위한 되돌리기 버튼입니다.]({% image_buster /assets/img/release_notes/2025_05_04/regenerate_from_html.png %})
 
### 강력한 채널

#### 안드로이드 라이브 업데이트

라이브 업데이트는 공식적으로 제공되지 않지만
[안드로이드 16](https://android-developers.googleblog.com/2025/01/first-beta-android16.html), 우리의 [안드로이드용 라이브 업데이트]({{site.baseurl}}/developer_guide/push_notifications/live_notifications/?sdktab=android&tab=local) 페이지는 그들의 동작을 에뮬레이트하는 방법을 보여주므로, [Swift Braze SDK]({{site.baseurl}}/developer_guide/push_notifications/live_notifications/?sdktab=swift)의 라이브 활동과 유사한 인터랙티브 잠금 화면 알림을 표시할 수 있습니다. 공식 라이브 업데이트와 달리, 이 기능은 이전 안드로이드 버전에서도 구현할 수 있습니다.

#### 작업 공간 간 기능 플래그가 있는 캠페인 복사하기

이제 [작업 공간 간 기능 플래그가 있는 캠페인 복사]({{site.baseurl}}/user_guide/engagement_tools/campaigns/managing_campaigns/copying_to_workspace/#copying-campaigns-with-feature-flags)가 가능합니다. 이를 위해서는 대상 작업 공간에 원래 캠페인에서 참조된 기능 플래그와 일치하는 ID로 구성된 기능 플래그 실험이 설정되어 있어야 합니다.

#### 새로운 WhatsApp 메시지 유형 지원

WhatsApp 메시지는 이제 [비디오, 오디오 및 문서 아웃바운드 메시지]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/create#outbound-messages)를 지원합니다. Contact your Braze account manager if you're interested in participating in the early access.

#### 오른쪽에서 왼쪽으로 읽는 메시지

[오른쪽에서 왼쪽으로 읽는 메시지 만들기]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/right_to_left_messages/)는 오른쪽에서 왼쪽으로 읽는 언어로 메시지를 작성하는 모범 사례를 다루어, 메시지가 가능한 한 정확하게 표시되도록 합니다.
 
### AI 및 ML 자동화
 
#### 항목 추천

[메시징에서 항목 추천 사용하기]({{site.baseurl}}/user_guide/brazeai/recommendations/using_recommendations)는 `product_recommendation` Liquid 객체를 다루며, 이 지식을 실제로 적용하는 데 도움이 되는 튜토리얼을 포함합니다.

### 새로운 Braze 파트너십
 
#### 이메일 사랑 - 채널 확장
 
Braze와 [이메일 사랑]({{site.baseurl}}/partners/message_orchestration/) 파트너십은 이메일 사랑의 Braze로 내보내기 기능과 Braze API를 활용하여 이메일 템플릿을 Braze에 원활하게 업로드합니다.

#### VWO - A/B 테스트
 
Braze와 [VWO]({{site.baseurl}}/partners/data_and_analytics/ab_testing/vwo/) 통합을 통해 VWO 실험 데이터를 활용하여 타겟 세그먼트를 만들고 개인화된 캠페인을 제공할 수 있습니다.
 
### SDK 업데이트
 
다음 SDK 업데이트가 릴리스되었습니다. 주요 업데이트는 아래에 나열되어 있으며, 그 외의 모든 업데이트는 해당 SDK 체인지로그를 확인하면 확인할 수 있습니다.
 
- [React Native](https://github.com/braze-inc/braze-react-native-sdk/blob/master/CHANGELOG.md)
    - React Native 최소 요구 버전을 [0.71.0](https://reactnative.dev/blog/2023/01/12/version-071)으로 증가시킵니다. 자세한 내용은 React 작업 그룹의 [릴리스 지원 정책](https://github.com/reactwg/react-native-releases#releases-support-policy)을 참조하십시오.
    - 최소 요구 iOS 버전을 12.0으로 증가시킵니다.
    - 네이티브 iOS 버전 바인딩을 [Braze Swift SDK 7.5.0에서 8.1.0](https://github.com/braze-inc/braze-swift-sdk/compare/7.5.0...8.1.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed)으로 업데이트합니다.
    - 네이티브 Android 버전 바인딩을 [Braze Android SDK 29.0.1에서 30.1.1로](https://github.com/braze-inc/braze-android-sdk/compare/v29.0.1...v30.1.1#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed) 업데이트합니다.

## 2025년 2월 4일 출시

### Braze 문서 개선

#### 기여 가이드
최근 [기여 가이드]({{site.baseurl}}/contributing/your_first_contribution)에 대한 업데이트로 비기술 사용자가 Braze 문서에 기여하기가 더 쉬워졌습니다.

#### 데이터 및 분석 개편
원하는 정보를 더 쉽게 찾을 수 있도록 "데이터 및 분석" 아래에 있던 기사를 [데이터]({{site.baseurl}}/user_guide/data)와 [분석]({{site.baseurl}}/user_guide/analytics)으로 분리했습니다. 

#### 개발자 가이드
모든 문서에 대한 대규모 정리를 수행했으며, [Braze 개발자 가이드]({{site.baseurl}}/developer_guide/home)에 포함된 여러 페이지에 나뉘어 있던 "사용 방법"을 하나의 페이지로 통합했습니다.

모든 Braze SDK에 대한 참조 문서와 리포지토리를 나열하는 새로운 [SDK 참조 페이지]({{site.baseurl}}/developer_guide/references)도 추가되었습니다.

##### 언리얼 엔진 Braze SDK
Unreal Engine Braze SDK GitHub 리포지토리 README의 모든 콘텐츠를 Braze 문서의 [전용 섹션]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=unreal%20engine)으로 마이그레이션하고 재작성했습니다.

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

#### 이메일 주소를 사용하여 캠페인 또는 캔버스를 트리거합니다.

{% multi_lang_include release_type.md release="일반 사용 가능" %}

이제 이메일 주소로 수신자를 지정하여 [캠페인]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/targeting_users/)과 [캔버스]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/?tab=target%20audience#step-2c-set-your-target-entry-audience)를 트리거할 수 있습니다.

#### API를 통해 사용자를 식별하기 위해 전화번호를 사용합니다.

{% multi_lang_include release_type.md release="일반 사용 가능" %}

이제 별칭 및 이메일 주소 외에도 전화번호를 사용하여 [`/users/identify` API 엔드포인트]({{site.baseurl}}/api/endpoints/user_data/post_user_identify)를 통해 사용자를 식별할 수 있습니다.

#### SAML 추적 가져오기
SAML SSO와 관련된 문제를 보다 효율적으로 해결하는 데 도움이 되는 [ SAML 추적을 얻는 방법에 대한 단계]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/set_up#obtaining-a-saml-trace)을 추가했습니다.
 
#### 지역별 데이터 센터
Braze가 새로운 지역을 서비스하기 위해 성장함에 따라, 운영 접근 방식을 명확히 하기 위해 [Braze 데이터 센터에 대한 기사]({{site.baseurl}}/user_guide/data/data_centers)를 추가했습니다.
 
### 창의력 발휘
 
#### 가격 인하 알림 및 재고 복귀 알림

{% multi_lang_include release_type.md release="일반 사용 가능" %}

이제 캔버스와 카탈로그를 통해 [재고 복귀 알림]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/catalog_triggers/back_in_stock_notifications)을 설정하여 고객에게 품목이 재고에 다시 들어왔을 때 알릴 수 있습니다.

또한 카탈로그와 캔버스에서 가격 인하 알림을 설정하여 품목의 가격이 하락했을 때 고객에게 알리는 [가격 인하 알림]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/catalog_triggers/price_drop_notifications)을 생성할 수 있습니다.

#### 선택 미리보기 

{% multi_lang_include release_type.md release="일반 사용 가능" %}

선택을 생성한 후, 무작위 사용자 또는 특정 사용자에 대해 [선택이 반환할 내용을 보기]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/selections/#test-and-preview)할 수 있습니다.

#### Liquid를 포함한 카탈로그 항목 템플릿 

{% multi_lang_include release_type.md release="일반 사용 가능" %}

Liquid를 포함하는 [템플릿 카탈로그 항목을 만들 수 있습니다]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/using_catalogs/#using-liquid).

#### 캔버스 템플릿
우리는 [선호도 설문조사로 온보딩 사용자]({{site.baseurl}}/user_guide/engagement_tools/canvas/get_started/braze_templates/preference_survey)와 [더블 옵트인으로 이메일 가입 생성]({{site.baseurl}}/user_guide/engagement_tools/canvas/get_started/braze_templates/email_signup)을 위한 새로운 캔버스 템플릿을 추가했습니다.

#### B2B를 위한 Salesforce Sales Cloud로 리드 관리
B2B 마케터가 Braze를 사용하는 한 가지 방법은 Salesforce Sales Cloud와의 통합을 통해서입니다. 이 [사용 사례]({{site.baseurl}}/user_guide/getting_started/b2b_use_cases/b2b_salesforce_sales_cloud)를 구현하는 방법에 대해 더 읽어보세요.
 
### 강력한 채널

#### 억제 목록

{% multi_lang_include release_type.md release="베타" %}
 
[억제 목록]({{site.baseurl}}/user_guide/engagement_tools/segments/suppression_lists)은 메시지를 절대 받지 않을 사용자 그룹을 지정합니다. 관리자는 세분화와 동일한 방식으로 사용자 그룹을 좁히기 위해 세그먼트 필터로 억제 목록을 생성할 수 있습니다.

### 새로운 Braze 파트너십

#### 생성자 - 동적 콘텐츠
[생성자]({{site.baseurl}}/partners/ecommerce/product_search_recommendations/constructor/)는 AI와 머신 러닝을 사용하여 전자상거래 및 소매 웹사이트를 위한 개인화된 검색, 추천 및 탐색 경험을 제공하는 검색 및 제품 발견 플랫폼입니다.
 
#### 트러스트파일럿 - 동적 콘텐츠
[트러스트파일럿]({{site.baseurl}}/partners/trustpilot/)은 고객이 피드백을 공유하고 리뷰를 관리하고 응답할 수 있도록 하는 온라인 리뷰 플랫폼입니다.

### SDK 업데이트
 
다음 SDK 업데이트가 릴리스되었습니다. 주요 업데이트는 아래에 나열되어 있으며, 그 외의 모든 업데이트는 해당 SDK 체인지로그를 확인하면 확인할 수 있습니다.
 
- [브레이즈 안드로이드 SDK 34.0.0](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#3400)
    - 최소 SDK 버전을 21(롤리팝)에서 25(누가)로 업데이트했습니다.

## 2025년 1월 7일 출시

### 창의력 발휘

#### 앱 내 메시지 템플릿

드래그 앤 드롭 앱 내 메시지를 위한 [템플릿]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/)을 추가했습니다.

#### B2B 세일즈포스 세일즈 클라우드 리드 관리

[세일즈포스 세일즈 클라우드로 리드 관리하기]({{site.baseurl}}/user_guide/getting_started/b2b_use_cases/b2b_salesforce_sales_cloud/)는 커뮤니티 제출 통합을 통해 브레이즈 웹훅을 사용하여 세일즈포스 세일즈 클라우드에서 리드를 생성하고 업데이트하는 방법을 보여줍니다.

### 강력한 채널

#### 캔버스 템플릿

이중 옵트인으로 [이메일 가입]({{site.baseurl}}/user_guide/engagement_tools/canvas/get_started/braze_templates/email_signup/) 및 [선호도 설문조사로 온보딩]({{site.baseurl}}/user_guide/engagement_tools/canvas/get_started/braze_templates/preference_survey/)을 위한 브레이즈 캔버스 템플릿을 추가했습니다.

#### WhatsApp 옵트인 정책 변경

메타는 최근 [옵트인 정책을](https://developers.facebook.com/docs/whatsapp/overview/getting-opt-in/) 업데이트했습니다. 추가 정보는 [WhatsApp 제품 업데이트]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/meta_resources/)를 참조하세요.

#### 이메일 드래그 앤 드롭 편집기의 콘텐츠 블록에 대한 너비 도구

드래그 앤 드롭 이메일 편집기에서 콘텐츠 블록의 [너비를 조정할 수 있습니다]({{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/dnd_content_blocks/#using-the-editor-to-add-a-content-block). 기본값 너비는 100%입니다.

### 데이터 유연성

#### 소프트 바운스된 세그먼트 필터

Y일 동안 소프트 바운스 횟수별로 사용자를 세분화하세요. 자세한 내용은 [세분화 필터 용어집]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters#soft-bounced)을 참조하세요.

#### 익명 사용자 개요

[익명 사용자]({{site.baseurl}}/user_guide/data/user_data_collection/user_profile_lifecycle/anonymous_users/)는 익명 사용자 및 사용자 별칭에 대한 개요를 제공하며, 그 중요성과 메시지에서 활용할 수 있는 방법을 설명합니다.

#### 글로벌 컨트롤 그룹 멤버십

개별 사용자의 프로필의 **참여** 탭으로 이동하여 [글로벌 컨트롤 그룹 멤버십]({{site.baseurl}}/user_guide/engagement_tools/testing/global_control_group/#view-whether-a-user-is-in-a-global-control-group)을 **기타** 섹션으로 스크롤하여 볼 수 있습니다.

### 새로운 Braze 파트너십

#### 저스투노 - 리드 캡처

[Justuno]({{site.baseurl}}/partners/data_and_analytics/leads_capture/justuno/)는 모든 청중을 위한 완전히 최적화된 방문자 경험을 동적 세그먼트를 통해 생성할 수 있게 해주며, 사이트 속도나 개발 작업을 증가시키지 않고도 가장 진보된 타겟팅을 제공합니다.

#### Odicci - 고객 데이터 플랫폼

Braze를 [Odicci]({{site.baseurl}}/partners/odicci/)와 통합하여, 기업이 로열티 기반의 옴니채널 경험을 통해 고객을 획득하고, 참여시키며, 유지할 수 있도록 합니다.

#### Optimizely - A/B 테스트

Braze와 [Optimizely]({{site.baseurl}}/partners/data_and_analytics/ab_testing/optimizely/) 통합은 양방향 통합으로, 다음을 가능하게 합니다:

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

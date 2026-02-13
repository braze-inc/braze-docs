---
nav_title: 홈
article_title: 새로운 기능 Braze
description: "주요 제품 릴리스, 지속적인 제품 개선, Braze 파트너십, 소프트웨어 개발 키트 변경 사항 및 기능 사용 중단에 대한 최신 정보를 확인할 수 있도록 매월 Braze 릴리스 노트가 게시됩니다."
page_order: 0
search_rank: 1
page_type: reference

---

# 새로운 기능 Braze

{% alert tip %}
이 페이지에 나열된 업데이트에 대한 자세한 내용은 계정 매니저에게 문의하거나 [지원 티켓을 개설하세요]({{site.baseurl}}/user_guide/administrative/access_braze/support/). 월간 소프트웨어 개발 키트 릴리스, 개선 사항 및 주요 변경 사항에 대한 자세한 내용은 [SDK 체인지로그에서]({{site.baseurl}}/developer_guide/changelogs) 확인할 수도 있습니다.
{% endalert %}

{% details February 5, 2026 %}

## 2025년 2월 4일 출시

### BrazeAI<sup>TM</sup>

#### 콘텐츠 최적화 프로그램

{% multi_lang_include release_type.md release="Beta" %}

[콘텐츠 옵티마이저는]({{site.baseurl}}/user_guide/brazeai/content_optimizer) 자동화된 참여 최적화를 제공하는 지속적인 고배리언트 콘텐츠 테스트 캔버스 단계입니다. 메시지 단계와 유사한 드래그 앤 드롭 인터페이스를 사용하여 테스트할 구성 요소를 정의하고, AI를 사용하여 배리언트를 생성하거나 수동으로 입력한 다음, Liquid 태그를 사용하여 이러한 구성 요소를 메시지 콘텐츠에 매핑할 수 있습니다.

상황별 멀티암드 옵티마이저를 기반으로 구축된 콘텐츠 옵티마이저는 사용자당 단일 메시지를 전송하며, 예측 권장 사항을 기반으로 전달할 컴포넌트 배리언트 조합을 결정합니다. 단계가 시간이 지남에 따라 데이터를 수집함에 따라 성능이 우수한 배리언트는 자연스럽게 전송 할당이 증가하고 성능이 낮은 배리언트는 감소합니다. 콘텐츠 옵티마이저는 지속적인 최적화를 인에이블먼트하기 위해 일일 사용자 수가 일정한(하루 최소 수천 명) 반복 전송 캔버스에서 가장 잘 작동합니다.

### 채널 & 터치포인트

#### 배너의 현지화 번역

{% multi_lang_include release_type.md release="Early access" %}

작업 영역에 현지화를 추가하면 하나의 배너 내에서 [다양한 언어의 사용자를 타겟팅할]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/locales#translating-locales) 수 있습니다.

#### 드래그 앤 드롭 콘텐츠 블록의 너비 구성하기

탐색 메뉴에서 버튼을 선택하여 [콘텐츠 블록의 너비를 조정합니다]({{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/dnd_content_blocks/#using-the-editor-to-add-a-content-block). 이메일 글로벌 스타일 설정에서 지정하지 않은 경우 기본값은 100%이며, 그렇지 않은 경우 글로벌 설정이 적용됩니다.

![폭을 편집할 수 있는 양면 화살표.]({% image_buster /assets/img_archive/content_block_width_updated.png %}){: style="max-width:30%;" }

#### 자동화 IP 워밍업 사용

{% multi_lang_include release_type.md release="Early access" %}

[자동화된 IP 워밍업을]({{site.baseurl}}/user_guide/message_building_by_channel/email/email_setup/ip_warming/#automated-ip-warming) 사용하여 일일 전송량을 점진적으로 늘려 수신편지함 제공업체가 사용자의 전송 패턴을 학습하고 신뢰할 수 있도록 할 수 있습니다. Braze는 참여도가 가장 높은 가입자에게 먼저 전송하므로 일일 볼륨이 모범 사례에 맞는 속도로 증가할 수 있습니다.

### 파트너십

#### LinkedIn - 캔버스 오디언스 동기화

[Braze 오디언스 동기화를 LinkedIn]({{site.baseurl}}/partners/canvas_audience_sync/linkedin_audience_sync/)에 사용하면 Braze 통합의 사용자 데이터를 LinkedIn 고객 목록에 추가하여 행동 트리거, 세그먼트화 등을 기반으로 광고를 게재할 수 있습니다. 일반적으로 사용자 데이터를 기반으로 푸시, 이메일, SMS, 웹훅과 같은 메시지를 트리거하는 데 사용했던 모든 기준을 이제 LinkedIn 고객 목록에서 해당 사용자에게 광고를 트리거할 수 있습니다.

#### 오라클 크라우드 트위스트 - 데이터 & 분석

[오라클 크라우드트위스트는]({{site.baseurl}}/partners/crowdtwist) 브랜드가 개인화된 고객 경험을 제공할 수 있도록 지원하는 선도적인 클라우드 네이티브 고객 로열티 솔루션입니다. 이 솔루션은 100개 이상의 즉시 사용 가능한 고객 참여 경로를 제공하여 마케터가 고객에 대한 보다 완전한 시각을 개발할 수 있도록 빠른 가치 창출 시간을 제공합니다.

#### 풀스토리 - 동적 콘텐츠

[풀스토리의]({{site.baseurl}}/partners/fullstory/) 행동 데이터 플랫폼은 기술 리더가 더 나은 정보에 기반한 의사 결정을 내릴 수 있도록 지원합니다. 풀스토리의 특허 기술은 디지털 행동 데이터를 분석 스택에 주입하여 양질의 행동 데이터를 대규모로 활용함으로써 모든 디지털 방문을 유용한 인사이트로 전환합니다. 

#### 오픈 로열티 - 데이터 & 분석

[오픈 로열티는]({{site.baseurl}}/partners/openloyalty) 고객 충성도 및 보상 프로그램을 구축하고 관리할 수 있는 클라우드 기반 로열티 프로그램 플랫폼입니다. Braze와 오픈 로열티 데이터 통합은 포인트 잔액, 등급 변경, 만료 경고와 같은 로열티 데이터를 실시간으로 Braze에 직접 동기화합니다. 이를 통해 사용자의 로열티 상태가 변경되면 개인화된 메시지(이메일, 푸시, SMS)를 트리거할 수 있습니다.

#### Extensions

[DOTS.ECO]({{site.baseurl}}/partners/docs.eco) 를 사용하면 추적 가능한 디지털 인증서를 통해 실제 환경에 미치는 영향에 대해 사용자에게 보상할 수 있습니다. 각 인증서는 공유 가능한 인증서 URL 및 이미지 URL과 같은 메타데이터를 포함할 수 있으므로 사용자는 자신의 영향력 증명을 보고 다시 방문할 수 있습니다.

### Mailizio - 메시지 오케스트레이션

[Mailizio는]({{site.baseurl}}/partners/mailizio/) 직관적인 시각적 편집기를 사용하여 재사용 가능하고 브랜드에 안전한 콘텐츠를 쉽게 디자인할 수 있는 이메일 제작 및 관리 플랫폼입니다. Mailizio를 Braze에 통합하면 콘텐츠 블록과 이메일 템플릿을 내보낸 다음 동일한 자산에서 인앱 메시지를 자동으로 생성하여 빠르고 완벽하게 제어되는 캠페인 배포를 할 수 있습니다.

### API

#### 미디어 라이브러리 POST API

{% multi_lang_include release_type.md release="General availability" %}

이제 API를 통해 미디어 라이브러리 자산을 추가할 수 있어 고객, 파트너, 대행사가 메시지 제작 워크플로우를 더 많이 자동화할 수 있습니다. [API를]({{site.baseurl}}/api/endpoints/media_library/manage_assets/create) 사용하여 자산 파일을 직접 업로드하거나 기존 URL에서 파일을 복사할 수 있습니다. 이 기능을 통해 통합 및 자동화 기능을 사용할 수 있습니다.

### 커런츠 및 데이터 공유

#### 스토리지 대상 및 데이터공유에 대한 에이전트 콘솔 이벤트

{% multi_lang_include release_type.md release="General availability" %}

이제 스토리지 대상(AWS S3, GCS, Azure Blob Storage) 및 Snowflake Datashare를 위한 두 가지 새로운 [이벤트](http://braze.com/docs/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events) ( `agentconsole.AgentExecuted` 및 `agentconsole.ToolInvocation`)를 이용할 수 있습니다. 이러한 이벤트를 통해 상담원 콘솔 사용량과 다운스트림 시스템의 세부 정보를 분석하여 상담원 사용량을 이해하고 최대한 활용할 수 있도록 인에이블먼트할 수 있습니다. 에이전트를 사용하면 캔버스 또는 카탈로그에서 콘텐츠를 생성하고 지능적인 의사 결정에 따라 사용자를 다른 경로로 라우팅하는 등 Braze 전반에서 특정 작업을 수행할 수 있는 지능형 에이전트를 만들고 배포할 수 있습니다. 자세한 내용은 [커런츠 체인지로그를](https://www.braze.com/docs/user_guide/data/distribution/braze_currents/event_glossary/currents_changelogs#changes-in-version-5-release-date-2026-02-04) 참조하세요.

#### 개별 채널에 대한 새로운 '재시도' 이벤트

{% multi_lang_include release_type.md release="General availability" %}

이제 이메일, LINE, 푸시 알림, SMS, 웹훅, WhatsApp 채널에 새로운 [재시도 이벤트를](https://www.braze.com/docs/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events) 사용할 수 있습니다. 이러한 이벤트는 최대 게재빈도 설정으로 인해 예약된 메시징이 중단되지 않고 지연되는 경우에 대한 가시성을 제공합니다. 메시지의 우선순위가 낮아지거나 게재빈도가 제한되는 경우, 이제 구성된 재시도 기간 내에 재시도할 수 있어 메시지 전달 패턴과 최대 게재빈도 제한의 영향에 대해 더 나은 인사이트를 얻을 수 있습니다. 자세한 내용은 [커런츠 체인지로그를](https://www.braze.com/docs/user_guide/data/distribution/braze_currents/event_glossary/currents_changelogs#changes-in-version-5-release-date-2026-02-04) 참조하세요.

#### 토큰 상태 변경 이벤트에 'time_ms' 필드 추가

{% multi_lang_include release_type.md release="General availability" %}

이벤트에 새로운 `time_ms` 필드가 추가되어 [`users.behaviors.pushnotification.TokenStateChange`](https://www.braze.com/docs/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events) 이벤트에 밀리초 수준의 세분성을 제공하여 푸시 토큰 상태 변화를 추적할 수 있습니다. 이 향상된 정밀도는 같은 초 내에 여러 변경 사항이 발생할 때 푸시 토큰의 최신 상태를 파악하는 데 도움이 되며, 다운스트림 시스템에서 올바른 구독 상태를 유지하고 있다는 확신을 줄 수 있습니다. 자세한 내용은 [커런츠 체인지로그를](https://www.braze.com/docs/user_guide/data/distribution/braze_currents/event_glossary/currents_changelogs#changes-in-version-5-release-date-2026-02-04) 참조하세요.

#### Tealium 대상으로 익명 사용자 보내기

{% multi_lang_include release_type.md release="General availability" %}

이제 외부 사용자 ID가 정의되지 않은 이벤트도 [Tealium]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/tealium/tealium_for_currents?redirected=1#tealium-for-currents) 대상으로 스트리밍할 수 있습니다. 커런츠 통합에서 '익명 사용자의 이벤트 포함' 확인란을 선택하면 외부 사용자 ID가 없는 이벤트가 억제되지 않고 대상에게 전송됩니다. 이 기능은 비식별자 및 익명 사용자와 관련된 다운스트림 분석 및 사용 사례에 매우 중요합니다.

##### 익명 사용자를 CustomHTTP 대상으로 보내기

{% multi_lang_include release_type.md release="Beta" %}

이제 외부 사용자 ID가 정의되지 않은 이벤트도 CustomHTTP 대상으로 스트리밍할 수 있습니다. 커런츠 통합에서 '익명 사용자의 이벤트 포함' 확인란을 선택하면 외부 사용자 ID가 없는 이벤트가 억제되지 않고 대상에게 전송됩니다. 이 기능은 비식별자 및 익명 사용자와 관련된 다운스트림 분석 및 사용 사례에 매우 중요합니다.

#### 이메일 오픈 이벤트 - "machine_open" 필드

[이메일 열기 이벤트는]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events#email-open-events) 이제 "machine_open" 필드 값을 생성하므로 다음을 보고할 수 있습니다. [_컴퓨터 열기_]({{site.baseurl}}/user_guide/analytics/reporting/report_metrics#machine-opens) 측정기준을 보고할 수 있습니다. 

### SDK

다음 SDK 업데이트가 릴리스되었습니다. Swift 소프트웨어 개발 키트 v14.0.1에서 유니버설 링크 처리 관련 문제가 수정되었습니다. Android 소프트웨어 개발 키트 v40.2.0은 잠재적인 메모리 누수를 수정하고 투명 활동이 있을 때 여러 세션이 열리는 문제를 해결합니다. 엑스포 SDK v3.2.0에는 `forwardUniversalLinks` 옵션(기본값: false)이 추가되어 유니버설 링크의 기본 Swift SDK 처리를 구성할 수 있습니다.

#### 소프트웨어 개발 키트 속보 업데이트

다음 SDK 업데이트가 릴리스되었습니다. 주요 업데이트는 아래에 나열되어 있으며, 그 외의 모든 업데이트는 해당 SDK 체인지로그를 확인하면 확인할 수 있습니다.

- [안드로이드 SDK 36.0.0](https://github.com/braze-inc/braze-android-sdk/releases/tag/v41.0.0)
    - 이름을 `BrazeConfig.Builder.setIsLocationCollectionEnabled()`에서 `setIsAutomaticLocationCollectionEnabled()`(으)로 변경했습니다.
    - 이름을 `BrazeConfig.isLocationCollectionEnabled`에서 `isAutomaticLocationCollectionEnabled`(으)로 변경했습니다.
    - 이름을 `BrazeConfigurationProvider.isLocationCollectionEnabled`에서 `isAutomaticLocationCollectionEnabled`(으)로 변경했습니다.
- [안드로이드 SDK 36.0.0](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#4020)
- [엑스포 플러그인 3.0.0](https://github.com/braze-inc/braze-expo-plugin/blob/main/CHANGELOG.md)
- [Swift SDK 11.0.1](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md)

{% enddetails %}

{% details January 8, 2026 %}
## 2025년 1월 7일 출시

### 데이터 & 보고

#### eCommerce 추천 이벤트

{% multi_lang_include release_type.md release="Early access" %}

전자상거래 추천 이벤트와 기존 구매 이벤트를 일치시키기 위해 '구매하기'와 유사한 ['주문하기' 전환 이벤트를]({{site.baseurl}}/user_guide/engagement_tools/canvas/ideas_and_strategies/ecommerce_use_cases/#conversions-report) 추가했습니다.

#### 커런츠 이벤트 업데이트

{% multi_lang_include release_type.md release="General availability" %}

버전 4에서 커런츠에 적용된 변경 사항은 다음과 같습니다:

* 이벤트 유형으로 필드 변경 `users.behaviors.pushnotification.TokenStateChange`:
    * 새로운 `string` 필드 추가 `push_token`: 이벤트의 푸시 토큰
* 이벤트 유형으로 필드 변경 `users.messages.pushnotification.Bounce`:
    * 새로운 `string` 필드 추가 `push_token`: 이벤트의 푸시 토큰
* 이벤트 유형으로 필드 변경 `users.messages.pushnotification.Send`:
    * 새로운 `string` 필드 추가 `push_token`: 이벤트의 푸시 토큰
* 이벤트 유형으로 필드 변경 `users.messages.rcs.Click`:
    * 새로운 `string` 필드 추가 `canvas_variation_name`: 이 사용자가 받은 캔버스 변형의 이름
    * `user_phone_number` 필드는 이제 *선택* 사항입니다.
* 이벤트 유형으로 필드 변경 `users.messages.rcs.InboundReceive`:
    * `user_id` 필드는 이제 *선택* 사항입니다.
* 이벤트 유형으로 필드 변경 `users.messages.rcs.Rejection`:
    * 새로운 `string` 필드 추가 `canvas_step_message_variation_id`: 이 사용자가 받은 캔버스 단계 메시지 변형의 API ID

각 릴리즈의 이벤트 변경 사항은 [커런츠 체인지로그를]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/currents_changelogs) 참조하세요.

#### 모든 행을 기준으로 동기화 로그 내보내기

{% multi_lang_include release_type.md release="Early access" %}

[클라우드 데이터 수집 **동기화 로그** 대시보드에서]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/sync_logs/#exporting-sync-logs) 동기화 실행에 대한 행 수준 로그를 내보내도록 선택할 수 있습니다:

* 오류가 있는 행 **오류** 상태인 행만 포함된 파일을 다운로드합니다.
* 모든 행 실행 중에 처리된 모든 행이 포함된 파일을 다운로드합니다.

### 채널 & 터치포인트

#### BYO(Bring Your Own) WhatsApp 커넥터

[BYO(Bring Your Own) WhatsApp 커넥터는]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/byo_connector/) Braze와 Infobip 간의 파트너십을 통해 사용자가 Infobip WhatsApp 비즈니스 매니저(WABA)에 대한 액세스 권한을 Braze에 부여하는 기능을 제공합니다. 이를 통해 메시지 세그먼트 세분화, 개인화, 캠페인 오케스트레이션을 위해 Braze를 사용하면서 Infobip으로 직접 메시징 비용을 관리하고 결제할 수 있습니다. 

#### 캔버스 배너

{% multi_lang_include release_type.md release="Early access" %}

캔버스의 [메시지 단계에서]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step) **배너를** 메시징 채널로 선택할 수 있습니다. 드래그 앤 드롭 편집기를 사용하여 개인화된 인라인 메시지를 생성하여 각 사용자 세션이 시작될 때 자동으로 업데이트되는 방해받지 않는 상황별 관련성 높은 경험을 제공할 수 있습니다. 

#### 동적 BCC

{% multi_lang_include release_type.md release="General availability" %}

[동적 BCC를]({{site.baseurl}}/user_guide/administrative/app_settings/email_settings/?tab=bcc%20address#dynamic-bcc) 사용하면 BCC 주소에 Liquid를 사용할 수 있습니다. 이 기능은 **이메일 환경설정에서만** 사용할 수 있으며 캠페인 자체에서는 설정할 수 없습니다. 이메일 수신자당 하나의 BCC 주소만 허용됩니다.

#### 채널 기반 요금 제한

전체 멀티채널 캠페인 또는 캔버스에서 공유되는 요금 제한 대신 채널별로 특정 요금 제한을 선택할 수 있습니다. 이 경우 선택한 각 채널에 요금 제한이 적용됩니다. 예를 들어, 캠페인 또는 캔버스에서 분당 최대 5,000개의 웹훅과 2,500개의 SMS 메시지를 전송하도록 설정할 수 있습니다. 자세한 내용은 [속도 제한 및 최대 게재빈도 설정을]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting) 참조하세요.

### 파트너십

#### LILT - 현지화

[LILT는]({{site.baseurl}}/partners/lilt/) 기업용 번역 및 콘텐츠 제작을 위한 완벽한 AI 솔루션입니다. LILT는 글로벌 조직이 AI 에이전트와 완전 자동화된 워크플로우를 통해 콘텐츠, 제품, 커뮤니케이션 및 지원 운영을 확장하고 최적화할 수 있도록 지원합니다.

### 소프트웨어 개발 키트 속보 업데이트

다음 SDK 업데이트가 릴리스되었습니다. 주요 업데이트는 아래에 나열되어 있으며, 그 외의 모든 업데이트는 해당 SDK 체인지로그를 확인하면 확인할 수 있습니다.

- [Android 13](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#4011)
- [안드로이드 SDK 36.0.0](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#4010)
- [Swift SDK 11.0.1](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md)
    - 뉴스피드를 제거합니다.
        - 이렇게 하면 뉴스피드와 관련된 모든 UI 요소, 데이터 모델 및 작업이 완전히 제거됩니다.
- [Web SDK 5.9.0](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md)

{% enddetails %}

{% details December 9, 2025 %}

## 2024년 12월 10일

### 데이터 & 보고

#### 랜딩 페이지에 Google 태그 매니저 추가하기

랜딩 페이지에 Google 태그 매니저를 추가하려면 드래그 앤 드롭 편집기에서 랜딩 페이지에 커스텀 코드 블록을 추가한 다음 [태그 매니저 코드를]({{site.baseurl}}/user_guide/engagement_tools/landing_pages#adding-google-tag-manager-to-a-landing-page) 블록에 [삽입합니다]({{site.baseurl}}/user_guide/engagement_tools/landing_pages#adding-google-tag-manager-to-a-landing-page).

### 오케스트레이션

#### SMS Liquid 사용 사례

[인바운드 SMS 키워드에 따라 다른 메시지로 응답]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/liquid_use_cases#sms-keyword-response) 사용 사례는 동적 SMS 키워드 처리를 통합하여 다른 메시지 카피로 특정 인바운드 메시징에 응답합니다. 예를 들어, 누군가 "START" 문자를 보낼 때와 "JOIN" 문자를 보낼 때 다른 응답을 보낼 수 있습니다.

#### 연결된 콘텐츠에 대한 허용 목록

[연결된 콘텐츠에]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/making_an_api_call) 사용할 특정 URL을 허용 목록에 추가할 수 있습니다. 이 기능을 이용하려면 고객 성공 매니저에게 문의하세요.

### 채널 & 터치포인트

#### SMS 문자 인코딩

이제 [SMS 세그먼트 계산기에]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/segments/#segment-calculator) 문자 인코딩 기능이 추가되었습니다! **문자 인코딩 표시를** 선택하여 어떤 문자가 GSM-7 또는 UCS-2로 인코딩되는지 식별할 수 있습니다. 

![텍스트 상자에 샘플 SMS 메시지를 입력하고 문자 인코딩이 켜져 있는 SMS 세그먼트 계산기.]({% image_buster /assets/img/sms/character_encoding.png %}){: style="max-width:70%;"}

#### 최적화가 적용된 WhatsApp 메시지

WhatsApp용 MM API는 100% 전달 가능성을 제공하지 않으므로, 다른 채널에서 메시지를 받지 못한 사용자를 리타겟팅하는 방법을 이해하는 것이 중요합니다. 

사용자를 리타겟팅하려면 특정 메시지를 수신하지 않은 사용자 세그먼트를 구축하는 것이 좋습니다. 이렇게 하려면 오류 코드 `131049` 로 필터링하세요. 이는 WhatsApp의 사용자별 마케팅 템플릿 제한 적용으로 인해 마케팅 템플릿 메시지가 전송되지 않았음을 나타냅니다. 이 작업은 [Braze 커런츠 또는 SQL 세그먼트 확장을 사용하여]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/optimized_delivery/#retargeting-users-on-other-braze-channels) 수행할 수 있습니다.

### 파트너십

#### 기타 레벨 - 동적 콘텐츠

[기타레벨은 제]({{site.baseurl}}/partners/otherlevels/) 너레이티브 AI를 사용하여 스포츠 브랜드, 퍼블리셔 및 운영자가 기존 콘텐츠를 대규모의 브랜드 개인화된 비디오 및 리치 미디어 경험으로 전환함으로써 고객과 연결하는 방식을 혁신하는 경험 플랫폼입니다.

### SDK

#### 소프트웨어 개발 키트 속보 업데이트

다음 SDK 업데이트가 릴리스되었습니다. 주요 업데이트는 아래에 나열되어 있으며, 그 외의 모든 업데이트는 해당 SDK 체인지로그를 확인하면 확인할 수 있습니다.

- [Web SDK 5.9.0](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md)

{% enddetails %}

{% details November 11, 2025 %}

## 2024년 11월:

### 데이터 유연성

#### `Live Activities Push to Start Registered for App` 세그먼트 세분화 필터

`Live Activities Push to Start Registered for App` 필터는 특정 앱에 대한 iOS 푸시 알림을 통해 라이브 활동을 시작하도록 등록되었는지 여부에 따라 사용자를 세그먼트화합니다.

#### RFM SQL 세그먼트 확장

[RFM(최근, 빈도, 금액) 세그먼트 확장을]({{site.baseurl}}/rfm_segments/) 생성하여 구매 습관을 측정하여 우수 사용자를 타겟팅할 수 있습니다.

RFM 분석은 각 카테고리(최근성, 빈도, 금액)별로 사용자에게 0~3점(3점이 최고점, 0점이 최저점)의 점수를 부여하여 최고의 사용자를 식별하는 마케팅 기법입니다. 최근성, 빈도 및 금전적 가치는 모두 사용자가 선택한 특정 시간 범위의 데이터를 기반으로 합니다.

#### 커스텀 속성 - 값 

사용량 보고서를 볼 때 [**값** 탭을]({{site.baseurl}}/user_guide/data/activation/custom_data/custom_attributes/#values-tab) 선택하면 약 25만 명의 사용자 샘플을 기준으로 선택한 커스텀 속성의 상위 값을 볼 수 있습니다.

#### 클라우드 데이터 수집을 위한 로그 및 통합 가시성 동기화

{% multi_lang_include release_type.md release="General availability" %}

클라우드 데이터 수집(CDI) [동기화 로그 대시보드를]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/sync_logs/) 사용하면 CDI에서 처리한 모든 데이터를 모니터링하고, 데이터가 성공적으로 동기화되었는지 확인하고, '부정확하거나 누락된' 데이터의 문제를 진단할 수 있습니다.

#### 다중 규칙 기능 플래그 롤아웃

[다중 규칙 기능 플래그 롤아웃을]({{site.baseurl}}/developer_guide/feature_flags/create/#multi-rule-feature-flag-rollouts) 사용하여 사용자를 평가하기 위한 일련의 규칙을 정의하면 정확한 세분화와 제어된 기능 릴리스가 가능합니다. 이 방법은 다양한 오디언스에게 동일한 기능을 배포하는 데 이상적입니다.

#### 드래그 앤 드롭 제품 블록을 위한 카탈로그 필드에 매핑하기

카탈로그 설정에서 **제품 블록** 토글을 선택하여 카탈로그의 [특정 필드]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/product_blocks/#catalog-setup) 및 [정보에 매핑할]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/product_blocks/#catalog-setup) 수 있습니다. 이를 통해 제품 제목, 제품 URL, 이미지 URL로 사용할 필드를 선택할 수 있습니다.

#### 커런츠에서 최대 게재빈도 설정 이벤트 중단

이제 커런츠 사용 시 채널 중단 이벤트에서 `abort_type` 을 참조할 수 있습니다. 최대 게재빈도 설정으로 인해 메시징이 중단되었음을 식별하고 중단의 원인이 된 최대 게재빈도 설정 규칙을 포함합니다. 최대 게재빈도 제한 규칙을 설정하는 데 도움이 됩니다. 특정 커런츠 이벤트에 대한 자세한 내용은 [메시지 참여 이벤트를]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events) 참조하세요.

### 강력한 채널

#### 배경 행 이미지 

{% multi_lang_include release_type.md release="General availability" %}

**행 속성** 패널에서 인앱 메시지 또는 랜딩 페이지에 [배경 행 이미지를 추가할]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/style_settings/#background-image) 수 있습니다. **배경 이미지를** 토글한 다음 이미지 URL을 입력하거나 [미디어 라이브러리에서]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/media_library/) 이미지를 선택합니다. 마지막으로 대체 텍스트, 크기, 위치, 이미지 반복 여부를 구성하여 행 전체에 패턴을 만들 수 있습니다.

![가로 반복 패턴이 있는 피자의 행 배경 이미지입니다.]({% image_buster /assets/img_archive/background_row.png %})

#### 미리보기 링크 복사

[배너]({{site.baseurl}}/user_guide/message_building_by_channel/banners/create/#step-5-test-your-message-optional), [이메일 커스텀 푸터]({{site.baseurl}}/user_guide/message_building_by_channel/email/custom_email_footer/#creating-your-custom-footer), [이메일 옵트인 및 탈퇴 페이지에서]({{site.baseurl}}/user_guide/administrative/app_settings/email_settings/?tab=custom%20footer#subscription-pages-and-footers) **미리보기 링크 복사를** 사용하여 콘텐츠가 임의의 사용자에게 어떻게 보이는지 보여주는 공유 가능한 링크를 생성할 수 있습니다.

#### 최적화된 전달이 가능한 WhatsApp 메시지

Meta의 진행된 AI 시스템을 사용하여 참여 가능성이 가장 높은 더 많은 사용자에게 마케팅 메시지를 전달하여 전달 가능성과 메시지 참여도를 크게 높일 수 있습니다.

[전달이 최적화된 WhatsApp 메시지는]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/optimized_delivery/) 기존 클라우드 API에 비해 뛰어난 성능을 제공하는 Meta의 새로운 [마케팅 메시지 라이트 API를](https://developers.facebook.com/docs/whatsapp/marketing-messages-lite-api/) 사용하여 전송됩니다. 이 새로운 전송 파이프라인을 사용하면 메시지를 소중히 여기고 수신하고자 하는 사용자에게 더 효과적으로 도달할 수 있습니다.

#### WhatsApp Flows

WhatsApp Flow 메시지를 Braze 캔버스 또는 캠페인에 통합할 때, 사용자가 Flow를 통해 제출하는 특정 정보를 캡처하여 활용하고 싶을 수 있습니다. Braze는 필요한 중첩 고객 속성(NCA) 스키마를 생성하기 위해 사용자 응답의 구조, 특히 JSON 응답의 예상 형태에 관한 추가 정보를 수신해야 합니다.

이제 [Flow 응답을 커스텀 속성으로 저장하고]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/whatsapp_flows/?tab=recommended%20method#step-1-generate-the-flow-custom-attribute) 테스트 전송을 완료하여 응답 구조에 대한 정보를 Braze에 제공할 수 있습니다.

#### 편집 가능한 사용자 미리보기

[무작위 또는 기존 사용자의 개별 필드를 편집하여]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/sending_test_messages/?tab=webhook#customizing-an-existing-user) 메시지 내의 동적 콘텐츠를 테스트할 수 있습니다. **편집을** 선택하여 선택한 사용자를 수정할 수 있는 커스텀 사용자로 전환합니다.

!['편집' 버튼이 있는 '사용자로 미리보기' 탭입니다.]({% image_buster /assets/img_archive/edit_user_preview.png %}){: style="max-width:50%;"}

### AI 및 ML 자동화

#### BrazeAI 의사 결정 스튜디오™ Go

이제 다음 구성 문서를 참조하여 [BrazeAI Decisioning Studio™ Go와의]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/go) 통합을 설정할 수 있습니다:

- [Braze]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/go/configuring_braze)
- [클라비요]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/go/configuring_klaviyo)
- [Salesforce 마케팅 클라우드]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/go/configuring_sfmc)

#### Braze 에이전트를 위한 새로운 기능

{% multi_lang_include release_type.md release="Beta" %}

이제 [Braze 에이전트를]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents) 다음과 같이 커스텀할 수 있습니다:

- 상담원이 응답할 때 준수해야 할 [브랜드 가이드라인을]({{site.baseurl}}/user_guide/administrative/app_settings/brand_guidelines) 적용합니다. 
- 카탈로그를 참조하여 메시지를 더욱 개인화할 수 있습니다.
- [출력 형식을]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents/#output-format) 제공하여 상담원의 출력을 구조화합니다.
- 상담원의 출력에 대한 편차 수준에 맞게 [온도를]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents/#temperature) 조정합니다.

### <sup>BrazeAITM</sup> 오퍼레이터를 사용한 ChatGPT 모델

{% multi_lang_include release_type.md release="Beta" %}

이러한 GPT 모델 중에서 선택하여 [오퍼레이터의]({{site.baseurl}}/user_guide/brazeai/operator) 다양한 요청 유형에 사용할 수 있습니다:

- GPT-5.2 Nano
- GPT-5 미니(기본값)
- GPT-5

### 새로운 Braze 파트너십

#### StackAdapt - 광고

[스택어댑터는]({{site.baseurl}}/partners/stackadapt/) 성과 중심의 타겟팅 광고를 제공하는 AI 기반 마케팅 플랫폼입니다. 이를 통해 Braze의 사용자 프로필 데이터를 StackAdapt 데이터 허브에 동기화할 수 있습니다. 두 플랫폼을 연결하면 고객에 대한 통합된 뷰를 생성하고 퍼스트파티 데이터를 활성화하여 광고 성과를 개선할 수 있습니다.

#### Cloudinary - 동적 콘텐츠

[Cloudinary는]({{site.baseurl}}/partners/cloudinary/) 이미지 및 비디오 플랫폼으로, 채널과 고객 여정에 걸쳐 모든 캠페인에 이미지와 비디오를 대규모로 관리, 편집, 최적화 및 전달할 수 있도록 지원합니다. 통합 및 인에이블먼트가 완료되면 Cloudinary의 미디어 매니저가 Braze 캠페인과 캔버스에 동적, 상황별, 개인화된 자산을 전달할 수 있습니다.

#### 카멜레온 - A/B 테스트

[Kameleoon은]({{site.baseurl}}/partners/kameleoon/) 하나의 통합 플랫폼에서 실험, AI 기반 개인화 및 기능 관리 기능을 갖춘 최적화 솔루션입니다.

### SDK 업데이트

다음 SDK 업데이트가 릴리스되었습니다. 주요 업데이트는 아래에 나열되어 있으며, 그 외의 모든 업데이트는 해당 SDK 체인지로그를 확인하면 확인할 수 있습니다.

- [React Native SDK 15.0.0](https://github.com/braze-inc/braze-react-native-sdk/blob/16.1.0/CHANGELOG.md)
    - `subscribeToInAppMessage` 및 `addListener` 의 콜백에 대한 타입스크립트 유형을 `Braze.Events.IN_APP_MESSAGE_RECEIVED` 로 수정했습니다.
        - 이제 이러한 리스너는 새로운 `InAppMessageEvent` 유형의 콜백을 올바르게 반환합니다. 이전에는 메서드에 `BrazeInAppMessage` 유형을 반환하도록 주석이 달렸지만 실제로는 `String` 유형을 반환했습니다.
         - 두 가지 구독 API 중 하나를 사용하는 경우 이 버전으로 업데이트한 후 인앱 메시징의 동작이 변경되지 않았는지 확인하세요. `BrazeProject.tsx` 에서 샘플 코드를 확인하세요.
    - 이제 API `logInAppMessageClicked`, `logInAppMessageImpression`, `logInAppMessageButtonClicked` 는 기존 공개 인터페이스와 일치하도록 `BrazeInAppMessage` 객체만 허용합니다.
        - 이전에는 `BrazeInAppMessage` 객체와 `String` 객체를 모두 허용했습니다.
    - `BrazeInAppMessage.toString()` 이제 JSON 문자열 표현 대신 사람이 읽을 수 있는 문자열을 반환합니다.
        - 인앱 메시지의 JSON 문자열 표현을 얻으려면 `BrazeInAppMessage.inAppMessageJsonString` 을 사용합니다.
    - iOS에서는 `[[BrazeReactUtils sharedInstance] formatPushPayload:withLaunchOptions:]` 이 `[BrazeReactDataTranslator formatPushPayload:withLaunchOptions:]` 으로 이전되었습니다.
        - 이 새로운 메서드는 이제 인스턴스 메서드가 아닌 클래스 메서드입니다.
    - `BrazeReactUtils` 메서드에 무효성 어노테이션을 추가합니다.
    - API에서 더 이상 사용되지 않는 다음 메서드와 프로퍼티를 제거합니다:
        - `getInstallTrackingId(callback:)` 에 찬성 `getDeviceId`.
        - `registerAndroidPushToken(token:)` 에 찬성 `registerPushToken`.
        - `setGoogleAdvertisingId(googleAdvertisingId:adTrackingEnabled:)` 에 찬성 `setAdTrackingEnabled`.
        - `PushNotificationEvent.push_event_type` 에 찬성 `payload_type`.
        - `PushNotificationEvent.deeplink` 에 찬성 `url`.
        - `PushNotificationEvent.content_text` 에 찬성 `body`.
        - `PushNotificationEvent.raw_android_push_data` 에 찬성 `android`.
        - `PushNotificationEvent.kvp_data` 에 찬성 `braze_properties`.
    - 기본 Android 소프트웨어 개발 키트 버전 바인딩을 [Braze Android SDK 39.0.0에서 40.0.2로](https://github.com/braze-inc/braze-android-sdk/compare/v39.0.0...v40.0.2#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed) 업데이트합니다.
- [NET MAUI(Xamarin) 소프트웨어 개발 키트 버전 8.0.0](https://github.com/braze-inc/braze-xamarin-sdk/blob/master/CHANGELOG.md)
    - [브레이즈 스위프트 SDK 9.0.0에서 10.0.0으로](https://github.com/braze-inc/braze-swift-sdk/compare/12.1.0...13.3.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed) iOS 바인딩을 업데이트했습니다. 여기에는 Xcode 26 지원이 포함됩니다.
- [Flutter SDK 14.0.0 5.9.0](https://pub.dev/packages/braze_plugin/changelog)
    - Braze Android SDK 35.0.0에서 36.0.0으로 네이티브 Android 브리지를 업데이트합니다.
- [Braze Swift SDK 12.0.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md)
- [Web SDK 5.9.0](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md)
- [안드로이드 SDK 36.0.0](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md)

{% enddetails %}

{% details October 14, 2025 %}

## 2024년 10월 15일 출시

### BrazeAI Decisioning Studio™

[BrazeAI Decisioning Studio™는](https://www.braze.com/product/brazeai-decisioning-studio/) A/B 테스트를 모든 것을 개인화하는 AI 의사 결정으로 대체하고 모든 측정기준을 극대화합니다: 클릭이 아니라 매출을 창출합니다. BrazeAI Decisioning Studio™를 사용하면 모든 비즈니스 KPI를 최적화할 수 있습니다. 샘플 사용 사례와 주요 기능은 전용 섹션 [BrazeAI Decisioning Studio™를]({{site.baseurl}}/user_guide/brazeai/decisioning_studio) 참조하세요.

### 데이터 유연성

#### 신규 커런츠 이벤트

[커런츠 용어집에]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events) 새로운 이벤트가 추가되었습니다:

- `users.messages.rcs.Click`
- `users.messages.rcs.Rejection`
- `users.messages.line.Abort`
- `users.messages.line.Send`
- `users.messages.line.InboundReceive`
- `users.messages.line.Click`
- `users.messages.rcs.Delivery`
- `users.messages.rcs.InboundReceive`
- `users.messages.rcs.Read`
- `users.messages.rcs.Send`
- `users.messages.rcs.Abort`
- `users.messages.inappmessage.Abort`

이러한 새로운 필드는 다음 커런츠 이벤트에 추가되었습니다:

- `is_sms_fallback` 
  - `users.messages.sms.Delivery`
  - `users.messages.sms.DeliveryFailure`
  - `users.messages.sms.Rejection`
- `message_id` 
  - `users.messages.whatsapp.InboundReceive`
- `message_id` 
  - `users.messages.whatsapp.Send`
  - `users.messages.whatsapp.Delivery`
  - `users.messages.whatsapp.Failure`
  - `users.messages.whatsapp.Read`

#### 억제 목록

{% multi_lang_include release_type.md release="General availability" %}

수신 [금지 목록은]({{site.baseurl}}/user_guide/engagement_tools/segments/suppression_lists) 캠페인이나 캔버스를 자동으로 받지 않는 사용자 그룹입니다. 금지 목록은 세그먼트 필터로 정의되며, 사용자는 필터 기준을 충족할 때 금지 목록에 들어가고 나갈 수 있습니다.

#### 제로 카피 개인화

{% multi_lang_include release_type.md release="Early access" %}

동기화 캔버스 트리거는 클라우드 데이터 수집을 사용하여 [복사본 없는 개인화를]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/zero_copy_sync/) 지원합니다. 이 기능은 데이터 스토리지 솔루션에서 사용자별 정보에 액세스하여 대상 캔버스로 전달합니다. 캔버스 단계에는 선택적으로 Braze 사용자 프로필에 유지되지 않는 개인화 필드를 포함할 수 있습니다.

#### 오디언스 경로 및 결정 분할 단계에 대한 캔버스 컨텍스트 변수

{% multi_lang_include release_type.md release="Early access" %}

[오디언스 경로]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/audience_paths) 및 [결정 분할]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/decision_split) 단계에서 이전에 선언한 컨텍스트 변수를 사용하는 [컨텍스트 변수 필터를 만들]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/context_variables/#context-variable-filters) 수 있습니다.

### 창의력 발휘

#### 이메일용 거래 카드

[딜 카드를]({{site.baseurl}}/user_guide/message_building_by_channel/email/html_editor/gmail_promotions_tab) 사용하여 이메일 본문 상단에 주요 딜 정보를 바로 제공할 수 있습니다. 이를 통해 수신자는 오퍼 세부 정보를 빠르게 파악하고 조치를 취할 수 있습니다.

#### 배너용 템플릿

이제 [배너를 작성할]({{site.baseurl}}/user_guide/message_building_by_channel/banners/create) 때 빈 템플릿으로 시작하거나 Braze 템플릿을 사용하거나 저장된 배너 템플릿을 선택할 수 있습니다.

### 강력한 채널

#### 억제 목록

{% multi_lang_include release_type.md release="General availability" %}
 
[억제 목록]({{site.baseurl}}/user_guide/engagement_tools/segments/suppression_lists/)은 메시지를 절대 받지 않을 사용자 그룹을 지정합니다. 관리자는 세분화와 동일한 방식으로 사용자 그룹을 좁히기 위해 세그먼트 필터로 억제 목록을 생성할 수 있습니다.

#### LINE 클릭 추적

{% multi_lang_include release_type.md release="General availability" %}

[LINE 클릭 추적을]({{site.baseurl}}/line/click_tracking/) 켜면 Braze는 자동으로 URL을 단축하고 추적 메커니즘을 추가하며 클릭 수를 실시간으로 기록합니다. LINE은 총체적인 클릭 데이터를 제공하는 반면, Braze는 시의적절하고 실행 가능한 세분화된 사용자 정보를 제공합니다. 이 데이터를 통해 클릭 행동에 따라 사용자를 세분화하고 특정 클릭에 대한 반응으로 메시지를 트리거하는 등 보다 타겟화된 세분화 및 리타겟팅 전략을 수립할 수 있습니다.

#### SMS 및 RCS 봇 클릭 필터링

{% multi_lang_include release_type.md release="General availability" %}

[SMS 및 RCS 봇 클릭 필터링은]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/bot_click_filtering/) 의심스러운 봇 클릭을 제외하여 캠페인 분석 및 워크플로우를 개선합니다. "봇 클릭"이란 웹 크롤러, Android 및 iOS 링크 미리보기 또는 CPaaS 보안 소프트웨어와 같은 SMS 및 RCS 메시징의 단축 링크에 대한 자동화된 클릭을 의미합니다. 이 기능은 정확한 보고, 세분화 및 오케스트레이션을 통해 실제 사용자의 참여를 유도할 수 있습니다.

#### WhatsApp 전화번호 전송

[한 워크스페이스에서 다른 워크스페이스로]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/transfer_between_workspaces/) WhatsApp 비즈니스 계정(WABA) 전화번호 및 관련 구독 그룹을 이전하세요.

#### WhatsApp 플로우 응답 메시지 및 미리보기

캔버스에서 [응답 메시지와]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/whatsapp_flows/?tab=response%20message#configuring-whatsapp-flow-messages-and-responses) 플로우 메시지를 사용하는 WhatsApp 메시지 단계를 만들 수 있습니다. 또한 **흐름 미리** 보기를 선택하여 Braze에서 바로 흐름을 미리 보고 예상대로 작동하는지 확인할 수 있습니다.

#### WhatsApp 제품 메시지

제품 메시지는 Meta 카탈로그에서 직접 제품을 보여주는 대화형 WhatsApp 메시지를 보낼 수 있도록 합니다.

#### 외부 시스템과 Braze 및 WhatsApp 통합하기

WhatsApp 채널에서 [AI 챗봇과 실시간 상담원 핸드오프의 강력한 기능을 활용하여]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_use_cases/external_system/) 고객 지원 운영을 간소화하세요. 일상적인 문의를 자동화하고 필요 시 상담원에게 원활하게 전환함으로써 응답 시간을 크게 개선하고 전반적인 고객 경험을 향상시킬 수 있습니다.

### AI 및 ML 자동화

#### Braze 에이전트

{% multi_lang_include release_type.md release="Beta" %}

[Braze 에이전트는]({{site.baseurl}}/user_guide/brazeai/agents/) Braze 내에서 생성할 수 있는 AI 기반 도우미입니다. 상담원은 콘텐츠를 생성하고, 지능적인 의사 결정을 내리고, 데이터를 보강하여 더욱 개인화된 고객 경험을 제공할 수 있습니다.

### 새로운 Braze 파트너십

#### 재스퍼 - 템플릿

[Jasper와]({{site.baseurl}}/partners/jasper/) Braze의 통합을 통해 콘텐츠 제작과 캠페인 실행을 간소화할 수 있습니다. Jasper를 사용하면 마케팅 팀은 몇 분 안에 고품질의 브랜드 카피를 생성할 수 있습니다. 그런 다음 Braze는 이러한 메시지를 최적의 타이밍에 적절한 오디언스에게 전달할 수 있도록 지원합니다. 이러한 통합은 원활한 워크플로우를 촉진하고 수작업을 줄이며 더 강력한 참여 성과를 이끌어냅니다.

#### Swym - 로열티 및 리타겟팅

[Swym은]({{site.baseurl}}/partners/swym/) 이커머스 브랜드가 위시리스트, 나중에 저장, 선물 등록 및 재고 부족 알림을 통해 쇼핑 의도를 파악할 수 있도록 지원합니다. 풍부한 권한 기반 데이터를 사용하여 하이퍼 타겟팅 캠페인을 제작하고 개인화된 쇼핑 경험을 제공하여 참여를 유도하고 전환율을 높이며 로열티를 높일 수 있습니다.

### SDK 업데이트

다음 SDK 업데이트가 릴리스되었습니다. 주요 업데이트는 아래에 나열되어 있으며, 다른 모든 업데이트는 해당 소프트웨어 개발 키트 체인지로그를 확인하면 확인할 수 있습니다.

- [Cordova SDK 12.0.0](https://github.com/braze-inc/braze-cordova-sdk/blob/master/CHANGELOG.md)
    - 네이티브 Android 브리지를 [Braze Android SDK 35.0.0에서 36.0.0으로 업데이트했습니다.](https://github.com/braze-inc/braze-android-sdk/compare/v37.0.0...v39.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed)
        - 이제 필요한 최소 GradlePluginKotlinVersion은 2.1.0입니다.
    - 네이티브 iOS 브리지를 [Braze Swift SDK 11.6.1에서 12.0.0으로 업데이트했습니다.](https://github.com/braze-inc/braze-swift-sdk/compare/12.0.0...13.2.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed) 여기에는 Xcode 26 지원이 포함됩니다.
    - 뉴스피드에 대한 지원을 제거합니다. 다음 API가 제거되었습니다:
        - `launchNewsFeed`
        - `getNewsFeed`
        - `getNewsFeedUnreadCount`
        - `getNewsFeedCardCount`
        - `getCardCountForCategories`
        - `getUnreadCardCountForCategories`
- [React Native SDK 15.0.0](https://www.npmjs.com/package/@braze/react-native-sdk/v/17.0.1)
    - 기본 Android 소프트웨어 개발 키트 버전 바인딩을 [Braze Android SDK 37.0.0에서 39.0.0으로](https://github.com/braze-inc/braze-android-sdk/compare/v37.0.0...v39.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed) 업데이트합니다.
    - 뉴스피드에 대한 지원을 제거합니다. 다음 API가 제거되었습니다:
        - `launchNewsFeed`
        - `requestFeedRefresh`
        - `getNewsFeedCards`
        - `logNewsFeedCardClicked`
        - `logNewsFeedCardImpression`
        - `getCardCountForCategories`
        - `getUnreadCardCountForCategories`
        - `Braze.Events.NEWS_FEED_CARDS_UPDATED`
        - `Braze.CardCategory`
- [Web SDK 5.9.0](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md)
- [Flutter SDK 14.0.0 5.9.0](https://pub.dev/packages/braze_plugin/changelog)
- [Unity SDK 3.11.0](https://github.com/braze-inc/braze-unity-sdk/blob/master/CHANGELOG.md)
    - 네이티브 iOS 브리지를 [Braze Swift SDK 11.6.1에서 12.0.0으로 업데이트했습니다.](https://github.com/braze-inc/braze-swift-sdk/compare/12.0.0...13.2.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed) 여기에는 Xcode 26 지원이 포함됩니다.

{% enddetails %}
{% details September 16, 2025 %}

## 2024년 9월 17일 출시

### 데이터 유연성

#### Braze 데이터 플랫폼

고객 데이터 플랫폼은 고객 생애주기 전반에 걸쳐 개인화되고 영향력 있는 경험을 제공할 수 있도록 지원하는 포괄적이고 구성 가능한 데이터 기능 및 파트너 통합의 집합입니다. 데이터와 관련된 세 가지 작업에 대해 자세히 알아보세요: 

- [데이터 통합]({{site.baseurl}}/user_guide/data/unification):
- []({{site.baseurl}}/user_guide/data/activation)데이터 활성화
- [데이터 배포]({{site.baseurl}}/user_guide/data/distribution):

#### 커스텀 배너 속성

{% multi_lang_include release_type.md release="Early access" %}

배너 캠페인의 커스텀 속성을 사용하여 소프트웨어 개발 키트를 통해 키값 데이터를 검색하고 앱의 행동이나 모양을 수정할 수 있습니다. 자세히 알아보려면 [커스텀 배너 속성을]({{site.baseurl}}/developer_guide/banners/placements/#custom-properties) 참조하세요.

#### 토큰 인증

{% multi_lang_include release_type.md release="General availability" %}

Braze 연결된 콘텐츠를 사용할 때 특정 API에 사용자 아이디와 비밀번호 대신 토큰이 필요할 수 있습니다. Braze는 [토큰 인증 헤더 값을]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/making_an_api_call#using-token-authentication) 포함하는 자격 증명을 저장할 수 있습니다.

#### 프로모션 코드

사용자 업데이트 단계를 통해 프로모션 코드를 사용자 프로필에 저장할 수 있습니다. 자세한 내용은 [고객 프로필에 프로모션 코드 저장을]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/promotion_codes#save-to-profile) 참조하세요.

### 창의력 발휘

#### Braze 파일럿

[Braze 파일럿은]({{site.baseurl}}/user_guide/getting_started/braze_pilot) 공개적으로 사용 가능한 Android 및 iOS용 앱으로, Braze 대시보드에서 휴대폰으로 메시지를 실행할 수 있습니다. 앱 다운로드, Braze 대시보드 연결 초기화, 설정 완료에 대한 안내는 [Braze 파일럿 시작하기를]({{site.baseurl}}/user_guide/getting_started/braze_pilot/getting_started) 참조하세요.

### 새로운 Braze 파트너십

#### 블링 - 시각적 및 인터랙티브 콘텐츠

[Blings는]({{site.baseurl}}/partners/blings/) 차세대 개인화된 비디오 플랫폼으로, 채널 전반에 걸쳐 실시간 데이터 중심의 인터랙티브 비디오 경험을 대규모로 제공할 수 있도록 지원합니다.

#### 타사 도구와 Shopify 표준 통합

Shopify 온라인 스토어의 경우 Braze의 표준 통합 방법을 사용하여 사이트에서 Braze SDK를 지원하는 것이 좋습니다.

하지만 Google 태그 매니저와 같은 타사 도구를 사용하는 것을 선호하실 수도 있으므로 그 방법에 대한 가이드를 준비했습니다. 시작하려면 [Shopify를 참조하세요: 타사 태그]({{site.baseurl}}/shopify_standard_integration_third_party_tagging/).

### SDK 업데이트

다음 SDK 업데이트가 릴리스되었습니다. 주요 업데이트는 아래에 나열되어 있으며, 그 외의 모든 업데이트는 해당 SDK 체인지로그를 확인하면 확인할 수 있습니다.

- [Braze Flutter 소프트웨어 개발 키트 15.0.0](https://github.com/braze-inc/braze-flutter-sdk/blob/main/CHANGELOG.md#1500)
    - Braze 소프트웨어 개발 키트 `36.0.0` 에서 `39.0.0` 으로 네이티브 Android 브릿지를 업데이트합니다.
    - 기본 iOS 브릿지를 Braze Swift 소프트웨어 개발 키트 `12.0.0` 에서 `13.2.0` 으로 업데이트합니다. 여기에는 Xcode 26 지원이 포함됩니다.

- [Braze Swift SDK 12.0.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#1300)
  - 브레이즈 스위프트 SDK 바인딩을 업데이트하여 `13.0.0+` SemVer 디노미네이션의 릴리스가 필요하도록 합니다. 이를 통해 `13.0.0` 에서 `14.0.0` 까지의 모든 버전의 Braze SDK와 호환이 가능합니다.

{% enddetails %}
{% details August 19, 2025 %}

## 2024년 8월 20일 출시

### 캔버스 컨텍스트에 대한 시간대 일관성 표준화

{% multi_lang_include release_type.md release="Early access" %}

[캔버스 컨텍스트 단계 얼리 액세스에]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context) 참여하는 경우, 동작 기반 캔버스의 트리거 이벤트 속성정보에서 날짜/시간 유형이 있는 모든 타임스탬프는 항상 [UTC로](https://en.wikipedia.org/wiki/Coordinated_Universal_Time) 정규화됩니다. 이에 대한 자세한 내용은 [시간대 일관성 표준화를]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context#time-zone-consistency-standardization) 참조하세요.

### 데이터 유연성

#### 셀프 서비스 커스텀 도메인

{% multi_lang_include release_type.md release="General access" %}

[셀프 서비스 커스텀 도메]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/link_shortening/custom_domains/) 인을 사용하면 Braze 대시보드에서 직접 SMS, RCS, WhatsApp에 대한 커스텀 도메인을 구성하고 관리할 수 있습니다. 최대 10개의 커스텀 도메인을 한 곳에서 쉽게 추가, 모니터링, 관리할 수 있습니다.

#### 세그먼트 퍼널 통계

[퍼널 통계 보기를]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/#viewing-funnel-statistics) 선택하여 해당 필터 그룹에 대한 통계를 표시하고 추가된 각 필터가 세그먼트 통계에 어떤 영향을 미치는지 확인합니다. 해당 시점까지 모든 필터에 의해 타겟팅된 사용자의 예상 수와 백분율을 확인할 수 있습니다. 필터 그룹에 대한 통계가 표시되면 필터를 변경할 때마다 통계가 자동으로 업데이트됩니다. 

#### 푸시 알림을 위한 `/campaigns/details` 엔드포인트에 대한 새로운 응답 필드 추가

이제 푸시 알림에 대한 `messages` 응답에 두 개의 새로운 필드가 포함됩니다:

- `image_url` Android 알림 이미지, iOS 알림 이미지 또는 웹 푸시 아이콘 이미지의 이미지 URL입니다.
- `large_image_url` Android Chrome 및 Windows 웹 푸시 작업을 위한 웹 알림 이미지 URL입니다.

#### PII 필드 정의하기

[특정 필드를 PII 필드로]({{site.baseurl}}/user_guide/administrative/app_settings/company_settings/security_settings#view-pii) 선택하고 [정의하는]({{site.baseurl}}/user_guide/administrative/app_settings/company_settings/security_settings#view-pii) 것은 사용자가 Braze 대시보드에서 볼 수 있는 항목에만 영향을 미치며, 해당 PII 필드의 최종 사용자 데이터가 처리되는 방식에는 영향을 미치지 않습니다.

법무팀에 문의하여 대시보드의 설정을 [데이터 보존과]({{site.baseurl}}/api/data_retention/) 관련된 규정을 포함하여 회사에 적용되는 모든 개인정보 보호 규정 및 정책에 맞게 조정하세요.

#### 보고서 빌더 다운로드 링크 공유하기

**공유를** 선택한 다음 **링크 공유를** 선택하거나 **이메일을 보내거나 예약하여** 보고서에 대한 [대시보드 링크를 공유할]({{site.baseurl}}/user_guide/analytics/reporting/report_builder/#sharing-a-report) 수 있습니다.

### 창의력 발휘

#### 드래그 앤 드롭 이메일을 위한 커스텀 헤드 태그

`<head>` 태그를 사용하여 이메일 메시징에 CSS 및 메타데이터를 추가하세요. 예를 들어 이러한 태그를 사용하여 스타일시트 또는 파비콘을 추가할 수 있습니다. Liquid는 `<head>` 태그에서 지원됩니다.

### 강력한 채널

#### 퍼지 아웃 아웃 모범 사례

모호한 옵트아웃 메시지를 신중하게 구성하고 가입자에게 명확하고 규정을 준수하며 긍정적인 경험을 제공하는 데 도움이 되는 [모범 사례 섹션을]({{site.baseurl}}) 추가했습니다.

#### WhatsApp Flows

{% multi_lang_include release_type.md release="Early access" %}

[WhatsApp 플로우는]({{site.baseurl}}/whatsapp_flows/) 기존 WhatsApp 채널을 개선한 기능으로, 대화형 및 동적 메시징 경험을 만들 수 있습니다. 

#### WhatsApp 인바운드 제품 관련 질문

사용자는 [제품]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/product_messages/#receiving-inbound-product-questions) 또는 카탈로그 메시지에 [제품 관련 질문으로]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/product_messages/#receiving-inbound-product-questions) 응답할 수 있습니다. 이러한 메시지는 인바운드 메시지로 도착하며, 행동 경로를 사용하여 정렬할 수 있습니다.

또한 Braze는 이러한 질문에서 제품 ID와 카탈로그 ID를 추출하므로 응답을 자동화하거나 다른 팀(예: 고객 지원팀)에 질문을 보내려는 경우 이러한 세부 정보를 포함할 수 있습니다.

### AI 및 ML 자동화

#### 새로운 BrazeAI™ 사용 사례 문서

BrazeAI™를 최대한 활용할 수 있도록 새로운 사용 사례 문서를 추가했습니다. 이 가이드는 다음을 포함하여 참여 전략에 AI를 적용할 수 있는 실용적인 방법을 강조합니다:

- 예측 이탈 고객이탈 위험이 있는 고객을 식별하고 조기에 조치를 취하세요.
- 예측 이벤트 주요 사용자 행동을 예측하고 실시간으로 경험을 형성하세요.
- [Recommendations]({{site.baseurl}}/user_guide/brazeai/recommendations/use_case ): 고객 행동에 따라 더욱 관련성 높은 콘텐츠와 제품을 전달하세요.

#### MCP 서버

{% multi_lang_include release_type.md release="Beta" %}

안전한 읽기 전용 연결인 [Braze MCP 서버를]({{site.baseurl}}/user_guide/brazeai/mcp_server/) 통해 Claude 및 Cursor와 같은 AI 도구는 데이터를 변경하지 않고 질문에 답하고, 트렌드를 분석하고, 인사이트를 제공하기 위해 비PII Braze 데이터에 액세스할 수 있습니다.

### SDK 업데이트

다음 SDK 업데이트가 릴리스되었습니다. 주요 업데이트는 아래에 나열되어 있으며, 그 외의 모든 업데이트는 해당 SDK 체인지로그를 확인하면 확인할 수 있습니다.

- [Swift SDK 11.0.1](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md)
    - '선택적' 인증 오류에 대해 트리거되도록 `BrazeSDKAuthDelegate.braze(_:sdkAuthenticationFailedWithError:)` 의 기능을 확장합니다.
        - 이제 '필수' 및 '선택' 인증 오류 모두에 대해 델리게이트 메서드 `BrazeSDKAuthDelegate.braze(_:sdkAuthenticationFailedWithError:)` 가 트리거됩니다.
        - "필수" 소프트웨어 개발 키트 인증 오류만 처리하려면 이 델리게이트 메서드 구현 내에서 `BrazeSDKAuthError.optional` 가 거짓인지 확인하는 검사를 추가하세요.
    - `Braze.Configuration.sdkAuthentication` 사용법을 인에이블먼트 시 적용되도록 수정했습니다.
        - 이전에는 이 구성의 값이 소프트웨어 개발 키트에서 소비되지 않았으며 토큰이 있는 경우 항상 요청에 토큰이 첨부되었습니다.
        - 이제 소프트웨어 개발 키트는 이 구성이 인에이블먼트된 경우에만 발신 네트워크 요청에 SDK 인증 토큰을 첨부합니다.
    - `Braze.FeatureFlag` 의 모든 속성 및 `Braze.Banner` 의 모든 속성에 대한 설정자는 `private` 으로 변경되었습니다. 이제 이러한 클래스의 프로퍼티는 읽기 전용입니다.
    - 버전 `11.4.0` 에서 더 이상 사용되지 않는 `Braze.Banner.id` 속성을 제거합니다.
        - 대신 `Braze.Banner.trackingId` 을 사용하여 배너의 캠페인 추적 ID를 확인합니다.
- [React Native SDK 15.0.0](https://github.com/braze-inc/braze-react-native-sdk/blob/master/CHANGELOG.md)
    - 기본 Android 소프트웨어 개발 키트 버전 바인딩을 [Braze Android SDK 36.0.0](https://github.com/braze-inc/braze-android-sdk/compare/v36.0.0...v37.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed)에서 [37.0.0으로](https://github.com/braze-inc/braze-android-sdk/compare/v36.0.0...v37.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed) 업데이트합니다.
    - 기본 Swift SDK 버전 바인딩을 [Braze Swift SDK 12.0.0](https://github.com/braze-inc/braze-swift-sdk/compare/12.0.0...13.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed)에서 [13.0.0으로](https://github.com/braze-inc/braze-swift-sdk/compare/12.0.0...13.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed) 업데이트합니다.
        - 이제 `sdkAuthenticationError` 이벤트는 '필수' 및 '선택' 인증 오류 모두에 대해 트리거됩니다.
- [Xamarin SDK 1.26.0](https://github.com/braze-inc/braze-xamarin-sdk/blob/7.0.0/CHANGELOG.md)
    - iOS 및 Android 바인딩에 대한 .NET 9.0 지원이 추가되었습니다.
        - 이렇게 하면 .NET 7.0에 대한 지원이 제거됩니다.
        - [최소 iOS 12.2 버전이](https://learn.microsoft.com/en-us/dotnet/maui/whats-new/dotnet-9?view=net-maui-9.0) 필요합니다.
    - Android 바인딩을 [Braze Android 30.4.0에서 32.0.0으로](https://github.com/braze-inc/braze-android-sdk/compare/v32.0.0...v37.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed) 업데이트했습니다.
    - [브레이즈 스위프트 SDK 9.0.0에서 10.0.0으로](https://github.com/braze-inc/braze-swift-sdk/compare/10.0.0...12.1.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed) iOS 바인딩을 업데이트했습니다.
    - 이 릴리스에는 배너 기능에 대한 API가 포함되어 있지만 현재 이 소프트웨어 개발 키트에서 완전히 지원되지는 않습니다. .NET MAUI 앱에서 배너를 사용하려면 애플리케이션에 통합하기 전에 고객 지원 매니저에게 문의하세요.
- [Cordova SDK 12.0.0](https://github.com/braze-inc/braze-cordova-sdk/blob/master/CHANGELOG.md#1300)
    - Swift 소프트웨어 개발 키트에서 더 이상 사용되지 않는 `_requestEnableSDKOnNextAppRun` 대신 `setEnabled`: 을 사용하도록 `enableSdk` 메서드의 내부 iOS 구현을 업데이트했습니다.
    - 이 메서드를 호출하면 더 이상 앱을 다시 실행할 필요가 없습니다. 이제 이 메서드를 실행하는 즉시 소프트웨어 개발 키트가 인에이블먼트됩니다.
    - [Braze 소프트웨어 개발 키트 `36.0.0` 에서 `37.0.0`](https://github.com/braze-inc/braze-android-sdk/compare/v36.0.0...v37.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed) 으로 네이티브 Android 브릿지를 업데이트했습니다.

{% enddetails %}
{% details July 22, 2025 %}

## 2024년 7월 23일 출시

### Amazon S3로 보안 이벤트 내보내기

매일 자정 UTC에 실행되는 작업으로 Amazon S3라는 클라우드 스토리지 제공업체에 보안 이벤트를 자동으로 내보낼 수 있습니다. 설정이 완료되면 대시보드에서 보안 이벤트를 수동으로 내보낼 필요가 없습니다.

### 데이터 유연성

#### CSV import

{% multi_lang_include release_type.md release="General availability" %}

CSV 가져오기를 사용하여 `first_name`, `last_destination_searched`, `trip_booked` 과 같은 Braze에서 고객 속성 및 커스텀 이벤트를 기록하고 업데이트할 수 있습니다. To get started, see [CSV Import]({{site.baseurl}}/user_guide/data/user_data_collection/user_import/csv_import).

#### API 사용량 경고

{% multi_lang_include release_type.md release="General availability" %}

API 사용량 알림은 API 사용량에 대한 중요한 가시성을 제공하여 예기치 않은 트래픽을 사전에 감지할 수 있게 해줍니다. 이러한 알림을 설정하여 주요 API 요청량을 추적하면 실시간 알림을 받고 마케팅 캠페인에 영향을 미치기 전에 문제를 해결할 수 있습니다.

#### 워크스페이스 API 속도 제한

작업 공간 API 속도 제한을 사용하면 작업 공간에서 특정 수집 엔드포인트(예: `/users/track` 또는 SDK 데이터)로 보낼 수 있는 API 요청의 최대 수를 설정할 수 있습니다. 또한 작업 공간 그룹에 속도 제한을 적용하여 해당 그룹의 모든 작업 공간에 제한이 공유되도록 할 수도 있습니다.

#### 신규 커런츠 이벤트

커런츠 용어집에 새로운 이벤트가 추가되었습니다:

- [Banner Abort events]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/#banner-abort-events)
- [Banner Click events]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/#banner-click-events)
- [Banner Impression events]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/#banner-impression-events)
- [배너 본 이벤트]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/#banner-viewed-events)
- [Webhook Failure events]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/#webhook-failure-events)

#### 캠페인 분석의 기본값 시간 범위

기본값은 다음과 같습니다. [**캠페인 분석**]({{site.baseurl}}/user_guide/analytics/reporting/campaign_analytics/) 의 시간 범위는 현재 시간으로부터 지난 90일을 표시합니다. 즉, 캠페인이 90일 이상 전에 시작된 경우 해당 기간 동안 분석 결과가 "0"으로 표시됩니다. 이전 캠페인에 대한 모든 분석을 보려면 보고 시간 범위를 조정하세요.

#### 캔버스 실험 경로 단계의 동작이 업데이트되었습니다.

If your Canvas has an active or in progress experiment and you update the active Canvas (even if it's not to the Experiment Path step), the in-progress experiment will end. To restart the experiment, you can disconnect the existing Experiment Path and launch a new one, or duplicate the Canvas and launch a new Canvas. 

For more information, refer to [Editing Canvases after launch]({{site.baseurl}}/post-launch_edits/).

#### `/users/export/ids` 엔드포인트에 더 빠른 속도 제한 사용 가능

또한 다음 요구 사항을 충족하여 [/users/export/ids 엔드포인트의]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/#rate-limit) 요청 [속도 제한을]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/#rate-limit) 초당 40건으로 늘릴 수도 있습니다:

- 워크스페이스에 기본값(분당 250건의 요청)의 속도 제한이 인에이블먼트되어 있습니다. 기존 요금 제한을 해제하는 데 대한 자세한 내용은 Braze 계정 매니저에게 문의하세요.
- 요청에 fields_to_export 매개변수를 포함하면 수신하려는 모든 필드를 나열할 수 있습니다.

#### 이메일 템플릿 엔드포인트를 위한 새로운 번역

{% multi_lang_include release_type.md release="Early access" %}

이러한 엔드포인트를 사용하여 이메일 템플릿의 번역 및 현지화를 확인하고 업데이트할 수 있습니다:

- [가져오기: 소스 번역 보기]({{site.baseurl}}/api/endpoints/translations/email_templates/get_view_source_template)
- [가져오기: 이메일 템플릿 엔드포인트의 특정 번역 및 로캘 보기
- [가져오기: 이메일 템플릿에 대한 모든 번역 및 로케일 보기
- [넣기: 이메일 템플릿에 대한 번역 업데이트

### 창의력 발휘

#### 랜딩 페이지

작은 화면에서 세로로 열을 쌓아 랜딩 페이지를 [사용자 기기의 크기에 맞게 반응하도록]({{site.baseurl}}/user_guide/engagement_tools/landing_pages/creating_pages#step-3-customize-the-page) 만들 수 있습니다. 이 기능을 인에이블하려면 반응형으로 만들려는 행에 열을 추가한 다음 **열 커스텀** 섹션에서 **작은 화면에서 세로 스택을** 토글합니다.

### 강력한 채널

#### 이메일에 대한 봇 필터링

{% multi_lang_include release_type.md release="General availability" %}

[이메일 환경설정에서]({{site.baseurl}}/user_guide/administrative/app_settings/email_settings) 봇 필터링을 설정하여 의심되는 모든 컴퓨터 또는 봇 클릭을 제외하세요. 이메일에서 '봇 클릭'이란 자동화된 프로그램에 의해 생성된 이메일 내의 하이퍼링크를 클릭하는 것을 말합니다. 이러한 봇 클릭을 필터링하여 참여 중인 수신자에게 의도적으로 메시지를 트리거하고 전달할 수 있습니다.

#### 드래그 앤 드롭 제품 블록

{% multi_lang_include release_type.md release="Early access" %}

드래그 앤 드롭 편집기를 사용하면 사용자 정의 Liquid 코드를 만들 필요 없이 메시지에 제품 블록을 신속하게 추가하고 구성하여 원활한 제품 쇼케이스를 만들 수 있습니다. 드래그 앤 드롭 제품 차단 기능은 현재 이메일에서만 사용할 수 있습니다.

#### 랜딩 페이지 및 인앱 메시지용 스팬 텍스트

스팬 텍스트를 사용하면 [랜딩 페이지와]({{site.baseurl}}/user_guide/engagement_tools/landing_pages/creating_pages/#step-3-customize-the-page) [인앱 메시지에]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/style_settings/#blocks) 사용자 지정 코드 없이도 텍스트 블록에 특정 스타일을 적용할 수 있습니다. 이렇게 하려면 **스타일을** 지정하려는 텍스트를 강조 표시한 다음 **스팬으로 줄 바꿈을** 선택하여 **스타일을** 지정합니다. 

#### WhatsApp으로 광고 클릭

[WhatsApp으로 클릭하는 광고는]({{site.baseurl}}/whatsapp_use_cases/) Facebook, Instagram 또는 기타 플랫폼의 메타 광고에서 신규 고객과 기존 고객을 모두 끌어올 수 있는 효율적인 방법입니다. 이러한 광고를 사용하여 제품 및 서비스를 홍보하는 동시에 사용자에게 WhatsApp의 존재를 알릴 수 있습니다. 

### 새로운 Braze 파트너십

#### Shopify 방문자 API - 전자상거래

Braze collects visitor information, such as email addresses and phone numbers, through in-browser messages. This information is then sent to Shopify. This data helps merchants recognize visitors to their store and create a more personalized shopping experience.

#### Okendo - 이커머스

Braze와 [Okendo의]({{site.baseurl}}/partners/okendo/) 통합은 리뷰, 로열티, 추천, 설문조사, 퀴즈 등 Okendo 플랫폼의 여러 제품에서 작동합니다. Okendo는 고객 이벤트 및 사용자 속성을 Braze에 전송하여 메시지를 개인화 및 트리거하는 데 사용할 수 있습니다.

#### Lemnisk - 고객 데이터 플랫폼

브랜드와 기업은 Braze와 [Lemnisk의]({{site.baseurl}}/partners/lemnisk/) 통합을 통해 여러 플랫폼에서 사용자 데이터를 실시간으로 통합하고 수집된 사용자 정보와 행동 데이터를 실시간으로 Braze로 전송하는 CDP 주도 인텔리전스 레이어 역할을 함으로써 Braze의 잠재력을 최대한 활용할 수 있습니다.

### SDK 업데이트

다음 SDK 업데이트가 릴리스되었습니다. 주요 업데이트는 아래에 나열되어 있으며, 그 외의 모든 업데이트는 해당 SDK 체인지로그를 확인하면 확인할 수 있습니다.

- [Web SDK 5.9.0](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md)
    - `Banner.html` 속성, `logBannerClick`, `logBannerImpressions` 메서드를 제거했습니다. 대신 [`insertBanner`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#insertbanner) 를 사용하면 노출 횟수 및 클릭 추적을 자동으로 처리합니다.
    - 기존 뉴스피드 기능에 대한 지원이 제거되었습니다. 여기에는 피드 클래스 및 관련 메서드의 제거가 포함됩니다.
    - 기존 뉴스피드 카드에서 사용되던 생성 및 카테고리 필드는 [`Card`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.card.html) 하위 클래스에서 제거되었습니다.
    - linkText 필드는 또한 [`ImageOnly`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.imageonly.html) Card 서브클래스와 그 생성자에서도 제거되었습니다.
    - 정의를 명확히 하고 특정 소프트웨어 개발 키트 메서드가 초기화되지 않은 경우 명시적으로 정의되지 않은 값을 반환하도록 유형을 업데이트하여 실제 런타임 동작과 유형이 일치하도록 했습니다. 이로 인해 이전의 (불완전한) 타이핑에 의존하는 프로젝트에 새로운 TypeScript 오류가 발생할 수 있습니다.
    - `CENTER_CROP` (기본값은 `FullScreenMessage` )의 `cropType` 인앱 메시지 이미지는 이제 접근성을 개선하기 위해 `<span>` 대신 `<img>` 태그를 통해 렌더링됩니다. 이렇게 하면 `.ab-center-cropped-img` 클래스 또는 그 하위 클래스에 대한 기존 CSS 커스텀이 손상될 수 있습니다.
- [Cordova SDK 12.0.0](https://github.com/braze-inc/braze-cordova-sdk/blob/master/CHANGELOG.md#1300)
    - Swift 소프트웨어 개발 키트에서 더 이상 사용되지 않는 `_requestEnableSDKOnNextAppRun` 대신 setEnabled: 를 사용하도록 `enableSdk` 메서드의 내부 iOS 구현을 업데이트했습니다.
        - 이 메서드를 호출하면 더 이상 앱을 다시 실행할 필요가 없습니다. 이제 이 메서드를 실행하는 즉시 소프트웨어 개발 키트가 인에이블먼트됩니다.
    - 네이티브 Android 브리지를 [Braze Android SDK 35.0.0에서 36.0.0으로 업데이트했습니다.](https://github.com/braze-inc/braze-android-sdk/compare/v36.0.0...v37.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed)
- [안드로이드 SDK 36.0.0](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md)
- [Swift SDK 11.0.1](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md)

{% enddetails %}
{% details June 24, 2025 %}

## 2025년 6월 24일 출시

### BrazeAI Decisioning Studio™

모든 것을 개인화하는 AI 의사결정으로 A/B 테스트를 대체하고 측정기준을 극대화하는 BrazeAI [Decisioning Studio](https://www.braze.com/product/brazeai-decisioning-studio/) ™를 사용하면 클릭이 아닌 매출을 극대화하여 모든 비즈니스 KPI를 최적화할 수 있습니다. 샘플 사용 사례와 주요 기능은 전용 섹션 [BrazeAI Decisioning Studio™를]({{site.baseurl}}/user_guide/brazeai/decisioning_studio) 참조하세요.

### 새로운 SDK 튜토리얼

각 Braze SDK 튜토리얼은 전체 샘플 코드와 함께 단계별 지침을 제공합니다. 시작하려면 아래에서 튜토리얼을 선택하십시오:

- [배너 표시하기]({{site.baseurl}}/developer_guide/banners/tutorial_displaying_banners)
- [인앱 메시지 스타일 사용자 정의하기]({{site.baseurl}}/developer_guide/in_app_messages/tutorials/customizing_message_styling)
- [인앱 메시지 조건부 표시하기]({{site.baseurl}}/developer_guide/in_app_messages/tutorials/conditionally_displaying_messages)
- [트리거된 인앱 메시지 연기하기]({{site.baseurl}}/developer_guide/in_app_messages/tutorials/deferring_triggered_messages)

### 데이터 유연성

#### SAML 즉시 프로비저닝

{% multi_lang_include release_type.md release="General availability" %}

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

{% multi_lang_include release_type.md release="General availability" %}

받은편지함 비전에서 [접근성 테스트]({{site.baseurl}}/user_guide/message_building_by_channel/email/inbox_vision/#accessibility-testing)를 사용하여 이메일에 존재할 수 있는 접근성 문제를 강조 표시합니다. 

접근성 테스트는 이메일 콘텐츠를 [웹 콘텐츠 접근성 지침](https://www.w3.org/WAI/standards-guidelines/wcag/) (WCAG) 2.2 AA 요구 사항에 대해 분석합니다. 이것은 어떤 요소가 접근성 기준을 충족하지 못하는지에 대한 통찰력을 제공할 수 있습니다.

#### WhatsApp 클릭 추적

{% multi_lang_include release_type.md release="General availability" %}

응답 및 템플릿 메시지 모두에서 [클릭 추적]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/click_tracking)을 활성화하여 WhatsApp 성과 보고서에서 클릭 데이터를 확인하고 클릭한 사용자에 따라 세그먼트할 수 있습니다.

#### WhatsApp용 비디오

{% multi_lang_include release_type.md release="General availability" %}

아웃바운드 WhatsApp 메시지의 본문 텍스트 내에 [비디오를 삽입할 수 있습니다.]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/create/#supported-whatsapp-features) 이 파일은 URL을 통해 호스팅되거나 [Braze 미디어 라이브러리]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/media_library)에 있어야 합니다.

### 새로운 Braze 파트너십

#### Stripe - 전자상거래

Braze와 [Stripe의]({{site.baseurl}}/partners/stripe) 통합을 통해 평가판 시작, 구독 활성화, 구독 취소 등과 같은 Stripe 이벤트에 따라 Braze에서 메시징을 트리거할 수 있습니다.

### SDK 업데이트

다음 SDK 업데이트가 릴리스되었습니다. 주요 업데이트는 아래에 나열되어 있으며, 그 외의 모든 업데이트는 해당 SDK 체인지로그를 확인하면 확인할 수 있습니다.

- [React Native SDK 15.0.1](https://github.com/braze-inc/braze-react-native-sdk/blob/master/CHANGELOG.md)
- [Flutter SDK 14.0.1-14.0.2](https://pub.dev/packages/braze_plugin/changelog)
- [Cordova SDK 12.0.0](https://github.com/braze-inc/braze-cordova-sdk/blob/master/CHANGELOG.md#1200)
    - 네이티브 Android 브리지를 [Braze Android SDK 35.0.0에서 36.0.0으로 업데이트했습니다.](https://github.com/braze-inc/braze-android-sdk/compare/v35.0.0...v36.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed)
    - 네이티브 iOS 브리지를 [Braze Swift SDK 11.6.1에서 12.0.0으로 업데이트했습니다.](https://github.com/braze-inc/braze-swift-sdk/compare/11.6.1...12.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed)
- [세그먼트 Kotlin 4.0.0-4.0.1](https://github.com/braze-inc/braze-segment-kotlin/blob/4.0.0/CHANGELOG.md#400)
    - Braze Android SDK를 [35.0.0에서 36.0.0으로 업데이트했습니다.](https://github.com/braze-inc/braze-android-sdk/compare/v35.0.0...v36.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed)

{% enddetails %}
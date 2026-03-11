---
nav_title: 홈
article_title: Braze의 새로운 소식
description: "Braze 릴리스 노트는 매월 발행되어 주요 제품 릴리스, 지속적인 제품 개선, Braze 파트너십, 중요한 SDK 변경 사항 및 기능 사용 중단에 대한 최신 정보를 유지할 수 있습니다."
page_order: 0
search_rank: 1
page_type: reference

---

# Braze의 새로운 소식

{% alert tip %}
이 페이지에 나열된 업데이트에 대한 자세한 내용은 계정 관리자에게 문의하거나 [지원 티켓을 개설하세요]({{site.baseurl}}/user_guide/administrative/access_braze/support/). 매월 SDK 릴리스, 개선 사항 및 중요한 변경 사항에 대한 자세한 내용은 [SDK 변경 로그]({{site.baseurl}}/developer_guide/changelogs)를 확인하세요.
{% endalert %}

{% details March 5, 2026 %}

## 2026년 3월 5일 출시

### 데이터 & 보고

#### 새 데이터 센터

{% multi_lang_include release_type.md release="General availability" %}

Braze는 새로운 [데이터 센터]({{site.baseurl}}/user_guide/data/data_centers/)을 출시했습니다: JP-01. Braze 계정을 설정할 때 지역별 데이터 센터에 가입할 수 있습니다.

#### 컨텍스트 변수

{% multi_lang_include release_type.md release="General availability" %}

[컨텍스트 변수]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/context_variables)는 특정 캔버스를 통해 사용자의 여정 내에서 생성하고 사용할 수 있는 임시 데이터 조각입니다. 사용자가 캔버스를 입력할 때마다(이전에 입력한 적이 있더라도) 최신 입력 데이터와 캔버스 설정을 기반으로 컨텍스트 변수가 재정의됩니다. 이 접근 방식은 각 캔버스 항목이 독립적인 컨텍스트를 유지할 수 있도록 하여 사용자가 동일한 여정 내에서 여러 활성 상태를 가지면서 각 상태에 대한 특정 컨텍스트를 유지할 수 있게 합니다.

#### 클라우드 데이터 수집 소스

{% multi_lang_include release_type.md release="Early access" %}

[클라우드 데이터 수집]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/file_storage_integrations/#setting-up-cloud-data-ingestion-in-braze)은 소스를 동기화와 분리하는 새로운 UI를 제공하여 단일 소스를 여러 동기화에서 재사용할 수 있게 합니다. 이로 인해 중복 구성이 줄어들고 여러 동기화가 있을 때 설정이 간소화됩니다. 기존 동기화가 있는 경우, 다운타임 없이 새로운 소스 및 동기화 구조로 자동 마이그레이션됩니다. 시작하려면 **클라우드 데이터 수집** > **소스**로 이동하여 소스를 보고, 편집하거나 생성한 다음, 동기화를 생성할 때 드롭다운에서 소스를 선택하세요.

#### Currents 및 데이터 공유 이벤트에 대한 추가 필드

{% multi_lang_include release_type.md release="General availability" %}

[Currents 및 데이터 공유 이벤트]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/currents_changelogs#changes-in-version-5-release-date-2026-02-04)는 분석 및 하류 시스템에 대한 데이터를 심화하기 위해 다음과 같은 새로운 필드를 포함합니다:

- `agentconsole.AgentExecuted`: 추가됨 `error` (문자열)—발생한 오류에 대한 설명입니다.
- `agentconsole.ToolInvocation`: 추가됨 `request_id` (문자열)—전체 LLM 요청 및 완전 실행을 위한 고유 ID입니다.
- `users.messages.rcs.InboundReceive`: 추가됨 `canvas_variation_name` (문자열)—사용자가 받은 Canvas 변형의 이름입니다.

#### Snowflake 데이터 공유를 위한 캠페인 및 Canvas 필드

{% multi_lang_include release_type.md release="General availability" %}

[Snowflake 데이터 공유]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/currents_changelogs/#changes-for-data-sharing-3)는 이제 66개의 기존 테이블에 걸쳐 캠페인 및 Canvas 정보를 반영하는 추가 필드를 포함합니다.

- `campaign_name`
- `canvas_name`
- `canvas_step_name`
- `canvas_variation_name`
- `message_variation_name`
- `conversion_behavior`
- `experiment_split_name`

#### CSV 사전 가져오기 유효성 검사 및 오류 보고

{% multi_lang_include release_type.md release="General availability" %}

[CSV 사용자 가져오기]({{site.baseurl}}/user_guide/data/user_data_collection/user_import)는 이제 사전 가져오기 유효성 검사 및 상세 오류 보고를 지원합니다. 가져오기 전에 **가져오기 전에 파일 유효성 검사**를 **사용자 가져오기** 페이지에서 선택하세요—Braze는 파일을 스캔하고 완전히 실패할 행(오류)과 일부 값이 건너뛰어 성공할 행(경고)을 식별하는 보고서를 생성합니다. 보고서를 다운로드하고 CSV를 수정한 후 다시 업로드하거나 그대로 진행할 수 있습니다. 가져오기가 완료된 후 실패한 행에 대한 다운로드 가능한 보고서도 제공되며, 각 문제에 대한 정확한 이유가 포함됩니다.

#### 메시징 진단 대시보드

{% multi_lang_include release_type.md release="Early access" %}

[메시징 진단 대시보드]({{site.baseurl}}/user_guide/analytics/dashboard/diagnostics_dashboard)는 메시지 전송 결과에 대한 고급 분석을 제공하여 트렌드를 파악하고 메시징 설정에서 잠재적인 문제를 진단할 수 있도록 합니다. 이 대시보드는 캠페인이나 Canvas에서 메시지가 예상대로 전송되지 않은 이유를 이해하는 데 도움이 될 수 있습니다.

### BrazeAI<sup>TM</sup>

#### 에이전트 콘솔의 Braze 에이전트

{% multi_lang_include release_type.md release="General availability" %}

[Braze 에이전트]({{site.baseurl}}/user_guide/brazeai/agents/)는 Braze 내에서 생성할 수 있는 AI 기반 도우미입니다. 에이전트는 콘텐츠를 생성하고, 지능적인 결정을 내리며, 데이터를 풍부하게 하여 보다 개인화된 고객 경험을 제공할 수 있습니다. 에이전트를 생성할 때 그 목적을 정의하고 어떻게 행동해야 하는지에 대한 가이드라인을 설정합니다. 라이브 상태가 되면 에이전트는 Braze에서 개인화된 카피를 생성하고, 실시간 결정을 내리거나 카탈로그 필드를 업데이트하는 [배포]({{site.baseurl}}/user_guide/brazeai/agents/deploying_agents)가 가능합니다.

### 오케스트레이션

#### 세분화된 사용자 권한

{% multi_lang_include release_type.md release="Early access" %}

Braze는 사용자 액세스를 관리하는 보다 유연한 방법인 [세분화된 권한]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/)을 도입하고 있습니다. [세분화된 권한으로 마이그레이션하기]({{site.baseurl}}/granular_permissions_migration/)를 참조하여 레거시 권한이 세분화된 권한에 매핑되는 방법을 포함한 마이그레이션 프로세스에 대해 알아보세요.

#### 채널 기반 속도 제한

{% multi_lang_include release_type.md release="General availability" %}

다중 채널 캠페인 또는 캔버스에 대한 배달 속도 제한을 설정할 때, 공유 속도 제한 또는 [채널 기반 제한]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#multichannel-campaigns-and-canvases)을 설정할 수 있습니다. 다중 채널 캠페인 또는 캔버스가 채널 기반 속도 제한을 사용할 때, 속도 제한은 선택된 각 채널에 적용됩니다. 예를 들어, 캠페인 또는 캔버스를 설정하여 캠페인 또는 캔버스 전반에 걸쳐 분당 최대 5,000개의 웹훅과 2,500개의 SMS 메시지를 전송할 수 있습니다.

#### 캔버스 컨텍스트 단계

{% multi_lang_include release_type.md release="General availability" %}

[캔버스 컨텍스트 단계]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context)를 사용하면 사용자가 캔버스를 이동할 때 하나 이상의 변수를 생성하고 업데이트할 수 있습니다. 예를 들어, 시즌별 할인을 관리하는 캔버스가 있는 경우 컨텍스트 변수를 사용하여 사용자가 캔버스에 들어갈 때마다 다른 할인 코드를 저장할 수 있습니다.

### 채널 & 터치포인트

#### 콘텐츠 블록에서 로케일 번역하기

{% multi_lang_include release_type.md release="Early access" %}

워크스페이스에 로케일을 추가한 후, 콘텐츠 블록 내에서 [다양한 언어의 사용자에게 타겟팅]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/locales/)할 수 있습니다.

### 파트너십

#### Algolia - 검색 추천

[Algolia]({{site.baseurl}}/partners/ecommerce/product_search_recommendations/algolia)는 개발자가 빠르고 관련성 높은 확장 가능한 검색 경험을 구축할 수 있도록 돕는 검색 및 발견 플랫폼입니다. 강력한 API 우선 접근 방식을 통해 Algolia는 고급 순위 알고리즘과 AI 기반 통찰력을 결합하여 원활한 사이트 검색, 탐색 및 개인화된 콘텐츠 발견을 제공합니다.

#### Anthropic - AI 모델 제공자

[Anthropic]({{site.baseurl}}/partners/ai_model_providers/anthropic)은 다양한 언어 작업에 유용하고 정직하며 안전하게 빌드된 차세대 AI 비서인 Claude를 개발하는 AI 안전 및 연구 회사입니다.

#### Canva - 메시지 개인화 - 크리에이티브 스튜디오

[Canva]({{site.baseurl}}/partners/canva)는 Canva의 이미지를 Braze 미디어 라이브러리에 직접 동기화하여 크리에이티브 워크플로를 간소화하고 모든 메시징 채널에서 시각적 자산을 최신 상태로 유지합니다.

#### DOTS.ECO \- 리워드

[DOTS.ECO]({{site.baseurl}}/partners/additional_channels_and_extensions/extensions/rewards/dots_eco)는 추적 가능한 디지털 인증서를 통해 사용자에게 실제 환경 영향을 보상할 수 있게 해줍니다. 각 인증서에는 공유 가능한 인증서 URL 및 이미지 URL과 같은 메타데이터를 포함할 수 있어 사용자가 자신의 영향 증명을 보고(및 다시 방문할 수) 있습니다.

#### Figma - 메시지 개인화 - 크리에이티브 스튜디오

[Figma]({{site.baseurl}}/partners/figma)는 제품을 구축하고 디자인하며 프로토타입을 만들 수 있는 협업 디자인 플랫폼입니다. 이 통합을 사용하여 Figma에서 Braze 미디어 라이브러리로 이미지를 직접 전송하세요.

#### Flybuy - 메시지 개인화 - 위치

[Flybuy]({{site.baseurl}}/partners/message_personalization/location/flybuy)는 AI 기반 기술을 활용하여 픽업, 배달, 드라이브 스루 및 식사 서비스의 속도를 최적화하는 선도적인 옴니채널 위치 플랫폼입니다. 통합된 마케팅 스위트를 통해 Flybuy는 브랜드가 하이퍼 타겟팅된 순간 기반 메시지를 전달할 수 있도록 하여 참여를 유도하고, 체크 크기를 늘리며, 더 넓은 로열티 이니셔티브를 지원합니다.

#### Google Gemini - AI 모델 제공자

[Google Gemini]({{site.baseurl}}/partners/ai_model_providers/google_gemini)는 텍스트, 코드 및 이미지 전반에 걸쳐 고급 추론을 결합하여 브랜드가 더욱 스마트하고 개인화된 경험을 제공할 수 있도록 지원하는 Google의 AI 모델 제품군입니다.

#### Limbik - 메시지 개인화 - 개인화 엔진

[Limbik]({{site.baseurl}}/partners/message_personalization/dynamic_content/personalization_engines/limbik)는 실제 청중이 메시지, 개념 및 AI 출력에 어떻게 반응하고 해석하는지를 예측하는 AI 공명 레이어입니다. 60개 이상의 국가와 25개 이상의 언어에 걸친 지속적인 1차 연구에 힘입어 Limbik는 인간 검증된 합성 청중을 제공합니다. 이는 실제 청중의 반응을 기계 속도와 연구 수준의 정확도로 시뮬레이션하는 디지털 인구입니다(95% 신뢰도, 1.5%에서 3%의 오차 범위). Limbik는 귀하의 메시지가 목표 청중이 믿고 느끼는 것과 공명하는지 즉시 확인할 수 있는 능력을 제공합니다.

#### Linkrunner - 메시지 오케스트레이션 - 귀속

[Linkrunner]({{site.baseurl}}/partners/message_orchestration/attribution/linkrunner)는 사용자 획득 캠페인을 추적하고 분석하는 데 도움을 주는 모바일 귀속 및 분석 플랫폼입니다.

#### Mailizio - 메시지 오케스트레이션 - 템플릿

[Mailizio]({{site.baseurl}}/partners/message_orchestration/templates/Mailizio)는 직관적인 비주얼 편집기를 사용하여 재사용 가능한 브랜드 안전 콘텐츠를 쉽게 디자인할 수 있는 이메일 생성 및 관리 플랫폼입니다. Mailizio의 Braze 통합을 통해 콘텐츠 블록과 이메일 템플릿을 내보낸 다음, 동일한 자산에서 자동으로 인앱 메시지를 생성하여 빠르고 완전히 제어된 캠페인 배포를 가능하게 합니다.

#### Open Loyalty - 데이터 및 분석 - 로열티

[Open Loyalty]({{site.baseurl}}/partners/data_and_analytics/loyalty/openloyalty)는 고객 로열티 및 보상 프로그램을 구축하고 관리할 수 있는 클라우드 기반 로열티 프로그램 플랫폼입니다. Braze와 Open Loyalty 통합은 포인트 잔액, 등급 변경 및 만료 경고와 같은 로열티 데이터를 실시간으로 Braze에 직접 동기화합니다. 사용자의 충성도 상태가 변경될 때 개인화된 메시지(이메일, 푸시, SMS)를 트리거할 수 있습니다.

#### OpenAI - AI 모델 제공자

[OpenAI]({{site.baseurl}}/partners/ai_model_providers/openai)는 자연어 이해 및 생성을 가능하게 하는 고급 AI 모델, 예를 들어 GPT를 생성하여 브랜드가 의미 있는 고객 상호 작용을 구축하고 확장할 수 있도록 합니다.

#### Shopgate - 채널

[Shopgate]({{site.baseurl}}/partners/additional_channels_and_extensions/additional_channels/shopgate)는 상인이 쇼핑 앱을 만들고 고객 데이터를 기반으로 한 개인화된 매장 내 고객 지원을 통해 오프라인 매장의 효율성을 개선하는 모바일 상거래 및 옴니채널 플랫폼입니다.

#### Splio - 데이터 및 분석 - 코호트 가져오기

[Splio]({{site.baseurl}}/partners/data_and_analytics/cohort_import/splio)는 고객 경험을 해치지 않으면서 캠페인 수와 수익을 늘릴 수 있는 잠재고객 구축 도구로, 온라인과 오프라인에서 CRM 캠페인의 성과를 추적할 수 있는 분석 기능을 제공합니다.

### SDK

#### SDK 주요 업데이트

다음 SDK 업데이트가 릴리스되었습니다. 주요 업데이트는 아래에 나열되어 있으며, 그 외의 모든 업데이트는 해당 SDK 체인지로그를 확인하면 확인할 수 있습니다.

- [Android SDK 41.1.1](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md)
- [Flutter SDK 17.1.0](https://pub.dev/packages/braze_plugin/changelog)
- [Swift SDK 14.0.2](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md)
- [Xamarin SDK 9.0.0](https://github.com/braze-inc/braze-xamarin-sdk/blob/master/CHANGELOG.md)
    - Android 바인딩을 [Braze Android SDK 37.0.0에서 41.0.0으로](https://github.com/braze-inc/braze-android-sdk/compare/v37.0.0...v41.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed) 업데이트했습니다.
    - iOS 바인딩을 [Braze Swift SDK 13.3.0에서 14.0.1로](https://github.com/braze-inc/braze-swift-sdk/compare/13.3.0...14.0.1#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed) 업데이트했습니다.
    - Braze Android SDK에 필요한 새로운 전이 NuGet 종속성을 추가했습니다:
        - Xamarin.AndroidX.DataStore.Preferences (1.1.7.1)
        - Xamarin.KotlinX.Serialization.Json.Jvm (1.9.0.2)
        - Xamarin.Kotlin.StdLib가 2.0.21.3에서 2.3.0.1로 업데이트되었습니다. 프로젝트가 이 패키지를 이전 버전으로 명시적으로 고정하는 경우 복원 오류를 피하기 위해 업데이트해야 합니다.
    - 뉴스 피드 기능이 제거되었습니다.
        - 이 기능은 [38.0.0](https://github.com/braze-inc/braze-android-sdk/releases/tag/v38.0.0) 버전의 기본 Android SDK에서 제거되었습니다.
        - 이 기능은 [14.0.0](https://github.com/braze-inc/braze-swift-sdk/releases/tag/14.0.0) 버전의 기본 Swift SDK에서 제거되었습니다.
    - BRZInAppMessageDismissalReason.BRZInAppMessageDismissalReasonWipeData 열거형 케이스의 이름이 BRZInAppMessageDismissalReason.WipeData로 변경되었습니다.
- [Expo 플러그인 4.0.0](https://github.com/braze-inc/braze-expo-plugin/releases/tag/4.0.0)
    - 이 버전을 사용하려면 Braze React Native SDK 19.0.0이 필요합니다.
    - (Android) 데이터 지속성 계층에서 메모리 누수를 수정했습니다.
    - (Android) 앱이 종료된 상태에서 시작될 때 푸시 알림 딥 링크를 처리하기 위해 Braze.getInitialPushPayload()에 대한 지원을 추가했습니다. 이것은 앱이 차가운 시작될 때 푸시 알림의 딥 링크가 Android에서 처리되지 않는 문제를 해결합니다.
- [React Native SDK 19.0.0](https://github.com/braze-inc/braze-react-native-sdk/releases/tag/19.0.0)
    - Braze Swift SDK 13.3.0에서 14.0.1로 기본 Swift SDK 버전 바인딩을 업데이트합니다.
    - Braze Android SDK 40.0.2에서 41.0.0으로 기본 Android SDK 버전 바인딩을 업데이트합니다.

{% enddetails %}

{% details February 5, 2026 %}

## 2026년 2월 5일 출시

### BrazeAI<sup>TM</sup>

#### 콘텐츠 최적화 프로그램

{% multi_lang_include release_type.md release="Beta" %}

[콘텐츠 최적화기]({{site.baseurl}}/user_guide/brazeai/content_optimizer)는 자동화된 참여 최적화를 제공하는 지속적이고 고변동 콘텐츠 테스트 캔버스 단계입니다. 메시지 단계와 유사한 드래그 앤 드롭 인터페이스를 사용하여 테스트할 구성 요소를 정의하고, AI를 사용하여 변형을 생성(또는 수동으로 입력)하고, Liquid 태그를 사용하여 이러한 구성 요소를 메시지 콘텐츠에 매핑합니다.

비맥락적 다중 무장 강도 최적화기를 기반으로 구축된 콘텐츠 최적화기는 사용자당 단일 메시지를 전송하며, 예측 추천에 따라 전달할 구성 요소 변형의 조합을 결정합니다. 단계가 시간이 지남에 따라 데이터를 수집함에 따라 성능이 높은 변형은 자연스럽게 전송 할당량이 증가하고 성능이 낮은 변형은 감소합니다. 콘텐츠 최적화기는 지속적인 최적화를 가능하게 하기 위해 일관된 일일 사용자 수(하루에 최소 몇 천 명의 사용자)가 있는 반복 전송 캔버스에서 가장 잘 작동합니다.

### 데이터 & 보고

#### eCommerce 추천 이벤트

{% multi_lang_include release_type.md release="Early access" %}

기존 구매 이벤트와 전자상거래 추천 이벤트를 일치시키기 위해 ["주문하기" 전환 이벤트]({{site.baseurl}}/user_guide/engagement_tools/canvas/ideas_and_strategies/ecommerce_use_cases/#conversions-report)를 추가했습니다. 이는 "구매하기"와 유사합니다.

### 채널 & 터치포인트

#### 배너에서 로케일 번역

{% multi_lang_include release_type.md release="Early access" %}

작업 공간에 로케일을 추가한 후, [다양한 언어의 사용자 타겟팅]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/locales#translating-locales)을 단일 배너 내에서 수행할 수 있습니다.

#### 드래그 앤 드롭 콘텐츠 블록의 너비를 구성하세요

[내비게이션 메뉴에서 버튼을 선택하여 콘텐츠 블록의 너비를 조정하세요]({{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/dnd_content_blocks/#using-the-editor-to-add-a-content-block) 이메일 전역 스타일 설정에서 지정하지 않으면 기본 너비는 100%입니다. 그렇지 않으면 전역 설정이 적용됩니다.

![폭을 편집할 수 있는 양면 화살표.]({% image_buster /assets/img_archive/content_block_width_updated.png %}){: style="max-width:30%;" }

#### 자동화된 IP 워밍 사용

{% multi_lang_include release_type.md release="Early access" %}

[자동화된 IP 워밍]({{site.baseurl}}/user_guide/message_building_by_channel/email/email_setup/ip_warming/#automated-ip-warming)을 사용하여 일일 발송 볼륨을 점진적으로 늘려 받은편지함 제공업체가 사용자의 전송 패턴을 학습하고 신뢰할 수 있도록 합니다. Braze는 가장 참여도가 높은 구독자에게 먼저 발송하여 일일 볼륨이 모범 사례에 맞는 속도로 증가하도록 합니다.

### 파트너십

#### LinkedIn – 캔버스 오디언스 동기화

[LinkedIn에 대한 Braze 오디언스 동기화]({{site.baseurl}}/partners/canvas_audience_sync/linkedin_audience_sync/)를 사용하여 Braze 통합의 사용자 데이터를 LinkedIn 고객 목록에 추가하여 행동 트리거, 세분화 등을 기반으로 광고를 전달합니다. 사용자 데이터를 기반으로 Braze 캔버스에서 메시지를 트리거하는 데 일반적으로 사용되는 모든 기준(푸시, 이메일, SMS, 웹훅 등)이 이제 LinkedIn 고객 목록에 있는 해당 사용자에게 광고를 트리거할 수 있습니다.

#### Oracle Crowdtwist - 데이터 & 분석

[Oracle Crowdtwist]({{site.baseurl}}/partners/crowdtwist)는 브랜드가 개인화된 고객 경험을 제공할 수 있도록 지원하는 선도적인 클라우드 네이티브 고객 충성도 솔루션입니다. 그들의 솔루션은 100개 이상의 즉시 사용 가능한 참여 경로를 제공하여 마케터가 고객에 대한 보다 완전한 관점을 개발할 수 있도록 빠른 가치를 제공합니다.

#### Fullstory - 동적 콘텐츠

[Fullstory의]({{site.baseurl}}/partners/fullstory/) 행동 데이터 플랫폼은 기술 리더가 더 나은 정보에 기반한 결정을 내릴 수 있도록 돕습니다. 디지털 행동 데이터를 분석 스택에 주입함으로써 Fullstory의 특허 기술은 대규모로 품질 높은 행동 데이터의 힘을 열어 모든 디지털 방문을 실행 가능한 통찰력으로 변환합니다. 

#### Open Loyalty - 데이터 & 분석

[Open Loyalty]({{site.baseurl}}/partners/openloyalty)는 고객 로열티 및 보상 프로그램을 구축하고 관리할 수 있는 클라우드 기반 로열티 프로그램 플랫폼입니다. Braze와 Open Loyalty 통합은 포인트 잔액, 등급 변경 및 만료 경고와 같은 로열티 데이터를 실시간으로 Braze에 직접 동기화합니다. 사용자의 충성도 상태가 변경될 때 개인화된 메시지(이메일, 푸시, SMS)를 트리거할 수 있습니다.

#### DOTS.ECO \- 확장

[DOTS.ECO]({{site.baseurl}}/partners/docs.eco)는 추적 가능한 디지털 인증서를 통해 사용자에게 실제 환경 영향을 보상할 수 있게 해줍니다. 각 인증서에는 공유 가능한 인증서 URL 및 이미지 URL과 같은 메타데이터를 포함할 수 있어 사용자가 자신의 영향 증명을 보고(및 다시 방문할 수) 있습니다.

#### Mailizio - 메시지 오케스트레이션

[Mailizio]({{site.baseurl}}/partners/mailizio/)는 직관적인 비주얼 편집기를 사용하여 재사용 가능한 브랜드 안전 콘텐츠를 쉽게 디자인할 수 있는 이메일 생성 및 관리 플랫폼입니다. Mailizio의 Braze 통합을 통해 콘텐츠 블록과 이메일 템플릿을 내보내고, 동일한 자산에서 자동으로 인앱 메시지를 생성하여 빠르고 완전히 제어된 캠페인 배포를 가능하게 합니다.

### API

#### 미디어 라이브러리 POST API

{% multi_lang_include release_type.md release="General availability" %}

미디어 라이브러리 자산은 이제 API를 통해 추가할 수 있으며, 고객, 파트너 및 에이전시가 메시지 생성 워크플로를 더 자동화할 수 있습니다. [API]({{site.baseurl}}/api/endpoints/media_library/manage_assets/create)를 사용하여 자산 파일을 직접 업로드하거나 기존 URL에서 파일을 복사하세요. 이 기능은 통합 및 자동화 기능을 열어줍니다.

### 커런트 및 데이터 공유

#### 저장소 목적지 및 데이터 공유를 위한 에이전트 콘솔 이벤트

{% multi_lang_include release_type.md release="General availability" %}

저장소 목적지(AWS S3, GCS 및 Azure Blob Storage) 및 Snowflake 데이터 공유를 위해 이제 두 개의 새로운 [이벤트](http://braze.com/docs/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events)이 제공됩니다: `agentconsole.AgentExecuted` 및 `agentconsole.ToolInvocation`. 이 이벤트는 에이전트 콘솔 사용 및 세부 정보를 다운스트림 시스템에서 분석할 수 있게 하여 에이전트 사용을 이해하고 최대한 활용하는 데 도움을 줍니다. 에이전트를 사용하면 Braze 전역에서 특정 작업을 수행할 수 있는 지능형 에이전트를 생성하고 배포할 수 있으며, 여기에는 캔버스나 카탈로그에서 콘텐츠를 생성하고 지능형 의사 결정에 따라 사용자를 다른 경로로 라우팅하는 것이 포함됩니다. 자세한 내용은 [커런트 변경 로그](https://www.braze.com/docs/user_guide/data/distribution/braze_currents/event_glossary/currents_changelogs#changes-in-version-5-release-date-2026-02-04)를 참조하세요.

#### 개별 채널에 대한 새로운 '재시도' 이벤트

{% multi_lang_include release_type.md release="General availability" %}

이제 이메일, LINE, 푸시 알림, SMS, 웹훅 및 WhatsApp 채널에 대해 새로운 [재시도 이벤트](https://www.braze.com/docs/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events)이 제공됩니다. 이 이벤트는 빈도 제한으로 인해 예정된 메시지가 중단되지 않고 지연되는 시점을 가시화합니다. 메시지가 우선 순위가 낮아지거나 빈도 제한이 걸리면 이제 구성된 재시도 창 내에서 재시도할 수 있으며, 이를 통해 메시지 전송 패턴 및 빈도 제한의 영향을 더 잘 이해할 수 있습니다. 자세한 내용은 [커런트 변경 로그](https://www.braze.com/docs/user_guide/data/distribution/braze_currents/event_glossary/currents_changelogs#changes-in-version-5-release-date-2026-02-04)를 참조하세요.

#### TokenStateChange 이벤트에 새로운 'time_ms' 필드 추가

{% multi_lang_include release_type.md release="General availability" %}

새로운 `time_ms` 필드가 [`users.behaviors.pushnotification.TokenStateChange`](https://www.braze.com/docs/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events) 이벤트에 추가되어 푸시 토큰 상태 변경을 밀리초 수준으로 추적할 수 있는 세분성을 제공합니다. 이 향상된 정밀도는 동일한 초 내에 여러 변경이 발생할 때 푸시 토큰의 최신 상태를 이해하는 데 도움을 주며, 다운스트림 시스템에서 올바른 구독 상태를 가지고 있다는 확신을 제공합니다. 자세한 내용은 [커런트 변경 로그](https://www.braze.com/docs/user_guide/data/distribution/braze_currents/event_glossary/currents_changelogs#changes-in-version-5-release-date-2026-02-04)를 참조하세요.

#### 익명 사용자를 Tealium 목적지로 전송

{% multi_lang_include release_type.md release="General availability" %}

정의된 외부 사용자 ID가 없는 이벤트는 이제 [Tealium]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/tealium/tealium_for_currents?redirected=1#tealium-for-currents) 목적지로 스트리밍될 수 있습니다. 커런트 통합에서 "익명 사용자로부터의 이벤트 포함" 체크박스를 선택하면 외부 사용자 ID가 없는 이벤트가 억제되지 않고 목적지로 전송됩니다. 이 기능은 비식별 및 익명 사용자를 포함한 하류 분석 및 사용 사례에 중요합니다.

##### 익명 사용자를 CustomHTTP 대상으로 전송

{% multi_lang_include release_type.md release="Beta" %}

외부 사용자 ID가 정의되지 않은 이벤트는 이제 CustomHTTP 대상으로 스트리밍할 수 있습니다. 커런트 통합에서 "익명 사용자로부터의 이벤트 포함" 체크박스를 선택하면 외부 사용자 ID가 없는 이벤트가 억제되지 않고 목적지로 전송됩니다. 이 기능은 비식별 및 익명 사용자를 포함한 하류 분석 및 사용 사례에 중요합니다.

#### 이메일 열기 이벤트 — "machine_open" 필드

[이메일 열기 이벤트]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events#email-open-events)는 이제 "machine_open" 필드 값을 생성하여 [_기계 열기_]({{site.baseurl}}/user_guide/analytics/reporting/report_metrics#machine-opens) 메트릭을 보고합니다. 

### SDK

다음 SDK 업데이트가 릴리스되었습니다. Swift SDK v14.0.1은 유니버설 링크 처리와 관련된 문제를 수정합니다. Android SDK v40.2.0은 잠재적인 메모리 누수를 수정하고 투명한 활동이 있을 때 여러 세션이 열리는 문제를 해결합니다. Expo SDK v3.2.0은 유니버설 링크의 네이티브 Swift SDK 처리를 구성하기 위해 `forwardUniversalLinks` 옵션(기본값: false)을 추가합니다.

#### SDK 주요 업데이트

다음 SDK 업데이트가 릴리스되었습니다. 주요 업데이트는 아래에 나열되어 있으며, 그 외의 모든 업데이트는 해당 SDK 체인지로그를 확인하면 확인할 수 있습니다.

- [Android SDK 41.0.0](https://github.com/braze-inc/braze-android-sdk/releases/tag/v41.0.0)
    - 이름을 `BrazeConfig.Builder.setIsLocationCollectionEnabled()`에서 `setIsAutomaticLocationCollectionEnabled()`(으)로 변경했습니다.
    - 이름을 `BrazeConfig.isLocationCollectionEnabled`에서 `isAutomaticLocationCollectionEnabled`(으)로 변경했습니다.
    - 이름을 `BrazeConfigurationProvider.isLocationCollectionEnabled`에서 `isAutomaticLocationCollectionEnabled`(으)로 변경했습니다.
- [Android SDK 40.2.0](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#4020)
- [Expo 플러그인 3.2.0](https://github.com/braze-inc/braze-expo-plugin/blob/main/CHANGELOG.md)
- [Swift SDK 14.0.1](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md)

{% enddetails %}

{% details January 8, 2026 %}
## 2026년 1월 8일 출시

### 데이터 & 보고

#### Currents 이벤트 업데이트

{% multi_lang_include release_type.md release="General availability" %}

버전 4에서 Currents에 대해 다음과 같은 변경 사항이 있었습니다:

* 이벤트 유형 `users.behaviors.pushnotification.TokenStateChange`에 대한 필드 변경 사항:
    * 새로운 `string` 필드 `push_token` 추가: 이벤트의 푸시 토큰
* 이벤트 유형 `users.messages.pushnotification.Bounce`에 대한 필드 변경 사항:
    * 새로운 `string` 필드 `push_token` 추가: 이벤트의 푸시 토큰
* 이벤트 유형 `users.messages.pushnotification.Send`에 대한 필드 변경 사항:
    * 새로운 `string` 필드 `push_token` 추가: 이벤트의 푸시 토큰
* 이벤트 유형 `users.messages.rcs.Click`에 대한 필드 변경 사항:
    * 새로운 `string` 필드 `canvas_variation_name` 추가: 이 사용자가 받은 캔버스 변형의 이름
    * 필드 `user_phone_number`은 이제 *선택적*입니다.
* 이벤트 유형 `users.messages.rcs.InboundReceive`에 대한 필드 변경 사항:
    * 필드 `user_id`은 이제 *선택적*입니다.
* 이벤트 유형 `users.messages.rcs.Rejection`에 대한 필드 변경 사항:
    * 새로운 `string` 필드 `canvas_step_message_variation_id` 추가: 이 사용자가 받은 캔버스 단계 메시지 변형의 API ID

각 릴리스에 대한 이벤트 변경 사항은 [Currents changelog]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/currents_changelogs)를 참조하십시오.

#### 모든 행으로 동기화 로그 내보내기

{% multi_lang_include release_type.md release="Early access" %}

[Cloud Data Ingestion **Sync Log** 대시보드]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/sync_logs/#exporting-sync-logs)에서 동기화 실행에 대한 행 수준 로그를 내보내도록 선택하십시오:

* **오류가 있는 행:** **Error** 상태인 행만 포함된 파일을 다운로드합니다.
* **모든 행:** 실행에서 처리된 모든 행을 포함하는 파일을 다운로드합니다.

### 채널 & 터치포인트

#### 자신의 WhatsApp 커넥터(BYO) 가져오기

[자신의 WhatsApp 커넥터(BYO)]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/byo_connector/)는 Braze와 Infobip 간의 파트너십을 제공하며, Braze에 Infobip WhatsApp Business Manager(WABA)에 대한 액세스를 제공합니다. 이를 통해 Braze를 사용하여 세분화, 개인화 및 캠페인 조정을 하면서 Infobip과 직접 메시징 비용을 관리하고 지불할 수 있습니다. 

#### 캔버스의 배너

{% multi_lang_include release_type.md release="Early access" %}

캔버스의 [메시지 단계]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step)에서 메시징 채널로 **배너**를 선택하십시오. 드래그 앤 드롭 편집기를 사용하여 개인화된 인라인 메시지를 생성하여 각 사용자 세션 시작 시 자동으로 업데이트되는 비침해적이고 맥락적으로 관련된 경험을 제공합니다. 

#### 동적 BCC

{% multi_lang_include release_type.md release="General availability" %}

[동적 BCC]({{site.baseurl}}/user_guide/administrative/app_settings/email_settings/?tab=bcc%20address#dynamic-bcc)를 사용하여 BCC 주소에 Liquid를 사용하십시오. 이 기능은 **이메일 기본 설정**에서만 사용할 수 있으며 캠페인 자체에서 설정할 수 없습니다. 이메일 수신자당 하나의 BCC 주소만 허용됩니다.

#### 채널 기반 속도 제한

전체 다중 채널 캠페인 또는 캔버스에 걸쳐 공유되는 속도 제한의 대안으로, 채널별로 특정 속도 제한을 선택하십시오. 이 경우, 속도 제한은 선택한 각 채널에 적용됩니다. 예를 들어, 캠페인 또는 캔버스를 설정하여 캠페인 또는 캔버스 전반에 걸쳐 분당 최대 5,000개의 웹훅과 2,500개의 SMS 메시지를 전송하도록 합니다. 자세한 내용은 [속도 제한 및 빈도 제한]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting)을 참조하십시오.

### 파트너십

#### LILT - 현지화

[LILT]({{site.baseurl}}/partners/lilt/)는 기업 번역 및 콘텐츠 생성에 대한 완전한 AI 솔루션입니다. LILT는 글로벌 조직이 AI 에이전트와 완전 자동화된 워크플로를 통해 콘텐츠, 제품, 커뮤니케이션 및 지원 운영을 확장하고 최적화할 수 있도록 합니다.

### SDK 주요 업데이트

다음 SDK 업데이트가 릴리스되었습니다. 주요 업데이트는 아래에 나열되어 있으며, 그 외의 모든 업데이트는 해당 SDK 체인지로그를 확인하면 확인할 수 있습니다.

- [안드로이드 40.1.1](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#4011)
- [안드로이드 SDK 40.1.0](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#4010)
- [스위프트 SDK 14.0.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md)
    - 뉴스 피드를 제거합니다.
        - 이것은 뉴스 피드와 관련된 모든 UI 요소, 데이터 모델 및 작업을 완전히 제거합니다.
- [웹 SDK 6.4.0](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md)

{% enddetails %}

{% details December 9, 2025 %}

## 2025년 12월 9일

### 데이터 & 보고

#### 랜딩 페이지에 Google 태그 관리자 추가하기

랜딩 페이지에 Google 태그 관리자를 추가하려면 드래그 앤 드롭 편집기에서 랜딩 페이지에 사용자 정의 코드 블록을 추가한 다음 [태그 관리자 코드를 삽입]({{site.baseurl}}/user_guide/engagement_tools/landing_pages#adding-google-tag-manager-to-a-landing-page)합니다.

### 오케스트레이션

#### SMS Liquid 사용 사례

[수신 SMS 키워드에 따라 다른 메시지로 응답]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/liquid_use_cases#sms-keyword-response) 사용 사례는 특정 수신 메시지에 대해 다른 메시지 복사본으로 응답하기 위해 동적 SMS 키워드 처리를 통합합니다. 예를 들어, 누군가 "START"라고 문자 메시지를 보낼 때와 "JOIN"이라고 보낼 때 다른 응답을 보낼 수 있습니다.

#### 연결된 콘텐츠에 대한 허용 목록

특정 URL을 [연결된 콘텐츠]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/making_an_api_call)에 사용할 수 있도록 허용 목록에 추가할 수 있습니다. 이 기능에 액세스하려면 고객 성공 관리자에게 문의하십시오.

### 채널 & 터치포인트

#### SMS 문자 인코딩

우리 [SMS 세그먼트 계산기]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/segments/#segment-calculator)는 이제 문자 인코딩을 지원합니다! **디스플레이 문자 인코딩**을 선택하여 어떤 문자가 GSM-7 또는 UCS-2로 인코딩되었는지 확인하세요. 

![SMS 세그먼트 계산기에는 텍스트 박스에 입력된 샘플 SMS 메시지와 문자 인코딩이 켜져 있습니다.]({% image_buster /assets/img/sms/character_encoding.png %}){: style="max-width:70%;"}

#### 최적화된 WhatsApp 메시지

WhatsApp의 MM API는 100% 배달 보장을 제공하지 않기 때문에, 다른 채널에서 메시지를 받지 못한 사용자를 재타겟팅하는 방법을 이해하는 것이 중요합니다. 

사용자를 재타겟팅하기 위해, 특정 메시지를 받지 못한 사용자 세그먼트를 구축하는 것을 권장합니다. 이를 위해, WhatsApp의 사용자별 마케팅 템플릿 제한 시행으로 인해 마케팅 템플릿 메시지가 전송되지 않았음을 나타내는 오류 코드 `131049`로 필터링하세요. 이 작업은 [Braze Currents 또는 SQL 세그먼트 확장]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/optimized_delivery/#retargeting-users-on-other-braze-channels)을 사용하여 수행할 수 있습니다.

### 파트너십

#### OtherLevels - 동적 콘텐츠

[OtherLevels]({{site.baseurl}}/partners/otherlevels/)는 스포츠 브랜드, 퍼블리셔 및 운영자가 고객과 연결하는 방식을 변화시키기 위해 생성 AI를 사용하는 경험 플랫폼으로, 전통적인 콘텐츠를 브랜드에 맞는 개인화된 비디오 및 풍부한 미디어 경험으로 변환합니다.

### SDK

#### SDK 주요 업데이트

다음 SDK 업데이트가 릴리스되었습니다. 주요 업데이트는 아래에 나열되어 있으며, 그 외의 모든 업데이트는 해당 SDK 체인지로그를 확인하면 확인할 수 있습니다.

- [웹 SDK 6.3.1](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md)

{% enddetails %}

{% details November 11, 2025 %}

## 2025년 11월 11일

### 데이터 유연성

#### `Live Activities Push to Start Registered for App` 세분화 필터

`Live Activities Push to Start Registered for App` 필터는 사용자가 특정 앱에 대한 iOS 푸시 알림을 통해 라이브 활동을 시작하도록 등록되었는지에 따라 사용자를 세분화합니다.

#### RFM SQL 세그먼트 확장

구매 습관을 측정하여 최고의 사용자를 타겟팅하기 위해 [RFM (최근성, 빈도, 금액) 세그먼트 확장]({{site.baseurl}}/rfm_segments/)을 생성할 수 있습니다.

RFM 분석은 사용자를 각 카테고리(최근성, 빈도, 금액)에 대해 0-3의 척도로 점수화하여 최고의 사용자를 식별하는 마케팅 기법입니다. 여기서 3은 최고의 점수이고 0은 최악의 점수입니다. 최근성, 빈도 및 금액 값은 모두 사용자가 선택한 특정 시간 범위의 데이터를 기반으로 합니다.

#### 커스텀 속성 — 값 

사용 보고서를 볼 때, [**값** 탭]({{site.baseurl}}/user_guide/data/activation/custom_data/custom_attributes/#values-tab)을 선택하여 약 250,000명의 사용자 샘플을 기반으로 선택한 사용자 정의 속성의 상위 값을 확인합니다.

#### 클라우드 데이터 수집을 위한 동기화 로그 및 가시성

{% multi_lang_include release_type.md release="General availability" %}

클라우드 데이터 수집(CDI) [동기화 로그 대시보드]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/sync_logs/)를 통해 CDI가 처리한 모든 데이터를 모니터링하고, 데이터가 성공적으로 동기화되었는지 확인하며, "잘못된" 또는 누락된 데이터와 관련된 문제를 진단할 수 있습니다.

#### 다중 규칙 기능 플래그 롤아웃

[다중 규칙 기능 플래그 롤아웃]({{site.baseurl}}/developer_guide/feature_flags/create/#multi-rule-feature-flag-rollouts)을 사용하여 사용자를 평가하기 위한 규칙의 순서를 정의할 수 있으며, 이를 통해 정밀한 세분화 및 제어된 기능 릴리스를 가능하게 합니다. 이 방법은 다양한 청중에게 동일한 기능을 배포하는 데 이상적입니다.

#### 드래그 앤 드롭 제품 블록을 위한 카탈로그 필드 매핑

카탈로그 설정에서 **제품 블록** 토글을 선택하여 [특정 필드]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/product_blocks/#catalog-setup) 및 카탈로그의 정보를 매핑할 수 있습니다. 이를 통해 제품 제목, 제품 URL 및 이미지 URL로 사용할 필드를 선택할 수 있습니다.

#### Currents에서 빈도 제한 중단 이벤트

Currents를 사용할 때 이제 채널 중단 이벤트에서 `abort_type`을 참조할 수 있습니다. 이는 빈도 제한으로 인해 메시지가 중단되었음을 식별하고, 중단을 유발한 빈도 제한 규칙을 포함합니다. 이는 빈도 제한 규칙을 설정하는 방법에 대한 정보를 제공합니다. 특정 Currents 이벤트 세부정보는 [메시지 참여 이벤트]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events)를 참조하십시오.

### 강력한 채널

#### 배경 행 이미지 

{% multi_lang_include release_type.md release="General availability" %}

[배경 행 이미지]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/style_settings/#background-image)를 인앱 메시지 또는 **행 속성** 패널의 랜딩 페이지에 추가할 수 있습니다. **배경 이미지**를 켜고, 이미지 URL을 제공하거나 [미디어 라이브러리]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/media_library/)에서 이미지를 선택합니다. 마지막으로, 대체 텍스트, 크기, 위치 및 이미지 반복 여부를 구성하여 행 전체에 패턴을 생성합니다.

![수평 반복 패턴이 있는 피자의 행 배경 이미지입니다.]({% image_buster /assets/img_archive/background_row.png %})

#### 미리보기 링크 복사

**미리보기 링크 복사**를 [배너]({{site.baseurl}}/user_guide/message_building_by_channel/banners/create/#step-5-test-your-message-optional), [이메일 맞춤 바닥글]({{site.baseurl}}/user_guide/message_building_by_channel/email/custom_email_footer/#creating-your-custom-footer), 및 [이메일 옵트인 및 구독 취소 페이지]({{site.baseurl}}/user_guide/administrative/app_settings/email_settings/?tab=custom%20footer#subscription-pages-and-footers)에서 사용하여 무작위 사용자에게 콘텐츠가 어떻게 보일지를 보여주는 공유 가능한 링크를 생성합니다.

#### 최적화된 배달을 위한 WhatsApp 메시지

메타의 고급 AI 시스템을 사용하여 마케팅 메시지를 더 많은 사용자에게 전달하여 참여할 가능성이 높은 사용자와의 상호작용을 크게 향상시킵니다.

[최적화된 배달을 위한 WhatsApp 메시지]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/optimized_delivery/)는 메타의 새로운 [마케팅 메시지 라이트 API](https://developers.facebook.com/docs/whatsapp/marketing-messages-lite-api/)를 사용하여 전통적인 클라우드 API에 비해 우수한 성능을 제공합니다. 이 새로운 전송 파이프라인은 메시지를 받고 싶어하는 사용자에게 더 잘 도달할 수 있도록 도와줍니다.

#### WhatsApp Flows

WhatsApp Flow 메시지를 Braze Canvas 또는 캠페인에 통합할 때, Flow를 통해 사용자가 제출한 특정 정보를 캡처하고 활용하고 싶을 수 있습니다. Braze는 필요한 중첩 사용자 정의 속성(NCA) 스키마를 생성하기 위해 사용자 응답의 구조에 대한 추가 정보를 받아야 합니다. 특히 JSON 응답의 예상 형태에 대한 정보가 필요합니다.

이제 [Flow 응답을 사용자 정의 속성으로 저장]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/whatsapp_flows/?tab=recommended%20method#step-1-generate-the-flow-custom-attribute)하여 응답 구조에 대한 정보를 Braze에 제공하고 테스트 전송을 완료할 수 있습니다.

#### 편집 가능한 사용자 미리보기

무작위 또는 기존 사용자로부터 [개별 필드를 편집]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/sending_test_messages/?tab=webhook#customizing-an-existing-user)하여 메시지 내에서 동적 콘텐츠를 테스트하는 데 도움을 줄 수 있습니다. 선택한 사용자를 수정할 수 있는 사용자 정의 사용자로 변환하려면 **편집**를 선택하십시오.

!["사용자로 미리보기" 탭과 "편집" 버튼이 있습니다.]({% image_buster /assets/img_archive/edit_user_preview.png %}){: style="max-width:50%;"}

### AI 및 ML 자동화

#### BrazeAI Decisioning Studio™ Go

이제 다음 구성 기사를 참조하여 [BrazeAI Decisioning Studio™ Go]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/go)와의 통합을 설정할 수 있습니다:

- [Braze]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/go/configuring_braze)
- [Klaviyo]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/go/configuring_klaviyo)
- [Salesforce Marketing Cloud]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/go/configuring_sfmc)

#### Braze 에이전트를 위한 새로운 기능

{% multi_lang_include release_type.md release="Beta" %}

이제 [Braze 에이전트]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents)를 다음과 같이 사용자 정의할 수 있습니다:

- 응답에서 준수해야 할 [브랜드 가이드라인]({{site.baseurl}}/user_guide/administrative/app_settings/brand_guidelines) 적용하기. 
- 메시지를 더욱 개인화하기 위해 카탈로그 참조하기.
- [출력 형식]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents/#output-format)을 제공하여 에이전트의 출력을 구조화하기.
- 에이전트 출력의 편차 수준에 대한 [온도]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents/#temperature) 조정.

### BrazeAI Operator<sup>TM</sup>가 포함된 ChatGPT 모델

{% multi_lang_include release_type.md release="Beta" %}

다양한 요청 유형에 사용할 수 있는 이러한 GPT 모델 중에서 선택할 수 있습니다 [Operator]({{site.baseurl}}/user_guide/brazeai/operator):

- GPT-5 나노
- GPT-5 미니 (기본)
- GPT-5

### 새로운 Braze 파트너십

#### StackAdapt - 광고

[StackAdapt]({{site.baseurl}}/partners/stackadapt/)는 성과 중심의 타겟 광고를 제공하는 AI 기반 마케팅 플랫폼입니다. Braze에서 StackAdapt 데이터 허브로 사용자 프로필 데이터를 동기화할 수 있습니다. 두 플랫폼을 연결하면 고객에 대한 통합된 뷰를 생성하고 1차 데이터를 활성화하여 광고 성과를 개선할 수 있습니다.

#### Cloudinary - 동적 콘텐츠

[Cloudinary]({{site.baseurl}}/partners/cloudinary/)는 대규모로 이미지와 비디오를 관리, 편집, 최적화 및 전달할 수 있게 해주는 이미지 및 비디오 플랫폼입니다. 통합 및 활성화되면 Cloudinary의 미디어 관리가 Braze 캠페인 및 캔버스에 대한 동적, 맥락적, 개인화된 자산 전달을 지원합니다.

#### Kameleoon - A/B 테스트

[Kameleoon]({{site.baseurl}}/partners/kameleoon/)은 실험, AI 기반 개인화 및 기능 관리 기능을 갖춘 최적화 솔루션입니다.

### SDK 업데이트

다음 SDK 업데이트가 릴리스되었습니다. 주요 업데이트는 아래에 나열되어 있으며, 그 외의 모든 업데이트는 해당 SDK 체인지로그를 확인하면 확인할 수 있습니다.

- [React Native SDK 18.0.0](https://github.com/braze-inc/braze-react-native-sdk/blob/16.1.0/CHANGELOG.md)
    - `subscribeToInAppMessage` 및 `addListener`의 콜백에 대한 Typescript 유형을 수정합니다.
        - 이 리스너는 이제 새로운 `InAppMessageEvent` 유형으로 콜백을 올바르게 반환합니다. 이전에는 메서드가 `BrazeInAppMessage` 유형을 반환하도록 주석이 달렸지만 실제로는 `String`을 반환하고 있었습니다.
         - 구독 API 중 하나를 사용하는 경우, 이 버전으로 업데이트한 후 인앱 메시지의 동작이 변경되지 않았는지 확인하십시오. `BrazeProject.tsx`에서 샘플 코드를 참조하십시오.
    - API `logInAppMessageClicked`, `logInAppMessageImpression`, `logInAppMessageButtonClicked`는 이제 기존 공개 인터페이스와 일치하는 `BrazeInAppMessage` 객체만 허용합니다.
        - 이전에는 `BrazeInAppMessage` 객체와 `String` 객체 모두를 허용했습니다.
    - `BrazeInAppMessage.toString()`은 이제 JSON 문자열 표현 대신 사람이 읽을 수 있는 문자열을 반환합니다.
        - 인앱 메시지의 JSON 문자열 표현을 얻으려면 `BrazeInAppMessage.inAppMessageJsonString`을 사용하세요.
    - iOS에서는 `[[BrazeReactUtils sharedInstance] formatPushPayload:withLaunchOptions:]`이 `[BrazeReactDataTranslator formatPushPayload:withLaunchOptions:]`로 이동했습니다.
        - 이 새로운 메서드는 인스턴스 메서드 대신 클래스 메서드가 되었습니다.
    - `BrazeReactUtils` 메서드에 nullability 주석을 추가합니다.
    - 다음의 더 이상 사용되지 않는 메서드와 속성을 API에서 제거합니다:
        - `getInstallTrackingId(callback:)`을 `getDeviceId`로 대체합니다.
        - `registerAndroidPushToken(token:)`을 `registerPushToken`로 대체합니다.
        - `setGoogleAdvertisingId(googleAdvertisingId:adTrackingEnabled:)`을 `setAdTrackingEnabled`로 대체합니다.
        - `PushNotificationEvent.push_event_type`을 `payload_type`로 대체합니다.
        - `PushNotificationEvent.deeplink`을 `url`로 대체합니다.
        - `PushNotificationEvent.content_text`을 `body`로 대체합니다.
        - `PushNotificationEvent.raw_android_push_data`을 `android`로 대체합니다.
        - `PushNotificationEvent.kvp_data`을 `braze_properties`로 대체합니다.
    - 네이티브 Android SDK 버전 바인딩을 [Braze Android SDK 39.0.0에서 40.0.2로](https://github.com/braze-inc/braze-android-sdk/compare/v39.0.0...v40.0.2#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed) 업데이트합니다.
- [.NET MAUI (Xamarin) SDK 버전 8.0.0](https://github.com/braze-inc/braze-xamarin-sdk/blob/master/CHANGELOG.md)
    - iOS 바인딩을 [Braze Swift SDK 12.1.0에서 13.3.0으로](https://github.com/braze-inc/braze-swift-sdk/compare/12.1.0...13.3.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed) 업데이트했습니다. 여기에는 Xcode 26 지원이 포함됩니다.
- [Flutter SDK 16.0.0](https://pub.dev/packages/braze_plugin/changelog)
    - 네이티브 Android 브릿지를 [Braze Android SDK 39.0.0에서 40.0.0으로](https://github.com/braze-inc/braze-android-sdk/compare/v39.0.0...v40.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed) 업데이트합니다.
- [Braze Swift SDK 13.3.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md)
- [Web SDK 6.3.0](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md)
- [Android SDK 40.0.0-40.0.2](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md)

{% enddetails %}

{% details October 14, 2025 %}

## 2025년 10월 14일 출시

### BrazeAI Decisioning Studio™

[BrazeAI Decisioning Studio™](https://www.braze.com/product/brazeai-decisioning-studio/)은 A/B 테스트를 AI 의사 결정으로 대체하여 모든 항목을 개인화하고, 모든 측정기준을 극대화합니다: 클릭이 아닌 수익을 유도합니다. BrazeAI Decisioning Studio™를 사용하면 모든 비즈니스 KPI를 최적화할 수 있습니다. 샘플 사용 사례 및 주요 기능에 대한 전용 섹션 [BrazeAI Decisioning Studio™]({{site.baseurl}}/user_guide/brazeai/decisioning_studio)를 참조하십시오.

### 데이터 유연성

#### 신규 커런츠 이벤트

다음 [Currents glossary]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events)에 새로운 이벤트가 추가되었습니다:

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

다음 Currents 이벤트에 새로운 필드가 추가되었습니다:

- `is_sms_fallback`: 
  - `users.messages.sms.Delivery`
  - `users.messages.sms.DeliveryFailure`
  - `users.messages.sms.Rejection`
- `message_id`, `in_reply_to`, `flow_id`, `flow_response_json`, `product_id`, `catalog_id`: 
  - `users.messages.whatsapp.InboundReceive`
- `message_id`, `flow_id`, `template_name`: 
  - `users.messages.whatsapp.Send`
  - `users.messages.whatsapp.Delivery`
  - `users.messages.whatsapp.Failure`
  - `users.messages.whatsapp.Read`

#### 억제 목록

{% multi_lang_include release_type.md release="General availability" %}

[Suppressions lists]({{site.baseurl}}/user_guide/engagement_tools/segments/suppression_lists)는 자동으로 캠페인이나 캔버스를 받지 않는 사용자 그룹입니다. Suppressions lists는 세그먼트 필터로 정의되며, 사용자는 필터 기준을 충족함에 따라 Suppressions lists에 들어가고 나옵니다.

#### 제로 카피 개인화

{% multi_lang_include release_type.md release="Early access" %}

Cloud Data Ingestion을 사용하여 [제로 카피 개인화]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/zero_copy_sync/)에 대한 Canvas 트리거를 동기화합니다. 이 기능은 데이터 저장 솔루션에서 사용자 특정 정보를 액세스하고 이를 대상 Canvas에 전달합니다. Canvas 단계에는 Braze 사용자 프로필에 지속되지 않는 개인화 필드를 선택적으로 포함할 수 있습니다.

#### 청중 경로 및 결정 분할 단계에 대한 Canvas Context 변수

{% multi_lang_include release_type.md release="Early access" %}

이전 선언된 Context 변수를 사용하여 [Context variable filters]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/context_variables/#context-variable-filters)를 [청중 경로]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/audience_paths) 및 [결정 분할]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/decision_split) 단계에서 생성할 수 있습니다.

### 창의력 발휘

#### 이메일용 거래 카드

이메일 본문의 맨 위에 주요 거래 정보를 제공하기 위해 [거래 카드]({{site.baseurl}}/user_guide/message_building_by_channel/email/html_editor/gmail_promotions_tab)를 사용하십시오. 이렇게 하면 수신자가 제안 세부정보를 빠르게 이해하고 조치를 취할 수 있습니다.

#### 배너 템플릿

배너를 [작성할 때<1>, 빈 템플릿으로 시작하거나, Braze 템플릿을 사용하거나, 저장된 배너 템플릿을 선택할 수 있습니다.

### 강력한 채널

#### 억제 목록

{% multi_lang_include release_type.md release="General availability" %}
 
[억제 목록]({{site.baseurl}}/user_guide/engagement_tools/segments/suppression_lists/)은 메시지를 절대 받지 않을 사용자 그룹을 지정합니다. 관리자는 세분화와 동일한 방식으로 사용자 그룹을 좁히기 위해 세그먼트 필터로 억제 목록을 생성할 수 있습니다.

#### LINE 클릭 추적

{% multi_lang_include release_type.md release="General availability" %}

[LINE 클릭 추적]({{site.baseurl}}/line/click_tracking/)이 활성화되면, Braze는 자동으로 URL을 단축하고, 추적 메커니즘을 추가하며, 실시간으로 클릭을 기록합니다. LINE은 집계된 클릭 데이터를 제공하지만, Braze는 시기적절하고 실행 가능한 세부 사용자 정보를 제공합니다. 이 데이터는 클릭 행동에 따라 사용자를 세분화하고 특정 클릭에 대한 메시지를 트리거하는 등의 보다 타겟팅된 세분화 및 리타겟팅 전략을 수립할 수 있도록 합니다.

#### SMS 및 RCS 봇 클릭 필터링

{% multi_lang_include release_type.md release="General availability" %}

[SMS 및 RCS 봇 클릭 필터링]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/bot_click_filtering/)은 의심되는 봇 클릭을 제외하여 캠페인 분석 및 워크플로를 향상시킵니다. “봇 클릭”은 SMS 및 RCS 메시지의 단축 링크에 대한 자동 클릭을 의미하며, 웹 크롤러, Android 및 iOS 링크 미리보기 또는 CPaaS 보안 소프트웨어에서 발생할 수 있습니다. 이 기능은 실제 사용자와의 참여를 위해 정확한 보고, 세분화 및 조정을 용이하게 합니다.

#### WhatsApp 전화번호 전송

WhatsApp 비즈니스 계정(WABA) 전화번호와 관련된 구독 그룹을 [하나의 작업 공간에서 다른 작업 공간으로]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/transfer_between_workspaces/) 전송합니다.

#### WhatsApp 흐름 응답 메시지 및 미리보기

캔버스에서 [응답 메시지]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/whatsapp_flows/?tab=response%20message#configuring-whatsapp-flow-messages-and-responses)와 흐름 메시지를 사용하는 WhatsApp 메시지 단계를 생성할 수 있습니다. 또한 **흐름 미리보기**를 선택하여 Braze에서 흐름이 예상대로 작동하는지 확인할 수 있습니다.

#### WhatsApp 제품 메시지

[제품 메시지]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/product_messages/)는 Meta 카탈로그에서 직접 제품을 보여주는 대화형 WhatsApp 메시지를 보낼 수 있도록 합니다.

#### Braze와 WhatsApp을 외부 시스템과 통합하기

[AI 챗봇과 실시간 상담원 전환의 힘을 활용하여]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_use_cases/external_system/) WhatsApp 채널에서 고객 지원 운영을 간소화합니다. 일상적인 문의를 자동화하고 필요할 때 인간 상담원으로 원활하게 전환함으로써, 응답 시간을 크게 개선하고 전반적인 고객 경험을 향상시킬 수 있습니다.

### AI 및 ML 자동화

#### Braze 에이전트

{% multi_lang_include release_type.md release="Beta" %}

[Braze 에이전트]({{site.baseurl}}/user_guide/brazeai/agents/)는 Braze 내에서 생성할 수 있는 AI 기반 도우미입니다. 에이전트는 콘텐츠를 생성하고, 지능적인 결정을 내리며, 데이터를 풍부하게 하여 보다 개인화된 고객 경험을 제공할 수 있습니다.

### 새로운 Braze 파트너십

#### 재스퍼 - 템플릿

[재스퍼]({{site.baseurl}}/partners/jasper/)와 Braze의 통합은 콘텐츠 생성 및 캠페인 실행을 간소화할 수 있도록 합니다. 재스퍼를 사용하면 마케팅 팀이 몇 분 만에 고품질의 브랜드 일치 카피를 생성할 수 있습니다. Braze는 이러한 메시지를 적절한 시간에 올바른 청중에게 전달하는 것을 용이하게 합니다. 이 통합은 원활한 워크플로를 촉진하고, 수작업 노력을 줄이며, 더 강력한 참여 결과를 이끌어냅니다.

#### 스윔 - 로열티 및 리타겟팅

[스윔]({{site.baseurl}}/partners/swym/)은 전자상거래 브랜드가 위시리스트, 나중에 저장, 선물 등록부 및 재입고 알림으로 쇼핑 의도를 포착하도록 돕습니다. 풍부하고 허가 기반의 데이터를 사용하여 하이퍼 타겟 캠페인을 제작하고 참여를 유도하며 전환을 증가시키고 로열티를 높이는 개인화된 쇼핑 경험을 제공할 수 있습니다.

### SDK 업데이트

다음 SDK 업데이트가 릴리스되었습니다. 주요 업데이트는 아래에 나열되어 있으며, 해당 SDK 체인지로그를 확인하면 모든 다른 업데이트를 찾을 수 있습니다.

- [Cordova SDK 14.0.0](https://github.com/braze-inc/braze-cordova-sdk/blob/master/CHANGELOG.md)
    - 네이티브 Android 브리지를 [Braze Android SDK 37.0.0에서 39.0.0으로](https://github.com/braze-inc/braze-android-sdk/compare/v37.0.0...v39.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed) 업데이트했습니다.
        - 필수 GradlePluginKotlinVersion은 이제 2.1.0입니다.
    - 네이티브 iOS 브리지를 [Braze Swift SDK 12.0.0에서 13.2.0으로](https://github.com/braze-inc/braze-swift-sdk/compare/12.0.0...13.2.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed) 업데이트했습니다. 여기에는 Xcode 26 지원이 포함됩니다.
    - 뉴스 피드에 대한 지원이 제거됩니다. 다음 API가 제거되었습니다:
        - `launchNewsFeed`
        - `getNewsFeed`
        - `getNewsFeedUnreadCount`
        - `getNewsFeedCardCount`
        - `getCardCountForCategories`
        - `getUnreadCardCountForCategories`
- [React Native SDK 17.0.0-17.0.1](https://www.npmjs.com/package/@braze/react-native-sdk/v/17.0.1)
    - 네이티브 Android SDK 버전 바인딩을 [Braze Android SDK 37.0.0에서 39.0.0으로](https://github.com/braze-inc/braze-android-sdk/compare/v37.0.0...v39.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed) 업데이트합니다.
    - 뉴스 피드에 대한 지원이 제거됩니다. 다음 API가 제거되었습니다:
        - `launchNewsFeed`
        - `requestFeedRefresh`
        - `getNewsFeedCards`
        - `logNewsFeedCardClicked`
        - `logNewsFeedCardImpression`
        - `getCardCountForCategories`
        - `getUnreadCardCountForCategories`
        - `Braze.Events.NEWS_FEED_CARDS_UPDATED`
        - `Braze.CardCategory`
- [Web SDK 6.2.0](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md)
- [Flutter SDK 15.1.0](https://pub.dev/packages/braze_plugin/changelog)
- [Unity SDK 10.0.0](https://github.com/braze-inc/braze-unity-sdk/blob/master/CHANGELOG.md)
    - 네이티브 iOS 브리지를 [Braze Swift SDK 12.0.0에서 13.2.0으로](https://github.com/braze-inc/braze-swift-sdk/compare/12.0.0...13.2.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed) 업데이트했습니다. 여기에는 Xcode 26 지원이 포함됩니다.

{% enddetails %}
{% details September 16, 2025 %}

## 2025년 9월 16일 출시

### 데이터 유연성

#### Braze 데이터 플랫폼

Braze 데이터 플랫폼은 고객 생애 주기 전반에 걸쳐 개인화되고 영향력 있는 경험을 창출할 수 있도록 하는 포괄적이고 조합 가능한 데이터 기능 및 파트너 통합 세트입니다. 수행해야 할 세 가지 데이터 관련 작업에 대해 자세히 알아보세요: 

- [데이터 통합]({{site.baseurl}}/user_guide/data/unification)
- [데이터 활성화]({{site.baseurl}}/user_guide/data/activation)
- [데이터 배포]({{site.baseurl}}/user_guide/data/distribution)

#### 사용자 정의 배너 속성

{% multi_lang_include release_type.md release="Early access" %}

배너 캠페인에서 사용자 정의 속성을 사용하여 SDK를 통해 키-값 데이터를 검색하고 앱의 동작이나 모양을 수정할 수 있습니다. 자세한 내용은 [사용자 정의 배너 속성]({{site.baseurl}}/developer_guide/banners/placements/#custom-properties)을 참조하세요.

#### 토큰 인증

{% multi_lang_include release_type.md release="General availability" %}

Braze 연결된 콘텐츠를 사용할 때 특정 API에 사용자 아이디와 비밀번호 대신 토큰이 필요할 수 있습니다. Braze는 [토큰 인증 헤더 값]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/making_an_api_call#using-token-authentication)을 보유하는 자격 증명을 저장할 수 있습니다.

#### 프로모션 코드

사용자 업데이트 단계를 통해 사용자 프로필에 프로모션 코드를 저장할 수 있습니다. 자세한 내용은 [사용자 프로필에 프로모션 코드 저장]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/promotion_codes#save-to-profile)을 참조하세요.

### 창의력 발휘

#### Braze 파일럿

[Braze 파일럿]({{site.baseurl}}/user_guide/getting_started/braze_pilot)은 Braze 대시보드에서 메시지를 휴대폰으로 전송할 수 있는 Android 및 iOS용 공개 앱입니다. 앱 다운로드, Braze 대시보드와의 연결 초기화 및 설정 완료에 대한 안내는 [Braze 파일럿 시작하기]({{site.baseurl}}/user_guide/getting_started/braze_pilot/getting_started)를 확인하세요.

### 새로운 Braze 파트너십

#### 블링스 - 시각적이고 인터랙티브한 콘텐츠

[블링스]({{site.baseurl}}/partners/blings/)는 실시간, 인터랙티브 및 데이터 기반 비디오 경험을 대규모로 제공할 수 있는 차세대 개인화 비디오 플랫폼입니다.

#### Shopify 표준 통합과 타사 도구

Shopify 온라인 상점의 경우, 사이트에서 Braze SDK를 지원하기 위해 Braze의 표준 통합 방법을 사용하는 것이 좋습니다.

그러나 서드파티 도구인 Google 태그 관리자와 같은 도구를 선호할 수 있다는 점을 이해하고, 이를 위한 가이드를 준비했습니다. 시작하려면 [Shopify: 을 참조하세요. 서드파티 태깅]({{site.baseurl}}/shopify_standard_integration_third_party_tagging/).

### SDK 업데이트

다음 SDK 업데이트가 릴리스되었습니다. 주요 업데이트는 아래에 나열되어 있으며, 그 외의 모든 업데이트는 해당 SDK 체인지로그를 확인하면 확인할 수 있습니다.

- [Braze Flutter SDK 15.0.0](https://github.com/braze-inc/braze-flutter-sdk/blob/main/CHANGELOG.md#1500)
    - 네이티브 Android 브릿지를 Braze Android SDK `36.0.0`에서 `39.0.0`로 업데이트합니다.
    - 네이티브 iOS 브릿지를 Braze Swift SDK `12.0.0`에서 `13.2.0`로 업데이트합니다. 여기에는 Xcode 26 지원이 포함됩니다.

- [Braze Swift SDK 7.0.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#1300)
  - 브레이즈 스위프트 SDK 바인딩을 업데이트하여 `13.0.0+` SemVer 디노미네이션의 릴리스가 필요하도록 합니다. 이를 통해 `13.0.0` 에서 `14.0.0` 까지의 모든 버전의 Braze SDK와 호환이 가능합니다.

{% enddetails %}
{% details August 19, 2025 %}

## 2025년 8월 19일 출시

### Canvas Context에 대한 시간대 일관성 표준화

{% multi_lang_include release_type.md release="Early access" %}

[Canvas Context 단계 조기 액세스]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context)에 참여하는 경우, 액션 기반 Canvas의 트리거 이벤트 속성에서 datetime 유형의 모든 타임스탬프는 항상 [UTC](https://en.wikipedia.org/wiki/Coordinated_Universal_Time)로 정규화됩니다. 이와 관련하여 더 알아보려면 [시간대 일관성 표준화]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context#time-zone-consistency-standardization)를 참조하세요.

### 데이터 유연성

#### 셀프 서비스 맞춤 도메인

{% multi_lang_include release_type.md release="General access" %}

[셀프 서비스 맞춤 도메인]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/link_shortening/custom_domains/)을 통해 SMS, RCS 및 WhatsApp을 위한 맞춤 도메인을 Braze 대시보드에서 직접 구성하고 관리할 수 있습니다. 한 곳에서 최대 10개의 맞춤 도메인을 쉽게 추가, 모니터링 및 관리할 수 있습니다.

#### 세그먼트 퍼널 통계

[퍼널 통계 보기]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/#viewing-funnel-statistics)를 선택하여 해당 필터 그룹의 통계를 표시하고 추가된 각 필터가 세그먼트 통계에 미치는 영향을 확인하세요. 해당 시점까지 모든 필터에 의해 타겟팅된 사용자에 대한 예상 수와 비율을 확인할 수 있습니다. 필터 그룹에 대한 통계가 표시되면 필터를 변경할 때마다 자동으로 업데이트됩니다. 

#### 푸시 알림을 위한 `/campaigns/details` 엔드포인트의 새로운 응답 필드

푸시 알림에 대한 `messages` 응답에는 이제 두 개의 새로운 필드가 포함됩니다:

- `image_url`: 안드로이드 알림 이미지, iOS 알림 이미지 또는 웹 푸시 아이콘 이미지의 이미지 URL입니다.
- `large_image_url`: 안드로이드 Chrome 및 Windows 웹 푸시 작업을 위한 웹 알림 이미지 URL입니다.

#### PII 필드 정의

특정 필드를 PII 필드로 선택하고 [정의하는 것]({{site.baseurl}}/user_guide/administrative/app_settings/company_settings/security_settings#view-pii)은 사용자가 Braze 대시보드에서 볼 수 있는 내용에만 영향을 미치며, 이러한 PII 필드의 최종 사용자 데이터 처리에는 영향을 미치지 않습니다.

귀사의 대시보드 설정을 귀사에 적용되는 모든 개인 정보 보호 규정 및 정책과 일치시키기 위해 법무팀에 상담하십시오. 여기에는 [데이터 보존]({{site.baseurl}}/api/data_retention/)과 관련된 규정이 포함됩니다.

#### 보고서 빌더 다운로드 링크 공유

[대시보드 링크 공유]({{site.baseurl}}/user_guide/analytics/reporting/report_builder/#sharing-a-report)를 선택하고 **공유**를 클릭한 다음 **링크 공유** 또는 **이메일 보내기 또는 예약**를 선택하여 보고서를 공유할 수 있습니다.

### 창의력 발휘

#### 드래그 앤 드롭 이메일을 위한 사용자 정의 헤드 태그

이메일 메시지에 CSS 및 메타데이터를 추가하려면 `<head>` 태그를 사용하십시오. 예를 들어, 이러한 태그를 사용하여 스타일시트나 파비콘을 추가할 수 있습니다. Liquid는 `<head>` 태그에서 지원됩니다.

### 강력한 채널

#### 퍼지 옵트아웃 모범 사례

구독자에게 명확하고 준수하며 긍정적인 경험을 제공하기 위해 퍼지 옵트아웃 메시지를 신중하게 구성하는 데 도움이 되는 [모범 사례 섹션]({{site.baseurl}})을 추가했습니다.

#### WhatsApp Flows

{% multi_lang_include release_type.md release="Early access" %}

[WhatsApp 흐름]({{site.baseurl}}/whatsapp_flows/)은 기존 WhatsApp 채널을 향상시켜 상호작용적이고 동적인 메시징 경험을 생성할 수 있게 합니다. 

#### WhatsApp 수신 제품 질문

사용자는 [제품 질문]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/product_messages/#receiving-inbound-product-questions)으로 귀하의 제품 또는 카탈로그 메시지에 응답할 수 있습니다. 이 메시지는 수신 메시지로 도착하며, 이후 작업 경로로 정렬할 수 있습니다.

또한, Braze는 이러한 질문에서 제품 ID와 카탈로그 ID를 추출하므로, 응답을 자동화하거나 다른 팀(예: 고객 지원)으로 질문을 전송하려는 경우 해당 세부정보를 포함할 수 있습니다.

### AI 및 ML 자동화

#### 새로운 BrazeAI™ 사용 사례 기사

BrazeAI™의 활용을 극대화할 수 있도록 새로운 사용 사례 기사를 추가했습니다. 이 가이드는 참여 전략에 AI를 적용하는 실용적인 방법을 강조합니다.

- [예측 이탈]({{site.baseurl}}/user_guide/brazeai/predictive_churn/use_case): 이탈 위험이 있는 고객을 식별하고 조기에 조치를 취하세요.
- [예측 이벤트]({{site.baseurl}}/user_guide/brazeai/predictive_events/use_case): 주요 사용자 행동을 예측하고 실시간으로 경험을 형성하세요.
- [Recommendations]({{site.baseurl}}/user_guide/brazeai/recommendations/use_case ): 고객 행동에 따라 더 관련성 높은 콘텐츠와 제품을 제공합니다.

#### MCP 서버

{% multi_lang_include release_type.md release="Beta" %}

[브레이즈 MCP 서버]({{site.baseurl}}/user_guide/brazeai/mcp_server/)는 안전하고 읽기 전용 연결로, Claude 및 Cursor와 같은 AI 도구가 비개인 식별 정보(PII) 브레이즈 데이터를 접근하여 질문에 답하고, 트렌드를 분석하며, 데이터를 변경하지 않고 통찰력을 제공합니다.

### SDK 업데이트

다음 SDK 업데이트가 릴리스되었습니다. 주요 업데이트는 아래에 나열되어 있으며, 그 외의 모든 업데이트는 해당 SDK 체인지로그를 확인하면 확인할 수 있습니다.

- [Swift SDK 13.0.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md)
    - "선택적" 인증 오류에 대해 트리거되도록 `BrazeSDKAuthDelegate.braze(_:sdkAuthenticationFailedWithError:)`의 기능을 확장합니다.
        - 이제 위임 메서드 `BrazeSDKAuthDelegate.braze(_:sdkAuthenticationFailedWithError:)`는 "필수" 및 "선택적" 인증 오류 모두에 대해 트리거됩니다.
        - "필수" SDK 인증 오류만 처리하려면, 이 위임 메서드의 구현 내에서 `BrazeSDKAuthError.optional`가 false인지 확인하는 검사를 추가하세요.
    - 활성화되면 `Braze.Configuration.sdkAuthentication`의 사용이 적용되도록 수정합니다.
        - 이전에는 이 구성의 값이 SDK에 의해 사용되지 않았으며, 토큰이 존재할 경우 항상 요청에 첨부되었습니다.
        - 이제 SDK는 이 구성이 활성화된 경우에만 SDK 인증 토큰을 외부 네트워크 요청에 첨부합니다.
    - `Braze.FeatureFlag`의 모든 속성과 `Braze.Banner`의 모든 속성에 대한 설정자가 `private`로 변경되었습니다. 이 클래스의 속성은 이제 읽기 전용입니다.
    - 버전 `11.4.0`에서 더 이상 사용되지 않는 `Braze.Banner.id` 속성을 제거합니다.
        - 대신, 배너의 캠페인 추적 ID를 읽기 위해 `Braze.Banner.trackingId`을 사용하세요.
- [React Native SDK 16.0.0](https://github.com/braze-inc/braze-react-native-sdk/blob/master/CHANGELOG.md)
    - 네이티브 Android SDK 버전 바인딩을 [Braze Android SDK 36.0.0에서 37.0.0으로](https://github.com/braze-inc/braze-android-sdk/compare/v36.0.0...v37.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed) 업데이트합니다.
    - 네이티브 Swift SDK 버전 바인딩을 [Braze Swift SDK 12.0.0에서 13.0.0으로](https://github.com/braze-inc/braze-swift-sdk/compare/12.0.0...13.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed) 업데이트합니다.
        - 이 `sdkAuthenticationError` 이벤트는 이제 "필수" 및 "선택적" 인증 오류 모두에 대해 트리거됩니다.
- [Xamarin SDK 7.0.0](https://github.com/braze-inc/braze-xamarin-sdk/blob/7.0.0/CHANGELOG.md)
    - iOS 및 Android 바인딩에 대한 .NET 9.0 지원이 추가되었습니다.
        - 이렇게 하면 .NET 8.0에 대한 지원이 제거됩니다.
        - 이것은 [최소 iOS 12.2 버전](https://learn.microsoft.com/en-us/dotnet/maui/whats-new/dotnet-9?view=net-maui-9.0)을 요구합니다.
    - Android 바인딩을 [Braze Android 32.0.0에서 37.0.0으로](https://github.com/braze-inc/braze-android-sdk/compare/v32.0.0...v37.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed) 업데이트했습니다.
    - iOS 바인딩을 [Braze Swift SDK 10.0.0에서 12.1.0으로](https://github.com/braze-inc/braze-swift-sdk/compare/10.0.0...12.1.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed) 업데이트했습니다.
    - 이 릴리스에는 배너 기능에 대한 API가 포함되어 있지만 현재 이 SDK에서 완전히 지원되지 않습니다. .NET MAUI 앱에서 배너를 사용하려면 애플리케이션에 통합하기 전에 고객 지원 관리자에게 문의하십시오.
- [Cordova SDK 13.0.0](https://github.com/braze-inc/braze-cordova-sdk/blob/master/CHANGELOG.md#1300)
    - 내부 iOS 구현의 `enableSdk` 메서드를 `setEnabled`:를 사용하도록 업데이트했습니다. 이는 Swift SDK에서 더 이상 사용되지 않습니다.
    - 이 메서드를 호출하는 데 더 이상 앱을 다시 시작할 필요가 없습니다. 이 메서드가 실행되면 SDK가 즉시 활성화됩니다.
    - 네이티브 Android 브리지를 [Braze Android SDK `36.0.0`에서 `37.0.0`](https://github.com/braze-inc/braze-android-sdk/compare/v36.0.0...v37.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed)로 업데이트했습니다.

{% enddetails %}
{% details July 22, 2025 %}

## 2025년 7월 22일 출시

### Amazon S3로 보안 이벤트 내보내기

매일 자정 UTC에 실행되는 작업으로 Amazon S3라는 클라우드 스토리지 제공업체에 [보안 이벤트를 자동으로 내보낼 수 있습니다.]({{site.baseurl}}/user_guide/administrative/app_settings/company_settings/security_settings/security_export_s3/) 설정이 완료되면 대시보드에서 보안 이벤트를 수동으로 내보낼 필요가 없습니다.

### 데이터 유연성

#### CSV import

{% multi_lang_include release_type.md release="General availability" %}

CSV 가져오기를 사용하여 Braze에서 `first_name`, `last_destination_searched` 및 `trip_booked`와 같은 사용자 속성과 사용자 정의 이벤트를 기록하고 업데이트할 수 있습니다. To get started, see [CSV Import]({{site.baseurl}}/user_guide/data/user_data_collection/user_import/csv_import).

#### API 사용량 경고

{% multi_lang_include release_type.md release="General availability" %}

API 사용량 경고는 API 사용에 대한 중요한 가시성을 제공하여 예기치 않은 트래픽을 사전에 감지할 수 있도록 합니다. 이러한 경고를 설정하여 주요 API 요청량을 추적하면 실시간 알림을 받고 마케팅 캠페인에 영향을 미치기 전에 문제를 해결할 수 있습니다.

#### 작업 공간 API 속도 제한

작업 공간 API 속도 제한을 사용하면 `/users/track` 또는 SDK 데이터와 같은 특정 수집 엔드포인트에 대해 작업 공간이 만들 수 있는 최대 API 요청 수를 설정할 수 있습니다. 작업 공간 그룹에 속도 제한을 적용할 수도 있으며, 이는 해당 그룹의 모든 작업 공간에서 제한이 공유됨을 의미합니다.

#### 신규 커런츠 이벤트

이 새로운 이벤트가 Currents 용어집에 추가되었습니다:

- [Banner Abort events]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/#banner-abort-events)
- [Banner Click events]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/#banner-click-events)
- [Banner Impression events]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/#banner-impression-events)
- [배너 조회 이벤트]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/#banner-viewed-events)
- [Webhook Failure events]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/#webhook-failure-events)

#### 캠페인 분석의 기본 시간 범위

기본적으로 [**캠페인 분석**]({{site.baseurl}}/user_guide/analytics/reporting/campaign_analytics/)의 시간 범위는 현재 시간으로부터 지난 90일을 표시합니다. 이는 캠페인이 90일 이상 전에 시작된 경우, 주어진 시간 범위에 대해 분석이 "0"으로 표시됨을 의미합니다. 이전 캠페인에 대한 모든 분석을 보려면 보고 시간 범위를 조정하십시오.

#### 캔버스 실험 경로 단계에 대한 업데이트된 동작

캔버스에 활성 또는 진행 중인 [실험]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step)이 있고 활성 캔버스를 업데이트하면(실험 경로 단계가 아니더라도) 진행 중인 실험이 종료됩니다. To restart the experiment, you can disconnect the existing Experiment Path and launch a new one, or duplicate the Canvas and launch a new Canvas. 

For more information, refer to [Editing Canvases after launch]({{site.baseurl}}/post-launch_edits/).

#### `/users/export/ids` 엔드포인트에 대해 더 빠른 속도 제한 사용 가능

다음 요구 사항을 충족하면 [ /users/export/ids 엔드포인트에 대한 속도 제한<1>을 초당 40 요청으로 늘릴 수 있습니다:

- 작업 공간에 기본 속도 제한(분당 250 요청)이 활성화되어 있습니다. 기존 속도 제한을 제거하는 데 추가 지원이 필요하면 Braze 계정 관리자에게 문의하십시오.
- 귀하의 요청에는 수신하려는 모든 필드를 나열하기 위한 fields_to_export 매개변수가 포함되어 있습니다.

#### 이메일 템플릿 엔드포인트에 대한 새 번역

{% multi_lang_include release_type.md release="Early access" %}

이 엔드포인트를 사용하여 이메일 템플릿의 번역 및 로캘을 보고 업데이트할 수 있습니다:

- [가져오기: 소스 번역 보기]({{site.baseurl}}/api/endpoints/translations/email_templates/get_view_source_template)
- [가져오기: 이메일 템플릿 엔드포인트의 특정 번역 및 로캘 보기]({{site.baseurl}}/api/endpoints/translations/email_templates/get_view_translation_locale_template)
- [가져오기: 이메일 템플릿에 대한 모든 번역 및 로캘 보기]({{site.baseurl}}/api/endpoints/translations/email_templates/get_view_translation_template)
- [넣기: 이메일 템플릿에 대한 번역 업데이트]({{site.baseurl}}/api/endpoints/translations/email_templates/put_update_template)

### 창의력 발휘

#### 랜딩 페이지

사용자의 장치 크기에 [반응형으로 만들 수 있습니다]({{site.baseurl}}/user_guide/engagement_tools/landing_pages/creating_pages#step-3-customize-the-page) 작은 화면에서 열을 수직으로 쌓아 올려서. 이를 활성화하려면 반응형으로 만들고 싶은 행에 열을 추가한 다음 **작은 화면에서 수직으로 쌓기**를 **열 사용자 지정** 섹션에서 켭니다.

### 강력한 채널

#### 이메일에 대한 봇 필터링

{% multi_lang_include release_type.md release="General availability" %}

[이메일 환경설정에서]({{site.baseurl}}/user_guide/administrative/app_settings/email_settings) 봇 필터링을 설정하여 의심되는 모든 컴퓨터 또는 봇 클릭을 제외하세요. 이메일에서 '봇 클릭'이란 자동화된 프로그램에 의해 생성된 이메일 내의 하이퍼링크를 클릭하는 것을 말합니다. 이러한 봇 클릭을 필터링하여 참여 중인 수신자에게 의도적으로 메시지를 트리거하고 전달할 수 있습니다.

#### 드래그 앤 드롭 제품 블록

{% multi_lang_include release_type.md release="Early access" %}

[드래그 앤 드롭 편집기]({{site.baseurl}}/dnd_product_blocks/)를 사용하면 사용자 정의 Liquid 코드를 만들 필요 없이 메시지에 제품 블록을 신속하게 추가하고 구성하여 원활한 제품 쇼케이스를 만들 수 있습니다. 드래그 앤 드롭 제품 블록 기능은 현재 이메일에만 제공됩니다.

#### 랜딩 페이지 및 인앱 메시지용 스팬 텍스트

스팬 텍스트를 사용하면 [랜딩 페이지]({{site.baseurl}}/user_guide/engagement_tools/landing_pages/creating_pages/#step-3-customize-the-page) 및 [인앱 메시지]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/style_settings/#blocks)에 대해 사용자 정의 코드 없이 텍스트 블록에 특정 스타일을 적용할 수 있습니다. 이렇게 하려면 스타일을 적용할 텍스트를 강조 표시한 다음 **스타일을 위한 스팬으로 감싸기**를 선택합니다. 

#### WhatsApp으로 클릭하는 광고

[WhatsApp으로 클릭하는 광고]({{site.baseurl}}/whatsapp_use_cases/)는 Facebook, Instagram 또는 기타 플랫폼의 Meta 광고에서 신규 및 기존 고객을 유치하는 효율적인 방법입니다. 이 광고를 사용하여 제품과 서비스를 홍보하고 사용자가 WhatsApp 존재를 인식하도록 합니다. 

### 새로운 Braze 파트너십

#### Shopify 방문자 API — 전자상거래

Braze collects visitor information, such as email addresses and phone numbers, through in-browser messages. This information is then sent to Shopify. This data helps merchants recognize visitors to their store and create a more personalized shopping experience.

#### Okendo — 전자상거래

Braze와 [Okendo]({{site.baseurl}}/partners/okendo/) 통합은 Okendo 플랫폼의 여러 제품에서 작동하며, 여기에는 리뷰, 충성도, 추천, 설문 조사 및 퀴즈가 포함됩니다. Okendo는 Braze에 사용자 정의 이벤트 및 사용자 속성을 전송하며, 이를 사용하여 메시지를 개인화하고 트리거할 수 있습니다.

#### Lemnisk - 고객 데이터 플랫폼

Braze와 [Lemnisk]({{site.baseurl}}/partners/lemnisk/) 통합은 브랜드와 기업이 사용자 데이터를 실시간으로 플랫폼 간에 통합하는 CDP 주도 인텔리전스 레이어로서 Braze의 전체 잠재력을 활용할 수 있도록 합니다. 사용자의 정보와 행동을 실시간으로 Braze에 전송합니다.

### SDK 업데이트

다음 SDK 업데이트가 릴리스되었습니다. 주요 업데이트는 아래에 나열되어 있으며, 그 외의 모든 업데이트는 해당 SDK 체인지로그를 확인하면 확인할 수 있습니다.

- [웹 SDK 6.0.0](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md)
    - `Banner.html` 속성, `logBannerClick` 및 `logBannerImpressions` 메서드를 제거했습니다. 대신 [`insertBanner`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#insertbanner)를 사용하여 노출 및 클릭 추적을 자동으로 처리합니다.
    - 구식 뉴스 피드 기능에 대한 지원이 제거되었습니다. 여기에는 Feed 클래스와 관련된 메서드의 제거가 포함됩니다.
    - 구식 뉴스 피드 카드에서 사용되었던 created 및 categories 필드가 [`Card`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.card.html) 하위 클래스에서 제거되었습니다.
    - linkText 필드도 [`ImageOnly`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.imageonly.html) 카드 하위 클래스와 그 생성자에서 제거되었습니다.
    - 정의가 명확해지고 특정 SDK 메서드가 SDK가 초기화되지 않았을 때 명시적으로 정의되지 않은 값을 반환한다는 점을 주목하여 유형이 업데이트되었습니다. 이는 실제 런타임 동작과 일치합니다. 이로 인해 이전(불완전한) 유형에 의존했던 프로젝트에서 새로운 TypeScript 오류가 발생할 수 있습니다.
    - `cropType`의 `CENTER_CROP` (기본적으로 `FullScreenMessage`와 같은) 인앱 메시지의 이미지는 접근성을 개선하기 위해 `<img>` 태그를 통해 렌더링되며 `<span>` 대신 사용됩니다. 이로 인해 `.ab-center-cropped-img` 클래스 또는 그 자식에 대한 기존 CSS 사용자 정의가 깨질 수 있습니다.
- [Cordova SDK 13.0.0](https://github.com/braze-inc/braze-cordova-sdk/blob/master/CHANGELOG.md#1300)
    - Swift SDK에서 더 이상 사용되지 않는 `_requestEnableSDKOnNextAppRun` 대신 setEnabled:를 사용하도록 `enableSdk` 메서드의 내부 iOS 구현이 업데이트되었습니다.
        - 이 메서드를 호출하는 데 더 이상 앱을 다시 시작할 필요가 없습니다. 이 메서드가 실행되면 SDK가 즉시 활성화됩니다.
    - 네이티브 Android 브리지를 [Braze Android SDK 36.0.0에서 37.0.0으로](https://github.com/braze-inc/braze-android-sdk/compare/v36.0.0...v37.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed) 업데이트했습니다.
- [Android SDK 37.0.0](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md)
- [Swift SDK 12.0.1-12.1.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md)

{% enddetails %}

---
nav_title: 플랫폼 개요
article_title: 플랫폼 개요
page_order: 1
description: "이 문서에서는 Braze 플랫폼의 기본적인 부분과 기능에 대해 설명합니다. 이 문서의 링크는 필수 Braze 주제로 연결됩니다."
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

# [![Braze 학습 과정]](https://learning.braze.com/path/developer)({% image_buster /assets/img/bl_icon3.png %}){: style="float:right;width:120px;border:0;" class="noimgborder"}시작하기: 플랫폼 개요

> 이 문서에서는 Braze 플랫폼의 기본적인 부분과 기능에 대해 설명합니다. 이 문서의 링크는 필수 Braze 주제로 연결됩니다. 

{% alert tip %}
이 글과 함께 무료 [개발자 학습 경로](https://learning.braze.com/path/developer) 과정을 확인해 보세요.
{% endalert %}

## Braze란 무엇인가요?

Braze는 고객 참여 플랫폼입니다. 즉, Braze는 사용자의 말을 경청하고 사용자의 행동과 행동을 이해한 다음 그에 따라 행동할 수 있도록 도와줍니다. Braze 플랫폼은 SDK, 대시보드, REST API와 같은 세 가지 주요 구성요소를 포함합니다.

Braze에 대한 보다 일반적인 개요를 찾고 있는 마케터라면, [마케터를 위한 시작하기 섹션]({{site.baseurl}}/user_guide/getting_started/overview/)을 참조하세요.

![Braze에는 다양한 레이어가 있습니다. 전체적으로 SDK, API, 대시보드, 파트너 통합으로 구성되어 있습니다. 각각 데이터 수집 레이어, 분류 레이어, 오케스트레이션 레이어, 개인화 레이어 및 작업 레이어의 일부에 기여합니다. 액션 레이어에는 푸시, 인앱 메시지, 커넥티드 카탈로그, 웹훅, SMS, 이메일 등 다양한 채널이 있습니다.]({% image_buster /assets/img/getting-started/getting-started-vertically-integrated-stack.png %}){: style="max-width:55%;float:right;margin-left:15px;"}

### SDK

[Braze SDK](#integrating-braze)는 모바일 및 웹 애플리케이션에 통합되어 강력한 마케팅, 사용자 관리 및 분석 툴을 제공할 수 있습니다.

간단히 말해, 완전히 통합되면 SDK는 다음을 지원합니다.

* 사용자 데이터를 수집하여 통합된 사용자 프로필로 동기화합니다.
* 세션 데이터, 기기 정보, 푸시 토큰 자동 수집
* 마케팅 인게이지먼트 데이터 및 비즈니스 특정 커스텀 데이터 캡처
* 보안을 고려한 설계 및 서드파티에서 침투 테스트 완료
* 배터리가 부족하거나 네트워크 속도가 느린 장치에 최적화되어 있습니다.
* 보안 강화를 위한 서버 측 JWT 서명 지원
* 시스템에 대한 쓰기 전용 액세스 권한 보유(사용자 데이터 검색 불가)
* 푸시 알림, 인앱 메시지 및 콘텐츠 카드 메시징 채널 지원

### 대시보드 사용자 인터페이스

대시보드는 Braze 플랫폼의 중심에서 모든 데이터 및 상호작용을 제어하는 UI입니다. 마케터는 대시보드를 사용하여 업무를 수행하고 콘텐츠를 제작합니다. 개발자는 대시보드를 사용하여 API 키 및 푸시 알림 자격 증명과 같은 앱 통합을 위한 설정을 관리합니다.

이제 막 시작했다면 팀 관리자가 [대시보드에 사용자]({{site.baseurl}}/user_guide/administrative/access_braze)로 본인 및 Braze에 액세스해야 하는 다른 모든 팀원을 추가해야 합니다.

### REST API

Braze API를 사용하면 대규모로 데이터를 Braze 안팎으로 이동할 수 있습니다. API를 사용하여 백엔드, 데이터 웨어하우스 및 기타 퍼스트파티 및 서드파티 소스에서 업데이트를 가져옵니다. 또한 API를 사용하여 웹 기반 애플리케이션에서 직접 세분화 목적으로 커스텀 이벤트를 추가할 수 있습니다. API를 통해 메시지를 트리거하고 발송할 수 있으므로 기술 리소스에서 캠페인의 일부로 복잡한 JSON 메타데이터를 포함할 수 있습니다.

또한 API는 모바일 및 웹 SDK가 아닌 HTTP를 통해 사용자가 직접 수행한 작업을 기록할 수 있는 웹 서비스도 제공합니다. 웹훅과 결합하면 앱 경험 안팎에서 사용자의 작업을 추적하고 활동을 트리거할 수 있습니다. [API 가이드]({{site.baseurl}}/api/home)에는 사용 가능한 Braze API 엔드포인트와 해당 용도가 나열되어 있습니다.

Braze의 일부와 해당 구성요소에 대한 자세한 내용은 다음을 참조하세요. [시작하기: 아키텍처 개요]({{site.baseurl}}/developer_guide/getting_started/architecture_overview/).

## 데이터 분석 및 조치

Braze에 저장된 데이터는 Braze 고객인 동안 보관되고 세분화, 개인화 및 타겟팅에 사용할 수 있습니다. 이를 통해 해당 정보를 더 이상 사용하지 않도록 선택할 때까지 고객 프로필 데이터(예: 세션 활동 또는 구매)에 대한 조치를 취할 수 있습니다. 예를 들어, 스트리밍 서비스에서는 각 가입자가 서비스 가입 첫날(수년 전일지라도)부터 시청한 콘텐츠를 추적하고 해당 데이터를 사용하여 관련 메시지를 전달할 수 있습니다.

!['최근 구매자'라는 Braze 대시보드의 세그먼트가 휴대폰 화면 옆에 나란히 표시된 'Linda의 상위 추천' 이메일.]({% image_buster /assets/img/getting-started/getting-started-segment.png %}){: style="max-width:80%"}

### 앱 분석

Braze 대시보드에는 애플리케이션에서 계측하는 커스텀 이벤트뿐만 아니라 다양한 분석 측정기준을 기반으로 실시간 업데이트되는 그래프가 표시됩니다. A/B 테스트, 맞춤형 보고 및 분석, 자동화된 인텔리전스를 통해 캠페인을 일관되게 측정하고 최적화하면 고객의 참여를 유지하고 업계 내 경쟁업체와 차별화할 수 있습니다.

### 사용자 세분화

세분화를 사용하면 인앱 행동, 인구 통계 데이터 등의 강력한 필터를 기반으로 사용자 그룹을 생성할 수 있습니다. 또한, 원하는 동작이 기본적으로 캡처되지 않는 경우 Braze에서는 인앱 사용자 작업을 '커스텀 이벤트'로 정의할 수 있습니다. "사용자 지정 속성"을 통한 사용자 특성도 마찬가지입니다. 대시보드에 사용자 세그먼트가 생성되면 사용자가 정의된 기준을 충족하거나 충족하지 못할 때 세그먼트 안팎으로 이동하게 됩니다. 예를 들어, 인앱에서 돈을 지출하고 마지막으로 앱을 사용한 지 2주가 넘은 모든 사용자를 포함하는 세그먼트를 생성할 수 있습니다.

데이터 모델에 대한 자세한 내용은 여기를 확인하세요: [시작하기: 애널리틱스 개요]({{site.baseurl}}/developer_guide/getting_started/architecture_overview/).

## 멀티 채널 메시징

세그먼트를 정의한 후에는 Braze 메시징 툴을 사용하여 역동적이고 개인화된 방식으로 사용자의 참여를 유도할 수 있습니다. Braze는 채널에 구애받지 않는 사용자 중심의 데이터 모델로 설계되었습니다. 메시징은 앱 또는 사이트 내부(예: 인앱 메시지 전송 또는 콘텐츠 카드 캐러셀 및 배너와 같은 그래픽 요소를 통해) 또는 앱 경험 외부(예: 푸시 알림 또는 이메일 전송)에서 이루어집니다. 예를 들어, 마케팅 담당자는 이전 섹션에서 정의한 예시 세그먼트에 푸시 알림과 이메일을 보낼 수 있습니다.

![앱이나 웹사이트 외부 또는 내부의 모든 채널에서 개인화된 메시지를 생성하고 트리거할 수 있습니다.]({% image_buster /assets/img/getting-started/messaging-channels.png %}){: style="border:none" }

| 채널                                                                                              | 설명                                                                                                                                            |
| ---------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [콘텐츠 카드]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/about/)* | 고객을 방해하지 않고 고도로 타겟팅된 동적 인앱 알림을 전송하세요. |
| [이메일]({{site.baseurl}}/user_guide/message_building_by_channel/email/about/) | 서식 있는 텍스트 편집기, 드래그 앤 드롭 편집기를 사용하거나 기존 HTML 템플릿 중 하나를 업로드하여 이메일을 작성하여 서식 있는 HTML 메시지를 전송하세요. |
| [인앱 메시지]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/about/) | Braze의 맞춤형 기본 사용자 인터페이스를 사용하여 눈에 거슬리지 않는 인앱 알림을 전송하세요. |
| [푸시]({{site.baseurl}}/user_guide/message_building_by_channel/push/about/) | iOS용 애플 푸시 알림 서비스(APN)나 Android용 Firebase 클라우드 메시징(FCM)을 사용하여 메시징 캠페인이나 뉴스 항목에서 푸시 알림을 자동으로 트리거합니다. |
| [SMS, MMS, and RCS]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs)* | SMS, MMS 또는 RCS를 사용하여 거래 알림을 보내고, 프로모션을 공유하고, 알림을 보내고, 그 이상을 수행하세요. |
| [웹 푸시]({{site.baseurl}}/user_guide/message_building_by_channel/push/web) | 사용자가 현재 사이트에서 활성 상태가 아니더라도 웹 브라우저 알림을 전송합니다. |
| [웹훅]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/understanding_webhooks/) | 웹훅을 사용하여 앱 이외의 작업을 트리거해 다른 시스템 및 애플리케이션에 실시간 데이터를 제공합니다. |
| [WhatsApp*]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/) | 인기 있는 P2P 메시징 플랫폼을 활용하여 사용자 및 고객과 직접 소통하세요: WhatsApp. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

<sup>\*\*추가 기능으로 제공됩니다.*</sup>

### 사용자 지정 가능한 구성 요소

{% gallery %}
{{site.baseurl}}/assets/img/getting-started/crawl-example.png <br> 모든 Braze 구성요소는 접근성, 적응성 및 사용자 지정이 가능하도록 제작되었습니다. 기본 `BrazeUI` 구성 요소를 사용하고 브랜드 요구 사항과 사용 사례에 맞게 사용자 지정하여 Braze를 시작할 수 있습니다.
{{site.baseurl}}/assets/img/getting-started/walk-example.png <br> 기본 옵션 외에도 메시지 채널의 모양과 느낌을 브랜드에 더 부합하도록 업데이트하는 커스텀 코드를 작성할 수 있습니다. 여기에는 구성요소의 글꼴 유형, 글꼴 크기 및 색상 변경이 포함됩니다. 마케터는 Braze 대시보드에서 직접 오디언스, 콘텐츠, 클릭 시 동작 및 만료를 관리할 수 있습니다.
{{site.baseurl}}/assets/img/getting-started/run-example.png <br> 또한 완전한 커스텀 구성요소를 생성하여 메시징의 모양, 작동 방식, 다른 메시징 채널과의 상호 작용 방식(예: 푸시 알림을 기반으로 콘텐츠 카드 트리거)을 제어할 수도 있습니다. Braze는 노출 횟수, 클릭, 해제와 같은 측정기준을 Braze 대시보드에 기록할 수 있는 SDK 메서드를 제공합니다. 각 메시징 채널에는 이 작업을 용이하게 수행하는 데 도움이 되는 분석 문서가 있습니다.
{% endgallery %}

<br>
<br>

## Braze 통합

Braze는 빠르고 쉽게 시작하고 실행할 수 있도록 설계되었습니다. 수백 개의 브랜드로 구성된 고객 기반에서 평균 가치 실현 시간은 6주입니다. 통합 프로세스에 대한 자세한 내용은 여기를 참조하세요: [시작하기: 통합 개요]({{site.baseurl}}/developer_guide/getting_started/integration_overview/).

## 북마크에 추가할 리소스

기술 리소스로, Braze의 많은 부분에 참여할 수 있습니다. 다음은 설명서 외부에서 북마크에 추가할 수 있는 좋은 리소스입니다. 앞으로 Braze를 사용하면서 용어에 대해 궁금한 점이 있을 때를 대비해 [관련 용어]({{site.baseurl}}/user_guide/getting_started/terms_to_know/) 용어집을 잘 보관해 두세요.

| 리소스 | 학습 내용|
|---|---|
| [SDK 디버깅]({{site.baseurl}}/developer_guide/sdk_integration/debugging) | 통합 문제를 해결할 때, SDK 디버깅 툴이 유용한 도구가 될 것입니다. 항상 준비해 두세요! |
| [Braze 공용 GitHub](https://github.com/braze-inc/) | 자세한 통합 정보와 샘플 코드는 GitHub 리포지토리에서 확인할 수 있습니다. |
| [Android SDK GitHub 리포지토리](https://github.com/braze-inc/braze-android-sdk/) | Android SDK GitHub 리포지토리. |
| [Android SDK 참조](https://appboy.github.io/appboy-android-sdk/kdoc/index.html) | Android SDK용 클래스 문서입니다. |
| [iOS(Swift) SDK GitHub 리포지토리](https://github.com/braze-inc/braze-swift-sdk) | Swift SDK GitHub 리포지토리. |
| [iOS(Swift) SDK 참조](https://braze-inc.github.io/braze-swift-sdk/) | iOS SDK용 클래스 문서입니다. |
| [웹 SDK GitHub 리포지토리](https://github.com/braze-inc/braze-web-sdk) | 웹 SDK GitHub 리포지토리. |
| [웹 SDK 참조](https://js.appboycdn.com/web-sdk/5.0/doc/modules/braze.html) | iOS SDK용 클래스 문서입니다. |
| [SDK 변경 로그]({{site.baseurl}}/developer_guide/changelogs) | Braze는 중요한 문제와 주요 OS 업데이트에 대한 릴리스 외에도 매월 예측 가능한 릴리스를 제공합니다. |
| [Braze API 우편배달부 컬렉션](https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest) | 여기에서 Postman 컬렉션을 다운로드하세요.  |
| [Braze 시스템 상태 모니터](https://braze.statuspage.io/) | 상태 페이지는 인시던트나 장애가 발생할 때마다 업데이트됩니다. 알림을 구독하려면 이 페이지로 이동하세요. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


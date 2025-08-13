---
nav_title: 세그먼트
article_title: 세그먼트
page_order: 1
alias: /partners/segment/
description: "이 참조 문서에서는 마케팅 스택의 소스 간에 정보를 수집하고 라우팅하는 고객 데이터 플랫폼인 Braze와 Segment 간의 파트너십에 대해 간략하게 설명합니다."
page_type: partner
search_tag: Partner

---

# 세그먼트

{% multi_lang_include video.html id="RfOHfZ34hYM" align="오른쪽" %}

> [Segment][5]는 고객 데이터를 수집, 정리 및 활성화하는 데 도움이 되는 고객 데이터 플랫폼입니다. 

Braze와 Segment 통합을 통해 사용자를 추적하고 다양한 사용자 분석 공급자로로 데이터를 라우팅할 수 있습니다. Segment를 통해 다음이 가능합니다.

- Braze 캠페인 및 캔버스 세분화에서 사용할 수 있도록 [Segment Enage]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/segment/segment_engage/)를 Braze에 동기화합니다.
- [두 플랫폼에서 데이터를 가져옵니다](#integration-options). We offer a side-by-side SDK integration for your Android, iOS, and web applications and a server-to-server integration for syncing your data to the Braze REST APIs
- [전류를 통해 데이터를 세그먼트에 연결합니다]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/segment/segment_for_currents/). 

## 전제 조건

| 요구 사항 | 설명 |
| ----------- | ----------- |
| Segment 계정 | 이 파트너십을 이용하려면 [세그먼트 계정이](https://app.segment.com/login) 필요합니다. |
| 설치된 소스 및 세그먼트 소스 [라이브러리](https://segment.com/docs/sources/) | 모바일 앱, 웹사이트 또는 백엔드 서버 등 Segment로 전송된 모든 데이터의 출처.<br><br>성공적인 `Source > Destination` 흐름을 설정하려면 먼저 앱, 사이트 또는 서버에 라이브러리를 설치해야 합니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 통합

Braze와 Segment를 통합하려면 [선택한 통합 유형](#integration-options)(연결 모드)에 따라 [Braze를 대상](#connection-settings)으로 설정해야 합니다. Braze를 처음 사용하는 고객이라면 [세그먼트 리플레이를](#segment-replays) 사용하여 과거 데이터를 Braze에 전달할 수 있습니다. 다음으로, [매핑](#methods)을 설정하고 [통합을 테스트](#step-4-test-your-integration)하여 Braze와 Segment 간 원활한 데이터 흐름을 보장해야 합니다.

### 1단계: Braze 대상 생성 {#connection-settings}

소스를 성공적으로 설정한 후에는 각 소스(iOS, Android, 웹 등)에 대해 Braze를 [대상](https://segment.com/docs/destinations/)으로 구성해야 합니다. 연결 설정을 사용하여 Braze와 세그먼트 간의 데이터 흐름을 사용자 지정할 수 있는 다양한 옵션이 있습니다.

### 2단계: 대상 프레임워크 및 연결 유형 선택 {#integration-options}

In Segment, navigate to **Destinations** > **Braze** > **Configure Braze** > **Select your Source** > **Setup**.

![소스 설정 페이지입니다. 이 페이지에는 대상 프레임워크를 '작업' 또는 '클래식'으로 설정하고 연결 모드를 '클라우드 모드' 또는 '기기 모드'로 설정하는 설정이 포함되어 있습니다.][42]

Segment의 웹 소스(Analytics.js)와 기본 클라이언트 측 라이브러리를 나란히(디바이스 모드) 통합하거나 서버 대 서버(클라우드 모드) 통합을 사용하여 Braze와 통합할 수 있습니다.

연결 모드 선택은 대상이 구성된 소스 유형에 따라 결정됩니다.

| 통합 | 세부 정보 |
| ----------- | ------- |
| [병렬<br>(기기 모드)](#side-by-side-sdk-integration) |Uses Segment's SDK to translate events into Braze native calls, allowing access to deeper features and more comprehensive usage of Braze than the server-to-server integration.<br><br>Segment는 일부 Braze 메서드(예: 콘텐츠 카드)를 지원하지 않습니다. 해당 매핑을 통해 매핑되지 않은 Braze 메서드를 사용하려면 코드베이스에 네이티브 Braze 코드를 추가하여 메서드를 호출해야 합니다. |
| [서버 간<br>(클라우드 모드)](#server-to-server-integration) | 세그먼트에서 Braze REST API 엔드포인트로 데이터를 전달합니다.<br><br>인앱 메시징, 콘텐츠 카드 또는 푸시 알림과 같은 Braze UI 기능을 지원하지 않습니다. 또한 이 메서드를 통해 사용할 수 없는 기기 수준 필드와 같이 자동으로 캡처된 데이터도 존재합니다.<br><br>이러한 기능을 사용하려면 병렬 통합을 고려하세요.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert note %}
[Segment](https://segment.com/docs/destinations/#connection-modes)를 방문하여 두 가지 통합 옵션(연결 모드) 및 각 옵션의 장점에 대해 자세히 알아보세요.
{% endalert %}

#### SDK 병렬 통합

기기 모드라고도 하는 이 통합은 Segment의 SDK와 [메소드](#methods)를 Braze SDK에 매핑하여 푸시, 인앱 메시징 및 기타 Braze의 기본 메서드 등 SDK가 제공하는 모든 기능에 액세스할 수 있도록 지원합니다. 

{% alert note %}
Segment의 기기 모드를 사용할 때는 Braze SDK를 직접 통합할 필요가 없습니다. Segment의 기기 모드 대상으로 Braze를 추가하면 Segment SDK가 Braze SDK를 초기화하고 매핑된 관련 Braze 메서드를 호출합니다.
{% endalert %}

기기 모드 연결을 사용하는 경우, 기본적으로 Braze SDK 통합과 마찬가지로 Braze SDK는 모든 사용자에게 `device_id` 및 백엔드 식별자(`braze_id`)를 할당합니다. 이를 통해 Braze는 `userId` 대신 해당 식별자를 일치시켜 기기에서 익명의 활동을 캡처할 수 있습니다. 

{% tabs local %}
{% tab Android %}

{% alert important %}
Android 기기 모드 통합을 위한 소스 코드는 Braze에서 관리하며, 새로운 Braze SDK 릴리스를 반영하기 위해 정기적으로 업데이트됩니다.

<br>
사용하는 Braze SDK는 사용하는 Segment SDK에 따라 달라집니다.

| | Segment SDK | Braze SDK |
| - | ----------- | --------- |
| 기본 설정 | [애널리틱스-코틀린](https://github.com/segmentio/analytics-kotlin) | [브레이즈 세그먼트 Kotlin](https://github.com/braze-inc/braze-segment-kotlin) |
레거시 | [애널리틱스-안드로이드](https://github.com/segmentio/analytics-android) | [브레이즈 세그먼트 안드로이드 | 브레이즈 세그먼트 안드로이드](https://github.com/braze-inc/braze-segment-android) |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }


{% endalert %}

To set up Braze as a device-mode destination for your Android source, choose **Actions** as the **Destination framework**, then select **Save**. 

나란히 통합을 완료하려면 [Android](https://segment.com/docs/connections/sources/catalog/libraries/mobile/kotlin-android/destination-plugins/braze-kotlin-android/) 앱에 Braze 대상 종속성을 추가하기 위한 Segment의 자세한 지침을 참조하세요.

[Android 디바이스 모드](https://github.com/braze-inc/braze-segment-kotlin) 통합을 위한 소스 코드는 Braze에서 관리하며 새로운 Braze SDK 릴리스를 반영하기 위해 정기적으로 업데이트됩니다.

{% endtab %}
{% tab iOS %}

{% alert important %}
iOS 기기 모드 통합을 위한 소스 코드는 Braze에서 관리하며, 새로운 Braze SDK 릴리스를 반영하기 위해 정기적으로 업데이트됩니다.

<br>
사용하는 Braze SDK는 사용하는 Segment SDK에 따라 달라집니다.

| | Segment SDK | Braze SDK |
| - | ----------- | --------- |
| 기본 | [Analytics-Swift](https://github.com/segmentio/analytics-swift) | [Braze Segment Swift](https://github.com/braze-inc/braze-segment-swift) |
| 레거시 | [애널리틱스-iOS](https://github.com/segmentio/analytics-ios) | [브레이즈 세그먼트 iOS](https://github.com/Appboy/appboy-segment-ios) |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }
{% endalert %}

To set up Braze as a device-mode destination for your iOS source, choose **Actions** as the **Destination framework**, then select **Save**. 

병렬 통합을 완료하려면 [iOS](https://segment.com/docs/connections/sources/catalog/libraries/mobile/apple/destination-plugins/braze-swift/) 앱에 Braze Segment 포드를 추가하는 방법에 대한 자세한 지침을 참조하세요.

[iOS 디바이스 모드](https://github.com/braze-inc/braze-segment-swift) 통합을 위한 소스 코드는 Braze에서 관리하며 새로운 Braze SDK 릴리스를 반영하기 위해 정기적으로 업데이트됩니다.

{% endtab %}
{% tab 웹 또는 자바스크립트 %}

Segment's Braze Web Mode (Actions) framework is recommended for setting up Braze as a device-mode destination for your web source. 

In Segment, select **Actions** as your destination framework and **Device Mode** as your connection mode.

![]({% image_buster /assets/img/segment/website.png %})

{% endtab %}
{% tab React Native %}
[React Native Braze 플러그인](https://github.com/segmentio/analytics-react-native/tree/master/packages/plugins/plugin-braze)의 소스 코드는 Segment에서 관리하며, 새로운 Braze SDK 릴리스를 반영하기 위해 정기적으로 업데이트됩니다.

React Native Segment 소스를 Braze에 연결할 때 운영 체제별로 소스 및 대상을 설정해야 합니다. 예를 들어 iOS 대상과 Android 대상을 설정합니다. 

앱 코드베이스 내에서 각 앱과 연결된 각각의 소스 쓰기 키를 사용하여 기기 유형별로 Segment SDK를 조건부로 초기화합니다.

기기에서 푸시 토큰이 등록되어 Braze로 전송되면, SDK를 초기화할 때 사용된 앱 식별자와 연결됩니다. 기기 유형 조건부 초기화는 Braze로 전송된 모든 푸시 토큰이 관련 앱과 연결되어 있는지 확인하는 데 도움이 됩니다.

{% alert important %}
React Native 앱이 모든 기기에 대해 동일한 Braze 앱 식별자로 Braze를 초기화하면 모든 React Native 사용자는 Braze에서 Android 또는 iOS 사용자로 간주되며 모든 푸시 토큰은 해당 운영 체제와 연결됩니다.
{% endalert %}

To set up Braze as a device-mode destination for each source, choose **Actions** as the **Destination framework**, then select **Save**.

{% endtab %}
{% endtabs %}

#### 서버 간 통합

Also called cloud-mode, this integration forwards data from Segment to the Braze REST APIs. Use Segment's [Braze Cloud Mode (Actions)](https://segment.com/docs/connections/destinations/catalog/braze-cloud-mode-actions/) framework to set up a cloud-mode destination for any of your sources. 

Unlike the side-by-side integration, the server-to-server integration does not support Braze UI features, such as in-app messaging, Content Cards, or automatic push token registration. 클라우드 모드에서는 사용할 수 없는 [자동 캡처]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/#user-data-collection)된 데이터(예: 익명 사용자 및 기기 수준 필드)도 존재합니다.

이 데이터와 이러한 기능을 사용하려면 SDK 병렬 통합(기기 모드)을 사용하는 것이 좋습니다.

[Braze 클라우드 모드(작업) 대상](https://github.com/segmentio/action-destinations/tree/main/packages/destination-actions/src/destinations/braze)의 소스 코드는 Segment에서 유지 관리합니다.

### 3단계: 설정

대상에 대한 설정을 정의합니다. 모든 설정이 모든 대상 유형에 적용되는 것은 아닙니다.

{% tabs local %}
{% tab 모바일 장치 모드 %}

| 설정 | 설명 |
| ------- | ----------- |
| 앱 식별자 | 특정 앱을 참조하는 데 사용되는 앱 식별자입니다. **설정 관리** 아래의 Braze 대시보드에서 확인할 수 있습니다. | 
| 사용자 지정 API 엔드포인트<br>(SDK 엔드포인트) | 인스턴스에 해당하는 Braze SDK 엔드포인트(예: `sdk.iad-01.braze.com`) | 
| 엔드포인트 지역 | Braze 인스턴스(예: 미국 01, 미국 02, 유럽 01 등) | 
| 자동 인앱 메시지 등록 활성화 | 인앱 메시지를 수동으로 등록하려면 이 기능을 비활성화하세요. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab 웹 기기 모드 %}

| 설정 | 설명 |
| ------- | ----------- |
| 앱 식별자 | 특정 앱을 참조하는 데 사용되는 앱 식별자입니다. **설정 관리** 아래의 Braze 대시보드에서 확인할 수 있습니다. | 
| 사용자 지정 API 엔드포인트<br>(SDK 엔드포인트) | 인스턴스에 해당하는 Braze SDK 엔드포인트(예: `sdk.iad-01.braze.com`) | 
| Safari 웹사이트 푸시 ID | Safari 푸시를 지원하는 경우, Safari 푸시 인증서를 생성할 때 Apple에 제공한 웹사이트 푸시 ID(`web`으로 시작, 예: `web.com.example.domain`)로 이 옵션을 지정해야 합니다. |
| Braze 웹 SDK 버전 | 사용하려는 Braze 웹 SDK 버전 |
| 인앱 메시지 자동 전송 | 기본적으로 사용자가 받을 수 있는 모든 인앱 메시지가 사용자에게 자동으로 전달됩니다. 인앱 메시지를 수동으로 표시하려면 이 기능을 비활성화합니다. |
| Font Awesome 로드 안 함 | Braze는 앱 내 메시지 아이콘에 Font Awesome을 사용합니다. 기본적으로 Braze는 FontAwesome CDN에서 FontAwesome을 자동으로 로드합니다. 이 동작을 비활성화하려면(예: 사이트에서 사용자 지정 버전의 FontAwesome을 사용하는 경우) 이 옵션을 `TRUE`로 설정합니다. 이 작업을 수행하는 경우 사이트에 FontAwesome이 로드되었는지 확인할 책임이 사용자에게 있습니다. 그렇지 않으면 인앱 메시지가 올바르게 렌더링되지 않을 수 있습니다. |
| HTML 인앱 메시지 활성화 | 이 옵션을 활성화하면 Braze 대시보드 사용자가 HTML 인앱 메시지를 사용할 수 있습니다. | 
| 새 탭에서 인앱 메시지 열기 | 기본적으로 인앱 메시지 클릭의 링크는 메시지별로 대시보드에 지정된 대로 현재 탭 또는 새 탭에 로드됩니다. 이 옵션을 `TRUE`로 설정하면 인앱 메시지 클릭의 모든 링크가 새 탭 또는 창에서 강제로 열립니다. |
| 인앱 메시지 z 인덱스 | Provide a value for this option to override the Braze default z-indexes. | 
| 명시적인 인앱 메시지 해제 요구 | 기본적으로 인앱 메시지가 표시될 때 이스케이프 버튼을 누르거나 페이지의 회색 배경을 클릭하면 메시지가 해제됩니다. 이 옵션을 true로 설정하여 이 동작을 방지하고 메시지를 해제하려면 명시적으로 버튼을 클릭하도록 요구합니다. |
| 트리거 동작 간 최소 간격(초) | 기본값은 30입니다.<br>기본적으로 트리거 동작은 마지막 트리거 동작 이후 최소 30초가 경과한 경우에만 실행됩니다. 이 구성 옵션에 값을 제공하여 기본값을 사용자 지정 값으로 재정의합니다. 사용자에게 스팸 알림을 보내지 않으려면 이 값을 10보다 작게 설정하지 않는 것이 좋습니다.|
| 서비스 종사자 위치 | 기본적으로 웹 푸시 알림을 위해 사용자를 등록할 때 Braze는 웹 서버의 루트 디렉토리(`/service-worker.js`)에서 필요한 서비스 종사자 파일을 찾습니다. 해당 서버의 다른 경로에서 서비스 종사자를 호스팅하려면 이 옵션에 파일의 절대 경로인 값(예: `/mycustompath/my-worker.js`)을 제공합니다. 여기에서 값을 설정하면 사이트에서 푸시 알림의 범위가 제한됩니다. 예를 들어 위의 예제에서 서비스 종사자 파일은 `/mycustompath/` 디렉토리에 있으므로 `requestPushPermission`은 `http://yoursite.com/mycustompath/`로 시작하는 웹 페이지에서만 호출할 수 있습니다. |
| 푸시 토큰 유지 관리 비활성화 | 기본적으로 웹 푸시 권한을 이미 부여한 사용자는 새 세션에서 푸시 토큰을 Braze 백엔드와 자동으로 동기화하여 전달 가능성을 보장합니다. 이 동작을 비활성화하려면 이 옵션을 `FALSE` 로 설정합니다. |
| 외부에서 서비스 종사자 관리 | 사용자가 등록하고 생애주기를 제어하는 자체 서비스 종사자가 있는 경우 이 옵션을 `TRUE`로 설정하면 Braze SDK는 서비스 종사자를 등록하거나 등록 취소하지 않습니다. If you set this option to `TRUE`, for push to function correctly, you must register the service worker yourself before calling `requestPushPermission` and ensure that it contains the Braze service worker code, either with `self.importScripts('https://js.appboycdn.com/web-sdk-develop/4.1/service-worker.js');` or by including the content of that file directly. 이 옵션이 `TRUE`인 경우 `serviceWorkerLocation` 옵션은 관련이 없으며 무시됩니다. |
| 콘텐츠 보안 nonce | 이 옵션에 값을 제공하면 Braze SDK는 SDK에서 생성한 `<script>` 및 `<style>` 요소에 nonce를 추가합니다. 이렇게 하면 Braze SDK가 웹사이트의 콘텐츠 보안 정책과 함께 작동할 수 있습니다. 이 nonce를 설정하는 것 외에도 콘텐츠 보안 정책 허용 목록에 `use.fontawesome.com`을 추가하거나 `doNotLoadFontAwesome` 옵션을 사용하고 수동으로 로드하여 FontAwesome을 로드하도록 허용해야 할 수도 있습니다. |
| 크롤러 활동 허용 | 기본적으로 Braze 웹 SDK는 사용자 에이전트 문자열을 기반으로 알려진 스파이더 또는 Google과 같은 웹 크롤러의 활동을 무시합니다. 이렇게 하면 데이터 포인트가 절약되고 분석이 더 정확해지며 페이지 순위가 향상될 수 있습니다. 그러나 Braze에서 이러한 크롤러의 활동을 대신 기록하려면 이 옵션을 `TRUE`로 설정할 수 있습니다. |
| 로깅 사용 | 기본적으로 로깅을 활성화하려면 `TRUE`로 설정합니다. 이렇게 하면 JavaScript 콘솔에 Braze가 기록되고, 모든 사용자가 볼 수 있습니다. 페이지를 프로덕션에 릴리스하기 전에 이 기능을 제거하거나 `setLogger`로 대체 로거를 제공해야 합니다. |
| 새 탭에서 뉴스피드 카드 열기(새 탭에서 카드 열기) | 기본적으로 카드 개체의 링크는 현재 탭 또는 창에 로드됩니다. 카드의 링크를 새 탭이나 창에서 열려면 이 옵션을 `TRUE` 으로 설정합니다. <br><br>**참고:** 뉴스피드는 사용 중지될 예정입니다. Braze는 뉴스피드 도구를 사용하는 고객에게 보다 유연하고 맞춤 설정이 가능하며 안정적인 콘텐츠 카드 메시징 채널로 전환할 것을 권장합니다. 자세한 내용은 [마이그레이션 가이드를]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/migrating_from_news_feed/) 확인하세요. |
| 사용자 제공 자바스크립트 허용 | 기본적으로 Braze 웹 SDK는 사용자가 제공한 JavaScript 클릭 동작을 허용하지 않습니다. 이 경우 Braze 대시보드 사용자가 사이트에서 JavaScript를 실행할 수 있도록 허용하기 때문입니다. 악의적이지 않은 JavaScript 클릭 동작을 작성한다고 Braze 대시보드 사용자를 신뢰함을 나타내려면 이 속성을 `TRUE`로 설정합니다. `enableHtmlInAppMessages`가 `TRUE`인 경우 이 옵션도 `TRUE`로 설정됩니다. |
| 앱 버전| 이 옵션에 값을 제공하면 Braze로 전송된 사용자 이벤트가 지정된 버전과 연결되며, 이를 통해 사용자 세분화에 사용할 수 있습니다. |
| 세션 시간 초과(초) | 기본값은 30입니다.<br>기본적으로 세션은 30분 동안 활동이 없으면 제한 시간이 초과됩니다. 이 구성 옵션에 값을 제공하여 기본값을 사용자 지정 값으로 재정의합니다. | 
| 장치 속성 허용 목록 | 기본적으로 Braze SDK는 `DeviceProperties`에서 모든 기기 속성정보를 자동으로 감지하고 수집합니다. 이 동작을 재정의하려면 `DeviceProperties`의 배열을 제공합니다. 일부 속성이 없으면 모든 기능이 제대로 작동하지 않을 수 있습니다. 예를 들어, 현지 시간대 전달은 시간대가 없으면 작동하지 않습니다. |
| 현지화 | 기본적으로 SDK에서 생성된 모든 사용자 표시 메시지는 사용자의 브라우저 언어로 표시됩니다. 이 옵션에 값을 제공하여 해당 동작을 재정의하고 특정 언어를 강제로 적용합니다. 이 옵션의 값은 ISO 639-1 언어 코드여야 합니다. |
| 쿠키 없음 | 기본적으로 Braze SDK는 소량의 데이터(사용자 ID, 세션 아이디)를 쿠키에 저장합니다. 이는 Braze가 사이트의 여러 하위 도메인에서 사용자와 세션을 인식할 수 있도록 하기 위한 것입니다. 문제가 되는 경우 이 옵션에 대해 `TRUE`를 전달하여 쿠키 저장을 비활성화하고 사용자와 세션을 식별하는 데 전적으로 HTML 5 localStorage에 의존합니다. |
| 모든 페이지 추적 | **클래식 대상 웹 기기 모드(유지 관리) 전용**<br><br>Segment는 이 설정이 [매핑을 통해 활성화](https://segment.com/docs/connections/destinations/catalog/braze-web-device-mode-actions/#braze-web-settings-mapping)될 수 있는 웹 작업 프레임워크 대상으로 마이그레이션할 것을 권장합니다.<br><br>이렇게 하면 모든 [페이지 호출](https://segment.com/docs/spec/page/)이 '페이지 로드/보기' 이벤트로 Braze에 전송됩니다. |
| 명명된 페이지만 추적 | **클래식 대상 웹 기기 모드(유지 관리) 전용**<br><br>Segment는 이 설정이 [매핑을 통해 활성화](https://segment.com/docs/connections/destinations/catalog/braze-web-device-mode-actions/#braze-web-settings-mapping)될 수 있는 웹 작업 프레임워크 대상으로 마이그레이션할 것을 권장합니다.<br><br>이렇게 하면 이름이 연결된 페이지 호출만 Braze로 전송됩니다. |
| 수익이 있는 경우 구매 기록 | **클래식 대상 웹 기기 모드(유지 관리) 전용**<br><br>Segment는 이 설정이 [매핑을 통해 활성화](https://segment.com/docs/connections/destinations/catalog/braze-web-device-mode-actions/#braze-web-settings-mapping)될 수 있는 웹 작업 프레임워크 대상으로 마이그레이션할 것을 권장합니다.<br><br>이 옵션을 활성화하면 매출 속성정보가 있는 모든 추적 호출이 구매 이벤트를 트리거합니다. | 
| 알려진 사용자만 추적 | **클래식 대상 웹 기기 모드(유지 관리) 전용**<br><br>Segment는 이 설정이 매핑을 통해 활성화될 수 있는 웹 작업 프레임워크 대상으로 마이그레이션할 것을 권장합니다.<br><br>활성화된 경우 이 새 설정은 유효한 `userId`가 있을 때까지 `window.appboy.initialize` 호출을 지연합니다. | 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab 클라우드 모드 %}

| 설정 | 설명 |
| ------- | ----------- |
| 앱 식별자 | 특정 앱을 참조하는 데 사용되는 앱 식별자입니다. **설정 관리** 아래의 Braze 대시보드에서 확인할 수 있습니다. | 
| REST API 키 | 이는 Braze 대시보드의 **설정** > **API 키에서** 확인할 수 있습니다. | 
| 사용자 지정 REST API 엔드포인트 | 인스턴스에 해당하는 Braze REST 엔드포인트(예: rest.iad-01.braze.com). | 
| 기존 사용자만 업데이트 | **클래식 대상 클라우드 모드(유지 관리) 전용**<br><br>Segment는 이 설정이 [매핑을 통해 활성화](https://segment.com/docs/connections/destinations/catalog/braze-web-device-mode-actions/#braze-web-settings-mapping)될 수 있는 클라우드 작업 프레임워크 대상으로 마이그레이션할 것을 권장합니다.<br><br>기존 사용자만 업데이트할지 여부를 결정합니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% endtabs %}

### 4단계: 매핑 방법 {#methods}

Braze는 [페이지](https://segment.com/docs/connections/sources/catalog/libraries/website/javascript/#page), [식별](https://segment.com/docs/spec/identify/), 세그먼트 [추적](https://segment.com/docs/spec/track/) 방식을 지원합니다. 이러한 방법에서 사용되는 식별자 유형은 데이터가 서버 간(클라우드 모드) 통합 또는 병렬(기기 모드) 통합 중 어떤 통합 방식으로 전송되는지에 따라 달라집니다. Braze 웹 모드 액션 및 클라우드 모드 액션 대상에서 [세그먼트 별칭 호출에](https://segment.com/docs/connections/spec/alias/) 대한 매핑을 설정하도록 선택할 수도 있습니다. 

{% alert note %}
사용자 별칭은 Braze 클라우드 모드(작업) 대상에서 식별자로 지원되지만, Segment의 별칭 호출은 Braze 사용자 별칭과 직접 관련이 없다는 점에 유의해야 합니다.
{% endalert %}

| 식별자 유형 | 지원 대상 |
| --------------- | --------------------- |
| `userId`(`external_id`) | 전체 |
| 익명 사용자 | 기기 모드 대상 |
| 사용자 별칭 | 클라우드 모드 대상 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

클라우드 모드(작업) 대상은 별칭 전용 사용자를 생성하거나 기존 `external_id` 프로필에 별칭을 추가하는 데 사용할 수 있는 [별칭 생성 작업](https://segment.com/docs/connections/destinations/catalog/actions-braze-cloud/#create-alias)을 제공합니다. [사용자 식별 작업](https://segment.com/docs/connections/destinations/catalog/actions-braze-cloud/#identify-user)은 별칭 생성 작업과 함께 사용하여 사용자에 대해 사용 가능한 별칭이 생긴 후에 별칭 전용 사용자를 `external_id`와 병합할 수 있습니다. 

해결 방법을 고안하고 `braze_id`를 사용하여 클라우드 모드에서 익명 사용자 데이터를 전송할 수도 있습니다. 이를 위해 모든 Segment API 호출에 사용자의 `braze_id`를 수동으로 포함해야 합니다. 이 해결 방법을 설정하는 방법에 대한 자세한 내용은 [Segment 설명서](https://segment.com/docs/connections/destinations/catalog/braze/#capture-the-braze_id-of-anonymous-users)에서 확인할 수 있습니다.

Braze로 전송된 대상 데이터는 클라우드 모드 작업 내에서 배치 처리할 수 있습니다. 배치 크기는 최대 75개의 이벤트로 제한되며, 이러한 배치는 30초 동안 누적된 후 플러시됩니다. 요청 배치 처리는 작업을 기준으로 수행됩니다. 예를 들어, 식별 호출(속성)은 요청에서 배치 처리되고 추적 호출(커스텀 이벤트)은 두 번째 요청에서 배치 처리됩니다. 이 기능을 활성화하면 Segment에서 Braze로 전송되는 요청의 수를 줄일 수 있으므로 Braze는 이 기능의 활성화를 권장합니다. 이렇게 하면 대상이 Braze 사용량 제한에 도달하여 요청을 재시도할 위험이 줄어듭니다. 

Braze 대상 > **매핑**으로 이동하여 작업에 대한 배치 처리를 켤 수 있습니다. 여기에서 매핑 오른쪽에 있는 점 3개 아이콘을 클릭하고 **매핑 편집**을 선택합니다. **매핑 선택** 섹션의 맨 아래로 스크롤하여 **Braze로 데이터 배치 처리** 설정이 **예**로 설정되어 있는지 확인합니다.


{% tabs local %}
{% tab 식별 %}
#### 식별

[식별](https://segment.com/docs/spec/identify/) 호출을 사용하면 사용자를 작업에 연결하고 사용자에 대한 속성을 기록할 수 있습니다. 

특정 세그먼트의 특수 특성은 Braze의 표준 속성 프로필 필드에 매핑됩니다:

| 특수 세그먼트 특성 | 브레이즈 표준 속성 |
| ------------- | ----------- |
| `userId` | `external_id` |
| `firstName` | `first_name` |
| `lastName` | `last_name` |
| `email` | `email` |
| `birthday` | `dob` |
| `address.country` | `country` |
| `address.city` | `home_city` |
| `gender` | `gender` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

`email_subscribe`, `push_subscribe` 등 다른 예약된 Braze 프로필 필드는 이러한 필드에 대한 Braze 명명 규칙을 사용하여 식별 호출 내에서 특성으로 전달하여 전송할 수 있습니다.

##### 구독 그룹에 사용자 추가하기

특성 매개변수의 다음 필드를 사용하여 지정된 구독 그룹에서 사용자의 가입 또는 탈퇴를 수행할 수도 있습니다.

예약된 Braze 프로필 필드(`braze_subscription_groups`)를 사용하여 여러 오브젝트 배열과 연결할 수 있습니다. 배열의 각 객체에는 두 개의 예약 키가 있어야 합니다:

1. `subscription_group_state`: 사용자가 특정 구독 그룹에 대해 `"subscribed"` 또는 `"unsubscribed"` 상태인지를 나타냅니다.
2. `subscription_group_id`: 구독 그룹의 고유 ID를 나타냅니다. 이 ID는 Braze 대시보드의 **정기구독 그룹 관리에서** 찾을 수 있습니다.

{% subtabs %}
{% subtab Swift %}
```swift
analytics.identify(
  userId: "{your-user}",
  traits: [
    "braze_subscription_groups": [
      [
        "subscription_group_id": "{your-group-id}",
        "subscription_group_state": "subscribed"
      ],
      [
        "subscription_group_id", "{your-group-id}",
        "subscription_group_state": "unsubscribed"
      ]
    ]
  ]
)
```
{% endsubtab %}
{% subtab Kotlin %}
```kotlin
analytics.identify(
  "{your-user}",
  buildJsonObject {
    put("braze_subscription_groups", buildJsonArray {
        add(
          buildJsonObject {
            put("subscription_group_id", "{your-group-id}")
            put("subscription_group_state", "subscribed")
          }
        )
        add(
          buildJsonObject {
            put("subscription_group_id", "{your-group-id}")
            put("subscription_group_state", "unsubscribed")
          }
        )
      }
    )
  }
)
```
{% endsubtab %}
{% subtab TypeScript %}
```typescript
analytics.identify(
  "{your-user}",
  {
    braze_subscription_groups: [
      {
        subscription_group_id: "{your-group-id}",
        subscription_group_state: "subscribed"
      },
      {
        subscription_group_id: "{your-group-id}",
        subscription_group_state: "unsubscribed"
      }
    ]
  }
)
```
{% endsubtab %}
{% endsubtabs %}

##### 사용자 지정 속성

다른 모든 특성은 [사용자 지정 속성으로]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/) 기록됩니다.

| Segment 메서드 | 브레이징 방법 | 예시 |
|---|---|---|
| 사용자 ID로 식별 | 외부 ID 설정 | Segment: `analytics.identify("dawei");`<br>Braze: `Braze.changeUser("dawei")` |
| 예약된 특성으로 식별 | 사용자 속성 설정 | 세그먼트: `analytics.identify({email: "dawei@braze.com"});`<br> Braze: `Braze.getUser().setEmail("dawei@braze.com");`
| 사용자 지정 특성으로 식별 | 사용자 지정 속성 설정 | 세그먼트: `analytics.identify({fav_cartoon: "Naruto"});`<br>Braze: `Braze.getUser().setCustomAttribute("fav_cartoon": "Naruto")`;
| 사용자 ID 및 특성으로 식별 | Segment: 외부 ID 및 속성 설정 | 앞의 방법을 결합합니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

[웹 모드 작업](https://segment.com/docs/connections/destinations/catalog/braze-web-device-mode-actions/#update-user-profile) 및 [클라우드 모드 작업](https://segment.com/docs/connections/destinations/catalog/braze-cloud-mode-actions/#update-user-profile) 대상에서 사용자 프로필 업데이트 작업을 사용하여 위의 매핑을 설정할 수 있습니다.

{% alert important %}
사용자 속성 데이터를 전달할 때 마지막 업데이트 이후 변경된 속성에 대한 값만 전달해야 합니다. 이렇게 하면 할당량에 대한 데이터 포인트가 불필요하게 소모되지 않습니다. 클라이언트 측 소스의 경우, Segment의 오픈 소스 [미들웨어](https://github.com/segmentio/segment-braze-mobile-middleware) 툴을 사용하여 통합을 최적화하고 Segment에서 중복된 `identify()` 호출을 디바운스하여 데이터 포인트 사용량을 제한합니다. 

{% endalert %}
{% endtab %}

{% tab 추적 %}
#### 추적

이벤트를 추적하면 제공된 이름을 사용하여 해당 이벤트를 [사용자 지정 이벤]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#custom-events) 트로 기록합니다. 

추적 호출의 속성정보 오브젝트 내에서 전송된 메타데이터는 Braze에서 연결된 이벤트의 커스텀 이벤트 속성정보로 기록됩니다. 모든 [사용자 지정 이벤트 속성 데이터 유형이]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#custom-event-properties) 지원됩니다.

[웹 모드 액션](https://segment.com/docs/connections/destinations/catalog/braze-web-device-mode-actions/#track-event) 및 [클라우드 모드 액션](https://segment.com/docs/connections/destinations/catalog/braze-cloud-mode-actions/#track-event) 대상에서 위의 매핑은 이벤트 추적 액션을 사용하여 설정할 수 있습니다.

| Segment 메서드 | 브레이징 방법 | 예시 |
|---|---|---|
| [추적](https://segment.com/docs/spec/track/) | [사용자 지정 이벤트로]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#custom-events) 기록됩니다. | 세그먼트: `analytics.track("played_game");` <br>Braze: `Braze.logCustomEvent("played_game");`|
| [속성정보로 추적](https://segment.com/docs/spec/track/) | [이벤트 속성정보]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#custom-event-properties)로 기록됩니다. | 세그먼트: `analytics.track("played_game", {name: "BotW", weapon: "boomerang"});` <br>Braze: `Braze.logCustomEvent("played_game", { "name": "BotW", "weapon": "boomerang"});` |
| [제품으로 추적](https://segment.com/docs/spec/track/) | [구매 이벤트로]({{site.baseurl}}/developer_guide/analytics/logging_purchases/?tab=web) 기록됩니다. | 세그먼트: `analytics.track("Order Completed", {products: [product_id: "ab12", price: 19]});` <br>Braze: `Braze.logPurchase("ab12", 19);` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

##### 주문 완료 {#order-completed}

When you track an event with the name `Order Completed` using the format described in Segment's [eCommerce API](https://segment.com/docs/spec/ecommerce/v2/), we will record the products you've listed as [purchases]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/exporting_revenue_data/#revenue-data).

[웹 모드 액션](https://segment.com/docs/connections/destinations/catalog/braze-web-device-mode-actions/#track-purchase) 및 [클라우드 모드 액션](https://segment.com/docs/connections/destinations/catalog/braze-cloud-mode-actions/#track-purchase) 대상에서 기본 매핑은 구매 액션 추적하기를 통해 사용자 지정할 수 있습니다.

{% endtab %}

{% tab 페이지 %}
#### 페이지 {#page}

[페이지](https://segment.com/docs/spec/page/) 호출을 사용하면 사용자가 웹사이트의 페이지를 볼 때마다 해당 페이지에 대한 선택적 속성과 함께 기록할 수 있습니다.

이 이벤트 유형은 웹 모드 액션 및 클라우드 액션 대상에서 트리거로 사용하여 사용자 지정 이벤트를 Braze에 기록할 수 있습니다.
{% endtab %}

{% endtabs %}

### 5단계: 통합 테스트

병렬(기기 모드) 통합을 사용하는 경우, [개요][27] 측정기준(평생 세션, MAU, DAU, 사용자 고착도, 일일 세션, MAU당 일일 세션)을 사용하여 Braze가 Segment에서 데이터를 수신하는지 확인할 수 있습니다.

[커스텀 이벤트][22] 또는 [매출][28] 페이지에서 데이터를 보거나 [세그먼트를 생성][23]하여 볼 수 있습니다. 대시보드의 **사용자 지정** 이벤트 페이지에서 시간 경과에 따른 사용자 지정 이벤트 수를 볼 수 있습니다. 서버 간(클라우드 모드) 통합을 사용하는 경우 MAU 및 DAU 통계가 포함된 [공식][24]을 사용할 수 없습니다.

구매 데이터를 Braze로 전송하는 경우( [3단계의](#methods) **추적** 탭에서 주문 완료 참조) [수익][28] 페이지에서 특정 기간 동안의 수익이나 구매 또는 앱의 총 수익에 대한 데이터를 확인할 수 있습니다.

[세그먼트를 생성하면][26] 사용자 지정 이벤트 및 속성 데이터를 기반으로 사용자를 필터링할 수 있습니다.

{% alert important %}
서버 간 통합(클라우드 모드)을 사용하는 경우 자동으로 수집된 세션 데이터와 관련된 필터('처음 사용한 앱' 및 '마지막으로 사용한 앱' 등)가 작동하지 않습니다. Segment와 Braze 통합에서 이러한 기능을 사용하려면 병렬 통합(기기 모드)을 사용합니다.
{% endalert %}

## 사용자 삭제 및 억제 

사용자를 삭제하거나 억제해야 하는 경우, [Segment의 사용자 삭제 기능](https://segment.com/docs/privacy/user-deletion-and-suppression/#which-destinations-can-i-send-deletion-requests-to)이 Braze [`/users/delete` 엔드포인트]({{site.baseurl}}/api/endpoints/user_data/post_user_delete/)에 **매핑**되어 있다는 점에 유의하세요. 이러한 삭제 확인에는 최대 30일이 소요될 수 있습니다.

Braze와 Segment 간에 공통 사용자 식별자를 선택해야 합니다(예: `external_id`). Segment에서 삭제 요청을 시작한 후에는 Segment 대시보드의 삭제 요청 탭에서 상태를 확인할 수 있습니다.

## Segment 재생

Segment는 고객에게 모든 과거 데이터를 새로운 기술 파트너에게 '재생'하는 서비스를 제공합니다. 모든 관련 과거 데이터를 가져오려는 신규 Braze 고객은 Segment를 통해 가져올 수 있습니다. 관심 있는 분야가 있다면 세그먼트 담당자에게 문의하세요.

세그먼트는 [`/users/track` 엔드포인트에]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) 연결하여 사용자를 대신하여 사용자 데이터를 Braze로 가져옵니다.

{% alert important %}
클라우드 모드 작업 대상에서 지원되는 모든 식별자는 Segment 재생의 일부로 지원됩니다.
{% endalert %}

## 모범 사례

{% details 사용 사례를 검토하여 데이터 초과를 방지하세요. %}

Segment는 클라이언트가 전송하는 데이터 요소의 수를 제한하지 **않습니다**. 세그먼트를 사용하면 모든 이벤트를 보내거나 어떤 이벤트를 Braze에 보낼지 결정할 수 있습니다. 모든 이벤트를 세그먼트를 사용하여 전송하는 대신, 마케팅 및 편집 팀과 함께 사용 사례를 검토하여 데이터 초과를 방지하기 위해 어떤 이벤트를 Braze에 전송할지 결정하는 것이 좋습니다.

{% enddetails %}

{% details 모바일 장치 모드 대상 설정에서 사용자 지정 API 엔드포인트와 사용자 지정 REST API 엔드포인트의 차이점을 이해합니다. %}

| Braze 용어 | Segment 등가 기능 |
| ----------------- | ------------------ |
| Braze SDK 엔드포인트 | 사용자 지정 API 엔드포인트 |
| Braze REST 엔드포인트 | 사용자 지정 REST API 엔드포인트 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Braze API 엔드포인트(Segment에서는 '커스텀 API 엔드포인트'라고 함)는 Braze가 SDK에 대해 설정하는 SDK 엔드포인트입니다(예: `sdk.iad-03.braze.com`). Braze REST API 엔드포인트(Segment에서 '커스텀 REST API 엔드포인트'라고 함)는 REST API 엔드포인트입니다(예: `https://rest.iad-03.braze.com`).
{% enddetails %}

{% details 사용자 지정 API 엔드포인트가 모바일 디바이스 모드 대상 설정에 올바르게 입력되었는지 확인합니다. %}

| Braze 용어 | Segment 등가 기능 |
| ----------------- | ------------------ |
| Braze SDK 엔드포인트 | 사용자 지정 API 엔드포인트 |
| Braze REST 엔드포인트 | 사용자 지정 REST API 엔드포인트 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Braze SDK 엔드포인트를 올바르게 입력하려면 적절한 형식을 따라야 합니다. Braze SDK 엔드포인트에 `https://`(예: `sdk.iad-03.braze.com`)가 포함되어서는 안 됩니다. 그렇지 않으면 Braze 통합이 중단됩니다. Segment가 자동으로 엔드포인트 앞에 `https://`를 추가하고 이로 인해 Braze가 잘못된 엔드포인트 `https://https://sdk.iad-03.braze.com`으로 초기화되기 때문입니다.

{% enddetails %}

{% details 데이터 매핑의 뉘앙스. %}

데이터가 예상대로 전달되지 않는 시나리오:

1. 중첩된 사용자 지정 속성
  - 기술적으로 [중첩 커스텀 속성]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/nested_custom_attribute_support/)을 Segment를 통해 Braze에 전송할 수 있지만, 매번 **전체 페이로드**가 전송됩니다. 이렇게 하면 페이로드가 전송될 때마다 중첩 오브젝트에 전달된 키당 [데이터 포인트]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/nested_custom_attribute_support/#data-points)가 발생합니다.<br><br> 페이로드가 전송될 때 데이터 포인트의 하위 집합만 사용하려면 Segment에서 제공하는 커스텀 [대상 함수](https://segment.com/docs/connections/functions/destination-functions/) 기능을 사용할 수 있습니다. Segment 플랫폼의 이 기능을 사용하면 데이터를 다운스트림 대상에 전송하는 방법을 사용자 지정할 수 있습니다.

  {% alert note %}
  커스텀 대상 기능은 Segment 내에서 제어되며, 외부에서 구성한 기능에 대한 Braze의 인사이트는 제한됩니다.
  {% endalert %}

{: start="2"}
2\. 익명 데이터 서버 간 전달.
  - 고객은 Segment의 서버 간 라이브러리를 사용하여 익명 데이터를 다른 시스템으로 전송할 수 있습니다. 서버 간(클라우드 모드) 통합을 통해 `external_id`가 없는 사용자를 Braze로 보내는 방법에 대해 자세히 알아보려면 매핑 방법 섹션을 참조하세요.

{% enddetails %}

{% details Braze 초기화 사용자 지정. %}

Braze는 푸시, 인앱 메시지, 콘텐츠 카드, 초기화 등 여러 가지 방법으로 사용자 지정할 수 있습니다. 병렬 통합을 사용하는 경우 Braze를 직접 통합할 때와 마찬가지로 푸시, 인앱 메시지 및 콘텐츠 카드를 사용자 지정할 수 있습니다.

그러나 Braze SDK를 통합할 때 사용자 지정하거나 초기화 구성을 지정하는 작업은 어렵고 때로는 불가능할 수도 있습니다. Segment 초기화가 수행될 때 Segment가 Braze SDK를 초기화하기 때문입니다.

{% enddetails %}

{% details Braze에 델타 전송. %}

사용자 속성 데이터를 전달할 때 마지막 업데이트 이후 변경된 속성에 대한 값만 전달해야 합니다. 이렇게 하면 할당량에 대한 데이터 포인트가 불필요하게 소모되지 않습니다. 클라이언트 측 소스의 경우, Segment의 오픈 소스 [미들웨어](https://github.com/segmentio/segment-braze-mobile-middleware) 툴을 사용하여 통합을 최적화하고 Segment에서 중복된 `identify()` 호출을 디바운스하여 데이터 포인트 사용량을 제한합니다. 

{% enddetails %}


[5]: https://segment.com
[13]: {{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#custom-events
[14]: {{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/
[18]: {{site.baseurl}}/developer_guide/rest_api/user_data/#user-attributes-object-specification
[19]: {{site.baseurl}}/developer_guide/rest_api/user_data/#user-data
[22]: {{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/export_custom_event_data/#custom-event-data
[23]: {{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/#creating-a-segment
[24]: {{site.baseurl}}/user_guide/data_and_analytics/creating_a_formula/#creating-a-formula
[25]: {{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/#user-data-collection
[26]: {{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/#creating-a-segment
[27]: {{site.baseurl}}/user_guide/data_and_analytics/analytics/understanding_your_app_usage_data/
[28]: {{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/exporting_revenue_data/#revenue-data
[34]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/
[35]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/
[36]: https://segment.com/docs/sources/#server
[38]: {{site.baseurl}}/developer_guide/platform_integration_guides/web/initial_sdk_setup/
[39]: {{site.baseurl}}/developer_guide/rest_api/basics/#app-group-rest-api-keys
[40]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints
[41]: https://segment.com/docs/spec/identify/#user-id
[42]: {% image_buster /assets/img/segment/setup.png %}
[43]: {% image_buster /assets/img/segment/website.png %}
[44]: {% image_buster /assets/img/segment/ios.png %}
[45]: {% image_buster /assets/img/segment/android.png %}

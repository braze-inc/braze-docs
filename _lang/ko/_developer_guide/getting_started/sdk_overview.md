---
nav_title: SDK 개요
article_title: 개발자용 SDK 개요
description: "이 온보딩 참조 문서에서는 Braze SDK 개발자를 위한 기술 개요를 제공합니다. SDK에서 추적하는 기본 분석, 자동 데이터 수집 차단, 앱의 라이브 SDK 버전도 논의합니다."
page_order: 0
---

# [![Braze 학습 과정]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/path/developer/sdk-integration-basics){: style="float:right;width:120px;border:0;" class="noimgborder"}개발자용 SDK 개요

> Braze SDK 통합을 시작하기 전에 정확히 무엇을 빌드하고 통합해야 하는지 알고 싶을 수 있습니다. 요구 사항에 맞게 SDK를 사용자 지정하는 방법도 궁금할 수 있습니다. 이 문서는 모든 SDK 관련 질문에 대한 답을 찾는 데 도움을 줄 수 있습니다. 

SDK에 대한 기본적인 개요를 찾고 계신 마케터인가요? 대신 [마케터 개요]({{site.baseurl}}/user_guide/getting_started/web_sdk/)를 확인하세요.

다음은 Braze SDK의 주요 기능입니다.
* 사용자 데이터를 수집하여 통합된 사용자 프로필로 동기화합니다.
* 세션 데이터, 기기 정보, 푸시 토큰 자동 수집
* 마케팅 인게이지먼트 데이터 및 비즈니스 특정 커스텀 데이터 캡처
* 푸시 알림, 인앱 메시지 및 콘텐츠 카드 메시징 채널 지원

## 앱 성능

Braze는 앱 성능에 부정적인 영향을 미치지 않아야 합니다.

Braze SDK는 설치에 필요한 공간이 매우 작습니다. 네트워크를 수동으로 제어하는 것 외에도 네트워크 품질에 따라 사용자 데이터를 플러시하는 속도를 자동으로 변경합니다. 또한 네트워크 효율성을 최대로 유지하면서 데이터를 신속하게 기록할 수 있도록 SDK에서 API 요청을 자동으로 일괄 처리합니다. 마지막으로, 각 API 호출에서 클라이언트로부터 Braze로 전송되는 데이터의 양은 매우 적습니다.

## SDK 호환성

Braze SDK는 앱에 있는 다른 SDK를 방해하지 않으면서 매우 원활하게 작동하도록 설계되었습니다. 다른 SDK와의 호환성 문제로 인한 것으로 생각되는 문제가 발생하면 Braze 지원팀에 문의하세요.

## 기본 분석 및 세션 처리

특정 사용자 데이터(예: 처음 사용한 앱, 마지막으로 사용한 앱, 총 세션 수, 기기 OS 등)는 SDK에서 자동으로 수집됩니다. 통합 가이드에 따라 SDK를 구현하면 이 [기본 데이터 수집]({{site.baseurl}}/user_guide/data/user_data_collection/sdk_data_collection/) 기능을 활용할 수 있습니다. 이 목록을 확인하면 사용자에 대한 동일한 정보를 두 번 이상 저장하지 않도록 하는 데 도움이 됩니다. 세션 시작과 세션 종료를 제외한 다른 모든 자동 추적 데이터는 데이터 포인트 할당에 포함되지 않습니다.

{% alert note %}
모든 기능이 구성 가능하지만 기본 데이터 수집 모델을 완전히 구현하는 것이 좋습니다.

<br>사용 사례에 필요한 경우 통합이 완료된 후 [특정 데이터의 수집을 제한](#blocking-data-collection)할 수 있습니다.
{% endalert %}

## 데이터 업로드 및 다운로드

Braze SDK는 데이터(세션, 커스텀 이벤트 등)를 캐시하고 주기적으로 업로드합니다. 데이터가 업로드된 후에만 대시보드에서 값이 업데이트됩니다. 업로드 간격은 기기의 상태를 고려하고 네트워크 연결 품질에 따라 결정됩니다.

|네트워크 연결 품질 |    데이터 플러시 간격|
|---|---|
|매우 양호    |10초|
|양호    |30초|
|미흡    |60초|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

네트워크 연결이 없으면 네트워크 연결이 다시 설정될 때까지 데이터가 기기에 로컬로 캐시됩니다. 연결이 다시 설정되면 데이터가 Braze에 업로드됩니다.

Braze는 세션이 시작될 때 사용자가 속한 Segment에 따라 세션 시작 시 데이터를 SDK로 전송합니다. 세션 중에는 새 인앱 메시지가 업데이트되지 않습니다. 그러나 세션 중 사용자 데이터는 클라이언트에서 전송되는 대로 계속 처리됩니다. 예를 들어, 이탈 사용자(앱을 마지막으로 사용한 지 7일이 넘은 사용자)는 앱에 다시 접속한 첫 번째 세션에서 이탈 사용자를 대상으로 하는 콘텐츠를 계속 받게 됩니다.

## 데이터 수집 차단

SDK 통합에서 특정 데이터의 자동 수집을 차단하거나 이를 수행하는 프로세스를 허용 목록에 추가할 수 있습니다(단, 권장하지 않음). 

분석 데이터를 제거하면 플랫폼의 개인화 및 타겟팅 기능이 저하되므로 데이터 수집 차단은 권장되지 않습니다. 예를 들어, 다음과 같습니다.

- SDK 중 하나에서 위치를 완전히 통합하지 않으려는 경우 언어 또는 위치를 기반으로 메시지를 개인화할 수 없습니다. 
- 표준 시간대를 통합하지 않으려는 경우 사용자의 표준 시간대 내에서 메시지를 보내지 못할 수 있습니다. 
- 특정 기기의 시각적 정보를 통합하지 않으려는 경우 메시지 콘텐츠가 해당 기기에 최적화되지 않을 수 있습니다.

제품의 기능을 최대한 활용하려면 SDK를 완전히 통합할 것을 적극 권장합니다.

{% tabs %}
{% tab 웹 SDK %}

SDK의 특정 부분을 통합하지 않거나 사용자 측에서 [`disableSDK`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#disablesdk)를 사용할 수 있습니다. 이 메서드는 `disableSDK()` 호출 이전에 기록된 데이터를 동기화하며, 이 페이지 및 향후 페이지 로드에서 이후 모든 Braze 웹 SDK 호출을 무시합니다. 나중에 데이터 수집을 재개하려면 향후 [`enableSDK()`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#enablesdk) 메서드를 사용하여 데이터 수집을 재개할 수 있습니다. 이에 대한 자세한 내용은 [웹 추적 비활성화]({{site.baseurl}}/developer_guide/analytics/managing_data_collection/?sdktab=web) 문서에서 확인할 수 있습니다.

{% endtab %}
{% tab Android SDK %}

[`setDeviceObjectAllowlist`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.configuration/-braze-config/-builder/set-device-object-allowlist.html?query=fun%20setDeviceObjectAllowlist(deviceObjectAllowlist:%20EnumSet%3CDeviceKey%3E):%20BrazeConfig.Builder)를 사용하여 설정된 허용 목록에 따라 기기 오브젝트 키 또는 값의 하위 집합만 전송하도록 SDK를 구성할 수 있습니다. [`setDeviceObjectAllowlistEnabled`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.configuration/-braze-config/-builder/set-device-object-allowlist-enabled.html?query=fun%20setDeviceObjectAllowlistEnabled(enabled:%20Boolean):%20BrazeConfig.Builder)를 통해 활성화해야 합니다.

{% alert important %}
허용 목록이 비어 있으면 Braze로 전송되는 디바이스 데이터가 **없습니다**.
{% endalert %}

{% endtab %}
{% tab Swift SDK %}

`Braze.Configuration`의 [`configuration.devicePropertyAllowList`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/devicepropertyallowlist)에 적격 필드 집합을 할당하여 SDK에서 수집하는 기기 필드에 대한 허용 목록을 지정할 수 있습니다. 전체 필드 목록은 [`Braze.Configuration.DeviceProperty`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/deviceproperty)에서 정의합니다. 모든 기기 필드 수집을 해제하려면 이 속성정보 값을 빈 집합(`[]`)으로 설정합니다.

{% alert important %}
기본적으로 모든 필드는 Braze Swift SDK에 의해 수집됩니다. 일부 기기 속성정보를 제거하면 SDK 기능이 비활성화될 수 있습니다.
{% endalert %}

자세한 사용법은 Swift SDK 설명서의 [스토리지]({{site.baseurl}}/developer_guide/storage/?tab=swift)를 참조하세요.

{% endtab %}
{% endtabs %}

## 어떤 버전의 SDK를 사용하고 있나요?

대시보드에서 **설정 > 앱 설정**으로 이동하여 특정 앱의 SDK 버전을 확인할 수 있습니다. **라이브 SDK 버전**에는 최소 5% 이상의 사용자가 최근 라이브 애플리케이션에서 사용하는 가장 높은 Braze SDK 버전이 나열됩니다.

![워크스페이스에 Swifty라는 앱이 있습니다. 라이브 SDK 버전은 6.6.0입니다.]({% image_buster /assets/img/live-sdk-version.png %}){: style="max-width:80%"} 

{% alert tip %}
iOS 앱이 있는 경우 **라이브 SDK 버전**이 Swift SDK의 첫 번째 릴리스 버전인 5.0.0 이상이면 기존 [Objective-C iOS SDK]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/overview/) 대신 [Swift SDK]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=swift)를 사용 중임을 확인할 수 있습니다.
{% endalert %}


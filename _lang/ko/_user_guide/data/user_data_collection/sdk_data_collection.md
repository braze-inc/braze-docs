---
nav_title: SDK 데이터 수집
article_title: SDK 데이터 수집
page_order: 1
page_type: reference
description: "이 참조 문서는 개인화된 통합, 자동 수집 통합 및 최소 통합을 통해 SDK가 수집하는 데이터에 대해 다룹니다."

---

# SDK 데이터 수집

> Braze SDK를 앱 또는 사이트에 통합하면 Braze가 특정 유형의 데이터를 자동으로 수집합니다. 이 데이터 중 일부는 프로세스에 필수적이며, 일부 데이터는 필요에 따라 설정하거나 해제할 수 있습니다. 또한 세분화 및 메시징을 더욱 강화하기 위해 추가 유형의 데이터를 수집하도록 Braze를 구성할 수도 있습니다.

Braze는 유연한 데이터 수집이 가능하도록 설계되었으므로 다음과 같은 방법으로 Braze SDK를 통합할 수 있습니다:

- **[최소한의 통합](#minimum-integration):** Braze는 Braze 서비스와의 통신에 필요한 데이터를 자동으로 수집합니다.
- **[기본적으로 수집되는 선택적 데이터입니다](#optional-data-collected-by-default):** Braze는 대부분의 사용 사례에 광범위하게 유용한 일부 데이터를 자동으로 캡처합니다. Braze 서비스와의 통신에 필수적이지 않은 경우 이 데이터의 자동 수집을 사용하지 않도록 설정할 수 있습니다.
- **[기본적으로 수집되지 않는 선택적 데이터입니다](#data-not-collected-by-default):** Braze는 특정 사용 사례에 유용한 일부 데이터를 캡처하며, 광범위한 규정 준수를 위해 자동으로 수집을 활성화하지는 않습니다. 사용 사례에 적합한 경우 이 데이터를 수집하도록 선택할 수 있습니다.
- **[맞춤형 통합](#personalized-integration):** Braze는 기본 옵션 데이터 외에도 데이터를 유연하게 수집할 수 있는 기능을 제공합니다.

## 최소 통합

다음은 SDK를 초기화할 때 Braze가 생성하고 수신하는 필수 데이터의 목록입니다. 이 데이터는 구성할 수 없으며 핵심 플랫폼 기능에 필수적입니다. 세션 시작과 세션 종료를 제외한 다른 모든 자동 추적 데이터는 데이터 포인트 할당량에 포함되지 않습니다.

| 속성 | 설명 | 수집하는 이유 |
| --------- | ----------- | ------------------ |
| 앱 버전 이름 /<br> 앱 버전 코드 | 최신 앱 버전 | 이 속성은 앱 버전 호환성과 관련된 메시지를 올바른 디바이스로 전송하는 데 사용됩니다. 서비스 중단이나 버그를 사용자에게 알리는 데 사용할 수 있습니다. |
| 국가 | IP 주소 지리적 위치로 식별된 국가. IP 주소 지리적 위치를 사용할 수 없는 경우 [디바이스 로캘로](#optional-data-collected-by-default) 식별됩니다. 이 값은 SDK가 `setCountry` 로 직접 설정한 값을 사용할 수도 있지만, SDK 또는 API를 통해 속성 값을 전달하면 데이터 포인트를 소비하게 됩니다.| 이 속성은 위치를 기준으로 메시지를 타겟팅하는 데 사용됩니다. |
| 기기 ID | 기기 식별자, 무작위로 생성된 문자열 | 이 속성은 사용자의 디바이스를 구분하고 올바른 디바이스로 메시지를 전송하는 데 사용됩니다. |
| OS 및 OS 버전 | 현재 보고된 기기 또는 브라우저 및 기기 또는 브라우저 버전 | 이 속성은 호환되는 디바이스로만 메시지를 보내는 데 사용됩니다. 세분화 내에서 사용하여 사용자가 앱 버전을 업그레이드하도록 타겟팅할 수도 있습니다. |
| 세션 시작 및 세션 종료 | 사용자가 통합된 앱 또는 사이트를 사용하기 시작할 때 | Braze SDK는 사용자 인게이지먼트를 계산하기 위해 Braze 대시보드에서 사용하는 세션 데이터 및 사용자를 이해하는 데 핵심적인 기타 분석을 보고합니다. Exactly when the session start and session end is called by your app or site is configurable by a developer ([Android]({{site.baseurl}}/developer_guide/analytics/tracking_sessions/?tab=android), [iOS]({{site.baseurl}}/developer_guide/analytics/tracking_sessions/?tab=swift), [Web]({{site.baseurl}}/developer_guide/analytics/tracking_sessions/?tab=web)). |
| SDK 메시지 상호작용 데이터 | 푸시 직접 열기, 인앱 메시지 상호작용, 콘텐츠 카드 상호작용 | 이 속성은 메시지가 수신되었는지 확인하고 전송이 중복되지 않도록 하는 등 품질 관리 목적으로 사용됩니다. |
| SDK 버전 | 현재 SDK 버전 | 이 속성은 호환되는 디바이스로만 메시지를 전송하고 서비스 중단을 방지하는 데 사용됩니다. |
| 세션 ID 및 세션 타임스탬프 | 세션 식별자, 무작위로 생성된 문자열 및 세션 타임스탬프 | 사용자가 새 세션을 시작하는지 기존 세션을 시작하는지 여부를 결정하고 이 사용자에게 의도된 메시지의 재적격성을 결정하는 데 사용됩니다.<br><br>일부 메시징 채널(예: 인앱 메시지 및 콘텐츠 카드)은 세션 시작 시 기기와 동기화됩니다. 그 후 백엔드는 사용자가 새로운 메시지를 받을 자격이 있는지 확인하기 위해 기기가 저장하고 다시 보내는 Braze 서버에 마지막으로 접속한 시점과 관련된 데이터를 사용합니다.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

### 계산된 측정기준

Braze는 SDK 데이터, 비 SDK 메시지와 관련된 메시지 상호작용 데이터 및 파생된 정보에 대해 계산된 지표를 생성합니다. 명확성을 위해, 이 계산된 데이터는 SDK에 의해 추적되지 않고 Braze 서비스에 의해 생성되며, 고객 프로필에는 추적된 데이터와 생성된 데이터가 모두 표시됩니다. 

계산된 측정기준에는 다음 속성이 포함됩니다.

| 속성                                      | 설명                                                          |
|-----------------------------------------------|----------------------------------------------------------------------|
| 처음 사용한 앱                                 | 시간                                                                 |
| 마지막으로 사용한 앱                                  | 시간                                                                 |
| 총 세션 수                            | 숫자                                                               |
| 클릭된 카드                                   | 숫자                                                               |
| 마지막으로 수신한 메시지                     | 시간                                                                 |
| 마지막으로 받은 이메일 캠페인                   | 시간                                                                 |
| 마지막으로 받은 푸시 캠페인                    | 시간                                                                 |
| 피드백 항목 수                       | 숫자                                                               |
| 지난 Y일 동안의 세션 수          | 숫자와 시간                                                      |
| 캠페인에서 메시지를 받았습니다                  | 부울. 이 필터는 이전 캠페인을 수신했는지 여부에 따라 사용자를 타겟팅합니다.                               |
| 캠페인에서 태그가 있는 메시지를 받았습니다        | 부울. 이 필터는 현재 태그가 있는 캠페인을 수신했는지 여부에 따라 사용자를 타겟팅합니다.                  |
| 리타겟 캠페인                              | 부울. 이 필터는 사용자가 과거에 특정 이메일, 푸시 또는 인앱 메시지를 열었거나 클릭했는지 여부에 따라 사용자를 타겟팅합니다. |
| 제거됨                                    | 부울 및 시간 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

{% alert important %}
최소한의 통합에만 관심이 있고 mParticle, Segment, Tealium 또는 GTM과 통합하는 경우 다음 사항에 유의하세요:
- **모바일 플랫폼**: 이러한 구성에 대한 코드를 수동으로 업데이트해야 합니다. mParticle 및 Segment는 해당 플랫폼을 통해 이 작업을 수행할 수 있는 방법을 제공하지 않습니다. 
- **웹**: Braze 통합은 최소 통합 구성을 허용하기 위해 네이티브로 수행되어야 합니다. 태그 관리자는 플랫폼을 통해 이 작업을 수행할 수 있는 방법을 제공하지 않습니다.
{% endalert %} 

## 기본적으로 수집된 선택적 데이터

최소 연동 데이터 외에도, SDK 연동을 초기화할 때 다음 속성이 Braze에 의해 자동으로 캡처됩니다. 최소한의 통합을 위해 이러한 속성 수집을 [거부할]({{site.baseurl}}/developer_guide/platform_integration_guides/sdk_primer/#blocking-data-collection) 수 있습니다.

| 속성               | 플랫폼          | 설명                                                                        | 수집하는 이유                                                                                                                                                      |
|-------------------------|-------------------|------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 브라우저 이름            | 웹               | 브라우저의 이름                                                                | 이 속성은 호환되는 브라우저에만 메시지를 보내는 데 사용됩니다. 브라우저 기반 세분화에도 사용할 수 있습니다.                                     |
| 기기 로캘           | Android, iOS      | 기기의 기본 로캘                                                   | 이 속성은 사용자의 선호 언어로 메시지를 번역하는 데 사용됩니다.                                                                                            |
| 최신 기기 로캘           | Android, iOS      | 장치의 가장 최근 기본 로캘                                                   | 이 속성은 사용자의 디바이스 설정에서 가져오며 메시지를 사용자가 선호하는 언어로 번역하는 데 사용됩니다. `Most Recent Location` 속성과는 독립적입니다.                                                                                            |
| 기기 모델            | Android, iOS      | 기기의 특정 하드웨어                                                | 이 속성은 호환되는 디바이스로만 메시지를 보내는 데 사용됩니다. 세분화 내에서도 사용할 수 있습니다.                                                 |
| 기기 브랜드            | Android           | 기기의 브랜드(예: 삼성)                                         | 이 속성은 호환되는 디바이스로만 메시지를 보내는 데 사용됩니다.                                                                                          |
| 기기 이동통신사 | Android, iOS      | 이동통신사                                                                 | 이 속성은 메시지 타겟팅에 선택적으로 사용됩니다.<br><br>**참고:** 이 필드는 iOS 16부터 더 이상 사용되지 않으며 향후 iOS 버전에서 `--`로 기본값이 설정될 것입니다. |
| 언어                | Android, iOS, 웹 | 장치 또는 브라우저 언어, 장치 로캘에서 가져온 언어                                                            | 이 속성은 메시지를 사용자가 선호하는 언어로 번역하는 데 사용됩니다. 디바이스 로캘을 기반으로 합니다.                                                                                            |
| 알림 설정   | Android, iOS, 웹 | 이 앱에 푸시 알림이 활성화되어 있는지 여부.                                   | 이 속성은 푸시 알림을 활성화하는 데 사용됩니다.                                                                                                                    |
| 해상도              | Android, iOS, 웹 | 장치 또는 브라우저 해상도                                                          | 선택적으로 기기 기반 메시지 타겟팅에 사용됩니다. 이 값의 형식은 "`<width>`x`<height>`"입니다.                                                                 |
| 시간대               | Android, iOS, 웹 | 기기 또는 브라우저 시간대                                                           | 이 속성은 각 사용자의 현지 표준 시간대에 따라 적절한 시간에 메시지를 보내는 데 사용됩니다.                                                   |
| 사용자 에이전트              | 웹               | [사용자 에이전트](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/User-Agent) | 이 속성은 호환되는 디바이스로만 메시지를 보내는 데 사용됩니다. 세분화 내에서도 사용할 수 있습니다.                                                 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

디바이스 수준 속성(디바이스 무선 통신사, 시간대, 해상도 등) 추적에 대해 자세히 알아보려면 플랫폼별 설명서를 참조하세요: [Android안드로이드]({{site.baseurl}}/developer_guide/platform_integration_guides/android/storage/ "허용 목록 문서"), [iOSiOS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/storage/ "허용 목록 문서"), [웹]({{site.baseurl}}/developer_guide/storage/#cookies).

## 데이터는 기본값으로 수집되지 않습니다

기본적으로 다음 속성은 수집되지 않습니다. 각 속성은 수동으로 통합해야 합니다.

| 속성                  | 플랫폼     | 설명                                                                                                                                                                                                                                                                                                               | 수집되지 않는 이유                                                                                                                                                                                                                                                                 |
|----------------------------|--------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 기기 광고 추적 활성화 | Android, iOS | iOS에서:<br>[`set(adTrackingEnabled:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/set(adtrackingenabled:))<br><br>Android에서:<br>[`Braze.setGoogleAdvertisingId()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/set-google-advertising-id.html) | 이 속성정보는 추가적인 앱 수준 권한이 필요하며, 통합자가 부여해야 합니다.                                                                                                                                                                                      |
| 기기 IDFA                | iOS          | 광고주를 위한 기기 식별자                                                                                                                                                                                                                                                                                         | 이는 앱 스토어에서 추가적인 개인정보 검토를 트리거할 광고 추적 투명성 프레임워크를 필요로 합니다. 자세한 내용은 [`set(identifierForAdvertiser:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/set(identifierforadvertiser:))를 참조하세요 |
| 구글 광고 ID      | Android      | Google Play 앱 내 광고를 위한 식별자                                                                                                                                                                                                                                                                        | 이를 위해 앱이 GAID를 검색하여 Braze에 전달해야 합니다. 자세한 내용은 [선택적 Google 광고 ID]({{site.baseurl}}/developer_guide/platform_integration_guides/android/sdk_integration#google-advertising-id)를 참조하십시오.                                         |
| 가장 최근 위치 | Android, iOS | 사용자 디바이스의 마지막으로 알려진 GPS 위치입니다. 세션 시작 시 업데이트되며 사용자의 프로필에 저장됩니다. | 이를 위해서는 사용자가 앱에 위치 권한을 부여해야 합니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

{% alert note %}
Braze SDK는 IP 주소를 로컬에 저장하지 않습니다.
{% endalert %}

## 개인화된 통합

Braze를 최대한 활용하기 위해 SDK 통합자는 종종 Braze SDK를 구현하고 자동으로 수집된 데이터 위에 비즈니스와 관련된 [사용자 지정 속성]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#setting-custom-attributes), [사용자 지정 이벤트]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#logging-custom-events) 및 [구매 이벤트를]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/purchase_events/#logging-purchase-events) 기록합니다.

개인화된 통합은 사용자 경험과 관련된 맞춤형 커뮤니케이션을 가능하게 합니다.

{% alert important %}
Braze는 세션 수가 5,000,000개가 넘는 사용자("더미 사용자")를 금지 또는 차단하고 더 이상 해당 사용자의 SDK 이벤트를 수집하지 않습니다. 추가 정보는 [스팸 차단]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_archival/#spam-blocking)을 참조하십시오.
{% endalert %}


[1]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.enums/-device-key/index.html "Android 기기 수준 필드"

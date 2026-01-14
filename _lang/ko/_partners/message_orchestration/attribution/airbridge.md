---
nav_title: Airbridge
article_title: Airbridge
alias: /partners/airbridge/
description: "이 참조 문서에서는 여러 기기, ID 및 플랫폼 전반에 걸쳐 실제 마케팅 효과를 측정하기 위해 사람 기반의 기여도 및 점진적 측정을 제공하는 Airbridge와 Braze 간의 파트너십을 간략히 설명합니다."
page_type: partner
search_tag: Partner

---

# Airbridge

> [Airbridge](https://www.airbridge.io/)는 모바일 기여도, 증분 측정 및 마케팅 믹스 모델링을 통해 성장의 진정한 원천을 발견할 수 있도록 도와주는 통합 모바일 측정 플랫폼입니다.

_이 통합은 Airbridge에서 유지 관리합니다._

## 통합 정보

Braze와 Airbridge 통합을 통해 Airbridge에서 Braze로 모든 비유기적 설치 경로 데이터를 전달하여 개인화된 마케팅 캠페인을 구축할 수 있습니다.

## 필수 조건

| 요구 사항 | 설명 |
|---|---|
| Airbridge 계정 | 이 파트너십을 활용하려면 Airbridge 계정이 필요합니다. |
| iOS 또는 Android 앱 | 이 통합은 iOS 및 Android 앱을 지원합니다. 플랫폼에 따라 애플리케이션에 코드 스니펫이 필요할 수 있습니다. |
| Airbridge SDK | 필수 Braze SDK 외에도 Airbridge [Android](https://help.airbridge.io/en/developers/android-sdk) 또는 [iOS](https://help.airbridge.io/en/developers/ios-sdk) SDK를 설치해야 합니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 통합

### 1단계: 기기 ID 매핑

서버 간 통합은 앱에 다음 코드 스니펫을 포함하여 활성화할 수 있습니다.

#### Android

Android 앱이 있는 경우 고유한 Braze 기기 ID를 Airbridge에 전달해야 합니다.

{% tabs %}
{% tab Android %}
{% subtabs %}
{% subtab Java %}

```java
// MainApplciation.java
@Override
public void onCreate() {
    super.onCreate();
    // Initialize Airbridge SDK
    AirbridgeConfig config = new AirbridgeConfig.Builder("APP_NAME", "APP_TOKEN")
        // Make Airbridge SDK explicitly start tracking
        .setAutoStartTrackingEnabled(false)
        .build();
    Airbridge.init(this, config);
    
    // Set device alias into Airbridge SDK
    Airbridge.getCurrentUser().setAlias("braze_device_id", Braze.getInstance(this).getDeviceId());
    // Explicitly start tracking
    Airbridge.startTracking();
}
```

{% endsubtab %}
{% subtab Kotlin %}

```kotlin
// MainApplication.kt
override fun onCreate() {
    super.onCreate()
    // Initialize Airbridge SDK
    val config = AirbridgeConfig.Builder("YOUR_APP_NAME", "YOUR_APP_SDK_TOKEN")
        // Make Airbridge SDK explicitly start tracking
        .setAutoStartTrackingEnabled(false)
        .build()
    Airbridge.init(this, config)

    // Set device alias into Airbridge SDK
    Airbridge.getCurrentUser().setAlias("braze_device_id", Braze.getInstance(this).deviceId)
    // Explicitly start tracking
    Airbridge.startTracking()
}
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

#### iOS

iOS 앱이 있는 경우 useUUIDAsDeviceId 필드를 false로 설정하여 IDFV를 수집하도록 선택할 수 있습니다. 설정하지 않으면 iOS 기여도가 Airbridge에서 Braze로 정확하게 매핑되지 않을 수 있습니다. 자세한 내용은 IDFV 수집을 참조하세요.

{% tabs %}
{% tab iOS %}
{% subtabs %}
{% subtab Swift %}

```swift
// AppDelegate.swift
func application(
  _ application: UIApplication,
  didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey : Any]?
) {
    AirBridge.setAutoStartTrackingEnabled(false)
    AirBridge.getInstance("YOUR_APP_TOKEN", appName:"YOUR_APP_NAME", withLaunchOptions:launchOptions)

    AirBridge.state()?.addUserAlias(withKey:"braze_device_id", value:Appboy.sharedInstance()?.getDeviceId())
    AirBridge.startTracking()
}
```

{% endsubtab %}
{% subtab Objective-C %}

```objc
// AppDelegate.m
-           (BOOL)application:(UIApplication *)application
didFinishLaunchingWithOptions:(NSDictionary *)launchOptions
{
  AirBridge.autoStartTrackingEnabled = NO;
  [AirBridge getInstance:@"YOUR_APP_TOKEN" appName:@"YOUR_APP_NAME" withLaunchOptions:launchOptions];

    [AirBridge.state addUserAliasWithKey:@"braze_device_id" value:Appboy.sharedInstance.getDeviceId];
    [AirBridge startTracking];
}
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

#### React Native

{% tabs %}
{% tab TypeScript %}

```typescript
Braze.getInstallTrackingId(function (error, brazeID) {
    Airbridge.state.setDeviceAlias("braze_device_id", brazeID)
    Airbirdge.state.startTracking()
})
```

{% endtab %}
{% endtabs %}

#### Cordova

{% tabs %}
{% tab TypeScript %}

```typescript
AppboyPlugin.getDeviceId(function (brazeID) {
    Airbridge.state.setDeviceAlias("braze_device_id", brazeID)
  Airbridge.state.startTracking()
})
```

{% endtab %}
{% endtabs %}

#### Flutter

{% tabs %}
{% tab TypeScript %}

```typescript
BrazePlugin.getInstallTrackingId().then((brazeID) {
    Airbridge.state.setDeviceAlias("braze_device_id", brazeID)
  Airbridge.state.startTracking()
})
```

{% endtab %}
{% endtabs %}

#### Unity

{% tabs %}
{% tab C# %}

```c#
string BrazeID = AppboyBinding.GetInstallTrackingId();
AirbridgeUnity.SetDeviceAlias("braze_device_id", BrazeID);
AirbridgeUnity.StartTracking()
```

{% endtab %}
{% endtabs %}

### 2단계: Braze 데이터 가져오기 키 받기

Braze에서 **파트너 통합** > **기술 파트너**로 이동하여 **Airbridge**를 선택합니다.

여기에서 REST 엔드포인트를 찾아 Braze 데이터 가져오기 키를 생성합니다. 키가 생성된 후에는 새 키를 생성하거나 기존 키를 무효화할 수 있습니다. 데이터 가져오기 키와 REST 엔드포인트는 Airbridge의 대시보드에서 포스트백을 설정할 때 다음 단계에서 사용됩니다.

]{% image_buster /assets/img/airbridge/airbridge_integration_step_1.png %}()

### 3단계: Airbridge의 대시보드에서 Braze를 구성합니다

1. Airbridge에서 왼쪽 사이드바의 **Integrations > Third-party Integrations**로 이동하여 **Braze**를 선택합니다.
2. Braze 대시보드에서 찾은 데이터 가져오기 키와 REST 엔드포인트를 입력합니다.
3. 이벤트 유형(설치 이벤트 또는 설치 및 딥링크 열기 이벤트)을 선택하고 저장합니다.

{% alert note %}
딥링크 열람 이벤트로 이어진 캠페인의 기여도 데이터는 기기 수준에서 업데이트됩니다. 예를 들어, 두 사용자가 하나의 기기를 사용하고 한 사용자가 딥링크 열람 이벤트를 수행하면, 이 이벤트의 기여도 데이터가 다른 사용자의 데이터에도 반영됩니다.
{% endalert %}

자세한 지침은 [Airbridge](https://help.airbridge.io/en/guides/braze)를 방문하십시오.

### 4단계: 통합을 확인하십시오

Braze가 Airbridge로부터 기여도 데이터를 수신하면 Braze의 Airbridge 기술 파트너 페이지에서 연결 상태 표시기가 '연결되지 않음'에서 '연결됨'으로 변경됩니다. 마지막 성공적인 요청의 타임스탬프도 포함될 것입니다.

기여도 설치에 대한 데이터가 수신될 때까지는 이 작업이 수행되지 않습니다. Airbridge 포스트백에서 제외되어야 하는 유기적 설치는 API에서 무시되며, 연결이 성공적으로 설정되었는지 확인할 때 계산되지 않습니다.

## 사용 가능한 데이터 필드

Airbridge는 다음 데이터 필드 차트에 나열된 Braze에 네 가지 유형의 기여도 데이터를 보낼 수 있습니다. 이 데이터는 Airbridge 대시보드에서 볼 수 있으며 사용자 설치 경로 및 필터링에 사용됩니다.

제안된 대로 통합을 구성하면, Braze는 설치 데이터를 세그먼트 필터에 매핑합니다.

| Airbridge 데이터 필드 | Braze 세그먼트 필터 | 설명 |
| -------------------- | ---------------------| ---- |
| `Channel` | 설치 속성 소스 | 설치 또는 딥링크 열람에 기여하는 채널 |
| `Campaign` | 설치 속성 캠페인 | 설치 또는 딥링크 열람에 기여하는 캠페인 |
| `Ad Group` | 설치 속성 광고 그룹 | 설치 또는 딥링크 열람에 기여하는 광고 그룹 |
| `Ad Creative` | 설치 속성 광고 | 설치 또는 딥링크 열람에 기여하는 광고 크리에이티브 |

Braze 대시보드에서 설치 경로 필터를 사용하여 사용자 기반을 기여도 데이터로 세분화할 수 있습니다.

]{% image_buster /assets/img/airbridge/airbridge_integration_step_2.png %}()

## 메타 비즈니스 기여도 데이터

메타 비즈니스 캠페인에 대한 기여도 데이터는 파트너를 통해 제공되지 않습니다. 이 미디어 소스는 파트너가 서드파티와 기여도 데이터 공유를 허용하지 않으므로 파트너는 해당 데이터를 Braze로 전송할 수 없습니다.

## Braze에서 Airbridge 클릭 추적 URL(선택 사항)

Braze 캠페인에서 클릭 추적 링크를 사용하면 어떤 캠페인이 앱 설치와 재참여를 유도하는지 쉽게 파악할 수 있습니다. 그 결과, 마케팅 활동을 보다 효과적으로 측정하고 ROI를 극대화하기 위해 더 많은 리소스를 투자할 위치에 대해 데이터에 기반한 의사 결정을 내릴 수 있습니다.

Airbridge 클릭 추적 링크를 시작하려면 [Airbridge](https://help.airbridge.io/en/guides/creating-a-new-tracking-link)를 방문하세요. 설정이 완료되면 Airbridge 클릭 추적 링크를 Braze 캠페인에 직접 삽입할 수 있습니다. Airbridge는 링크를 클릭한 사용자를 속성하기 위해 [확률적 기여도 방법론](https://help.airbridge.io/en/guides/identity-matching)을 사용할 것입니다. Braze 캠페인에서 기여도의 정확성을 개선하기 위해 Airbridge 추적 링크에 기기 식별자를 추가하는 것이 좋습니다. 이것은 링크를 클릭한 사용자를 결정적으로 속성할 것입니다.

{% tabs %}
{% tab Android %}
Android의 경우 Braze는 고객이 [Google 광고 ID 수집 (GAID)]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/optional_gaid_collection/#optional-google-advertising-id)에 옵트인할 수 있도록 합니다. GAID도 Airbridge SDK 통합을 통해 기본적으로 수집됩니다. 다음 Liquid 로직을 활용하여 Airbridge 클릭 추적 링크에 GAID를 포함할 수 있습니다.
{% raw %}
```
{% if most_recently_used_device.${platform} == 'android' %}
aifa={{most_recently_used_device.${google_ad_id}}}
{% endif %}
```
{% endraw %}
{% endtab %}

{% tab iOS %}
iOS의 경우, Braze와 Airbridge 모두 SDK 통합을 통해 기본적으로 IDFV를 자동으로 수집합니다. 이는 기기 식별자로 사용할 수 있습니다. 다음 Liquid 로직을 활용하여 Airbridge 클릭 추적 링크에 IDFV를 포함할 수 있습니다.

{% raw %}
```
{% if most_recently_used_device.${platform} == 'ios' %}
idfv={{most_recently_used_device.${id}}}
{% endif %}
```
{% endraw %}
{% endtab %}
{% endtabs %}

{% alert note %}
**이 권장 사항은 순전히 선택 사항입니다**<br>
현재 클릭 추적 링크에서 IDFV 또는 GAID와 같은 기기 식별자를 사용하지 않거나 향후에도 사용할 계획이 없는 경우에도 Airbridge는 여전히 확률적 모델링을 통해 이러한 클릭의 기여도를 측정할 수 있습니다.
{% endalert %}



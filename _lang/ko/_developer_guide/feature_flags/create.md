---
nav_title: 기능 플래그 생성
article_title: 기능 플래그 생성
page_order: 20
description: "이 참조 문서에서는 새 기능 롤아웃을 조정하기 위해 기능 플래그를 생성하는 방법을 다룹니다."
tool: Feature Flags
platform:
  - iOS
  - Android
  - Web

---

# 기능 플래그 생성

> 기능 플래그를 사용하면 선택한 사용자에 대해 원격으로 기능을 활성화 또는 비활성화할 수 있습니다. Braze 대시보드 내에서 새 기능 플래그를 만듭니다. 이 기능을 활성화할 사용자의 이름과 `ID`, 오디언스 및 비율을 입력합니다. 그런 다음, 앱이나 웹사이트의 코드에서 동일한 `ID`를 사용하여 비즈니스 로직의 특정 부분을 조건부로 실행할 수 있습니다. 기능 플래그와 Braze에서 기능 플래그를 사용하는 방법에 대해 자세히 알아보려면 [기능 플래그 정보를]({{site.baseurl}}/developer_guide/feature_flags/) 참조하세요.

## 전제 조건

### SDK 버전

기능 플래그를 사용하려면 SDK가 이 최소 버전 이상의 최신 상태인지 확인하세요.

{% sdk_min_versions swift:5.9.0 android:24.2.0 web:4.6.0 unity:4.1.0 cordova:5.0.0 reactnative:4.1.0 flutter:6.0.0 roku:1.0.0 %}

### Braze 권한

대시보드에서 기능 플래그를 관리하려면 관리자 [권한]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/)이 있거나 다음 권한이 있어야 합니다:

| 권한                                                                    | 할 수 있는 작업                           |
|-------------------------------------------------------------------------------|-------------------------------------------|
| **피처 플래그 관리**                                                      | 기능 플래그를 보고, 만들고, 편집합니다.     |
| **캠페인, 캔버스, 카드, 피처 플래그, 세그먼트, 미디어 라이브러리에 액세스하기** | 사용 가능한 기능 플래그 목록을 확인합니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## 기능 플래그 생성

### 1단계: 새 기능 플래그 만들기

**메시징** > **기능 플래그**로 이동한 다음, **기능 플래그 생성**을 선택합니다.

![Braze 대시보드에서 이전에 생성한 기능 플래그 목록]({% image_buster /assets/img/feature_flags/feature-flags-list.png %}){: style="max-width:75%"}

### 2단계: 세부 정보 입력

**세부** 정보에서 기능 플래그의 이름, ID 및 설명을 입력합니다.

| 필드        | 설명                                                                                                                                                                                                         |
|--------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 이름         | 마케터와 관리자를 위한 사람이 읽을 수 있는 제목입니다.                                                                                                                                                       |
| ID           | 코드에서 이 기능이 [사용자에 대해 활성화되어](#enabled) 있는지 확인하기 위해 사용할 고유 ID입니다. 이 아이디는 나중에 변경할 수 없으므로 계속하기 전에 [아이디 이름 지정 모범 사례를](#naming-conventions) 검토하세요. |
| 설명  | 기능 플래그에 대한 컨텍스트를 제공하는 선택적 설명입니다.                                                                                                                                            |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### 3단계: 사용자 지정 속성 만들기

**속성정보**에서 기능이 활성화된 경우 앱이 Braze SDK를 통해 액세스할 수 있는 커스텀 속성정보를 생성합니다. 각 변수에 문자열, 부울, 이미지, 타임스탬프, JSON 또는 숫자 값을 할당하고 기본값을 설정할 수 있습니다.

{% tabs local %}
{% tab 예제 %}
다음 예제에서 기능 플래그는 나열된 사용자 지정 속성을 사용하는 전자상거래 스토어의 품절 배너를 표시합니다: 

|등록정보 이름|유형|값|
|--|--|--|
|`banner_height`|`number`|`75`|
|`banner_color`|`string`|`blue`|
|`banner_text`|`string`|`Widgets are out of stock until July 1.`|
|`dismissible`|`boolean`|`false`|
|`homepage_icon`|`image`|`http://s3.amazonaws.com/[bucket_name]/`|
|`account_start`|`timestamp`|`2011-01-01T12:00:00Z`|
|`footer_settings`|`JSON`|`{ "colors": [ "red", "blue", "green" ], "placement": 123 }`|

{% alert tip %}
추가할 수 있는 속성 수에는 제한이 없습니다. 그러나 기능 플래그의 속성은 총 10KB로 제한됩니다. 속성 값과 키의 길이는 모두 255자로 제한됩니다.
{% endalert %}
{% endtab %}
{% endtabs %}

### 4단계: 타겟팅할 세그먼트 선택

기능 플래그를 롤아웃하기 전에 타겟팅할 사용자 [세그먼트]({{site.baseurl}}/user_guide/engagement_tools/segments/)를 선택해야 합니다. **필터 추가** 드롭다운 메뉴를 사용하여 타겟 오디언스에서 사용자를 필터링할 수 있습니다. 여러 필터를 추가하여 대상 범위를 더욱 좁히세요.

![두 개의 드롭다운 메뉴. 첫 번째는 세그먼트별 타겟 사용자를 읽습니다. 두 번째는 추가 필터입니다.]({% image_buster /assets/img/feature_flags/feature-flags-targeting.png %})

### 5단계: 롤아웃 트래픽 설정 {#rollout}

기본적으로 기능 플래그는 항상 비활성화되어 있으므로 전체 사용자 활성화에서 기능 릴리스 날짜를 분리할 수 있습니다. 롤아웃을 시작하려면 **롤아웃 트래픽** 슬라이더를 사용하거나 텍스트 상자에 백분율을 입력하여 선택한 세그먼트에서 이 새 기능을 받을 무작위 사용자의 비율을 선택합니다.

![0에서 100 사이의 롤아웃 트래픽이라는 레이블이 붙은 슬라이더.]({% image_buster /assets/img/feature_flags/feature-flags-rollout.png %}){: style="max-width:75%;"}

{% alert important %}
새 기능을 출시할 준비가 될 때까지 롤아웃 트래픽을 0% 넘게 설정하지 마세요. 대시보드에서 처음 기능 플래그를 정의할 때는 이 설정을 0%로 그대로 둡니다.
{% endalert %}

## 기능 플래그에 '활성화됨' 필드 사용 {#enabled}

기능 플래그를 정의한 후에는 특정 사용자에 대해 해당 기능이 활성화되어 있는지 여부를 확인하도록 앱 또는 사이트를 구성합니다. 이 기능이 활성화되면 사용 사례에 따라 몇 가지 작업을 설정하거나 기능 플래그의 변수 속성을 참조하게 됩니다. Braze SDK는 기능 플래그의 상태와 해당 속성정보를 앱으로 가져오는 getter 메서드를 제공합니다. 

세션 시작 시 기능 플래그를 자동으로 새로 고치므로 시작 시 최신 버전의 기능을 표시할 수 있습니다. SDK는 이러한 값을 캐시하여 오프라인 상태에서도 사용할 수 있도록 합니다. 

{% alert note %}
[기능 플래그 노출 횟수](#impressions)를 기록해야 합니다.
{% endalert %}

앱에 새로운 유형의 고객 프로필을 배포한다고 가정합니다. `ID`를 `expanded_user_profile`로 설정할 수 있습니다. 그런 다음, 앱에서 이 새 고객 프로필을 특정 사용자에게 표시해야 하는지 확인합니다. 예를 들어, 다음과 같습니다.

{% tabs %}
{% tab 자바스크립트 %}

```javascript
const featureFlag = braze.getFeatureFlag("expanded_user_profile");
if (featureFlag?.enabled) {
  console.log(`expanded_user_profile is enabled`);
} else {
  console.log(`expanded_user_profile is not enabled`);
}
```

{% endtab %}
{% tab Swift %}

```swift
let featureFlag = braze.featureFlags.featureFlag(id: "expanded_user_profile")
if featureFlag?.enabled == true {
  print("expanded_user_profile is enabled")
} else {
  print("expanded_user_profile is not enabled")
}
```
{% endtab %}
{% tab Java %}
```java
FeatureFlag featureFlag = braze.getFeatureFlag("expanded_user_profile");
if (featureFlag != null && featureFlag.getEnabled()) {
  Log.i(TAG, "expanded_user_profile is enabled");
} else {
  Log.i(TAG, "expanded_user_profile is not enabled");
}
```

{% endtab %}
{% tab Kotlin %}

```kotlin
val featureFlag = braze.getFeatureFlag("expanded_user_profile")
if (featureFlag?.enabled == true) {
  Log.i(TAG, "expanded_user_profile is enabled.")
} else {
  Log.i(TAG, "expanded_user_profile is not enabled.")
}
```

{% endtab %}
{% tab React Native %}

```javascript
const featureFlag = await Braze.getFeatureFlag("expanded_user_profile");
if (featureFlag?.enabled) {
  console.log(`expanded_user_profile is enabled`);
} else {
  console.log(`expanded_user_profile is not enabled`);
}
```

{% endtab %}
{% tab Unity %}
```csharp
var featureFlag = Appboy.AppboyBinding.GetFeatureFlag("expanded_user_profile");
if (featureFlag != null && featureFlag.Enabled) {
  Console.WriteLine("expanded_user_profile is enabled");
} else {
  Console.WriteLine("expanded_user_profile is not enabled");
}
```
{% endtab %}

{% tab 코르도바 %}
```javascript
const featureFlag = await BrazePlugin.getFeatureFlag("expanded_user_profile");
if (featureFlag?.enabled) {
  console.log(`expanded_user_profile is enabled`);  
} else {
  console.log(`expanded_user_profile is not enabled`);
}
```
{% endtab %}
{% tab Flutter %}
```dart
BrazeFeatureFlag? featureFlag = await braze.getFeatureFlagByID("expanded_user_profile");
if (featureFlag?.enabled == true) {
  print("expanded_user_profile is enabled");
} else {
  print("expanded_user_profile is not enabled");
}
```
{% endtab %}

{% tab Roku %}
```brightscript
featureFlag = m.braze.getFeatureFlag("expanded_user_profile")
if featureFlag <> invalid and featureFlag.enabled
  print "expanded_user_profile is enabled"
else
  print "expanded_user_profile is not enabled"
end if
```
{% endtab %}
{% endtabs %}

### 기능 플래그 노출 횟수 기록 {#impressions}

사용자가 새 기능과 상호 작용할 기회가 있었을 때 또는 기능이 비활성화되었을 때 상호 작용__할 수__ 있었던 경우(A/B 테스트 대조군의 경우) 기능 플래그 노출 횟수를 추적합니다. 기능 플래그 노출은 세션당 한 번만 기록됩니다. 

일반적으로 앱에서 기능 플래그를 참조하는 위치 바로 아래에 이 코드 줄을 넣으면 됩니다:

{% tabs %}
{% tab 자바스크립트 %}

```javascript
braze.logFeatureFlagImpression("expanded_user_profile");
```

{% endtab %}
{% tab Swift %}

```swift
braze.featureFlags.logFeatureFlagImpression(id: "expanded_user_profile")
```

{% endtab %}
{% tab Java %}

```java
braze.logFeatureFlagImpression("expanded_user_profile");
```

{% endtab %}
{% tab Kotlin %}

```kotlin
braze.logFeatureFlagImpression("expanded_user_profile")
```

{% endtab %}
{% tab React Native %}

```javascript
Braze.logFeatureFlagImpression("expanded_user_profile");
```

{% endtab %}
{% tab Unity %}

```csharp
Appboy.AppboyBinding.LogFeatureFlagImpression("expanded_user_profile");
```

{% endtab %}
{% tab 코르도바 %}
```javascript
BrazePlugin.logFeatureFlagImpression("expanded_user_profile");
```
{% endtab %}
{% tab Flutter %}
```dart
braze.logFeatureFlagImpression("expanded_user_profile");
```
{% endtab %}
{% tab Roku %}
```brightscript
m.Braze.logFeatureFlagImpression("expanded_user_profile");
```
{% endtab %}
{% endtabs %}

### 속성정보에 액세스 {#accessing-properties}

기능 플래그의 속성정보에 액세스하려면 대시보드에서 정의한 유형에 따라 다음 메서드 중 하나를 사용합니다.

참조한 프로퍼티가 존재하지 않는 경우 이 메서드는 `null` 을 반환합니다.

{% tabs %}
{% tab 자바스크립트 %}

```javascript
// Returns the Feature Flag instance
const featureFlag = braze.getFeatureFlag("expanded_user_profile");

// Returns the String property
const stringProperty = featureFlag.getStringProperty("color");

// Returns the boolean property
const booleanProperty = featureFlag.getBooleanProperty("expanded");

// Returns the number property
const numberProperty = featureFlag.getNumberProperty("height");

// Returns the Unix UTC millisecond timestamp property as a number
const timestampProperty = featureFlag.getTimestampProperty("account_start");

// Returns the image property as a String of the image URL
const imageProperty = featureFlag.getImageProperty("homepage_icon");

// Returns the JSON object property as a FeatureFlagJsonPropertyValue
const jsonProperty = featureFlag.getJsonProperty("footer_settings");
```

{% endtab %}
{% tab Swift %}

```swift
// Returns the Feature Flag instance
let featureFlag: FeatureFlag = braze.featureFlags.featureFlag(id: "expanded_user_profile")

// Returns the String property
let stringProperty: String? = featureFlag.stringProperty(key: "color")

// Returns the boolean property
let booleanProperty: Bool? = featureFlag.boolProperty(key: "expanded")

// Returns the number property as a double
let numberProperty: Double? = featureFlag.numberProperty(key: "height")

// Returns the Unix UTC millisecond timestamp property as an integer
let timestampProperty : Int? = featureFlag.timestampProperty(key: "account_start")

// Returns the image property as a String of the image URL
let imageProperty : String? = featureFlag.imageProperty(key: "homepage_icon")

// Returns the JSON object property as a [String: Any] dictionary
let jsonObjectProperty : [String: Any]? = featureFlag.jsonObjectProperty(key: "footer_settings")
```

{% endtab %}
{% tab Java %}

```java
// Returns the Feature Flag instance
FeatureFlag featureFlag = braze.getFeatureFlag("expanded_user_profile");

// Returns the String property
String stringProperty = featureFlag.getStringProperty("color");

// Returns the boolean property
Boolean booleanProperty = featureFlag.getBooleanProperty("expanded");

// Returns the number property
Number numberProperty = featureFlag.getNumberProperty("height");

// Returns the Unix UTC millisecond timestamp property as a long
Long timestampProperty = featureFlag.getTimestampProperty("account_start");

// Returns the image property as a String of the image URL
String imageProperty = featureFlag.getImageProperty("homepage_icon");

// Returns the JSON object property as a JSONObject
JSONObject jsonObjectProperty = featureFlag.getJSONProperty("footer_settings");
```

{% endtab %}
{% tab Kotlin %}

```kotlin
// Returns the Feature Flag instance
val featureFlag = braze.getFeatureFlag("expanded_user_profile")

// Returns the String property
val stringProperty: String? = featureFlag.getStringProperty("color")

// Returns the boolean property
val booleanProperty: Boolean? = featureFlag.getBooleanProperty("expanded")

// Returns the number property
val numberProperty: Number? = featureFlag.getNumberProperty("height")

// Returns the Unix UTC millisecond timestamp property as a long
val timestampProperty: Long? = featureFlag.getTimestampProperty("account_start")

// Returns the image property as a String of the image URL
val imageProperty: String?  = featureFlag.getImageProperty("homepage_icon")

// Returns the JSON object property as a JSONObject
val jsonObjectProperty: JSONObject? = featureFlag.getJSONProperty("footer_settings")
```

{% endtab %}
{% tab React Native %}

```javascript
// Returns the String property
const stringProperty = await Braze.getFeatureFlagStringProperty("expanded_user_profile", "color");

// Returns the boolean property
const booleanProperty = await Braze.getFeatureFlagBooleanProperty("expanded_user_profile", "expanded");

// Returns the number property
const numberProperty = await Braze.getFeatureFlagNumberProperty("expanded_user_profile", "height");

// Returns the Unix UTC millisecond timestamp property as a number
const timestampProperty = await Braze.getFeatureFlagTimestampProperty("expanded_user_profile", "account_start");

// Returns the image property as a String of the image URL
const imageProperty = await Braze.getFeatureFlagImageProperty("expanded_user_profile", "homepage_icon");

// Returns the JSON object property as an object
const jsonObjectProperty = await Braze.getFeatureFlagJSONProperty("expanded_user_profile", "footer_settings");
```

{% endtab %}
{% tab Unity %}

```csharp
// Returns the Feature Flag instance
var featureFlag = Appboy.AppboyBinding.GetFeatureFlag("expanded_user_profile");

// Returns the String property
var stringProperty = featureFlag.GetStringProperty("color");

// Returns the boolean property
var booleanProperty = featureFlag.GetBooleanProperty("expanded");

// Returns the number property as an integer
var integerProperty = featureFlag.GetIntegerProperty("height");

// Returns the number property as a double
var doubleProperty = featureFlag.GetDoubleProperty("height");

// Returns the Unix UTC millisecond timestamp property as a long
var timestampProperty = featureFlag.GetTimestampProperty("account_start");

// Returns the image property as a String of the image URL
var imageProperty = featureFlag.GetImageProperty("homepage_icon");

// Returns the JSON object property as a JSONObject
var jsonObjectProperty = featureFlag.GetJSONProperty("footer_settings");
```

{% endtab %}
{% tab 코르도바 %}

```javascript
// Returns the String property
const stringProperty = await BrazePlugin.getFeatureFlagStringProperty("expanded_user_profile", "color");

// Returns the boolean property
const booleanProperty = await BrazePlugin.getFeatureFlagBooleanProperty("expanded_user_profile", "expanded");

// Returns the number property
const numberProperty = await BrazePlugin.getFeatureFlagNumberProperty("expanded_user_profile", "height");

// Returns the Unix UTC millisecond timestamp property as a number
const timestampProperty = await BrazePlugin.getFeatureFlagTimestampProperty("expanded_user_profile", "account_start");

// Returns the image property as a String of the image URL
const imageProperty = await BrazePlugin.getFeatureFlagImageProperty("expanded_user_profile", "homepage_icon");

// Returns the JSON object property as an object
const jsonObjectProperty = await BrazePlugin.getFeatureFlagJSONProperty("expanded_user_profile", "footer_settings");
```

{% endtab %}
{% tab Flutter %}

```dart
// Returns the Feature Flag instance
BrazeFeatureFlag featureFlag = await braze.getFeatureFlagByID("expanded_user_profile");

// Returns the String property
var stringProperty = featureFlag.getStringProperty("color");

// Returns the boolean property
var booleanProperty = featureFlag.getBooleanProperty("expanded");

// Returns the number property
var numberProperty = featureFlag.getNumberProperty("height");

// Returns the Unix UTC millisecond timestamp property as an integer
var timestampProperty = featureFlag.getTimestampProperty("account_start");

// Returns the image property as a String of the image URL
var imageProperty = featureFlag.getImageProperty("homepage_icon");

// Returns the JSON object property as a Map<String, dynamic> collection
var jsonObjectProperty = featureFlag.getJSONProperty("footer_settings");
```

{% endtab %}
{% tab Roku %}

```brightscript
' Returns the String property
color = featureFlag.getStringProperty("color")

' Returns the boolean property
expanded = featureFlag.getBooleanProperty("expanded")

' Returns the number property
height = featureFlag.getNumberProperty("height")

' Returns the Unix UTC millisecond timestamp property
account_start = featureFlag.getTimestampProperty("account_start")

' Returns the image property as a String of the image URL
homepage_icon = featureFlag.getImageProperty("homepage_icon")

' Returns the JSON object property
footer_settings = featureFlag.getJSONProperty("footer_settings")
```

{% endtab %}
{% endtabs %}

### 모든 기능 플래그 목록 가져오기 {#get-list-of-flags}

{% tabs %}
{% tab 자바스크립트 %}

```javascript
const features = getAllFeatureFlags();
for(const feature of features) {
  console.log(`Feature: ${feature.id}`, feature.enabled);
}
```

{% endtab %}
{% tab Swift %}

```swift
let features = braze.featureFlags.featureFlags
for let feature in features {
  print("Feature: \(feature.id)", feature.enabled)
}
```

{% endtab %}
{% tab Java %}

```java
List<FeatureFlag> features = braze.getAllFeatureFlags();
for (FeatureFlag feature: features) {
  Log.i(TAG, "Feature: ", feature.getId(), feature.getEnabled());
}
```

{% endtab %}
{% tab Kotlin %}

```kotlin
val featureFlags = braze.getAllFeatureFlags()
featureFlags.forEach { feature ->
  Log.i(TAG, "Feature: ${feature.id} ${feature.enabled}")
}
```

{% endtab %}
{% tab React Native %}

```javascript
const features = await Braze.getAllFeatureFlags();
for(const feature of features) {
  console.log(`Feature: ${feature.id}`, feature.enabled);
}
```

{% endtab %}
{% tab Unity %}

```csharp
List<FeatureFlag> features = Appboy.AppboyBinding.GetAllFeatureFlags();
foreach (FeatureFlag feature in features) {
  Console.WriteLine("Feature: {0} - enabled: {1}", feature.ID, feature.Enabled);
}
```

{% endtab %}
{% tab 코르도바 %}
```javascript
const features = await BrazePlugin.getAllFeatureFlags();
for(const feature of features) {
  console.log(`Feature: ${feature.id}`, feature.enabled);
}
```
{% endtab %}
{% tab Flutter %}
```dart
List<BrazeFeatureFlag> featureFlags = await braze.getAllFeatureFlags();
featureFlags.forEach((feature) {
  print("Feature: ${feature.id} ${feature.enabled}");
});
```
{% endtab %}
{% tab Roku %}
```brightscript
features = m.braze.getAllFeatureFlags()
for each feature in features
      print "Feature: " + feature.id + " enabled: " + feature.enabled.toStr()
end for
```
{% endtab %}
{% endtabs %}

### 기능 플래그 새로 고침 {#refreshing}

세션 도중에 현재 사용자의 기능 플래그를 새로고침하여 Braze에서 최신 값을 가져올 수 있습니다.

{% alert tip %}
세션이 시작되면 새로 고침이 자동으로 수행됩니다. 새로 고침은 결제 페이지를 로드하기 전과 같이 중요한 사용자 작업 전이나 기능 플래그가 참조될 것을 알고 있는 경우에만 필요합니다.
{% endalert %}

{% tabs %}
{% tab 자바스크립트 %}

```javascript
braze.refreshFeatureFlags(() => {
  console.log(`Feature flags have been refreshed.`);
}, () => {
  console.log(`Failed to refresh feature flags.`);
});
```

{% endtab %}
{% tab Swift %}

```swift
braze.featureFlags.requestRefresh { result in
  switch result {
  case .success(let features):
    print("Feature flags have been refreshed:", features)
  case .failure(let error):
    print("Failed to refresh feature flags:", error)
  }
}
```

{% endtab %}
{% tab Java %}

```java
braze.refreshFeatureFlags();
```

{% endtab %}
{% tab Kotlin %}

```kotlin
braze.refreshFeatureFlags()
```

{% endtab %}
{% tab React Native %}

```javascript
Braze.refreshFeatureFlags();
```

{% endtab %}
{% tab Unity %}

```csharp
Appboy.AppboyBinding.RefreshFeatureFlags();
```

{% endtab %}
{% tab 코르도바 %}
```javascript
BrazePlugin.refreshFeatureFlags();
```
{% endtab %}
{% tab Flutter %}
```dart
braze.refreshFeatureFlags();
```
{% endtab %}
{% tab Roku %}
```brightscript
m.Braze.refreshFeatureFlags()
```
{% endtab %}
{% endtabs %}

### 변경 사항 수신 대기 {#updates}

SDK가 기능 플래그를 새로 고칠 때 앱을 수신 대기하고 업데이트하도록 Braze SDK를 구성할 수 있습니다.

사용자가 더 이상 기능을 사용할 수 없는 경우 앱을 업데이트하려는 때에 유용합니다. 예를 들어, 기능의 활성화 여부 또는 속성정보 값 중 하나를 기반으로 앱에서 일부 상태를 설정하는 경우가 이에 해당합니다.

{% tabs %}
{% tab 자바스크립트 %}

```javascript
// Register an event listener
const subscriptionId = braze.subscribeToFeatureFlagsUpdates((features) => {
  console.log(`Features were updated`, features);
});
// Unregister this event listener
braze.removeSubscription(subscriptionId);
```

{% endtab %}
{% tab Swift %}

```swift
// Create the feature flags subscription
// - You must keep a strong reference to the subscription to keep it active
let subscription = braze.featureFlags.subscribeToUpdates { features in
  print("Feature flags were updated:", features)
}
// Cancel the subscription
subscription.cancel()
```

{% endtab %}
{% tab Java %}

```java
braze.subscribeToFeatureFlagsUpdates(event -> {
  Log.i(TAG, "Feature flags were updated.");
  for (FeatureFlag feature: event.getFeatureFlags()) {
    Log.i(TAG, "Feature: ", feature.getId(), feature.getEnabled());
  }
});
```

{% endtab %}
{% tab Kotlin %}

```kotlin
braze.subscribeToFeatureFlagsUpdates() { event ->
  Log.i(TAG, "Feature flags were updated.")
  event.featureFlags.forEach { feature ->
    Log.i(TAG, "Feature: ${feature.id}")
  }
}
```

{% endtab %}
{% tab React Native %}

```javascript
// Register an event listener
Braze.addListener(braze.Events.FEATURE_FLAGS_UPDATED, (featureFlags) => {
  console.log(`featureFlagUpdates`, JSON.stringify(featureFlags));
});
```

{% endtab %}
{% tab Unity %}

변경 사항을 수신 대기하려면 **Braze 구성** > **기능 플래그**에서 **게임 오브젝트 이름** 및 **콜백 메서드 이름** 값을 애플리케이션의 해당 값으로 설정합니다.

{% endtab %}
{% tab 코르도바 %}
```javascript
// Register an event listener
BrazePlugin.subscribeToFeatureFlagUpdates((featureFlags) => {
    console.log(`featureFlagUpdates`, JSON.stringify(featureFlags));
});
```
{% endtab %}
{% tab Flutter %}

앱의 Dart 코드에서 다음 샘플 코드를 사용합니다:

```dart
// Create stream subscription
StreamSubscription featureFlagsStreamSubscription;

featureFlagsStreamSubscription = braze.subscribeToFeatureFlags((featureFlags) {
  print("Feature flags were updated");
});

// Cancel stream subscription
featureFlagsStreamSubscription.cancel();
```

그런 다음 iOS 네이티브 레이어에서도 이러한 변경을 수행합니다. Android 레이어에는 추가 단계가 필요하지 않습니다.

1. `featureFlags.subscribeToUpdates`를 구현하여 [subscribeToUpdates](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/featureflags-swift.class/subscribetoupdates(_:)) 설명서에서 설명한 대로 기능 플래그 업데이트에 가입합니다.

2. `featureFlags.subscribeToUpdates` 콜백 구현은 `BrazePlugin.processFeatureFlags(featureFlags)` 을 호출해야 합니다.

예제는 샘플 앱의 [AppDelegate.swift](https://github.com/braze-inc/braze-flutter-sdk/blob/master/example/ios/Runner/AppDelegate.swift) 를 참조하세요.

{% endtab %}
{% tab Roku %}
```brightscript
' Define a function called `onFeatureFlagChanges` to be called when feature flags are refreshed
m.BrazeTask.ObserveField("BrazeFeatureFlags", "onFeatureFlagChanges")
```
{% endtab %}

{% tab React 훅 %}
```typescript
import { useEffect, useState } from "react";
import {
  FeatureFlag,
  getFeatureFlag,
  removeSubscription,
  subscribeToFeatureFlagsUpdates,
} from "@braze/web-sdk";

export const useFeatureFlag = (id: string): FeatureFlag => {
  const [featureFlag, setFeatureFlag] = useState<FeatureFlag>(
    getFeatureFlag(id)
  );

  useEffect(() => {
    const listener = subscribeToFeatureFlagsUpdates(() => {
      setFeatureFlag(getFeatureFlag(id));
    });
    return () => {
      removeSubscription(listener);
    };
  }, [id]);

  return featureFlag;
};
```
{% endtab %}
{% endtabs %}

## 변경 로그 보기

기능 플래그의 체인지로그를 보려면 기능 플래그를 열고 **체인지로그**를 선택합니다.

!['변경 로그' 버튼이 강조 표시된 기능 플래그의 '수정' 페이지.]({% image_buster /assets/img/feature_flags/changelog/open_changelog.png %}){: style="max-width:60%;"}

여기에서 변경이 발생한 시기, 변경을 수행한 사람, 변경이 속한 카테고리 등을 검토할 수 있습니다.

![선택한 기능 플래그의 변경 로그입니다.]({% image_buster /assets/img/feature_flags/changelog/changelog.png %}){: style="max-width:90%;"}

## 기능 플래그에서 세분화 {#segmentation}

Braze는 현재 어떤 사용자가 기능 플래그를 활성화했는지 자동으로 추적합니다. [**기능 플래그** 필터]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/#feature-flags)를 사용하여 세그먼트 또는 타겟 메시지를 생성할 수 있습니다. 세그먼트 필터링에 대한 자세한 내용은 [세그먼트 생성]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/)을 참조하세요.

![필터 검색창에 '기능 플래그'를 입력한 '필터' 섹션]({% image_buster /assets/img/feature_flags/feature-flags-filter-name.png %}){: style="max-width:75%;"}

{% alert note %}
재귀 세그먼트를 방지하기 위해 다른 기능 플래그를 참조하는 세그먼트를 생성할 수 없습니다.
{% endalert %}

## 모범 사례

### 롤아웃과 캔버스 또는 실험을 결합하지 마세요.

다른 진입점에 의해 사용자가 활성화 및 비활성화되는 것을 방지하려면 롤아웃 슬라이더를 0보다 큰 값으로 설정하거나 캔버스 또는 실험에서 기능 플래그를 활성화해야 합니다. 캔버스나 실험에서 기능 플래그를 사용하려는 경우 롤아웃 비율을 0으로 유지하는 것이 모범 사례입니다.

### 이름 지정 규칙

코드를 명확하고 일관되게 유지하려면 기능 플래그 ID의 이름을 지정할 때 다음 형식을 사용하는 것이 좋습니다.

```plaintext
BEHAVIOR_PRODUCT_FEATURE
```

다음을 교체합니다:

| 입력 안내 | 설명                                                                                                               |
|-------------|---------------------------------------------------------------------------------------------------------------------------|
| `BEHAVIOR`  | 기능의 동작. 코드에서 동작이 기본적으로 비활성화되어 있는지 확인하고 기능 플래그 이름에 `disabled`와 같은 문구를 사용하지 마세요. |
| `PRODUCT`   | 해당 기능이 속한 제품입니다.                                                                                       |
| `FEATURE`    | 기능의 이름입니다.                                                                                                  |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

다음은 기능 플래그의 예제입니다. 여기서 `show`는 동작, `animation_profile`은 제품, `driver`는 기능입니다.

```plaintext
show_animation_profile_driver
```

### 미리 계획하기

항상 안전하게 작업하세요. 끄기 스위치가 필요할 수 있는 새로운 기능을 고려할 때는 새로운 앱 업데이트가 필요하다는 점을 깨닫는 것보다는 필요하지 않아도 기능 플래그를 포함하여 새 코드를 출시하는 것이 좋습니다.

### 설명하기

기능 플래그에 설명을 추가합니다. 이 필드는 Braze에서 선택 사항이지만, 다른 사람이 사용 가능한 기능 플래그를 검색할 때 궁금해할 수 있는 질문에 답하는 데 도움이 될 수 있습니다.

- 이 플래그의 활성화 및 동작을 담당하는 담당자에 대한 연락처 정보
- 이 플래그를 비활성화해야 하는 경우
- 이 플래그가 제어하는 새로운 기능에 대한 문서 또는 참고 사항 링크
- 기능 사용 방법에 대한 종속성 또는 참고 사항

### 오래된 기능 플래그 정리

기능의 롤아웃을 필요 이상으로 오랫동안 100% 상태로 두는 상황에 대해 모두가 책임을 안고 있습니다.

코드 및 Braze 대시보드를 깔끔하게 유지하려면 모든 사용자가 업그레이드하여 기능을 비활성화하는 옵션이 더 이상 필요하지 않게 된 후 코드 베이스에서 영구 기능 플래그를 제거합니다. 이렇게 하면 개발 환경의 복잡성을 줄일 수 있을 뿐만 아니라 기능 플래그 목록도 깔끔하게 정리할 수 있습니다.


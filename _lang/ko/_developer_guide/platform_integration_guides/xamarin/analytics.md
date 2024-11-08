---
nav_title: 분석
article_title: Xamarin용 분석
platform: 
  - Xamarin
  - iOS
  - Android
page_order: 4
description: "이 문서에서는 Xamarin 플랫폼용 iOS, Android 및 FireOS 분석을 다룹니다."

---
 
# Xamarin 분석

> Xamarin 플랫폼에 대한 분석을 생성하고 검토하는 방법을 알아보세요.

## 세션 추적

Braze SDK는 사용자 인게이지먼트를 계산하기 위해 Braze 대시보드에서 사용하는 세션 데이터 및 사용자를 이해하는 데 핵심적인 기타 분석을 보고합니다. SDK는 다음 세션 의미 체계에 따라 Braze 대시보드 내에서 볼 수 있는 세션 길이와 세션 수를 설명하는 '세션 시작' 및 '세션 종료' 데이터 포인트를 생성합니다.

사용자 ID를 설정하거나 세션을 시작하려면 사용자 ID 매개변수를 받는 `ChangeUser` 메서드를 사용합니다.

{% tabs %}
{% tab Android %}
```csharp
Braze.GetInstance(this).ChangeUser("user_id");
```

사용자 아이디를 설정하고 변경하는 시기와 방법에 대한 자세한 내용은 [Android 통합 지침을]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/setting_user_ids/) 참조하세요.

{% endtab %}
{% tab iOS %}
```csharp
App.braze?.ChangeUser("user_id");
```

사용자 아이디를 설정하고 변경하는 시기와 방법에 대한 자세한 내용은 [iOS 통합 지침을]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/setting_user_ids/) 참조하세요.

{% endtab %}
{% endtabs %}

## 사용자 지정 이벤트 로깅

`LogCustomEvent` 을 사용하여 Braze에서 사용자 지정 이벤트를 기록하여 앱의 사용 패턴에 대해 자세히 알아보고 대시보드에서 사용자의 행동에 따라 사용자를 세분화할 수 있습니다.

{% tabs %}
{% tab Android %}
```csharp
Braze.GetInstance(this).LogCustomEvent("event_name");
```

이벤트 추적 모범 사례 및 인터페이스에 대한 자세한 내용은 [Android 통합 지침]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/tracking_custom_events/)을 참조하세요.

{% endtab %}
{% tab iOS %}
```csharp
App.braze?.LogCustomEvent("event_name");
```

이벤트 추적 모범 사례 및 인터페이스에 대한 자세한 내용은 [iOS 통합 지침]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/tracking_custom_events/)을 참조하세요.

{% endtab %}
{% endtabs %}

## 구매 기록

`LogPurchase`를 사용하여 인앱 구매를 기록하면 여러 매출원에서 시간 경과에 따른 매출을 추적하고 생애주기 가치에 따라 사용자를 세분화할 수 있습니다.

Braze는 여러 통화로 구매를 지원합니다. USD가 아닌 다른 통화로 신고한 구매는 신고한 날짜의 환율을 기준으로 대시보드에 USD로 표시됩니다.

{% tabs %}
{% tab Android %}
```csharp
Braze.GetInstance(this).LogPurchase("product_id", "USD", new Java.Math.BigDecimal(3.50));
```

매출 추적 모범 사례 및 인터페이스에 대한 자세한 내용은 [Android 통합 지침]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/logging_purchases/)을 참조하세요.

{% endtab %}
{% tab iOS %}
```csharp
App.braze?.LogPurchase("product_id", "USD", 3.50);
```

매출 추적 모범 사례 및 인터페이스에 대한 자세한 내용은 [iOS 통합 지침]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/logging_purchases/)을 참조하세요.

{% endtab %}
{% endtabs %}

### 주문 수준에서 구매 기록

제품 수준 대신 주문 수준에서 구매를 기록하려면 주문 이름 또는 주문 카테고리를 `product_id` 으로 사용하면 됩니다. 자세한 내용은 [구매 개체 사양을]({{site.baseurl}}/api/objects_filters/purchase_object/#product-id-naming-conventions) 참조하세요. 

### 예약 키

다음 키는 예약되어 있으며 구매 속성으로 사용할 **수 없습니다**:

- `time`
- `product_id`
- `quantity`
- `event_name`
- `price`
- `currency`

## 사용자 지정 속성 로깅

Braze는 사용자에게 속성을 할당하는 방법을 제공합니다. 대시보드에서 이러한 속성에 따라 사용자를 필터링하고 세분화할 수 있습니다.

### 기본 사용자 속성

Braze에서 자동으로 수집한 사용자 속성을 할당하려면 SDK와 함께 제공되는 setter 메서드를 사용할 수 있습니다. 예를 들어 사용자의 이름을 설정할 수 있습니다:

{% tabs %}
{% tab Android %}
```csharp
Braze.GetInstance(this).CurrentUser.SetFirstName("first_name");
```

{% endtab %}
{% tab iOS %}

```csharp
App.braze?.User.SetFirstName("first_name");
```

{% endtab %}
{% endtabs %}

지원되는 속성은 다음과 같습니다:

- 이름
- 성
- 성별
- 생년월일
- 출생지
- 국가
- 전화번호
- 이메일

### 사용자 지정 사용자 속성

Braze는 사전 정의된 사용자 속성 메서드 외에도 애플리케이션의 데이터를 추적하기 위해 `SetCustomUserAttribute`를 사용하는 커스텀 속성도 제공합니다.

{% tabs %}
{% tab Android %}
```csharp
Braze.GetInstance(this).CurrentUser.SetCustomUserAttribute("custom_attribute_key", true);
```

속성 추적 모범 사례 및 인터페이스에 대한 자세한 내용은 [Android 통합 지침]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/setting_custom_attributes/)을 참조하세요.

{% endtab %}
{% tab iOS %}

```csharp
App.braze?.User.SetCustomAttributeWithKey("custom_attribute_key", true);
```

속성 추적 모범 사례 및 인터페이스에 대한 자세한 내용은 [iOS 통합 지침]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/setting_custom_attributes/)을 참조하세요.

{% endtab %}
{% endtabs %}

## 위치 추적

로깅 및 추적 분석의 예는 [Android MAUI](https://github.com/braze-inc/braze-xamarin-sdk/blob/master/appboy-component/samples/android-net-maui/BrazeAndroidMauiSampleApp/BrazeAndroidMauiSampleApp/MainActivity.cs) 및 [iOS MAUI](https://github.com/braze-inc/braze-xamarin-sdk/blob/master/appboy-component/samples/ios-net-maui/BrazeiOSMauiSampleApp/BrazeiOSMauiSampleApp/MainPage.xaml.cs) 샘플 애플리케이션을 참조하세요.

{% tabs %}
{% tab android %}
자세한 내용은 [Android 연동 지침을]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/location_tracking/) 참조하세요.
{% endtab %}

{% tab ios %}
로컬 추적을 지원하려면 [iOS를 참조하세요: 백그라운드 위치 사용](http://developer.xamarin.com/guides/cross-platform/application_fundamentals/backgrounding/part_4_ios_backgrounding_walkthroughs/location_walkthrough/) 및 [iOS 통합 지침]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/advanced_use_cases/locations_and_geofences/)을 참조하세요.
{% endtab %}
{% endtabs %}


---
nav_title: 초기 SDK 설정
article_title: Xamarin용 초기 SDK 설정
platform: 
  - Xamarin
  - iOS
  - Android
page_order: 0
toc_headers: h2
description: "이 문서에서는 Xamarin 플랫폼용 초기 iOS, Android 및 FireOS SDK 설정을 다룹니다."
search_rank: 1
---

# 초기 SDK 설정

> Xamarin용 Braze SDK를 설치하는 방법을 알아보세요. Braze SDK를 설치하면 기본 분석 기능과 사용자와 상호 작용할 수 있는 작동 중인 인앱 메시지가 제공됩니다. 

{% alert important %}
`version 3.0.0`부터 이 SDK는 .NET 6 이상을 사용해야 하며 Xamarin 프레임워크를 사용하는 프로젝트에 대한 지원을 제거합니다.
`version 4.0.0`부터 이 SDK는 Xamarin 및 Xamarin.Forms에 대한 지원을 중단하고 .NET MAUI에 대한 지원을 추가합니다.
Xamarin 지원 종료에 대해서는 [Microsoft의 정책](https://dotnet.microsoft.com/en-us/platform/support/policy/xamarin)을 참조하세요.
{% endalert %}

## 1단계: Xamarin 바인딩 받기

{% tabs %}
{% tab android %}
Xamarin 바인딩은 Xamarin 앱에서 기본 라이브러리를 사용하는 방법입니다. 바인딩 구현은 라이브러리에 대한 C# 인터페이스를 빌드한 다음, 애플리케이션에서 해당 인터페이스를 사용하는 작업으로 구성됩니다.  [Xamarin 설명서](http://developer.xamarin.com/guides/android/advanced_topics/java_integration_overview/binding_a_java_library_%28.jar%29/)를 참조하세요. Braze SDK 바인딩을 포함시키는 두 가지 방법(NuGet 사용 또는 소스에서 컴파일)이 있습니다.

{% subtabs local %}
{% subtab NuGet %}
가장 간단한 통합 방법은 [NuGet.org](https://www.nuget.org/) 중앙 리포지토리에서 Braze SDK를 가져오는 것입니다. Visual Studio 사이드바에서 `Packages` 폴더를 오른쪽 클릭하고 `Add Packages...`를 클릭합니다.  'Braze'를 검색하고 [`BrazePlatform.BrazeAndroidBinding`](https://www.nuget.org/packages/BrazePlatform.BrazeAndroidBinding/) 패키지를 프로젝트에 설치합니다.
{% endsubtab %}

{% subtab Source %}
두 번째 통합 방법은 [바인딩 소스를](https://github.com/braze-inc/braze-xamarin-sdk) 포함하는 것입니다. [`appboy-component/src/androidnet6`](https://github.com/braze-inc/braze-xamarin-sdk/tree/master/appboy-component/src/androidnet6/BrazeAndroidNet6Binding)에서 바인딩 소스 코드를 찾을 수 있습니다. Xamarin 애플리케이션에서 ```BrazeAndroidBinding.csproj```에 대한 프로젝트 참조를 추가하면 프로젝트와 함께 바인딩이 빌드되고 Braze Android SDK에 액세스할 수 있습니다.
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab ios %}
{% alert important %}
Xamarin SDK 버전 4.0.0 이상용 iOS 바인딩은 [Braze Swift SDK](https://github.com/braze-inc/braze-swift-sdk/)를 사용하는 반면, 이전 버전은 [레거시 AppboyKit SDK](https://github.com/Appboy/Appboy-ios-sdk)를 사용합니다.
{% endalert %}

Xamarin 바인딩은 Xamarin 앱에서 기본 라이브러리를 사용하는 방법입니다.  바인딩 구현은 라이브러리에 대한 C# 인터페이스를 빌드한 다음 애플리케이션에서 해당 인터페이스를 사용하는 작업으로 구성됩니다. Braze SDK 바인딩을 포함시키는 두 가지 방법(NuGet 사용 또는 소스에서 컴파일)이 있습니다.

{% subtabs local %}
{% subtab NuGet %}
가장 간단한 통합 방법은 [NuGet.org](https://www.nuget.org/) 중앙 리포지토리에서 Braze SDK를 가져오는 것입니다. Visual Studio 사이드바에서 `Packages` 폴더를 오른쪽 클릭하고 `Add Packages...`를 클릭합니다.  'Braze'를 검색하고 최신 Xamarin iOS NuGet 패키지([Braze.iOS.BrazeKit](https://www.nuget.org/packages/Braze.iOS.BrazeKit), [Braze.iOS.BrazeUI](https://www.nuget.org/packages/Braze.iOS.BrazeUI), [Braze.iOS.BrazeLocation]https://www.nuget.org/packages/Braze.iOS.BrazeLocation)를 프로젝트에 설치합니다.

또한 .NET MAUI로 쉽게 마이그레이션할 수 있도록 호환성 라이브러리 패키지([Braze.iOS.BrazeKitCompat](https://www.nuget.org/packages/Braze.iOS.BrazeKitCompat), [Braze.iOS.BrazeUICompat](https://www.nuget.org/packages/Braze.iOS.BrazeUICompat))도 제공합니다.
{% endsubtab %}

{% subtab Source %}
두 번째 통합 방법은 [바인딩 소스를](https://github.com/braze-inc/braze-xamarin-sdk) 포함하는 것입니다. [`appboy-component/src/iosnet6`](https://github.com/braze-inc/braze-xamarin-sdk/tree/master/appboy-component/src/iosnet6/BrazeiOSNet6Binding)에서 바인딩 소스 코드를 찾을 수 있습니다. Xamarin 애플리케이션에서 ```BrazeiOSBinding.csproj```에 대한 프로젝트 참조를 추가하면 프로젝트와 함께 바인딩이 빌드되고 Braze iOS SDK에 액세스할 수 있습니다. 프로젝트의 '참조' 폴더에 `BrazeiOSBinding.csproj`가 표시되는지 확인합니다.
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

## 2단계: Braze 인스턴스 구성

{% tabs %}
{% tab android %}
### 2.1단계: Braze.xml에서 Braze SDK 구성

라이브러리가 통합되었으므로 프로젝트의 `Resources/values` 폴더에서 `Braze.xml` 파일을 생성해야 합니다. 해당 파일의 내용은 다음 코드 스니펫과 비슷해야 합니다:

{% alert note %}
Braze 대시보드의 **설정** > **API 키에** 있는 API 키를 `YOUR_API_KEY` 으로 대체하세요.
<br><br>
[이전 탐색]({{site.baseurl}}/navigation)을 사용하는 경우 **개발자 콘솔** > **API 설정**에서 API 키를 찾을 수 있습니다.
{% endalert %}

```xml
  <?xml version="1.0" encoding="utf-8"?>
  <resources>
    <string translatable="false" name="com_braze_api_key">YOUR_API_KEY</string>
    <string translatable="false" name="com_braze_custom_endpoint">YOUR_CUSTOM_ENDPOINT_OR_CLUSTER</string>
    <string-array name="com_braze_internal_sdk_metadata">
      <item>XAMARIN</item>
      <item>NUGET</item>
    </string-array>
  </resources>
```
바인딩 소스를 수동으로 포함하는 경우 코드에서 `<item>NUGET</item>`을 제거합니다.

{% alert tip %}
예를 보려면 `Braze.xml`, [Android MAUI 샘플 앱을](https://github.com/braze-inc/braze-xamarin-sdk/blob/master/appboy-component/samples/android-net-maui/BrazeAndroidMauiSampleApp/BrazeAndroidMauiSampleApp/Resources/values/Braze.xml) 확인하세요.
{% endalert %}

### 2.2단계: Android 매니페스트에 필수 권한 추가

API 키를 추가했으므로 `AndroidManifest.xml` 파일에 다음 권한을 추가해야 합니다.

```xml
<uses-permission android:name="android.permission.INTERNET" />
```
`AndroidManifest.xml` 의 예는 [Android MAUI](https://github.com/braze-inc/braze-xamarin-sdk/blob/master/appboy-component/samples/android-net-maui/BrazeAndroidMauiSampleApp/BrazeAndroidMauiSampleApp/AndroidManifest.xml) 샘플 애플리케이션을 참조하세요.

### 2.3단계: 사용자 세션 추적 및 인앱 메시지 등록

사용자 세션 추적을 활성화하고 인앱 메시지를 위해 앱을 등록하려면 앱에서 `Application` 클래스의 `OnCreate()` 생애주기 메서드에 다음 호출을 추가합니다.

```kotlin
RegisterActivityLifecycleCallbacks(new BrazeActivityLifecycleCallbackListener());
```
{% endtab %}

{% tab ios %}
Braze 인스턴스를 설정할 때 다음 스니펫을 추가하여 인스턴스를 구성합니다.

{% alert note %}
Braze 대시보드의 **설정** > **API 키에** 있는 API 키를 `YOUR_API_KEY` 으로 대체하세요.

[이전 탐색]({{site.baseurl}}/navigation)을 사용하는 경우 **개발자 콘솔** > **API 설정**에서 API 키를 찾을 수 있습니다.
{% endalert %}

```csharp
var configuration = new BRZConfiguration("YOUR_API_KEY", "YOUR_ENDPOINT");
configuration.Api.AddSDKMetadata(new[] { BRZSDKMetadata.Xamarin });
braze = new Braze(configuration);
```

[iOS MAUI](https://github.com/braze-inc/braze-xamarin-sdk/blob/master/appboy-component/samples/ios-net-maui/BrazeiOSMauiSampleApp/BrazeiOSMauiSampleApp/App.xaml.cs) 샘플 애플리케이션의 `App.xaml.cs` 파일을 참조하세요.
{% endtab %}
{% endtabs %}

## 3단계: 통합 테스트

{% tabs %}
{% tab android %}
이제 애플리케이션을 실행하고 기기 정보 및 기타 분석과 함께 Braze 대시보드에 기록되는 세션을 확인할 수 있습니다. 기본 SDK 통합 모범 사례에 대한 자세한 내용은 [Android 통합 지침]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/)을 참조하세요.
{% endtab %}

{% tab ios %}
이제 애플리케이션을 실행하고 Braze 대시보드에 기록되는 세션을 확인할 수 있습니다. 기본 SDK 통합 모범 사례에 대한 자세한 내용은 [iOS 통합 지침]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/overview/)을 참조하세요.

{% alert important %}
현재 iOS SDK용 공개 Xamarin 바인딩은 iOS Facebook SDK(소셜 데이터 연결)에 연결되지 않으며, Braze에 IDFA를 전송하는 기능도 포함하지 않습니다.
{% endalert %}
{% endtab %}
{% endtabs %}

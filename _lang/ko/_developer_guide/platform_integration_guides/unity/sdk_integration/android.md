---
nav_title: Android
article_title: Unity용 SDK Android 통합
platform: 
  - Unity
  - Android
page_order: 0
description: "이 참조 문서에서는 Unity 플랫폼용 Android SDK 통합을 다룹니다."
search_rank: .9
---

# SDK Android 통합

> 이 참조 문서에서는 Unity 플랫폼용 Android SDK 통합을 다룹니다. Unity 애플리케이션에서 Braze를 실행하려면 다음 지침을 따르세요.

## 1단계: Braze Unity 패키지 선택

Braze [`.unitypackage`](https://docs.unity3d.com/Manual/AssetPackages.html)는 C# 인터페이스와 함께 Android 및 iOS 플랫폼용 기본 바인딩을 번들로 제공합니다.

[Braze Unity 릴리즈 페이지](https://github.com/Appboy/appboy-unity-sdk/releases)에서 여러 Braze Unity 패키지를 다운로드할 수 있습니다.
 
- `Appboy.unitypackage`
    - 이 패키지는 Braze 인앱 메시징 및 iOS의 콘텐츠 카드 기능이 제대로 작동하는 데 필요한 Braze Android 및 iOS SDK와 iOS SDK에 대한 [SDWebImage](https://github.com/SDWebImage/SDWebImage) 종속성을 번들로 제공합니다. SDWebImage 프레임워크는 GIF를 포함한 이미지를 다운로드하고 표시하는 데 사용됩니다. Braze의 모든 기능을 활용하려면 이 패키지를 다운로드하여 가져오세요.
- `Appboy-nodeps.unitypackage`
    - 이 패키지는 [SDWebImage](https://github.com/SDWebImage/SDWebImage) 프레임워크가 없다는 점을 제외하면 `Appboy.unitypackage` 과 유사합니다. 이 패키지는 iOS 앱에 SDWebImage 프레임워크가 표시되지 않도록 하려는 경우에 유용합니다.

**iOS**: iOS 프로젝트에 [SDWebImage](https://github.com/SDWebImage/SDWebImage) 종속성이 필요한지 확인하려면 [iOS 인앱 메시지 문서]({{ site.baseurl }}/developer_guide/platform_integration_guides/android/in-app_messaging/integration/).<br>
**Android**: Unity 2.6.0부터 번들로 제공되는 Braze Android SDK 아티팩트에는 [AndroidX](https://developer.android.com/jetpack/androidx) 종속성이 필요합니다. 이전에 `jetified unitypackage`를 사용했다면 해당되는 `unitypackage`로 안전하게 전환할 수 있습니다.

## 2단계: 패키지 가져오기

Unity 편집기에서 **자산 > 패키지 가져오기 > 커스텀 패키지**로 이동하여 패키지를 Unity 프로젝트로 가져옵니다 다음으로, **가져오기**를 클릭합니다.

또는 커스텀 Unity 패키지 가져오기에 대한 자세한 가이드는 [Unity 자산 패키지 가져오기](https://docs.unity3d.com/Manual/AssetPackages.html) 지침을 따릅니다. 

{% alert note %}
iOS 또는 Android 플러그인만 가져오려면 Braze `.unitypackage`를 가져올 때 `Plugins/Android` 또는 `Plugins/iOS` 하위 디렉토리를 선택 해제합니다.
{% endalert %}

## 3단계: AndroidManifest.xml 업데이트

애플리케이션을 실행하려면 Android Unity 프로젝트에 [`AndroidManifest.xml`](https://docs.unity3d.com/Manual/android-manifest.html)이 있어야 합니다. 또한 작동하려면 Braze에서 [`AndroidManifest.xml`](https://docs.unity3d.com/Manual/android-manifest.html)에 몇 가지를 추가해야 합니다.

### AndroidManifest.xml 구성

앱에 `AndroidManifest.xml`이 없는 경우 다음을 템플릿으로 사용할 수 있습니다. 그렇지 않으면 이미 `AndroidManifest.xml`이 있는 경우 기존 `AndroidManifest.xml`에 다음 중 누락된 섹션이 추가되었는지 확인합니다.

```xml
<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
          package="REPLACE_WITH_YOUR_PACKAGE_NAME">

  <uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
  <uses-permission android:name="android.permission.INTERNET" />

  <application android:icon="@drawable/app_icon" 
               android:label="@string/app_name">

    <!-- Calls the necessary Braze methods to ensure that analytics are collected and that push notifications are properly forwarded to the Unity application. -->
    <activity android:name="com.braze.unity.BrazeUnityPlayerActivity" 
      android:theme="@style/UnityThemeSelector"
      android:label="@string/app_name" 
      android:configChanges="fontScale|keyboard|keyboardHidden|locale|mnc|mcc|navigation|orientation|screenLayout|screenSize|smallestScreenSize|uiMode|touchscreen" 
      android:screenOrientation="sensor">
      <meta-data android:name="android.app.lib_name" android:value="unity" />
      <meta-data android:name="unityplayer.ForwardNativeEventsToDalvik" android:value="true" />
      <intent-filter>
        <action android:name="android.intent.action.MAIN" />
        <category android:name="android.intent.category.LAUNCHER" />
      </intent-filter>
    </activity>

    <!-- A Braze specific FirebaseMessagingService used to handle push notifications. -->
    <service android:name="com.braze.push.BrazeFirebaseMessagingService"
      android:exported="false">
      <intent-filter>
        <action android:name="com.google.firebase.MESSAGING_EVENT" />
      </intent-filter>
    </service>
  </application>
</manifest>
```

> `Assets/Plugins/Android/AndroidManifest.xml` 아래에 `AndroidManifest.xml`이 있어야 합니다. 자세한 내용은 [Unity AndroidManifest 설명서](https://docs.unity3d.com/Manual/android-manifest.html)를 참조하세요.

> `AndroidManifest.xml` 파일에 등록된 모든 활동 클래스는 Braze Android SDK와 완전히 통합되어야 합니다. 자체 활동 클래스를 추가하는 경우, 분석이 수집되고 있는지 확인하기 위해 [Unity 활동 통합 지침](#extending-braze-unity-player)을 따라야 합니다.

{% alert note %}
최종 `AndroidManifest.xml`에는 `"android.intent.category.LAUNCHER"`가 있는 단일 활동만 포함되어야 합니다.
{% endalert %}

### 패키지 이름으로 AndroidManifest.xml 업데이트

패키지 이름을 찾으려면 **파일 > 빌드 설정 > 플레이어 설정 > Android 탭**을 클릭합니다.
![]({% image_buster /assets/img_archive/UnityPackageName.png %})

`AndroidManifest.xml`에서 `REPLACE_WITH_YOUR_PACKAGE_NAME`의 모든 인스턴스는 이전 단계의 `Package Name`으로 바뀌어야 합니다.

## 4단계: 그레이들 종속성 추가 {#unity-android-gradle-configuration}

Unity 프로젝트에 그래들 종속성을 추가하려면 먼저 퍼블리싱 설정에서 ['커스텀 메인 그래들 템플릿'](https://docs.unity3d.com/Manual/class-PlayerSettingsAndroid.html#Publishing) 을 활성화합니다. 그러면 프로젝트에서 사용할 템플릿 gradle 파일이 생성됩니다. gradle 파일은 설정 종속성 및 기타 빌드 시점 프로젝트 설정을 처리합니다. 자세한 내용은 Braze Unity 샘플 앱의 [mainTemplate.gradle](https://github.com/braze-inc/braze-unity-sdk/blob/master/unity-samples/Assets/Plugins/Android/mainTemplate.gradle).

다음 종속성이 필요합니다:

```groovy
implementation 'com.google.firebase:firebase-messaging:22.0.0'
implementation "androidx.swiperefreshlayout:swiperefreshlayout:1.1.0"
implementation "androidx.recyclerview:recyclerview:1.2.1"
implementation "org.jetbrains.kotlin:kotlin-stdlib:1.6.0"
implementation "org.jetbrains.kotlinx:kotlinx-coroutines-android:1.6.1"
implementation 'androidx.core:core:1.6.0'
```

[외부 종속성 매니저](https://github.com/googlesamples/unity-jar-resolver)를 사용하여 이러한 종속성을 설정할 수도 있습니다.

## 5단계: SDK 구성 {#unity-static-configuration}

Braze는 Unity Android 통합을 자동화하기 위한 기본 Unity 솔루션을 제공합니다. 

1. Unity 편집기에서 **Braze > Braze 구성**으로 이동하여 Braze 구성 설정을 엽니다.
2. **Unity Android 통합 자동화** 확인란을 선택합니다.
3. **Braze API 키** 필드에 Braze 대시보드의 **설정 관리**에서 찾은 애플리케이션의 API 키를 입력합니다.

{% alert note %}
이 자동 통합은 프로젝트 빌드 중에 구성 값이 충돌할 수 있으므로 수동으로 생성한 `braze.xml` 파일과 함께 사용해서는 안 됩니다. 수동 `braze.xml`이 필요한 경우 자동 통합을 비활성화합니다.
{% endalert %}

## 기본 SDK 통합 완료

이제 Braze가 애플리케이션에서 데이터를 수집하며 기본 통합이 완료됩니다. 통합 푸시에 대한 자세한 내용은 다음 문서를 참조하세요: [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/unity/push_notifications/android/) 및 [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/unity/push_notifications/ios/), [인앱 메시지]({{site.baseurl}}/developer_guide/platform_integration_guides/unity/in-app_messaging/), [콘텐츠 카드]({{site.baseurl}}/developer_guide/platform_integration_guides/unity/content_cards/).

고급 SDK 통합 옵션에 대한 자세한 내용은 [고급 구현]({{site.baseurl}}/developer_guide/platform_integration_guides/unity/sdk_integration/advanced_use_cases/#android-sdk-advanced)을 참조하세요.


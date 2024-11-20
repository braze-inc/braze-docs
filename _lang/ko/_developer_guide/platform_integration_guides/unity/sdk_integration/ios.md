---
nav_title: iOS
article_title: Unity용 SDK iOS 통합
platform: 
  - Unity
  - iOS
page_order: 1
description: "이 참조 문서에서는 Unity 플랫폼용 iOS SDK 통합을 다룹니다."
search_rank: .9
---

# SDK iOS 통합

> 이 참조 문서에서는 Unity 플랫폼용 iOS SDK 통합을 다룹니다. Unity 애플리케이션에서 Braze를 실행하려면 다음 가이드를 따르세요. 

수동 통합에서 자동 통합으로 전환하는 경우 [자동 통합으로 전환](#transitioning-from-manual-to-automated-integration-ios) 지침을 읽어보세요.

## 1단계: Braze Unity 패키지 선택

Braze [`.unitypackage`](https://docs.unity3d.com/Manual/AssetPackages.html)는 C# 인터페이스와 함께 Android 및 iOS 플랫폼용 기본 바인딩을 번들로 제공합니다.

Braze Unity 패키지는 다음과 같은 두 가지 통합 옵션을 사용해 [Braze Unity 릴리즈 페이지](https://github.com/Appboy/appboy-unity-sdk/releases)에서 다운로드할 수 있습니다.

1. `Appboy.unitypackage`만
  - 이 패키지는 추가 종속성 없이 Braze Android 및 iOS SDK를 번들로 제공합니다. 이 통합 방법을 사용하는 경우 iOS에서 Braze 인앱 메시징 및 콘텐츠 카드 기능이 제대로 작동하지 않습니다. 커스텀 코드 없이 전체 Braze 기능을 활용하려는 경우 대신 아래 옵션을 사용합니다.
  - 이 통합 옵션을 사용하려면 Unity UI의 'Braze 구성' 아래에서 `Import SDWebImage dependency` 옆의 확인란이 *선택 해제*되었는지 확인합니다.
2. `Appboy.unitypackage`(`SDWebImage` 포함)
  - 이 통합 옵션은 Braze 인앱 메시징 및 iOS의 콘텐츠 카드 기능이 제대로 작동하는 데 필요한 Braze Android 및 iOS SDK와 iOS SDK에 대한 [SDWebImage](https://github.com/SDWebImage/SDWebImage) 종속성을 번들로 제공합니다. `SDWebImage` 프레임워크는 GIF를 포함한 이미지를 다운로드하고 표시하는 데 사용됩니다. Braze의 모든 기능을 활용하려면 이 패키지를 다운로드하여 가져오세요.
  - `SDWebImage`를 자동으로 가져오려면 Unity UI의 'Braze 구성' 아래 `Import SDWebImage dependency` 옆의 확인란을 *선택*해야 합니다.

**iOS**: iOS 프로젝트에 [SDWebImage](https://github.com/SDWebImage/SDWebImage) 종속성이 필요한지 확인하려면 [iOS 인앱 메시지 문서]({{ site.baseurl }}/developer_guide/platform_integration_guides/swift/in-app_messaging/overview/).<br>
**Android**: Unity 2.6.0부터 번들로 제공되는 Braze Android SDK 아티팩트에는 [AndroidX](https://developer.android.com/jetpack/androidx) 종속성이 필요합니다. 이전에 `jetified unitypackage`를 사용했다면 해당되는 `unitypackage`로 안전하게 전환할 수 있습니다.

## 2단계: 패키지 가져오기

Unity 편집기에서 **자산 > 패키지 가져오기 > 커스텀 패키지**로 이동하여 패키지를 Unity 프로젝트로 가져옵니다 다음으로, **가져오기**를 클릭합니다.

또는 커스텀 Unity 패키지 가져오기에 대한 자세한 가이드는 [Unity 자산 패키지 가져오기](https://docs.unity3d.com/Manual/AssetPackages.html) 지침을 따릅니다. 

{% alert note %}
iOS 또는 Android 플러그인만 가져오려면 Braze `.unitypackage`를 가져올 때 `Plugins/Android` 또는 `Plugins/iOS` 하위 디렉토리를 선택 해제합니다.
{% endalert %}

## 3단계: API 키 설정

Braze는 Unity iOS 통합을 자동화하기 위한 기본 Unity 솔루션을 제공합니다. 이 솔루션은 Unity의 [`PostProcessBuildAttribute`](http://docs.unity3d.com/ScriptReference/Callbacks.PostProcessBuildAttribute.html)를 사용하여 빌드된 Xcode 프로젝트를 수정하고 `IMPL_APP_CONTROLLER_SUBCLASS` 매크로를 사용하여 `UnityAppController`를 서브클래스로 구성합니다.

1. Unity 편집기에서 **Braze > Braze 구성**으로 이동하여 Braze 구성 설정을 엽니다.
2. **Unity iOS 통합 자동화** 확인란을 선택합니다.
3. **Braze API 키** 필드에 **설정 관리**에서 찾은 애플리케이션의 API 키를 입력합니다.

![]({% image_buster /assets/img_archive/unity-ios-appboyconfig.png %})

애플리케이션에서 이미 다른 `UnityAppController` 서브클래스를 사용하고 있는 경우, 서브클래스 구현을 `AppboyAppDelegate.mm`과 병합해야 합니다.

## 기본 SDK 통합 완료

이제 Braze가 애플리케이션에서 데이터를 수집하며 기본 통합이 완료됩니다. 푸시 통합에 대한 자세한 내용은 다음 문서를 참조하세요. [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/unity/push_notifications/android/) 및 [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/unity/push_notifications/ios/), [인앱 메시지]({{site.baseurl}}/developer_guide/platform_integration_guides/unity/in-app_messaging/), [콘텐츠 카드]({{site.baseurl}}/developer_guide/platform_integration_guides/unity/content_cards/).

고급 SDK 통합 옵션에 대한 자세한 내용은 [고급 구현]({{site.baseurl}}/developer_guide/platform_integration_guides/unity/sdk_integration/advanced_use_cases/#ios-sdk-advanced)을 참조하세요.


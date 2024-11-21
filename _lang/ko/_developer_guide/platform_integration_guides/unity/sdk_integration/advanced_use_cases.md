---
nav_title: 고급 구현
article_title: 고급 SDK 구현
platform: 
  - Unity
  - iOS
  - Android
page_order: 2
description: "이 참조 문서에서는 Unity 플랫폼용 고급 SDK 구현을 다룹니다."
---

# 고급 구현

> 이 참조 문서에서는 Unity 플랫폼용 고급 SDK 구현을 다룹니다.

## Unity 패키지 커스터마이징

제공된 스크립트를 사용하여 Braze Unity 패키지를 사용자 지정하고 내보낼 수 있습니다.

1. [Braze Unity SDK GitHub 프로젝트를](https://github.com/appboy/appboy-unity-sdk) 복제합니다:

	```bash
	git clone git@github.com:braze-inc/braze-unity-sdk.git
	```
2. `braze-unity-sdk/scripts` 디렉토리에서 `./generate_package.sh`를 실행하여 Unity 패키지를 내보냅니다. Unity는 `generate_package.sh`를 실행하는 동안 열려 있어야 합니다.
3. 패키지는 `braze-unity-sdk/unity-package/` 으로 내보내집니다.
4. Unity 에디터에서 **에셋** > **패키지 임포트** > **커스텀 패키지로** 이동하여 원하는 패키지를 Unity 프로젝트로 임포트합니다.
5. (선택 사항) 가져오지 않으려는 파일은 모두 선택 해제합니다.

`generate_package.sh` 및 `Assets/Editor/Build.cs`에 있는 내보내기 스크립트를 모두 편집하여 내보낸 Unity 패키지를 사용자 지정할 수 있습니다.

## Prime 31 호환성

Prime31 플러그인과 함께 Braze Unity 플러그인을 사용하려면 프로젝트의 `AndroidManifest.xml`을 편집하여 Prime31 호환 활동 클래스를 사용합니다. 의 모든 참조를 변경합니다.
`com.braze.unity.BrazeUnityPlayerActivity`부터 `com.braze.unity.prime31compatible.BrazeUnityPlayerActivity`까지

## Amazon ADM 푸시

Braze는 [Amazon ADM 푸시](https://developer.amazon.com/public/apis/engage/device-messaging)를 Unity 앱에 통합하는 기능을 지원합니다. Amazon ADM 푸시를 통합하려면 ADM API 키가 포함된 `api_key.txt` 파일을 만들어 `Plugins/Android/assets/` 폴더에 넣습니다.  Amazon ADM과 Braze를 통합하는 방법에 대한 자세한 내용은 [ADM 푸시 통합 지침]({{site.baseurl}}/developer_guide/platform_integration_guides/unity/push_notifications/adm_push_notifications/)을 참조하세요.

## Android SDK 고급 구현 옵션 {#android-sdk-advanced}

### Unity 에디터에서 자세한 로깅 활성화하기
Unity 편집기에서 상세 로깅을 활성화하려면 다음을 수행합니다.

1. **Braze** > **Braze 구성**으로 이동하여 Braze 구성 설정을 엽니다.
2. **Braze Android 설정 표시** 드롭다운을 클릭합니다.
3. **SDK 로그 수준** 필드에 '0' 값을 입력합니다.

### Braze Unity 플레이어 확장(Android) {#extending-braze-unity-player}

제공된 예제 `AndroidManifest.xml` 파일에는 하나의 활동 클래스([`BrazeUnityPlayerActivity`](https://github.com/braze-inc/braze-android-sdk/blob/e804cb3a10ae68364b354b52abf1bef8a0d1a9dc/android-sdk-unity/src/main/java/com/braze/unity/BrazeUnityPlayerActivity.kt))가 등록되어 있습니다. 이 클래스는 Braze SDK와 통합되어 있으며 세션 처리, 인앱 메시지 등록, 푸시 알림 분석 로깅 등을 통해 `UnityPlayerActivity`를 확장합니다. `UnityPlayerActivity` 클래스 확장에 대한 자세한 내용은 [Unity](https://docs.unity3d.com/Manual/AndroidUnityPlayerActivity.html)를 참조하세요.

라이브러리 또는 플러그인 프로젝트에서 커스텀 `UnityPlayerActivity`를 만드는 경우, 커스텀 기능을 Braze와 통합하려면 `BrazeUnityPlayerActivity`를 확장해야 합니다. `BrazeUnityPlayerActivity` 확장 작업을 시작하기 전에, Unity 프로젝트에 Braze를 통합하기 위한 지침을 따르세요.
1. [Braze Android SDK 통합 지침]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/)에서 설명한 대로 라이브러리 또는 플러그인 프로젝트에 Braze Android SDK를 종속성으로 추가합니다.
2. Unity 전용 기능이 포함된 Unity `.aar`을 Unity용으로 빌드 중인 Android 라이브러리 프로젝트에 통합합니다. `appboy-unity.aar`은 [공개 리포지토리](https://github.com/braze-inc/braze-unity-sdk/tree/master/Assets/Plugins/Android)에서 사용할 수 있습니다. Unity 라이브러리가 성공적으로 통합되면 `BrazeUnityPlayerActivity`를 확장하도록 `UnityPlayerActivity`를 수정합니다.
3. 라이브러리 또는 플러그인 프로젝트를 내보내고 평소처럼 `/<your-project>/Assets/Plugins/Android` 에 끌어다 놓습니다. Braze 소스 코드는 이미 `/<your-project>/Assets/Plugins/Android`에 있으므로 라이브러리나 플러그인에 포함하지 마세요.
4. `/<your-project>/Assets/Plugins/Android/AndroidManifest.xml` 을 수정하여 `BrazeUnityPlayerActivity` 하위 클래스를 기본 활동으로 지정합니다.

이제 Braze와 완전히 통합되고 커스텀 `UnityPlayerActivity` 기능이 포함된 `.apk` 패키지를 Unity IDE에서 생성할 수 있습니다.

## iOS SDK 고급 구현 옵션 {#ios-sdk-advanced}

### Unity 에디터에서 자세한 로깅 활성화하기
Unity 편집기에서 상세 로깅을 활성화하려면 다음을 수행합니다.

1. **Braze** > **Braze 구성**으로 이동하여 Braze 구성 설정을 엽니다.
2. **Braze iOS 설정 표시** 드롭다운을 클릭합니다.
3. **SDK 로그 수준** 필드에 '0' 값을 입력합니다.

### SDK 확장(iOS)

SDK의 동작을 확장하려면 [Braze Unity SDK GitHub 프로젝트](https://github.com/appboy/appboy-unity-sdk)를 분기로 생성하고 필요한 사항을 변경합니다.

수정한 코드를 Unity 패키지로 게시하려면 [고급 사용 사례]({{site.baseurl}}/developer_guide/platform_integration_guides/unity/advanced_use_cases/)를 참조하세요.

### 수동 통합에서 자동 통합으로 전환하기(iOS)

Braze Unity SDK에서 제공하는 자동화된 iOS 통합 기능을 활용하려면 수동 통합에서 자동 통합으로 전환하는 다음 단계를 따르세요.

1. Xcode 프로젝트의 `UnityAppController` 서브클래스에서 모든 Braze 관련 코드를 제거합니다.
2. Unity 또는 Xcode 프로젝트에서 Braze iOS 라이브러리를 제거하고(예: `Appboy_iOS_SDK.framework` 및 `SDWebImage.framework`) Unity 프로젝트로 [Braze Unity 패키지를 가져옵니다](#step-1-importing-the-braze-unity-package).
3. [Unity를 통해 API 키 설정](#step-2-setting-your-api-key)에 대한 통합 지침을 따르세요.


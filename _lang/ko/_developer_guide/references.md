---
nav_title: 참조 및 샘플 앱
article_title: "Braze SDK 참조, 리포지토리 및 샘플 앱"
page_order: 5.5
description: "각 Braze SDK에 속한 참조 문서, GitHub 리포지토리 및 샘플 앱의 목록입니다."
---

# 참조, 리포지토리 및 샘플 앱

> 각 Braze SDK에 속한 참조 문서, GitHub 리포지토리 및 샘플 앱의 목록입니다. SDK의 참조 문서에는 사용 가능한 클래스, 유형, 함수 및 변수가 자세히 설명되어 있습니다. GitHub 리포지토리는 해당 SDK의 기능 및 속성 선언, 코드 변경 및 버전 관리에 대한 인사이트를 제공합니다. 각 저장소에는 Braze 기능을 테스트하거나 자체 애플리케이션과 함께 구현하는 데 사용할 수 있는 완전히 빌드 가능한 샘플 애플리케이션도 포함되어 있습니다.

## 리소스 목록

{% alert note %}
현재 일부 SDK에는 전용 참조 문서가 없지만 적극적으로 작업 중입니다.
{% endalert %}

| 플랫폼          | 참조                                                                                                                                    | 리포지토리                                                                 | 샘플 앱                                                                |
| ----------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| Android SDK       | [참조 문서](https://braze-inc.github.io/braze-android-sdk/kdoc/index.html)                                                                           | [GitHub 리포지토리](https://github.com/braze-inc/braze-android-sdk)      | [샘플 앱](https://github.com/braze-inc/braze-android-sdk/tree/master/samples)      |
| Swift SDK         | [참조 문서](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze)                                                                | [GitHub 리포지토리](https://github.com/braze-inc/braze-swift-sdk)            | [샘플 앱](https://github.com/braze-inc/braze-swift-sdk/tree/main/Examples)            |
| 웹 SDK           | [참조 문서](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initialize)                                                               | [GitHub 리포지토리](https://github.com/braze-inc/braze-web-sdk)              | [샘플 앱](https://github.com/braze-inc/braze-web-sdk/tree/master/sample-builds)              |
| Cordova SDK       | [선언 파일](https://github.com/braze-inc/braze-cordova-sdk/blob/master/www/BrazePlugin.js)                                      | [GitHub 리포지토리](https://github.com/braze-inc/braze-cordova-sdk)      | [샘플 앱](https://github.com/braze-inc/braze-cordova-sdk/tree/master/sample-project)      |
| Flutter SDK       | [참조 문서](https://pub.dev/documentation/braze_plugin/latest/braze_plugin/)                                                   | [GitHub 리포지토리](https://github.com/braze-inc/braze-flutter-sdk)      | [샘플 앱](https://github.com/braze-inc/braze-flutter-sdk/tree/master/example)      |
| 리액트 네이티브 SDK  | [선언 파일](https://github.com/braze-inc/braze-react-native-sdk/blob/master/src/index.d.ts)                   | [GitHub 리포지토리](https://github.com/braze-inc/braze-react-native-sdk) | [샘플 앱](https://github.com/braze-inc/braze-react-native-sdk/tree/master/BrazeProject) |
| Roku SDK          | N/A                                                                                                                                                         | [GitHub 리포지토리](https://github.com/braze-inc/braze-roku-sdk)            | [샘플 앱](https://github.com/braze-inc/braze-roku-sdk/tree/main/torchietv)            |
| Unity SDK         | [선언 파일](https://github.com/braze-inc/braze-unity-sdk/blob/master/Assets/Plugins/Appboy/BrazePlatform.cs)     | [GitHub 리포지토리](https://github.com/braze-inc/braze-unity-sdk)          | [샘플 앱](https://github.com/braze-inc/braze-unity-sdk/tree/master/unity-samples)          |
| 언리얼 엔진 SDK | N/A                                                                                                                                                         | [GitHub 리포지토리](https://github.com/braze-inc/braze-unreal-sdk)        | [샘플 앱](https://github.com/braze-inc/braze-unreal-sdk/tree/master/BrazeSample)        |
| .NET MAUI SDK       | N/A                                                                                                                                                         | [GitHub 리포지토리](https://github.com/braze-inc/braze-xamarin-sdk)      | [샘플 앱](https://github.com/braze-inc/braze-xamarin-sdk/tree/master/appboy-component/samples)      |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## 샘플 앱 빌드

{% tabs %}
{% tab Android %}
### "드로이드보이" 만들기

Android SDK 깃허브 리포지토리 내 테스트 [애플리케이션브레이즈](https://github.com/braze-inc/braze-android-sdk "안드로이드 깃허브 리포지토리의") 이름은 Droidboy입니다. 다음 지침에 따라 프로젝트와 함께 모든 기능을 갖춘 사본을 빌드합니다.

1. 새 [워크스페이스]({{site.baseurl}}/developer_guide/platform_wide/app_group_configuration/#app-group-configuration)를 생성하고Braze API 식별자 키를 기록합니다.<br><br>
2. `/droidboy/res/values/braze.xml` 내의 적절한 위치(각각 `com_braze_push_fcm_sender_id` 및 `com_braze_api_key`라는 문자열의 태그 사이)에 FCM 발신자 ID와 Braze API 식별자 키를 복사합니다.<br><br>
3. **설정 관리** 아래 워크스페이스 설정에 FCM 서버 키와 서버 ID를 복사합니다.<br><br>
4. Droidboy APK를 어셈블링하려면 SDK 디렉토리 내에서 `./gradlew assemble`을 실행합니다. Windows에서는 `gradlew.bat` 을 사용합니다.<br><br>
5. 테스트 기기에서 Droidboy APK를 자동으로 설치하려면 SDK 디렉토리 내에서 `./gradlew installDebug`를 실행합니다.

### "헬로 브레이즈" 구축

Hello Braze 테스트 애플리케이션은 Braze SDK의 최소 사용 사례를 보여주며, 추가적으로 Braze SDK를 Gradle 프로젝트에 쉽게 통합하는 방법을 보여줍니다.

1. **설정 관리** 페이지에서 API 식별자 키를 `res/values` 폴더의 `braze.xml` 파일에 복사합니다.
![]({% image_buster /assets/img_archive/hello_appboy.png %})<br><br>
2. 기기 또는 에뮬레이터에 샘플 앱을 설치하려면 SDK 디렉토리 내에서 다음 명령을 실행합니다.
```
./gradlew installDebug
```
`ANDROID_HOME` 변수가 제대로 설정되어 있지 않거나 `local.properties` 폴더에 유효한 `sdk.dir` 폴더가 없는 경우, 이 플러그인이 기본 SDK도 설치해 줍니다. 자세한 내용은 [플러그인 저장소를](https://github.com/JakeWharton/sdk-manager-plugin) 참조하세요.

Android SDK 빌드 시스템에 대한 자세한 내용은 [GitHub 리포지토리 README](https://github.com/braze-inc/braze-android-sdk/blob/master/README.md)를 참조하세요.
{% endtab %}

{% tab swift %}
### Swift 테스트 앱 빌드

이 지침을 따라 테스트 애플리케이션을 구축하고 실행하십시오.

1. 새 [워크스페이스]({{site.baseurl}}/developer_guide/platform_wide/app_group_configuration/#creating-your-app-group-in-my-apps)를 생성하고 앱 식별자 API 키와 엔드포인트를 기록합니다.
2. 통합 방법(스위프트 패키지 매니저, CocoaPods, 수동)에 따라 적절한 `xcodeproj` 파일을 선택하여 엽니다.
3. `Credentials` 파일의 해당 필드에 API 키와 엔드포인트를 입력합니다.
{% endtab %}
{% endtabs %}

{% alert note %}
SDK 통합에 대한 QA를 수행하는 동안 [SDK 디버거를]({{site.baseurl}}/developer_guide/sdk_integration/debugging) 사용하면 앱에 대한 자세한 로깅을 켜지 않고도 문제를 해결할 수 있습니다.
{% endalert %}
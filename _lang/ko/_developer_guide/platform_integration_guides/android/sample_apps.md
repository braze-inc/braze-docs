---
nav_title: 샘플 앱
article_title: Android 및 FireOS용 샘플 앱
platform: 
  - Android
  - FireOS
page_order: 10
description: "이 참조 문서에서는 Android 샘플 앱을 사용하는 방법을 다룹니다."

---

# 샘플 앱

> Braze SDK에는 각각 사용자의 편의를 위해 리포지토리 내 샘플 애플리케이션이 포함되어 있습니다. 이러한 각 앱은 완전히 빌드할 수 있으므로 자체 애플리케이션 내에서 구현하는 동시에 Braze 기능을 테스트할 수 있습니다. 

자체 애플리케이션 내 동작과 샘플 애플리케이션 내 예상 동작 및 코드 경로를 비교하여 테스트하는 것은 발생할 수 있는 문제를 디버깅하는 훌륭한 방법입니다.

## Droidboy 테스트 애플리케이션 빌드
Android SDK 깃허브 리포지토리 내 테스트 [애플리케이션브레이즈](https://github.com/braze-inc/braze-android-sdk "안드로이드 깃허브 리포지토리의") 이름은 Droidboy입니다. 다음 지침에 따라 프로젝트와 함께 모든 기능을 갖춘 사본을 빌드합니다.

1. 새 [워크스페이스]({{site.baseurl}}/developer_guide/platform_wide/app_group_configuration/#app-group-configuration)를 생성하고Braze API 식별자 키를 기록합니다.<br><br>
2. `/droidboy/res/values/braze.xml` 내의 적절한 위치(각각 `com_braze_push_fcm_sender_id` 및 `com_braze_api_key`라는 문자열의 태그 사이)에 FCM 발신자 ID와 Braze API 식별자 키를 복사합니다.<br><br>
3. **설정 관리** 아래 워크스페이스 설정에 FCM 서버 키와 서버 ID를 복사합니다.<br><br>
4. Droidboy APK를 어셈블링하려면 SDK 디렉토리 내에서 `./gradlew assemble`을 실행합니다. Windows에서는 `gradlew.bat` 을 사용합니다.<br><br>
5. 테스트 기기에서 Droidboy APK를 자동으로 설치하려면 SDK 디렉토리 내에서 `./gradlew installDebug`를 실행합니다.

## Hello Braze 테스트 애플리케이션 구축
Hello Braze 테스트 애플리케이션은 Braze SDK의 최소 사용 사례를 보여주며, 추가적으로 Braze SDK를 Gradle 프로젝트에 쉽게 통합하는 방법을 보여줍니다.

1. **설정 관리** 페이지에서 API 식별자 키를 `res/values` 폴더의 `braze.xml` 파일에 복사합니다.
![]({% image_buster /assets/img_archive/hello_appboy.png %})<br><br>
2. 기기 또는 에뮬레이터에 샘플 앱을 설치하려면 SDK 디렉토리 내에서 다음 명령을 실행합니다.
```
./gradlew installDebug
```
`ANDROID_HOME` 변수가 제대로 설정되어 있지 않거나 `local.properties` 폴더에 유효한 `sdk.dir` 폴더가 없는 경우, 이 플러그인이 기본 SDK도 설치해 줍니다. 자세한 내용은 [플러그인 저장소를](https://github.com/JakeWharton/sdk-manager-plugin) 참조하세요.

Android SDK 빌드 시스템에 대한 자세한 내용은 [GitHub 리포지토리 README](https://github.com/braze-inc/braze-android-sdk/blob/master/README.md)를 참조하세요.


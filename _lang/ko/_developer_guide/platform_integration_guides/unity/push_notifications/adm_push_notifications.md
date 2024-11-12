---
nav_title: Amazon 디바이스 메시징
article_title: Unity용 Amazon 디바이스 메시징 푸시 알림
platform: 
  - Unity
  - Android
page_order: 2
description: "이 참조 문서에서는 Unity 플랫폼용 Amazon Android 푸시 알림 통합을 다룹니다."
channel: push

---

# Amazon 디바이스 메시징

> 이 참조 문서에서는 Unity 플랫폼용 Amazon Android 푸시 알림 통합을 다룹니다.

푸시 알림은 중요한 업데이트가 발생하면 사용자 화면에 표시되는 앱 외 알림입니다. 푸시 알림은 사용자에게 시의적절하고 관련성 높은 콘텐츠를 제공하거나 앱에 다시 참여하도록 유도할 수 있는 유용한 방법입니다.

ADM(Amazon 장치 메시징)은 Amazon 이외의 장치에서는 지원되지 않습니다. Kindle 푸시를 테스트하려면 [FireOS 기기가](https://developer.amazon.com/appsandservices/apis/engage/device-messaging/tech-docs/04-integrating-your-app-with-adm) 있어야 합니다. 추가 모범 사례는 [도움말 섹션에서]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/fireos/troubleshooting/) 확인하세요.

Braze는 [Amazon 디바이스 메시징(ADM)을](https://developer.amazon.com/public/apis/engage/device-messaging) 사용하여 Amazon 디바이스로 푸시 알림을 보냅니다.

## 1단계: ADM 활성화

1. 계정을 생성하십시오 [Amazon Apps & Games 개발자 포털](https://developer.amazon.com/public) 이미 그렇게 하지 않은 경우.
2. [OAuth 자격 증명(클라이언트 ID 및 클라이언트 비밀)과 ADM API 키](https://developer.amazon.com/public/apis/engage/device-messaging/tech-docs/02-obtaining-adm-credentials)를 구합니다.
3. Unity Braze 구성 창에서 **자동 ADM 등록 활성화됨**을 활성화합니다. 
  - 또는 다음 줄을 `res/values/braze.xml` 파일에 추가하여 ADM 등록을 활성화할 수 있습니다:

  ```xml
  <bool name="com_braze_push_adm_messaging_registration_enabled">true</bool>
  ```

## 2단계: Unity AndroidManifest.xml 업데이트

앱에 `AndroidManifest.xml`이 없는 경우 다음을 템플릿으로 사용할 수 있습니다. 그렇지 않으면 이미 `AndroidManifest.xml`이 있는 경우 기존 `AndroidManifest.xml`에 다음 중 누락된 섹션이 추가되었는지 확인합니다.

```xml
<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
          package="REPLACE_WITH_YOUR_PACKAGE_NAME">

  <uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
  <uses-permission android:name="android.permission.INTERNET" />
  <permission
    android:name="REPLACE_WITH_YOUR_PACKAGE_NAME.permission.RECEIVE_ADM_MESSAGE"
    android:protectionLevel="signature" />
  <uses-permission android:name="REPLACE_WITH_YOUR_PACKAGE_NAME.permission.RECEIVE_ADM_MESSAGE" />
  <uses-permission android:name="com.amazon.device.messaging.permission.RECEIVE" />

  <application android:icon="@drawable/app_icon" 
               android:label="@string/app_name">

    <!-- Calls the necessary Braze methods to ensure that analytics are collected and that push notifications are properly forwarded to the Unity application. -->
    <activity android:name="com.braze.unity.BrazeUnityPlayerActivity" 
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

    <receiver android:name="com.braze.push.BrazeAmazonDeviceMessagingReceiver" android:permission="com.amazon.device.messaging.permission.SEND">
      <intent-filter>
          <action android:name="com.amazon.device.messaging.intent.RECEIVE" />
          <action android:name="com.amazon.device.messaging.intent.REGISTRATION" />
          <category android:name="REPLACE_WITH_YOUR_PACKAGE_NAME" />
      </intent-filter>
    </receiver>
  </application>
</manifest>
```

## 3단계: ADM API 키 저장

먼저 [앱의 ADM API 키를 구합니다](https://developer.amazon.com/public/apis/engage/device-messaging/tech-docs/02-obtaining-adm-credentials).  그런 다음 ADM API 키를 `api_key.txt` 파일에 저장하고 프로젝트의 [`Assets/`](https://docs.unity3d.com/Manual/AndroidAARPlugins.html) 폴더에 저장합니다.

Amazon은 `api_key.txt`에 후행 줄 바꿈과 같은 공백 문자가 포함된 경우 키를 인식하지 않습니다.

`mainTemplate.gradle` 파일에 다음을 추가합니다:

```gradle
task copyAmazon(type: Copy) {
    def unityProjectPath = $/file:///**DIR_UNITYPROJECT**/$.replace("\\", "/")
    from unityProjectPath + '/Assets/api_key.txt'
    into new File(projectDir, 'src/main/assets')
}

preBuild.dependsOn(copyAmazon)
```

## 4단계: ADM Jar 추가

필수 ADM Jar 파일은 [Unity JAR 문서에](https://docs.unity3d.com/Manual/AndroidJARPlugins.html) 따라 프로젝트의 어느 곳에나 배치할 수 있습니다.

## 5단계: Braze 대시보드에 클라이언트 비밀 및 클라이언트 ID 추가하기

마지막으로 [1단계](#step-1-enable-adm)에서 얻은 클라이언트 비밀과 클라이언트 ID를 Braze 대시보드의 **설정 관리** 페이지에 추가해야 합니다.

![]({% image_buster /assets/img_archive/fire_os_dashboard.png %})


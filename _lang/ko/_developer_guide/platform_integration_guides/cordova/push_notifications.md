---
nav_title: 푸시 알림
article_title: Cordova Braze SDK용 푸시 알림
platform:
  - Cordova
  - iOS
  - Android
page_order: 1
page_type: reference
description: "이 문서에서는 Cordova에서 푸시 알림을 구현하는 방법에 대해 설명합니다."
channel: push
---

# 푸시 알림 통합

> Cordova Braze SDK에 푸시 알림을 통합하는 방법을 알아보세요.

{% multi_lang_include cordova/prerequisites.md %}

## 기본 푸시 기능

기본적으로 Braze Cordova 플러그인에서는 기본 푸시 알림 기능이 활성화되어 있습니다. [XML 구성을 사용자 지정]({{site.baseurl}}/developer_guide/platform_integration_guides/cordova/initial_setup/customizations/#customization-options)하여 이러한 기능을 비활성화할 수 있습니다. 기본 푸시 알림 기능에 대한 자세한 내용은 [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/) 및 [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration/) 푸시 알림 가이드를 참조하세요.

## 확장된 푸시 기능

{% alert important %}
Cordova 플러그인을 추가, 제거 또는 업데이트할 때마다 Cordova는 Xcode 프로젝트의 Podfile을 덮어씁니다. 즉, Cordova 플러그인을 수정할 때마다 이 프로세스를 반복해야 합니다.
{% endalert %}

### 다양한 푸시 알림

#### 1단계: 알림 서비스 확장 만들기

Xcode 프로젝트에서 알림 서비스 확장 프로그램을 생성합니다. 전체 안내는 [iOS 리치 푸시 알림 튜토리얼](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/b2-rich-push-notifications)을 참조하세요.

#### 2단계: 새 대상 추가

Podfile을 열고 [방금 생성](#step-1-create-a-notification-service-extension)한 알림 서비스 확장 대상에 `BrazeNotificationService`를 추가합니다. `BrazeNotificationService`가 이미 대상에 추가되어 있는 경우 계속하기 전에 제거합니다. 중복된 심볼 오류를 방지하려면 정적 링크를 사용하세요.

```ruby
target 'NOTIFICATION_SERVICE_EXTENSION' do
  use_frameworks! :linkage => :static
  pod 'BrazeNotificationService'
end
```

`NOTIFICATION_SERVICE_EXTENSION` 을 알림 서비스 확장자의 이름으로 바꿉니다. 팟파일은 다음과 비슷해야 합니다:

```ruby
target 'MyAppRichNotificationService' do
  use_frameworks! :linkage => :static
  pod 'BrazeNotificationService'
end
```

#### 3단계: CocoaPods 종속성 다시 설치

터미널에서 프로젝트의 iOS 디렉토리로 이동하여 CocoaPod 종속 요소를 다시 설치합니다.

```bash
cd PATH_TO_PROJECT/platform/ios
pod install
```

### 푸시 스토리

#### 1단계: 알림 콘텐츠 확장 생성

Xcode 프로젝트에서 알림 콘텐츠 확장을 생성합니다. 전체 안내는 [iOS 푸시 스토리 튜토리얼](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/b3-push-stories/)을 참조하세요.

#### 2단계: 푸시 앱 그룹 구성

프로젝트의 `config.xml` 파일에서 [방금 만든](#step-1-create-a-notification-content-extension) 푸시 앱 그룹을 구성합니다.

```xml
<preference name="com.braze.ios_push_app_group" value="NOTIFICATION_CONTENT_EXTENTION" />
```

`PUSH_APP_GROUP` 을 푸시 앱 그룹의 이름으로 바꿉니다. `config.xml` 은 다음과 유사해야 합니다:

```xml
<preference name="com.braze.ios_push_app_group" value="MyPushAppGroup" />
```

#### 3단계: 새 대상 추가

Podfile을 열고 [이전에 생성](#step-1-create-a-notification-content-extension)한 알림 콘텐츠 서비스 확장 대상에 `BrazePushStory`를 추가합니다. 중복된 심볼 오류를 방지하려면 정적 링크를 사용하세요.

```ruby
target 'NOTIFICATION_CONTENT_EXTENSION' do
  use_frameworks! :linkage => :static
  pod 'BrazePushStory'
end
```

`NOTIFICATION_CONTENT_EXTENSION` 을 알림 콘텐츠 확장자의 이름으로 바꿉니다. 팟파일은 다음과 비슷해야 합니다:

```ruby
target 'MyAppNotificationContentExtension' do
  use_frameworks! :linkage => :static
  pod 'BrazePushStory'
end
```

#### 4단계: CocoaPods 종속성 다시 설치

터미널에서 iOS 디렉토리로 이동하여 CocoaPod 종속성을 다시 설치합니다.

```bash
cd PATH_TO_PROJECT/platform/ios
pod install
```

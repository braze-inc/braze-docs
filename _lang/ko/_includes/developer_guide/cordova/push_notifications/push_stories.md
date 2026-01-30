{% multi_lang_include developer_guide/prerequisites/cordova.md %} [푸시 알림도 설정해야]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=cordova) 합니다.

## 푸시 스토리 설정하기

### 1단계: 알림 콘텐츠 확장 생성

Xcode 프로젝트에서 알림 콘텐츠 확장을 생성합니다. 전체 안내는 [iOS 푸시 스토리 튜토리얼](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/b3-push-stories/)을 참조하세요.

### 2단계: 푸시 앱 그룹 구성

프로젝트의 `config.xml` 파일에서 [방금 만든](#cordova_step-1-create-a-notification-content-extension) 푸시 앱 그룹을 구성합니다.

```xml
<preference name="com.braze.ios_push_app_group" value="NOTIFICATION_CONTENT_EXTENTION" />
```

`PUSH_APP_GROUP` 을 푸시 앱 그룹의 이름으로 바꿉니다. `config.xml` 은 다음과 유사해야 합니다:

```xml
<preference name="com.braze.ios_push_app_group" value="MyPushAppGroup" />
```

### 3단계: 새 대상 추가

Podfile을 열고 [이전에 생성](#cordova_step-1-create-a-notification-content-extension)한 알림 콘텐츠 서비스 확장 대상에 `BrazePushStory`를 추가합니다. 중복된 심볼 오류를 방지하려면 정적 링크를 사용하세요.

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

### 4단계: CocoaPods 종속성 다시 설치

터미널에서 iOS 디렉토리로 이동하여 CocoaPod 종속성을 다시 설치합니다.

```bash
cd PATH_TO_PROJECT/platform/ios
pod install
```

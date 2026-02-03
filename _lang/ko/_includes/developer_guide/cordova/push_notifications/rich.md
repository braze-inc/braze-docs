{% multi_lang_include developer_guide/prerequisites/cordova.md %} [푸시 알림도 설정해야]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=cordova) 합니다.

## 리치 푸시 알림 설정하기

### 1단계: 알림 서비스 확장 만들기

Xcode 프로젝트에서 알림 서비스 확장 프로그램을 생성합니다. 전체 안내는 [iOS 리치 푸시 알림 튜토리얼](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/b2-rich-push-notifications)을 참조하세요.

### 2단계: 새 대상 추가

Podfile을 열고 [방금 생성](#cordova_step-1-create-a-notification-service-extension)한 알림 서비스 확장 대상에 `BrazeNotificationService`를 추가합니다. `BrazeNotificationService`가 이미 대상에 추가되어 있는 경우 계속하기 전에 제거합니다. 중복된 심볼 오류를 방지하려면 정적 링크를 사용하세요.

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

### 3단계: CocoaPods 종속성 다시 설치

터미널에서 프로젝트의 iOS 디렉토리로 이동하여 CocoaPod 종속 요소를 다시 설치합니다.

```bash
cd PATH_TO_PROJECT/platform/ios
pod install
```

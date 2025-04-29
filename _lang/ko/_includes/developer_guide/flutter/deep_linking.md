## Prerequisites

Flutter 앱에 딥링킹을 구현하려면 먼저 기본 [Android]({{site.baseurl}}/developer_guide/push_notifications/deep_linking/?sdktab=android) 또는 [iOS]({{site.baseurl}}/developer_guide/push_notifications/deep_linking/?sdktab=swift) 레이어에서 딥링킹을 설정해야 합니다.

## 딥링킹 구현

### 1단계: Flutter의 기본 제공 처리 설정

{% tabs %}
{% tab iOS %}
1. Xcode 프로젝트에서 `Info.plist` 파일을 엽니다.
2. 새 키-값 쌍을 추가합니다.
3. 키를 `FlutterDeepLinkingEnabled` 로 설정합니다.
4. 유형을 `Boolean`로 설정합니다.
5. 값을 `YES` 으로 설정합니다.
    ![키-값 쌍이 추가된 예제 프로젝트의 `Info.plist` 파일]({% image_buster /assets/img/flutter/flutter-ios-deep-link-info-plist.png %} "Xcode 프로젝트 Info.plist 파일")
{% endtab %}

{% tab Android %}
1. Android Studio 프로젝트에서 `AndroidManifest.xml` 파일을 엽니다.
2. `activity` 태그에서 `.MainActivity` 을 찾습니다.
3. `activity` 태그 안에 다음 `meta-data` 태그를 추가합니다:
    ```xml
    <meta-data android:name="flutter_deeplinking_enabled" android:value="true" />
    ```
{% endtab %}
{% endtabs %}

### 2단계: Dart 레이어로 데이터 전달(선택 사항)

사용자를 앱의 특정 위치로 보내거나 특정 함수를 호출하는 등 복잡한 사용 사례에 기본, 퍼스트파티 또는 서드파티 링크 처리를 사용할 수 있습니다.

#### 예시: 알림 대화 상자로 딥 링크하기

{% alert note %}
다음 예제에서는 추가 패키지에 의존하지 않지만 유사한 접근 방식을 사용하여 기본, 퍼스트파티 또는 서드파티 패키지(예: [`go_router`](https://pub.dev/packages/go_router))를 구현할 수 있습니다. 추가 Dart 코드가 필요할 수 있습니다.
{% endalert %}

먼저 기본 레이어에서 메서드 채널을 사용하여 딥링크의 URL 문자열 데이터를 Dart 레이어로 전달합니다.

{% tabs %}
{% tab iOS %}
```swift
extension AppDelegate {
  
  // Delegate method for handling custom scheme links.
  override func application(_ app: UIApplication, open url: URL, options: [UIApplication.OpenURLOptionsKey : Any] = [:]) -> Bool {
    forwardURL(url)
    return true
  }
  
  // Delegate method for handling universal links.
  override func application(_ application: UIApplication, continue userActivity: NSUserActivity, restorationHandler: @escaping ([UIUserActivityRestoring]?) -> Void) -> Bool {
    guard userActivity.activityType == NSUserActivityTypeBrowsingWeb,
        let url = userActivity.webpageURL else {
      return false
    }
    forwardURL(url)
    return true
  }

  private func forwardURL(_ url: URL) {
    guard let controller: FlutterViewController = window?.rootViewController as? FlutterViewController else { return }
    let deepLinkChannel = FlutterMethodChannel(name: "deepLinkChannel", binaryMessenger: controller.binaryMessenger)
    deepLinkChannel.invokeMethod("receiveDeepLink", arguments: url.absoluteString)
  }

}
```
{% endtab %}

{% tab Android %}
```kotlin
class MainActivity : FlutterActivity() {

  override fun onCreate(savedInstanceState: Bundle?) {
    super.onCreate(savedInstanceState)
    handleDeepLink(intent)
  }

  override fun onNewIntent(intent: Intent) {
      super.onNewIntent(intent)
    handleDeepLink(intent)
  }

  private fun handleDeepLink(intent: Intent) {
    val binaryMessenger = flutterEngine?.dartExecutor?.binaryMessenger
    if (intent?.action == Intent.ACTION_VIEW && binaryMessenger != null) {
      MethodChannel(binaryMessenger, "deepLinkChannel")
        .invokeMethod("receivedDeepLink", intent?.data.toString())
    }
  }

}
```
{% endtab %}
{% endtabs %}

다음으로, 이전에 전송된 URL 문자열 데이터를 사용하여 경고 대화 상자를 표시하기 위해 Dart 레이어에서 콜백 함수가 사용됩니다.

```dart
MethodChannel('deepLinkChannel').setMethodCallHandler((call) async {
  deepLinkAlert(call.arguments, context);
});

void deepLinkAlert(String link, BuildContext context) {
  showDialog(
    context: context,
    builder: (BuildContext context) {
      return AlertDialog(
        title: Text("Deep Link Alert"),
        content: Text("Opened with deep link: $link"),
        actions: <Widget>[
          TextButton(
            child: Text("Close"),
            onPressed: () {
              Navigator.of(context).pop();
            },
          ),
        ],
      );
    },
  );
}
```

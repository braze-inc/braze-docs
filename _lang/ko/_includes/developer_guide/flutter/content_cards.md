## Flutter 콘텐츠 카드에 대하여

Braze SDK에는 콘텐츠 카드를 시작할 수 있는 기본 카드 피드가 포함되어 있습니다. 카드 피드를 표시하려면 `braze.launchContentCards()` 메서드를 사용할 수 있습니다. Braze SDK에 포함된 기본 카드 피드는 사용자의 콘텐츠 카드에 대한 모든 분석 추적, 해제 및 렌더링을 처리합니다.

{% multi_lang_include developer_guide/prerequisites/flutter.md %}

## 카드 메서드

[플러그인 공개 인터페이스](https://github.com/braze-inc/braze-flutter-sdk/blob/master/lib/braze_plugin.dart)에서 사용할 수 있는 다음 메서드를 사용하여 앱 내에서 커스텀 콘텐츠 카드 피드를 구축할 수 있습니다:

| 메서드                                         | 설명                                                                                            |
| ---------------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| `braze.requestContentCardsRefresh()`     | Braze SDK 서버에서 최신 콘텐츠 카드를 요청합니다.                                           |
| `braze.logContentCardClicked(contentCard)`    | 주어진 콘텐츠 카드 오브젝트에 대해 클릭을 기록합니다.                                                            |
| `braze.logContentCardImpression(contentCard)` | 주어진 콘텐츠 카드 오브젝트에 대해 노출 횟수를 기록합니다.                                                      |
| `braze.logContentCardDismissed(contentCard)`  | 주어진 콘텐츠 카드 오브젝트에 대한 해제를 기록합니다.                                                        |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 콘텐츠 카드 데이터 수신

Flutter 앱에서 콘텐츠 카드 데이터를 수신하기 위해 `BrazePlugin`은 [Dart Streams](https://dart.dev/tutorials/language/streams)를 사용한 콘텐츠 카드 데이터 전송을 지원합니다.

`BrazeContentCard` [오브젝트](https://pub.dev/documentation/braze_plugin/latest/braze_plugin/BrazeContentCard-class.html)는 `description`, `title`, `image`, `url`, `extras` 등을 포함하여 네이티브 모델 오브젝트에서 사용할 수 있는 필드의 하위 집합을 지원합니다.

### Dart 레이어에서 콘텐츠 카드 데이터 수신

Dart 레이어에서 콘텐츠 카드 데이터를 수신하려면 아래 코드를 사용하여 `StreamSubscription`을 생성하고 `braze.subscribeToContentCards()`를 호출합니다. 스트림 구독이 더 이상 필요하지 않으면 `cancel()`을 호출하세요.

```dart
// Create stream subscription
StreamSubscription contentCardsStreamSubscription;

contentCardsStreamSubscription = braze.subscribeToContentCards((List<BrazeContentCard> contentCards) {
  // Handle Content Cards
}

// Cancel stream subscription
contentCardsStreamSubscription.cancel();
```

예제는 Braze Flutter SDK 샘플 애플리케이션의 [main.dart](https://github.com/braze-inc/braze-flutter-sdk/blob/master/example/lib/main.dart)를 참조하세요.

### 네이티브 iOS 레이어에서 콘텐츠 카드 데이터 전달

{% tabs %}
{% tab Flutter SDK 18.0.0+ %}

콘텐츠 카드 데이터는 Android 및 iOS 네이티브 레이어 모두에서 자동으로 전달됩니다. 추가 설정은 필요하지 않습니다.

{% endtab %}
{% tab Flutter SDK 17.1.0 and earlier %}

Flutter SDK 17.1.0 이하를 사용하는 경우, iOS 네이티브 레이어에서 콘텐츠 카드 데이터를 전달하려면 수동 설정이 필요합니다. 애플리케이션에 `BrazePlugin.processContentCards(contentCards)`를 호출하는 `contentCards.subscribeToUpdates` 콜백이 포함되어 있을 수 있습니다. Flutter SDK 18.0.0으로 마이그레이션하려면 `BrazePlugin.processContentCards(_:)` 호출을 제거하세요. 데이터 전달은 이제 자동으로 처리됩니다.

예제는 Braze Flutter SDK 샘플 애플리케이션의 [AppDelegate.swift](https://github.com/braze-inc/braze-flutter-sdk/blob/master/example/ios/Runner/AppDelegate.swift)를 참조하세요.

{% endtab %}
{% endtabs %}

#### 콘텐츠 카드에 대한 콜백 재생

콜백을 사용할 수 있기 전에 트리거된 콘텐츠 카드를 저장하고 콜백이 설정된 후에 재생하려면 `BrazePlugin`을 초기화할 때 `customConfigs` 맵에 다음 항목을 추가합니다:
```dart
BrazePlugin braze = new BrazePlugin(customConfigs: {replayCallbacksConfigKey: true});
```

## 플러터 콘텐츠 카드에 대하여

Braze SDK에는 콘텐츠 카드를 시작할 수 있는 기본 카드 피드가 포함되어 있습니다. 카드 피드를 표시하려면 `braze.launchContentCards()` 메서드를 사용할 수 있습니다. 기본 카드 피드는 Braze SDK에 포함되어 있으며 모든 분석 추적, 해제 및 사용자의 콘텐츠 카드 렌더링을 처리합니다.

{% multi_lang_include developer_guide/prerequisites/flutter.md %}

## 카드 방법

[플러그인 공개 인터페이스에서](https://github.com/braze-inc/braze-flutter-sdk/blob/master/lib/braze_plugin.dart) 사용할 수 있는 다음 방법을 사용하여 앱 내에서 사용자 지정 콘텐츠 카드 피드를 구축할 수 있습니다:

| 방법                                         | 설명                                                                                            |
| ---------------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| `braze.requestContentCardsRefresh()`     | Braze SDK 서버에서 최신 콘텐츠 카드를 요청합니다.                                           |
| `braze.logContentCardClicked(contentCard)`    | 주어진 콘텐츠 카드 객체에 대해 클릭을 기록합니다.                                                            |
| `braze.logContentCardImpression(contentCard)` | 지정된 콘텐츠 카드 객체에 대해 노출 횟수를 기록합니다.                                                      |
| `braze.logContentCardDismissed(contentCard)`  | 주어진 콘텐츠 카드 객체에 대한 해제를 기록합니다.                                                        |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 콘텐츠 카드 데이터 수신

Flutter 앱에서 콘텐츠 카드 데이터를 수신하려면 `BrazePlugin`이 [Dart Streams](https://dart.dev/tutorials/language/streams)를 사용하여 콘텐츠 카드 데이터 전송을 지원합니다.

`BrazeContentCard` [오브젝트](https://pub.dev/documentation/braze_plugin/latest/braze_plugin/BrazeContentCard-class.html)는 `description`, `title`, `image`, `url`, `extras` 등을 포함하여 기본 모델 오브젝트에서 사용할 수 있는 필드의 하위 집합을 지원합니다.

### 1단계: Dart 레이어에서 콘텐츠 카드 데이터 수신

Dart 레이어에서 콘텐츠 카드 데이터를 수신하려면 아래 코드를 사용하여 `StreamSubscription`을 생성하고 `braze.subscribeToContentCards()`를 호출합니다. 스트림 가입이 더 이상 필요하지 않은 경우 `cancel()`을 수행합니다.

```dart
// Create stream subscription
StreamSubscription contentCardsStreamSubscription;

contentCardsStreamSubscription = braze.subscribeToContentCards((List<BrazeContentCard> contentCards) {
  // Handle Content Cards
}

// Cancel stream subscription
contentCardsStreamSubscription.cancel();
```

예제는 샘플 앱의 [main.dart](https://github.com/braze-inc/braze-flutter-sdk/blob/master/example/lib/main.dart) 를 참조하세요.

### 2단계: 네이티브 레이어에서 콘텐츠 카드 데이터를 전달

1단계의 Dart 레이어에서 데이터를 수신하려면 다음 코드를 추가하여 기본 레이어에서 콘텐츠 카드 데이터를 전달합니다.

{% tabs %}
{% tab Android %}

콘텐츠 카드 데이터는 Android 계층에서 자동으로 전달됩니다.

{% endtab %}
{% tab iOS %}

1. 콘텐츠 카드 업데이트에 가입하려면 `contentCards.subscribeToUpdates`를 구현합니다. 자세한 내용은 [subscribeToUpdates](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcards-swift.class/subscribetoupdates(_:)) 설명서를 참조하세요.

2. 귀하의 `contentCards.subscribeToUpdates` 콜백 구현은 `BrazePlugin.processContentCards(contentCards)`를 호출해야 합니다.

예제는 샘플 앱의 [AppDelegate.swift](https://github.com/braze-inc/braze-flutter-sdk/blob/master/example/ios/Runner/AppDelegate.swift) 를 참조하세요.

{% endtab %}
{% endtabs %}

#### 콘텐츠 카드에 대한 콜백 재생

콜백을 사용하기 위해 먼저 트리거된 콘텐츠 카드를 저장하고 설정된 후에 재생하려면 `BrazePlugin`을 초기화할 때 `customConfigs` 맵에 다음 항목을 추가합니다.
```dart
BrazePlugin braze = new BrazePlugin(customConfigs: {replayCallbacksConfigKey: true});
```

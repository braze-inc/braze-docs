---
nav_title: 콘텐츠 카드
article_title: Flutter용 콘텐츠 카드
platform: Flutter
page_order: 3
page_type: reference
description: "이 문서에서는 Flutter 앱용 콘텐츠 카드 시작 방법을 다룹니다."
channel: content cards

---

# 콘텐츠 카드 통합

> 이 기사에서는 Flutter 앱에 대한 콘텐츠 카드를 설정하는 방법을 다룹니다.

Braze SDK에는 콘텐츠 카드를 시작할 수 있는 기본 카드 피드가 포함되어 있습니다. 카드 피드를 표시하려면 `braze.launchContentCards()` 메서드를 사용할 수 있습니다. 기본 카드 피드는 Braze SDK에 포함되어 있으며 모든 분석 추적, 해제 및 사용자의 콘텐츠 카드 렌더링을 처리합니다.

## 사용자 지정

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

## 샘플 콘텐츠 카드를 표시하는 테스트

다음 단계를 따라 샘플 콘텐츠 카드를 테스트하세요.

1. `braze.changeUserId('your-user-id')` 메서드를 호출하여 React 애플리케이션에서 활성 사용자를 설정합니다.
2. **캠페인**으로 이동하여 [이 가이드]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/create)를 따라 새 콘텐츠 카드 캠페인을 만드세요.
3. 테스트 콘텐츠 카드 캠페인을 작성하고 **테스트** 탭으로 이동하세요. 테스트 사용자와 동일한 `user-id`를 추가하고 **테스트 보내기**를 클릭합니다.
4. 푸시 알림을 탭하면 기기에서 콘텐츠 카드가 실행됩니다. 피드를 표시하려면 새로고침해야 할 수 있습니다.

![자신의 사용자 ID를 테스트 수신자로 추가하여 콘텐츠 카드를 테스트할 수 있는 Braze 콘텐츠 카드 캠페인]({% image_buster /assets/img/react-native/content-card-test.png %} "콘텐츠 카드 캠페인 테스트")

각 플랫폼에 대한 자세한 내용은 [Android 연동]({{site.baseurl}}/developer_guide/platform_integration_guides/android/content_cards/data_models/) 또는 [iOS 연동](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/c2-contentcardsui) 가이드를 참조하세요.

## GIF 지원

{% multi_lang_include wrappers/gif_support/content_cards.md %}


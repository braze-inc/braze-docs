---
nav_title: 사용자 지정 온클릭 동작
article_title: iOS용 인앱 메시지 클릭 동작 사용자 지정하기
platform: Swift
page_order: 5
description: "이 참조 문서에서는 Swift SDK의 커스텀 iOS 인앱 메시징 클릭 시 동작을 다룹니다."
channel:
  - in-app messages
---

# 사용자 지정 클릭 동작

> 각 `Braze.InAppMessage` 오브젝트에는 해당 [`ClickAction`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage/clickaction)이 포함되어 있으며, 이는 클릭 시 동작을 정의합니다. 

이 동작을 사용자 지정하려면 다음 샘플을 참조하여 `clickAction` 속성정보를 수정할 수 있습니다.

{% tabs %}
{% tab swift %}

```swift
func inAppMessage(
  _ ui: BrazeInAppMessageUI, 
  prepareWith context: inout BrazeInAppMessageUI.PresentationContext
) {
  if let newUrl = URL(string: "{your-url}") {
    context.message.clickAction = .url(newUrl, useWebView: true)
  }
}
```

{% endtab %}
{% tab 목표-C %}

`inAppMessage(_:prepareWith:)` 메서드는 Objective-C에서 사용할 수 없습니다.

{% endtab %}
{% endtabs %}

## 클릭 작업 유형

`Braze.InAppMessage`의 `clickAction` 속성정보에서 기본값은 `.none`이지만 다음 값 중 하나로 설정할 수 있습니다.

| `ClickAction` | 클릭 시 동작 |
| -------------------------- | -------- |
| `.url(URL, useWebView: Bool)` | 외부 브라우저에서 지정된 URL을 엽니다. `useWebView` 을 `true` 으로 설정하면 웹 보기로 열립니다. |
| `.newsFeed` | 메시지를 클릭하면 뉴스피드가 표시되고 메시지가 해제됩니다.<br><br>**참고:** 뉴스피드는 더 이상 사용되지 않습니다. 자세한 내용은 [마이그레이션 가이드를]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/migrating_from_news_feed/) 확인하세요. |
| `.none` | 클릭하면 메시지가 삭제됩니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert important %}
버튼이 포함된 인앱 메시지의 경우 버튼 텍스트를 추가하기 전에 클릭 동작이 추가되면 `clickAction` 메시지도 최종 페이로드에 포함됩니다.
{% endalert %}

## 인앱 메시지 및 버튼 클릭 사용자 지정하기

다음 [`BrazeInAppMessageUIDelegate`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate) 위임 메서드가 인앱 메시지를 클릭할 때 호출됩니다. 인앱 메시지 버튼 및 HTML 인앱 메시지 버튼(링크)을 클릭한 경우 버튼 ID가 선택적 매개변수로 제공됩니다.

{% tabs %}
{% tab swift %}

```swift
func inAppMessage(
  _ ui: BrazeInAppMessageUI,
  shouldProcess clickAction: Braze.InAppMessage.ClickAction,
  buttonId: String?,
  message: Braze.InAppMessage,
  view: InAppMessageView
) -> Bool
```

{% endtab %}
{% tab 목표-C %}

```objc
- (BOOL)inAppMessage:(BrazeInAppMessageUI *)ui
       shouldProcess:(enum BRZInAppMessageRawClickAction)clickAction
                 url:(NSURL *)uri
            buttonId:(NSString *)buttonId
             message:(BRZInAppMessageRaw *)message
                view:(UIView *)view;
```

{% endtab %}
{% endtabs %}

이 메서드는 Braze에서 클릭 동작을 계속 실행할지 여부를 나타내는 부울 값을 반환합니다.


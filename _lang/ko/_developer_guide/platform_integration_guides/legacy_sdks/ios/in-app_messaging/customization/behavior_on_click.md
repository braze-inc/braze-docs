---
nav_title: 사용자 지정 온클릭 동작
article_title: iOS용 인앱 메시지 온클릭 동작 사용자 지정하기
platform: iOS
page_order: 5
description: "이 참조 문서에서는 iOS 애플리케이션의 사용자 지정 인앱 메시징 클릭 시 동작을 다룹니다."
channel:
  - in-app messages
noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# 클릭 시 인앱 메시지 동작 사용자 지정

{% alert note %}
이 문서에는 더 이상 사용되지 않는 뉴스피드에 대한 정보가 포함되어 있습니다. Braze는 뉴스피드 도구를 사용하는 고객에게 보다 유연하고 맞춤 설정이 가능하며 안정적인 콘텐츠 카드 메시징 채널로 전환할 것을 권장합니다. 자세한 내용은 [마이그레이션 가이드를]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/migrating_from_news_feed/) 확인하세요.
{% endalert %}

`ABKInAppMessage`의 `inAppMessageClickActionType` 속성정보는 인앱 메시지를 클릭한 후 실행 동작을 정의합니다. 이 속성은 읽기 전용입니다. 인앱 메시지의 클릭 동작을 변경하려면 `ABKInAppMessage`에서 다음 메서드를 호출할 수 있습니다.

{% tabs %}
{% tab 목표-C %}

```objc
[inAppMessage setInAppMessageClickAction:clickActionType withURI:uri];
```

{% endtab %}
{% tab swift %}

```swift
inAppMessage.setInAppMessageClickAction(clickActionType: clickActionType, withURI: uri)
```

{% endtab %}
{% endtabs %}

`inAppMessageClickActionType` 은 다음 값 중 하나로 설정할 수 있습니다:

| `ABKInAppMessageClickActionType` | 클릭 시 동작 |
| -------------------------- | -------- |
| `ABKInAppMessageDisplayNewsFeed` | 메시지를 클릭하면 뉴스피드에 메시지가 표시되고 메시지가 삭제됩니다. `uri` 매개변수는 무시되고 `ABKInAppMessage`의 `uri` 속성정보는 nil로 설정됩니다. |
| `ABKInAppMessageRedirectToURI` | 메시지를 클릭하면 지정된 URI가 표시되고 메시지가 해제됩니다. `uri` 매개변수는 null일 수 없습니다. |
| `ABKInAppMessageNoneClickAction` | 클릭하면 메시지가 삭제됩니다. `uri` 매개변수는 무시되고 `ABKInAppMessage`의 `uri` 속성정보는 nil로 설정됩니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert important %}
버튼이 포함된 인앱 메시지의 경우 버튼 텍스트를 추가하기 전에 클릭 동작이 추가되면 `clickAction` 메시지도 최종 페이로드에 포함됩니다.
{% endalert %}

## 인앱 메시지 본문 클릭 사용자 지정

다음 [`ABKInAppMessageUIDelegate`](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyUI/ABKInAppMessage/ABKInAppMessageUIDelegate.h) 위임 메서드는 인앱 메시지를 클릭할 때 호출됩니다.

{% tabs %}
{% tab 목표-C %}

```objc
- (BOOL) onInAppMessageClicked:(ABKInAppMessage *)inAppMessage;
```

{% endtab %}
{% tab swift %}

```swift
func onInAppMessageClicked(inAppMessage: ABKInAppMessage!) -> Bool
```

{% endtab %}
{% endtabs %}

## 인앱 메시지 버튼 클릭 수 사용자 지정

인앱 메시지 버튼 및 HTML 인앱 메시지 버튼(예: 링크) 클릭 시 [`ABKInAppMessageUIDelegate`](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyUI/ABKInAppMessage/ABKInAppMessageUIDelegate.h)에는 다음과 같은 위임 메서드가 포함됩니다.

{% tabs %}
{% tab 목표-C %}

```objc
- (BOOL)onInAppMessageButtonClicked:(ABKInAppMessageImmersive *)inAppMessage
                             button:(ABKInAppMessageButton *)button;

- (BOOL)onInAppMessageHTMLButtonClicked:(ABKInAppMessageHTML *)inAppMessage
                             clickedURL:(nullable NSURL *)clickedURL
                               buttonID:(NSString *)buttonID;
```

{% endtab %}
{% tab swift %}

```swift
func onInAppMessageButtonClicked(inAppMessage: ABKInAppMessageImmersive!,
                                 button: ABKInAppMessageButton) -> Bool

func onInAppMessageHTMLButtonClicked(inAppMessage: ABKInAppMessageHTML!,
                                     clickedURL: URL, buttonID: String) -> Bool
```

{% endtab %}
{% endtabs %}

각 메서드는 Braze에서 클릭 동작을 계속 실행할지 여부를 나타내는 `BOOL` 값을 반환합니다.

델리게이트 메서드에서 버튼의 클릭 액션 유형에 액세스하려면 다음 코드를 사용할 수 있습니다:

{% tabs %}
{% tab 목표-C %}

```objc
if ([inAppMessage isKindOfClass:[ABKInAppMessageImmersive class]]) {
      ABKInAppMessageImmersive *immersiveIAM = (ABKInAppMessageImmersive *)inAppMessage;
      NSArray<ABKInAppMessageButton *> *buttons = immersiveIAM.buttons;
      for (ABKInAppMessageButton *button in buttons) {
         // Button action type is accessible via button.buttonClickActionType
      }
   }
```

{% endtab %}
{% tab swift %}

```swift
if inAppMessage is ABKInAppMessageImmersive {
      let immersiveIAM = inAppMessage as! ABKInAppMessageImmersive;
      for button in inAppMessage.buttons as! [ABKInAppMessageButton]{
        // Button action type is accessible via button.buttonClickActionType
      }
    }
```

{% endtab %}
{% endtabs %}

인앱 메시지에 버튼이 있는 경우 실행되는 클릭 동작은 `ABKInAppMessageButton` 모델에 있는 것만 실행됩니다. `ABKInAppMessage` 모델에 기본 클릭 동작('뉴스피드')이 할당되어 있어도 인앱 메시지 본문은 클릭할 수 없습니다.

## 메서드 선언

추가 정보는 다음 헤더 파일을 참조하십시오:

- [`ABKInAppMessage.h`](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/ABKInAppMessage.h)


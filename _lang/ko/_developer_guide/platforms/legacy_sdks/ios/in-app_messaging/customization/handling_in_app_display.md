---
nav_title: 커스텀 디스플레이 처리
article_title: iOS용 인앱 메시지 표시 처리 사용자 지정
platform: iOS
page_order: 4
description: "이 참조 문서에서는 iOS 애플리케이션의 인앱 메시징 커스텀 표시 처리를 다룹니다."
channel:
  - in-app messages

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# 커스텀 처리 인앱 메시지 표시

[`ABKInAppMessageControllerDelegate`](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/ABKInAppMessageControllerDelegate.h)이(가) 설정되면, 다음 대리자 메서드가 인앱 메시지가 표시되기 전에 호출됩니다:

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
- (ABKInAppMessageDisplayChoice) beforeInAppMessageDisplayed:(ABKInAppMessage *)inAppMessage;
```

{% endtab %}
{% tab swift %}

```swift
func beforeInAppMessageDisplayed(inAppMessage: ABKInAppMessage!) -> ABKInAppMessageDisplayChoice
```

{% endtab %}
{% endtabs %}

[`ABKInAppMessageUIDelegate`](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyUI/ABKInAppMessage/ABKInAppMessageUIDelegate.h)만 구현한 경우 다음 UI 위임 메서드가 대신 호출됩니다.

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
- (ABKInAppMessageDisplayChoice) beforeInAppMessageDisplayed:(ABKInAppMessage *)inAppMessage withKeyboardIsUp:(BOOL)keyboardIsUp;
```

{% endtab %}
{% tab swift %}

```swift
func beforeInAppMessageDisplayed(inAppMessage: ABKInAppMessage!, withKeyboardIsUp keyboardIsUp: Bool) -> ABKInAppMessageDisplayChoice
```

{% endtab %}
{% endtabs %}

이 위임 메서드를 구현하고 `ABKInAppMessageDisplayChoice`에 대해 다음 값 중 하나를 반환하여 인앱 메시지 처리를 사용자 지정할 수 있습니다.

| `ABKInAppMessageDisplayChoice` | 동작 |
| -------------------------- | -------- |
| Objective-C: `ABKDisplayInAppMessageNow`<br>Swift: `displayInAppMessageNow` | 메시지는 즉시 표시됩니다. |
| Objective-C: `ABKDisplayInAppMessageLater`<br>Swift: `displayInAppMessageLater` | 메시지는 표시되지 않고 스택의 맨 위로 다시 배치됩니다. |
| Objective-C: `ABKDiscardInAppMessage`<br>Swift: `discardInAppMessage`| 메시지는 폐기되며 표시되지 않습니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

`beforeInAppMessageDisplayed:` 델리게이트 메서드를 사용하여 인앱 메시지 표시 로직을 추가하거나, Braze가 표시하기 전에 인앱 메시지를 사용자 지정하거나, Braze 인앱 메시지 표시 로직 및 UI를 완전히 옵트아웃할 수 있습니다.

구현 예제는 [샘플 애플리케이션](https://github.com/Appboy/appboy-ios-sdk/blob/master/Samples/InAppMessage/BrazeInAppMessageSample/BrazeInAppMessageSample/AppDelegate.m)을 확인하세요.

## 표시 전에 인앱 메시지 재정의

인앱 메시지의 디스플레이 동작을 변경하려면 필요한 디스플레이 로직을 `beforeInAppMessageDisplayed:` 위임 메서드에 추가해야 합니다. 예를 들어, 키보드가 현재 표시 중인 경우 화면 상단에 인앱 메시지를 표시하거나 인앱 메시지 데이터 모델을 가져와 직접 인앱 메시지를 표시할 수 있습니다.

세션이 시작될 때 인앱 메시지 캠페인이 표시되지 않으면 필요한 표시 로직이 `beforeInAppMessageDisplayed:` 위임 메서드에 추가되었는지 확인하세요. 이 기능을 사용하면 키보드가 표시 중이어도 화면 상단에서 인앱 메시지 캠페인을 표시할 수 있습니다.

## 다크 모드 비활성화

사용자 기기에 다크 모드가 켜져 있는 경우 인앱 메시지에 다크 모드 스타일이 적용되지 않도록 하려면 [`ABKInAppMessage.enableDarkTheme`](https://appboy.github.io/appboy-ios-sdk/docs/interface_a_b_k_in_app_message.html#ae89df6090bed623099ab0ecc0a74ad5d) 속성정보를 사용합니다. `ABKInAppMessageControllerDelegate.beforeInAppMessageDisplayed:` 또는 `ABKInAppMessageUIDelegate.beforeInAppMessageDisplayed:` 메서드에서 메서드의 `inAppMessage` 매개변수에 대한 `enableDarkTheme` 속성정보를 `NO`로 설정합니다.

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
// ABKInAppMessageControllerDelegate
- (ABKInAppMessageDisplayChoice)beforeInAppMessageDisplayed:(ABKInAppMessage *)inAppMessage {
  ...
  inAppMessage.enableDarkTheme = NO;
  ...
  return ABKDisplayInAppMessageNow;
}

// ABKInAppMessageUIDelegate
- (ABKInAppMessageDisplayChoice)beforeInAppMesssageDisplayed:(ABKInAppMessage *)inAppMessage
                                            withKeyboardIsUp:(BOOL)keyboardIsUp {
  ...
  inAppMessage.enableDarkTheme = NO;
  ...
  return ABKDisplayInAppMessageNow;
}
```

{% endtab %}
{% tab swift %}

```swift
// ABKInAppMessageControllerDelegate
func before(inAppMessageDisplayed inAppMessage: ABKInAppMessage) -> ABKInAppMessageDisplayChoice {
  ...
  inAppMessage.enableDarkTheme = false
  ...
  return ABKInAppMessageDisplayChoice.displayInAppMessageNow
}

// ABKInAppMessageUIDelegate
func before(inAppMessageDisplayed inAppMessage: ABKInAppMessage, withKeyboardIsUp keyboardIsUp: Bool) -> ABKInAppMessageDisplayChoice {
  ...
  inAppMessage.enableDarkTheme = false
  ...
  return ABKInAppMessageDisplayChoice.displayInAppMessageNow
}
```

{% endtab %}
{% endtabs %}

## 디스플레이 중 상태 표시줄 숨기기

`Full` 및 `HTML` 인앱 메시지의 경우, SDK는 기본적으로 메시지를 상태 표시줄 위에 배치하려고 시도합니다. 그러나 여전히 상태 표시줄이 인앱 메시지 위에 나타나는 경우가 있습니다. iOS SDK의 [3.21.1](https://github.com/Appboy/appboy-ios-sdk/blob/master/CHANGELOG.md#3211) 버전부터 `Full` 및 `HTML` 인앱 메시지를 표시할 때 상태 표시줄을 숨기도록 `startWithApiKey:`에 전달된 `appboyOptions`에서 `ABKInAppMessageHideStatusBarKey`를 `YES`로 설정할 수 있습니다.

## 노출 횟수 및 클릭 기록

인앱 메시지 노출 횟수 및 클릭의 기록은 완전히 커스텀 처리를 구현할 때 자동으로 수행되지 않습니다(예: `beforeInAppMessageDisplayed:`에서 `ABKDiscardInAppMessage`를 반환하여 Braze 인앱 메시지 표시를 우회하는 경우). 자체 UI를 인앱 메시지 모델을 사용하여 구현하기로 선택한 경우 `ABKInAppMessage` 클래스에서 다음 메서드를 사용하여 분석을 기록해야 합니다:

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
// Registers that a user has viewed an in-app message with the Braze server.
- (void) logInAppMessageImpression;
// Registers that a user has clicked on an in-app message with the Braze server.
- (void) logInAppMessageClicked;
```

{% endtab %}
{% tab swift %}

```swift
// Registers that a user has viewed an in-app message with the Braze server.
func logInAppMessageImpression()
// Registers that a user has clicked on an in-app message with the Braze server.
func logInAppMessageClicked()
```

{% endtab %}
{% endtabs %}

게다가 `ABKInAppMessageImmersive`(즉, *i.e*, `Modal` 및 `Full` 인앱 메시지)의 서브클래스에서 버튼 클릭을 기록해야 합니다.

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
// Logs button click analytics
- (void)logInAppMessageClickedWithButtonID:(NSInteger)buttonID;
```

{% endtab %}
{% tab swift %}

```swift
// Logs button click analytics
func logInAppMessageClickedWithButtonID(buttonId: NSInteger)
```

{% endtab %}
{% endtabs %}

## 메서드 선언

추가 정보는 다음 헤더 파일을 참조하십시오:

- [`ABKInAppMessage.h`](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/ABKInAppMessage.h)
- [`ABKInAppMessageControllerDelegate.h`](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/ABKInAppMessageControllerDelegate.h)

## 구현 샘플

[`AppDelegate.m`](https://github.com/Appboy/appboy-ios-sdk/blob/master/Samples/InAppMessage/BrazeInAppMessageSample/BrazeInAppMessageSample/AppDelegate.m) 인앱 메시지 샘플 앱을 참조하십시오.




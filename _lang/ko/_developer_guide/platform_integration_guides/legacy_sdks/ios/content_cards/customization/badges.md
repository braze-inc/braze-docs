---
nav_title: 배지
article_title: iOS용 콘텐츠 카드 배지
platform: iOS
page_order: 5
description: "이 문서에서는 iOS 애플리케이션에서 콘텐츠 카드에 배지를 추가하는 방법에 대해 설명합니다."
channel:
  - content cards

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# 배지

## 미열람 콘텐츠 카드 수 요청

사용자가 가지고 있는 읽지 않은 콘텐츠 카드의 수를 표시하려면 카드 수를 요청하고 배지로 표시하는 것이 좋습니다. 배지는 콘텐츠 카드에서 사용자를 기다리는 새로운 콘텐츠에 대한 관심을 끌 수 있는 좋은 방법입니다. 콘텐츠 카드에 배지를 추가하려는 경우 Braze SDK에서 다음을 쿼리하는 메서드를 제공합니다.

- 현재 사용자가 보지 않은 콘텐츠 카드
- 현재 사용자가 볼 수 있는 총 콘텐츠 카드

[`ABKContentCardsController`](https://appboy.github.io/appboy-ios-sdk/docs/interface_a_b_k_content_cards_controller.html)에서 다음 메서드 선언이 이를 자세히 설명합니다.

```objc
- (NSInteger)unviewedContentCardCount;
/*
This method returns the number of currently active Content Cards that have not been viewed.
A "view" happens when a card becomes visible in the Content Cards view. This differentiates between cards that are off-screen in the scrolling view and those which are on-screen; when a card scrolls onto the screen, it's counted as viewed.
Cards are counted as viewed only once -- if a card scrolls off the screen and back on, it's not re-counted.
Cards are counted only once, even if they appear in multiple Content Cards views or across multiple devices.
*/

- (NSInteger)contentCardCount;
/* 
This method returns the total number of currently active Content Cards. Cards are counted only once even if they appear in multiple Content Cards views.
 */
```

## 앱 배지 수에 미열람 콘텐츠 카드 수 표시

앱의 푸시 알림에 대한 미리 알림 기능 외에도 배지를 활용하여 사용자의 콘텐츠 카드에서 미열람 항목을 나타낼 수 있습니다. 미열람 콘텐츠 카드 업데이트를 기반으로 배지 수를 업데이트하는 기능은 사용자를 앱으로 다시 끌어들이고 세션을 늘리는 데 유용합니다.

앱이 닫히고 사용자의 세션이 종료된 후 이 메서드는 배지 수를 기록합니다.

{% tabs %}
{% tab 목표-C %}

```objc
(void)applicationDidEnterBackground:(UIApplication *)application
```

이 메서드 내에서 주어진 세션 동안 사용자가 카드를 볼 때 배지 수를 적극적으로 업데이트하는 다음 코드를 구현합니다.

```objc
[UIApplication sharedApplication].applicationIconBadgeNumber = [[Appboy sharedInstance].contentCardsController unviewedContentCardCount];
```

{% endtab %}
{% tab swift %}

```swift
func applicationDidEnterBackground(_ application: UIApplication)
```

이 메서드 내에서 주어진 세션 동안 사용자가 카드를 볼 때 배지 수를 적극적으로 업데이트하는 다음 코드를 구현합니다.

```swift
UIApplication.shared.applicationIconBadgeNumber =
  Appboy.sharedInstance()?.contentCardsController.unviewedContentCardCount() ?? 0
```

{% endtab %}
{% endtabs %}

자세한 내용은 `Appboy.h` [헤더 파일을](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/Appboy.h) 참조하세요.

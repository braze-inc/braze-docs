---
nav_title: 배지
article_title: 뉴스피드 배지 iOS용
platform: iOS
page_order: 3
description: "이 참조 문서에서는 iOS 애플리케이션에서 뉴스피드 배지 수를 구현하는 방법을 다룹니다."
channel:
  - news feed

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# 배지

{% multi_lang_include deprecations/braze_sdk/news_feed.md %}

## 미열람 뉴스피드 카드 수 요청

![]({% image_buster /assets/img_archive/newsfeed_badges.png %}){: style="float:right;max-width:25%;margin-left:15px;"}

배지는 뉴스피드에서 사용자가 기다리고 있는 새로운 콘텐츠에 주목하게 하는 좋은 방법입니다. 뉴스피드에 배지를 추가하려는 경우 Braze SDK에서 다음을 쿼리하는 메서드를 제공합니다.

- 현재 사용자의 읽지 않은 뉴스피드 카드
- 현재 사용자의 총 조회 가능 뉴스피드 카드

다음 메서드 선언은 [`ABKFeedController`](http://appboy.github.io/appboy-ios-sdk/docs/interface_a_b_k_feed_controller.html "abk 피드 컨트롤러") 에 자세히 설명되어 있습니다:

```
- (NSInteger)unreadCardCountForCategories:(ABKCardCategory)categories;
/*
This method returns the number of currently active Content Cards that have not been viewed.
A "view" happens when a card becomes visible in the Content Cards view. This differentiates between cards that are off-screen in the scrolling view and those which are on-screen; when a card scrolls onto the screen, it's counted as viewed.
Cards are counted as viewed only once -- if a card scrolls off the screen and back on, it's not re-counted.
Cards are counted only once, even if they appear in multiple Content Cards views or across multiple devices.
*/

- (NSInteger)cardCountForCategories:(ABKCardCategory)categories;
/* 
This method returns the total number of currently active Content Cards. Cards are counted only once, even if they appear in multiple Content Cards views.
 */
 ```

## 앱 배지 수에 미열람 뉴스피드 항목 수 표시

앱의 푸시 알림에 대한 미리 알림 기능 외에도 배지는 사용자의 뉴스피드에서 보지 않은 항목을 나타낼 수 있습니다. 미열람 않은 뉴스피드 업데이트를 기반으로 배지 수를 업데이트하는 기능은 사용자를 앱으로 다시 끌어들이고 세션을 늘리는 데 유용한 툴이 될 수 있습니다.

앱이 닫히고 사용자의 세션이 종료된 후 배지 수를 기록하는 이 메서드를 호출합니다.

{% tabs %}
{% tab 목표-C %}

```objc
(void)applicationDidEnterBackground:(UIApplication *)application
```

{% endtab %}
{% tab swift %}

```swift
func applicationDidEnterBackground(_ application: UIApplication)
```

{% endtab %}
{% endtabs %}

이 메서드 내에서 주어진 세션 동안 사용자가 카드를 볼 때 배지 수를 적극적으로 업데이트하는 다음 코드를 구현합니다.

{% tabs %}
{% tab 목표-C %}

```objc
[UIApplication sharedApplication].applicationIconBadgeNumber = [[Appboy sharedInstance].feedController unreadCardCountForCategories:ABKCardCategoryAll];
```

{% endtab %}
{% tab swift %}

```swift
UIApplication.shared.applicationIconBadgeNumber = Appboy.sharedInstance()?.feedController.unreadCardCount(forCategories: ABKCardCategory.all) ?? 0
```

{% endtab %}
{% endtabs %}

어떤 시점에서든 예를 들어 `applicationDidBecomeActive` 메서드에서 배지 수를 지우기 위해 다음 코드를 사용합니다.

{% tabs %}
{% tab 목표-C %}

```objc
[UIApplication sharedApplication].applicationIconBadgeNumber = 0;
```

{% endtab %}
{% tab swift %}

```swift
UIApplication.shared.applicationIconBadgeNumber = 0
```

{% endtab %}
{% endtabs %}

자세한 내용은 `Appboy.h` [헤더 파일](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/Appboy.h "Appboy.h 헤더 파일을") 참조하세요.


---
nav_title: 배지
article_title: 뉴스피드 배지 iOS용
platform: iOS
page_order: 3
description: "이 참조 문서는 iOS 애플리케이션에서 뉴스피드 배지 수를 구현하는 방법을 다룹니다."
channel:
  - news feed

noindex: true
---

{% multi_lang_include 사용 중단/목적-c.md %}

# 배지

{% alert note %}
뉴스피드는 사용 중지될 예정입니다. Braze는 뉴스피드 도구를 사용하는 고객이 더 유연하고, 맞춤화 가능하며, 신뢰할 수 있는 콘텐츠 카드 메시징 채널로 이동할 것을 권장합니다. [마이그레이션 가이드]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/migrating_from_news_feed/)를 확인해 보세요.
{% endalert %}

## 읽지 않은 뉴스피드 카드 수 요청

![][45]{: style="float:right;max-width:25%;margin-left:15px;"}

배지는 뉴스피드에서 사용자가 기다리고 있는 새로운 콘텐츠에 주목하게 하는 좋은 방법입니다. 뉴스피드에 배지를 추가하려면 Braze 소프트웨어 개발 키트에서 다음을 쿼리하는 방법을 제공합니다:

- 현재 사용자의 읽지 않은 뉴스피드 카드
- 현재 사용자의 총 조회 가능 뉴스피드 카드

다음 메서드 선언은 \[`ABKFeedController`][44]에서 이를 자세히 설명합니다:

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

## 앱 배지 수에 읽지 않은 뉴스피드 항목 수 표시

앱의 푸시 알림 알림 외에도 배지는 사용자의 뉴스피드에서 보지 않은 항목을 나타낼 수 있습니다. 읽지 않은 뉴스피드 업데이트를 기반으로 배지 수를 업데이트하는 것은 사용자를 앱으로 다시 끌어들이고 세션을 증가시키는 데 유용한 도구가 될 수 있습니다.

이 메서드를 호출하여 앱이 닫히고 사용자의 세션이 종료된 후 배지 수를 기록합니다:

{% tabs %}
{% tab 오브젝티브-C %}

```objc
(void)applicationDidEnterBackground:(UIApplication *)application
```

{% endtab %}
{% tab 스위프트 %}

```swift
func applicationDidEnterBackground(_ application: UIApplication)
```

{% endtab %}
{% endtabs %}

이 메서드 내에서 사용자가 주어진 세션 동안 카드를 볼 때 배지 수를 적극적으로 업데이트하는 다음 코드를 구현하십시오.

{% tabs %}
{% tab 오브젝티브-C %}

```objc
[UIApplication sharedApplication].applicationIconBadgeNumber = [[Appboy sharedInstance].feedController unreadCardCountForCategories:ABKCardCategoryAll];
```

{% endtab %}
{% tab 스위프트 %}

```swift
UIApplication.shared.applicationIconBadgeNumber = Appboy.sharedInstance()?.feedController.unreadCardCount(forCategories: ABKCardCategory.all) ?? 0
```

{% endtab %}
{% endtabs %}

어떤 시점에서든 예를 들어 `applicationDidBecomeActive` 메서드에서 배지 수를 지우기 위해 다음 코드를 사용하십시오:

{% tabs %}
{% tab 오브젝티브-C %}

```objc
[UIApplication sharedApplication].applicationIconBadgeNumber = 0;
```

{% endtab %}
{% tab 스위프트 %}

```swift
UIApplication.shared.applicationIconBadgeNumber = 0
```

{% endtab %}
{% endtabs %}

자세한 내용은 `Appboy.h` [헤더 파일][15]을 참조하십시오.

[15]: https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/Appboy.h "Appboy.h 헤더 파일"
[42]: {% image_buster /assets/img_archive/badge_example.png %} "배지 예시"
[44]: http://appboy.github.io/appboy-ios-sdk/docs/interface_a_b_k_feed_controller.html "abk 피드 컨트롤러"
[45]: {% image_buster /assets/img_archive/newsfeed_badges.png %}
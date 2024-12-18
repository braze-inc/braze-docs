---
nav_title: 사용자 ID 설정
article_title: iOS용 사용자 ID 설정
platform: Swift
page_order: 1
description: "이 문서에서는 iOS 앱에서 사용자 ID를 설정하는 방법, 제안된 사용자 ID 명명 규칙 및 몇 가지 모범 사례를 보여줍니다."
 
---

# 사용자 ID 설정

{% multi_lang_include archive/setting_user_ids/setting_user_ids.md %}

## 추천 사용자 ID 명명 규칙

{% multi_lang_include archive/setting_user_ids/naming_convention.md %}

## 사용자 ID 할당

사용자가 식별되면 일반적으로 로그인 후 사용자 ID를 설정하기 위해 다음 호출을 즉시 수행해야 합니다.

{% tabs %}
{% tab swift %}

```swift
AppDelegate.braze?.changeUser(userId: "YOUR_USER_ID")
```

{% endtab %}
{% tab 목표-C %}

```objc
[AppDelegate.braze changeUser:@"YOUR_USER_ID_STRING"];
```

{% endtab %}
{% endtabs %}

{% alert warning %}
**사용자가 로그아웃할 때 `changeUser()`를 호출하지 마세요. `changeUser()`는 사용자가 애플리케이션에 로그인할 때만 호출해야 합니다.** [`changeUser()`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/changeuser%28userid%3Asdkauthsignature%3Afileid%3Aline%3A%29)를 정적 기본값으로 설정하면 사용자가 다시 로그인할 때까지 모든 사용자 활동이 해당 기본값 '사용자'와 연결됩니다.
{% endalert %}

또한 사용자가 로그아웃할 때 사용자 ID를 변경하지 않도록 권장합니다. 이렇게 하면 이전에 로그인한 사용자를 재참여 캠페인으로 타겟팅할 수 없게 됩니다. 여러 사용자가 동일한 기기를 사용할 것으로 예상되지만 앱에서 로그아웃한 상태일 때 사용자 중 한 명만을 타겟팅하려는 경우, 로그아웃 상태에서 타겟팅하려는 사용자 ID를 별도로 추적하고 앱의 로그아웃 프로세스의 일환으로 해당 사용자 ID로 전환하는 방법을 권장합니다.

## 사용자 ID 통합 모범 사례 및 참고 사항

{% multi_lang_include archive/setting_user_ids/best_practices.md %}

## 사용자 별칭 지정

{% multi_lang_include archive/setting_user_ids/aliasing.md platform="Swift" %}


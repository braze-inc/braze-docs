---
nav_title: 읽음 및 미열람 표시기
article_title: 콘텐츠 카드 읽음 및 미열람 표시기 iOS용
platform: iOS
page_order: 4
description: "이 참조 문서에서는 iOS의 열람 및 미열람 표시기와 이를 콘텐츠 카드에서 구현하는 방법을 다룹니다."
channel:
  - content cards

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# 열람 및 미열람 표시기

## 미열람 표시기 비활성화

![두 개의 콘텐츠 카드가 나란히 표시됩니다. 왼쪽 카드에서 하단에 파란색 선이 있고 이는 열람하지 않았음을 나타냅니다. 오른쪽 카드에는 파란색 선이 없어서 이미 본 카드임을 나타냅니다.]({% image_buster /assets/img/braze-content-cards-seen-unseen-behavior.png %}){: style="max-width:80%"}

카드 하단의 파란색 선을 비활성화할 수 있습니다. `ABKContentCardsTableViewController`에서 `disableUnviewedIndicator` 속성정보를 `YES`로 설정하여 카드의 열람 여부를 나타냅니다.

## 미열람 표시기 사용자 지정

미열람 표시기는 `ABKBaseContentCardCell` 클래스의 `unviewedLineView` 속성정보를 통해 액세스할 수 있습니다. `UITableViewCell` 구현을 사용하는 경우 셀이 그려지기 전에 속성에 접근해야 합니다.

예를 들어, 미열람 표시기의 색상을 빨간색으로 설정하려면 다음을 수행합니다.

{% tabs %}
{% tab 목표-C %}

```objc
((ABKBaseContentCardCell *)cell).unviewedLineView.backgroundColor = [UIColor redColor];
```

{% endtab %}
{% tab swift %}

```swift
(card as? ABKBaseContentCardCell).unviewedLineView.backgroundColor = UIColor.red
```

{% endtab %}
{% endtabs %}

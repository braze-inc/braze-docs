---
nav_title: 사용자 지정 스타일
article_title: iOS용 사용자 지정 콘텐츠 카드 스타일링
platform: iOS
page_order: 1
description: "이 문서에서는 iOS 애플리케이션의 콘텐츠 카드 사용자 지정 스타일링 옵션에 대해 설명합니다."
channel:
  - content cards
noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# 사용자 지정 스타일

## 기본 이미지 재정의

{% alert important %}
iOS 인앱 메시지 또는 콘텐츠 카드에서 이미지를 표시하기 위해 Braze UI를 사용하려는 경우 `SDWebImage`의 통합이 필요합니다.
{% endalert %}

Braze를 사용하면 고객이 기존의 기본 이미지를 자신만의 사용자 지정 이미지로 대체할 수 있습니다. 이를 위해 커스텀 이미지를 사용하여 새 `png` 파일을 만들고 앱의 이미지 번들에 추가합니다. 그런 다음, 라이브러리의 기본 이미지를 덮어쓰도록 파일 이름을 이미지 이름으로 변경합니다. 또한 다양한 휴대폰 크기에 맞추기 위해 `@2x` 및 `@3x` 버전의 이미지를 업로드해야 합니다. 다음은 콘텐츠 카드에서 재정의할 수 있는 이미지입니다.

- 플레이스홀더 이미지: `appboy_cc_noimage_lrg`
- 고정된 아이콘 이미지: `appboy_cc_icon_pinned`

대시보드에 입력하는 콘텐츠(메시지 텍스트, 이미지 URL, 링크 및 모든 키-값 페어 포함)의 콘텐츠 카드 크기는 최대 2KB이므로 보내기 전에 크기를 확인합니다. 이 크기를 초과하면 카드가 전송되지 않습니다.

{% alert important %}
현재 Xamarin iOS 통합에서 기본 이미지 재정의는 지원되지 않습니다.
{% endalert %}

## 다크 모드 비활성화하기

사용자 기기에서 다크 모드가 활성화된 경우 콘텐츠 카드 UI에 다크 테마 스타일이 적용되지 않도록 하려면 `ABKContentCardsTableViewController.enableDarkTheme` 속성정보를 설정합니다. `ABKContentCardsTableViewController` 인스턴스에서 직접 `enableDarkTheme` 속성정보에 액세스하거나 자체 UI에 가장 적합하도록 `ABKContentCardsViewController.contentCardsViewController` 속성정보를 통해 액세스할 수 있습니다.

{% tabs %}
{% tab 목표-C %}

```objc
// Accessing enableDarkTheme via ABKContentCardsViewController.contentCardsViewController.
- (IBAction)presentModalContentCards:(id)sender {
  ABKContentCardsViewController *contentCardsVC = [ABKContentCardsViewController new];
  contentCardsVC.contentCardsViewController.enableDarkTheme = NO;
  ...
  [self.navigationController presentViewController:contentCardsVC animated:YES completion:nil];
}

// Accessing enableDarkTheme directly.
- (IBAction)presentNavigationContentCards:(id)sender {
  ABKContentCardsTableViewController *contentCardsTableVC = [[ABKContentCardsTableViewController alloc] init];
  contentCardsTableVC.enableDarkTheme = NO;
  ...
  [self.navigationController pushViewController:contentCardsTableVC animated:YES];
}
```

{% endtab %}
{% tab swift %}

```swift
// Accessing enableDarkTheme via ABKContentCardsViewController.contentCardsViewController.
@IBAction func presentModalContentCards(_ sender: Any) {
  let contentCardsVC = ABKContentCardsViewController()
  contentCardsVC.contentCardsViewController.enableDarkTheme = false
  ...
  self.navigationController?.present(contentCardsVC, animated: true, completion: nil)
}

// Accessing enableDarkTheme directly.
@IBAction func presentNavigationContentCards(_ sender: Any) {
  let contentCardsTableVC = ABKContentCardsTableViewController()
  contentCardsTableVC.enableDarkTheme = false
  ...
  self.navigationController?.present(contentCardsTableVC, animated: true, completion: nil)
}
```

{% endtab %}
{% endtabs %}


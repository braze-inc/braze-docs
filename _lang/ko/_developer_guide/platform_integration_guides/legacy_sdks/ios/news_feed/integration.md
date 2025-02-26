---
nav_title: 통합
article_title: 뉴스피드 통합 for iOS
platform: iOS
page_order: 0
description: "이 문서에서는 뉴스피드 데이터 모델의 개요, iOS 애플리케이션에 뉴스피드를 통합하는 방법, 그리고 커스텀 보기 컨트롤러 통합 예제를 다룹니다."
channel:
  - news feed

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# 뉴스피드 통합

{% multi_lang_include deprecations/braze_sdk/news_feed.md %}

## 뉴스피드 데이터 모델

### 데이터 가져오기

뉴스피드 데이터 모델에 액세스하려면 뉴스피드 업데이트 이벤트에 가입합니다.

{% tabs %}
{% tab 목표-C %}

```objc
// Subscribe to feed updates
// Note: you should remove the observer where appropriate
[[NSNotificationCenter defaultCenter] addObserver:self
                                         selector:@selector(feedUpdated:)
                                             name:ABKFeedUpdatedNotification
                                           object:nil];
```                                           

```objc
// Called when the feed is refreshed (via `requestFeedRefresh`)
- (void)feedUpdated:(NSNotification *)notification {
  BOOL updateIsSuccessful = [notification.userInfo[ABKFeedUpdatedIsSuccessfulKey] boolValue];
  // check for success
  // get the cards using [[Appboy sharedInstance].feedController getCardsInCategories:ABKCardCategoryAll];
}
```

{% endtab %}
{% tab swift %}

```swift
// Subscribe to feed updates
// Note: you should remove the observer where appropriate
NotificationCenter.default.addObserver(self, selector:
  #selector(feedUpdated),
  name:NSNotification.Name.ABKFeedUpdated, object: nil)
```

```swift
// Called when the feed is refreshed (via `requestFeedRefresh`)
private func feedUpdated(_ notification: Notification) {
  if let updateSuccessful = notification.userInfo?[ABKFeedUpdatedIsSuccessfulKey] as? Bool {
    // check for success
    // get the cards using Appboy.sharedInstance()?.feedController.getCardsInCategories(.all);      
  }
}
```

{% endtab %}
{% endtabs %}

Braze에서 카드 데이터를 보낸 후에 변경하려면 카드 데이터의 딥 카피를 로컬에 저장하고 데이터를 업데이트한 후 직접 표시하는 것이 좋습니다. 카드는 [`ABKFeedController`](http://appboy.github.io/appboy-ios-sdk/docs/interface_a_b_k_feed_controller.html "abk 피드 컨트롤러")를 통해 접근할 수 있습니다.

## 뉴스피드 모델

Braze에는 배너 이미지, 자막 이미지, 텍스트 공지, 클래식과 같은 다섯 가지 고유한 카드 유형이 있습니다. 각 유형은 기본 모델에서 공통 속성을 상속하며 다음과 같은 추가 속성이 있습니다.

### 기본 카드 모델 속성

|등록정보|설명|
|---|---|
| `idString` | (읽기 전용) Braze에서 설정한 카드의 ID. |
| `viewed` | 이 속성은 사용자가 카드를 읽었는지 읽지 않았는지를 반영합니다. |
| `created` | (읽기 전용) 속성은 Braze 대시보드에서 카드 생성 시간의 Unix 타임스탬프입니다. |
| `updated` | (읽기 전용) 속성은 Braze 대시보드에서 카드의 최신 업데이트 시간의 Unix 타임스탬프입니다. |
| `categories` | 카드에 할당된 카테고리 목록, 카테고리가 없는 카드는 `ABKCardCategoryNoCategory`에 할당됩니다.<br><br>사용 가능한 카테고리:<br>- `ABKCardCategoryNoCategory`<br>- `ABKCardCategoryNews`<br>- `ABKCardCategoryAdvertising`<br>- `ABKCardCategoryAnnouncements`<br>- `ABKCardCategorySocial`<br>- `ABKCardCategoryAll` |
| `extras` | 선택적 `NSDictionary`(값: `NSString`). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### 배너 이미지 카드 속성

|등록정보|설명|
|---|---|
| `image` | (Required) 이 속성은 카드 이미지의 URL입니다. |
| `URL` | (Optional) 카드를 클릭한 후 열리는 URL입니다. HTTP(S) URL 또는 프로토콜 URL일 수 있습니다. |
| `domain` | (선택 사항) 속성 URL의 링크 텍스트, 예: @"blog.braze.com". 카드의 UI에 표시되어 카드 클릭의 동작 및 방향을 나타낼 수 있지만 기본 Braze 뉴스피드에서는 숨겨져 있습니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### 캡션이 있는 이미지 카드 속성

|등록정보|설명|
|---|---|
| `image` | (Required) 이 속성은 카드 이미지의 URL입니다. |
| `title` | (필수) 카드의 제목 텍스트. |
| `description` (필수) 카드의 본문 텍스트. |
| `URL` | (Optional) 카드를 클릭한 후 열리는 URL입니다. HTTP(S) URL 또는 프로토콜 URL일 수 있습니다. |
| `domain` | (선택 사항) 속성 URL의 링크 텍스트, 예: @"blog.braze.com". 카드의 UI에 표시되어 카드를 클릭할 때 동작과 방향을 나타낼 수 있습니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### 텍스트 공지 카드 (이미지 없는 자막 이미지) 속성

|등록정보|설명|
|---|---|
| `title` | (필수) 카드의 제목 텍스트. |
| `description` | (필수) 카드의 본문 텍스트. |
| `url` | (Optional) 카드를 클릭한 후 열리는 URL입니다. HTTP(S) URL 또는 프로토콜 URL일 수 있습니다. |
| `domain` | (선택 사항) 속성 URL의 링크 텍스트, 예: @"blog.braze.com". 카드의 UI에 표시되어 카드를 클릭할 때 동작과 방향을 나타낼 수 있습니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### 클래식 카드 속성

|등록정보|설명|
|---|---|
| `image` | (Required) 이 속성은 카드 이미지의 URL입니다. |
| `title` | (Optional) 카드의 제목 텍스트. |
| `description` | (필수) 카드의 본문 텍스트. |
| `URL` | (Optional) 카드를 클릭한 후 열리는 URL입니다. HTTP(S) URL 또는 프로토콜 URL일 수 있습니다. |
| `domain` | (선택 사항) 속성 URL의 링크 텍스트, 예: @"blog.braze.com". 카드의 UI에 표시되어 카드를 클릭할 때 동작과 방향을 나타낼 수 있습니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 카드 방법

|방법|설명|
|---|---|
| `logCardImpression` | 특정 카드에 대해 Braze에 노출 횟수를 수동으로 기록합니다. |
| `logCardClicked` | 특정 카드에 대해 Braze에 클릭을 수동으로 기록합니다. SDK는 카드에 유효한 값이 있는 `url` 속성정보가 있을 때만 카드 클릭을 기록합니다. 모든 `ABKCard`의 서브클래스에는 `url` 속성정보가 있습니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 로그 피드 디스플레이

자신의 사용자 인터페이스에 뉴스피드를 표시할 때 `- (void)logFeedDisplayed;`을 통해 뉴스피드 노출을 수동으로 기록할 수 있습니다. 예를 들어, 다음과 같습니다.

{% tabs %}
{% tab 목표-C %}

```objc
[[Appboy sharedInstance] logFeedDisplayed];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.logFeedDisplayed()
```

{% endtab %}
{% endtabs %}

## 뉴스피드 뷰 컨트롤러 통합

보기 컨트롤러 `ABKNewsFeedViewController`를 통합하면 Braze 뉴스피드가 표시됩니다.

보기 컨트롤러를 표시하는 방법을 선택할 때 많은 유연성이 지원됩니다. 다양한 탐색 구조를 수용하는 다양한 버전의 보기 컨트롤러가 있습니다.

{% alert note %}
인앱 메시지 클릭 시 기본 동작으로 호출되는 뉴스피드는 뉴스피드에 대해 설정한 모든 위임을 고려하지 않습니다. 그것을 존중하려면 [위임자를 `ABKInAppMessageUIController`]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/in-app_messaging/customization/setting_delegates/)에 설정하고 `ABKInAppMessageUIDelegate` 위임자 메서드 [`onInAppMessageClicked:`]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/in-app_messaging/customization/behavior_on_click/#customizing-in-app-message-body-clicks)을(를) 구현해야 합니다.
{% endalert %}

뉴스피드는 두 가지 뷰 컨트롤러 컨텍스트(네비게이션 또는 모달)와 통합될 수 있습니다.

### 탐색 컨텍스트 - ABKFeedViewControllerNavigationContext

{% tabs %}
{% tab 목표-C %}

```objc
ABKNewsFeedTableViewController *newsFeed = [[ABKNewsFeedTableViewController alloc] init];
[self.navigationController pushViewController:newsFeed animated:YES];
```

{% endtab %}
{% tab swift %}

```swift
let newsFeed = ABKNewsFeedTableViewController()
self.navigationController?.pushViewController(newsFeed, animated: true)
```

{% endtab %}
{% endtabs %}

탐색 모음의 `title`을 사용자 지정하려면 `ABKNewsFeedTableViewController` 인스턴스 `navigationItem`의 제목 속성정보를 설정합니다.

### 모달 context - ABKFeedViewControllerModalContext

이 모달은 모달 보기에서 보기 컨트롤러를 표시하는 데 사용되며, 상단에 탐색 막대가 있고 막대 오른쪽에 **Done** 버튼이 있습니다. Modal의 제목을 사용자 지정하려면 `ABKNewsFeedTableViewController` 인스턴스 `navigationItem`의 `title` 속성정보를 설정합니다. 

위임이 **설정되지 않은** 경우 **완료** 버튼은 Modal 보기를 닫습니다. 위임이 **설정된** 경우, **완료** 버튼은 위임을 호출하며, 위임 자체가 보기를 닫아야 합니다.

{% tabs %}
{% tab 목표-C %}

```objc
ABKNewsFeedViewController *newsFeed = [[ABKNewsFeedViewController alloc] init];
[self presentViewController:newsFeed animated:YES completion:nil];
```

{% endtab %}
{% tab swift %}

```swift
let newsFeed = ABKNewsFeedViewController()
self.present(newsFeed, animated: true, completion: nil)
```

{% endtab %}
{% endtabs %}

보기 컨트롤러 예제를 보려면 [뉴스피드 샘플 앱](https://github.com/Appboy/appboy-ios-sdk/tree/master/Samples/NewsFeed/BrazeNewsFeedSample)을 확인하세요.



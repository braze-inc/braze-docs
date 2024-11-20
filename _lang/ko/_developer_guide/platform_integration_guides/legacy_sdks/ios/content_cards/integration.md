---
nav_title: 통합
article_title: iOS용 콘텐츠 카드 보기 컨트롤러 통합
platform: iOS
page_order: 1
description: "이 참조 문서에서는 iOS 애플리케이션에 사용할 수 있는 통합 단계, 데이터 모델 및 카드별 속성정보를 다룹니다."
channel:
  - content cards
search_rank: 3
noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# 콘텐츠 카드 통합

## 콘텐츠 카드 데이터 모델

콘텐츠 카드 데이터 모델은 iOS SDK에서 사용할 수 있습니다.

### 데이터 가져오기

콘텐츠 카드 데이터 모델에 액세스하려면 콘텐츠 카드 업데이트 이벤트에 가입합니다.

{% tabs %}
{% tab 목표-C %}
```objc
// Subscribe to Content Cards updates
// Note: you should remove the observer where appropriate
[[NSNotificationCenter defaultCenter] addObserver:self
                                         selector:@selector(contentCardsUpdated:)
                                             name:ABKContentCardsProcessedNotification
                                           object:nil];
```

```objc
// Called when Content Cards are refreshed (via `requestContentCardsRefresh`)
- (void)contentCardsUpdated:(NSNotification *)notification {
  BOOL updateIsSuccessful = [notification.userInfo[ABKContentCardsProcessedIsSuccessfulKey] boolValue];
  if (updateIsSuccessful) {
    // get the cards using [[Appboy sharedInstance].contentCardsController getContentCards];
  }
}
```
{% endtab %}
{% tab swift %}
```swift
// Subscribe to content card updates
// Note: you should remove the observer where appropriate
NotificationCenter.default.addObserver(self, selector:
  #selector(contentCardsUpdated),
  name:NSNotification.Name.ABKContentCardsProcessed, object: nil)
```

```swift
// Called when the Content Cards are refreshed (via `requestContentCardsRefresh`)
@objc private func contentCardsUpdated(_ notification: Notification) {
  if let updateIsSuccessful = notification.userInfo?[ABKContentCardsProcessedIsSuccessfulKey] as? Bool {
    if (updateIsSuccessful) {
      // get the cards using Appboy.sharedInstance()?.contentCardsController.contentCards
    }
  }
}
```
{% endtab %}
{% endtabs %}

Braze에서 카드 데이터를 보낸 후에 변경하려면 카드 데이터의 딥 카피를 로컬에 저장하고 데이터를 업데이트한 후 직접 표시하는 것이 좋습니다. 카드는 [`ABKContentCardsController`](https://appboy.github.io/appboy-ios-sdk/docs/interface_a_b_k_content_cards_controller.html)를 통해 접근할 수 있습니다.

## 콘텐츠 카드 모델

Braze는 세 가지 콘텐츠 카드 유형(배너, 자막 이미지 및 클래식)을 제공합니다. 각 유형은 기본 `ABKContentCard` 클래스에서 공통 속성정보를 상속받으며 다음과 같은 추가 속성정보가 있습니다.

### 기본 콘텐츠 카드 모델 속성 - ABKContentCard

|등록정보|설명|
|---|---|
|`idString` | (읽기 전용) Braze에서 설정한 카드의 ID. |
| `viewed` | 이 속성정보는 사용자가 카드를 조회했는지 여부를 반영합니다.|
| `created` | (읽기 전용) 이 속성은 Braze에서 카드 생성 시간의 Unix 타임스탬프입니다. |
| `expiresAt` | (읽기 전용) 이 속성은 카드의 만료 시간에 대한 Unix 타임스탬프입니다.|
| `dismissible` | 이 속성은 사용자가 카드를 해제할 수 있는지 여부를 반영합니다.|
| `pinned` | 이 속성정보는 대시보드에서 카드가 '고정됨'으로 설정되었는지 여부를 반영합니다.|
| `dismissed` | 이 속성은 사용자가 카드를 닫았는지 여부를 반영합니다.|
| `url` | 카드를 클릭한 후 열리는 URL입니다. HTTP(s) URL 또는 프로토콜 URL일 수 있습니다.|
| `openURLInWebView` | 이 속성정보는 URL이 앱 내에서 열릴지, 외부 웹 브라우저에서 열릴지를 결정합니다.|
| `extras`| 선택적 `NSDictionary`(값: `NSString`).|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### 배너 콘텐츠 카드 속성정보 - ABKBannerContentCard

|등록정보|설명|
|---|---|
| `image` | 이 속성은 카드 이미지의 URL입니다.|
| `imageAspectRatio` | 이 속성정보는 카드 이미지의 종횡비이며 이미지 로드가 완료되기 전에 힌트로 사용됩니다. 특정 상황에서는 속성이 제공되지 않을 수 있습니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### 캡션이 있는 이미지 콘텐츠 카드 속성 - ABKCaptionedImageCard

|등록정보|설명|
|---|---|
| `image` | 이 속성은 카드 이미지의 URL입니다.|
| `imageAspectRatio` | 이 속성은 카드 이미지의 종횡비입니다.|
| `title` | 카드의 제목 텍스트입니다.|
| `cardDescription` | 카드의 본문 텍스트.|
| `domain` | 속성 URL의 링크 텍스트, 예를 들어 @"blog.braze.com". 카드의 UI에 표시되어 카드를 클릭할 때 동작과 방향을 나타낼 수 있습니다.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### 클래식 콘텐츠 카드 속성 - ABKClassicContentCard

|등록정보|설명|
|---|---|
| `image` | (Optional) 이 속성은 카드 이미지의 URL입니다.|
| `title` | 카드의 제목 텍스트입니다. |
| `cardDescription` | 카드의 본문 텍스트. |
| `domain` | 속성 URL의 링크 텍스트, 예를 들어 @"blog.braze.com". 카드의 UI에 표시되어 카드를 클릭할 때 동작과 방향을 나타낼 수 있습니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 카드 방법

|방법|설명|
|---|---|
| `logContentCardImpression` | 특정 카드에 대해 Braze에 노출 횟수를 수동으로 기록합니다. |
| `logContentCardClicked` | 특정 카드에 대해 Braze에 클릭을 수동으로 기록합니다. SDK는 카드에 유효한 값이 있는 `url` 속성정보가 있을 때만 카드 클릭을 기록합니다. |
| `logContentCardDismissed` | 특정 카드에 대해 Braze에 해제를 수동으로 기록합니다. SDK는 카드의 `dismissed` 속성정보가 이미 `true`로 설정되지 않은 경우에만 카드 방출을 기록합니다. |
| `isControlCard` | 카드가 A/B 테스트의 제어 카드인지 확인합니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

자세한 내용은 [클래스 참조 설명서](https://appboy.github.io/appboy-ios-sdk/docs/interface_a_b_k_content_card.html)를 참조하십시오.

## Content Cards 뷰 컨트롤러 통합

콘텐츠 카드는 두 가지 보기 컨트롤러 컨텍스트(탐색 또는 Modal)와 통합될 수 있습니다.

### 탐색 컨텍스트

내비게이션 컨트롤러에 `ABKContentCardsTableViewController` 인스턴스를 푸시하는 예: 

{% tabs %}
{% tab 목표-C %}

```objc
ABKContentCardsTableViewController *contentCards = [[ABKContentCardsTableViewController alloc] init];
contentCards.title = @"Content Cards Title";
contentCards.disableUnreadIndicator = YES;
[self.navigationController pushViewController:contentCards animated:YES];
```

{% endtab %}
{% tab swift %}

```swift
let contentCards = ABKContentCardsTableViewController()
contentCards.title = "Content Cards Title"
contentCards.disableUnreadIndicator = true
navigationController?.pushViewController(contentCards, animated: true)
```

{% endtab %}
{% endtabs %}

{% alert note %}
탐색 모음의 제목을 사용자 지정하려면 `ABKContentCardsTableViewController` 인스턴스 `navigationItem`의 제목 속성정보를 설정합니다.
{% endalert %}

### 모달 컨텍스트

이 모달은 모달 보기에서 보기 컨트롤러를 표시하는 데 사용되며, 상단에 탐색 막대가 있고 막대 측면에 **Done** 버튼이 있습니다.

{% tabs %}
{% tab 목표-C %}

```objc
ABKContentCardsViewController *contentCards = [[ABKContentCardsViewController alloc] init];
contentCards.contentCardsViewController.title = @"Content Cards Title";
contentCards.contentCardsViewController.disableUnreadIndicator = YES;
[self.navigationController presentViewController:contentCards animated:YES completion:nil];
```

{% endtab %}
{% tab swift %}

```swift
let contentCards = ABKContentCardsViewController()
contentCards.contentCardsViewController.title = "Content Cards Title"
contentCards.contentCardsViewController.disableUnreadIndicator = true
self.present(contentCards, animated: true, completion: nil)
```

{% endtab %}
{% endtabs %}

보기 컨트롤러 예제를 보려면 [콘텐츠 카드 샘플 앱](https://github.com/Appboy/appboy-ios-sdk/tree/master/Samples/ContentCards/BrazeContentCardsSampleApp)을 확인하세요.

{% alert note %}
헤더를 사용자 정의하려면 부모 `ABKContentCardsViewController` 인스턴스에 포함된 `ABKContentCardsTableViewController` 인스턴스에 속하는 `navigationItem`의 제목 속성을 설정하십시오.
{% endalert %}

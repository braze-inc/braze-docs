---
nav_title: 통합
article_title: Android 및 FireOS용 뉴스피드 통합
page_order: 1.2
platform: 
  - Android
  - FireOS
description: "이 참조 문서에서는 Android 또는 FireOS 애플리케이션에 대한 다양한 뉴스피드 카드 유형, 사용 가능한 다양한 카드별 속성정보 및 커스텀 통합 예제를 다룹니다."
channel:
  - news feed
  
---

# 뉴스피드 통합

> 이 참조 문서에서는 Android 또는 FireOS 애플리케이션에 대한 다양한 뉴스피드 카드 유형, 사용 가능한 다양한 카드별 속성정보 및 커스텀 통합 예제를 다룹니다.

{% multi_lang_include deprecations/braze_sdk/news_feed.md %}

Android에서 뉴스피드는 Braze Android UI 프로젝트에서 사용할 수 있는 [조각](http://developer.android.com/guide/components/fragments.html)으로 구현됩니다. [조각에 대한 Google의 문서 조각안드로이드](https://developer.android.com/guide/fragments#Adding "문서를") 참조하세요: 활동에 조각을 추가하는 방법에 대한 자세한 내용은 조각을 참조하세요.

`BrazeFeedFragment` 클래스는 자동으로 새로 고쳐지고 뉴스피드와 로그 사용량 분석의 콘텐츠를 표시합니다. 사용자의 뉴스피드에 표시할 수 있는 카드는 Braze 대시보드에서 설정할 수 있습니다.

## 카드 유형

Braze에는 배너 이미지, 자막 이미지, 텍스트 공지, 짧은 뉴스와 같은 다섯 가지 고유한 카드 유형이 있습니다. 각 유형은 기본 모델에서 공통 속성을 상속하며 다음과 같은 추가 속성이 있습니다.

### 기본 카드 모델 속성

[기본 카드](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/index.html) 모델은 모든 카드의 기본 동작을 제공합니다.  

|등록정보|설명|
|---|---|
| `getId()` | Braze가 설정한 카드의 ID를 반환합니다. |
| `getViewed()` | 사용자가 카드를 읽었는지 또는 읽지 않았는지를 반영하는 부울을 반환합니다. |
| `getExtras()` | 이 카드에 대한 키-값 추가 항목의 맵을 반환합니다. |
| `setViewed(boolean)` | 카드의 표시되는 필드를 설정합니다. |
| `getCreated()` | Braze 대시보드에서 카드 생성 시간의 유닉스 타임스탬프를 반환합니다. |
| `getUpdated()` | Braze 대시보드에서 카드의 최신 업데이트 시간의 유닉스 타임스탬프를 반환합니다. |
| `getCategories()` | 카드에 할당된 카테고리 목록을 반환하며, 이때 카테고리가 없는 카드에 `ABKCardCategoryNoCategory`가 할당됩니다. |
| `isInCategorySet(EnumSet)` | 카드가 지정된 카테고리 세트에 속하면 true를 반환합니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### 배너 이미지 카드 속성

[배너 이미지 카드는](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-banner-image-card/index.html) 클릭 가능한 전체 크기 이미지입니다.

|등록정보|설명|
|---|---|
| `getImageUrl()` | 카드 이미지의 URL을 반환합니다. |
| `getUrl()` | 카드를 클릭한 후 열릴 URL을 반환합니다. HTTP 또는 HTTPS URL 또는 프로토콜 URL일 수 있습니다. |
| `getDomain()` | 속성 URL의 링크 텍스트를 반환합니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### 캡션 이미지 카드 속성

[자막 이미지 카드](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-captioned-image-card/index.html)는 클릭 가능한 전체 크기 이미지로, 설명 텍스트와 함께 제공됩니다.

|등록정보|설명|
|---|---|
| `getImageUrl()` | 카드 이미지의 URL을 반환합니다. |
| `getTitle()` | 카드의 제목 텍스트를 반환합니다. |
| `getDescription()` | 카드의 본문 텍스트를 반환합니다. |
| `getUrl()` | 카드를 클릭한 후 열릴 URL을 반환합니다.  HTTP 또는 HTTPS URL 또는 프로토콜 URL일 수 있습니다. |
| `getDomain()` | 속성 URL의 링크 텍스트를 반환합니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### 텍스트 공지 카드(이미지가 없는 캡션 이미지) 속성

[텍스트 공지 카드는](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-text-announcement-card/index.html) 설명 텍스트가 포함된 클릭 가능한 카드입니다.

|등록정보|설명|
|---|---|
| `getTitle()` | 카드의 제목 텍스트를 반환합니다. |
| `getDescription()` | 카드의 본문 텍스트를 반환합니다. |
| `getUrl()` | 카드를 클릭한 후 열릴 URL을 반환합니다. HTTP 또는 HTTPS URL 또는 프로토콜 URL일 수 있습니다. |
| `getDomain()` | 속성 URL의 링크 텍스트를 반환합니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### 짧은 뉴스 카드 속성

[짧은 뉴스 카드는](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-short-news-card/index.html) 이미지와 함께 설명 텍스트가 포함된 클릭 가능한 카드입니다.

|등록정보|설명|
|---|---|
| `getImageUrl()` | 카드 이미지의 URL을 반환합니다. |
| `getTitle()` | 카드의 제목 텍스트를 반환합니다. |
| `getDescription()` | 카드의 본문 텍스트를 반환합니다. |
| `getUrl()` | 카드를 클릭한 후 열릴 URL을 반환합니다. HTTP 또는 HTTPS URL 또는 프로토콜 URL일 수 있습니다. |
| `getDomain()` | 속성 URL의 링크 텍스트를 반환합니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 세션 분석

Android UI 조각은 세션 분석을 자동으로 추적하지 않습니다. 세션이 [올바르게 추적]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/tracking_sessions/)되는지 확인하려면 앱이 열릴 때 `IBraze.openSession()`을 호출합니다.

## 링크 처리

`AndroidManifest.xml`에서 `BrazeFeedActivity`를 등록하여 인앱 메시지에서 뉴스피드에 연결 기능을 활성화해야 합니다.

## 사용자 지정 피드 통합

완전히 사용자 정의된 방식으로 피드를 표시하려면 모델의 데이터로 채워진 자체 보기를 사용하여 표시할 수 있습니다. 뉴스피드 모델을 얻으려면 뉴스피드 업데이트에 가입하고 결과 모델 데이터를 사용하여 보기를 채워야 합니다. 또한 사용자가 뷰와 상호 작용할 때 모델 개체에 대한 분석을 기록해야 합니다.

### 1부: 피드 업데이트 구독하기

먼저 커스텀 피드 클래스에서 가입자를 보유할 비공개 변수를 선언합니다.

```java
// subscriber variable
private IEventSubscriber<FeedUpdatedEvent> mFeedUpdatedSubscriber;
```

다음으로, 일반적으로 커스텀 피드 활동의 `Activity.onCreate()`에 다음 코드를 추가하여 Braze의 피드 업데이트에 가입합니다.

```java
// Remove the old subscription first
Braze.getInstance(context).removeSingleSubscription(mFeedUpdatedSubscriber, FeedUpdatedEvent.class);
mFeedUpdatedSubscriber = new IEventSubscriber<FeedUpdatedEvent>() {
  @Override
  public void trigger(final FeedUpdatedEvent event) {
    // This list of Card objects included in the FeedUpdatedEvent should be used to populate your News Feed views.
    List<Card> cards = event.getFeedCards();
    // your logic here
  }
};
Braze.getInstance(context).subscribeToFeedUpdates(mFeedUpdatedSubscriber);

// Request a refresh of feed data
Braze.getInstance(context).requestFeedRefresh();
```

커스텀 피드 활동이 보기 밖으로 이동하면 가입을 취소하는 것이 좋습니다. 활동의 `onDestroy()` 생명 주기 메서드에 다음 코드를 추가하십시오:

```
Braze.getInstance(context).removeSingleSubscription(mFeedUpdatedSubscriber, FeedUpdatedEvent.class);
```

### 2부: 로그 분석

분석은 Braze 보기를 사용할 때만 자동으로 처리되므로 커스텀 보기를 사용하는 경우 분석을 수동으로 기록해야 합니다.

피드 표시를 기록하려면 [`Braze.logFeedDisplayed()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/log-feed-displayed.html)를 호출합니다.

노출을 기록하거나 카드를 클릭하면 [`Card.logClick()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/log-click.html) 및 [`Card.logImpression()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/log-impression.html) 를 각각 누르세요.


---
nav_title: 통합
article_title: Android 및 FireOS용 콘텐츠 카드 통합
page_order: 0
platform: 
  - Android
  - FireOS
description: "이 참조 문서에서는 Android 또는 FireOS 애플리케이션에 사용할 수 있는 콘텐츠 카드 통합, 여러 데이터 모델 및 카드별 속성정보를 다룹니다."
channel:
  - content cards
search_rank: 1
---

# Content Cards 통합

> 이 참조 문서에서는 Android 또는 FireOS 애플리케이션에 사용할 수 있는 콘텐츠 카드 통합, 여러 데이터 모델 및 카드별 속성정보를 다룹니다.

{% alert note %}
준비가 되면 구현 및 사용자 정의를 시작하려면 [콘텐츠 카드 사용자 정의 가이드]({{site.baseurl}}/developer_guide/customization_guides/content_cards)를 참조하세요.
{% endalert %}

Android에서 콘텐츠 카드 피드는 Braze Android UI 프로젝트에서 사용할 수 있는 [프래그먼트](https://developer.android.com/guide/components/fragments.html)로 구현됩니다. [Google의 조각 안드로이드](https://developer.android.com/guide/fragments#Adding "문서") 보기: 활동에 조각을 추가하는 방법에 대한 정보는 조각 문서를 참조하세요.

[`ContentCardsFragment`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards/-content-cards-fragment/index.html) 클래스는 자동으로 새로고침되고 콘텐츠 카드의 내용을 표시하며 사용 분석을 기록합니다. 사용자의 `ContentCards`에 나타날 수 있는 카드는 Braze 대시보드에서 생성됩니다.

## 콘텐츠 카드 데이터 모델 {#card-types-for-android}

콘텐츠 카드 데이터 모델은 Android SDK에서 사용할 수 있습니다. 콘텐츠 카드 데이터 모델에 대한 전체 참조는 [SDK 참조 설명서](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/index.html)를 참조하세요.

Braze에는 기본 모델을 공유하는 네 가지 고유한 콘텐츠 카드 유형이 있습니다: [이미지 전용](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-image-only-card/index.html), [캡션이 있는 이미지](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-captioned-image-card/index.html), [클래식(텍스트 공지)](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-text-announcement-card/index.html), 및 [클래식 (짧은 뉴스)](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-short-news-card/index.html). 각 유형은 기본 모델에서 공통 속성을 상속받으며 다음과 같은 추가 속성을 가지고 있습니다.

카드 데이터 구독에 대한 정보는 [로그 분석]({{site.baseurl}}/developer_guide/customization_guides/content_cards/logging_analytics)을 참조하십시오.

### 기본 콘텐츠 카드 모델 속성 {#base-card-for-android}

[기본 카드](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/index.html) 모델은 모든 카드에 대한 기초적인 동작을 제공합니다.  

|등록정보 | 설명 |
|---|---|
|`getId()` | Braze가 설정한 카드의 ID를 반환합니다.|
|`getViewed()` | 부울값을 반환하여 사용자가 카드를 읽었는지 읽지 않았는지를 반영합니다.|
|`getExtras()` | 이 카드에 대한 키-값 추가 항목의 맵을 반환합니다.|
|`getCreated()`  | Braze에서 카드 생성 시간의 Unix 타임스탬프를 반환합니다.|
|`getIsPinned` | 카드가 고정되어 있는지 여부를 반영하는 부울 값을 반환합니다.|
|`getOpenUriInWebView()`  | 불리언을 반환하여 이 카드의 Uris를 열어야 하는지 여부를 반영합니다 <br> Braze WebView에서 또는 이외 위치에서.|
|`getExpiredAt()` | 카드의 만료일을 가져옵니다.|
|`getIsRemoved()` | 최종사용자가 이 카드를 해제했는지 여부를 반영하는 부울을 반환합니다.|
|`getIsDismissible()`  | 카드가 고정되어 있는지 여부를 반영하는 부울 값을 반환합니다.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### 이미지 전용 이미지 카드 속성 {#banner-image-card-for-android}

[이미지 전용 카드](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-image-only-card/index.html)는 클릭 가능한 전체 크기 이미지입니다.

|등록정보 | 설명 |
|---|---|
|`getImageUrl()` | 카드 이미지의 URL을 반환합니다.|
|`getUrl()` | 카드를 클릭한 후 열리는 URL을 반환합니다. HTTP(s) URL 또는 프로토콜 URL일 수 있습니다.|
|`getDomain()` | 속성 URL의 링크 텍스트를 반환합니다.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### 캡션이 있는 이미지 카드 속성 {#captioned-image-card-for-android}

[캡션이 있는 이미지 카드](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-captioned-image-card/index.html)는 설명 텍스트가 포함된 클릭 가능한 전체 크기 이미지입니다.

|등록정보 | 설명 |
|---|---|
|`getImageUrl()` | 카드 이미지의 URL을 반환합니다.|
|`getTitle()` | 카드의 제목 텍스트를 반환합니다.|
|`getDescription()` | 카드의 본문 텍스트를 반환합니다.|
|`getUrl()` | 카드를 클릭한 후 열리는 URL을 반환합니다. HTTP(s) URL 또는 프로토콜 URL일 수 있습니다.|
|`getDomain()` | 속성 URL의 링크 텍스트를 반환합니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### 클래식 카드 속성정보 {#text-Announcement-card-for-android}

이미지가 포함되지 않은 클래식 카드는 [텍스트 공지 카드](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-text-announcement-card/index.html)가 됩니다. 이미지가 포함된 경우 [짧은 뉴스 카드](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-short-news-card/index.html)를 받게 됩니다.

|등록정보 | 설명 |
|---|---|
|`getTitle()` | 카드의 제목 텍스트를 반환합니다. |
|`getDescription()` | 카드의 본문 텍스트를 반환합니다. |
|`getUrl()` | 카드를 클릭한 후 열리는 URL을 반환합니다. HTTP(s) URL 또는 프로토콜 URL일 수 있습니다. | 
|`getDomain()` | 속성 URL의 링크 텍스트를 반환합니다. |
|`getImageUrl()` | 카드 이미지의 URL을 반환하며, 클래식 짧은 뉴스 카드에만 적용됩니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 카드 방법

모든 [`Card`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/index.html) 데이터 모델 오브젝트는 Braze 서버에 사용자 이벤트를 기록하기 위해 다음 분석 메서드를 제공합니다.

|방법 | 설명 |
|---|---|
|`logImpression()` | 특정 카드에 대해 Braze에 노출 횟수를 수동으로 기록합니다. |
|`logClick()` | 특정 카드에 대해 Braze에 클릭을 수동으로 기록합니다. |
|`setIsDismissed()` | 특정 카드에 대해 Braze에 해제를 수동으로 기록합니다. 카드가 이미 해제됨 상태로 표시된 경우 다시 해제됨 상태로 표시할 수 없습니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }


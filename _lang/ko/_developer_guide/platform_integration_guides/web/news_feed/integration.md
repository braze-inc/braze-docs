---
nav_title: 통합
article_title: 웹을 위한 뉴스피드 통합
platform: Web
page_order: 0
page_type: reference
description: "이 문서에서는 뉴스피드 카드 유형과 Braze SDK를 통해 뉴스피드를 웹 애플리케이션에 통합하는 방법을 다룹니다."
channel: news feed

---

# 뉴스피드 통합

> 이 문서에서는 Braze 웹 SDK에 대한 뉴스피드 설정 방법을 다룹니다.

{% multi_lang_include deprecations/braze_sdk/news_feed.md %}

뉴스피드는 사용자를 위한 완전히 맞춤화할 수 있는 인앱 콘텐츠 피드입니다. 우리의 타겟팅 및 세분화는 각 사용자의 관심사에 맞춘 콘텐츠 스트림을 생성할 수 있게 해줍니다. 사용자 생애주기에서 위치와 앱의 특성에 따라, 온보딩 콘텐츠 서버, 광고 센터, 교육 지원 센터 또는 일반 뉴스 센터일 수 있습니다.

## 예시 뉴스피드

<img src="{% image_buster /assets/img_archive/WebNewsFeed.png %}" alt="팔로우 요청, 업데이트 공지, 광고 등 여러 알림을 표시하는 뉴스피드 예제." height="600" />

## 통합

뉴스피드의 표시를 토글하려면 Braze 웹 SDK를 통해 다음을 호출하면 됩니다.

``` javascript
braze.toggleFeed();
```

최근에 캐시된 뉴스피드 카드를 표시합니다(이 카드가 1분 넘게 경과했거나 뉴스피드를 한 번도 새로 고치지 않은 경우 새로 고침 시작). 화면에 있는 동안 Braze 서버에서 새 카드가 수신되면 자동으로 표시를 업데이트합니다.

기본적으로 피드는 웹사이트의 오른쪽에 고정 위치 사이드바로 표시됩니다. 또는 응답형 CSS를 통해 모바일 기기에서는 전체 화면 오버레이로 표시됩니다. 이 동작을 재정의하고 고정 위치의 뉴스피드를 상위 요소 내부에 표시하려면 다음 요소를 `showFeed`의 첫 번째 인수로 제공합니다.

``` javascript
braze.toggleFeed(document.getElementById('my-news-feed-parent'));
```

뉴스피드 카드의 특정 정적 세트를 표시하거나 서버에서 카드를 필터링하거나 직접 새로 고침 의미 체계를 제공하려면 자동 업데이트를 비활성화하고 직접 카드를 제공할 수 있습니다.

``` javascript
braze.subscribeToFeedUpdates(function(feed) {
  var cards = feed.cards;
  braze.showFeed(undefined, cards);
});
braze.requestFeedRefresh();
```

`showFeed`, `destroyFeed`, `toggleFeed`에 대한 전체 설명서는 [JSDocs](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#showfeed)를 참조하세요.

## 카드 유형

Braze 웹 SDK는 기본 모델 [카드](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.card.html)를 공유하는 세 가지 고유한 뉴스피드 카드 유형([ClassicCard](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.classiccard.html), [Banner](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.imageonly.html), [CaptionedImage](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.captionedimage.html))을 지원합니다.

### 읽지 않은 카드 수 요청

언제든지 전화로 읽지 않은 카드의 수를 요청할 수 있습니다:

``` javascript
braze.getCachedFeed().getUnreadCardCount();
```

종종 미열람 뉴스피드 카드 개수를 나타내는 배지를 구동하는 데 사용됩니다. 자세한 내용은 [JS 참조 문서](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.feed.html)를 참조하십시오. Braze는 피드를 표시하거나 `braze.requestFeedRefresh();`를 호출할 때까지 새 페이지를 로드할 때 뉴스피드 카드를 새로 고치지 않으며, 이 함수는 0을 반환합니다.

### 키-값 쌍

`Card` 오브젝트는 선택적으로 키-값 페어를 `extras`와 같이 전달할 수 있습니다. 애플리케이션에서 추가 처리를 위해 카드와 함께 데이터를 전송하는 데 사용할 수 있습니다. `card.extras`를 호출하여 이러한 값에 액세스합니다.

## 맞춤화

Braze UI 요소는 Braze 대시보드 내 작성기와 일치하는 기본 모양과 느낌을 사용하며, 다른 Braze 모바일 플랫폼과의 일관성을 목표로 합니다. 기본 스타일은 Braze SDK 내 CSS에서 정의됩니다. 애플리케이션에서 선택한 스타일을 재정의하여 나만의 배경 이미지, 글꼴 모음, 스타일, 크기, 애니메이션 등으로 표준 피드를 맞춤 설정할 수 있습니다.

예를 들어, 다음은 뉴스피드를 800px 너비로 표시하는 재정의 예제입니다.

``` css
body .ab-feed {
  width: 800px;
}
```

## 카테고리

Braze 뉴스피드의 인스턴스는 특정 '카테고리'의 카드만 수신하도록 구성할 수 있습니다. 이를 통해 단일 애플리케이션 내에서 여러 개의 뉴스피드 스트림을 효과적으로 통합할 수 있습니다.

뉴스피드 카테고리는 `toggleFeed` 에 세 번째 `allowedCategories` 파라미터를 제공하여 정의할 수 있습니다:

``` javascript
braze.toggleFeed(undefined, undefined, [braze.Card.Category.NEWS]);
```

다음 예시와 같이 여러 카테고리의 조합으로 피드를 채울 수도 있습니다:

``` javascript
braze.toggleFeed(undefined, undefined, [braze.Card.Category.ANNOUNCEMENTS, braze.Card.Category.NEWS]);
```

## 읽음 및 읽지 않음 표시기

Braze는 아래 그림과 같이 뉴스피드 카드에 읽지 않음 및 읽음 표시기를 제공합니다:

![텍스트와 함께 시계 이미지가 표시된 뉴스피드 카드입니다. 텍스트의 오른쪽 상단 모서리에는 카드가 읽혔는지 여부를 나타내는 파란색 또는 회색 삼각형이 있습니다. 파란색 삼각형은 카드를 읽었음을 나타냅니다.]({% image_buster /assets/img_archive/UnreadvsReadNewsFeedCard.png %})

### 표시기 비활성화

이 기능을 비활성화하려면 다음 스타일을 CSS에 추가하십시오:

``` css
.ab-read-dot { display: none; }
.ab-read-indicator { display: none; }
```


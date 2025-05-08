---
nav_title: 캐러셀 뷰
article_title: iOS용 콘텐츠 카드 캐러셀 보기
platform: iOS
page_order: 5
description: "이 문서에서는 iOS 애플리케이션에 대해 콘텐츠 카드 캐러셀 뷰 사용 사례를 구현하는 방법을 다룹니다."
channel:
  - content cards
noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# 사용 사례: 캐러셀 뷰

![문서에서 콘텐츠 카드의 캐러셀을 보여주는 샘플 뉴스 앱.]({% image_buster/assets/img_archive/cc_politer_carousel.png %}){: style="max-width:35%;float:right;margin-left:15px;border:none;"}

이 섹션에서는 사용자가 수평으로 스와이프하여 추가 추천 카드를 볼 수 있는 다중 카드 캐러셀 피드를 구현하는 방법을 다룹니다. 캐러셀 뷰를 통합하려면 완전히 사용자 지정된 콘텐츠 카드 구현을 사용해야 합니다. [기기, 걷기, 달리기 접근 방식]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/customize/#customization-approaches)의 '달리기' 단계에 해당합니다.

이 접근 방식을 사용하면 Braze 뷰와 기본 로직을 사용하지 않고, 대신 Braze 모델의 데이터로 채워진 자체 뷰를 사용하여 콘텐츠 카드를 완전히 커스텀 방식으로 표시하게 됩니다.

개발 노력 수준 측면에서 기본 구현과 캐러셀 구현 간의 주요 차이점은 다음과 같습니다.

- 자체 보기 빌드
- 콘텐츠 카드 분석 기록
- 추가 클라이언트 측 로직을 도입하여 캐러셀에 표시할 카드 수와 종류 결정

## 구현

### 1단계: 커스텀 보기 컨트롤러 생성

콘텐츠 카드 캐러셀을 생성하려면, 커스텀 보기 컨트롤러(예: `UICollectionViewController`)를 생성하고 [데이터 업데이트에 가입]({{site.baseurl}}/developer_guide/platform_integration_guides/legacy_sdks/ios/content_cards/integration/#getting-the-data)합니다. 기본 `ABKContentCardTableViewController`를 확장하거나 서브클래스로 만들 수 없습니다. 기본 콘텐츠 카드 유형만 처리할 수 있기 때문입니다.

### 2단계: 분석 구현

완전한 커스텀 보기 컨트롤러를 생성할 때, 콘텐츠 카드 노출 횟수, 클릭 및 해제는 자동으로 기록되지 않습니다. 노출 횟수, 해제 이벤트 및 클릭이 Braze 대시보드 분석에 제대로 기록되도록 각 분석 방법을 구현해야 합니다.

분석 방법에 대한 정보는 [카드 방법]({{site.baseurl}}/developer_guide/platform_integration_guides/legacy_sdks/ios/content_cards/integration/#card-methods)을 참조하십시오. 

{% alert note %}
같은 페이지에서 보기 구현 중에 유용할 수 있는 일반 콘텐츠 카드 모델 클래스에서 상속된 다양한 속성정보도 자세히 설명합니다.
{% endalert %}

### 3단계: 콘텐츠 카드 옵저버를 생성합니다

[콘텐츠 카드 관찰자]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/content_cards/multiple_feeds/#step-2-set-up-a-content-card-listener)를 생성하여 콘텐츠 카드의 도착을 처리하고, 캐러셀에서 한 번에 특정 수의 카드를 표시하기 위한 조건 로직을 구현합니다. 기본적으로 콘텐츠 카드는 생성 날짜를 기준으로 정렬되며(최신 날짜부터), 사용자는 적격한 모든 카드를 볼 수 있습니다.

즉, 다양한 방식으로 추가 디스플레이 논리를 주문하고 적용할 수 있습니다. 예를 들어, 배열에서 처음 다섯 개의 콘텐츠 카드 객체를 선택하거나 데이터 모델의 `extras` 속성에 키-값 쌍을 도입하여 조건 로직을 구축할 수 있습니다.

캐러셀을 보조 콘텐츠 카드 피드로 구현하는 경우 [여러 콘텐츠 카드 피드 사용]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/content_cards/multiple_feeds/)을 참조하여 키-값 페어에 따라 카드를 올바른 피드로 정렬하는 방법을 알아봅니다.

{% alert important %}
마케팅 팀과 개발자 팀이 어떤 키-값 페어를 사용할지 조율하는 것이 중요합니다(예: `feed_type = brand_homepage`). 마케터가 Braze 대시보드에 입력하는 키-값 페어는 개발자가 앱 로직에 빌드하는 키-값 페어와 정확히 일치해야 하기 때문입니다.
{% endalert %}

iOS 특정 개발자 설명서에서 콘텐츠 카드 클래스, 메서드 및 속성은 iOS [`ABKContentCard` 클래스 참조](https://appboy.github.io/appboy-ios-sdk/docs/interface_a_b_k_content_card.html)를 참조하세요.

## 고려사항

- 완전히 커스텀 보기를 사용하면 `ABKContentCardsController`에서 사용되는 메서드를 확장하거나 서브클래스로 작성할 수 없습니다. 대신 데이터 모델 메서드와 속성을 직접 통합해야 합니다.
- 캐러셀 뷰의 로직 및 구현은 Braze의 기본 콘텐츠 카드 유형이 아니므로 사용 사례를 달성하기 위한 로직은 개발 팀에서 제공하고 지원해야 합니다.
- 캐러셀에 특정 수의 카드를 한 번에 표시하도록 클라이언트 측 로직을 구현해야 합니다.


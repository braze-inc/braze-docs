---
nav_title: 콘텐츠 카드 정보
article_title: 콘텐츠 카드 정보
page_order: 0
description: "이 참고 문서에서는 Braze 콘텐츠 카드 채널에 대한 개요와 일반적인 사용 사례를 제공합니다."
channel:
  - content cards
search_rank: 4
---

# [![Braze 학습 과정]](https://learning.braze.com/content-cards) ( [{% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/content-cards){: style="float:right;width:120px;border:0;" class="noimgborder"} 콘텐츠 카드 정보

> 콘텐츠 카드는 앱이나 웹사이트에 직접 임베드되므로 자연스럽고 매끄러운 사용자 경험을 통해 사용자의 참여를 유도할 수 있습니다. 이를 통해 앱 또는 웹사이트 환경을 더 잘 제어할 수 있으며 메시지 받은 편지함, 캐러셀, 배너를 만들고 다른 채널(예: 이메일 또는 푸시 알림)의 도달 범위를 확장할 수 있습니다.

콘텐츠 카드는 추가 기능이며 반드시 구매해야 합니다. 콘텐츠 카드를 시작하려면 Braze 고객 성공 매니저 또는 지원팀에 문의하세요.

{% alert note %}
뉴스피드 도구를 사용 중인 경우 보다 유연하고 맞춤 설정이 가능하며 안정적인 콘텐츠 카드 메시징 채널로 전환하는 것이 좋습니다. 뉴스피드도 더 이상 사용되지 않습니다. 자세한 내용은 [마이그레이션 가이드를]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/migrating_from_news_feed/) 참조하거나 Braze 계정 관리자에게 문의하세요.
{% endalert %}

## 콘텐츠 카드 사용의 이점

다음은 개발자가 앱에 콘텐츠를 빌드하는 것과 콘텐츠 카드를 사용하는 것의 몇 가지 이점입니다:

- **더욱 간편한 세분화 및 개인화:** 사용자 데이터는 Braze에 저장되므로 콘텐츠 카드를 사용하여 오디언스를 쉽게 정의하고 메시지를 개인화할 수 있습니다.
- **중앙 집중식 보고:** 콘텐츠 카드 분석은 Braze에서 추적되므로 모든 캠페인에 대한 인사이트를 한 곳에서 확인할 수 있습니다.
- **일관된 고객 여정:** Braze에서 콘텐츠 카드를 다른 채널과 결합하여 일관된 고객 경험을 만들 수 있습니다. 인기 있는 사용 사례는 푸시 알림을 보낸 다음 푸시에 참여하지 않은 사람을 위해 앱에 콘텐츠 카드로 알림을 저장하는 것입니다. 개발자가 앱에 직접 콘텐츠를 구축한 경우 해당 콘텐츠는 나머지 메시징과 분리되어 있습니다.
- **필수 옵트인이 필요하지 않습니다:** 인앱 메시지와 마찬가지로 콘텐츠 카드에는 사용자의 옵트인이나 권한이 필요하지 않습니다. 하지만 인앱 메시지는 권한이 없고 수명이 짧지만, 콘텐츠 카드는 권한이 없고 영구적입니다. 즉, 인앱 메시지와 콘텐츠 카드를 함께 사용하는 메시징 전략이 균형을 이룰 수 있습니다.
- **메시징 경험을 더욱 효과적으로 제어할 수 있습니다.** 콘텐츠 카드의 초기 설정은 여전히 개발자의 도움이 필요하지만, 그 이후에는 메시지, 수신자, 타이밍 등을 Braze 대시보드에서 직접 제어할 수 있습니다.

### 숫자로 보는 콘텐츠 카드

마케팅 담당자가 Braze에서 콘텐츠 카드를 직접 제작하기 때문에 앱이나 웹사이트를 완전히 개편하지 않고도 메시징을 업데이트하고 투자 수익을 얻을 수 있습니다. 다음은 콘텐츠 카드의 ROI에 대한 몇 가지 유용한 통계입니다:

- 콘텐츠 카드는 72시간 동안 매출을 높이는 데 이메일보다 **38배** 더 효과적입니다.[^1]
- 로열티 등록 캠페인에 콘텐츠 카드를 사용하면 전환율이 **5배** 증가합니다.[^1]
- 푸시 알림, 인앱 메시지, 콘텐츠 카드를 통해 사용자에게 아웃리치를 보내면 푸시만 통해 참여한 사용자에 비해 **6.9배** 더 많은 세션이 생성됩니다.]
- 이메일, 인앱 메시지, 콘텐츠 카드를 통해 사용자에게 아웃리치를 보내면 이메일만으로 참여한 사용자에 비해 평균 사용자 수명이 **3.6배** 더 길어집니다[^2]

## 작동 방식

콘텐츠 카드의 핵심은 데이터의 모양이 아니라 실제로 데이터의 페이로드입니다. Braze는 콘텐츠 카드 데이터를 표시하는 템플릿 보기(배너, 모달, 캡션 이미지)를 제공하며, 이는 궁극적으로 메시지의 모양을 결정합니다.

이제 조금 더 기술적인 이야기를 해보겠습니다. 콘텐츠 카드에는 크게 세 가지 부분이 있습니다:

- **모델:** 카드에 저장되는 데이터의 종류
- **보기:** 카드의 모양
- **컨트롤러:** 사용자가 카드와 상호 작용하는 방식

기본 구현의 경우 대시보드 또는 API를 통해 카드 콘텐츠(모델)를 추가하고 뷰 및 컨트롤러는 뷰 컨트롤러라고 하는 것으로 처리합니다. 뷰 컨트롤러는 전체 애플리케이션과 화면 사이의 '접착제'입니다.

## 사용 사례

콘텐츠 카드의 몇 가지 일반적인 사용 사례는 이 섹션을 참조하세요.

{% alert tip %}
더 많은 영감을 얻으려면 추천 프로그램, 신제품 출시, 구독 갱신 등 20개 이상의 맞춤형 캠페인이 포함된 [콘텐츠 카드 영감 가이드를](https://www.braze.com/resources/reports-and-guides/content-cards-inspiration-guide) 확인하는 것이 좋습니다.
{% endalert %}

{% tabs %}
{% tab 온보딩 및 다음 단계 %}

신규 사용자가 앱과 웹사이트를 탐색할 때 전략적으로 배치된 콘텐츠 카드를 통해 제공하는 콘텐츠의 가치와 이점을 안내하세요. 홈페이지에서 콘텐츠 카드를 사용하여 사용자가 다른 커뮤니케이션 채널을 선택하도록 유도하고, 콘텐츠 카드가 제공하는 전용 온보딩 탭에 미완료 온보딩 작업을 저장하세요. 사용자가 원하는 작업을 완료한 후 카드를 제거하는 것을 잊지 마세요!

<style>
  .imgDiv {
      text-align: center;
    }
</style>

<div class="imgDiv">
<img src="{% image_buster /assets/img_archive/cc_usecase_onboarding.png %}" style="border:0px">
</div>

{% endtab %}
{% tab 이벤트 참여 %}

사용자의 홈페이지 상단에 콘텐츠 카드를 표시하여 이벤트 참여를 유도하고, 위치 타겟팅을 사용하여 잠재 사용자가 있는 곳에 도달할 수 있도록 합니다. 관련 오프라인 이벤트에 사용자를 초대하면 특히 브랜드와의 이전 활동을 활용한 개인화된 메시지를 통해 특별한 느낌을 줄 수 있습니다.

<div class="imgDiv">
<img src="{% image_buster /assets/img_archive/cc_usecase_event.png %}" style="border:0px">
</div>

{% endtab %}
{% tab 권장 사항 %}

사용자 행동 및 선호도에 대한 데이터를 사용하여 홈페이지 또는 받은편지함 콘텐츠 카드에서 관련 콘텐츠를 실시간으로 표시하고 이를 다시 제품 오퍼링으로 끌어들일 수 있습니다.

<div class="imgDiv">
<img src="{% image_buster /assets/img_archive/cc_usecase_recommendation.png %}" style="border:0px">
</div>

{% endtab %}
{% tab 영업 및 프로모션 %}

콘텐츠 카드를 활용하여 홈페이지 또는 전용 프로모션 받은편지함에서 바로 프로모션 메시지와 미신청 오퍼를 강조 표시할 수 있습니다. 각 고객의 이전 구매 내역을 기반으로 관련 콘텐츠를 가져와 관심을 끄는 개인화된 프로모션을 제공하세요.

<div class="imgDiv">
<img src="{% image_buster /assets/img_archive/cc_usecase_promo.png %}" style="border:0px">
</div>

{% endtab %}
{% endtabs %}

### 기타 사용 사례

이러한 주요 사용 사례 외에도 고객은 콘텐츠 카드를 매우 다양한 방식으로 사용합니다. 콘텐츠 카드의 강점은 유연성입니다. 원하는 사용 사례가 여기에 표시되지 않은 경우 [키-값 쌍을]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/key_value_pairs/) 설정하고 페이로드를 앱이나 웹사이트로 전송할 수 있습니다.

## 콘텐츠 카드 배치

이 섹션에서는 앱이나 웹사이트 내에 콘텐츠 카드를 배치하는 가장 일반적인 세 가지 방법에 대해 설명합니다:

- [메시지 받은편지함](#message-inbox)
- [캐러셀](#carousel)
- [배너](#banner)

이러한 배치의 로직과 구현은 Braze의 기본값이 아니므로 엔지니어링 팀에서 이러한 사용 사례를 달성하기 위한 작업을 제공하고 지원해야 합니다. 이러한 배치를 구현하는 방법에 대한 개요는 [사용자 지정 콘텐츠 카드 만들기를]({{site.baseurl}}/developer_guide/customization_guides/content_cards/creating_custom_content_cards) 참조하세요.

![]({% image_buster /assets/img_archive/cc_placements.png %}){: style="border:0px;"}

### 메시지 받은편지함

![]({% image_buster /assets/img_archive/cc_placement_inbox.png %}){: style="float:right;margin-left:15px;max-width:30%;border:0px;"}

메시지 받은 편지함(알림 센터 또는 피드라고도 함)은 앱이나 웹사이트에서 원하는 형식으로 콘텐츠 카드를 표시할 수 있는 영구적인 공간입니다. 받은편지함의 각 메시지는 고유한 콘텐츠 카드입니다. 

메시지 받은 편지함은 최소한의 개발이 필요한 기본 구현입니다. Braze는 iOS, Android 및 웹에서 메시지 받은 편지함을 위한 [보기 컨트롤러를](#how-it-works) 제공하여 작성 프로세스를 쉽게 만들 수 있도록 합니다.

#### 혜택

- 사용자는 한 곳에서 여러 장의 카드를 받을 수 있습니다.
- 다른 채널(특히 푸시 알림)에서 놓치거나 무시한 정보를 다시 표시하는 효율적인 방법
- 옵트인 필요 없음

#### 동작

사용자가 카드를 받을 자격이 되면 받은 편지함에 카드가 자동으로 표시됩니다. 콘텐츠 카드는 일괄적으로 볼 수 있도록 제작되었으므로 사용자는 자격이 있는 모든 카드를 한 번에 볼 수 있습니다.

기본 구현을 사용하면 받은편지함의 콘텐츠 카드가 클래식(제목, 텍스트 및 선택적 이미지 포함), 이미지 전용 또는 캡션이 있는 이미지 카드로 표시될 수 있습니다. 앱에서 메시지 받은편지함의 위치를 선택할 수 있습니다.

콘텐츠 카드에는 기본 스타일이 제공되지만 앱의 모양과 느낌에 따라 카드와 피드를 표시하도록 커스텀 구현을 선택할 수 있습니다.

### 캐러셀

![]({% image_buster /assets/img_archive/cc_politer_carousel.png %}){: style="float:right;margin-left:15px;max-width:30%;border:0px;"}

캐러셀은 고객이 스와이프하여 볼 수 있는 여러 콘텐츠를 단일 공간에 표시합니다. 이미지, 텍스트, 동영상 또는 이들의 조합으로 구성된 슬라이드쇼가 될 수 있습니다. 이는 사용자 정의 구현이며 개발자의 약간의 작업이 필요합니다.

#### 혜택

- 사용자는 한 곳에서 여러 장의 카드를 받을 수 있습니다.
- 추천을 표시하는 매력적인 방법

#### 동작

사용자가 카드를 받을 자격이 되면 캐러셀이 추가되는 앱 페이지의 캐러셀에 카드가 표시됩니다. 사용자는 가로로 스와이프하여 추가 추천 카드를 볼 수 있습니다.

이 기능은 커스텀 구현이므로 개발자와 협력하여 콘텐츠 카드를 표시하는 고유한 보기를 구축해야 합니다. 기본 클래식, 이미지 전용 및 캡션이 있는 이미지 카드는 이 구현에서 지원되지 않습니다.

### 배너

![]({% image_buster /assets/img_archive/cc_placement_banner.png %}){: style="float:right;margin-left:15px;max-width:30%;border:0px;"}

콘텐츠 카드는 홈페이지 또는 다른 지정된 페이지 상단에 지속적으로 표시되는 동적 배너로 표시될 수 있습니다.

#### 혜택

- 인앱 메시지와 달리 페이지에 지속되므로 잠재 고객에게 도달할 수 있는 시간이 더 길어집니다.
- 홈페이지의 눈에 잘 띄는 위치에 새로운 콘텐츠를 소개할 수 있는 좋은 방법

#### 동작

사용자는 자신에게 가장 적합한 관련성 높은 콘텐츠를 보고 참여할 수 있습니다. 이 기능은 사용자 지정 구현이므로 개발자와 협력하여 콘텐츠 카드를 표시하도록 보기를 사용자 지정해야 합니다.

## 콘텐츠 카드 통합

개발자는 Braze SDK를 통합할 때 콘텐츠 카드를 통합하게 됩니다. 콘텐츠 카드와 통합하는 방법에 대한 자세한 내용은 해당 플랫폼의 개발자 가이드 문서를 참조하세요.

- [iOSiOS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/content_cards/integration/ "콘텐츠 카드 통합 가이드")
- [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/content_cards/integration/ "Android 콘텐츠 카드 통합 가이드")
- [웹]({{site.baseurl}}/developer_guide/platform_integration_guides/web/content_cards/integration/ "웹 콘텐츠 카드 통합 가이드")

## 출처

<span></span>

[^1]: [고객 유지 캠페인을 최대한 활용하기 위한 8가지 팁](https://www.braze.com/resources/articles/8-tips-for-making-the-most-of-your-customer-retention-campaigns)
[^2]: [보고서: 크로스 채널 마케팅의 차이점](https://www.braze.com/resources/reports-and-guides/the-cross-channel-marketing-difference-report)
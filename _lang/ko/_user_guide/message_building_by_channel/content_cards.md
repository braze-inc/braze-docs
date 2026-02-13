---
nav_title: 콘텐츠 카드
article_title: 콘텐츠 카드
page_order: 1
layout: dev_guide
guide_top_header: "콘텐츠 카드"
guide_top_text: "콘텐츠 카드를 사용하면 고객의 경험을 방해하지 않으면서도 고객이 좋아하는 앱 내에서 고도로 타겟팅된 동적 스트림의 풍부한 콘텐츠를 고객에게 전송할 수 있습니다. <br><br>콘텐츠 카드는 귀하의 앱이나 웹사이트에 직접 삽입되어 메시지 수신함과 이메일 또는 푸시 알림과 같은 다른 채널의 범위를 확장하는 커스텀 인터페이스를 생성할 수 있습니다. 또한, 콘텐츠 카드는 카드 고정, 카드 방출, API 기반 전달, 연결된 콘텐츠, 커스텀 카드 만료 시간, 카드 분석 및 푸시 알림과의 쉬운 조정을 포함한 보다 개인화된 기능을 지원합니다. <br><br>**콘텐츠 카드의 가용성은 귀하의 Braze 패키지에 따라 다릅니다.** 시작하려면 귀하의 계정 매니저 또는 고객 성공 매니저에게 문의하십시오.**"
description: "이 랜딩 페이지에는 Braze 콘텐츠 카드가 있습니다. 여기에서 콘텐츠 카드를 만드는 방법, 콘텐츠 카드를 커스텀하는 방법, 테스트, 보고 등에 대한 문서를 찾을 수 있습니다."
channel:
  - content cards
search_rank: 5
guide_featured_title: "섹션 기사"
guide_featured_list:
- name: 콘텐츠 카드 만들기
  link: /docs/user_guide/message_building_by_channel/content_cards/create/
  image: /assets/img/braze_icons/columns-01.svg
- name: 카드 생성
  link: /docs/user_guide/message_building_by_channel/content_cards/create/card_creation
  image: /assets/img/braze_icons/message-check-circle.svg
- name: 크리에이티브 디테일
  link: /docs/user_guide/message_building_by_channel/content_cards/creative_details/
  image: /assets/img/braze_icons/brush-02.svg
- name: 테스트
  link: /docs/user_guide/engagement_tools/campaigns/testing_and_more/sending_test_messages/
  image: /assets/img/braze_icons/beaker-02.svg
- name: 보고
  link: /docs/user_guide/message_building_by_channel/content_cards/reporting/
  image: /assets/img/braze_icons/pie-chart-01.svg
- name: 모범 사례
  link: /docs/user_guide/message_building_by_channel/content_cards/best_practices
  image: /assets/img/braze_icons/check-square-broken.svg
---

## [![Braze 학습 과정]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/content-cards){: style="float:right;width:120px;border:0;" class="noimgborder"} 콘텐츠 카드 사용의 이점

다음은 콘텐츠 카드를 사용하는 몇 가지 이점으로, 개발자가 귀하의 앱에 콘텐츠를 구축하는 것과 비교됩니다:

- **더욱 간편한 세분화 및 개인화:** 사용자 데이터는 Braze에 저장되므로 콘텐츠 카드를 사용하여 오디언스를 쉽게 정의하고 메시지를 개인화할 수 있습니다.
- **중앙 집중식 보고:** 콘텐츠 카드 분석은 Braze에서 추적되므로 모든 캠페인에 대한 인사이트를 한 곳에서 확인할 수 있습니다.
- **일관된 고객 여정:** Braze에서 콘텐츠 카드를 다른 채널과 결합하여 일관된 고객 경험을 만들 수 있습니다. 인기 있는 사용 사례는 푸시 알림을 보낸 다음 푸시에 참여하지 않은 사람을 위해 앱에 콘텐츠 카드로 알림을 저장하는 것입니다. 만약 콘텐츠가 개발자에 의해 귀하의 앱에 직접 구축된다면, 나머지 메시징과는 격리됩니다.
- **필수 옵트인 없음:** 인앱 메시지와 마찬가지로 콘텐츠 카드에는 사용자의 옵트인이나 권한이 필요하지 않습니다. 하지만 인앱 메시지는 허가 없이 짧은 기간 동안 존재하는 반면, 콘텐츠 카드는 허가 없이 영구적입니다. 이는 인앱 메시지와 콘텐츠 카드를 함께 사용하는 메시징 전략이 훌륭한 균형을 이룬다는 것을 의미합니다.
- **메시징 경험을 더욱 효과적으로 제어할 수 있습니다.** 콘텐츠 카드의 초기 설정을 도와줄 개발자가 여전히 필요하지만, 이후에는 Braze 대시보드에서 메시지, 수신자, 타이밍 등을 직접 제어할 수 있습니다.

### 숫자로 보는 콘텐츠 카드

마케터인 귀하가 Braze에서 콘텐츠 카드를 직접 구축하므로, 앱이나 웹사이트를 완전히 개편하지 않고도 메시징 업데이트를 하고 투자 수익을 얻을 수 있습니다. 다음은 콘텐츠 카드의 ROI에 대한 몇 가지 유용한 통계입니다:

- 콘텐츠 카드는 이메일보다 판매를 증가시키는 데 **38X** 더 효과적입니다.[^1]
- 로열티 등록 캠페인에서 콘텐츠 카드를 사용하면 전환율이 **5X** 증가합니다.[^1]
- 푸시 알림, 인앱 메시지 및 콘텐츠 카드를 통해 사용자에게 아웃리치를 보내면 푸시만으로 참여한 사용자에 비해 **6.9X** 더 많은 세션이 발생합니다.[^2]
- 이메일, 인앱 메시지 및 콘텐츠 카드를 통해 사용자에게 아웃리치를 보내면 이메일만으로 참여한 사용자에 비해 **3.6X** 더 긴 평균 사용자 수명이 발생합니다.[^2]

## 작동 방식

Braze는 콘텐츠 카드를 표시하기 위해 다양한 콘텐츠 카드 유형을 제공합니다: 클래식, 캡션 이미지 또는 이미지. 콘텐츠 카드의 핵심은 데이터의 모양이 아니라 실제로 데이터의 페이로드입니다. 

이제 조금 더 기술적인 이야기를 해보겠습니다. 콘텐츠 카드에는 크게 세 가지 부분이 있습니다:

- **모델:** 카드에 저장되는 데이터의 종류
- **보기:** 카드의 모양
- **컨트롤러:** 사용자가 카드와 상호 작용하는 방식

기본 구현을 위해 카드 콘텐츠—모델—을 대시보드 또는 API를 통해 추가하고, 뷰와 컨트롤러는 뷰 컨트롤러라고 불리는 것에 의해 처리됩니다. 뷰 컨트롤러는 전체 애플리케이션과 화면 사이의 '접착제'입니다.

## 사용 사례

이 섹션에서는 콘텐츠 카드의 일반적인 사용 사례를 참조하십시오.

{% alert tip %}
더 많은 영감을 얻으려면 [콘텐츠 카드 영감 가이드](https://www.braze.com/resources/reports-and-guides/content-cards-inspiration-guide)를 확인하는 것을 강력히 권장합니다. 이 가이드에는 추천 프로그램, 신제품 출시 및 구독 갱신을 포함하여 20개 이상의 사용자 정의 캠페인이 포함되어 있습니다.
{% endalert %}

{% tabs %}
{% tab Onboarding and next steps %}

새로운 사용자가 귀하의 앱과 웹사이트를 탐색할 때, 전략적으로 배치된 콘텐츠 카드를 통해 제공하는 가치와 이점을 안내하십시오. 홈페이지에 콘텐츠 카드로 다른 커뮤니케이션 채널에 사용자가 참여하도록 유도하고, 콘텐츠 카드로 구동되는 전용 온보딩 탭에 미완료된 온보딩 작업을 저장하십시오. 사용자가 원하는 작업을 완료한 후 카드를 제거하는 것을 잊지 마십시오!

<style>
  .imgDiv {
      text-align: center;
    }
</style>

<div class="imgDiv">
<img src="{% image_buster /assets/img_archive/cc_usecase_onboarding.png %}" style="border:0px">
</div>

{% endtab %}
{% tab Event attendance %}

사용자의 홈페이지 상단에 콘텐츠 카드를 전시하여 이벤트 참석을 유도하고, 위치 타겟팅을 사용하여 잠재 사용자에게 도달하십시오. 관련 오프라인 이벤트에 사용자를 초대하면 특히 브랜드와의 이전 활동을 활용한 개인화된 메시지를 통해 특별한 느낌을 줄 수 있습니다.

<div class="imgDiv">
<img src="{% image_buster /assets/img_archive/cc_usecase_event.png %}" style="border:0px">
</div>

{% endtab %}
{% tab Recommendations %}

사용자 행동 및 선호도에 대한 데이터를 사용하여 홈페이지 또는 받은편지함 콘텐츠 카드에서 관련 콘텐츠를 실시간으로 표시하고 이를 다시 제품 오퍼링으로 끌어들일 수 있습니다.

<div class="imgDiv">
<img src="{% image_buster /assets/img_archive/cc_usecase_recommendation.png %}" style="border:0px">
</div>

{% endtab %}
{% tab Sales and promotions %}

콘텐츠 카드를 활용하여 홈페이지 또는 전용 프로모션 받은편지함에서 바로 프로모션 메시지와 미신청 오퍼를 강조 표시할 수 있습니다. 각 고객의 이전 구매 내역을 기반으로 관련 콘텐츠를 가져와 관심을 끄는 개인화된 프로모션을 제공하세요.

<div class="imgDiv">
<img src="{% image_buster /assets/img_archive/cc_usecase_promo.png %}" style="border:0px">
</div>

{% endtab %}
{% endtabs %}

### 기타 사용 사례

이러한 주요 사용 사례 외에도 고객은 콘텐츠 카드를 매우 다양한 방식으로 사용합니다. 콘텐츠 카드의 강점은 유연성입니다. 원하는 사용 사례가 여기에 표시되지 않는 경우, [키-값 쌍]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/key_value_pairs/)을 설정하고 페이로드를 귀하의 앱이나 웹사이트로 전송할 수 있습니다.

## 귀하의 앱 내 콘텐츠 카드

이 섹션에서는 귀하의 앱이나 웹사이트 내에서 콘텐츠 카드를 배치하는 가장 일반적인 방법을 다룹니다:

- [메시지 받은편지함](#message-inbox)
- [캐러셀](#carousel)

이 배치의 논리와 구현은 Braze의 기본값이 아니므로 귀하의 엔지니어링 팀이 이러한 사용 사례를 달성하기 위한 작업을 제공하고 지원해야 합니다. 이러한 배치를 구현하는 방법에 대한 개요는 [사용자 지정 콘텐츠 카드 만들기를]({{site.baseurl}}/developer_guide/content_cards/creating_cards/) 참조하세요.

![메시지 받은편지함, 캐러셀 및 배너와 같은 다양한 배치 옵션을 보여주는 3개의 예시 콘텐츠 카드.]({% image_buster /assets/img_archive/cc_placements.png %}){: style="border:0px;"}

### 메시지 받은편지함

!["메시지 받은편지함" 배치를 사용하는 예시 콘텐츠 카드.]({% image_buster /assets/img_archive/cc_placement_inbox.png %}){: style="float:right;margin-left:15px;max-width:30%;border:0px;"}

메시지 받은 편지함(알림 센터 또는 피드라고도 함)은 앱이나 웹사이트에서 원하는 형식으로 콘텐츠 카드를 표시할 수 있는 영구적인 공간입니다. 받은편지함의 각 메시지는 고유한 콘텐츠 카드입니다. 

메시지 받은편지함은 최소한의 개발이 필요한 기본 구현입니다. Braze는 iOS, Android 및 웹에서 메시지 받은편지함을 위한 [뷰 컨트롤러](#how-it-works)를 제공하여 생성 프로세스를 쉽게 만듭니다.

#### Benefits

- 사용자는 한 곳에서 여러 장의 카드를 받을 수 있습니다.
- 다른 채널(특히 푸시 알림)에서 놓치거나 거부된 정보를 다시 표시하는 효율적인 방법입니다.
- 옵트인 필요 없음

#### 동작

사용자가 카드를 받을 자격이 되면 받은 편지함에 카드가 자동으로 표시됩니다. 콘텐츠 카드는 대량으로 보기 위해 설계되었으므로 사용자는 자신이 자격이 있는 모든 카드를 한 번에 볼 수 있습니다.

기본 구현을 사용하면 받은편지함의 콘텐츠 카드가 클래식(제목, 텍스트 및 선택적 이미지 포함), 이미지 전용 또는 캡션이 있는 이미지 카드로 표시될 수 있습니다. 앱에서 메시지 받은편지함의 위치를 선택할 수 있습니다.

콘텐츠 카드에는 기본 스타일이 제공되지만 앱의 모양과 느낌에 따라 카드와 피드를 표시하도록 커스텀 구현을 선택할 수 있습니다.

### 캐러셀

!["캐러셀" 배치를 사용하는 예시 콘텐츠 카드.]({% image_buster /assets/img_archive/cc_politer_carousel.png %}){: style="float:right;margin-left:15px;max-width:30%;border:0px;"}

캐러셀은 고객이 스와이프하여 볼 수 있는 여러 콘텐츠를 단일 공간에 표시합니다. 그들은 이미지, 텍스트, 비디오 또는 이들의 조합으로 된 슬라이드쇼일 수 있습니다. 이는 사용자 정의 구현이며 개발자의 약간의 작업이 필요합니다.

#### 혜택

- 사용자는 한 곳에서 여러 장의 카드를 받을 수 있습니다.
- 추천을 표시하는 매력적인 방법

#### 동작

사용자가 카드를 받을 자격이 되면 캐러셀이 추가되는 앱 페이지의 캐러셀에 카드가 표시됩니다. 사용자는 가로로 스와이프하여 추가 추천 카드를 볼 수 있습니다.

이 기능은 커스텀 구현이므로 개발자와 협력하여 콘텐츠 카드를 표시하는 고유한 보기를 구축해야 합니다. 기본 클래식, 이미지 전용 및 캡션이 있는 이미지 카드는 이 구현에서 지원되지 않습니다.

## 콘텐츠 카드 통합

개발자는 Braze SDK를 통합할 때 콘텐츠 카드를 통합하게 됩니다. 콘텐츠 카드와 통합하는 방법에 대한 자세한 내용은 해당 플랫폼의 개발자 가이드 문서를 참조하세요.

- [iOS]({{site.baseurl}}/developer_guide/content_cards/?sdktab=swift)
- [Android]({{site.baseurl}}/developer_guide/content_cards/?sdktab=android)
- [Web]({{site.baseurl}}/developer_guide/content_cards/?sdktab=web)

## 출처

<span></span>

[^1]: [고객 유지 캠페인을 최대한 활용하기 위한 8가지 팁](https://www.braze.com/resources/articles/8-tips-for-making-the-most-of-your-customer-retention-campaigns)
[^2]:  [보고서: 크로스 채널 마케팅의 차이점](https://www.braze.com/resources/reports-and-guides/the-cross-channel-marketing-difference-report)

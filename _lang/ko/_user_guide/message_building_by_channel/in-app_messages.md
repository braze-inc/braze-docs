---
nav_title: "앱 내 메시지"
article_title: 앱 내 메시지
page_order: 2
alias: /in-app_messages/
layout: dev_guide
guide_top_header: "앱 내 메시지"
guide_top_text: "앱 내 메시지는 푸시 알림으로 사용자의 하루를 방해하지 않고 콘텐츠를 사용자에게 전달하는 데 도움을 줍니다. 이러한 메시지는 사용자의 앱 외부로 전달되지 않으며 홈 화면에 침입하지 않습니다. <br><br>맞춤형 앱 내 메시지는 사용자 경험을 향상시키고 청중이 앱에서 최대 가치를 얻도록 돕습니다. 다양한 레이아웃과 사용자 정의 도구를 선택할 수 있어 앱 내 메시지가 사용자와의 상호작용을 그 어느 때보다 높입니다. 이 메시지는 맥락을 가지고 있으며 긴급성이 낮고 사용자가 앱 내에서 활동할 때 전달됩니다. 앱 내 메시지의 예시는 <a href='https://www.braze.com/customers'>고객 사례</a>를 확인하세요."
description: "이 랜딩 페이지는 모든 앱 내 메시지 관련 정보를 제공합니다. 여기에서 앱 내 메시지를 만드는 방법, 드래그 앤 드롭 편집기, 메시지 사용자 정의 방법, 보고서 작성 등과 관련된 기사를 찾을 수 있습니다."
channel:
  - in-app messages
search_rank: 5
guide_featured_title: "인기 기사"
guide_featured_list:
- name: "드래그 앤 드롭 편집기"
  link: /docs/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/
  image: /assets/img/braze_icons/phone-02.svg
- name: "전통적인 편집기"
  link: /docs/user_guide/message_building_by_channel/in-app_messages/traditional/
  image: /assets/img/braze_icons/phone-02.svg
- name: "창의적인 세부사항"
  link: /docs/user_guide/message_building_by_channel/in-app_messages/creative_details/
  image: /assets/img/braze_icons/brush-02.svg

guide_menu_title: "More articles"
guide_menu_list:
- name: "테스트"
  link: /docs/user_guide/message_building_by_channel/in-app_messages/testing/
  image: /assets/img/braze_icons/beaker-02.svg
- name: "보고서"
  link: /docs/user_guide/message_building_by_channel/in-app_messages/reporting/
  image: /assets/img/braze_icons/bar-chart-01.svg
- name: "다크 모드"
  link: /docs/user_guide/message_building_by_channel/in-app_messages/traditional/dark-mode/
  image: /assets/img/braze_icons/phone-02.svg
- name: "앱 스토어 평가 요청"
  link: /docs/user_guide/message_building_by_channel/in-app_messages/ios_app_rating_prompt/
  image: /assets/img/braze_icons/star-01.svg
- name: "간단한 설문조사"
  link: /docs/user_guide/message_building_by_channel/in-app_messages/traditional/templates/simple_survey/
  image: /assets/img/braze_icons/bar-chart-07.svg
- name: "메시지의 로케일"
  link: /docs/locales_in_messages/
  image: /assets/img/braze_icons/translate-01.svg
- name: "모범 사례"
  link: /docs/user_guide/message_building_by_channel/in-app_messages/best_practices
  image: /assets/img/braze_icons/check-square-broken.svg
- name: "자주 묻는 질문"
  link: /docs/user_guide/message_building_by_channel/in-app_messages/faq/
  image: /assets/img/braze_icons/annotation-question.svg
---

## [![브레이즈 학습 과정]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/messaging-channels-in-app-in-browser){: style="float:right;width:120px;border:0;" class="noimgborder"} 잠재적 사용 사례

인앱 메시지에서 제공하는 풍부한 콘텐츠 수준을 활용하여 다양한 사용 사례에 이 채널을 활용할 수 있습니다:

| 사용 사례 | 설명 |
| --- | --- |
| 푸시 프라이밍 | 고객에게 앱이나 사이트의 푸시 수신 동의를 받는 이점을 보여주기 위해 풍부한 인앱 메시지를 사용하여 [푸시 프라이밍]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/) 캠페인을 실행하고 푸시 권한을 부여하라는 프롬프트를 제공합니다.
| 판매 및 프로모션 | 정적 프로모션 코드나 제안을 포함한 시각적으로 매력적인 미디어로 고객을 맞이하기 위해 모달 인앱 메시지를 사용하세요. 그들이 그렇지 않았을 때 구매 또는 전환을 유도하세요. |
| 기능 채택 장려 | 고객이 앱의 다른 부분을 사용하거나 서비스를 활용하도록 유도하세요. |
| 매우 개인화된 캠페인 | 고객이 앱이나 사이트에 들어올 때 가장 먼저 인앱 메시지를 표시하세요. 사용자가 행동을 취하도록 유도하고 따라서 아웃리치를 더 효과적으로 만들기 위해 [연결된 콘텐츠]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/)과 같은 브레이즈 개인화 기능을 추가하세요.
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

고려해야 할 다른 사용 사례는 다음과 같습니다:

- 새로운 앱 기능
- 앱 관리
- 리뷰
- 앱 업그레이드 또는 업데이트
- 경품 및 추첨

## 표준 메시지 유형

다음 탭은 사용자가 우리의 표준 인앱 메시지 유형 중 하나인 슬라이드업, 모달 및 전체 화면 인앱 메시지를 열 때의 모습을 보여줍니다.

{% tabs %}
{% tab Slideup %}

슬라이드업 메시지는 일반적으로 앱 화면의 상단과 하단에 나타납니다(메시지를 생성할 때 이 설정을 할 수 있습니다). 이 메시지는 사용자에게 새로운 서비스 약관, 쿠키 및 기타 정보 조각을 알리는 데 좋습니다.

\![슬라이드업 인앱 메시지가 앱 화면의 하단에서 나타나는 모습. 슬라이드업에는 아이콘 이미지와 간단한 메시지가 포함됩니다.]({% image_buster /assets/img/slideup-behavior.gif %}){: style="border:0px;"}

<br>

{% endtab %}
{% tab Modal %}

모달은 장치 화면의 중앙에 나타나며, 배경의 앱과 구별되도록 도와주는 화면 오버레이가 있습니다. 이 메시지는 사용자가 세일이나 경품을 이용하도록 부드럽게 제안하는 데 완벽합니다.

\![모달 인앱 메시지가 앱과 웹사이트의 중앙에 대화 상자로 나타나는 모습. 모달에는 이미지, 헤더, 메시지 본문 및 두 개의 버튼이 포함됩니다.]({% image_buster /assets/img/modal-behavior.gif %}){: style="border:0px;"}

<br>

{% endtab %}
{% tab Fullscreen %}

전체 화면 메시지는 예상한 대로 장치의 전체 화면을 차지합니다! 이 메시지 유형은 필수 앱 업데이트와 같이 사용자의 주의를 정말로 필요로 할 때 좋습니다.

\![전체 화면 인앱 메시지가 앱 화면을 차지하는 모습. 전체 화면 메시지에는 큰 이미지, 헤더, 메시지 본문 및 두 개의 버튼이 포함됩니다.]({% image_buster /assets/img/full-screen-behavior.gif %}){: style="border:0px;"}

<br>

{% endtab %}
{% endtabs %}

이러한 기본 제공 메시지 템플릿 외에도 사용자 정의 HTML 인앱 메시지, CSS가 포함된 웹 모달 또는 웹 이메일 캡처 양식을 사용하여 메시지를 추가로 사용자 정의할 수 있습니다. 자세한 내용은 [사용자 정의]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/customize/)을 참조하십시오.

## 더 많은 리소스

자신만의 인앱 메시지 캠페인을 만들기 시작하기 전에—또는 다채널 캠페인에서 인앱 메시지를 사용할 때—[인앱 메시지 준비 가이드]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/best_practices/prep_guide/)를 확인하는 것을 강력히 권장합니다. 이 가이드는 인앱 메시지를 만들 때 고려해야 할 타겟팅, 콘텐츠 및 전환 질문을 다룹니다.

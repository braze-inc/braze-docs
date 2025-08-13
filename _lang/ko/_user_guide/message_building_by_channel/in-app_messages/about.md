---
nav_title: "인앱 메시지 정보"
article_title: 인앱 메시지 정보
page_order: 0
page_type: reference
description: "이 참고 문서에서는 인앱 메시지, 잠재적 사용 사례 및 표준 메시지 유형에 대한 간략한 개요를 제공합니다."
channel:
  - in-app messages
search_rank: 4.9
---

# [![Braze 학습 과정]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/messaging-channels-in-app-in-browser){: style="float:right;width:120px;border:0;" class="noimgborder"}인앱 메시지 정보

> 인앱 메시지는 여러모로 유용합니다. 이러한 메시지는 사용자의 앱 외부로 전달되지 않고 홈 화면을 방해하지 않기 때문에 콘텐츠가 풍부하고 긴박감이 낮습니다. 인앱 메시지는 앱 내에 존재하며(따라서 이름), 맥락과 함께 제공되며, 반갑지 않은 경우가 거의 없습니다! 사용자가 앱 내에서 활성화되어 있을 때 항상 전달됩니다.

To see examples of in-app messages, check out our [Case Studies](https://www.braze.com/customers).

## 잠재적 사용 사례

인앱 메시지에서 제공하는 풍부한 수준의 콘텐츠를 통해 이 채널을 다양한 사용 사례에 활용할 수 있습니다.

| 사용 사례 | 설명 |
| --- | --- |
| 푸시 프라이밍 | Run a [push priming]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/) campaign using a rich in-app message to show your customers the benefit of opting into push for your app or site, and present them with a prompt to grant push permission.
| 영업 및 프로모션 | 모달 인앱 메시지를 사용하여 정적 프로모션 코드 또는 오퍼가 포함된 시각적으로 매력적인 미디어로 고객을 맞이하세요. 그렇지 않았다면 구매나 전환을 하지 않았을 고객이 구매나 전환을 하도록 인센티브를 제공하세요. |
| 기능 채택 장려 | 고객이 앱의 다른 부분을 사용하거나 서비스를 이용하도록 유도하세요. |
| 고도로 개인화된 캠페인 | 고객이 앱이나 사이트에 들어왔을 때 가장 먼저 보게 되는 인앱 메시지를 배치하세요. Add in some Braze personalization features, such as [Connected Content]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/), to compel users to take action and therefore make your outreach more effective.
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

고려해야 할 다른 사용 사례는 다음과 같습니다:

- 새로운 앱 기능
- 앱 관리
- 리뷰
- 앱 업그레이드 또는 업데이트
- 경품 및 경품 행사

## 표준 메시지 유형

다음 탭은 사용자가 슬라이드업, 모달, 전체 화면 인앱 메시지 등 표준 인앱 메시지 유형 중 하나를 열었을 때 어떤 모습인지 보여줍니다.

{% tabs %}
{% tab 슬라이드업 %}

슬라이드업 메시지는 일반적으로 앱 화면의 상단과 하단에 표시됩니다(메시지를 작성할 때 설정할 수 있음). 새로운 서비스 약관, 쿠키 및 기타 정보 스니펫에 대해 사용자에게 알리는 데 유용합니다.

![앱 화면 하단에서 슬라이드업 인앱 메시지가 나타납니다. 슬라이드 업에는 아이콘 이미지와 간단한 메시지가 포함되어 있습니다.]({% image_buster /assets/img/slideup-behavior.gif %}){: style="border:0px;"}

<br>

{% endtab %}
{% tab 모달 %}

모달은 기기 화면 중앙에 화면 오버레이와 함께 표시되어 백그라운드에서 앱이 눈에 잘 띄도록 도와줍니다. 사용자에게 세일이나 경품 행사를 이용하도록 은근히 제안하는 데 적합합니다.

![앱과 웹사이트의 중앙에 대화 상자로 표시되는 모달 인앱 메시지. 모달에는 이미지, 헤더, 메시지 본문 및 두 개의 버튼이 포함됩니다.]({% image_buster /assets/img/modal-behavior.gif %}){: style="border:0px;"}

<br>

{% endtab %}
{% tab 전체 화면 %}

전체 화면 메시지는 기기의 전체 화면을 차지하는, 여러분이 기대하는 바로 그 메시지입니다! 이 메시지 유형은 필수 앱 업데이트와 같이 사용자의 주의가 정말 필요한 경우에 유용합니다.

![앱 화면을 가득 채우는 전체 화면 인앱 메시지. 전체 화면 메시지에는 큰 이미지, 헤더, 메시지 본문 및 두 개의 버튼이 포함됩니다.]({% image_buster /assets/img/full-screen-behavior.gif %}){: style="border:0px;"}

<br>

{% endtab %}
{% endtabs %}

이러한 기본 메시지 템플릿 외에도 커스텀 HTML 인앱 메시지, CSS가 포함된 웹 모달 또는 웹 이메일 캡처 양식을 사용하여 메시지를 추가로 사용자 지정할 수 있습니다. For more information, refer to [Customization]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/customize/).

## 추가 리소스

Before you get started with creating your own in-app message campaigns—or using in-app messages in a multi-channel campaign—we highly recommend that you check out our [In-app message prep guide]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/best_practices/prep_guide/). 이 가이드에서는 인앱 메시지를 작성할 때 고려해야 할 타겟팅, 콘텐츠 및 전환 관련 질문에 대해 설명합니다.



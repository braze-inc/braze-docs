---
nav_title: 사용자 지정 키워드 처리
article_title: 사용자 지정 키워드 처리
page_order: 3
description: "이 참고 문서에서는 Braze가 양방향 SMS 메시징 및 자동 응답을 처리하는 방법에 대해 설명합니다. 여기에는 키워드 트리거링 작동 방식과 사용자 지정 키워드 카테고리 및 다국어 지원에 대한 설명이 포함됩니다."
page_type: reference
channel:
  - SMS

---

# 사용자 지정 키워드 처리

> 이 참고 문서에서는 Braze가 양방향 SMS 메시징 및 자동 응답을 처리하는 방법에 대해 설명합니다. 여기에는 키워드 트리거링 작동 방식과 사용자 지정 키워드 카테고리 및 다국어 지원에 대한 설명이 포함됩니다.

## 양방향 메시징(사용자 지정 키워드 응답)

양방향 메시징을 사용하면 메시지를 보내고 해당 메시지에 대한 응답을 처리할 수 있습니다. 최종 사용자가 Braze에 키워드를 보내면 해당 사용자가 자동 응답을 받게 됩니다. 양방향 메시징을 올바르게 적용하면 고객 마케팅에 간단하고 즉각적이며 역동적인 솔루션이 되어 시간과 리소스를 절약할 수 있습니다.

## 키워드 및 자동 응답 관리

Braze가 포함된 SMS는 키워드 트리거, 커스텀 응답, 여러 언어에 대한 키워드 세트 정의, 커스텀 키워드 카테고리 설정 등의 옵션을 제공합니다. 

{% tabs %}
{% tab 키워드 트리거 추가 %}

#### 키워드 트리거 추가

기본 옵트인 및 옵트아웃 키워드 외에도 옵트인, 옵트아웃 및 도움말 응답을 트리거하는 고유한 키워드를 정의할 수도 있습니다.

나만의 키워드를 정의하려면 다음과 같이 하세요:

1. Braze 대시보드에서 **오디언스** > **구독 그룹으로** 이동하여 SMS 구독 그룹을 선택합니다.<br><br>
2. **SMS 전역 키워드**에서 키워드를 추가하려는 키워드 카테고리 옆의 연필 아이콘을 클릭합니다. ![]({% image_buster /assets/img/sms/sms_keywords.png %})<br><br>
3. 탭이 열리면 이 키워드 카테고리를 트리거할 키워드를 추가합니다. 키워드는 대소문자를 구분하지 않으며 `START`, `YES`, `UNSTOP`과 같은 범용 키워드는 변경할 수 없습니다. !['옵트인' 카테고리의 키워드 수정하기. 추가된 키워드는 "START", "UNSTOP", "YES"입니다. 답장 메시지 필드에 "이 번호의 메시지 수신이 취소되었습니다. 도움을 요청하려면 HELP을 입력합니다. 구독 취소하려면 STOP을 입력합니다. 메시지 및 데이터 요금이 적용될 수 있습니다."]({% image_buster /assets/img/sms/keyword_edit2.png %})

키워드 및 키워드 응답에는 다음 규칙이 적용됩니다:

| 키워드 | 키워드 응답 |
| -------- | ----------------- |
| \- 유효한 UTF-8 인코딩 문자<br>\- 카테고리당 최대 20개의 키워드 총합<br>\- 최대 34자 길이<br>\- 최소 1자 길이 <br>\- 공백을 포함할 수 없습니다.<br>\- 구독 그룹 전체에서 대소문자를 구분하지 않고 고유해야 합니다. | \- 비워 둘 수 없습니다.<br>\- 최대 300자 길이<br>\- 유효한 UTF-8 문자 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert tip %}
캠페인과 캔버스에서 이러한 키워드를 사용하여 메시지를 리타겟팅하고 트리거하는 방법에 대해 알고 싶으신가요? 자세한 내용은 [SMS 리타겟팅]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/retargeting/) 문서를 참조하세요.
{% endalert %}
{% endtab %}

{% tab 응답 관리 %}

#### 응답 관리

사용자가 특정 키워드 카테고리에 키워드를 입력한 후 사용자에게 전송되는 응답을 직접 관리할 수 있습니다.

1. Braze 대시보드에서 **오디언스** > **구독 그룹으로** 이동하여 SMS 구독 그룹을 선택합니다. <br><br>
2. **SMS 전역키워드**에서 연필 아이콘을 선택하여 응답을 수정할 키워드 카테고리를 선택합니다. ![]({% image_buster /assets/img/sms/sms_keywords.png %})<br><br> 
3. 탭이 열리면 응답을 편집합니다. 응답을 작성할 때 [규정 준수를 위한 6가지 규칙을]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_laws_and_regulations/#the-six-rules-to-get-compliance-right) 염두에 두고 키워드 및 키워드 응답에 적용되는 다음 규칙을 읽어보세요. ![응답]({% image_buster /assets/img/sms/keyword_home.png %})<br><br>
4. 응답에서 정적 URL을 자동으로 줄이려면 **링크 단축** 토글을 선택합니다. 문자 카운터가 업데이트되어 단축 URL의 예상 길이를 표시합니다. !['링크 단축' 토글이 켜져 있을 때 문자 카운터가 업데이트되는 모습을 보여주는 GIF입니다.]({% image_buster /assets/img/sms/link_shortening.gif %}){: style="max-width:50%;"}

##### 고려 사항

| 키워드 | 키워드 응답 |
| -------- | ----------------- |
| \- 유효한 UTF-8 인코딩 문자<br>\- 카테고리당 최대 20개의 키워드 총합<br>\- 최대 34자 길이<br>\- 최소 1자 길이 <br>\- 공백을 포함할 수 없습니다.<br>\- 구독 그룹 전체에서 대소문자를 구분하지 않고 고유해야 합니다. | \- 비워 둘 수 없습니다.<br>\- 최대 300자 길이<br>\- 유효한 UTF-8 문자 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% endtabs %}

{% alert tip %}
액션 기반 캔버스가 인바운드 SMS 메시지에 의해 트리거되는 경우 캔버스의 첫 번째 [메시지 단계]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/)에서 SMS 속성을 참조할 수 있습니다.
{% endalert %}

## 다국어 지원

특정 국가로 보내는 경우 발신자는 인바운드 키워드와 아웃바운드 답장을 현지 언어로 지원해야 할 수 있습니다. 이를 지원하기 위해 Braze에서는 언어별 키워드 설정을 만들 수 있습니다.
![][16]{: style="float:right;max-width:40%;margin-left:10px;"}

### 언어별 키워드 만들기

**언어 추가**를 클릭하고 대상 언어를 선택하거나 드롭다운에서 언어를 검색합니다.

{% alert important %}
다른 언어에는 영어와 같은 사전 설정 키워드 및 응답이 제공되지 않으므로 발신자는 마케팅 및 법무팀과 협력하여 이 세트에 필요한 키워드를 추가해야 합니다. 그렇지 않으면 Braze는 해당 언어에 대해 현지화된 수신 메시지를 처리하지 않습니다.
{% endalert %}

언어를 삭제해야 하는 경우 오른쪽 하단의 **언어 삭제** 버튼을 클릭합니다.

!["프랑스어" 탭이 선택된 SMS 글로벌 키워드 페이지로 이동합니다. 추가된 각 언어에 대한 추가 탭이 있습니다.][5]

## 사용자 지정 키워드 카테고리

세 가지 기본 키워드 카테고리(옵트인, 옵트아웃, 도움말) 외에 최대 25개의 고유한 키워드 카테고리를 만들 수도 있습니다. 이를 통해 임의의 키워드를 식별하고 비즈니스에 맞는 응답을 설정할 수 있습니다. 예를 들어 "프로모션" 또는 "할인"이라는 카테고리를 사용하면 이번 달에 진행되는 프로모션에 대한 응답을 표시할 수 있습니다. 

이러한 사용자 지정 키워드는 '상시 작동' 방식으로 작동하므로 메시지 서비스에 가입한 모든 사용자가 언제든 키워드로 문자를 보내고 응답을 받을 수 있습니다. 이 동작 외에도 사용자 생애주기의 [특정 시점]({{site.baseurl}}/user_guide/message_building_by_channel/sms/keywords/keyword_handling/#lifecycle-specific-keywords)에만 보낼 수 있는 특정 키워드를 정의할 수 있는 옵션도 있습니다. 

!["더블옵틴" 카테고리에 대한 키워드. 사용자가 "Y"라는 문자를 보내면 "헤어 커터 SMS 등록을 확인해주셔서 감사합니다."라는 메시지가 표시됩니다.][12]

### 사용자 지정 카테고리 만들기

사용자 지정 키워드 카테고리를 만들려면 다음과 같이 하세요:

1. 적절한 구독 그룹을 편집합니다.
2. **커스텀 키워드 추가**를 클릭합니다. ![][13]{: style="max-width:90%;"}
3. 키워드 카테고리 이름을 입력하고 사용자가 답장 메시지를 받기 위해 문자로 입력할 수 있는 키워드를 정의합니다.

이 키워드 카테고리가 생성되면 캠페인과 캔버스에서 [필터링하고 트리거할]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/retargeting/) 수 있습니다.

맞춤 키워드 카테고리에서 생성된 키워드는 새 키워드 생성을 위한 모든 규칙과 유효성 검사를 준수합니다. 

### 라이프사이클별 키워드

고객이 생애주기 동안 특정 키워드를 보내 응답을 받을 수 있는 시기(예: 첫 번째 초기 온보딩 시)를 제한하려는 사용 사례가 있는 경우, 캠페인 또는 캔버스에서 **키워드 카테고리 기타 내의 구독 그룹으로 인바운드 SMS 보내기** 트리거를 사용하여 사용자가 특정 시점에 보낼 수 있는 키워드를 정의할 수 있습니다.

이 트리거는 메시지의 일치 여부 비교를 사용하여 특정 인바운드 메시지에 대한 필터링을 지원하고 정규식 규칙과 일치하거나 일치하지 않음을 비교하여 사용자 입력의 유효성을 검사합니다.

#### 캔버스

![트리거가 있는 액션 기반 캔버스 단계는 메시지 본문이 정규표현식 "캐럿 기호 건너뛰기"와 일치하는 키워드 카테고리 "기타" 내의 구독 그룹 "메시징 서비스"로 인바운드 SMS 보내기입니다.][14]{: style="max-width:90%;"}

#### 캠페인

![트리거가 있는 액션 기반 캠페인 메시지 본문이 "키워드1"이거나 "키워드2"이거나 "키워드 A"가 아닌 키워드 카테고리 "기타" 내의 구독 그룹 "마케팅 메시지 서비스 A"로 인바운드 SMS 보내기입니다.][15]{: style="max-width:90%;"}

### 알 수 없는 키워드 처리

필수는 아니지만 사용자가 기존 키워드와 일치하지 않는 인바운드 SMS 키워드를 보낼 때 자동 응답을 설정하는 것을 적극 권장합니다. 이 메시지는 사용자에게 키워드가 인식되지 않는다는 사실을 알리고 몇 가지 안내를 제공합니다. 

"죄송합니다!"와 같은 메시지가 포함된 SMS 캠페인을 생성하여 이를 수행할 수 있습니다. 그 키워드를 인식하지 못했고, 중단하려면 STOP, 도와주려면 HELP라는 문자를 보냈습니다." 다음으로, 전달 단계에서 **실행 기반 전달**을 선택하고 **키워드 카테고리 기타 내에서 구독 그룹으로 인바운드 SMS 보내기** 트리거를 사용합니다.

![]({% image_buster /assets/img/sms/sms_other.png %})

{% alert tip %}
이러한 키워드와 키워드 카테고리를 캠페인과 캔버스에서 어떻게 사용하여 메시지를 리타겟팅하고 트리거할 수 있는지 알고 싶으신가요? 자세한 내용은 [SMS 리타겟팅]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/retargeting/) 문서를 참조하세요.
{% endalert %}

[oblink]: {{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_subscription_group/#setup-process
[1]: {% image_buster /assets/img/sms/keyword_edit2.png %}
[2]: {% image_buster /assets/img/sms/keyword_home.png %}
[unknown]: {{site.baseurl}}/user_guide/message_building_by_channel/sms/keywords/unknown_phone_numbers/
[endpoint]: {{site.baseurl}}/api/endpoints/user_data/post_user_alias/
[IMAGE2]: {% image_buster /assets/img/sms/sms_message_body.png %}
[5]: {% image_buster /assets/img/sms/multi-language2.png %}
[12]: {% image_buster /assets/img/sms/sms_custom_keyword.png %}
[13]: {% image_buster /assets/img/sms/sms_custom_step.png %}
[14]: {% image_buster /assets/img/sms/canvas_trigger.png %}
[15]: {% image_buster /assets/img/sms/campaign_trigger.png %}
[16]: {% image_buster /assets/img/sms/multi-language.png %}

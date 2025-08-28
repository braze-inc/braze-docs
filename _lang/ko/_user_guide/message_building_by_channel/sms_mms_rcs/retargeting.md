---
nav_title: 사용자 리타겟팅
article_title: 사용자 리타겟팅
description: "이 참조 문서에서는 사용자의 SMS 및 RCS 상호 작용을 통해 메시지를 리타겟팅하는 방법에 대해 설명합니다."
page_type: reference
page_order: 4
alias: /sms_mms_rcs_user_retargeting/
tool:
  - Campaigns
channel:
  - SMS
  - MMS
  - RCS

---

# 사용자 리타겟팅

> 사용자의 가입 상태를 변경하고 수신 키워드를 기반으로 자동 응답을 보내는 것 외에도, Braze는 메시지를 필터링하고 트리거하기 위해 사용자 프로필에 상호 작용을 기록합니다.<br><br>이러한 필터 및 트리거를 사용하면 SMS, MMS 및 RCS 캠페인을 전송했거나 이에 응답한 사용자를 기준으로 작업을 필터링하거나 단축 URL을 클릭한 사용자와의 추가 참여를 유도할 수 있습니다.

{% alert tip %}
맞춤 키워드와 이러한 리타겟팅 옵션을 활용하기 위해 양방향 메시지를 설정하는 방법에 대해 자세히 알아보려면 [맞춤 키워드]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/keywords/keyword_handling/) 도움말 문서를 참조하세요.
{% endalert %}  

## 리타겟팅 옵션

{% alert note %}
사용자 리타겟팅으로 오디언스를 구축할 때, 선호도에 따라 특정 사용자를 포함하거나 제외할 수 있으며, CUP에 따른 '판매 또는 공유 금지' 권한과 같은 개인정보 보호법을 준수하기 위해 특정 사용자를 포함하거나 제외할 수 있습니다. 마케팅 담당자는 캔버스 및/또는 캠페인 참여 기준 내에서 사용자의 자격에 맞는 관련 필터를 구현해야 합니다.
{% endalert %}

### SMS, MMS, RCS로 사용자 필터링하기

사용자를 마지막으로 수신한 시간 또는 특정 캠페인에서 SMS, MMS 또는 RCS를 수신했는지 여부에 따라 필터링할 수 있습니다. 필터는 캠페인 빌더의 **타겟 오디언스** 단계에서 설정할 수 있습니다. 

**마지막 수신 기준으로 필터링 SMS/MMS/RCS**<br>
![세분화 필터 2020년 12월 8일 이후 마지막으로 수신한 SMS]({% image_buster /assets/img/sms/filter2.png %})

**SMS/MMS/RCS 캠페인에서 받은 메시지로 필터링**<br>
특정 캠페인에서 메시지를 받은 사용자를 필터링합니다. 이 필터를 사용하면 캠페인에서 메시지를 받지 않은 사람들을 필터링하는 옵션도 있습니다. <br>
![세분화 필터 "SMS 리타겟팅" 캠페인에서 메시지를 받았습니다.]({% image_buster /assets/img/sms/filter1.png %})

### 사용자가 SMS, MMS 또는 RCS를 수신하면 메시지 트리거 {#trigger-messages}

사용자가 특정 캠페인에서 SMS, MMS 또는 RCS 메시지를 수신할 때 메시지를 트리거하려면 액션 기반 캠페인의 트리거 작업으로 **캠페인과 상호 작용을** 선택합니다. 다음으로 **SMS 수신을** 선택하고 사용하려는 SMS, MMS 또는 RCS 캠페인을 선택합니다.

![]({% image_buster /assets/img/sms/trigger.png %})

### 고급 추적 링크로 필터링

[고급 추적 링크]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/link_shortening/)를 사용하여 캠페인을 클릭한 사용자를 리타겟팅하세요.
고급 추적이 활성화된 캠페인만 다음 드롭다운에 표시됩니다:

**특정 SMS, MMS 또는 RCS 캠페인을 클릭한 사용자를 리타겟팅합니다.**
1. **클릭/열기 캠페인** 필터를 사용하여 세그먼트를 생성합니다.
2. **단축된 SMS 링크를 클릭합니다**.
3. 원하는 캠페인을 선택합니다.

![]({% image_buster /assets/img/sms/retargeting5.png %})

**특정 캔버스 단계를 클릭한 사용자를 리타겟팅합니다.**
1. **클릭/열기 단계** 필터를 사용하여 세그먼트를 만듭니다.
2. **단축된 SMS 링크를 클릭합니다**.
3. 원하는 캔버스 및 캔버스 단계를 선택합니다.

![]({% image_buster /assets/img/keyword_example1.jpg %})

## 키워드 카테고리별 리타겟팅

세 가지 기본 키워드 카테고리(옵트인, 옵트아웃, 도움말) 외에도 최대 25개의 자체 키워드 카테고리를 생성하여 임의의 키워드와 응답을 식별할 수 있습니다. 이러한 카테고리는 필터링 및 리타겟팅에 사용할 수 있습니다. 글로벌 키워드 카테고리 및 설정 방법에 대한 자세한 내용은 [키워드 처리를]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/keywords/) 참조하세요. 

### 최근 기준으로 필터링

SMS, MMS 또는 RCS 프로그램에 응답한 사용자의 최근 기록을 필터링합니다. 이 필터는 사용자가 키워드 카테고리 중 하나에 속하는 인바운드 메시지를 보낸 마지막 날짜를 평가합니다. 

![세분화 필터 2020년 8월 11일 이후 '옵트인' 키워드를 사용하여 '마케팅 SMS' 구독 그룹에 마지막으로 전송된 SMS]({% image_buster /assets/img/sms/retargeting1.png %})

### 캠페인 또는 캔버스 어트리뷰션으로 필터링

특정 SMS, MMS 또는 RCS 캠페인이나 Canvas 구성 요소, 키워드 카테고리 또는 태그에 답글을 단 사용자를 필터링합니다.

**키워드 카테고리로 특정 캠페인에 대한 답글을 기준으로 필터링하기**<br>
![캠페인 "SMS-283" "프로모션"에 대해 "SMS에 답장함" 필터가 있는 캠페인. 필터 아래에 "이 필터는 활성 캠페인에서 사용되지 않는 경우 '프로모션'에서 마지막 메시지를 보낸 후 25개월 후에 만료됩니다."]({% image_buster /assets/img/sms/clicked_opened_campaign.png %})

**특정 태그가 있는 캠페인 또는 캔버스에 댓글을 단 사람으로 필터링하기**
![캠페인에 "SMS에 답장함" 필터가 있는 캠페인 또는 "커브사이드 메시징 서비스 C" 태그가 있는 캔버스.]({% image_buster /assets/img/sms/clicked_opened_campaign_canvas_tag.png %})

**특정 단계에 대한 답글을 기준으로 필터링하기**
!["SMS 더블 옵트" "단계 - 도움말" 단계에 대해 "SMS에 답장했습니다" 필터가 있는 캠페인]({% image_buster /assets/img/sms/clicked_opened_step.png %})

### 키워드별 메시지 트리거

사용자가 키워드 카테고리(사용자가 키워드 중 하나를 보낸 경우) 또는 기타 키워드(사용자가 기존 카테고리 중 하나에 속하지 않는 키워드를 보낸 경우)에 따라 메시지를 인바운드 전송할 때 메시지가 트리거될 수 있습니다. 이러한 트리거는 캠페인 빌더의 전달 단계에서 설정할 수 있습니다.

인바운드 메시지가 정의된 트리거 이벤트를 충족하는지 평가할 때 평가를 시작하기 전에 선행 및 후행 공백이 제거됩니다.

{% alert tip %}
액션 기반 캔버스가 인바운드 SMS 또는 MMS 메시지에 의해 트리거되는 경우, 다음 액션 경로까지 모든 캔버스 단계에서 [지원되는 SMS 리퀴드 속성을]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/) 참조할 수 있습니다.
{% endalert %}

**인바운드 키워드 카테고리별 트리거**<br>
![세분화 필터를 사용한 액션 기반 SMS 캠페인 "옵트인" 키워드를 구독 그룹 "마케팅 SMS"로 전송]({% image_buster /assets/img/sms/retargeting2.png %}){: style="margin-top:10px;"}

**임의의 키워드로 트리거**<br>
'기타' 키워드 응답에 대한 메시지를 트리거할 때는 정확한 텍스트 일치 여부에 따라 키워드 본문을 평가할 수 있다는 점에 유의하세요. 이 경기는 앞서 설명한 것과 동일한 규칙을 따릅니다: **정확한 한 단어 메시지만** 처리됩니다(대소문자 _구분 없음_). `Hello Braze!` 키워드로 전송된 키워드는 다음 예제에 표시된 기준과 일치하지 않습니다.
![메시지 본문이 정확히 "Hello" 또는 "Hey"인 키워드 카테고리가 "기타"인 액션 기반 SMS 캠페인.]({% image_buster /assets/img/sms/retargeting3.png %}){: style="margin-top:10px;"}

**템플릿 키워드**<br>
인바운드 SMS 또는 MMS에서 캠페인 또는 캔버스 구성요소를 트리거할 때, 사용자가 Liquid를 사용하여 캠페인 또는 캔버스 본문으로 보낸 텍스트 또는 미디어 첨부파일을 선택적으로 템플릿으로 만들 수 있습니다. 이렇게 하면 사용자의 응답에 액세스하여 답장에 포함하거나 조건부 논리를 적용하는 등 Liquid로 할 수 있는 모든 작업을 수행할 수 있습니다. 

{% raw %}

```liquid
Sorry, we didn't recognize {{sms.${inbound_message_body}}}. Text HELP for help or STOP to stop.
```

```liquid
{% if {{sms.${inbound_message_body}}} == "SNEAKERS" %}
OK, you're subscribed to updates on all our sneaker deals!
{% elsif {{sms.${inbound_message_body}}} == "SHIRTS" %}
Shirt deals coming up for you!
{% else %}
Want to receive a specific deal? Just text us the category you're interested in. For example SHIRTS or SNEAKERS.
{% endif %}
```

{% endraw %}

[16]: {% image_buster /assets/img/keyword_example1.jpg %}
[16]: {% image_buster /assets/img/sms/retargeting4.png %}

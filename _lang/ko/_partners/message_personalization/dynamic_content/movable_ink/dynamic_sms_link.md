---
nav_title: 동적 SMS 링크 미리보기
article_title: 동적 SMS 링크 미리보기
description: "이 참조 문서에서는 Movable Ink의 SMS 링크 미리보기 기능을 켜고 사용하는 방법을 간략히 설명합니다."
page_type: partner
search_tag: Partner
---

# 동적 SMS 링크 미리보기

> Movable Ink의 동적 SMS 링크 미리보기 기능을 사용하면 동일한 SMS 비용으로 MMS의 몰입감을 활용할 수 있습니다. 이를 통해 Braze 및 Movable Ink를 사용하여 비용 효율적이고 개인화된 리치 메시징 경험을 전달할 수 있습니다.

## 필수 조건

| 요구 사항 | 설명 |
| --- | --- |
| Movable Ink 계정 | 이 파트너십을 활용하려면 Movable Ink 계정이 필요합니다. |
| 데이터 소스 | Movable Ink에 데이터 소스를 연결해야 합니다. 이는 CSV, 웹사이트 가져오기 또는 API를 통해 수행할 수 있습니다. |
| MMS 전송 기능 | MMS를 통해 Braze에 설정되었는지 확인하십시오.
| [링크 단축]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/link_shortening/) | 링크 단축이 켜져 있는지 확인하세요. | 
| 연락처 카드 | 링크 미리보기가 iOS에서 작동하려면 사용자의 전화에 연락처로 브랜드(발신자)를 저장해야 합니다. 연락처 카드나 다른 방법도 가능합니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 통합

아래의 각 단계를 따라 iOS 및 Android 운영 체제에 대한 동적 SMS 링크를 전송합니다.

### iOS

{% alert important %}
iOS에서 링크 미리보기 이미지를 허용하려면 사용자가 귀하의 브랜드(발신자)를 연락처로 추가해야 합니다.
{% endalert %}

#### 1단계: 연락처 카드 캠페인 만들기

사용자가 [연락처 카드]({{site.baseurl}}/user_guide/message_building_by_channel/sms/mms/contact_card/) 또는 다른 방법을 통해 브랜드를 연락처로 저장하면 **탭하여 로드 미리보기** 프롬프트와 이동 가능한 잉크 링크를 볼 수 있습니다.

![1]{: style="max-width:30%;"}

#### 2단계: Movable Ink 링크 보내기

1. Movable Ink에서 SMS 캠페인을 생성하고 클릭 유도 URL을 생성하세요.
2. Braze 대시보드에서 **캠페인**으로 이동하여 **캠페인 생성** 드롭다운에서 새로운 SMS/MMS 캠페인을 설정합니다.
3. SMS 캠페인 작성기에서:
    - 구독 그룹을 설정하세요.
    - 메시지를 입력하세요.
    - 메시지 본문에 있는 다른 모든 텍스트 뒤에 **last** Movable Ink 링크를 추가합니다. <br><br>![2]{: style="max-width:50%;"}

{% alert tip %}
[Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/using_liquid/) 개인화를 다시 확인해 보세요.  
{% endalert %}

{: start="4"}
4\. 모든 준비가 완료되어 동적 SMS 링크 미리보기 캠페인을 테스트하고 시작할 수 있습니다.

![3]{: style="max-width:70%;"}

사용자가 링크 미리보기를 로드한 후, 개인화된 이미지가 렌더링되어 웹사이트, 앱 또는 랜딩 페이지로 연결할 수 있습니다.

![4]{: style="max-width:30%;"}

### Android(Google 및 삼성 디바이스)

Android 사용자는 동적 SMS 링크 미리보기를 받기 위해 귀하의 브랜드를 연락처로 저장할 필요가 없습니다. 그러나 기기가 링크 미리보기를 자동으로 로드할 수 있도록 여전히 권장됩니다.

![5]{: style="max-width:30%;"}

브랜드를 연락처로 저장하지 않았고 자동 미리 보기를 사용 설정한 사용자는 미리 보기 이미지를 로드하려면 **탭하여 미리 보기를 로드하기를** 선택해야 합니다.

![6]{: style="max-width:30%;"}

## 고려사항

- 메시지에 미리보기 링크를 하나만 포함하세요. SMS 본문에 여러 링크가 포함된 콘텐츠는 생성되지 않습니다. 
- 미리보기 링크 뒤에 문자를 포함하지 마세요. 그렇지 않으면 경험이 중단될 수 있습니다.


[1]: {% image_buster /assets/img/movable_ink/ios_link.png %}
[2]: {% image_buster /assets/img/movable_ink/ios_message.png %}
[3]: {% image_buster /assets/img/movable_ink/ios_test_launch.png %}
[4]: {% image_buster /assets/img/movable_ink/ios_example.png %}
[5]: {% image_buster /assets/img/movable_ink/android_automatic.png %}
[6]: {% image_buster /assets/img/movable_ink/android_tap.png %}

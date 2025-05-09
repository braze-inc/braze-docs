---
nav_title: SMS 및 WhatsApp 가입 양식
article_title: SMS 및 WhatsApp 가입 양식
alias: "/phone_number_capture/"
page_order: 1
description: "이 페이지에서는 앱 내 메시지 끌어서 놓기 편집기를 사용하여 SMS 및 WhatsApp 가입 양식을 만드는 방법에 대해 설명합니다."
---

# SMS 및 WhatsApp 가입 양식

> SMS 및 WhatsApp 가입 양식은 인앱 메시지용 드래그 앤 드롭 편집기에서 사용할 수 있는 템플릿입니다. 이 템플릿을 사용하여 사용자의 전화번호를 수집하고 SMS 및 WhatsApp 구독 그룹을 성장시키세요.

![전화 가입 양식 템플릿을 사용하여 생성된 인앱 메시지의 세 가지 예][img7]

{% multi_lang_include drag_and_drop/templates.md section='SDK 요구 사항' %}

## 전화번호 가입 양식 만들기

### 1단계: 템플릿 선택

드래그 앤 드롭 인앱 메시지를 만들 때 템플릿에 대해 **SMS 가입** 또는 **WhatsApp 가입을** 선택한 다음 **메시지 작성을** 선택합니다. 이 템플릿은 모바일 앱과 웹 브라우저 모두에서 지원됩니다.

![SMS 가입 또는 WhatsApp 가입을 선택하는 모달을 인앱 메시지를 만들 때 템플릿으로 사용합니다.][img2]{: style="max-width:70%"}

### 2단계: 메시지 스타일을 설정하세요

{% multi_lang_include drag_and_drop/templates.md section='메시지 스타일' %}

![커스텀 폰트 업로드 및 선택 워크플로우.][img6]

### 3단계: 전화번호 입력 구성 요소 사용자 지정

시작하려면 가입 양식을 작성하고 편집기에서 전화번호 입력 구성 요소를 선택하세요.

![전화번호 입력 구성 요소가 선택된 가입 양식 생성 시 미리보기 영역.][img3]{: style="max-width:40%"}

사이드 메뉴에서 이 템플릿이 전화번호를 수집할 구독 그룹을 지정합니다. 준수 모범 사례를 따르기 위해 전화번호 가입 양식당 하나의 구독 그룹에 대한 동의만 수집할 수 있습니다. 그러나 원할 경우 다른 구독 그룹에 대한 동의를 얻기 위해 여러 양식을 사용할 수 있습니다.

![구독 그룹 드롭다운에 구독 그룹이 선택되었습니다.][img4]{: style="max-width:40%"}

기본값으로, 우리는 전 세계적으로 숫자를 수집하지만, 숫자를 수집할 국가의 수를 제한할 수 있습니다. 이것은 특정 국가의 전화번호를 가진 사용자에게만 메시지를 보내려는 경우에 유용하며, 목록 청결을 도울 수 있습니다. 이를 위해 **모든 국가에서 숫자 수집**을 끄고 드롭다운을 사용하여 특정 국가를 선택하십시오. 사용자는 명시적으로 추가한 국가만 선택할 수 있습니다.

![국가 드롭다운에서 번호를 수집하려는 국가를 선택합니다.][img5]{: style="max-width:40%"}

#### 유효하지 않은 전화번호

사용자가 허용되지 않는 특수 문자가 포함된 전화번호를 입력하면 사용자에게 사용자 지정할 수 없는 일반 오류 표시기가 표시되며 양식을 제출할 수 없습니다. **미리보기 및 테스트** 탭과 테스트 기기에서 오류 동작을 확인할 수 있습니다. 이 문서를 참조하여 [Braze가 전화번호를 형식화하는 방법][2]을 배우십시오.

### 4단계: 면책 조항 언어 추가 (SMS 가입 양식용)

SMS 가입 양식의 경우, 발송할 SMS 유형을 명확하게 전달하는 것이 중요합니다. 양식에 다음 정보를 포함하여 목록 성장이 준수되도록 하세요.

- 고객이 받을 수 있는 SMS 메시지 유형에 대한 설명(장바구니 알림, 프로모션 및 거래, 약속 알림 등). 모든 사용 사례를 나열할 필요는 없지만 브랜드가 보낼 메시지 유형에 대한 설명을 제공해야 합니다.
- 동의는 구매의 조건이 아님을 유의하십시오(해당되는 경우).
- 메시지 빈도 및 메시지 및 데이터 요금이 적용된다는 알림입니다. 정확한 메시지 빈도를 모를 경우, 빈도가 다를 수 있다고 말할 수 있습니다.
- 귀하의 이용 약관 및 SMS 개인정보 보호정책에 대한 링크.
- 도움말 및 수신 거부 키워드 알림 (도움말은 HELP; 취소는 STOP).

저희는 템플릿에 입력 안내 면책 조항을 예시로 제공했을 뿐이며, 이는 법률 자문을 구성하지 않으며 준수 목적으로 의존해서는 안 됩니다. 귀하의 특정 브랜드에 맞춘 언어를 개발하기 위해 법률 팀과 협력하는 것이 중요합니다.

{% alert note %}
이 설명서는 법률 자문을 제공하기 위한 것이 아니며, 법률 자문으로 전적으로 의존할 수 없습니다.
{% endalert %}

SMS 준수에 대한 자세한 내용은 [SMS 법률 및 규정][4]을 참조하십시오.

### 5단계: 메시지를 스타일링하세요

드래그 앤 드롭 [인앱 메시지 구성요소를][3] 사용하여 메시지의 모양과 느낌을 사용자 지정하세요.

## 결과 분석

{% multi_lang_include drag_and_drop/templates.md section='reporting' %}

![인앱 메시지 성능/성과 패널은 인앱 메시지의 각 링크에 대한 클릭 수를 보여줍니다.][img8]

[2]: {{site.baseurl}}/user_guide/message_building_by_channel/sms/phone_numbers/user_phone_numbers/#importing-phone-numbers
[3]: {{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/style_settings/#message-components
[4]: {{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_laws_and_regulations/

[img1]: {% image_buster /assets/img_archive/dnd_iam_phone_capture_example.png %}
[img2]: {% image_buster /assets/img_archive/dnd_iam_phone_capture_template.png %}
[img3]: {% image_buster /assets/img_archive/dnd_iam_phone_capture_select.png %}
[img4]: {% image_buster /assets/img_archive/dnd_iam_phone_capture_subscription.png %}
[img5]: {% image_buster /assets/img_archive/dnd_iam_phone_capture_countries.png %}
[img6]: {% image_buster /assets/img_archive/dnd_iam_phone_capture_custom_font.gif %}
[img7]: {% image_buster /assets/img_archive/dnd_iam_phone_capture_example2.png %}
[img8]: {% image_buster /assets/img_archive/dnd_iam_phone_capture_analytics.png %}

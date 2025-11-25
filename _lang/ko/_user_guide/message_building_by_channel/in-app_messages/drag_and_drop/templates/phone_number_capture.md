---
nav_title: "SMS, RCS 및 WhatsApp 가입 양식"
article_title: "SMS, RCS 및 WhatsApp 가입 양식"
alias: "/phone_number_capture/"
page_order: 1
description: "이 페이지에서는 인앱 메시지 드래그 앤 드롭 편집기를 사용하여 SMS, RCS 및 WhatsApp 가입 양식을 만드는 방법을 다룹니다."
---

# SMS, RCS 및 WhatsApp 가입 양식

> SMS, RCS 및 WhatsApp 가입 양식은 인앱 메시지용 드래그 앤 드롭 편집기에서 사용할 수 있는 템플릿입니다. 이 템플릿을 사용하여 사용자의 전화번호를 수집하고 SMS, MMS, RCS 및 WhatsApp 구독 그룹을 성장시키세요.

\![전화 가입 양식 템플릿을 사용하여 생성된 인앱 메시지의 세 가지 예.]({% image_buster /assets/img_archive/dnd_iam_phone_capture_example2.png %})

{% multi_lang_include drag_and_drop/templates.md section='SDK requirements' %}

## 전화번호 가입 양식 만들기

### 1단계: 템플릿 선택

드래그 앤 드롭 인앱 메시지를 만들 때 **SMS 가입** (이것은 RCS 가입을 수용합니다) 또는 **WhatsApp 가입**을 템플릿으로 선택한 다음 **메시지 작성**을 선택하세요. 이 템플릿은 모바일 앱과 웹 브라우저 모두에서 지원됩니다.

\![인앱 메시지를 만들 때 SMS 가입 또는 WhatsApp 가입을 템플릿으로 선택하는 모달.]({% image_buster /assets/img_archive/dnd_iam_phone_capture_template.png %}){: style="max-width:80%"}

### 2단계: 메시지 스타일 설정

{% multi_lang_include drag_and_drop/templates.md section='message style' %}

\![사용자 정의 글꼴을 업로드하고 선택하는 워크플로우.]({% image_buster /assets/img_archive/dnd_iam_phone_capture_custom_font.gif %})

### 3단계: 전화번호 입력 구성 요소 사용자 정의

가입 양식을 만들기 시작하려면 편집기에서 전화번호 입력 구성 요소를 선택하세요.

\![전화번호 입력 구성 요소가 선택된 가입 양식을 만들 때의 미리보기 영역.]({% image_buster /assets/img_archive/dnd_iam_phone_capture_select.png %}){: style="max-width:80%"}

측면 메뉴에서 이 템플릿이 전화번호를 수집할 구독 그룹을 지정하십시오. 준수 모범 사례를 준수하기 위해, 전화번호 가입 양식당 하나의 구독 그룹에 대한 동의만 수집할 수 있습니다. 그러나 원하신다면, 다른 구독 그룹에 대한 동의를 수집하기 위해 여러 양식을 사용할 수 있습니다.

\![구독 그룹이 선택된 구독 그룹 드롭다운.]({% image_buster /assets/img_archive/dnd_iam_phone_capture_subscription.png %}){: style="max-width:40%"}

기본적으로 우리는 전 세계적으로 번호를 수집하지만, 번호를 수집할 국가 수를 제한할 수 있습니다. 이는 특정 국가에 전화번호가 있는 사용자에게만 메시지를 보내려는 경우에 유용하며, 목록의 청결성을 유지하는 데 도움이 될 수 있습니다. 이를 위해 **모든 국가에서 번호 수집**을 끄고 드롭다운을 사용하여 특정 국가를 선택하십시오. 사용자는 명시적으로 추가한 국가만 선택할 수 있습니다.

\![번호를 수집할 국가를 선택하는 국가 드롭다운.]({% image_buster /assets/img_archive/dnd_iam_phone_capture_countries.png %}){: style="max-width:40%"}

#### 유효하지 않은 전화번호

사용자가 수용되지 않는 특수 문자가 포함된 전화번호를 입력하면, 그들은 사용자 정의할 수 없는 일반 오류 표시기를 보게 되며 양식을 제출할 수 없습니다. **미리보기 & 테스트** 탭과 테스트 장치에서 오류 동작을 확인할 수 있습니다. 이 기사를 참조하여 [Braze가 전화번호를 형식화하는 방법]({{site.baseurl}}/user_guide/message_building_by_channel/sms/phone_numbers/user_phone_numbers/#importing-phone-numbers)을 알아보십시오.

### 4단계: 면책 조항 언어 추가 (SMS 및 RCS 가입 양식용)

SMS 및 RCS 가입 양식의 경우, 보낼 SMS 또는 RCS의 유형을 명확하게 전달하는 것이 중요합니다. 양식에 다음 정보를 포함하여 목록 성장의 준수를 확인하십시오:

- 고객이 기대할 수 있는 SMS 및 RCS 메시지 유형에 대한 설명(장바구니 알림, 프로모션 및 거래, 약속 알림 등). 모든 사용 사례를 나열할 필요는 없지만, 귀하의 브랜드가 보낼 메시지 유형에 대한 설명을 제공해야 합니다.
- 동의는 구매의 조건이 아님을 유의하십시오(해당되는 경우).
- 메시지 빈도 및 메시지 및 데이터 요금이 적용된다는 알림입니다. 정확한 메시지 빈도를 모르는 경우 빈도가 달라질 수 있다고 말할 수 있습니다.
- 귀하의 약관 & 조건 및 SMS 및 RCS 개인정보 보호정책에 대한 링크입니다.
- 도움 및 선택 해제 키워드에 대한 알림(도움이 필요하면 HELP; 취소하려면 STOP).

우리는 템플릿에 자리 표시자 면책 조항을 예시로 제공했습니다. 이는 법적 조언을 구성하지 않으며 준수 목적으로 의존해서는 안 됩니다. 특정 브랜드에 맞춘 언어를 개발하기 위해 법률 팀과 협력하는 것이 중요합니다.

{% alert note %}
이 문서는 법적 조언을 제공하기 위한 것이 아니며, 법적 조언을 제공한다고 완전히 의존할 수 없습니다.
{% endalert %}

SMS 및 RCS 준수에 대한 자세한 내용은 [Laws and regulations for SMS, MMS, and RCS]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/laws_and_regulations/)를 참조하십시오.

### 5단계: 메시지 스타일 지정

드래그 앤 드롭 [앱 내 메시지 구성 요소]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/style_settings/#message-components)를 사용하여 메시지의 모양과 느낌을 사용자 지정하십시오.

## 결과 분석

{% multi_lang_include drag_and_drop/templates.md section='reporting' %}

\![앱 내 메시지 성능 패널이 앱 내 메시지의 각 링크에 대한 클릭 수를 보여줍니다.]({% image_buster /assets/img_archive/dnd_iam_phone_capture_analytics.png %})



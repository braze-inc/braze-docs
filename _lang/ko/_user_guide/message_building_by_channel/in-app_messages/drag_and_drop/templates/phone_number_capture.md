---
nav_title: SMS 및 WhatsApp 가입 양식
article_title: SMS 및 WhatsApp 가입 양식
alias: "/phone_number_capture/"
description: "이 참조 페이지는 인앱 메시지 드래그 앤 드롭 편집기를 사용하여 SMS 및 WhatsApp 가입 양식을 만드는 방법을 다룹니다."
---

# SMS 및 WhatsApp 가입 양식

> SMS 및 WhatsApp 가입 양식은 인앱 메시지용 드래그 앤 드롭 편집기에서 사용할 수 있는 템플릿입니다. 이 템플릿을 사용하여 사용자의 전화번호를 수집하고 SMS 및 WhatsApp 구독 그룹을 성장시키세요.

![전화 가입 양식 템플릿을 사용하여 생성된 인앱 메시지의 세 가지 예][img7]

## SDK 요구 사항

### 최소 SDK 버전

드래그 앤 드롭 편집기를 사용하여 생성된 메시지는 다음 최소 SDK 버전의 사용자에게만 보낼 수 있습니다. [사전 조건][1] 섹션에서 [드래그 앤 드롭으로 인앱 메시지 만들기]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/create/)에 대한 자세한 내용과 유의할 점을 확인하세요.

{% sdk_min_versions swift:5.0.0 android:8.0.0 web:2.5.0 %}

### 텍스트 링크용 소프트웨어 개발 키트 버전

메시지를 해제하지 않는 텍스트 링크를 포함하려면 사용자가 다음 최소 SDK 버전을 사용해야 합니다.

{% sdk_min_versions swift:6.2.0 android:26.0.0 %}

{% alert warning %}
인앱 메시지에 URL로 리디렉션되는 링크를 포함하고 최종 사용자가 지정된 최소 소프트웨어 개발 키트(SDK) 버전에 있지 않은 경우, 링크를 클릭하면 메시지가 닫히고 사용자가 양식을 제출하기 위해 메시지로 돌아갈 수 없습니다.
{% endalert %}

## 전화번호 가입 양식 만들기

드래그 앤 드롭 인앱 메시지를 만들 때 템플릿으로 **SMS 가입** 또는 **WhatsApp 가입**을 선택하세요.

![SMS 가입 또는 WhatsApp 가입을 선택하는 모달을 인앱 메시지를 만들 때 템플릿으로 사용합니다.][img2]{: style="max-width:70%"}

이 템플릿은 모바일 앱과 웹 브라우저 모두에서 지원됩니다.

### 1단계: 메시지 스타일을 설정하세요

템플릿을 사용자 정의하기 전에 사이드 메뉴를 사용하여 전체 메시지에 대한 메시지 수준 스타일을 설정할 수 있습니다. 예를 들어, 메시지에 포함된 모든 텍스트의 글꼴이나 모든 링크의 색상을 사용자 정의할 수 있습니다. 메시지를 모달 또는 전체 화면 디스플레이 유형으로 만들 수도 있습니다.

![커스텀 폰트 업로드 및 선택 워크플로우.][img6]

### 2단계: 전화번호 입력 구성 요소 사용자 지정

시작하려면 가입 양식을 작성하고 편집기에서 전화번호 입력 구성 요소를 선택하세요.

![전화번호 입력 구성 요소가 선택된 가입 양식 생성 시 미리보기 영역.][img3]{: style="max-width:40%"}

사이드 메뉴에서 이 템플릿이 전화번호를 수집할 구독 그룹을 지정합니다. 준수 모범 사례를 따르기 위해 전화번호 가입 양식당 하나의 구독 그룹에 대한 동의만 수집할 수 있습니다. 그러나 원할 경우 다른 구독 그룹에 대한 동의를 얻기 위해 여러 양식을 사용할 수 있습니다.

![구독 그룹 드롭다운에 구독 그룹이 선택되었습니다.][img4]{: style="max-width:40%"}

기본값으로, 우리는 전 세계적으로 숫자를 수집하지만, 숫자를 수집할 국가의 수를 제한할 수 있습니다. 이것은 특정 국가의 전화번호를 가진 사용자에게만 메시지를 보내려는 경우에 유용하며, 목록 청결을 도울 수 있습니다. 이를 위해 **모든 국가에서 숫자 수집**을 끄고 드롭다운을 사용하여 특정 국가를 선택하십시오. 사용자는 명시적으로 추가한 국가만 선택할 수 있습니다.

![국가 드롭다운에서 번호를 수집하려는 국가를 선택합니다.][img5]{: style="max-width:40%"}

#### 유효하지 않은 전화번호

사용자가 허용되지 않는 특수 문자가 포함된 전화번호를 입력하면 사용자에게 사용자 지정할 수 없는 일반 오류 표시기가 표시되며 양식을 제출할 수 없습니다. **미리보기 및 테스트** 탭과 테스트 기기에서 오류 동작을 확인할 수 있습니다. 이 문서를 참조하여 [Braze가 전화번호를 형식화하는 방법][2]을 배우십시오.

### 3단계: 면책 조항 언어 추가 (SMS 가입 양식용)

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

### 4단계: 메시지를 스타일링하세요

드래그 앤 드롭 [인앱 메시지 구성 요소][3]를 사용하여 메시지의 모양과 느낌을 사용자 정의할 수 있습니다.

## 보고

캠페인이 시작된 후, 실시간으로 결과를 분석하여 몇 명의 사용자가 캠페인에 참여했는지 확인할 수 있습니다. 구독 그룹에 가입한 사용자가 몇 명인지 확인하려면, 인앱 메시지를 받고 양식을 제출한 사용자를 필터링하여 구독 그룹에 가입한 사용자로 [세그먼트를 생성][5]할 수 있습니다.

![인앱 메시지 성능/성과 패널은 인앱 메시지의 각 링크에 대한 클릭 수를 보여줍니다.][img8]

[1]: {{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/create/#prerequisites
[2]: {{site.baseurl}}/user_guide/message_building_by_channel/sms/phone_numbers/user_phone_numbers/#importing-phone-numbers
[3]: {{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/create/#drag-and-drop-in-app-message-components
[4]: {{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_laws_and_regulations/
[5]: {{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/

[img1]: {% image_buster /assets/img_archive/dnd_iam_phone_capture_example.png %}
[img2]: {% image_buster /assets/img_archive/dnd_iam_phone_capture_template.png %}
[img3]: {% image_buster /assets/img_archive/dnd_iam_phone_capture_select.png %}
[img4]: {% image_buster /assets/img_archive/dnd_iam_phone_capture_subscription.png %}
[img5]: {% image_buster /assets/img_archive/dnd_iam_phone_capture_countries.png %}
[img6]: {% image_buster /assets/img_archive/dnd_iam_phone_capture_custom_font.gif %}
[img7]: {% image_buster /assets/img_archive/dnd_iam_phone_capture_example2.png %}
[img8]: {% image_buster /assets/img_archive/dnd_iam_phone_capture_analytics.png %}

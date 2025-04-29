---
nav_title: 이메일 수집 양식
article_title: 이메일 수집 양식
page_order: 3
page_type: reference
description: "이 문서에서는 이메일 캡처 인앱 메시지 유형에 대한 개요를 설명합니다."
channel:
  - in-app messages
---

# 이메일 캡처 양식 {#email-capture-form}

> 이메일 캡처 메시지를 사용하면 사이트 사용자에게 이메일 주소를 제출하라는 메시지를 쉽게 보낼 수 있으며, 이후에는 사용자 프로필에서 해당 이메일 주소를 모든 메시징 캠페인에 사용할 수 있습니다.

최종 사용자가 이 양식에 이메일 주소를 입력하면 해당 이메일 주소가 사용자 프로필에 추가됩니다.

- 아직 계정이 없는 [익명 사용자의]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/#anonymous-user-profiles) 경우 이메일 주소는 사용자의 디바이스에 연결된 익명 사용자 프로필에 저장됩니다.
- 사용자 프로필에 이미 이메일 주소가 있는 경우 기존 이메일 주소는 새로 입력한 이메일 주소로 덮어쓰기됩니다.
- 알려진 사용자에게 [하드 반송된]({{site.baseurl}}/help/help_articles/email/email_bounces#email-bounces) 것으로 플래그가 지정된 이메일 주소가 있는 경우, 새로 입력한 이메일 주소가 Braze 프로필에 있는 이메일 주소와 다른지 확인합니다. 입력한 이메일 주소가 다른 경우 이메일 주소가 업데이트되고 하드 반송 상태가 제거됩니다. 
- 사용자가 잘못된 이메일 주소를 입력하면 오류 메시지가 표시됩니다: "유효한 이메일을 입력하세요."
    - 잘못된 이메일 주소입니다: 
        - `example`
        - `example@`
        - `@gmail.com`
        - `example@gmail`
    - 유효한 이메일 주소: 
        - `example@gmail.com`
        - `example@gnail.com`(오타 포함)
    - For more information on email validation in Braze, refer to [Email technical guidelines and notes]({{site.baseurl}}/user_guide/message_building_by_channel/email/email_setup/email_validation/).

{% details 식별된 사용자와 익명 사용자에 대해 자세히 알아보기 %}

일반적으로 이메일 캡처 양식의 로직은 간단합니다. 현재 활성 상태인 사용자의 Braze 내 고객 프로필에 이메일 주소가 설정됩니다. 그러나 이는 사용자가 식별되었는지(로그인, `changeUser` 호출) 여부에 따라 동작이 달라진다는 의미입니다.

익명의 사용자가 양식에 이메일을 입력하고 제출하면 Braze는 해당 이메일 주소를 프로필에 추가합니다. 웹 여정 후반에 `changeUser`가 호출되고 새 `external_id`가 할당되는 경우(예: 새 사용자가 서비스에 등록하는 경우) 이메일 주소를 포함한 모든 익명 사용자 프로필 데이터가 병합됩니다.

`changeUser`가 기존 `external_id`와 함께 호출되는 경우 익명 사용자 프로필은 고아가 되고 식별된 사용자에 아직 존재하지 않는 [특정 고객프로필 데이터 필드]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/#merge_updates-behavior)는 병합되지만 이메일 주소를 포함하여 이미 존재하는 필드는 모두 손실됩니다.

For more information, refer to the [User profile lifecycle]({{site.baseurl}}/user_guide/data/user_data_collection/user_profile_lifecycle/).

{% enddetails %}

## 1단계: 인앱 메시지 캠페인 만들기

이 옵션으로 이동하려면 인앱 메시징 캠페인을 만들어야 합니다. 여기에서 사용 사례에 따라 **받는 사람**을 **웹 브라우저**, **모바일 앱** 또는 **모바일 앱과 웹 브라우저 모두로** 설정한 다음 **메시지 유형**으로 **이메일 캡처 양식**을 선택합니다.

![][4]

{% alert note %}
웹 SDK를 통해 HTML 인앱 메시지를 활성화하려면, 예를 들어 `braze.initialize('YOUR-API_KEY', {allowUserSuppliedJavascript: true})`와 같이 `allowUserSuppliedJavascript` 초기화 옵션을 Braze에 제공해야 합니다. 이는 보안상의 이유로, HTML 인앱 메시지는 JavaScript를 실행할 수 있으므로 사이트 관리자가 이를 활성화해야 합니다.
{% endalert %}

## 2단계: 양식 사용자 지정 {#customizable-features}

그런 다음 필요에 따라 양식을 사용자 지정합니다. 이메일 캡처 양식에 대해 다음 기능을 사용자 지정할 수 있습니다:

- 헤더, 본문 및 제출 버튼 텍스트
- 선택적 이미지
- 선택 사항인 '서비스 약관' 링크
- 헤더 및 본문 텍스트, 버튼, 배경의 색상을 다르게 지정할 수 있습니다.
- 키-값 쌍
- 머리글 및 본문 텍스트, 버튼, 버튼 테두리 색상, 배경 및 오버레이 스타일

![이메일 캡처 양식용 작성기입니다.][5]

추가 커스텀이 필요한 경우 **메시지 유형**에 대한 **커스텀 코드**를 선택합니다. 이 [이메일 캡처 모달 템플릿](https://github.com/braze-inc/in-app-message-templates/tree/master/braze-templates/5-email-capture-modal)은 [Braze 템플릿](https://github.com/braze-inc/in-app-message-templates/tree/master/braze-templates) GitHub 리포지토리에서 시작 코드로 사용할 수 있습니다.

## 3단계: 참가 오디언스 설정

기존 이메일 주소가 없는 사용자에게만 이 양식을 보내려면 `Email Available is false` 필터를 사용하세요.

![사용 가능한 이메일로 필터링이 거짓입니다.][10]{: style="max-width:50%"}

외부 ID가 없는 사용자(익명 사용자)에게만 이 양식을 보내려면 `External User ID is blank` 필터를 사용하세요.

![외부 사용자 ID로 필터링이 비어 있습니다.][11]{: style="max-width:50%"}

원하는 경우 `AND` 로직을 사용하여 두 필터를 결합할 수도 있습니다.

## 4단계: 양식을 작성한 사용자 타겟팅(선택 사항)

이메일 캡처 양식을 실행하고 사용자로부터 이메일 주소를 수집한 후에는 `Clicked/Opened Campaign` 필터를 사용하여 해당 사용자를 타겟팅할 수 있습니다. 

캠페인 `<CAMPAIGN_NAME>` 에 대해 필터를 `Has clicked in-app message button 1` 로 설정합니다. `<CAMPAIGN_NAME>` 을 이메일 캡처 양식 캠페인의 이름으로 바꿉니다.

![웹 이메일 캡처 양식 캠페인의 인앱 메시지 버튼 1을 클릭한 경우 필터링하기][12]

[4]: {% image_buster /assets/img/email_capture_config.png %}
[5]: {% image_buster /assets/img/email_capture.png %}
[10]: {% image_buster /assets/img_archive/web_email_filter_1.png %}
[11]: {% image_buster /assets/img_archive/web_email_filter_2.png %}
[12]: {% image_buster /assets/img_archive/web_email_filter_3.png %}

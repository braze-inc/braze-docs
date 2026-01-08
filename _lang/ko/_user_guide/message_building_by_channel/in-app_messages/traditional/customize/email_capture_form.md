---
nav_title: 이메일 캡처 양식
article_title: 이메일 캡처 양식
page_order: 3
page_type: reference
description: "이 문서는 이메일 캡처 인앱 메시지 유형에 대한 개요를 제공합니다."
channel:
  - in-app messages
---

# 이메일 캡처 양식 {#email-capture-form}

> 이메일 캡처 메시지는 사이트 사용자에게 이메일 주소를 제출하도록 쉽게 유도할 수 있으며, 이후 해당 이메일 주소는 모든 메시징 캠페인에서 사용할 수 있도록 사용자 프로필에 저장됩니다.

최종 사용자가 이 양식에 이메일 주소를 입력하면, 이메일 주소가 사용자 프로필에 추가됩니다.

- 계정이 없는 [익명 사용자]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/#anonymous-user-profiles)의 경우, 이메일 주소는 사용자의 장치에 연결된 익명 사용자 프로필에 저장됩니다.
- 사용자 프로필에 이미 이메일 주소가 존재하는 경우, 기존 이메일 주소는 새로 입력된 이메일 주소로 덮어씌워집니다.
- 알려진 사용자가 [하드 바운스]({{site.baseurl}}/help/help_articles/email/email_bounces#email-bounces)로 표시된 이메일 주소를 가지고 있다면, 새로 입력된 이메일 주소가 Braze 프로필에 있는 이메일 주소와 다른지 확인합니다. 제공된 이메일 주소가 다르면, 이메일 주소가 업데이트되고 하드 바운스 상태가 제거됩니다. 
- 사용자가 유효하지 않은 이메일 주소를 입력하면, 사용자에게 오류 메시지가 표시됩니다: "유효한 이메일을 입력해 주세요."
    - 유효하지 않은 이메일 주소: 
        - `example`
        - `example@`
        - `@gmail.com`
        - `example@gmail`
    - 유효한 이메일 주소: 
        - `example@gmail.com`
        - `example@gnail.com` (오타 포함)
    - Braze에서 이메일 검증에 대한 자세한 정보는 [이메일 기술 지침 및 노트]({{site.baseurl}}/user_guide/message_building_by_channel/email/email_setup/email_validation/)를 참조하세요.

{% details More on identified versus anonymous users %}

일반적으로 이메일 캡처 양식의 논리는 간단합니다. 현재 활성화된 사용자에 대해 Braze의 사용자 프로필에 이메일 주소가 설정됩니다. 그러나 이는 사용자가 식별되었는지(로그인, `changeUser` 호출됨) 여부에 따라 동작이 다르다는 것을 의미합니다.

익명 사용자가 양식에 이메일을 입력하고 제출하면, Braze는 이메일 주소를 그들의 프로필에 추가합니다. 만약 `changeUser`이 웹 여정에서 나중에 호출되고 새로운 `external_id`가 할당되면(예: 새로운 사용자가 서비스에 등록할 때), 모든 익명 사용자 프로필 데이터가 이메일 주소를 포함하여 병합됩니다.

만약 `changeUser`이 기존 `external_id`와 함께 호출되면, 익명 사용자 프로필은 고아가 되고 [특정 사용자 프로필 데이터 필드]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/#merge_updates-behavior)는 식별된 사용자에게 이미 존재하지 않는 경우에만 병합되지만, 이미 존재하는 필드는 잃게 되며, 이메일 주소도 포함됩니다.

자세한 정보는 [사용자 프로필 생애 주기]({{site.baseurl}}/user_guide/data/user_data_collection/user_profile_lifecycle/)를 참조하십시오.

{% enddetails %}

## 1단계: 앱 내 메시지 캠페인 만들기

이 옵션으로 이동하려면, 앱 내 메시징 캠페인을 만들어야 합니다. 거기에서 사용 사례에 따라 **보내기 대상**을 **웹 브라우저**, **모바일 앱** 또는 **모바일 앱 & 웹 브라우저** 중 하나로 설정한 다음, **이메일 캡처 양식**을 **메시지 유형**으로 선택하십시오.

{% alert note %}
**웹 사용자 타겟팅?** <br>웹 SDK를 통해 HTML 앱 내 메시지를 활성화하려면, Braze에 `allowUserSuppliedJavascript` 초기화 옵션을 제공해야 합니다. 예: `braze.initialize('YOUR-API_KEY', {allowUserSuppliedJavascript: true})`. 이는 HTML 앱 내 메시지가 JavaScript를 실행할 수 있기 때문에 보안상의 이유로 필요하며, 사이트 유지 관리자가 이를 활성화해야 합니다.
{% endalert %}

## 2단계: 양식 {#customizable-features} 사용자 정의하기

다음으로, 필요에 따라 양식을 사용자 정의하십시오. 이메일 캡처 양식에 대해 다음 기능을 사용자 정의할 수 있습니다:

- 헤더, 본문 및 제출 버튼 텍스트
- 선택적 이미지
- 선택적 "서비스 약관" 링크
- 헤더 및 본문 텍스트, 버튼 및 배경의 다양한 색상
- 키-값 쌍
- 헤더 및 본문 텍스트, 버튼, 버튼 테두리 색상, 배경 및 오버레이 스타일

\![이메일 캡처 양식용 컴포저.]({% image_buster /assets/img/email_capture.png %})

추가 사용자 지정을 해야 하는 경우, **사용자 정의 코드**를 **메시지 유형**으로 선택하세요. 시작 코드로 [브레이즈 템플릿](https://github.com/braze-inc/in-app-message-templates/tree/master/braze-templates) GitHub 리포지토리에서 이 [이메일 캡처 모달 템플릿](https://github.com/braze-inc/in-app-message-templates/tree/master/braze-templates/5-email-capture-modal)을 사용할 수 있습니다.

## 3단계: 진입 청중 설정

사용자 이메일을 캡처하기 위해 인앱 메시지를 사용하는 경우, 이미 이 정보를 제공하지 않은 사용자로 청중을 제한할 수 있습니다.

- **이메일 주소가 없는 사용자 타겟팅:** 필터 `Email Available`가 `false`인 경우 사용하세요. 이렇게 하면 이메일이 파일에 없는 사용자에게만 양식이 표시되어, 이미 알려진 사용자에게 중복 프롬프트를 피할 수 있습니다.
- **외부 ID가 없는 익명 사용자 타겟팅:** 필터 `External User ID` `is blank`를 사용하세요. 이것은 인증되지 않았거나 아직 등록되지 않은 사용자를 식별하고자 할 때 유용합니다.

원하는 경우 `AND` 논리를 사용하여 두 필터를 결합할 수도 있습니다. 이렇게 하면 이메일 주소와 외부 사용자 ID가 모두 없는 사용자에게만 양식이 표시됩니다. 이는 새로운 리드를 캡처하거나 계정 생성을 유도하는 데 이상적입니다.

## 4단계: 양식을 작성한 사용자 타겟팅(선택 사항)

이메일 캡처 양식을 시작하고 사용자로부터 이메일 주소를 수집한 후, 양식을 작성한 사용자를 타겟팅할 수 있습니다.

1. 브레이즈의 모든 세그먼트 필터에서 필터 `Clicked/Opened Campaign`을 선택하세요. 
2. 드롭다운에서 `clicked in-app message button 1`을(를) 선택하세요.
3. 이메일 캡처 양식 캠페인을 선택하세요.


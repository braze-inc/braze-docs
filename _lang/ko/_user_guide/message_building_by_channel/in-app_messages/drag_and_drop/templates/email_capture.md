---
nav_title: 이메일 가입 양식
article_title: 이메일 가입 양식
alias: "/email_capture/"
page_order: 2
description: "이 페이지에서는 앱 내 메시지 드래그 앤 드롭 편집기를 사용하여 이메일 가입 양식을 만드는 방법을 설명합니다."
---

# 이메일 가입 양식

> 드래그 앤 드롭 이메일 가입 인앱 메시지 템플릿을 사용하여 사용자의 이메일 주소를 수집하고 구독 그룹을 늘릴 수 있습니다.

{% multi_lang_include drag_and_drop/templates.md section='SDK 요구 사항' %}

## 이메일 가입 양식 만들기

### 1단계: 템플릿 선택

드래그 앤 드롭 인앱 메시지를 만들 때 템플릿에 대한 **이메일 가입을** 선택한 다음 **메시지 작성을** 선택합니다. 이 템플릿은 모바일 앱과 웹 브라우저 모두에서 지원됩니다.

![The in-app message editor with the template for an email capture form.]({% image_buster /assets/img/drag_and_drop/templates/email_capture_template1.png %})

### 2단계: 메시지 스타일을 설정하세요

{% multi_lang_include drag_and_drop/templates.md section='메시지 스타일' %}

### 3단계: 이메일 가입 구성 요소 사용자 지정

이메일 가입 양식 작성을 시작하려면 편집기에서 이메일 캡처 요소를 선택합니다. 기본적으로 수집된 이메일 주소에는 글로벌 구독 그룹이 **구독됨**으로 설정됩니다. 특정 구독 그룹에 사용자를 옵트인하려면 [이메일 구독 상태 업데이트하기]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions#updating-email-subscription-states)를 참조하세요.

이메일 캡처 요소의 플레이스홀더 텍스트와 레이블 텍스트를 사용자 지정할 수 있습니다.

![The in-app message editor with a side menu for customizing the email capture element.]({% image_buster /assets/img/drag_and_drop/templates/email_capture_field1.png %})

#### 이메일 유효성 검사

사용자가 허용되지 않는 특수 문자가 포함된 이메일 주소를 입력하면 일반 오류 표시기가 표시되며 양식을 제출할 수 없습니다. 이 오류 메시지는 사용자 지정할 수 없습니다. **미리보기 및 테스트** 탭과 테스트 기기에서 오류 동작을 확인할 수 있습니다. [이메일 유효성 검사]({{site.baseurl}}/user_guide/message_building_by_channel/email/email_setup/email_validation/)에서 Braze가 이메일 주소 형식을 지정하는 방법에 대해 자세히 알아보세요.

### 4단계: 고지 사항 언어 추가(선택 사항)

{% multi_lang_include drag_and_drop/templates.md section='이메일 고지 사항' %}

### 5단계: 메시지를 스타일링하세요

Customize the look and feel of your sign-up form using the drag-and-drop [in-app message components]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/style_settings/#message-components).

## 결과 분석

{% multi_lang_include drag_and_drop/templates.md section='reporting' %}

## 모범 사례

{% multi_lang_include drag_and_drop/templates.md section='이메일 이중 옵트인' %}


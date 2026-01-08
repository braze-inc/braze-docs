---
nav_title: 이메일 가입 양식
article_title: 이메일 가입 양식
alias: "/email_capture/"
page_order: 2
description: "이 페이지에서는 인앱 메시지 드래그 앤 드롭 편집기를 사용하여 이메일 가입 양식을 만드는 방법을 다룹니다."
---

# 이메일 가입 양식

> 드래그 앤 드롭 이메일 가입 인앱 메시지 템플릿을 사용하여 사용자의 이메일 주소를 수집하고 구독 그룹을 늘리세요.

{% multi_lang_include drag_and_drop/templates.md section='SDK requirements' %}

## 이메일 가입 양식 만들기

### 1단계: 템플릿 선택

드래그 앤 드롭 인앱 메시지를 만들 때, 템플릿으로 **이메일 가입**을 선택한 후 **메시지 작성**을 선택하세요. 이 템플릿은 모바일 앱과 웹 브라우저 모두에서 지원됩니다.

\![이메일 캡처 양식 템플릿이 있는 인앱 메시지 편집기.]({% image_buster /assets/img/drag_and_drop/templates/email_capture_template1.png %})

### 2단계: 메시지 스타일 설정

{% multi_lang_include drag_and_drop/templates.md section='message style' %}

### 3단계: 이메일 가입 구성 요소 사용자 정의

이메일 가입 양식을 만들기 시작하려면 편집기에서 이메일 캡처 요소를 선택하세요. 기본적으로 수집된 이메일 주소는 전역 구독 그룹 **구독됨**에 포함됩니다. 특정 구독 그룹에 사용자를 추가하려면 [이메일 구독 상태 업데이트]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions#updating-email-subscription-states)를 참조하세요.

이메일 캡처 요소의 자리 표시자 텍스트와 레이블 텍스트를 사용자 정의할 수 있습니다.

\![이메일 캡처 요소를 사용자 정의하기 위한 사이드 메뉴가 있는 인앱 메시지 편집기.]({% image_buster /assets/img/drag_and_drop/templates/email_capture_field1.png %})

#### 이메일 유효성 검사

사용자가 허용되지 않는 특수 문자가 포함된 이메일 주소를 입력하면 일반 오류 표시기가 표시되며 양식을 제출할 수 없습니다. 이 오류 메시지는 사용자 정의할 수 없습니다. **미리보기 & 테스트** 탭과 테스트 장치에서 오류 동작을 확인할 수 있습니다. Braze가 이메일 주소를 형식화하는 방법에 대해 [이메일 유효성 검사]({{site.baseurl}}/user_guide/message_building_by_channel/email/email_setup/email_validation/)에서 자세히 알아보세요.

### 4단계: 면책 조항 언어 추가(선택 사항)

{% multi_lang_include drag_and_drop/templates.md section='email disclaimer' %}

### 5단계: 메시지 스타일 지정

드래그 앤 드롭 [앱 내 메시지 구성 요소]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/style_settings/#message-components)를 사용하여 가입 양식의 모양과 느낌을 사용자 정의하세요.

## 결과 분석

{% multi_lang_include drag_and_drop/templates.md section='reporting' %}

## 모범 사례

{% multi_lang_include drag_and_drop/templates.md section='email double opt-in' %}


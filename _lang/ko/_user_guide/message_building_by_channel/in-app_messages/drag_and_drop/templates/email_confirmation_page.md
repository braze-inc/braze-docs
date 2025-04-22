---
nav_title: 이메일 가입 확인
article_title: 이메일 가입 확인 페이지
alias: "/email_confirmation_page/"
page_order: 6
description: "이 페이지에서는 앱 내 메시지 끌어서 놓기 편집기를 사용하여 확인 페이지가 있는 이메일 가입 양식을 만드는 방법에 대해 설명합니다."
---

# 확인 페이지가 포함된 이메일 가입

> 앱 내 메시지 드래그 앤 드롭 편집기를 사용하여 확인 페이지가 포함된 이메일 가입 양식을 만들 수 있습니다.

{% multi_lang_include drag_and_drop/templates.md section='SDK 요구 사항' %}

## 확인 페이지가 있는 이메일 가입 양식 만들기

### 1단계: 템플릿 선택

 이 템플릿은 모바일 앱과 웹 브라우저 모두에서 지원됩니다.



### 2단계: 메시지 스타일을 설정하세요

{% multi_lang_include drag_and_drop/templates.md section='메시지 스타일' %}

### 3단계: 이메일 가입 구성 요소 사용자 지정

이메일 가입 양식 작성을 시작하려면 편집기에서 이메일 캡처 요소를 선택합니다. 기본적으로 수집된 이메일 주소에는 글로벌 구독 그룹이 **구독됨**으로 설정됩니다. 특정 구독 그룹에 사용자를 옵트인하려면 [이메일 구독 상태 업데이트하기]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions#updating-email-subscription-states)를 참조하세요.

이메일 캡처 요소의 플레이스홀더 텍스트와 레이블 텍스트를 사용자 지정할 수 있습니다.

![이메일 캡처 요소를 사용자 지정할 수 있는 사이드 메뉴가 있는 인앱 메시지 편집기.][img2]

#### 이메일 유효성 검사

{% multi_lang_include drag_and_drop/templates.md section='이메일 유효성 검사' %}

### 4단계: 고지 사항 언어 추가(선택 사항)

{% multi_lang_include drag_and_drop/templates.md section='이메일 고지 사항' %}

### 5단계: 메시지를 스타일링하세요

드래그 앤 드롭 [인앱 메시지 구성 요소를][3] 사용하여 이메일 가입 양식 및 확인 페이지의 모양과 느낌을 사용자 지정할 수 있습니다.

## 결과 분석

{% multi_lang_include drag_and_drop/templates.md section='reporting' %}

## 모범 사례

{% multi_lang_include drag_and_drop/templates.md section='이메일 이중 옵트인' %}

[img1]: {% image_buster /assets/img/drag_and_drop/templates/email_capture_confirmation.png %}
[img2]: {% image_buster /assets/img/drag_and_drop/templates/email_capture_field_confirmation.png %} 

[3]: {{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/style_settings/#message-components

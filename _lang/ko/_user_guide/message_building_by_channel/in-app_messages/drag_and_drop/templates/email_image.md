---
nav_title: 이미지로 이메일 가입하기
article_title: 배경 이미지가 포함된 이메일 가입
alias: "/email_image/"
page_order: 4
description: "이 페이지에서는 인앱 메시지 드래그 앤 드롭 편집기를 사용하여 간단한 메시지 하나로 브랜드 스타일을 뽐내고 이메일 목록을 구축하는 방법에 대해 설명합니다."
---

# 배경 이미지가 포함된 이메일 가입

> 인앱 메시지 드래그 앤 드롭 편집기를 사용해 간단한 메시지 하나로 브랜드 스타일을 뽐내고 이메일 목록을 구축하세요.

{% multi_lang_include drag_and_drop/templates.md section='SDK requirements' %}

## 배경 이미지가 있는 이메일 가입 양식 만들기

### 1단계: 템플릿 선택

드래그 앤 드롭 인앱 메시지를 만들 때는 템플릿에 **배경 이미지가 있는 이메일 가입을** 선택한 다음 **메시지 구축을** 선택합니다. 이 템플릿은 모바일 앱과 웹 브라우저 모두에서 지원됩니다.

배경 이미지가 있는 이메일 가입 양식 템플릿이 포함된 인앱 메시지 편집기입니다.]({% image_buster /assets/img/drag_and_drop/templates/email_capture_image.png %})

### 2단계: 메시지 스타일 설정하기

{% multi_lang_include drag_and_drop/templates.md section='message style' %}

### 3단계: 이메일 가입 구성 요소 커스텀하기

이메일 가입 양식 구축을 시작하려면 편집기에서 이메일 캡처 요소를 선택합니다. 기본값으로 수집된 이메일 주소에는 글로벌 구독 그룹이 **구독한** 상태로 설정됩니다. 특정 구독 그룹에 사용자를 옵트인하려면 [이메일 구독 상태 업데이트하기를]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions#updating-email-subscription-states) 참조하세요.

이메일 캡처 요소의 입력 안내 텍스트와 레이블 텍스트를 커스텀할 수 있습니다.

이메일 캡처 요소를 커스텀할 수 있는 사이드 메뉴가 있는 인앱 메시지 편집기.]({% image_buster /assets/img/drag_and_drop/templates/email_capture_field_image.png %})

#### 이메일 유효성 검사

{% multi_lang_include drag_and_drop/templates.md section='email validation' %}

### 4단계: 고지 사항 언어 추가(선택 사항)

{% multi_lang_include drag_and_drop/templates.md section='email disclaimer' %}

### 5단계: 메시지 스타일 지정하기

드래그 앤 드롭 [인앱 메시지 구성 요소를]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/style_settings/#message-components) 사용하여 가입 양식의 모양과 느낌을 커스텀할 수 있습니다. **메시지 컨테이너** 메뉴에서 기본값 배경 이미지 URL을 바꾸어 나만의 배경 이미지를 추가하거나 URL을 제거하고 [미디어 라이브러리에서]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/media_library/) 이미지를 선택합니다.

## 결과 분석

{% multi_lang_include drag_and_drop/templates.md section='reporting' %}

## 모범 사례

{% multi_lang_include drag_and_drop/templates.md section='email double opt-in' %}





---
nav_title: 이미지 사양
article_title: 이미지 사양
page_order: 4.1

page_type: reference
description: "이 참조 문서에서는 각 채널 유형에 권장되는 이미지 크기와 사양에 대해 설명합니다."
tool:
  - Templates
  - Media

---

# 이미지 사양

> 일반적으로 크기가 작고 품질이 좋은 이미지일수록 더 빨리 로드되므로 원하는 결과물을 얻으려면 가능한 한 가장 작은 자산을 사용하는 것이 좋습니다. 특정 채널에서 이미지 사용을 극대화하려면 이 도움말의 자세한 내용을 참조하세요.

항상 다양한 기기에서 [메시지를 미리 보고 테스트하여]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/testing/) 이미지와 메시징의 가장 중요한 부분이 예상대로 표시되는지 확인해야 합니다.

{% alert tip %} 자신 있게 자산을 생성하세요! 인앱 메시지 이미지 템플릿과 안전 영역 오버레이는 모든 크기의 기기에 잘 어울리도록 설계되었습니다. [디자인 템플릿 ZIP 다운로드]({% image_buster /assets/download_file/Braze-In-App-Message-Design-Templates.zip %}). {% endalert %}

{% multi_lang_include image_specs.md variable_name='payload size' %}

## 인앱 메시지

{% multi_lang_include image_specs.md variable_name='in-app messages' %}

### 글꼴 어썸

Braze는 모달 인앱 메시지 아이콘에 [Font Awesome v4.3.0](https://fontawesome.com/v4.7.0/cheatsheet/) 사용을 지원합니다.

## 푸시 알림

{% multi_lang_include image_specs.md variable_name='push notifications' %}

## 이메일

{% multi_lang_include image_specs.md variable_name='email' %}

## 이미지 동작

{% multi_lang_include image_specs.md variable_name='image behavior' %}

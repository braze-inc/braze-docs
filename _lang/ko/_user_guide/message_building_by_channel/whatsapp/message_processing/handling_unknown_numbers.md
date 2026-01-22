---
nav_title: 알 수 없는 전화번호 처리
article_title: 알 수 없는 전화번호 처리
description: "이 참조 문서에서는 Braze가 WhatsApp 사용자에 대한 알 수 없는 전화번호를 처리하는 방법을 다룹니다."
page_type: reference
channel:
  - WhatsApp
page_order: 50
---

# 알 수 없는 전화번호 처리

> Braze와 함께 WhatsApp을 설정한 후 알 수 없는 사용자로부터 메시지를 받을 수 있습니다. 다음 단계에서는 식별되지 않은 사용자와 번호가 처리되는 방법을 설명합니다.

## 알 수 없는 번호에 대한 옵트인/옵트아웃 및 사용자 지정 키워드 워크플로우

Braze는 먼저 일치하는 번호를 가진 사용자를 찾으려고 시도합니다. 일치하는 사용자가 없으면 Braze는 알 수 없는 번호를 두 가지 방법 중 하나로 자동으로 처리합니다:

1. **트리거 단어가 [옵트인 캔버스]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/message_processing/opt-ins_and_opt-outs/)로 설정된 경우:**
- Braze는 익명 프로필을 생성합니다.
- 다음 세부정보로 프로필에 사용자 별칭을 할당합니다:
  - 사용자가 제공한 전화번호 값을 가진 `alias_name`
  - 값이 `phone`인 `alias_label`
- 우리 시스템은 전화 속성을 설정합니다.
- 사용자는 캔버스 내에서 설정된 논리에 따라 해당 구독 그룹에 가입됩니다.<br><br>
2. **옵트인 캔버스가 설정되지 않은 경우:**
- Braze는 익명 프로필을 생성합니다.
- 다음 세부정보로 프로필에 사용자 별칭을 할당합니다:
  - 사용자가 제공한 전화번호 값을 가진 `alias_name`
  - 값이 `phone`인 `alias_label`
- 우리 시스템은 전화 속성을 설정합니다.
- 사용자의 구독 상태는 모든 WhatsApp 구독 그룹에 대해 `unsubscribed`로 기본 설정됩니다.<br><br>


---
nav_title: 알 수 없는 전화번호 처리
article_title: 알 수 없는 전화번호 처리
description: "이 참고 문서에서는 Braze가 WhatsApp 사용자의 알 수 없는 전화번호를 처리하는 방법에 대해 설명합니다."
page_type: reference
channel:
  - WhatsApp
page_order: 50
---

# 알 수 없는 전화번호 처리

> Braze로 WhatsApp을 실행한 후 알 수 없는 사용자로부터 메시지를 받는 경우가 있을 수 있습니다. 다음 단계에서는 미확인 사용자 및 번호가 처리되는 방법에 대해 설명합니다.

## 알 수 없는 번호에 대한 옵트인/아웃 및 사용자 지정 키워드 워크플로

Braze는 먼저 일치하는 번호를 가진 사용자를 찾으려고 시도합니다. 알 수 없는 번호가 발견되면 Braze는 두 가지 방법 중 하나를 사용하여 자동으로 주소를 지정합니다.

1. **[옵트인 캔버스가]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/message_processing/opt-ins_and_opt-outs/) 있는 트리거 단어가 설정된 경우:**
- Braze는 익명 프로필을 생성합니다.
- 프로필에 사용자 별칭을 다음과 같은 세부 정보로 할당합니다.
  - `alias_name` 값은 사용자가 제공한 전화번호입니다.
  - `phone` 값이 있는 `alias_label`
- 시스템에서 전화 속성을 설정합니다.
- 사용자는 캔버스 내에서 설정된 로직에 따라 해당 구독 그룹에 구독됩니다.<br><br>
2. **옵트인 캔버스가 설정되어 있지 않은 경우:**
- Braze는 익명 프로필을 생성합니다.
- 프로필에 사용자 별칭을 다음과 같은 세부 정보로 할당합니다.
  - `alias_name` 값은 사용자가 제공한 전화번호입니다.
  - `phone` 값이 있는 `alias_label`
- 시스템에서 전화 속성을 설정합니다.
- 사용자의 가입 상태는 모든 WhatsApp 구독 그룹에 대해 기본적으로 `unsubscribed`로 설정됩니다.<br><br>


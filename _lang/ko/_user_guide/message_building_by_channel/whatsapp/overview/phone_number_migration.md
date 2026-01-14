---
nav_title: WhatsApp 전화번호 마이그레이션
article_title: WhatsApp 전화번호 마이그레이션
page_order: 2
description: "이 참조 문서에서는 WhatsApp 전화번호를 마이그레이션하는 방법을 다룹니다."
page_type: reference
channel:
  - WhatsApp
---

# WhatsApp 전화번호 마이그레이션

> Meta의 임베디드 가입을 사용하여 WhatsApp 비즈니스 계정 간에 WhatsApp 전화번호를 마이그레이션하세요.

## 전제 조건

귀하의 전화번호는 마이그레이션 자격을 갖추기 위해 Meta의 요구 사항을 충족해야 합니다:

- 귀하의 Meta 비즈니스 계정이 인증되었습니다.
- 귀하의 기존 WhatsApp 비즈니스 계정이 승인되었습니다.
- 귀하의 기존 WhatsApp 비즈니스 계정에는 **결제 설정**에 유효한 결제 방법이 있습니다.
- 귀하의 비즈니스 전화번호에는 이중 인증이 꺼져 있어야 합니다. WhatsApp 비즈니스 계정을 소유하고 있다면 WhatsApp 관리자에서 해당 번호의 이중 인증을 끌 수 있습니다. 그렇지 않으면 솔루션 제공자에게 이를 끄도록 요청해야 합니다.

WhatsApp 전화번호를 마이그레이션하는 방법에 대한 정보는 Meta의 문서에서 [임베디드 가입을 통한 WhatsApp 비즈니스 계정 간 전화번호 마이그레이션](https://developers.facebook.com/docs/whatsapp/business-management-api/guides/migrate-phone-to-different-waba/)을 참조하세요.

## WhatsApp 전화번호 마이그레이션

1. WhatsApp 관리자에서 전화번호와 연결된 WhatsApp 비즈니스 계정(WABA)을 선택한 다음 **계정 도구** > **전화번호**로 이동합니다.
2. **이중 인증 끄기**를 선택하고 이후 단계를 완료하세요.<br><br>\![WhatsApp 비즈니스 관리자가 "전화번호" 페이지로 열려 있습니다.]({% image_buster /assets/img/whatsapp/waba_manager.png %}){: style="max-width:80%;"} <br><br> 전화번호를 다른 WhatsApp 비즈니스 그룹으로 마이그레이션하는 경우 Meta의 임베디드 가입에서 표시 이름이 일치해야 하므로 **전화번호** 페이지에서 기존 표시 이름을 확인하세요. 다음 단계에서 해당 이름을 입력하게 됩니다.<br><br>\![WhatsApp 비즈니스 관리자의 전화번호 페이지에 "Braze"라는 표시 이름이 전화번호 옆에 나열되어 있습니다.]({% image_buster /assets/img/whatsapp/phone_numbers.png %}){: style="max-width:80%;"}<br><br>
3. 메타의 내장 가입 워크플로우를 완료하십시오. 


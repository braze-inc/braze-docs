---
nav_title: WhatsApp 전화번호 마이그레이션
article_title: WhatsApp 전화번호 마이그레이션
page_order: 2
description: "이 참조 문서에서는 WhatsApp 전화번호를 마이그레이션하는 방법에 대해 설명합니다."
page_type: reference
channel:
  - WhatsApp
---

# WhatsApp 전화번호 마이그레이션

> 메타의 임베디드 가입을 사용하여 WhatsApp 비즈니스 계정 간에 WhatsApp 전화번호를 마이그레이션하세요.

## 전제 조건

마이그레이션 자격을 얻으려면 전화번호가 메타의 요구 사항을 충족해야 합니다.

- 메타 비즈니스 계정이 인증되었습니다.
- 기존 WhatsApp 비즈니스 계정이 승인되었습니다.
- 기존 WhatsApp 비즈니스 계정의 **결제 설정**에 유효한 결제 수단이 있습니다.
- 비즈니스 전화번호의 2단계 인증이 해제되어 있습니다. WhatsApp 비즈니스 계정을 소유하고 있는 경우, WhatsApp 관리자에서 해당 번호에 대한 2단계 인증을 해제할 수 있습니다. 그렇지 않은 경우 솔루션 제공업체에 이 기능을 해제해 달라고 요청해야 합니다.

WhatsApp 전화번호 마이그레이션에 대한 자세한 내용은 [임베디드 가입을 통해 WhatsApp 비즈니스 계정 간에 전화번호 마이그레이션](https://developers.facebook.com/docs/whatsapp/business-management-api/guides/migrate-phone-to-different-waba/)에 대한 메타 설명서를 참조하세요.

## WhatsApp 휴대폰 번호 마이그레이션하기

1. WhatsApp 관리자에서 내 휴대폰 번호와 연결된 WhatsApp 비즈니스 계정(WABA)을 선택한 다음 **계정 도구** > **휴대폰 번호로** 이동합니다.
2. **2단계 인증 끄기를** 선택하고 다음 단계를 완료합니다.<br><br>![WhatsApp Business Manager opened to the "Phone numbers" page.]({% image_buster /assets/img/whatsapp/waba_manager.png %}){: style="max-width:80%;"} <br><br> 전화번호를 다른 WhatsApp 비즈니스 그룹으로 마이그레이션하는 경우 메타의 임베디드 가입에 표시 이름이 일치해야 하는 경우 **전화번호** 페이지에서 기존 표시 이름을 메모해 두세요. 다음 단계에서 해당 이름을 입력합니다.<br><br>![전화번호 옆에 표시 이름이 'Braze'로 표시된 WhatsApp 비즈니스 매니저의 전화번호 페이지(]({% image_buster /assets/img/whatsapp/phone_numbers.png %}){: style="max-width:80%;"}<br><br>
3. 메타의 임베디드 가입 워크플로우를 완료할 때까지 계속 진행하세요. 


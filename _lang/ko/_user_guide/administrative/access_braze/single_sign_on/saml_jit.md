---
nav_title: SAML Just-in-Time 프로비저닝
article_title: SAML Just-in-Time 프로비저닝
page_order: 1
page_type: tutorial
description: "이 문서에서는 새로운 대시보드 사용자가 처음 로그인할 때 Braze 계정을 생성할 수 있도록 SAML 즉시 프로비저닝을 구성하는 방법을 안내합니다." 

---

# SAML 즉시 프로비저닝 

> Just-in-time 프로비저닝은 [SAML SSO]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/set_up/)와 함께 작동하여 새로운 대시보드 사용자가 처음 로그인할 때 Braze 계정을 생성할 수 있도록 합니다. 따라서 관리자가 새 대시보드 사용자의 계정을 수동으로 만들고, 권한을 선택하고, 워크스페이스에 할당하고, 사용자가 계정을 활성화할 때까지 기다릴 필요가 없습니다.

## 필수 조건

이 기능은 SAML SSO가 설정되고 통합되어야 하며 Google SSO와 호환되지 않습니다.

## SAML 즉시 프로비저닝 설정

Braze 관리자에게 다음 작업을 수행하도록 하십시오:

1. **설정** > **보안 설정**로 이동합니다.
2. **SAML SSO** 섹션에서 **자동 사용자 프로비저닝** 옵션을 토글합니다.
3. 기본값 작업 공간을 선택하여 새 대시보드 사용자를 추가하십시오.
4. 새 대시보드 사용자에게 할당할 기본 권한 세트를 선택합니다. 사용자 권한 설정에 대해 알아보려면 [사용자 권한 설정]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/)을 참조하세요.
6. 페이지 하단에서 **저장 변경 사항**을 선택하십시오
7. SSO 제공자의 설정에서 Braze 액세스가 필요한 모든 사용자를 SSO 제공자의 디렉토리에 추가하세요.
8. 이제 사용자는 가입하거나 로그인할 수 있습니다.

---
nav_title: SAML 즉시 프로비저닝
article_title: SAML Just-in-Time 프로비저닝
page_order: 1
page_type: tutorial
description: "이 문서에서는 새로운 회사 사용자가 첫 로그인 시 Braze 계정을 생성할 수 있도록 SAML 즉시 프로비저닝을 구성하는 방법을 안내합니다." 

---

# SAML 즉시 프로비저닝 

> 즉시 프로비저닝은 [SAML SSO]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/set_up/)와 함께 작동하여 새로운 회사 사용자가 첫 로그인 시 Braze 계정을 생성할 수 있도록 합니다. 이로 인해 관리자가 새로운 회사 사용자를 위해 수동으로 계정을 생성하고, 권한을 선택하고, 작업 공간에 할당하고, 계정을 활성화할 때까지 기다릴 필요가 없습니다.

보안 조치로서, SAML 즉시 프로비저닝(JITP)은 이미 회사에 존재하는 이메일 도메인을 가진 사용자에게만 작동합니다. JITP는 회사에 이미 확인된 비가장 개발자가 최소한 한 명 이상 있는 도메인에서만 가능합니다. 

예를 들어, 계정 ```jon.smith@decorumsoft.com```이 JITP를 사용하여 Decorumsoft에 로그인할 수 있다고 가정해 보겠습니다. 계정 ```jane.smith@decorumsoft.com```는 동일한 도메인을 가지고 있으며 프로비저닝이 허용될 수 있습니다. 그러나 ```jon.smith@decorumsoft.eu```와 함께 JITP를 사용하려고 하면, Decorumsoft Braze 대시보드 내에 ```decorumsoft.eu``` 계정이 없기 때문에 프로비저닝이 허용되지 않습니다. 

회사를 위한 예외를 만들려면 [지원]({{site.baseurl}}/braze_support/)에 문의하십시오.

## 필수 조건

SAML JITP는 SAML SSO가 설정되고 통합되어야 합니다. Google SSO와 호환되지 않으며, Identity Provider Initiated (IdP-initiated) 로그인 워크플로우에 대해서만 지원됩니다.

## SAML 즉시 프로비저닝(JITP) 설정하기

Braze 관리자에게 다음 작업을 수행하도록 하십시오:

1. **설정** > **관리자 설정** > **보안 설정**으로 이동합니다.
2. **SAML SSO** 섹션에서 **자동 사용자 프로비저닝** 옵션을 토글합니다.
3. 새로운 회사 사용자를 추가할 기본 작업 공간을 선택합니다.
4. 그 새로운 회사 사용자에게 할당할 기본 권한 세트를 선택합니다. 사용자 권한 설정에 대해 알아보려면 [사용자 권한 설정]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/)을 참조하세요.
6. 페이지 하단에서 **저장 변경 사항**을 선택하십시오
7. SSO 제공자의 설정에서 Braze 액세스가 필요한 모든 사용자를 SSO 제공자의 디렉토리에 추가하세요.
8. 사용자에게 첫 로그인 시 IdP 포털을 통해 Braze에 접근하도록 지시합니다. 이후 SAML 단일 로그인 버튼이 향후 로그인 시 표시됩니다.

## Frequently asked questions

### SAML JITP를 비활성화하려면 어떻게 해야 하나요?

JITP를 설정한 후, 이를 끄기 위해 [지원에 연락해야 합니다.]({{site.baseurl}}/braze_support/)

## 문제 해결

### Microsoft Entra ID와 함께 단일 로그인 버튼이 나타나지 않습니다.

Braze의 Microsoft Entra **기본 SAML 구성** 양식에서 **로그인 URL** 필드는 사용자가 SSO 버튼이 아닌 비밀번호 옵션만 보게 할 수 있습니다. 이 문제를 방지하려면 Microsoft Entra 관리 센터에서 Braze를 구성할 때 **로그인 URL** 필드를 비워 두십시오.
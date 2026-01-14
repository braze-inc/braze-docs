---
nav_title: SAML Just-in-Time 프로비저닝
article_title: SAML 적시 프로비저닝
page_order: 1
page_type: tutorial
description: "이 문서에서는 새 대시보드 사용자가 처음 로그인할 때 Braze 계정을 만들 수 있도록 SAML 적시 프로비저닝을 구성하는 방법을 안내합니다." 

---

# SAML 적시 프로비저닝 

> 적시 프로비저닝은 [SAML SSO와]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/set_up/) 함께 작동하여 새로운 대시보드 사용자가 처음 로그인할 때 Braze 계정을 만들 수 있도록 합니다. 따라서 관리자가 새 대시보드 사용자의 계정을 수동으로 만들고, 권한을 선택하고, 워크스페이스에 할당하고, 사용자가 계정을 활성화할 때까지 기다릴 필요가 없습니다.

보안 조치로 SAML 적시 프로비저닝(JITP)은 회사에 이미 존재하는 이메일 도메인을 가진 사용자에 대해서만 작동합니다. JITP는 회사에 이미 확인된 가장이 아닌 개발자가 한 명 이상 있는 도메인에만 사용할 수 있습니다. 

예를 들어 ```jon.smith@decorumsoft.com``` 계정에서 JITP를 사용하여 Decorumsoft에 로그인할 수 있다고 가정해 보겠습니다. ```jane.smith@decorumsoft.com``` 계정은 동일한 도메인을 가지고 있으며 프로비저닝을 허용할 수도 있습니다. 그러나 ```jon.smith@decorumsoft.eu``` 로 JITP를 사용하려고 하면 Decorumsoft Braze 대시보드 내에 ```decorumsoft.eu``` 계정이 없기 때문에 프로비저닝이 허용되지 않습니다. 

회사에 예외를 적용하려면 [지원팀에]({{site.baseurl}}/braze_support/) 문의하세요.

## 전제 조건

SAML JITP를 사용하려면 SAML SSO를 설정하고 통합해야 합니다. Google SSO와 호환되지 않으며 IdP 시작(IdP 시작) 로그인 워크플로에만 지원됩니다.

## SAML 적시 프로비저닝(JITP) 설정하기

Braze 관리자에게 다음을 수행하도록 합니다:

1. **설정** > **관리자 설정** > **보안 설정으로** 이동합니다.
2. **SAML SSO** 섹션에서 **자동 사용자 프로비저닝** 옵션을 토글합니다.
3. 새 대시보드 사용자를 추가할 기본값 워크스페이스를 선택합니다.
4. 새 대시보드 사용자에게 할당할 기본값 권한 집합을 선택합니다. 권한 집합을 만드는 방법을 알아보려면 [사용자 권한 설정하기를]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/) 참조하세요.
6. 페이지 하단에서 **변경 사항 저장을** 선택합니다.
7. SSO 공급업체의 설정에서 Braze 액세스가 필요한 모든 사용자를 SSO 공급업체의 디렉터리에 추가합니다.
8. 이제 사용자가 가입하거나 로그인할 수 있습니다.

## 자주 묻는 질문

### SAML JITP를 비활성화하려면 어떻게 하나요?

JITP를 설정한 후에는 [지원팀에 문의하여]({{site.baseurl}}/braze_support/) 기능을 해제해야 합니다.

## 문제 해결

### Microsoft Entra ID에 단일 서명 버튼이 나타나지 않습니다.

Braze용 Microsoft Entra의 **기본 SAML 구성** 양식의 로그인 **URL** 필드에 IdP 시작 로그인 시 사용자에게 SSO 버튼이 아닌 비밀번호 옵션만 표시될 수 있습니다. 이 문제를 방지하려면 Microsoft Entra 관리 센터에서 Braze를 구성할 때 **로그인 URL** 필드를 비워 두세요.
---
nav_title: 계정에 접속하기
article_title: 계정에 접속하기
page_order: 0
page_type: reference
description: "이 문서에서는 Braze 계정을 만드는 방법, 액세스 권한을 부여받은 후 로그인하는 방법, 대시보드 접근 및 대시보드 성능 문제를 해결하는 방법에 대해 설명합니다."

---

# 계정에 접속하기

> 이 문서에서는 Braze 계정을 만드는 방법, 액세스 권한을 부여받은 후 로그인하는 방법, 대시보드 접근 및 대시보드 성능 문제를 해결하는 방법에 대해 설명합니다.

회사의 첫 번째 Braze 사용자이고 처음 로그인하는 경우, 계약 첫날에 이메일 확인 및 로그인을 요청하는 환영 이메일(`@alerts.braze.com`)을 받게 됩니다.

계정을 확인한 후 대시보드의 [회사 사용자]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/) 페이지에서 추가 사용자를 추가할 수 있습니다. 모든 사용자는 추가된 후 계정 확인을 요청하는 이메일을 받게 됩니다.

회사의 Braze 계정에서 첫 번째 사용자가 아닌 경우, 회사의 Braze 계정 관리자에게 연락하여 계정 생성을 요청하세요. 그러면 이메일 확인 및 로그인을 요청하는 환영 이메일(`@alerts.braze.com`)이 전송됩니다.

## 로그인

처음이든 수백만 번째이든, 로그인 방법에 대해 알아보겠습니다! 회사의 첫 번째 사용자라면 이전 섹션의 안내를 따르세요. 그렇지 않은 경우, 회사의 Braze 관리자가 계정을 생성한 후 로그인할 수 있습니다.

[Braze.com](https://www.braze.com) 홈 사이트에서 로그인하거나, 특정 [Braze 인스턴스]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints/)에 해당하는 대시보드 URL을 사용할 수 있습니다. 편의를 위해 Braze는 다음과 같은 여러 SSO(Single Sign-On) 옵션을 제공합니다:

* [SAML SSO]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/set_up/)
    * [SAML just-in-time provisioning]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/saml_jit/)
* [Microsoft Entra SSO]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/entra/)
* [Okta]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/okta/)
* [OneLogin]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/onelogin/)

{% alert note %}
SSO로 Braze에 로그인한 후에는 더 이상 비밀번호를 사용하여 대시보드에 로그인할 수 없습니다.
{% endalert %}

## 지원 브라우저

Braze 대시보드는 다음 브라우저를 지원합니다:
- Chrome (버전 87 이상)
- Firefox (버전 85 이상)
- Safari (버전 15.4 이상)
- Edge (버전 87 이상)

Braze 대시보드에서 예기치 않은 오류가 발생하고 브라우저 콘솔 도구에 `ReferenceError: structuredClone is not defined` 오류가 표시되면 브라우저가 오래된 것입니다. 이 오류가 계속 발생하면 브라우저를 제거한 후 다시 설치하세요.

## 여러 Braze 대시보드에 접근하기

Braze는 동일한 클러스터 내에서 동일한 이메일 주소를 여러 대시보드 사용자에게 등록하는 것을 허용하지 않습니다(예: US-01에 두 개의 대시보드가 있는 경우). 동일한 이메일로 서로 다른 클러스터에 계정을 생성할 수는 있습니다(예: US-01에 하나의 대시보드가 있고 US-05에 다른 대시보드가 있는 경우). 동일 클러스터 내 여러 Braze 대시보드에 접근해야 하는 경우 다음 방법을 사용할 수 있습니다:

### 이메일 별칭 사용

이메일 서비스가 Gmail인 경우, 이메일 주소에 `+` 기호 다음에 원하는 텍스트를 추가하여 별칭을 생성할 수 있습니다. 예를 들어:
- **원본 이메일:** `rocky@gmail.com`
- **별칭 이메일:** `rocky+1@gmail.com`

두 이메일 주소 모두 동일한 받은편지함으로 이메일을 전달하지만, Braze에 로그인할 때는 별개의 계정으로 인식됩니다.

### 다른 공급자에서 별도의 별칭 생성

이메일 제공업체가 `+` 별칭을 지원하지 않는 경우에도 별도의 별칭을 생성할 수 있습니다. 예를 들어 `rocky@braze.com`이 `rocky.lotito@braze.com`으로 전달되도록 설정할 수 있습니다. 이를 통해 여러 주소가 동일한 받은편지함으로 통합되면서도 Braze에서는 서로 다른 이메일로 인식됩니다.

### 다중 회사 개발자 활용

다중 회사 개발자 기능을 사용하면 단일 사용자 계정을 여러 회사에서 공유할 수 있습니다. 사용자는 고객 프로필 메뉴에서 서로 다른 회사 대시보드 간에 토글할 수 있습니다.

SSO를 사용 중이며 다중 회사 개발자를 설정하려면, 커스텀 SAML SSO 통합을 설정하여 SAML 커스텀 엔터티 ID를 활성화해야 합니다. [서비스 공급자(SP) 시작 로그인]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/set_up/) 단계를 따르되, 다음 변경 사항을 적용하세요:
- 각 대시보드 통합에 대해 **엔터티 ID**를 `braze_dashboard_<companyID>`로 변경하세요.
- 각 대시보드에 대한 `saml_sso_custom_entity_id` 기능 플리퍼를 활성화하려면 고객 성공 매니저 또는 계정 매니저에게 문의하세요.

### SSO(Single Sign-On) 고려 사항

SSO(Single Sign-On)를 사용하는 경우, 여러 개의 서로 다른 이메일 주소를 보유하면 문제가 발생할 수 있습니다. 접근 문제를 방지하려면 SSO 설정이 올바르게 구성되었는지 확인하세요.

## 문제 해결

### 비밀번호 재설정하기

비밀번호를 재설정하려면 대시보드 로그인 페이지에서 **비밀번호를 잊으셨나요?** 링크를 선택하세요. 비밀번호 재설정 링크를 받을 이메일을 입력하라는 메시지가 표시됩니다.

!["비밀번호를 잊으셨나요?" 메시지가 표시되는 대시보드 로그인]({% image_buster /assets/img_archive/enable_reset.png %}){: style="max-width:60%"}

### 브라우저 캐시 및 쿠키 삭제

대시보드 또는 세그먼트 성과 목록이 로드되지 않는 등 대시보드 성능에 문제가 있는 경우, 사용 중인 브라우저에 맞는 단계를 따라 브라우저 캐시와 쿠키를 삭제해 보세요.

{% alert important %}
쿠키를 삭제하면 로그아웃되므로 저장하지 않은 작업이 손실됩니다.
{% endalert %}

- [Chrome에서 캐시 및 쿠키 삭제](https://support.google.com/accounts/answer/32050?hl=en&co=GENIE.Platform%3DDesktop)
- [Mac의 Safari에서 쿠키 삭제](https://support.apple.com/en-gb/guide/safari/sfri11471/16.1/mac/13.0)
- [Firefox에서 쿠키 및 사이트 데이터 삭제](https://support.mozilla.org/en-US/kb/clear-cookies-and-site-data-firefox)
- [Microsoft Edge에서 모든 쿠키 삭제](https://support.microsoft.com/en-us/windows/manage-cookies-in-microsoft-edge-view-allow-block-delete-and-use-168dab11-0753-043d-7c16-ede5947fc64d#bkmk_deleteallcookies)

브라우저 캐시와 쿠키를 삭제해도 문제가 해결되지 않으면 [고객지원]({{site.baseurl}}/support_contact/)에 문의하세요.

### 대시보드 탐색 중 "페이지를 새로고침하세요" 또는 "예기치 않은 오류" 발생

이 오류는 회사 사용자가 어떤 워크스페이스에도 속하지 않은 경우 나타날 수 있습니다. 문제를 해결하려면:

1. [회사 사용자]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/) 페이지로 이동합니다.
2. 해당 사용자가 워크스페이스에 추가되었는지 확인합니다.
3. 어떤 워크스페이스에도 속하지 않은 경우, 사용자를 추가하고 적절한 권한을 할당합니다.
4. 사용자에게 대시보드를 새로고침하도록 요청합니다.
5. 문제가 지속되면 [고객지원]({{site.baseurl}}/support_contact/)에 문의하세요.

### 드래그 앤 드롭 편집기 접근

대부분의 회사 사용자에게는 드래그 앤 드롭 편집기가 정상적으로 로드됩니다. 그러나 VPN을 사용하거나 방화벽 뒤에 있는 경우 도메인을 허용 목록에 추가해야 할 수 있습니다. IT 관리자에게 `*.bz-rndr.com`이 허용 목록에 추가되었는지 확인하도록 문의하세요.

편집기는 다음과 같은 이유로 로딩 문제가 발생할 수 있습니다:

- **일시적 오류:** 연결, 통신 또는 데이터 전송에 영향을 줄 수 있는 일시적인 장애입니다. 다행히 이러한 오류는 일반적으로 단기적인 조건에 의해 발생하며 시스템적 문제를 나타내지 않으므로, 별도의 조치 없이 자체적으로 해결되는 경우가 많습니다.
- **주요 오류:** 기본 인프라 또는 제품 문제가 관련될 수 있습니다. [Braze 시스템 상태 페이지](https://braze.statuspage.io/)를 확인하세요. 저희가 이미 상황을 인지하고 적극적으로 해결에 나서고 있을 가능성이 높습니다.

{% alert important %}
여전히 문제가 발생하는 경우 [지원 티켓을 열어주세요]({{site.baseurl}}/user_guide/administrative/access_braze/support/). 그 전에 IT 관리자가 `*.bz-rndr.com`이 허용 목록에 추가되었는지 확인해 주세요.
{% endalert %}

### Braze Learning에 접근하기

Braze Learning에 로그인하는 데 문제가 발생하고 대시보드로 계속 리디렉션되는 루프에 갇힌 경우 다음 단계를 수행하세요:

1. 여러 개의 Braze 계정이 있는 경우, 잘못된 계정으로 두 번 로그인하면 Braze 대시보드로 이동됩니다. 올바른 계정으로 로그인하고 있는지 확인하세요. 
2. 광고 차단기가 설치되어 있다면, 꺼져 있는지 확인하세요. SSO 기능에 필요한 쿠키를 차단할 수 있습니다.
3. 회사 설정 > 보안 설정으로 이동하여 SSO(Single Sign-On)가 활성화되어 있는지 확인하세요.
4. 대시보드 고객 프로필에 이름과 성이 모두 포함되어 있는지 확인하세요. 성(姓)이 없으면 로그인 과정에 문제가 발생할 수 있습니다.
5. 대시보드에서 **고객지원** > **Braze Learning**으로 이동하여 Braze Learning에 접근하세요. 
6. 문제가 계속 발생할 경우 계정을 다시 생성해 보시기 바랍니다. 무료 체험 기간 동안 Braze Learning에 접속했던 사용자는 현재 접속에 어려움을 겪을 수 있습니다.

### 2단계 인증(2FA) 문제

사용자가 2단계 인증(2FA) 문제로 Braze 대시보드에 접근할 수 없는 경우, 여러 가지 원인이 있을 수 있습니다. 가장 흔한 경우는 등록된 전화번호나 Authy 앱이 설치된 기기에 더 이상 접근할 수 없게 된 것입니다.

관리자는 다음 단계를 수행하여 해당 사용자의 2단계 인증을 재설정해야 합니다: 

1. **사용자 관리**로 이동하세요.
2. 2단계 인증 문제를 겪고 있는 사용자에 대해 **사용자 편집**을 선택하세요.
3. 2단계 인증 재설정 옵션을 선택하세요.
4. 메시지가 표시되면 2단계 인증 재설정을 확인하세요.
5. 재설정으로 문제가 즉시 해결되지 않으면 쿠키와 캐시를 삭제하세요.

보안상의 이유로 Braze는 사용자를 대신하여 2단계 인증을 재설정할 수 없습니다. 따라서 관리자가 2단계 인증을 재설정할 수 없는 경우 지원 티켓을 생성하세요.

#### 고려 사항

- 회사 차원에서 2단계 인증이 적용되는 경우: 재설정 후, Braze는 사용자가 다음에 로그인할 때 2단계 인증을 다시 설정하도록 안내합니다.
- 회사 차원에서 2단계 인증이 의무화되지 않은 경우: 사용자는 2단계 인증을 다시 설정할 필요 없이 대시보드에 로그인할 수 있습니다. 2단계 인증을 활성화하려면 계정 설정에서 설정할 수 있습니다.

{% alert note %}
이 재설정 절차는 지난 1시간 동안 너무 많은 토큰을 요청하여 계정이 잠긴 사용자에게도 적용됩니다.
{% endalert %}
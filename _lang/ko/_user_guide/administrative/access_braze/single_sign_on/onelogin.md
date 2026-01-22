---
nav_title: OneLogin
article_title: OneLogin
page_order: 5
page_type: tutorial
description: "이 문서에서는 통합 인증에 OneLogin을 사용하도록 Braze를 구성하는 방법을 안내합니다."

---

# OneLogin

> [OneLogin은](https://www.onelogin.com/) 사용자 ID 관리를 위한 종합적인 솔루션을 제공하는 클라우드 ID 플랫폼입니다. OneLogin은 싱글 사인온(SSO), 사용자 프로비저닝, 다단계 인증 등을 위해 SAML 2.0을 사용하여 클라우드 및 온프레미스 애플리케이션과 통합됩니다.

## 요구 사항

설정 시 로그인 URL과 ACS(어설션 소비자 서비스) URL을 입력하라는 메시지가 표시됩니다.  

| 요구 사항 | 세부 정보 |
|---|---|
| Braze 도메인 | 원로그인 내에서 Braze를 설정하려면 Braze 도메인이 필요합니다. 인스턴스가 `US-01` 인 경우 대시보드 URL을 원로그인 대시보드에 입력해야 합니다. <br><br> 예를 들어 대시보드 URL이 `https://dashboard-01.braze.com` 인 경우 `dashboard-01.braze.com` 을 입력해야 합니다.  |
| 릴레이스테이트 API 키 | IdP 로그인을 인에이블먼트하려면 **설정** > **API 키로** 이동하여 `sso.saml.login` 권한으로 API 키를 만듭니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 원로그인 내 IdP 시작 로그인

### 1단계: Braze 앱 구성하기

1. [원로그인에](https://app.onelogin.com/login) 로그인합니다. **관리를** 클릭합니다.!\![원로그인 관리 페이지]를 클릭합니다.]({% image_buster /assets/img/onelogin_1.jpg %})<br><br>
2. 상단 탐색 모음에서 **앱** > **앱 추가로** 이동합니다. "Braze"를 검색하고 Braze 앱을 선택합니다.!\![원로그인에서 Braze 검색 결과.]({% image_buster /assets/img/onelogin_2.jpg %})<br><br>
3. Braze 앱을 회사에 저장하세요.!\![]({% image_buster /assets/img/onelogin_3.jpg %})<br><br>
4. 저장되면 **구성으로** 이동하여 Braze **도메인** 및 **RelayState** API 키를 추가합니다.!\![Braze 앱의 OneLogin 구성 탭].]({% image_buster /assets/img/onelogin_4.png %})<br><br>
5. Braze는 [특정 형식의]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/set_up/#configure-your-identity-provider) SAML 어설션을 기대합니다. **매개변수** 아래에는 Braze가 지원하는 속성이 미리 입력되어 있어야 합니다. 올바른지 확인합니다.!\![OneLogin에서 SAML 매개변수를 Braze합니다.]({% image_buster /assets/img/onelogin_5.jpg %})<br><br>
6. **SSO** 탭 아래에서 Braze 대시보드 설정에 필요한 **인증서와** **SAML 2.0 엔드포인트(HTTP)** 를 복사합니다.!\![OneLogin의 Braze 앱 SSO 탭에서 복사할 인증서.]({% image_buster /assets/img/onelogin_6.jpg %})

### 2단계: Braze 내에서 OneLogin 구성하기

원로그인 내에서 Braze를 설정하면 타겟팅 URL(`SAML 2.0 Endpoint (HTTP)`)과 `x.509` 인증서가 제공되며, 이를 Braze 계정에 입력하면 됩니다.

계정 매니저가 계정에 대해 SAML SSO를 인에이블한 후 **설정** > **관리자 설정** > **보안 설정으로** 이동하여 SAML SSO 섹션을 **켜기로** 토글합니다.

이 페이지에서 다음을 입력합니다:

| 요구 사항 | 세부 정보 |
|---|---|
| `SAML Name` | 로그인 화면의 버튼 텍스트로 표시됩니다. 일반적으로 'OneLogin'과 같은 ID 공급자의 이름입니다. |
| `Target URL` | 원로그인에서 제공하는 `SAML 2.0 Endpoint (HTTP)` URL입니다.|
| `Certificate` | `x.509` PEM 인코딩된 인증서는 원로그인에서 제공합니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

토글이 선택된 SAML SSO 설정.]({% image_buster /assets/img/samlsso.png %})

{% alert tip %}
Braze 계정 사용자가 SAML SSO로만 로그인하도록 하려면 **회사 설정** 페이지에서 [통합 인증을 제한할]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/set_up/#restriction) 수 있습니다.
{% endalert %}


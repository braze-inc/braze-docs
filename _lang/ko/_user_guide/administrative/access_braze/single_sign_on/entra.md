---
nav_title: Microsoft Entra SSO
article_title: Microsoft Entra SSO
page_order: 3
page_type: tutorial
description: "이 문서에서는 Microsoft Entra 단일 로그인 기능을 Braze와 설정하는 방법을 안내합니다."

---

# Microsoft Entra SSO

> [Microsoft Entra SSO](https://learn.microsoft.com/en-us/entra/identity/saas-apps/braze-tutorial)는 Microsoft의 클라우드 기반 아이덴티티 및 액세스 관리 서비스로, 직원들이 로그인하고 리소스에 접근할 수 있도록 도와줍니다. 비즈니스 요구 사항에 따라 Entra SSO를 사용하여 앱 및 앱 리소스에 대한 액세스를 제어할 수 있습니다.

## 요구 사항

설정 후, Assertion Consumer Service (ACS) URL을 제공하라는 요청을 받게 됩니다.  

| Requirement | 세부 정보 |
|---|---|
| 어설션 소비자 서비스(ACS) URL | `https://<SUBDOMAIN>.braze.com/auth/saml/callback` <br> 일부 ID 공급자의 경우 이를 회신 URL, 오디언스 URL 또는 오디언스 URI라고도 합니다. |
| 엔티티 ID | `braze_dashboard`|
| RelayState API 키 | ID 공급자 로그인을 사용 **설정하려면 설정** > **API 키**로 이동하여 `sso.saml.login` 권한으로 API 키를 만듭니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Microsoft Entra SSO 내에서 서비스 제공자(SP) 주도 로그인

### 1단계: 갤러리에서 Braze 추가하기

1. Microsoft Entra 관리 센터에서 **Identity** > **Applications** > **Enterprise Applications**로 이동한 다음 **New application**을 선택합니다.
2. 검색 상자에서 **Braze**를 검색하고 결과 패널에서 선택한 다음 **Add**를 선택합니다.

### 2단계: Microsoft Entra SSO 구성

1. Microsoft Entra 관리 센터에서 Braze 애플리케이션 통합 페이지로 이동하여 **Single sign-on**을 선택합니다.
2. **Select a single sign-on method** 페이지에서 **SAML**을 방법으로 선택합니다.
3. **Set up Single Sign-On with SAML** 페이지에서 **Basic SAML Configuration**의 편집 아이콘을 선택합니다.
4. [Braze 인스턴스]({{site.baseurl}}/user_guide/administrative/access_braze/braze_instances/#braze-instances)와 `https://<SUBDOMAIN>.braze.com/auth/saml/callback` 패턴을 결합하는 **응답 URL**을 입력하여 IdP 시작 모드에서 애플리케이션을 구성합니다.
5. RelayState를 구성하려면 생성된 API 키를 **Relay State** 필드에 입력합니다.

{% alert important %}
**Do not** **Sign-On URL** 필드를 설정하지 마십시오. IdP 주도 SAML SSO와의 문제를 방지하기 위해 이 필드를 비워 두십시오.
{% endalert %}

{: start="6"}
6\. Braze에서 예상하는 특정 형식으로 SAML 어설션 형식을 지정합니다. 커스텀 및 사용자 클레임에 대한 다음 탭을 참조하여 이러한 속성 및 값의 형식을 지정하는 방법을 이해하세요.

{% tabs %}
{% tab User Attributes %}
**애플리케이션 통합** 페이지의 **사용자 속성** 섹션에서 이러한 속성 값을 관리할 수 있습니다.

다음 속성 페어링을 사용합니다:

- `givenname` = `user.givenname`
- `surname`= `user.surname`
- `emailaddress` = `user.mail`
- `name` = `user.userprincipalname`
- `email` = `user.userprincipalname`
- `first_name` = `user.givenname`
- `last_name` = `user.surname`
- `Unique User Identifier` = `user.userprincipalname`

{% alert important %}
이메일 필드가 Braze에서 사용자를 위해 설정된 것과 일치하는 것이 매우 중요합니다. 대부분의 경우 `user.userprincipalname` 과 동일하지만, 구성이 다른 경우에는 시스템 관리자와 협력하여 이러한 필드가 정확히 일치하는지 확인하세요.
{% endalert %}

{% endtab %}
{% tab User Claims %}

**SAML을 사용한 통합 인증 설정** 페이지에서 **편집을** 선택하여 **사용자 속성** 대화 상자를 엽니다. 그런 다음 적절한 형식에 따라 사용자 클레임을 편집합니다.

다음 클레임 이름 쌍을 사용합니다:

- `claims/givenname` = `user.givenname`
- `claims/surname` = `user.surname`
- `claims/emailaddress` = `user.userprincipalname`
- `claims/name` = `user.userprincipalname`
- `claims/nameidentifier` = `user.userprincipalname`

{% alert important %}
이메일 필드가 Braze에서 사용자를 위해 설정된 것과 일치하는 것이 매우 중요합니다. 대부분의 경우 `user.userprincipalname` 과 동일하지만, 구성이 다른 경우에는 시스템 관리자와 협력하여 이러한 필드가 정확히 일치하는지 확인하세요.
{% endalert %}

이러한 사용자 클레임 및 값은 **클레임 관리** 섹션에서 관리할 수 있습니다.

{% endtab %}
{% endtabs %}

{: start="8"}
8\. **SAML을 사용한 SSO 설정**으로 이동한 다음 **SAML 서명 인증서** 섹션으로 스크롤하여 요구 사항에 따라 적절한 **인증서(Base64)** 를 다운로드합니다.
9\. **Braze 설정** 섹션으로 이동하여 [Braze 구성](#step-3)에 사용할 적절한 URL을 복사합니다.

### 3단계: Braze 내에서 Microsoft Entra SSO 구성 {#step-3}

Microsoft Entra 관리 센터 내에서 Braze를 설정한 후, Microsoft Entra는 대상 URL(로그인 URL)과 **x.509** 인증서를 제공하며, 이를 Braze 계정에 입력합니다.

계정 매니저가 계정에 대해 SAML SSO를 사용 설정한 후 다음을 수행합니다.

1. **설정** > **관리자 설정** > **보안 설정으로** 이동하여 SAML SSO 섹션을 **켜기로** 전환합니다.
2. 같은 페이지에서 다음을 추가합니다:

| 요구 사항 | 세부 정보 |
|---|---|
| `SAML Name` | 이것은 로그인 화면에 버튼 텍스트로 나타납니다. 이는 일반적으로 "Microsoft Entra"와 같은 귀하의 아이덴티티 제공자의 이름입니다. |
| `Target URL` | 이는 Microsoft Entra에서 제공하는 로그인 URL입니다.|
| `Certificate` | `x.509` PEM 인코딩 인증서는 ID 공급업체에서 제공합니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert tip %}
Braze 계정 사용자가 SAML SSO로만 로그인하도록 하려면 **회사 설정** 페이지에서 [SSO 인증을 제한할]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/set_up/#restriction) 수 있습니다.
{% endalert %}

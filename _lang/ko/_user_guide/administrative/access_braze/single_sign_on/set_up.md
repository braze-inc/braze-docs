---
nav_title: SAML SSO 설정
article_title: SAML SSO 설정
page_order: 0
page_type: tutorial
description: "이 문서에서는 Braze 계정에 SAML SSO을 활성화하는 방법을 안내합니다."

---

# 서비스 공급자(SP)가 로그인 시작

> 이 문서에서는 Braze 계정에 SAML 싱글 사인온을 활성화하는 방법과 SAML 추적을 얻는 방법을 안내합니다.

## 요구 사항

설정 시 로그인 URL과 ACS(어설션 소비자 서비스) URL을 입력하라는 메시지가 표시됩니다.  

| 요구 사항 | 세부 정보 |
|---|---|
| 어설션 소비자 서비스(ACS) URL | `https://<SUBDOMAIN>.braze.com/auth/saml/callback` <br><br> 유럽 연합 도메인의 경우 ASC URL은 `https://<SUBDOMAIN>.braze.eu/auth/saml/callback` 입니다. <br><br> 일부 IdP의 경우 이를 회신 URL, 로그인 URL, 오디언스 URL 또는 오디언스 URI라고도 합니다. |
| 엔티티 ID | `braze_dashboard` |
| RelayState API 키 | **설정** > **API 키**로 이동하여 `sso.saml.login` 권한으로 API 키를 생성한 다음 생성된 API 키를 IdP 내에서 `RelayState` 매개변수로 입력합니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert note %}
[이전 탐색]({{site.baseurl}}/navigation)을 사용하는 경우 **설정**에서 **개발자 콘솔** > **API 설정** 아래에 API 키를 찾을 수 있습니다.
{% endalert %}

## SAML SSO 설정

### 1단계: ID 공급자 구성

다음 정보를 사용하여 ID 공급자(IdP)에서 Braze를 서비스 공급자(SP)로 설정하세요. 또한 SAML 속성 매핑을 설정합니다.

{% alert important %}
Okta를 ID 제공업체로 사용하려는 경우 [Okta 사이트](https://www.okta.com/integrations/braze/)에서 미리 구축된 통합 기능을 사용해야 합니다.
{% endalert %}

| SAML 속성 | 필수 사항인가요? | 허용되는 SAML 속성 |
|---|---|---|
|`email` | 필수 | `email` <br> `mail` <br> `http://schemas.xmlsoap.org/ws/2005/05/identity/claims/email` |
| `first_name` | 선택 사항 | `first_name` <br> `firstname` <br> `firstName`<br>`http://schemas.xmlsoap.org/ws/2005/05/identity/claims/first_name` |
| `last_name` | 선택 사항 | `last_name` <br> `lastname` <br> `lastName` <br>`http://schemas.xmlsoap.org/ws/2005/05/identity/claims/last_name` |

{% alert note %}
Braze는 SAML 어설션에 `email`만 필요합니다.
{% endalert %}

### 2단계: Braze 구성

ID 제공업체에서 Braze 설정을 완료하면, ID 공급업체에서 Braze 계정에 입력할 대상 URL과 `x.509` 인증서를 제공합니다.

계정 매니저가 계정에 대해 SAML SSO를 켜면 **설정** > **관리자** > **보안 설정**으로 이동하여 SAML SSO 섹션을 **켜기**로 전환합니다.

{% alert note %}
[이전 탐색]({{site.baseurl}}/navigation)을 사용하는 경우 계정 아이콘을 선택하고 **회사 설정** > **보안 설정**으로 이동하여 SAML SSO 섹션을 찾으십시오.
{% endalert %}

같은 페이지에서 다음을 입력합니다:

| 요구 사항 | 세부 정보 |
|---|---|
| `SAML Name` | 로그인 화면의 버튼 텍스트에 표시됩니다.<br>일반적으로 "Okta"와 같은 ID 공급자의 이름입니다. |
| `Target URL` | 이는 IdP 내에서 Braze를 설정한 후에 제공됩니다.<br> 일부 IdP는 이를 SSO URL 또는 SAML 2.0 엔드포인트로 참조합니다. |
| `Certificate` | ID 공급업체에서 제공하는 `x.509` 인증서입니다.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

대시보드에 인증서를 추가할 때 `x.509` 인증서가 이 형식을 따르는지 확인하세요:

```
-----BEGIN CERTIFICATE-----
<certificate>
-----END CERTIFICATE-----
```

![보안 설정 열기 및 SAML SSO 세부 정보 추가]({% image_buster /assets/img/samlsso.gif %})

### 3단계: Braze에 로그인

보안 설정을 저장하고 로그아웃합니다. 그런 다음 ID 공급업체를 통해 다시 로그인합니다.

![SSO가 활성화된 대시보드 로그인 화면]({% image_buster /assets/img/sso1.png %}){: style="max-width:40%;"}

## SSO 동작

SSO를 사용하기로 선택한 회원은 더 이상 이전처럼 비밀번호를 사용할 수 없습니다. 다음 설정에 의해 제한되지 않는 한 비밀번호를 계속 사용하는 사용자는 비밀번호를 사용할 수 있습니다.

## 제한 사항

조직의 구성원이 Google SSO 또는 SAML SSO로만 로그인하도록 제한할 수 있습니다. 제한을 사용 설정하려면 **보안 설정**으로 이동하여 **Google SSO 전용 로그인 적용** 또는 **커스텀 SAML SSO 전용 로그인 적용**을 선택합니다.

![보안 설정 페이지의 인증 규칙 섹션]({% image_buster /assets/img/sso3.png %})

제한을 설정하면 이전에 비밀번호로 로그인한 적이 있더라도 회사의 Braze 사용자는 더 이상 비밀번호를 사용하여 로그인할 수 없게 됩니다.

## SAML 추적 얻기

SSO와 관련된 로그인 문제가 발생하는 경우 SAML 추적을 받으면 SAML 요청에서 전송된 내용을 파악하여 SSO 연결 문제를 해결하는 데 도움이 될 수 있습니다.

### 필수 조건

SAML 추적을 실행하려면 SAML 추적기가 필요합니다. 다음은 브라우저에 따라 가능한 두 가지 옵션입니다:

- [Google Chrome](https://chromewebstore.google.com/detail/saml-tracer/mpdajninpobndbfcldcmbpnnbhibjmch)
- [Mozilla Firefox](https://addons.mozilla.org/en-US/firefox/addon/saml-tracer/)

### 1단계: SAML 추적기 열기

브라우저 탐색 모음에서 SAML 추적기를 선택합니다. **일시 중지를** 선택하지 않으면 SAML 추적기가 SAML 요청에서 전송된 내용을 캡처할 수 없으므로 반드시 일시 중지를 선택하지 마세요. SAML 추적기가 열리면 추적이 채워지는 것을 볼 수 있습니다.

![]({% image_buster /assets/img/saml_tracer_example.png %})

### 2단계: SSO를 사용하여 Braze에 로그인

Braze 대시보드로 이동하여 SSO를 사용하여 로그인을 시도합니다. 오류가 발생하면 SAML 추적기를 열고 다시 시도하세요. `https://dashboard-XX.braze.com/auth/saml/callback` 같은 URL과 주황색 SAML 태그가 있는 행이 있으면 SAML 추적이 성공적으로 수집된 것입니다.

### 3단계: 내보내기 및 Braze로 보내기

**내보내기를** 선택합니다. **쿠키 필터 프로필 선택에서** **없음을** 선택합니다. 그런 다음 **내보내기를** 선택합니다. 이렇게 하면 추가 문제 해결을 위해 Braze 지원팀에 보낼 수 있는 JSON 파일이 생성됩니다.

!["SAML 추적 환경설정 내보내기" 메뉴에서 "없음" 옵션을 선택합니다.]({% image_buster /assets/img/export_saml_trace_preferences.png %})

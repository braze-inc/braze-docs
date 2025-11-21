---
nav_title: SAML SSO 설정
article_title: SAML SSO 설정
page_order: 0
page_type: tutorial
description: "이 글에서는 Braze 계정에 SAML 싱글 사인온을 인에이블먼트하는 방법을 안내합니다."

---

# 서비스 공급자(SP) 로그인 시작

> 이 도움말에서는 Braze 계정에 SAML 싱글 사인온을 인에이블먼트하는 방법과 SAML 추적을 얻는 방법을 안내합니다.

## 요구 사항

설정 시 로그인 URL과 ACS(어설션 소비자 서비스) URL을 입력하라는 메시지가 표시됩니다.  

| 요구 사항 | 세부 정보 |
|---|---|
| 어설션 소비자 서비스(ACS) URL | `https://<SUBDOMAIN>.braze.com/auth/saml/callback` <br><br> 유럽 연합 도메인의 경우 ASC URL은 `https://<SUBDOMAIN>.braze.eu/auth/saml/callback` 입니다. <br><br> 일부 IdP의 경우 이를 회신 URL, 로그인 URL, 오디언스 URL 또는 오디언스 URI라고도 합니다. |
| 엔티티 ID | `braze_dashboard` |
| 릴레이스테이트 API 키 | **설정** > **API 키로** 이동하여 `sso.saml.login` 권한으로 API 키를 생성한 다음 생성된 API 키를 IdP 내에서 `RelayState` 파라미터로 입력합니다. 자세한 단계는 [릴레이 상태 설정을](#setting-up-your-relaystate) 참조하세요. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## SAML SSO 설정하기

### 1단계: ID 공급자 구성

다음 정보를 사용하여 ID 공급자(IdP)에서 Braze를 서비스 공급자(SP)로 설정하세요. 또한 SAML 속성 매핑을 설정합니다.

{% alert important %}
Okta를 ID 공급업체로 사용하려는 경우 [Okta 사이트에서](https://www.okta.com/integrations/braze/) 미리 구축된 통합 기능을 사용해야 합니다.
{% endalert %}

| SAML 속성 | 필수 사항인가요? | 허용된 SAML 속성 |
|---|---|---|
|`email` | 필수 | `email` <br> `mail` <br> `http://schemas.xmlsoap.org/ws/2005/05/identity/claims/email` |
| `first_name` | 선택 사항 | `first_name` <br> `firstname` <br> `firstName`<br>`http://schemas.xmlsoap.org/ws/2005/05/identity/claims/first_name` |
| `last_name` | 선택 사항 | `last_name` <br> `lastname` <br> `lastName` <br>`http://schemas.xmlsoap.org/ws/2005/05/identity/claims/last_name` |

{% alert note %}
Braze는 SAML 어설션에 `email` 만 필요합니다.
{% endalert %}

### 2단계: Braze 구성하기

ID 공급업체에서 Braze 설정을 완료하면 ID 공급업체에서 타겟팅 URL과 `x.509` 인증서를 제공하여 Braze 계정에 입력할 수 있습니다.

계정 매니저가 계정에 대해 SAML SSO를 켜면 **설정** > **관리자 설정** > **보안 설정으로** 이동하여 SAML SSO 섹션을 **켜짐으로** 토글합니다.

같은 페이지에서 다음을 입력합니다:

| 요구 사항 | 세부 정보 |
|---|---|
| SAML 이름 | 로그인 화면의 버튼 텍스트로 표시됩니다.<br>일반적으로 "Okta"와 같은 ID 공급자의 이름입니다. |
| 타겟팅 URL | 이 기능은 IdP 내에서 Braze를 설정한 후에 제공됩니다.<br> 일부 IdP는 이를 SSO URL 또는 SAML 2.0 엔드포인트라고 합니다. |
| 인증서 | ID 공급업체에서 제공하는 `x.509` 인증서입니다.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

`x.509` 인증서를 대시보드에 추가할 때 이 형식을 따르는지 확인하세요:

```
-----BEGIN CERTIFICATE-----
<certificate>
-----END CERTIFICATE-----
```

토글이 선택된 SAML SSO 설정.]({% image_buster /assets/img/samlsso.png %})

### 3단계: Braze에 로그인하기

보안 설정을 저장하고 로그아웃합니다. 그런 다음 ID 공급업체를 통해 다시 로그인합니다.

\![SSO가 인에이블된 대시보드 로그인 화면]({% image_buster /assets/img/sso1.png %}){: style="max-width:60%;"}

## 릴레이 상태 설정

1. Braze에서 **설정** > **API 및 식별자로** 이동합니다.
2. **API 키** 탭에서 **API 키 만들기** 버튼을 선택합니다.
3. **API 키 이름** 필드에 키의 이름을 입력합니다.
4. **권한에서** **SSO** 드롭다운을 확장하고 **sso.saml.login**.<br><br>sso.saml.login 이 체크되어 있는 '권한' 섹션.]({% image_buster /assets/img/relaystate_troubleshoot.png %}){: style="max-width:70%;"}<br><br>
5. **API 키 생성을** 선택합니다.
6. **API 키** 탭에서 생성한 API 키 옆에 있는 식별자를 복사합니다.
7. 릴레이 상태 API 키를 IdP의 릴레이 상태에 붙여넣습니다(IdP에 따라 "릴레이 상태" 또는 "기본값 릴레이 상태"로 표시될 수도 있습니다).

## SSO 동작

SSO 사용을 옵트인한 회원은 더 이상 이전처럼 비밀번호를 사용할 수 없게 됩니다. 다음 설정에 의해 제한되지 않는 한 비밀번호를 계속 사용하는 사용자는 비밀번호를 사용할 수 있습니다.

## 제한 사항

조직의 구성원이 Google SSO 또는 SAML SSO로만 로그인하도록 제한할 수 있습니다. 제한을 사용 설정하려면 **보안 설정으로** 이동하여 **Google SSO 전용 로그인 적용** 또는 **커스텀 SAML SSO 전용 로그인 적용** 중 하나를 선택합니다.

비밀번호 길이 최소 8자, 비밀번호 재사용 횟수 3회인 '인증 규칙' 섹션 설정 예시입니다. 비밀번호는 180일 후에 만료되며, 사용자는 1,440분 동안 활동이 없으면 로그아웃됩니다.]({% image_buster /assets/img/sso3.png %})

제한을 설정하면 이전에 비밀번호로 로그인한 적이 있더라도 회사의 Braze 사용자는 더 이상 비밀번호를 사용하여 로그인할 수 없게 됩니다.

## SAML 추적 얻기

SSO와 관련된 로그인 문제가 발생하는 경우 SAML 추적을 확보하면 SAML 요청에서 전송된 내용을 식별하여 SSO 연결 문제 해결에 도움이 될 수 있습니다.

### 전제 조건

SAML 추적을 실행하려면 SAML 추적기가 필요합니다. 다음은 브라우저에 따라 가능한 두 가지 옵션입니다:

- [Google 크롬](https://chromewebstore.google.com/detail/saml-tracer/mpdajninpobndbfcldcmbpnnbhibjmch)
- [Mozilla Firefox](https://addons.mozilla.org/en-US/firefox/addon/saml-tracer/)

### 1단계: SAML 추적기 열기

브라우저의 탐색 모음에서 SAML 추적기를 선택합니다. **일시 중지를** 선택하지 않으면 SAML 추적기가 SAML 요청에서 전송된 내용을 캡처할 수 없으므로 반드시 선택하지 마세요. SAML 추적기가 열리면 추적이 채워지는 것을 볼 수 있습니다.

구글 크롬용 SAML 추적기.]({% image_buster /assets/img/saml_tracer_example.png %})

### 2단계: SSO를 사용하여 Braze에 로그인하기

Braze 대시보드로 이동하여 SSO를 사용하여 로그인을 시도합니다. 오류가 발생하면 SAML 추적기를 열고 다시 시도하세요. `https://dashboard-XX.braze.com/auth/saml/callback` 같은 URL과 주황색 SAML 태그가 있는 행이 있으면 SAML 추적이 성공적으로 수집된 것입니다.

### 3단계: Braze로 내보내기 및 보내기

**내보내기를** 선택합니다. **쿠키 필터 프로필 선택에서** **없음을** 선택합니다. 그런 다음 **내보내기를** 선택합니다. 그러면 추가 문제 해결을 위해 Braze 지원팀에 보낼 수 있는 JSON 파일이 생성됩니다.

"없음" 옵션이 선택된 "SAML 추적 환경설정 내보내기" 메뉴.]({% image_buster /assets/img/export_saml_trace_preferences.png %})

## 문제 해결

### 사용자의 이메일 주소가 올바르게 설정되어 있나요?

`ERROR_CODE_SSO_INVALID_EMAIL` 라는 오류가 표시되는 경우 사용자의 이메일 주소가 유효하지 않습니다. SAML 추적에서 `saml2:Attribute Name="email"` 필드가 사용자가 로그인에 사용하는 이메일 주소와 일치하는지 확인합니다. Microsoft Entra ID(이전의 Azure 액티브 디렉토리)를 사용하는 경우, 속성 매핑은 `email = user.userprincipalname` 입니다.

이메일 주소는 대소문자를 구분하며, ID 공급자(예: Okta, OneLogin, Microsoft Entra ID 등)에 설정된 주소를 포함하여 Braze에서 설정한 주소와 정확히 일치해야 합니다.

사용자의 이메일 주소에 문제가 있음을 나타내는 다른 오류로는 다음과 같은 것들이 있습니다:
- `ERROR_CODE_SSO_EMAIL_DOES_NOT_EXIST`: 사용자의 이메일 주소가 대시보드에 없습니다.
- `ERROR_CODE_SSO_SESSION_SIGN_IN_EMAIL_MISSING`: 사용자의 이메일 주소가 비어 있거나 잘못 구성되었습니다.
- `ERROR_CODE_SSO_SESSION_SIGN_IN_EMAIL_MISMATCH` 또는 `ERROR_CODE_SSO_SIGN_IN_EMAIL_MISMATCH`: 사용자의 이메일 주소가 SSO 설정에 사용된 이메일 주소와 일치하지 않습니다.

### 유효한 SAML 인증서(x.509 인증서)가 있으신가요?

[이 SAML 유효성 검사 도구를](https://www.samltool.com/validate_response.php) 사용하여 SAML 인증서의 유효성을 검사할 수 있습니다. 만료된 SAML 인증서도 유효하지 않은 SAML 인증서입니다.

### 올바른 SAML 인증서(x.509 인증서)를 업로드하셨나요?

SAML 추적의 `ds:X509Certificate` 섹션에 있는 인증서가 Braze에 업로드한 인증서와 일치하는지 확인합니다. 여기에는 `-----BEGIN CERTIFICATE-----` 헤더와 `-----END CERTIFICATE-----` 바닥글은 포함되지 않습니다.

### SAML 인증서(x.509 인증서)를 잘못 입력했거나 형식을 잘못 지정했나요?

Braze 대시보드에서 제출한 인증서에 공백이나 추가 문자가 없는지 확인합니다.

Braze에 인증서를 입력할 때는 PEM(Privacy Enhanced Mail) 인코딩 및 형식( `-----BEGIN CERTIFICATE-----` 헤더 및 `-----END CERTIFICATE-----` 바닥글 포함)이 올바르게 지정되어 있어야 합니다. 

다음은 올바른 형식의 인증서 예시입니다:

```
-----BEGIN CERTIFICATE-----
THIS_IS_A_MOCKED_CERTIFICATE_4ysJLTzETANBgkqhkiG9w0BAQsFADA0MTIwMAYDVQQDEylNaWNyb3NvZnQgQXp1cmUgRmVkZXJhdGVkIFNTTyBDZXJ0aWZpY2F0ZTAeFw0yMjA1MjcwOTA4MzFaFw0yNTAbMjcwOTA4MzFaMDQxMjAwBgNVBAMTKU1pY3Jvca9mdCBBenVyZSBGZWRlcmF0ZWQgU1NPIENlcnAFWAOKGPAWIGKJPOAMWANBgkqhkiG9w0BAQEFAAaCAQ8AMIIBCgKCAQEA1+KFJwxoac6jdFztQd+vQu59qM8rgfX5RICk0ODfpXkuDUNudcI0XmOAkKHRoMNPYlmMEf5NSiZ7TMElEPtK9zZlpAoSchxxC0Ndegc1AMFi7i2BsEIqPwrer0G6kx2vuAjdrDROPPafkmwalkfmklaw23FlYmV7doE0Vrj2WxR1PG0eFAdsxPLsO1ny55fPj2ibwaqc0XpDkfTrO9GnFvmZAS8ebYtLZsYAMAGLKWAMLGKAWMLKMFDW6vBDaK290s9FdaWza3GPHTcDstawRhyqbXpVjiqpQ0mtxANW4WduSiohhpeqv05TlSOhx87QalkfmwalfmAWMFLKQEBCwUAA4IBAQBdZ5E9FqICfL1q+G6D1tChKl1Y6I6IVULQb4LESSJRaxv53nakmflwakmMALKFMWOYKAeUWO2hdED54qGMgUnLL6YheQBrsm6ilBC68F7ZFmIzVKycvw65yamWbTMi2f2lF60GNYMrq8sGQUkgO0O2zTN07J9wGTe9M+MAFLKWAMFLKalkmflkawoij4jpcsLXXFZJoHSXnF3+qQuzu+49D6pR2lF7DDW+5+PRoc1QpDSytdXxWzItsjQ6IFRuvIGsbrMg0FVaze7ePdKrc47wSlElno7SQ0H+6g40q25rsDSLO
-----END CERTIFICATE-----
```

### 사용자의 세션 토큰이 유효한가요?

영향을 받은 사용자에게 [브라우저의 캐시와 쿠키를 지운](https://its.uiowa.edu/services/how-clear-cache-and-cookies-your-web-browser) 다음 SAML SSO로 다시 로그인을 시도하도록 하세요.

### 릴레이 상태를 설정하셨나요?

`ERROR_CODE_SSO_INVALID_RELAY_STATE` 라는 오류가 표시되는 경우 RelayState가 잘못 구성되었거나 존재하지 않을 수 있습니다. 아직 설정하지 않았다면 IdP 관리 시스템에서 RelayState를 설정해야 합니다. 단계는 [릴레이 상태 설정을](#setting-up-your-relaystate) 참조하세요. 

### 사용자가 Okta와 Braze 사이에 로그인 루프에 갇혀 있나요?

사용자가 Okta SSO와 Braze 대시보드 사이를 오가는 중이어서 로그인할 수 없는 경우, Okta로 이동하여 SSO URL 대상을 [Braze 인스턴스]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints/) (예: `https://dashboard-07.braze.com`)로 설정해야 합니다. 

다른 IdP를 사용하는 경우, 회사에서 올바른 SAML 또는 x.509 인증서를 Braze에 업로드했는지 확인하세요.

### 수동 통합을 사용하고 계신가요?

회사에서 IdP의 앱 스토어에서 Braze 앱을 다운로드하지 않은 경우 사전 구축된 통합을 다운로드해야 합니다. 예를 들어 Okta가 IdP인 경우 [통합 페이지에서](https://www.okta.com/integrations/braze/) Braze 앱을 다운로드할 수 있습니다.

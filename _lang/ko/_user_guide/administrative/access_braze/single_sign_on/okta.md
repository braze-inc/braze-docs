---
nav_title: 옥타
article_title: 옥타
page_order: 4
page_type: tutorial
description: "이 문서는 Braze를 Okta와 함께 SSO으로 사용하는 방법을 안내합니다." 

---

# 옥타 

> Okta는 모든 기기에서 모든 사람을 모든 애플리케이션과 연결합니다. 클라우드를 위해 구축된 엔터프라이즈급 ID 관리 서비스로, 많은 온프레미스 애플리케이션과 호환됩니다. Okta를 사용하면 IT 팀이 모든 직원의 애플리케이션 또는 기기에 대한 액세스를 관리할 수 있습니다.

## 요구 사항

| 요구 사항 | 세부 정보 |
| ----------- | ------- |
| Okta가 계정에 활성화되었습니다 | 귀하의 계정에 대해 이를 활성화하려면 Braze 계정 매니저에게 문의하십시오. |
| Okta 관리자 권한 | Okta를 설정하기 전에 관리자 권한이 있는지 확인하십시오. |
| Braze 관리자 권한 | Okta를 설정하기 전에 관리자 권한이 있는지 확인하십시오. |
| RelayState API 키 | IdP 로그인을 활성화하려면 **설정** > **API 키**로 이동하여 `sso.saml.login` 권한이 있는 API 키를 생성하십시오. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 1단계: Braze 구성

### 1a 단계  Braze에서 보안 설정으로 이동

계정 매니저가 계정에 대해 SAML SSO를 활성화한 후, **설정** > **관리자 설정** > **보안 설정**으로 이동하여 SAML SSO 섹션을 **ON**으로 토글합니다.

![Okta SAML SSO enabled on the Security Settings page.]({% image_buster/assets/img/Okta/okta1.png %})

### 1b 단계: SAML SSO 설정 편집

Okta 관리자 대시보드에서 대상 URL(로그인 URL)과 `x.509` 인증서가 제공되며, 이를 Braze 계정의 **보안 설정** 페이지에 입력해야 합니다.

![]({% image_buster /assets/img/Okta/okta5.png %}){: style="max-width:75%"}

| 요구 사항 | 세부 정보 |
|---|---|
| `SAML Name` | 이것은 로그인 화면에 버튼 텍스트로 나타납니다. 이것은 일반적으로 귀하의 ID 공급자의 이름입니다. 예를 들어, "Okta". |
| `Target URL` | 이것은 Okta 관리자 대시보드에서 제공한 로그인 URL입니다. **애플리케이션** > 내 애플리케이션 > **일반** 탭 > **앱 임베드 링크** > **임베드 링크**에서 찾습니다. |
| `Certificate` | `x.509` PEM 인코딩 인증서는 ID 공급자가 제공합니다. 이 필드에 복사하여 붙여넣어야 합니다. Okta에서 **SAML 서명 인증서**로 이동하여 **작업** > **인증서 다운로드**를 선택합니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

완료되면 페이지 하단에서 **저장 변경 사항**을 선택하세요.

## 2단계: Okta 구성

Okta에서 Braze SAML 앱의 **로그인** 탭을 선택한 다음 **편집**을 클릭합니다. 

다음으로, `sso.saml.login` 권한이 있는 RelayState API 키를 **기본값 릴레이 상태** 필드에 입력합니다. 

![Okta Default RelayState in the Sign On tab.]({% image_buster /assets/img/Okta/okta2.png %}){: style="max-width:75%"}

이 새로운 설정을 저장하십시오.

{% alert tip %}
Braze 계정 사용자가 SAML SSO로만 로그인하도록 하려면 **회사 설정** 페이지에서 [SSO 인증을 제한할]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/set_up/#restriction) 수 있습니다.
{% endalert %}

## 3단계: 로그인

이제 Okta를 사용하여 Braze에 로그인할 수 있습니다!

![Braze dashboard login with Okta SSO enabled.]({% image_buster /assets/img/Okta/okta4.png %}){: style="max-width:60%"}


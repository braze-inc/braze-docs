---
nav_title: Okta
article_title: Okta
page_order: 4
page_type: tutorial
description: "이 문서에서는 싱글 사인온에 Okta를 사용하도록 Braze를 구성하는 방법을 안내합니다." 

---

# Okta 

> Okta는 모든 사람을 모든 기기의 모든 애플리케이션과 연결합니다. 클라우드용으로 구축되었지만 많은 온프레미스 애플리케이션과 호환되는 엔터프라이즈급 ID 관리 서비스입니다. IT 팀은 Okta를 통해 모든 애플리케이션 또는 기기에 대한 직원의 액세스를 관리할 수 있습니다.

## 요구 사항

| 요구 사항 | 세부 정보 |
| ----------- | ------- |
| 계정에 Okta가 켜져 있습니다. | 계정에 이 기능을 사용 설정하려면 Braze 계정 매니저에게 문의하세요. |
| Okta 관리자 권한 | Okta를 설정하기 전에 관리자 권한이 있는지 확인하세요. |
| Braze 관리자 권한 | Okta를 설정하기 전에 관리자 권한이 있는지 확인하세요. |
| 릴레이스테이트 API 키 | IdP 로그인을 인에이블먼트하려면 **설정** > **API 키로** 이동하여 `sso.saml.login` 권한으로 API 키를 만듭니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 1단계: Braze 구성하기

### 1a단계: Braze에서 보안 설정으로 이동합니다.

계정 매니저가 계정에 SAML SSO를 인에이블먼트한 후에는 **설정** > **관리자 설정** > **보안 설정으로** 이동하여 SAML SSO 섹션을 **켜기로** 토글하세요.

보안 설정 페이지에서 SAML SSO를 인에이블먼트합니다.]({% image_buster/assets/img/Okta/okta1.png %})

### 1b단계: SAML SSO 설정 편집하기

Okta 관리자 대시보드에서 타겟팅 URL(로그인 URL)과 `x.509` 인증서를 제공받게 되며, 이를 Braze 계정의 **보안 설정** 페이지에 입력해야 합니다.

\![]({% image_buster /assets/img/Okta/okta5.png %}){: style="max-width:75%"}

| 요구 사항 | 세부 정보 |
|---|---|
| `SAML Name` | 로그인 화면의 버튼 텍스트로 표시됩니다. 일반적으로 ID 공급자의 이름입니다(예: "Okta"). |
| `Target URL` | Okta 관리자 대시보드에서 제공하는 로그인 URL입니다. **애플리케이션** > 내 애플리케이션 > **일반** 탭 > **앱 임베드 링크** > **임베드 링크로** 이동하여 찾습니다. |
| `Certificate` | `x.509` PEM 인코딩 인증서는 ID 공급업체에서 제공합니다. 이 필드에 복사하여 붙여넣어야 합니다. **SAML 서명 인증서로** 이동하여 **작업** > **인증서 다운로드를** 선택하면 Okta에서 검색할 수 있습니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

완료되면 페이지 하단에서 **변경사항 저장을** 선택합니다.

## 2단계: Okta 구성

Okta에서 Braze SAML 앱의 **로그온** 탭을 선택한 다음 **편집을** 클릭합니다. 

다음으로 **기본값 릴레이 상태** 필드에 `sso.saml.login` 권한이 있는 RelayState API 키를 입력합니다. 

로그인 탭에서 기본값 릴레이 상태를 클릭합니다.]({% image_buster /assets/img/Okta/okta2.png %}){: style="max-width:75%"}

이 새 설정을 저장하세요.

{% alert tip %}
Braze 계정 사용자가 SAML SSO로만 로그인하도록 하려면 **회사 설정** 페이지에서 [통합 인증을 제한할]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/set_up/#restriction) 수 있습니다.
{% endalert %}

## 3단계: 로그인

이제 Okta를 사용하여 Braze에 로그인할 수 있습니다!

\![Okta SSO가 인에이블된 상태에서 Braze 대시보드 로그인.]({% image_buster /assets/img/Okta/okta4.png %}){: style="max-width:60%"}


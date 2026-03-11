---
nav_title: 자동화된 사용자 프로비저닝
article_title: 자동화된 사용자 프로비저닝
page_order: 10
page_type: reference
description: "이 참조 문서에서는 자동화된 사용자 프로비저닝을 위해 제공해야 하는 정보와 생성된 SCIM(System for Cross-domain Identity Management) 토큰을 사용하는 방법 및 위치에 대해 설명합니다."
alias: /scim/automated_user_provisioning/

---

# 자동화된 사용자 프로비저닝

> Use SCIM provisioning to automatically create and manage Braze users through API. This article walks you through what information to provide, how to generate your SCIM token, and where to find your SCIM API endpoint.

{% multi_lang_include early_access_beta_alert.md feature='SCIM provisioning' %}

## SCIM 프로비저닝 설정에 접근하기

1. Braze 대시보드에서 **설정** > **관리 설정** > **SCIM 프로비저닝**으로 이동한 다음 **SCIM 통합 구성**을 선택합니다.
2. **Braze 구성** 단계에서 프로비저닝 방법을 선택하고 접근 설정을 제공합니다.

![프로비저닝 방법을 선택하고 접근 설정을 제공하는 섹션이 있는 SCIM 통합 설정 페이지입니다.]({% image_buster /assets/img_archive/scim_braze_config.png %}){: style="max-width:70%;"}

{: start="3"}
3\. **IdP 구성** 단계에서 선택한 프로비저닝 방법에 대한 플랫폼 내의 단계를 따릅니다.

{% tabs %}
{% tab Okta - Braze app %}

{% multi_lang_include early_access_beta_alert.md feature='The Okta integration' %}

Okta에서 SAML SSO를 위해 Braze 앱을 설정한 경우 **Okta - Braze 앱** 옵션을 사용합니다. SSO를 위해 커스텀 앱을 설정한 경우 [Okta - 커스텀 앱 통합]({{site.baseurl}}/user_guide/administrative/app_settings/company_settings/automated_user_provisioning/?tab=okta%20-%20custom%20app%20integration#step-1-set-up-scim-provisioning) 탭의 지침을 따릅니다.

## 1단계: SCIM 프로비저닝 설정하기

### 1.1단계: SCIM 활성화

1. Okta에서 **애플리케이션** > **애플리케이션**으로 이동한 다음 **앱 통합 만들기**를 선택합니다. 로그인 방법으로 **SAML 2.0**을 선택합니다.
2. 커스텀 앱을 만들기 위해 다음 세부정보를 입력합니다(이는 Braze [**IdP 구성** 단계](#accessing-scim-provisioning-settings)에 있습니다):
- 앱 로고
- 싱글 사인온 URL
- 오디언스 URL (SP 엔터티 ID)
3. Select **Finish**.
4. **일반** 탭을 선택합니다. 
5. **앱 설정** 섹션에서 **편집**을 선택합니다.
6. **프로비저닝** 필드에서 **SCIM**을 선택합니다. 

### 1.2단계: 애플리케이션 가시성 비활성화

1. **애플리케이션 가시성** 필드에서 **사용자에게 애플리케이션 아이콘 표시 안 함** 체크박스를 선택합니다. 이것은 사용자가 SCIM 전용 앱을 통해 SSO에 접근하는 것을 방지합니다. 
2. Select **Save**.

### 1.3단계: SCIM 통합을 설정하십시오.

1. **프로비저닝** 탭을 선택하십시오.
2. **설정** > **통합** > **SCIM 연결**에서 **편집**을 선택하고 **SCIM 프로비저닝 설정** 페이지의 표에 채워지는 필드 값을 입력하십시오.

### 1.4단계: API 자격 증명을 테스트하십시오.

**API 자격 증명 테스트**을 선택하십시오. 통합이 성공하면 확인 메시지가 나타나고 저장할 수 있습니다.

### 1.5단계: 앱에 대한 프로비저닝을 활성화하십시오.

1. **프로비저닝** > **설정** > **앱으로** > **앱으로의 프로비저닝**에서 **편집**을 선택하십시오.
2. 다음을 활성화하십시오:
    - 사용자 생성
    - 사용자 속성 업데이트
    - 사용자 비활성화
3. **속성 매핑** 섹션을 검토하고 구성하여 **SCIM 프로비저닝 설정** 페이지의 표에 채워지는 매핑으로 설정하십시오.

## 2단계: 사용자를 앱에 할당하십시오.

1. **할당** 탭을 선택하십시오.
2. **할당**을 선택하고 옵션을 선택하십시오.
3. Braze에 접근해야 하는 사람들에게 앱을 할당하십시오.
4. 할당을 완료했으면 **완료**을 선택하십시오.

{% endtab %}
{% tab Okta - Custom app integration %}

{% multi_lang_include early_access_beta_alert.md feature='The Okta integration' %}

SSO를 위해 커스텀 앱을 설정한 경우 **Okta - 커스텀 앱 통합** 옵션을 사용하십시오. Okta에서 SAML SSO를 위한 Braze 앱을 설정하면 [Okta - Braze 앱]({{site.baseurl}}/user_guide/administrative/app_settings/company_settings/automated_user_provisioning/?tab=okta%20-%20braze%20app#step-1-set-up-scim-provisioning) 탭의 지침을 따르세요.

## 1단계: SCIM 프로비저닝 설정하기

### 1.1단계: SCIM 활성화

1. Okta에서 Braze 앱으로 이동합니다.
2. **일반** 탭을 선택합니다.
3. **앱 설정** 섹션에서 **편집**을 선택합니다.
4. **프로비저닝** 필드에서 **SCIM**을 선택합니다.
5. Select **Save**.

### 1.2단계: SCIM 통합 설정

1. **프로비저닝** 탭을 선택하십시오.
2. **설정** > **통합** > **SCIM 연결**에서 **편집**을 선택하고 **SCIM 프로비저닝 설정** 페이지의 표에 채워지는 필드 값을 입력합니다.
3. **API 자격 증명 테스트**을 선택하여 API 자격 증명을 테스트합니다.
4. Select **Save**.

### 1.3단계: 앱에 대한 프로비저닝을 활성화하십시오.

1. **프로비저닝** > **설정** > **앱으로** > **앱으로의 프로비저닝**에서 **편집**을 선택하십시오.
2. 다음을 활성화하십시오:
    - 사용자 생성
    - 사용자 속성 업데이트
    - 사용자 비활성화
3. **속성 매핑** 섹션을 검토하고 구성하여 **SCIM 프로비저닝 설정** 페이지의 표에 채워지는 매핑으로 설정하십시오.

## 2단계: 사용자를 앱에 할당하십시오.

1. **할당** 탭을 선택하십시오.
2. **할당**을 선택하고 옵션을 선택하십시오.
3. Braze에 접근해야 하는 사람들에게 앱을 할당하십시오.
4. **완료**을 선택합니다.

{% endtab %}
{% tab Entra ID %}

{% multi_lang_include early_access_beta_alert.md feature='The Entra ID integration' %}

## 1단계: SCIM 프로비저닝 앱 설정

### 1.1단계: Microsoft Entra 관리 센터에 로그인합니다.

Microsoft Entra 관리 센터에 로그인합니다.

### 1.2단계: SCIM 앱을 생성하고 설정합니다.

1. 탐색 메뉴에서 **Entra ID** > **기업 앱**으로 이동합니다.
2. **새 애플리케이션**을 선택합니다.
3. **자신의 애플리케이션 만들기**을 선택합니다.
4. 패널에서 앱의 이름을 입력합니다.
5. **애플리케이션으로 무엇을 하시겠습니까?** 섹션에서 **갤러리에서 찾을 수 없는 애플리케이션 통합(비갤러리)**를 선택합니다.
6. Select **Create**.

### 1.3단계: SCIM 통합 설정

1. SCIM 애플리케이션의 **관리** > **프로비저닝** 섹션으로 이동합니다.
2. **애플리케이션 연결** 또는 **새 구성**을 선택하고 **SCIM 프로비저닝 설정** 페이지의 표에 채워지는 필드 값을 입력합니다.

### 1.4단계: 앱에 대한 프로비저닝을 활성화하십시오.

1. SCIM 애플리케이션의 **관리** > **속성 매핑(미리 보기)** 섹션으로 이동합니다.
2. **Microsoft Entra ID 사용자 프로비저닝**을 선택합니다.
3. **속성 매핑** 섹션을 검토하고 구성하여 **SCIM 프로비저닝 설정** 페이지의 표에 채워지는 속성과 일치시킵니다.
4. **속성 매핑** 페이지를 닫습니다.

## 2단계: 사용자를 앱에 할당하십시오.

1. **관리** > **사용자 및 그룹**으로 이동합니다.
2. **사용자/그룹 추가**를 선택합니다.
3. 앱에 사용자를 할당하려면 **선택 안 함**을 선택합니다.
4. 할당을 확인하려면 **선택** 버튼을 선택합니다.

{% endtab %}
{% tab Custom %}

## 1단계: Configure your SCIM settings

- **Default Workspace:** 기본적으로 새 사용자가 추가될 작업공간을 선택합니다. If you don’t specify a workspace in your [SCIM API request]({{site.baseurl}}/post_create_user_account/), Braze assigns users to this workspace.
- **Service Origin:** Enter the origin domain of your SCIM requests. Braze uses this in the `X-Request-Origin` header to verify where requests are coming from.
- **IP Allowlisting (optional):** You can restrict SCIM requests to specific IP addresses. Enter a comma-separated list or range of IP addresses to allow. 각 요청의 `X-Request-Origin` 헤더는 요청 IP 주소를 허용 목록과 대조하는 데 사용됩니다.

![SCIM Provisioning settings form with three fields: 기본 작업공간, 서비스 출처 및 선택적 IP 허용 목록입니다. “SCIM 토큰 생성” 버튼이 비활성화되었습니다.]({% image_buster /assets/img/scim_unfilled.png %})

## 2단계: SCIM 토큰을 생성합니다.

After completing the required fields, press **Generate SCIM token** to generate a SCIM token and see your SCIM API endpoint. Make sure to copy the SCIM token before you navigate away. **이 토큰은 한 번만 나타납니다.** 

![SCIM API Endpoint and SCIM Token fields displayed with masked values and copy buttons. 토큰 필드 아래에 “토큰 재설정” 버튼이 있습니다.]({% image_buster /assets/img/scim.png %})

Braze expects all SCIM requests to contain the SCIM API bearer token attached via an HTTP `Authorization` header.

{% endtab %}
{% endtabs %}

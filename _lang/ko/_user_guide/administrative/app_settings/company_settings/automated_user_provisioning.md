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

## SCIM 프로비저닝 설정에 액세스

1. Braze 대시보드에서 **설정** > **관리자 설정** > **SCIM 프로비저닝으로** 이동하여 ID 공급자를 추가합니다.
2. **Braze 프로비저닝** 단계에서 프로비저닝 방법을 선택하고 액세스 설정을 입력합니다.

![프로비저닝 방법 선택 및 액세스 설정을 위한 섹션이 있는 SCIM 통합을 설정하는 페이지입니다.]({% image_buster /assets/img_archive/scim_braze_config.png %}){: style="max-width:70%;"}

{: start="3"}
3\. **IdP 구성** 단계에서 선택한 프로비저닝 방법에 대한 플랫폼 내 단계를 따릅니다.

{% tabs %}
{% tab Okta - Braze app %}

{% alert important %}
Okta 통합은 현재 얼리 액세스 중입니다. Contact your Braze account manager if you're interested in participating in the early access.
{% endalert %}

## 1단계: SCIM 프로비저닝 설정

### 1.1단계: SCIM 활성화

1. Okta에서 Braze 앱으로 이동합니다.
2. **일반** 탭을 선택합니다.
3. **앱 설정** 섹션에서 **편집을** 선택합니다.
4. **프로비저닝** 필드에서 **SCIM을** 선택한 다음 **저장을** 선택합니다.

### 1.2단계: SCIM 통합 설정하기

1. **프로비저닝** 탭을 선택합니다.
2. **설정** > **통합** > **SCIM 연결에서** **편집을** 선택하고 **SCIM 프로비저닝 설정** 페이지의 표에 채워지는 필드 값을 입력합니다.

### 1.3단계: API 자격 증명 테스트

**API 자격 증명 테스트를** 선택합니다. 통합이 성공하여 저장할 수 있으면 확인 메시지가 표시됩니다.

### 1.4단계: 앱에 대해 프로비저닝 활성화

1. **프로비저닝** > **설정** > **앱으로** > **앱에 프로비저닝에서** **편집을** 선택합니다.
2. 다음을 활성화합니다.
    - 사용자 생성
    - 사용자 속성 업데이트
    - 사용자 비활성화
3. **SCIM 프로비저닝 설정** 페이지의 표에 채워지는 매핑으로 **속성 매핑** 섹션을 검토하고 구성하세요.

## 2단계: 앱에 사용자 할당하기

1. **과제** 탭을 선택합니다.
2. **할당을** 선택하고 옵션을 선택합니다.
3. Braze에 액세스할 수 있어야 하는 사용자에게 앱을 할당합니다.
4. 과제를 완료하면 **완료를** 선택합니다.

{% endtab %}
{% tab Okta - Custom app integration %}

{% alert important %}
Okta 통합은 현재 얼리 액세스 중입니다. Contact your Braze account manager if you're interested in participating in the early access.
{% endalert %}

## 1단계: SCIM 프로비저닝 설정

### 1.1단계: SCIM 활성화

1. Okta에서 Braze 앱으로 이동합니다.
2. **일반** 탭을 선택합니다.
3. **앱 설정** 섹션에서 **편집을** 선택합니다.
4. **프로비저닝** 필드에서 **SCIM을** 선택합니다.
5. Select **Save**.

### 1.2단계: SCIM 통합 설정하기

1. **프로비저닝** 탭을 선택합니다.
2. **설정** > **통합** > **SCIM 연결에서** **편집을** 선택하고 **SCIM 프로비저닝 설정** 페이지의 표에 채워지는 필드 값을 입력합니다.
3. **API 자격** 증명 테스트를 선택하여 API 자격 증명을 테스트합니다.
4. Select **Save**.

### 1.3단계: 앱에 대해 프로비저닝 활성화

1. **프로비저닝** > **설정** > **앱으로** > **앱에 프로비저닝에서** **편집을** 선택합니다.
2. 다음을 활성화합니다.
    - 사용자 생성
    - 사용자 속성 업데이트
    - 사용자 비활성화
3. **SCIM 프로비저닝 설정** 페이지의 표에 채워지는 매핑으로 **속성 매핑** 섹션을 검토하고 구성하세요.

## 2단계: 앱에 사용자 할당하기

1. **과제** 탭을 선택합니다.
2. **할당을** 선택하고 옵션을 선택합니다.
3. Braze에 액세스할 수 있어야 하는 사람들에게 앱을 할당합니다.
4. **완료를** 선택합니다.

{% endtab %}
{% tab Entra ID %}

{% alert important %}
Entra ID 통합은 현재 얼리 액세스 중입니다. Contact your Braze account manager if you're interested in participating in the early access.
{% endalert %}

## 1단계: SCIM 프로비저닝 앱 설정

### 1.1단계. Microsoft Entra 관리 센터에 로그인
Microsoft Entra 관리 센터에 로그인합니다.

### 1.2단계: SCIM 앱 만들기 및 설정하기

1. 탐색 메뉴에서 **Entra ID** > **기업 앱으로** 이동합니다.
2. **새 애플리케이션을** 선택합니다.
3. **나만의 애플리케이션 만들기를** 선택합니다.
4. 패널에서 앱의 이름을 입력합니다.
5. **애플리케이션으로 무엇을 하려고 하나요?** 섹션에서 **갤러리에서 찾을 수 없는 애플리케이션 통합(갤러리 외)을** 선택합니다.
6. Select **Create**.

### 1.3단계: SCIM 통합 설정하기

1. SCIM 애플리케이션의 **관리** > **프로비저닝** 섹션으로 이동합니다.
2. **애플리케이션 연결** 또는 **새 구성을** 선택하고 **SCIM 프로비저닝 설정** 페이지의 표에 채워지는 필드 값을 입력합니다.

### 1.4단계: 앱에 대해 프로비저닝 활성화

1. SCIM 애플리케이션의 **관리** > **속성 매핑(미리보기)** 섹션으로 이동합니다.
2. **Microsoft Entra ID 사용자 프로비저닝을** 선택합니다.
3. **SCIM 프로비저닝 설정** 페이지의 테이블에 채워지는 속성과 일치하도록 **속성 매핑** 섹션을 검토하고 구성하세요.
4. **속성 매핑** 페이지를 닫습니다.

## 2단계: 앱에 사용자 할당하기

1. **관리** > **사용자 및 그룹으로** 이동합니다.
2. **사용자/그룹 추가를** 선택합니다.
3. 앱에 사용자를 할당하려면 선택되지 **않음을** 선택합니다.
4. **선택** 버튼을 선택하여 할당을 확인합니다.

{% endtab %}
{% tab Custom %}

## 1단계: Configure your SCIM settings

- **Default Workspace:** 기본값으로 새 사용자를 추가할 워크스페이스를 선택합니다. If you don’t specify a workspace in your [SCIM API request]({{site.baseurl}}/post_create_user_account/), Braze assigns users to this workspace.
- **Service Origin:** Enter the origin domain of your SCIM requests. Braze uses this in the `X-Request-Origin` header to verify where requests are coming from.
- **IP Allowlisting (optional):** You can restrict SCIM requests to specific IP addresses. Enter a comma-separated list or range of IP addresses to allow. 각 요청의 `X-Request-Origin` 헤더는 허용 목록에서 요청 IP 주소를 확인하는 데 사용됩니다.

![SCIM Provisioning settings form with three fields: Default Workspace, Service Origin , and optional IP Allowlisting. "SCIM 토큰 생성" 버튼이 비활성화됩니다.]({% image_buster /assets/img/scim_unfilled.png %})

## 2단계: SCIM 토큰 생성하기

After completing the required fields, press **Generate SCIM token** to generate a SCIM token and see your SCIM API endpoint. Make sure to copy the SCIM token before you navigate away. **이 토큰은 한 번만 표시됩니다.** 

![SCIM API Endpoint and SCIM Token fields displayed with masked values and copy buttons. 토큰 필드 아래에는 '토큰 재설정' 버튼이 있습니다.]({% image_buster /assets/img/scim.png %})

Braze expects all SCIM requests to contain the SCIM API bearer token attached via an HTTP `Authorization` header.

{% endtab %}
{% endtabs %}

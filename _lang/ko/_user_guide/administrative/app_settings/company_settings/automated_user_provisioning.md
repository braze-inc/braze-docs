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

## Step 1: Access SCIM privioning settings

In the Braze dashboard, go to **Settings** > **Admin Settings** > **SCIM Provisioning**.

## Step 2: Configure your SCIM settings

To enable SCIM provisioning, provide the following information:

- **Default Workspace:** Select the workspace where new users will be added by default. If you don’t specify a workspace in your [SCIM API request]({{site.baseurl}}/post_create_user_account/), Braze assigns users to this workspace.
- **Service Origin:** Enter the origin domain of your SCIM requests. Braze uses this in the `X-Request-Origin` header to verify where requests are coming from.
- **IP Allowlisting (optional):** You can restrict SCIM requests to specific IP addresses.
Enter a comma-separated list or range of IP addresses to allow. The `X-Request-Origin` header in each request will be used to check the request IP address against the allowlist.

{% alert note %}
이 SCIM 엔드포인트는 ID 공급자와 직접 통합되지 않습니다.
{% endalert %}

![SCIM Provisioning settings form with three fields: Default Workspace, Service Origin , and optional IP Allowlisting. The “Generate SCIM Token” button is disabled.]({% image_buster /assets/img/scim_unfilled.png %})

## Step 3: Get your SCIM token and endpoint

After completing the required fields, press **Generate SCIM token** to generate a SCIM token and see your SCIM API endpoint. Make sure to copy the SCIM token before you navigate away. **This token will only be presented once.** 

![SCIM API Endpoint and SCIM Token fields displayed with masked values and copy buttons. Below the token field is a “Reset Token” button.]({% image_buster /assets/img/scim.png %})

Braze expects all SCIM requests to contain the SCIM API bearer token attached via an HTTP `Authorization` header.


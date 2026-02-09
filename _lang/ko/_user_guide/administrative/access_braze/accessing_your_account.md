---
nav_title: 계정에 액세스
article_title: 계정에 액세스
page_order: 0
page_type: reference
description: "이 도움말에서는 Braze 계정을 만드는 방법, 액세스 권한을 부여받은 후 로그인하는 방법, Braze 비밀번호를 재설정하는 방법에 대해 설명합니다."

---

# 계정에 액세스

> This article covers how to get your Braze account, how to log in after being granted access, and how to troubleshoot your dashboard access and dashboard performance.

회사의 첫 번째 Braze 사용자이고 처음 로그인하는 경우, 계약 첫날에 이메일 확인 및 로그인을 요청하는 환영 이메일(`@alerts.braze.com`)을 받게 됩니다.

After confirming your account, you can add additional users from the [Company Users]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/) page of your dashboard. 모든 사용자는 계정을 추가한 후 계정 확인을 요청하는 이메일을 받게 됩니다.

If you aren't the first user on your company's Braze account, contact your company's Braze account administrator and ask them to create your account. 그러면 이메일 확인 및 로그인을 요청하는 환영 이메일(`@alerts.braze.com`)이 전송됩니다.

## 로그인

Let's talk about how to log in, whether it's the first time or the millionth! 회사의 첫 번째 사용자라면 이전 섹션의 안내를 따르세요. If not, you can log in after your company's Braze admin creates your account.

You can either log in from the [Braze.com](https://www.braze.com) home site, or just use your dashboard URL that corresponds to your specific [Braze instance]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints/). For your convenience, Braze has several single sign-on (SSO) options such as:

* [SAML SSO]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/set_up/)
    * [SAML just-in-time provisioning]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/saml_jit/)
* [Microsoft Entra SSO]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/entra/)
* [Okta]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/okta/)
* [OneLogin]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/onelogin/)

{% alert note %}
After you log into Braze with SSO, you can no longer use your password to log into the dashboard.
{% endalert %}

## Supported browsers

The Braze dashboard supports the following browsers:
- Chrome (version 87 or newer)
- Firefox (version 85 or newer)
- Safari (version 15.4 or newer)
- Edge (version 87 or newer)

If your Braze dashboard says you have an unexpected error and your browser console tool shows the error `ReferenceError: structuredClone is not defined`, your browser is outdated. If this error keeps reoccurring, uninstall and reinstall your browser.

## 여러 개의 Braze 대시보드에 액세스하기

Braze에서는 동일한 클러스터에 있는 여러 대시보드 사용자에게 동일한 이메일 주소를 등록할 수 없습니다(예: US-01에 두 개의 대시보드가 있는 경우). 동일한 이메일을 사용하여 서로 다른 클러스터에 계정을 만들 수 있습니다(예: US-01에 대시보드가 하나 있고 US-05에 대시보드가 있는 경우). 동일한 클러스터에서 여러 개의 Braze 대시보드에 액세스해야 하는 경우 다음과 같이 할 수 있습니다:

### 이메일 별칭 사용

이메일 제공업체가 Gmail인 경우 이메일 주소에 `+` 기호 뒤에 아무 텍스트나 추가하여 별칭을 만들 수 있습니다. For example:
- **원본 이메일:** `rocky@gmail.com`
- **별칭 이메일:** `rocky+1@gmail.com`

두 이메일 주소 모두 동일한 받은편지함으로 이메일을 보내지만, 로그인할 때 Braze는 이를 별도의 계정으로 인식합니다.

### 다른 제공업체와 별도의 별칭 만들기

이메일 제공업체가 `+` 별칭을 지원하지 않는 경우에도 `rocky@braze.com` 을 `rocky.lotito@braze.com` 으로 전달하도록 설정하는 등 별도의 별칭을 만들 수 있습니다. 이렇게 하면 여러 주소가 동일한 받은편지함으로 퍼널링되면서도 Braze에서는 서로 다른 이메일로 인식됩니다.

### 여러 회사 개발자 사용

여러 회사 개발자 기능을 사용하면 여러 회사에서 단일 사용자 계정을 공유할 수 있습니다. 사용자는 고객 프로필 메뉴에서 여러 회사 대시보드를 토글할 수 있습니다.

SSO가 있고 여러 회사의 개발자를 설정하려는 경우 커스텀 SAML SSO 통합을 설정하여 SAML 사용자 지정 엔티티 ID를 인에이블먼트해야 합니다. [서비스 제공업체(SP) 시작 로그인의]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/set_up/) 단계를 따르되 이러한 변경 사항을 적용합니다:
- 각 대시보드 통합에 대해 **엔티티 ID를** `braze_dashboard_<companyID>` 로 변경합니다.
- 고객 성공 관리자 또는 계정 매니저에게 문의하여 각 대시보드에 `saml_sso_custom_entity_id` 기능 플리퍼를 인에이블먼트하세요.

### 싱글 사인온(SSO)에 대한 고려 사항

싱글 사인온(SSO)을 사용하는 경우, 여러 개의 다른 이메일 주소를 사용하면 문제가 발생할 수 있다는 점에 유의하세요. 액세스 문제를 방지하기 위해 SSO 설정이 올바르게 구성되었는지 확인하세요.

## 문제 해결

### 비밀번호 재설정하기

To reset your password, select the **Forgot your password?** link on the dashboard login page. You'll be prompted to input your email to receive a link to reset your password.

!["비밀번호를 잊으셨나요?" 메시지가 표시되는 대시보드 로그인.]({% image_buster /assets/img_archive/enable_reset.png %}){: style="max-width:60%"}

### Clearing your browser cache and cookies

If you're having issues with dashboard performance, such as your dashboard or segment performance list not loading, try clearing your browser cache and cookies by following the steps for your respective browser.

{% alert important %}
Clearing cookies will log you out, so unsaved work will be lost.
{% endalert %}

- [Chrome에서 캐시 & 쿠키 지우기](https://support.google.com/accounts/answer/32050?hl=en&co=GENIE.Platform%3DDesktop)
- [Clear cookies in Safari on Mac](https://support.apple.com/en-gb/guide/safari/sfri11471/16.1/mac/13.0)
- [Clear cookies and site data in Firefox](https://support.mozilla.org/en-US/kb/clear-cookies-and-site-data-firefox)
- [Delete all cookies in Microsoft Edge](https://support.microsoft.com/en-us/windows/manage-cookies-in-microsoft-edge-view-allow-block-delete-and-use-168dab11-0753-043d-7c16-ede5947fc64d#bkmk_deleteallcookies)

If clearing your browser cache and cookies doesn't resolve your issues, contact [Support]({{site.baseurl}}/support_contact/).

### Accessing the drag-and-drop editor

For most Braze users, the drag-and-drop editor should load. However, if you're using a VPN or are behind a firewall, you may need to allowlist a domain. Contact your IT administrator to check that `*.bz-rndr.com` is allowlisted.

The editor may experience loading issues due to the following:

- **Transient error:** These are temporary failures that may affect connectivity, communication, or data transfer. Fortunately, they typically resolve on their own without requiring significant intervention, as they're often caused by short-lived conditions and do not indicate systemic problems.
- **Major error:** This may involve an underlying infrastructure or product issue.  You can check our [Braze system status page](https://braze.statuspage.io/) as we are likely aware of the situation and actively working to resolve it.

{% alert important %}
If you're still experiencing issues, [open a support ticket]({{site.baseurl}}/user_guide/administrative/access_braze/support/). Before doing so, check that your IT administrator has confirmed that `*.bz-rndr.com` is allowlisted on your end.
{% endalert %}

### Braze 학습에 액세스하기

Braze Learning에 로그인하는 데 문제가 있거나 대시보드로 리디렉션되는 루프에 갇혀 있는 경우 다음 단계를 수행하세요:

1. 여러 개의 Braze 계정이 있는 경우, 잘못된 계정으로 두 번 로그인하면 Braze 대시보드로 이동합니다. 올바른 계정으로 로그인했는지 확인합니다. 
2. 광고 차단기가 있는 경우 차단기가 꺼져 있는지 확인하세요. 싱글 사인온 기능에 필요한 쿠키를 차단할 수 있습니다.
3. 회사 설정 > 보안 설정으로 이동하여 싱글 사인온(SSO)이 켜져 있는지 확인합니다.
4. 대시보드 고객 프로필에 이름과 성이 모두 포함되어 있는지 확인합니다. 성이 없으면 로그인 프로세스가 중단될 수 있습니다.
5. 대시보드에서 **지원** > **Braze 학습으로** 이동하여 **Braze 학습**에 액세스하세요. 
6. 문제가 계속 발생하면 계정을 다시 만들어 보세요. 무료 평가판 단계에서 Braze Learning에 액세스한 사용자는 현재 액세스하는 데 어려움이 있을 수 있습니다.

### 2단계 인증(2FA) 문제

사용자가 2단계 인증(2FA)에 문제가 발생하여 Braze 대시보드에 액세스할 수 없는 경우 몇 가지 이유가 있을 수 있습니다. 가장 흔하게는 등록된 휴대폰 번호 또는 Authy 앱이 설치된 기기에 더 이상 액세스할 수 없는 경우입니다.

관리자는 다음을 수행하여 영향을 받는 사용자의 2FA를 재설정해야 합니다: 

1. **사용자 관리로** 이동합니다.
2. 2FA 문제가 발생한 사용자에 대해 **사용자 편집을** 선택합니다.
3. 2FA 재설정 옵션을 선택합니다.
4. 메시지가 표시되면 2FA 재설정을 확인합니다.
5. 재설정을 해도 문제가 즉시 해결되지 않으면 쿠키와 캐시를 지우세요.

Braze는 보안상의 이유로 사용자를 대신하여 2FA를 재설정할 수 없으므로 관리자가 2FA를 재설정할 수 없는 경우 지원 티켓을 만드세요.

#### 고려 사항

- 회사 수준에서 2FA를 시행하는 경우: 재설정 후 Braze는 사용자가 다음에 로그인할 때 2FA를 다시 설정하라는 메시지를 표시합니다.
- 회사 수준에서 2FA를 적용하지 않는 경우: 사용자는 2FA를 다시 설정할 필요 없이 대시보드에 로그인할 수 있습니다. 2FA를 인에이블하려면 계정 설정에서 인에이블할 수 있습니다.

{% alert note %}
이 재설정 절차는 지난 1시간 이내에 너무 많은 토큰을 요청하여 계정이 잠긴 사용자에게도 적용됩니다.
{% endalert %}
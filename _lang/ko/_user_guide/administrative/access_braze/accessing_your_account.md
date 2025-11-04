---
nav_title: 계정 액세스하기
article_title: 계정 액세스하기
page_order: 2
page_type: reference
description: "이 도움말에서는 Braze 계정을 만드는 방법, 액세스 권한을 부여받은 후 로그인하는 방법, Braze 비밀번호를 재설정하는 방법에 대해 설명합니다."

---

# 계정 액세스하기

> This article covers how to get your Braze account, how to log in after being granted access, and how to troubleshoot your dashboard access and dashboard performance.

회사의 첫 번째 Braze 사용자이고 처음 로그인하는 경우, 계약 첫날에 이메일 확인 및 로그인을 요청하는 환영 이메일(`@alerts.braze.com`)을 받게 됩니다.

After confirming your account, you can add additional users from the [Company Users]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/adding_users_to_your_dashboard/) page of your dashboard. 모든 사용자는 계정을 추가한 후 계정 확인을 요청하는 이메일을 받게 됩니다.

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

## Troubleshooting

### 비밀번호 재설정하기

To reset your password, select the **Forgot your password?** link on the dashboard login page. You'll be prompted to input your email to receive a link to reset your password.

![Dashboard login with "Forgot your password?" prompt.]({% image_buster /assets/img_archive/enable_reset.png %}){: style="max-width:60%"}

### Clearing your browser cache and cookies

If you're having issues with dashboard performance, such as your dashboard or segment performance list not loading, try clearing your browser cache and cookies by following the steps for your respective browser.

{% alert important %}
Clearing cookies will log you out, so unsaved work will be lost.
{% endalert %}

- [Clear cache & cookies in Chrome](https://support.google.com/accounts/answer/32050?hl=en&co=GENIE.Platform%3DDesktop)
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


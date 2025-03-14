---
nav_title: Access Braze
article_title: Access Braze
page_order: 0
layout: dev_guide
guide_top_header: "Access Braze"
guide_top_text: "Here you can find articles to help you access your Braze account or dashboard, such as logging into your account for the first time, double-checking your endpoints, resetting passwords, and more."

page_type: reference
description: "This landing page is home to articles on accessing your Braze account or dashboard. Here, you can find resources on SSO, login, Braze instances, SDK endpoints, password resetting, and more."

guide_featured_title: "Section articles"
guide_featured_list:
- name: Navigation
  link: /docs/user_guide/administrative/access_braze/navigation/
  image: /assets/img/braze_icons/list.svg
- name: Searching Your Dashboard
  link: /docs/user_guide/administrative/access_braze/global_search/
  image: /assets/img/braze_icons/search-sm.svg
- name: API and SDK Endpoints
  link: /docs/user_guide/administrative/access_braze/sdk_endpoints/
  image: /assets/img/braze_icons/navigation-pointer-01.svg
- name: Accessing Your Account
  link: /docs/user_guide/administrative/access_braze/accessing_your_account/
  image: /assets/img/braze_icons/user-circle.svg
- name: Language Settings
  link: /docs/user_guide/administrative/access_braze/language/
  image: /assets/img/braze_icons/globe-04.svg
- name: SAML and Single Sign-On
  link: /docs/user_guide/administrative/access_braze/single_sign_on/
  image: /assets/img/braze_icons/log-in-01.svg
- name: Product Portal
  link: /docs/user_guide/administrative/access_braze/portal/
  image: /assets/img/braze_icons/annotation-question.svg
---

## Supported browsers

The Braze dashboard supports the following browsers:
- Chrome (version 87 or newer)
- Firefox (version 85 or newer)
- Safari (version 15.4 or newer)
- Edge (version 87 or newer)

If your Braze dashboard says you have an unexpected error and your browser console tool shows the error `ReferenceError: structuredClone is not defined`, your browser is outdated. If this error keeps reoccurring, uninstall and reinstall your browser.

### Browser cache and cookies

If you're having issues with dashboard performance, such as your dashboard or segment performance list not loading, try clearing your browser cache and cookies by following the steps for your respective browser.

{% alert important %}
Clearing cookies will log you out, so unsaved work will be lost.
{% endalert %}

- [Clear cache & cookies in Chrome](https://support.google.com/accounts/answer/32050?hl=en&co=GENIE.Platform%3DDesktop)
- [Clear cookies in Safari on Mac](https://support.apple.com/en-gb/guide/safari/sfri11471/16.1/mac/13.0)
- [Clear cookies and site data in Firefox](https://support.mozilla.org/en-US/kb/clear-cookies-and-site-data-firefox)
- [Delete all cookies in Microsoft Edge](https://support.microsoft.com/en-us/windows/manage-cookies-in-microsoft-edge-view-allow-block-delete-and-use-168dab11-0753-043d-7c16-ede5947fc64d#bkmk_deleteallcookies)

If clearing your browser cache and cookies doesn't resolve your issues, contact [Support]({{site.baseurl}}/support_contact/).

#### Creating a helpful Support ticket

If you contact Support, it'll be useful to have the impacted user collect network logs (Har Logs) from their browser while the issue occurs. This will show the network requests between the browser and the server, for the individual components of a webpage, and the Braze dashboard the user is trying to open.

Have the affected user do the following:

1. Open their developer tools. If using Chrome, this can be be done using the keyboard shortcut `option` + `⌘` + `J` (on macOS). If using Windows or Linux, this can be done using the shortcut `shift` + `CTRL` + `J`.
2. Select **Network** > **Fetch/XHR** or **XHR**.
3. Capture a screen recording or screenshot showing the **Name**, **Status**, **Size**, and **Time** for the elements.<br><br>![The "Fetch/XHR" tab in a Chrome browser.][1]{: style="max-width:60%;"}

Then attach the user's recording or screenshot to the Support ticket. This information can help Support's investigation.

<br><br>

[1]: {% image_buster /assets/img/network_xhr.png %}
---
nav_title: Troubleshooting HTML Rendering in Test Emails
article_title: Troubleshooting HTML Rendering in Test Emails
page_order: 0

page_type: solution
description: "This help article walks you through how to troubleshoot issues with HTML rendering in test emails."
channel: email
---

# Troubleshooting HTML rendering in test emails

If your [Test Email][37] looks off, we recommend that you...

* [Check HTML](#check-html-setup),
* [Check Conflicts](#check-conflicts),
* [Check Rendering](#check-rendering), or
* [Switch CSS In-lining](#switch-css-in-lining).

### Check HTML setup

First, confirm with your developers that your HTML is set up properly.

### Check conflicts

Certain Chrome extensions will cause issues with Braze’s email editor (one example is [Grammarly][38]). If you’re using one of these, you should either: 
- edit Braze emails in a browser that does not have Grammarly
- contact your Braze account manager and ask to flip your email editors to HTML only/plain text. 

NB plain text view removes your ```WYSIWYG``` (what you see is what you get) editor, so you should first ensure that all team members are comfortable with HTML before making this request.

### Check rendering

Emails render differently on different browsers and email clients. Record which browsers and email clients you’re experiencing issues with.

- Preview your emails in a program like [Email on Acid][39] or [Litmus][40]. These allow you to preview what emails look like in different browsers and email clients.

- Once you’ve identified which browsers/email clients are causing issues, let your developer team know that they’ll need to modify their HTML and make edits to accommodate those browsers/email clients.

### Switch CSS in-lining

There are times when the preview in Email on Acid or Litmus still does not match what is sent via the Braze dashboard. One possible cause for this is the CSS in-lining that is performed by Braze may differ from the CSS in-lining performed by other tools. If you suspect that this is the case, contact your Braze account manager to ask for CSS in-lining to be turned off.

Still need help? Open a [support ticket]({{site.baseurl}}/braze_support/) or leave feedback below.

_Last updated on December 12, 2019_

[37]: {{site.baseurl}}/developer_guide/platform_wide/sending_test_messages/#sending-a-test-push-notification-or-in-app-messages-a-classmargin-fix-namepush-inapp-testa
[38]: https://chrome.google.com/webstore/detail/grammarly-for-chrome/kbfnbcaeplbcioakkpcpgfkobkghlhen?hl=en
[39]: https://www.emailonacid.com/
[40]: https://litmus.com/

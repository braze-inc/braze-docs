---
nav_title: The HTML Looks Strange
page_order: 0
---

# The HTML Looks Strange When I Send A Test Email To Myself

If your [Test Email][37] looks off, we recommend that you...

* [Check HTML](#check-html-setup),
* [Check Conflicts](#check-conflicts),
* [Check Rendering](#check-rendering), or
* [Switch CSS In-lining](#switch-css-in-lining).

### Check HTML Setup

First, confirm with your developers that your HTML is set up properly.

### Check Conflicts

Certain Chrome extensions will cause issues with Braze’s email editor (one example is [Grammarly][38]). If you’re using one of these, you should either: 
- edit Braze emails in a browser that does not have Grammarly
- contact your Braze account manager and ask to flip your email editors to HTML only/plain text. 

NB plain text view removes your ```WYSIWYG``` (what you see is what you get) editor, so you should first ensure that all team members are comfortable with HTML before making this request.

### Check Rendering

Emails render differently on different browsers and email clients. Record which browsers and email clients you’re experiencing issues with.

- Preview your emails in a program like [Email on Acid][39] or [Litmus][40]. These allow you to preview what emails look like in different browsers and email clients.

- Once you’ve identified which browsers/email clients are causing issues, let your developer team know that they’ll need to modify their HTML and make edits to accommodate those browsers/email clients.

### Switch CSS In-lining

There are times when the preview in Email on Acid or Litmus still does not match what is sent via the Braze dashboard. One possible cause for this is the CSS in-lining that is performed by Braze may differ from the CSS in-lining performed by other tools. If you suspect that this is the case, contact your BRaze account manager to ask for CSS in-lining to be turned off.

Still need help? [Open a support ticket]({{site.baseurl}}/support_contact/), or leave feedback below.

[37]: {{site.baseurl}}/developer_guide/platform_wide/sending_test_messages/#sending-a-test-push-notification-or-in-app-messages-a-classmargin-fix-namepush-inapp-testa
[38]: https://chrome.google.com/webstore/detail/grammarly-for-chrome/kbfnbcaeplbcioakkpcpgfkobkghlhen?hl=en
[39]: https://www.emailonacid.com/
[40]: https://litmus.com/

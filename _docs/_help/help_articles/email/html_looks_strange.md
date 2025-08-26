---
nav_title: HTML rendering in test emails
article_title: HTML Rendering in Test Emails
page_order: 2

page_type: solution
description: "This help article walks you through how to troubleshoot issues with HTML rendering in test emails."
channel: email
---

# Troubleshooting HTML rendering in test emails

If your [test email]({{site.baseurl}}/developer_guide/platform_wide/sending_test_messages/#sending-a-test-push-notification-or-in-app-messages-a-classmargin-fix-namepush-inapp-testa) looks off, we recommend first checking your HTML setup. Next, you can check for these issues:
* [Extension conflicts](#check-conflicts)
* [Email rendering](#check-rendering)
* [CSS inlining](#switch-css-inlining)

### Extension conflicts

Certain browser extensions may cause issues with our email editor. One example is [Grammarly](https://chrome.google.com/webstore/detail/grammarly-for-chrome/kbfnbcaeplbcioakkpcpgfkobkghlhen?hl=en)) when used with Google Chrome. If you're using one of these extensions, you should either: 
- Edit Braze emails in a browser that does not have Grammarly as a browser extension
- Contact your Braze account manager and ask to switch your email editors to HTML only or plain text. 

The plain text view removes your ```WYSIWYG``` (what you see is what you get) editor, so you should first confirm that all team members are comfortable with HTML before making this request.

### Email rendering

Emails render differently depending on browsers and email clients, so take note of which browsers and email clients you're experiencing issues with.

- Preview your emails using [Inbox Vision]({{site.baseurl}}/user_guide/message_building_by_channel/email/inbox_vision/#inbox-vision/) to see what your emails look like in different browsers and email clients.
- After you've identified which browsers or email clients are causing issues, let your developer team know that they'll need to modify their HTML and make edits to accommodate those browsers or email clients.

### CSS inlining

There are times when the previews in Inbox Vision still do not match what is sent with Braze. This may be caused by the difference in CSS inlining performed by Braze and by other tools. If you suspect that this is the case, contact your Braze account manager to ask for CSS inlining to be turned off.

Still need help? Open a [support ticket]({{site.baseurl}}/braze_support/).

_Last updated on December 21, 2021_


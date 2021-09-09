---
nav_title: Inbox Vision
article_title: Inbox Vision
page_order: 5
description: "Inbox Vision allows marketers to view their emails from the perspective of various email clients and mobile devices. This reference article covers how to set up and use Inbox Vision."
tool:
  - Dashboard
channel:
  - email

---

# Inbox Vision

Inbox Vision allows marketers to view their emails from the perspective of various email clients and mobile devices. Access Inbox Vision from the email editor by clicking **Preview and Test**.  It also allows you to spam test from the **Spam Test** tab.

## Test Your Email

To test your email message in Inbox Vision, click **Preview and Test** within the email composer. Braze then sends an HTML version of your email to various email clients used across the globe, which may take between two and ten minutes to complete.

Braze will then display screenshots of a sample, rendered HTML on desktops, mobile devices, and tablets. The devices in which screenshots are displayed are scrollable, to allow for better viewing. If you encounter unclear screenshots for certain email clients, click **Reprocess Screenshot** to create another screenshot.

If you run an Inbox Vision test, you will also receive a code analysis and spam testing results.

![inboxvision1][1]

Once you make changes to a template, you will need to click **Re-Run Test** to see the effect of the changes on the previews.

{% alert important %} In general, your email will not work with Inbox Vision if your email content relies on templating info such as user profile information. This is because Braze templates in an empty user when we send emails using this feature. {% endalert %}

## Code Analysis

Code analysis is a way for Braze to highlight issues that may exist with your HTML, showing the number of occurrences of each issue and providing insight into which HTML elements are not supported. This information can be found on the Inbox Vision preview page by selecting the list icon in the upper left-hand corner.

![inboxvision2][2]
![inboxvision3][3]

{% alert note %} Sometimes the code analysis will show up faster than the preview for a particular email client. This is because we wait until the email arrives in the inbox before taking the screenshot. {% endalert %}

## Spam Testing

[Spam testing][4] attempts to predict whether your email will land in spam folders or your customers' inboxes.  Spam testing runs across major spam filters, such as IronPort, SpamAssassin, and Barracuda, as well as major ISP filters such as Gmail.com and Outlook.com.

## Test Accuracy

All of our tests are run through actual email clients. We work hard to ensure that all renderings are as accurate as possible.  If you consistently see an issue with an email client, please [open a support ticket]({{site.baseurl}}/support_contact/).

[1]: {% image_buster /assets/img_archive/inboxvision1.png %}
[2]: {% image_buster /assets/img_archive/inboxvision2.png %}
[3]: {% image_buster /assets/img_archive/inboxvision3.png %}
[4]: {{site.baseurl}}/email_spam_testing/

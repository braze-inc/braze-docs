---
nav_title: Inbox Vision
article_title: Inbox Vision
page_order: 9
description: "This page covers how to set up Inbox Vision, a feature that allows marketers to view their emails from the perspective of various email clients and mobile devices."
tool:
  - Dashboard
channel:
  - email

---

# Inbox Vision

> Inbox Vision allows you to view your emails from the perspective of various email clients and mobile devices. For example, you can use Inbox Vision to test for differences across dark and light modes to confirm you've got your emails just right.

{% alert important %} 
In general, your email won't work with Inbox Vision if your email content relies on templating information, such as user profile information. This is because Braze templates in an empty user when we send emails using this feature.
{% endalert %}

## Testing your email in Inbox Vision

Your email must include a subject line and a valid sending domain in order to see these previews. Be mindful of how your email can render different on the desktop versus on mobile devices. As you view these previews, you can review your content and ensure that your email is displaying as intended.

To test your email message in Inbox Vision, do the following:

1. Go to your drag-and-drop editor or HTML email editor.
2. In your editor, select **Preview & Test**.
3. Select **Inbox Vision**. 
4. Select **Run Inbox Vision**. This may take between two to ten minutes to complete.
5. Next, select a tile to view the preview in more detail. These previews are grouped into these sections: **Web Clients**, **Application Clients**, and **Mobile Clients**.

![Overview of Inbox Vision for the HTML editor.][1]

{: start="6"}
6. Make changes to a template, if necessary.
7. Select **Re-run Test** to see the updated previews.

### Previewing as a user

When you preview the email as a random user, any specific settings or attributes associated with a user, such as their name or preferences, aren't saved for current or future previews. When you select a custom user, the preview shown in Inbox Vision may differ from the message preview elsewhere since this option uses specific user data to create the preview.

## Code analysis

Code analysis is a way for Braze to highlight issues that may exist with your HTML, showing the number of occurrences of each issue and providing insight into which HTML elements are not supported. 

### Viewing code analysis information

This information can be found on the **Inbox Vision** tab by selecting <i class="fas fa-list"></i> **List view**. This list view is available for HTML email templates only. If you're using drag-and-drop email templates, check the previews to resolve any possible issues instead.

![Example code analysis on the Inbox Vision preview.][2]

{% alert note %} 
Sometimes the code analysis will display faster than the preview for a particular email client. This is because Braze waits until the email arrives in the inbox before taking the screenshot. 
{% endalert %}

## Spam testing

Spam testing attempts to predict whether your email will land in spam folders or your customers' inboxes. Spam testing runs across major spam filters, such as IronPort, SpamAssassin, and Barracuda, as well as major internet service provider (ISP) filters such as Gmail.com and Outlook.com.

### Viewing spam test results

To check your spam test results, do the following:

1. Select the **Spam Testing** tab in the **Inbox Vision** section. The **Spam Test Result** table lists the spam filter name, status, and type.

![Spam Test Result table with three columns: Name, Status, and Type. There is a list of spam filters and ISP filters that have passed spam testing, indicating that the email campaign will not land in the spam folder.][4]

{: start="2"}
2. Review these results and making any adjustments to your email campaign.
3. Select **Re-run Test** to reload your spam test results.

## Test accuracy

All of our tests are run through actual email clients. Braze works hard to check that all renderings are as accurate as possible. If you consistently see an issue with an email client, open a [support ticket]({{site.baseurl}}/braze_support/).

[1]: {% image_buster /assets/img_archive/inboxvision1.png %}
[2]: {% image_buster /assets/img_archive/inboxvision2.png %}
[3]: {% image_buster /assets/img_archive/inboxvision4.png %}
[4]: {% image_buster /assets/img_archive/email_spam_testing.png %}

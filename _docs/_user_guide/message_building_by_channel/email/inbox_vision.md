---
nav_title: Inbox Vision
article_title: Inbox Vision
page_order: 9
description: "This reference article covers how to set up Inbox Vision, a feature that allows marketers to view their emails from the perspective of various email clients and mobile devices."
tool:
  - Dashboard
channel:
  - email

---

# Inbox Vision

> Inbox Vision allows marketers to view their emails from the perspective of various email clients and mobile devices. 

To test your email message in Inbox Vision, go to the **Preview and Test** tab in your Drag & Drop Editor or HTML email composer. Select **Inbox Vision** and click **Run Inbox Vision**.

![][3]{: style="max-width:80%;"}

Braze then sends an HTML version of your email to various email clients used across the globe, which may take between two and ten minutes to complete. You'll see these rendered HTML previews divided into three sections: **Web Clients**, **Application Clients**, and **Mobile Clients**. 

Select a tile to view the preview in more detail. Your email must include a subject line and a valid sending domain in order to see these previews. Be mindful of how your email can render different on the desktop versus on mobile devices. As you view these previews, you can review your content and ensure that your email is displaying as intended.

{% alert tip %}
Use Inbox Vision to test for differences across dark and light modes to ensure you get your emails just right!
{% endalert %}

![Overview of Inbox Vision for the HTML editor.][1]

Once you make changes to a template, click **Re-run Test** to see the updated previews.

{% alert important %} 
In general, your email will not work with Inbox Vision if your email content relies on templating info such as user profile information. This is because Braze templates in an empty user when we send emails using this feature. 
{% endalert %}

## Code analysis

Code analysis is a way for Braze to highlight issues that may exist with your HTML, showing the number of occurrences of each issue and providing insight into which HTML elements are not supported. This information can be found on the **Inbox Vision** tab by selecting <i class="fas fa-list"></i> **List view**. Note that the list view is available for HTML email templates only. If you're using drag-and-drop email templates, check the previews to resolve any possible issues instead.

![Example code analysis on the Inbox Vision preview.][2]

{% alert note %} 
Sometimes the code analysis will display faster than the preview for a particular email client. This is because Braze waits until the email arrives in the inbox before taking the screenshot. 
{% endalert %}

## Spam testing

Spam testing attempts to predict whether your email will land in spam folders or your customers' inboxes. Spam testing runs across major spam filters, such as IronPort, SpamAssassin, and Barracuda, as well as major internet service provider (ISP) filters such as Gmail.com and Outlook.com.

To check your spam test results, click the **Spam Testing** tab in the **Inbox Vision** section. The **Spam Test Result** table lists the spam filter name, status, and type.

![Spam Test Result table with three columns: Name, Status, and Type. There is a list of spam filters and ISP filters that have passed spam testing, indicating that the email campaign will not land in the spam folder.][4]

After reviewing these results and making any adjustments to your email campaign, click **Re-run Test** to reload your spam test results.

## Test accuracy

All of our tests are run through actual email clients. We work hard to ensure that all renderings are as accurate as possible. If you consistently see an issue with an email client, open a [support ticket]({{site.baseurl}}/braze_support/).

[1]: {% image_buster /assets/img_archive/inboxvision1.png %}
[2]: {% image_buster /assets/img_archive/inboxvision2.png %}
[3]: {% image_buster /assets/img_archive/inboxvision4.png %}
[4]: {% image_buster /assets/img_archive/email_spam_testing.png %}

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
In general, your email won't work with Inbox Vision if your email content relies on templating information, such as user profile information. This is because Braze templates in an empty user when we send emails using this feature.<br><br>Make sure you've added default values to any Liquid in your email message. If no default values are provided, you may receive a false positive or the test may fail to run.
{% endalert %}

## Testing your email in Inbox Vision

Your email must include a subject line and a valid sending domain in order to see these previews. Be mindful of how your email can render different on the desktop versus on mobile devices. As you view these previews, you can review your content and ensure that your email is displaying as intended.

To test your email message in Inbox Vision, do the following:

1. Go to your drag-and-drop editor or HTML email editor.
2. In your editor, select **Preview & Test**.
3. Select **Inbox Vision**.
4. Select **Run Inbox Vision**. This may take between two to ten minutes to complete.
5. Next, select a tile to view the preview in more detail. These previews are grouped into these sections: **Web Clients**, **Application Clients**, and **Mobile Clients**.

![Overview of Inbox Vision for the HTML editor.]({% image_buster /assets/img_archive/inboxvision1.png %})

{: start="6"}
6. Make changes to a template, if necessary.
7. Select **Re-run Test** to see the updated previews.

{% alert note %}
Inbox Vision isn't supported if your email message includes [abort logic]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/aborting_messages) as these emails are rendered as static content.
{% endalert %}

### Previewing as a user

When you preview the email as a random user, any specific settings or attributes associated with a user, such as their name or preferences, aren't saved for current or future previews. When you select a custom user, the preview shown in Inbox Vision may differ from the message preview elsewhere since this option uses specific user data to create the preview

## Code analysis

Code analysis is a way for Braze to highlight issues that may exist with your HTML, showing the number of occurrences of each issue and providing insight into which HTML elements are not supported.

### Viewing code analysis information

This information can be found on the **Inbox Vision** tab by selecting <i class="fas fa-list"></i> **List view**. This list view is available for HTML email templates only. If you're using drag-and-drop email templates, check the previews to resolve any possible issues instead.

![Example code analysis on the Inbox Vision preview.]({% image_buster /assets/img_archive/inboxvision2.png %})

{% alert note %}
Sometimes the code analysis will display faster than the preview for a particular email client. This is because Braze waits until the email arrives in the inbox before taking the screenshot.
{% endalert %}

## Spam testing

Spam testing attempts to predict whether your email will land in spam folders or your customers' inboxes. Spam testing runs across major spam filters, such as IronPort, SpamAssassin, and Barracuda, as well as major internet service provider (ISP) filters such as Gmail.com and Outlook.com.

### Viewing spam test results

To check your spam test results, do the following:

1. Select the **Spam Testing** tab in the **Inbox Vision** section. The **Spam Test Result** table lists the spam filter name, status, and type.

![Spam Test Result table with three columns: Name, Status, and Type. There is a list of spam filters and ISP filters that have passed spam testing, indicating that the email campaign will not land in the spam folder.]({% image_buster /assets/img_archive/email_spam_testing.png %})

{: start="2"}
2. Review these results and making any adjustments to your email campaign.
3. Select **Re-run Test** to reload your spam test results.

## Accessibility testing

Accessibility testing in Inbox Vision highlights accessibility issues that may exist with your email to provide insight into which elements are not meeting accessibility standards. It analyzes your email content against some Web Content Accessibility Guidelines ([WCAG](https://www.w3.org/WAI/standards-guidelines/wcag/)). WCAG is a set of internationally recognized technical standards developed by the World Wide Web Consortium (W3C) to make web content more accessible to people with disabilities. 

### How it works

When you run an Inbox Vision test, the tool automatically checks for common email accessibility issues in the [WCAG 2.2 AA rule set](https://www.w3.org/WAI/WCAG22/quickref/?versions=2.2&currentsidebar=%23col_customize&levels=aaa), such as missing alt text, insufficient color contrast, and improper heading structure, then categorizes the severity of each issue to help you prioritize fixes. 

{% alert important %}
Accessibility Testing may be used to support Customer's compliance efforts of regulations or laws such as the [European Accessibility Act](https://www.braze.com/resources/articles/european-accessibility-at-what-it-means-for-marketers), however Customer acknowledges that Braze makes no representations or warranties with respect to whether or not use of Accessibility Testing satisfies Customer's compliance obligations, and disclaims all liability in relation thereto.
{% endalert %}

### Viewing accessibility testing results

Accessibility testing will generate results for each rule as passed, failed, or needs review in the **Accessibility Testing** tab. Each rule is categorized using POUR (Perceivable, Operable, Understandable, Robust), which are the four main principles behind WCAG.

#### POUR categories

Issues are categorized under the four foundational [POUR principles](https://www.w3.org/WAI/WCAG22/Understanding/intro#understanding-the-four-principles-of-accessibility): Perceivable, Operable, Understandable, and Robust. Each principle addresses a different aspect of accessible design.

| Principle | Definition |
| --- | --- |
| Perceivable | Information and user interface components must be presentable to users in ways they can perceive.<br><br>Users must be able to perceive the information being presented (it can't be invisible to all of their senses). |
| Operable | User interface components and navigation must be operable.<br><br>Users must be able to operate the interface (the interface cannot require interaction that a user cannot perform). |
| Understandable | Information and the operation of the user interface must be understandable.<br><br>Users must be able to understand the information as well as the operation of the user interface (the content or operation cannot be beyond their understanding). |
| Robust | Content must be robust enough that it can be interpreted reliably by a wide variety of user agents, including assistive technologies.<br><br>Users must be able to access the content as technologies advance (as technologies and user agents evolve, the content should remain accessible). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Severity levels

Inbox Vision classifies accessibility issues by severity to help you prioritize remediation efforts.

| Status | Definition |
| --- | --- |
| Critical | Issues that can block access to content or functionality for users with disabilities. These are the most severe and should be prioritized for fixing. |
| Serious | Issues that can cause significant barriers but may not completely block access. These should be addressed promptly. |
| Moderate | Issues that may cause some difficulty for users with disabilities, but are less likely to block access entirely. |
| Minor | Issues that have a relatively low impact on accessibility and may cause only minor inconvenience. |
| Needs review | Unable to detect if there might be an issue or not. This can occur when we are unable to determine the contrast ratio as the text is placed on a background image. This will need to be manually reviewed because it cannot be automatically determined. |
| Passed | Passed WCAG A, AA, or accessibility best practice. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert important %}
The email drag-and-drop editor currently does not support setting a document `<title>` element. As a result, the accessibility scanner will always fail this check.<br><br>
We're tracking this limitation for future improvements. If this affects your workflows or your users, [share your feedback]({{site.baseurl}}/user_guide/administrative/access_braze/navigation/#sharing-feedback) so we can prioritize the most impactful fixes.
{% endalert %}

### Understanding automated accessibility testing

{% multi_lang_include accessibility/automated_testing.md %}

## Test accuracy

All of our tests are run through actual email clients. Braze works hard to check that all renderings are as accurate as possible. If you consistently see an issue with an email client, open a [support ticket]({{site.baseurl}}/braze_support/).

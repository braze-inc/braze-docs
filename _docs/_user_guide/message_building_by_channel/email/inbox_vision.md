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

> Inbox Vision lets you view your emails from the perspective of various email clients and mobile devices. For example, you can test dark and light mode differences to confirm your emails render as intended.

{% alert important %}
Inbox Vision may not work if your email content relies on templating information such as user profile data. Braze templates an empty user when sending emails for this feature.<br><br>Add default values to any Liquid in your email message. Without defaults you may receive a false positive or the test may fail.
{% endalert %}

## Testing your email in Inbox Vision

Include a subject line and a valid sending domain to view previews. Be mindful of desktop versus mobile rendering differences. Use the previews to confirm the email appears as intended.

To test your email message in Inbox Vision:

1. Go to your drag-and-drop editor or HTML email editor.
2. In your editor, select **Preview & Test**.
3. Select **Inbox Vision**.
4. Select **Run Inbox Vision**. This takes up to ten minutes.
5. Next, select a tile to view the preview in more detail. These previews are grouped into these sections: **Web Clients**, **Application Clients**, and **Mobile Clients**.

![Overview of Inbox Vision for the HTML editor.]({% image_buster /assets/img_archive/inboxvision1.png %})

{: start="6"}
6. Make changes to a template, if necessary.
7. Select **Re-run Test** to see the updated previews.

{% alert note %}
Inbox Vision doesn't support email messages that include [abort logic]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/aborting_messages) because these emails render as static content.
{% endalert %}

### Previewing as a user

When you preview as a random user, Inbox Vision doesn't save user-specific settings or attributes (such as name or preferences). When you select a custom user, the Inbox Vision preview may differ from other previews because it uses specific user data.

## Code analysis

Code analysis highlights potential HTML issues, shows the number of occurrences, and indicates unsupported HTML elements.

### Viewing code analysis information

Find this information on the **Inbox Vision** tab by selecting <i class="fas fa-list"></i> **List view**. List view is available only for HTML email templates. For drag-and-drop templates, use previews to resolve issues instead.

![Example code analysis on the Inbox Vision preview.]({% image_buster /assets/img_archive/inboxvision2.png %})

{% alert note %}
Code analysis can appear faster than the preview for a particular client because Braze waits until the email arrives before taking the screenshot.
{% endalert %}

## Spam testing

Spam testing predicts whether your email lands in spam folders or inboxes. Braze runs tests across major spam filters (IronPort, SpamAssassin, Barracuda) and major ISP filters (Gmail.com, Outlook.com).

### Viewing spam test results

To check your spam test results:

1. Select the **Spam Testing** tab in the **Inbox Vision** section. The **Spam Test Result** table lists the spam filter name, status, and type.

![Spam Test Result table with three columns: Name, Status, and Type. There is a list of spam filters and ISP filters that have passed spam testing, indicating that the email campaign will not land in the spam folder.]({% image_buster /assets/img_archive/email_spam_testing.png %})

{: start="2"}
2. Review these results and making any adjustments to your email campaign.
3. Select **Re-run Test** to reload your spam test results.

## Accessibility testing

Accessibility testing highlights potential accessibility issues in your email and shows which elements don't meet standards. Braze analyzes content against select Web Content Accessibility Guidelines ([WCAG](https://www.w3.org/WAI/standards-guidelines/wcag/)), a set of internationally recognized standards developed by the W3C to make web content more accessible.

### How it works

When you run Inbox Vision, Braze automatically checks for common accessibility issues in the [WCAG 2.2 AA rule set](https://www.w3.org/WAI/WCAG22/quickref/?versions=2.2&currentsidebar=%23col_customize&levels=aaa) (such as missing alt text, insufficient color contrast, improper heading structure) and categorizes severity to help you prioritize fixes. 

{% alert important %}
Accessibility Testing may be used to support Customer's compliance efforts of regulations or laws such as the [European Accessibility Act](https://www.braze.com/resources/articles/european-accessibility-at-what-it-means-for-marketers); however, Customer acknowledges that Braze makes no representations or warranties with respect to whether or not use of Accessibility Testing satisfies Customer's compliance obligations, and disclaims all liability in relation thereto.
{% endalert %}

### Viewing accessibility testing results

Accessibility testing generates results for each rule as passed, failed, or needs review in the **Accessibility Testing** tab. Braze categorizes each rule using POUR (Perceivable, Operable, Understandable, Robust), the four principles behind WCAG.

#### POUR categories

Inbox Vision categorizes issues under the four foundational [POUR principles](https://www.w3.org/WAI/WCAG22/Understanding/intro#understanding-the-four-principles-of-accessibility): Perceivable, Operable, Understandable, and Robust.

| Principle | Definition |
| --- | --- |
| Perceivable | Information and user interface components must be presentable to users in ways they can perceive.<br><br>Users must be able to perceive the information being presented (it can't be invisible to all of their senses). |
| Operable | User interface components and navigation must be operable.<br><br>Users must be able to operate the interface (the interface cannot require interaction that a user cannot perform). |
| Understandable | Information and the operation of the user interface must be understandable.<br><br>Users must be able to understand the information as well as the operation of the user interface (the content or operation cannot be beyond their understanding). |
| Robust | Content must be robust enough that it can be interpreted reliably by a wide variety of user agents, including assistive technologies.<br><br>Users must be able to access the content as technologies advance (as technologies and user agents evolve, the content should remain accessible). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Severity levels

Inbox Vision classifies accessibility issues by severity to help you prioritize remediation.

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
The drag-and-drop editor does not support setting a document `<title>` element, so the accessibility scanner always fails this check.<br><br>We are tracking this limitation for improvements. If this affects your workflows or your users, [share your feedback]({{site.baseurl}}/user_guide/administrative/access_braze/navigation/#sharing-feedback) so we can prioritize impactful fixes.
{% endalert %}

### Understanding automated accessibility testing

{% multi_lang_include accessibility/automated_testing.md %}

## Test accuracy

Braze runs tests through actual email clients and works to ensure renderings are accurate. If you consistently see an issue with a client, open a [support ticket]({{site.baseurl}}/braze_support/).

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

> In Inbox Vision, you can customize which email clients are included in your preview. Choose from our list of popular clients, like Gmail and Yahoo, or build your own list tailored to your audience.

To use Inbox Vision, your email must include a subject line. Consider how your email can render differently on the desktop versus on mobile devices. As you review these previews, you can check that your email displays as intended.

{% alert important %}
Every company has 750 previews per calendar month shared across all workspaces. Each preview shows how your email appears in a particular email client and device combination. For example, `Gmail.com Chrome | Windows 10` is counted as one preview. When the preview capacity is reached, you must wait until the following month for your preview capacity to reset. Contact your account manager if you have any questions about this capacity.
{% endalert %}

## Considerations

In general, your email won’t work with Inbox Vision if your email content relies on templating information, such as user profile information. This is because Braze templates an empty user when we send emails using this feature.

You can resolve this by adding default values or any values to the Liquid in your email message before you run Inbox Vision. When you finish testing in Inbox Vision, revert to the original email message. If no values are provided, the test may fail to render the previews successfully.

Your company has a limit on how many emails you can preview with Inbox Vision. You can monitor this in the **Email Previews** tab of Inbox Vision.

## Previewing your emails

To test your email message in Inbox Vision, do the following:

1. Go to your drag-and-drop editor or HTML email editor.
2. In your editor, select **Preview & Test**.
3. Select **Inbox Vision**.
4. In the **Preview settings** section, you can select the email clients to render your preview and save this group for future runs by enabling “Remember Selection”. Otherwise, Braze defaults to the top 20 most popular previews. These previews are grouped by clients.

![The option to select email clients to preview.]({% image_buster /assets/img/select_email_preview_inbox_vision.png %}){: style="max-width:85%;"}

{:start="5"}
5. Select **Run Inbox Vision**. This may take between two to ten minutes to complete.

![Email previews for mobile clients on Gmail and iOS.]({% image_buster /assets/img/inbox_vision_previews.png %})

{:start="6"}
6. Make changes to a template, if necessary.
7. Select **Re-run Test** to see the updated previews.

{% alert note %}
Inbox Vision isn’t supported if your email message includes abort logic, as these emails are rendered as static content.
{% endalert %}

## Spam testing

Spam testing attempts to predict whether your email will land in spam folders or your customers’ inboxes. Spam testing runs across major spam filters, such as IronPort, SpamAssassin, and Barracuda, as well as major internet service provider (ISP) filters such as Gmail.com and Outlook.com.

![Spam Test Result table with three columns: Name, Status, and Type. There is a list of spam filters and ISP filters that have passed spam testing, indicating that the email campaign will not land in the spam folder.]({% image_buster /assets/img_archive/email_spam_testing.png %})

### Viewing spam test results

To check your spam test results, do the following:

1. Select the **Spam Testing** tab in the **Inbox Vision** section. The **Spam Test Result** table lists the spam filter name, status, and type.
2. Review these results and make any adjustments to your email campaign.
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

## Best practices

### Review your email subscriber list

Reference the [email insights dashboard]({{site.baseurl}}/user_guide/analytics/dashboard/email_performance_dashboard#email-insights-dashboard) to determine the most popular device type and providers where your subscribers are engaging. If you need more granularity, such as the browser, device model, and more, you can leverage your [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents) data or [Query Builder]({{site.baseurl}}/user_guide/analytics/query_builder) to retrieve this level of detail about your users’ recent email engagement.

Otherwise, Braze defaults to the top 20 previews based on general industry and expert data, which covers the majority of where your subscribers are engaging with your emails. If your data analysis points to other, more popular previews, you can define a default set of previews every time you run Inbox Vision.

### Select meaningful previews and impacted previews

If your business is primarily based in the US, there may be specific previews, such as international previews like GMX.de, that are only used by a nominal number of users. We recommend prioritizing and optimizing for inboxes with a sizable subscriber impact and reserving your previews for higher-impact inboxes.

When making fixes that affect specific previews, be sure to select only the impacted previews to prevent consuming unused previews.

### Run Inbox Vision on the final email version

We suggest running Inbox Vision when the email message is production-ready or close to it. This allows you to reduce the number of generated previews, as the email will go through multiple iterations before it’s finalized and ready to be sent to users.

Running Inbox Vision every time you make a single edit or change can quickly consume previews. We suggest making all the necessary changes to the email first, and then running Inbox Vision to preview how all your changes can affect the rendering of your email across environments.

These practices help conserve previews by focusing on high-impact client previews and minimizing redundant or unused previews.

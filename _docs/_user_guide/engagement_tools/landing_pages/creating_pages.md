---
nav_title: Creating Landing Pages
article_title: Creating Landing Pages
description: "This article covers how to create and customize Braze landing pages with the drag-and-drop editor."
page_order: 0
---

# Creating landing pages

> Learn how to create and customize a landing page using the drag-and-drop editor, so you can grow your audience and collect preferences directly in Braze.

## Creating a landing page

### Step 1: Create a new draft

Go to **Messaging** > **Landing Pages**, then select **Create landing page**. You can also click the name of an existing landing page to duplicate or make changes to it.

![The landing pages section in the Braze dashboard.]({% image_buster /assets/img/landing_pages/landing-pages-homepage.png %})

### Step 2: Enter the page details

#### General details

The landing page name and description are used to search for the page in your internal workspace. These won't be visible to your customers.

#### Site details

Set up metatags to customize how your page appears on the browser tab and optimize for search engine results. These will be visible to your customers.

We suggest following these best practices:

| Detail | Description | Recommendations |
| --- | --- |
| Site title | The title that displays on the browser tab. | Use up to 60 characters. |
| Meta description | A text snippet that displays in search results. | Use between 140-160 characters.|
| Favicon | The icon that appears next to the site title on the browser tab. | Use an aspect ratio of 1:1, and a supported file type of PNG, JPEG, or ICO. |
| Page URL | This is URL path to your landing page. This value is also referenced when using [landing page liquid tags]({{site.baseurl}}/user_guide/engagement_tools/landing_pages/tracking_users) that you can embed in a message to automatically identify when they submit your form.| This value must be unique across your workspace. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### Step 3: Customize the page

If you haven't already, select **Save as draft**. To start customizing your page, select **Edit landing page**. The drag-and-drop editor will preload with a default template that you can customize to fit your use case.

![An example landing page being created in the drag-and-drop editor.]({% image_buster /assets/img/landing_pages/template.png %})

#### Page container styles

You can set styles to be applied across all relevant component blocks in your landing page from the **Page container** tab. These styles will be used everywhere on your page except where you override them with a specific block.

We recommend setting up page container-level styles before you customize styles at the block level. 

You can also add a background image for the entire page. If you use a background image, double-check that text placed over it is still readable for a wide range of users. You may need to use a high-contrast color for your text. Refer to [Accessibility considerations](#accessibility-considerations) in this article for more.

![The 'Page container' section with options to customize background images, colors, border details, and content styling.]({% image_buster /assets/img/landing_pages/page_container.png %}){: style="max-width:30%" }

{% alert note %}
Braze editors allow you to select custom color combinations. Keep in mind that certain color choices can negatively affect accessibility. Choose your colors carefully to make sure your content is readabile and compliant with accessibility standards.
{% endalert %}

#### Landing page blocks

The editor uses two types of components for landing page composition: [basic blocks](#basic-blocks) and [form blocks](#form-blocks). All blocks must be placed in a row.

<table style="width: 100%; table-layout: fixed;">
    <tr>
        <th style="width: 50%;">Basic blocks</th>
        <th style="width: 50%;">Form blocks</th>
    </tr>
    <tr>
        <td style="text-align: center;">
            <img src="{% image_buster /assets/img/landing_pages/landing_page_blocks.png %}" alt="Landing page blocks." style="max-width: 90%; height: auto; border:none;">
        </td>
        <td style="text-align: center;">
            <img src="{% image_buster /assets/img/landing_pages/landing_page_form_blocks.png %}" alt="Landing page form blocks" style="max-width: 90%; height: auto; border:none;">
        </td>
    </tr>
</table>
{: .reset-td-br-1 role="presentation"}

##### Basic blocks

You can use these blocks to add content and customize the layout of your landing page.

| Block Type   | Description |
|-------------|-------------|
| Title       | A text block for adding a heading or title to your content. Useful for structuring sections and improving readability. |
| Paragraph   | A text block for longer descriptions or additional context. Supports rich text formatting. |
| Button      | A clickable element that directs users to a specified action, such as opening a link or submitting a form. |
| Image       | A block for displaying images. You can upload an image or provide a URL to reference an external source. Remember to provide [alt text](#alt-text) for all meaningful images.  |
| Link        | A hyperlink that users can click to navigate to a specified URL. Can be embedded within text or standalone. |
| Spacer      | An invisible block that adds vertical spacing between elements for improved layout and readability. |
| Custom Code | A block that allows you to insert and run custom HTML, CSS, or JavaScript for advanced customization. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

##### Form blocks

You can use these blocks to create a form that links user-submitted data to their profile in Braze. Keep in mind, if you use form blocks, you'll also need to create an additional landing page for the confirmation state.

![A form block that registers a new customer and will send a discount code to their email.]({% image_buster /assets/img/landing_pages/form.png %}){: style="max-width:70%;"}

| Block Type     | Description |
|---------------|-------------|
| Email Capture | A form field for email addresses. When submitted, the email address is added to that user's profile in Braze. |
| Phone Capture | A form field for phone numbers. When submitted, the user is subscribed to your SMS or WhatsApp subscription group. |
| Input Field   | A form field that supports standard attributes (such as first and last name) or a custom attribute string of your choice. |
| Dropdown      | Users can select an item from a pre-defined list. You can add any custom attribute strings to the list. |
| Checkbox      | If a user checks the box, the block's attribute is set to `true`. If left unchecked, it's attribute is set to `false`. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert note %}
Form blocks in landing pages are a flexible way to collect information—but they currently have some accessibility limitations. For example, there’s no built-in way to group related fields or programmatically associate field labels with inputs. We are actively tracking and planning remediations for these issues. In the meantime, we recommend reviewing our [accessibility best practices](#best-practices) to help guide your content choices.
{% endalert%}

### Step 4: Create a confirmation page (optional)

If you added a [form](#form-block) to your landing page in the previous step, create an additional landing page for the confirmation state. Then, add the **Open web URL** link to the button that submits the form. Map this button to your confirmation page.

Be sure to embed its [landing page Liquid tag]({{site.baseurl}}/user_guide/engagement_tools/landing_pages/tracking_users) into your message. With this tag, Braze can automatically identify and update existing user profiles when they submit the form.

### Step 5: Preview the page

You can preview your landing page in the editor's **Preview** tab. After saving your landing page as a draft, you can visit the URL by going to **Landing Pages** and selecting **Copy URL** next to your landing page. You can also share the URL with collaborators.

![A landing page with the menu open to show the "Copy URL" option.]({% image_buster /assets/img/landing_pages/copy-url.png %})

When you're ready, select **Publish Landing Page**.

## Handling form submission errors

If a user inputs an invalid form value (such as unaccepted special characters), they will see a generic error indicator that isn’t customizable and won’t be able to submit the form. You can view the error behavior on the landing page preview.

{% alert note %}
This error behavior has known accessibility issues. The default indicator is a red outline and subtle vibration on the input field—without a visible error message or clear indication of required fields. These patterns aren’t accessible to screen reader users or those with cognitive or visual disabilities. For more, see [Known issues](#known-issues).
{% endalert %}

## Viewing analytics

To analyze the effectiveness of your landing page, go to **Messaging** > **Landing Pages**, then selected a landing page you've published. Here, you can track the number of page views, page clicks, page submissions, and the submission rates for your landing page.

![The analytics section for a landing page.]({% image_buster /assets/img/landing_pages/analytics.png %})

## Accessibility considerations

Accessible landing pages help everyone—including people with disabilities—understand and interact with your content. The Braze landing page editor has some known accessibility issues. We're actively working on addressing [known issues](#known-issues), and welcome feedback to help guide our priorities. 

In the meantime, there are still meaningful steps you can take to improve accessibility in your content. Learn more in our dedicated [accessibilty]({{site.baseurl}}/help/accessibility/) article.

### Best practices

#### Add alt text to meaningful images {#alt-text}

Alt text is a short description of an image that screen readers announce to users who can’t see the screen. If your image is meaningful—like a visual of a product, chart, or call to action—include clear and concise alt text so everyone understands what’s being shown. This supports users who are blind, have low vision, or rely on text-to-speech tools. (WCAG 1.1.1)

If you use an image as a submit button—like a “Buy now” icon—add alt text that clearly describes the action it performs. Otherwise, screen reader users won’t know what clicking the image will do.

#### Write in plain, clear language

Use short sentences and simple words that are easy to understand. This helps users who have cognitive disabilities, are reading in a second language, or are quickly scanning. Aim for a middle school reading level, and avoid jargon or overly complex sentence structures. (WCAG 3.1.5)

#### Break content into clear sections

Organize your landing page using headings and group related content together. This helps users understand what each part of the page is about and lets screen reader users jump between sections. Without headings, the content can feel like a wall of text. (WCAG 2.4.6)

#### Label all form fields clearly

Every form input—like name, email, or phone number—should have a visible label that explains what users need to enter. Placeholder text is not a substitute. Clear labels help users who rely on screen readers or have cognitive impairments complete forms accurately. (WCAG 1.3.1, 3.3.2)

#### Use high contrast between text and background

Make sure text stands out clearly from the background color. Low-contrast text can be hard to read for users with visual impairments or in bright environments. For most text, a contrast ratio of at least 4.5:1 is recommended. (WCAG 1.4.3)

### Known issues

Some accessibility features are not yet supported in the Braze landing page editor. These limitations may impact the experience for users who rely on assistive technology:

- No support for customizing ARIA roles or labels (WCAG 4.1.2)
- Decorative images can’t be marked as such (WCAG 1.1.1)
- Language metadata (`lang` attribute) is always set to English (WCAG 3.1.1)
- No way to group related form fields with `<fieldset>` or `<legend>` (WCAG 1.3.1)
- Heading levels can’t be set manually (WCAG 2.4.6)
- Error states for form fields aren’t surfaced visually or programmatically (WCAG 3.3.1, 3.3.3)

These issues are being tracked for future improvements. If these limitations affect your workflows or users, [share your feedback]({{site.baseurl}}/user_guide/administrative/access_braze/navigation/#sharing-feedback) so we can prioritize the most impactful fixes.
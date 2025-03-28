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

The editor uses two types of components for landing page composition: [basic blocks](#basic-blocks) and [form blocks](#form-blocks). All blocks must be placed in a row.

![The 'Build' section containing 'Rows' and 'Form Blocks'.]({% image_buster /assets/img/landing_pages/dnd.png %}){: style="max-width:35%;"}

#### Basic blocks

You can use these blocks to add content and customize the layout of your landing page.

| Block Type   | Description |
|-------------|-------------|
| Title       | A text block for adding a heading or title to your content. Useful for structuring sections and improving readability. |
| Paragraph   | A text block for longer descriptions or additional context. Supports rich text formatting. |
| Button      | A clickable element that directs users to a specified action, such as opening a link or submitting a form. |
| Image       | A block for displaying images. You can upload an image or provide a URL to reference an external source. |
| Link        | A hyperlink that users can click to navigate to a specified URL. Can be embedded within text or standalone. |
| Spacer      | An invisible block that adds vertical spacing between elements for improved layout and readability. |
| Custom Code | A block that allows you to insert and run custom HTML, CSS, or JavaScript for advanced customization. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Form blocks

You can use these blocks to create a form that links user-submitted data to their profile in Braze. Keep in mind, if you use form blocks, you'll also need to create an additional landing page for the confirmation state.

![A form block that registers a new customer and will send a discount code to their email.]({% image_buster /assets/img/landing_pages/form.png %}){: style="max-width:70%;"}

| Block Type     | Description |
|---------------|-------------|
| Email Capture | A form field for email addresses. When submitted, the email address is added to that user's profile in Braze. |
| Phone Capture | A form field for phone numbers. When submitted, the user is subscribed to your SMS or Whatsapp subscription group. |
| Input Field   | A form field that supports standard attributes (such as first and last name) or a custom attribute string of your choice. |
| Dropdown      | Users can select an item from a pre-defined list. You can add any custom attribute strings to the list. |
| Checkbox      | If a user checks the box, the block's attribute is set to `true`. If left unchecked, it's attribute is set to `false`. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert important %}
After creating a landing page with a form, be sure to embed its [landing page Liquid tag]({{site.baseurl}}/user_guide/engagement_tools/landing_pages/tracking_users) into your message. With this tag, Braze can automatically identify and update existing user profiles when they submit the form.
{% endalert %}

#### Page container styles

You can set styles to be applied across all relevent component blocks in your landing page from the **Page container** tab. These styles will be used everywhere on your page except where you override them with a specific block.

We recommend setting up page container-level styles before you customize styles at the block level. You can also add a background image for the entire page.

![The 'Page container' section with options to customize background images, colors, border details, and content styling.]({% image_buster /assets/img/landing_pages/page_container.png %}){: style="max-width:30%;"}

### Step 4: Create a confirmation page

If you added a [form](#form-block) to your landing page in the previous step, create an additional landing page for the confirmation state, then add the **Open web URL** link to the button that submits the form. Otherwise, continue to the next step.

### Step 5: Preview the page

You can preview your landing page in the editor's **Preview** tab. After saving your landing page as a draft, you can visit the URL by going to **Landing Pages** and selecting **Copy URL** next to your landing page. You can also share the URL with collaborators.

![A landing page with the menu open to show the "Copy URL" option.]({% image_buster /assets/img/landing_pages/copy-url.png %})

When you're ready, select **Publish Landing Page**.

## Handling form submission errors

If a user inputs an invalid form value (such as unaccepted special characters), they will see a generic error indicator that isn't customizable and won't be able to submit the form. You can view the error behavior on the landing page preview.

## Viewing analytics

To analyze the effectiveness of your landing page, go to **Messaging** > **Landing Pages**, then selected a landing page you've published. Here, you can track the number of page views, page clicks, page submissions, and the submission rates for your landing page.

![The analytics section for a landing page.]({% image_buster /assets/img/landing_pages/analytics.png %})

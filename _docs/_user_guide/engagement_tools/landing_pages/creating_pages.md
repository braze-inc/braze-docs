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
| URL handle | This is the link users will click to navigate to your landing page. This link is also used to generate [landing page liquid tags]({{site.baseurl}}/user_guide/engagement_tools/landing_pages/identifying_users) that you can embed in a message to automatically identify when they submit your form.| This handle must be unique. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### Step 3: Customize the page

If you haven't already, select **Save as draft**. To start customizing your page, select **Edit landing page**.

![The landing page previewing showing the option to edit the page.]({% image_buster /assets/img/landing_pages/select-edit-landing-page.png %})

The drag-and-drop editor will preload with a default template that you can customize to fit your use case.

![An example landing page being created in the drag-and-drop editor.]({% image_buster /assets/img/landing_pages/editor.png %})

#### Drag-and-drop blocks

The editor uses two types of components for landing page composition: rows and blocks. All blocks must be placed in a row.

![The 'Build' section containing 'Rows' and 'Form Blocks'.]({% image_buster /assets/img/landing_pages/dnd.png %}){: style="max-width:35%;"}

#### Form block

Use various form block components to log custom and standard profile attributes and custom events. The input field form block can log both standard and custom attributes for your users, and the phone capture and email capture form blocks can capture phone and email fields for your users' form submissions. Button actions can be logged as custom attributes, custom events, or both on form submission. 

If you include a form block, each button will have the option to submit the form. However, you'll need to create a separate landing page for the [confirmation state](#confirmation-state).

![A form block that registers a new customer and will send a discount code to their email.]({% image_buster /assets/img/landing_pages/form.png %}){: style="max-width:70%;"}

{% alert tip %}
After creating a landing page with a form, be sure to embed its [landing page liquid tag]({{site.baseurl}}/user_guide/engagement_tools/landing_pages/identifying_users) into your message. With this tag, Braze can automatically identify and update existing user profiles when they submit the form.
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

## Linking to your landing page

You can include a link to the landing page in any channel by copying and pasting the link into a Braze message or social media campaign.

## Handling form submission errors

If a user inputs an invalid form value (such as unaccepted special characters), they will see a generic error indicator that isn't customizable and won't be able to submit the form. You can view the error behavior on the landing page preview.

## Viewing analytics

To analyze the effectiveness of your landing page, go to **Messaging** > **Landing Pages**, then selected a landing page you've published. Here, you can track the number of page views, page clicks, page submissions, and the submission rates for your landing page.

![The analytics section for a landing page.]({% image_buster /assets/img/landing_pages/analytics.png %})

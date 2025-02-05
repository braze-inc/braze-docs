---
nav_title: Creating Landing Pages
article_title: Creating Landing Pages
description: "This article covers how to create and customize Braze landing pages with the drag-and-drop editor."
page_order: 0
alias: /landing_pages/drag_and_drop/
---

# Creating landing pages

> Learn how to create and customize a landing page using the drag-and-drop editor, so you can grow your audience and collect preferences directly in Braze.

## Prerequisites

Before you can access, create, and publish landing pages, you either need administrator permissions or all of the following permissions:

- Access Landing Pages
- Create Landing Page Drafts
- Publish Landing Pages

## Creating a landing page

### Step 1: Create a new draft

Go to **Messaging** > **Landing Pages** and select **Create landing page**, or select the name of an existing one to duplicate it or make changes to it.

![The "Landing Pages" homepage.]({% image_buster /assets/img/landing_pages/create.png %}){: style="max-width:90%;"}

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
| URL handle | This is the link users will click to navigate to your landing page. | This must be unique. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### Step 3: Customize the page

Select **Launch Editor** to start designing your landing page in the drag-and-drop editor. The editor will preload with a default template that you can customize to fit your use case.

![Landing page template with a form for customer sign-up.]({% image_buster /assets/img/landing_pages/template.png %}){: style="max-width:90%;"}

#### Drag-and-drop blocks

The editor uses two types of components for landing page composition: rows and blocks. All blocks must be placed in a row.

![The "Build" editor section containing "Rows" and "Form Blocks".]({% image_buster /assets/img/landing_pages/dnd.png %}){: style="max-width:30%;"}

#### Form block

Use various form block components to log custom and standard profile attributes and custom events. The input field form block can log both standard and custom attributes for your users, and the phone capture and email capture form blocks can capture phone and email fields for your users' form submissions. Button actions can be logged as custom attributes, custom events, or both on form submission. 

If you include a form block, each button will have the option to submit the form. However, you'll need to create a separate landing page for the [confirmation state](#confirmation-state).

![A form block that registers a new customer and will send a discount code to their email.]({% image_buster /assets/img/landing_pages/form.png %}){: style="max-width:70%;"}

#### Page container styles

You can set styles to be applied across all relevent component blocks in your landing page from the **Page container** tab. These styles will be used everywhere on your page except where you override them with a specific block.

We recommend setting up page container-level styles before you customize styles at the block level. You can also add a background image for the entire page.

![The page container with options to customize background images, colors, border details, and content styling.]({% image_buster /assets/img/landing_pages/page_container.png %}){: style="max-width:30%;"}

### Step 4: Create a confirmation page

If you added a [form](#form-block) to your landing page in the previous step, create an additional landing page for the confirmation state, then add the **Open web URL** link to the button that submits the form. Otherwise, continue to the next step.

### Step 5: Preview the page

You can preview your landing page in the editor's **Preview** tab. After saving your landing page as a draft, you can visit the URL by going to **Landing Pages** and selecting **Copy URL** next to your landing page. You can also share the URL with collaborators.

If you're satisfied with the landing page, select **Publish Landing Page**.

![A landing page with the menu open to show the "Copy URL" option.]({% image_buster /assets/img/landing_pages/url_handle.png %}){: style="max-width:90%;"}

## Linking to your landing page

You can include a link to the landing page in any channel by copying and pasting the link into a Braze message or social media campaign.

## Handling form submission errors

If a user inputs an invalid form value (such as unaccepted special characters), they will see a generic error indicator that isn't customizable and won't be able to submit the form. You can view the error behavior on the landing page preview.

## Merging users created from your landing page

Each form submission on a landing page creates a new anonymous user profile in Braze. If a user with the same email address already exists, you can merge the new user profile into the existing profile using the [`/users/merge`]({{site.baseurl}}/api/endpoints/user_data/post_users_merge#merging-unidentified-user) endpoint. To learn about the different ways to deduplicate users in Braze, see [Duplicate users]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/duplicate_users).

User merging will be handled automatically via a liquid tag in the future. 

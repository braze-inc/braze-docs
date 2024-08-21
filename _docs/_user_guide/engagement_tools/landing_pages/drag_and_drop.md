---
nav_title: Drag-and-Drop Landing Pages
article_title: Creating Drag-and-Drop Landing Pages
description: "This article covers how to create and customize Braze landing pages with the drag-and-drop editor."
page_order: 31
hidden: true
alias: /landing_pages/drag_and_drop/
---

# Drag-and-drop landing pages

> Using the drag-and-drop editor, you can create and customize a landing page to grow your audience and collect preferences directly in Braze.

{% alert important %}
Landing pages are currently in beta. Contact your Braze account manager if you're interested in participating in this beta.
{% endalert %}

## Creating a landing page (drag-and-drop)

### Step 1: Create a landing page

Go to **Messaging** > **Landing Pages** and select **Create landing page**, or select the name of an existing one to duplicate it or make changes to it.

![The "Landing Pages" homepage.][2]{: style="max-width:90%;"}

### Step 2: Set up your landing page details

#### General details

The landing page name and description are used to search for the page in your internal workspace. These won't be visible to your customers.

#### Site details

Set up metatags to customize how your page appears on the browser tab and optimize for search engine results. These will be visible to your customers.

We suggest following these best practices:

| Detail | Description | Recommendations |
| --- | --- |
| Site title | The title that displays on the browser tab. | Use up to 60 characters. |
| Site description | A text snippet that displays in search results. | Use between 140-160 characters.|
| Favicon | The icon that appears next to the site title on the browser tab. | Use an aspect ratio of 1:1, and a supported file type of PNG, JPEG, or ICO. |
| URL handle | This is the link users will click to navigate to your landing page. | This must be unique. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

{% alert note %}
Custom subdomain support is not available during the beta.
{% endalert %}

### Step 3: Customize your landing page

Select **Launch Editor** to start designing your landing page in the drag-and-drop editor. The editor will preload with a default template that you can customize to fit your use case.

![Landing page template with a form for customer sign-up.][8]{: style="max-width:90%;"}

#### Drag-and-drop blocks

The editor uses two types of components for landing page composition: rows and blocks. All blocks must be placed in a row.

![The "Build" editor section containing "Rows" and "Form Blocks".][4]{: style="max-width:30%;"}

#### Form block

If you include a form block, you must include at least one button with the toggle turned on for **Submit form when button is clicked**. You should also create another landing page for the [confirmation state](#confirmation-state).

![A form block that registers a new customer and will send a discount code to their email.][5]{: style="max-width:70%;"}

#### Page container styles

You can set styles to be applied across all relevent component blocks in your landing page from the **Page container** tab. These styles will be used everywhere on your page except where you override them with a specific block.

We recommend setting up page container-level styles before you customize styles at the block level. You can also add a background image for the entire page.

![The page container with options to customize background images, colors, border details, and content styling.][6]{: style="max-width:30%;"}

### Step 4: Preview your landing page

You can preview your landing page in the editor's **Preview** tab, but testing functionality is disabled for the beta. After saving your landing page as a draft, you can visit the URL by going to **Landing Pages** and selecting **Copy URL** next to your landing page. You can also share the URL with collaborators.

![A landing page with the menu open to show the "Copy URL" option.][7]{: style="max-width:90%;"}

After you're satisfied with the landing page, select **Publish Landing Page**.

{% alert important %}
The URL handle cannot be edited after the landing page is published.
{% endalert %}

## Creating a confirmation landing page {#confirmation-state}

If you include a [form](#form-block) on your landing page, don't forget to create a confirmation landing page. Create another landing page for the confirmation state and then add the link in the **Open web URL** field of the button that submits the form.

## Linking to your landing page

In beta, you can include a link to the landing page in any channel by copying and pasting the link into a Braze message or social media campaign.

## Handling form submission errors

If a user inputs an invalid form value (such as unaccepted special characters), they will see a generic error indicator that isn't customizable and won't be able to submit the form. You can view the error behavior on the preview landing page.

## Merging users created from your landing page

During the beta, each form submission on a landing page will create a new anonymous user profile in Braze. If a user with the same email address already exists, you can merge the new user profile into the existing profile using the [`/users/merge`]({{site.baseurl}}/api/endpoints/user_data/post_users_merge#merging-unidentified-user) endpoint. To learn about the different ways to deduplicate users in Braze, see [Duplicate users]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/duplicate_users).

## Considerations

- The landing page body size can be up to 1 MB.

## Frequently asked questions

### What happens when a user submits their information on the landing page?

When a user submits a form, a new Braze user profile is created with the submitted user data.

{% alert note %}
During the beta, Braze will create a new user with each form submission regardless of where the user clicks on the landing page.
{% endalert %}

### Are there any technical requirements to publish a landing page?

No, there aren't any technical requirements.

### Is there an HTML editor for landing pages?

No, this isn't currently available.

### Is reporting available for landing pages?

No, this isn't currently available.

### Is there an HTML editor for landing pages?

No, this isn’t currently available. You can use the Custom Code block in the editor.

### What features are on the road map for landing pages?

Because landing pages are currently in beta, additional features are in development. These include:
* Custom subdomain support
* New Liquid tag for linking a landing page in a Braze messaging channel
* Basic reporting page
* Drag-and-drop form blocks for checkboxes and dropdowns
* Standard event for tracking and retargeting based on form submissions


[1]: {% image_buster /assets/img/landing_pages/homepage.gif %}
[2]: {% image_buster /assets/img/landing_pages/create.png %}
[3]: {% image_buster /assets/img/landing_pages/details.png %}
[4]: {% image_buster /assets/img/landing_pages/dnd.png %}
[5]: {% image_buster /assets/img/landing_pages/form.png %}
[6]: {% image_buster /assets/img/landing_pages/page_container.png %}
[7]: {% image_buster /assets/img/landing_pages/url_handle.png %}
[8]: {% image_buster /assets/img/landing_pages/template.png %}
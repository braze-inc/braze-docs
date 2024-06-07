---
nav_title: Drag-and-drop Landing Pages
article_title: Creating Drag-and-Drop Landing Pages
description: "This article covers how to create and customize Braze landing pages with the drag-and-drop editor."
page_order: 31
hidden: true
---

# Drag-and-drop landing pages

> Using the drag-and-drop editor, you can create and customize a landing page to grow your audience and collect preferences directly in Braze.

![GIF demonstrating how components can be dragged and dropped into an editor to create a landing page.][1]{: style="max-width:70%;"}

Check out our [Customer Ed Quick Tips]() video to get a jumpstart on creating Braze landing pages.

## Creating a landing page (drag-and-drop)

### Step 1: Create a landing page

Go to **Messaging** > **Landing Pages** and select **Create landing page**, or select the name of an existing one to duplicate it or make changes to it.

![The "Landing Pages" page showing a list of existing landing pages and a button to "Create landing page".][2]{: style="max-width:70%;"}

### Step 2: Set up your landing page details

#### General details

The landing page name and description are used to search for the page in your internal workspace. These won't be visible to your customers.

#### Site details

Set up metatags to customize how your page appears on the browser tab and optimize for search engine results. These will be visible to your customers.

We suggest following these best practices:

| Detail | Best practice |
| --- | --- |
| Site title | Use a maximum of 60 characters. |
| Site description | Stay between 140-160 characters.|
| Favicon | Use an aspect ratio of 1:1, and the supported file types of PNG, JPEG, or ICO. |
| URL handle | This is the link users will click to navigate to your landing page. It must be unique. |
{: .reset-td-br-1 .reset-td-br-2}

{% alert note %}
Custom subdomain support is not available during the beta.
{% endalert %}

![Tab to provide a landing page's site details.][3]{: style="max-width:70%;"}

### Step 3: Customize your landing page

Select **Launch Editor** to start designing your landing page in the drag-and-drop editor. The editor will preload with a default template that you can customize to fit your use case.

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

You can preview your landing page in the editor's **Preview** tab, but testing functionality is disabled for the beta. After you save your landing page as a draft, you can visit the URL under **URL handle** to preview the page on your browser. You can also share the URL with collaborators.

![The "URL handle" section has the full URL to preview the landing page.][7]{: style="max-width:70%;"}

After you're satisfied with the landing page, select **Publish Landing Page**.

{% alert important %}
The URL handle cannot be edited after the landing page is published.
{% endalert %}

## Creating a confirmation landing page {#confirmation-state}

If you include a [form](#form-block) on your landing page, don't forget to create a confirmation landing page. Create another landing page for the confirmation state and then add the link in the **Open web URL** field of the button that submits the form.

## Linking to your landing page

In beta, you can include a link to the landing page in any channel by copying and pasting the link into a Braze message or social media campaign.

## Handling user errors

If an error occurs when a user submits a form on a landing page, they'll be presented with a default error message that can't be customized or styled in the editor.

## Considerations

- The landing page body size can be a maximum of 1 MB.

## Frequently asked questions

### What happens when a user submits their information on the landing page?

When a user submits their information, 

### Are there any technical requirements to publish a landing page?

No, there aren't any technical requirements.

### Is there an HTML editor for landing pages?

No, this isn't currently available.

### Is reporting available for landing pages?

No, this isn't currently available.

[1]: {% image_buster /assets/img/landing_pages/homepage.gif %}
[2]: {% image_buster /assets/img/landing_pages/create.png %}
[3]: {% image_buster /assets/img/landing_pages/details.png %}
[4]: {% image_buster /assets/img/landing_pages/dnd.png %}
[5]: {% image_buster /assets/img/landing_pages/form.png %}
[6]: {% image_buster /assets/img/landing_pages/page_container.png %}
[7]: {% image_buster /assets/img/landing_pages/url_handle.png %}
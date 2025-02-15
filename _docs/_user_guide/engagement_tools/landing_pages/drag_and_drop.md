---
nav_title: Drag-and-Drop Editor
article_title: Creating Drag-and-Drop Landing Pages
description: "This article covers how to create and customize Braze landing pages with the drag-and-drop editor."
page_order: 0
alias: /landing_pages/drag_and_drop/
---

# Drag-and-drop landing pages

> Using the drag-and-drop editor, you can create and customize a landing page to grow your audience and collect preferences directly in Braze.

{% alert important %}
Landing pages are currently in early access. There is a limit of five landing pages per company. End user sessions recorded on landing pages count towards your Monthly Active Users (MAU) calculation.
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
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### Step 3: Customize your landing page

Select **Launch Editor** to start designing your landing page in the drag-and-drop editor. The editor will preload with a default template that you can customize to fit your use case.

![Landing page template with a form for customer sign-up.][8]{: style="max-width:90%;"}

#### Drag-and-drop blocks

The editor uses two types of components for landing page composition: rows and blocks. All blocks must be placed in a row.

![The "Build" editor section containing "Rows" and "Form Blocks".][4]{: style="max-width:30%;"}

#### Form block

Use various form block components to log custom and standard profile attributes and custom events. The input field form block can log both standard and custom attributes for your users, and the phone capture and email capture form blocks can capture phone and email fields for your users' form submissions. Button actions can be logged as custom attributes, custom events, or both on form submission. 

If you include a form block, you must include at least one button with the toggle turned on for **Submit form when button is clicked**. You should also create another landing page for the [confirmation state](#confirmation-state).

![A form block that registers a new customer and will send a discount code to their email.][5]{: style="max-width:70%;"}

#### Page container styles

You can set styles to be applied across all relevent component blocks in your landing page from the **Page container** tab. These styles will be used everywhere on your page except where you override them with a specific block.

We recommend setting up page container-level styles before you customize styles at the block level. You can also add a background image for the entire page.

![The page container with options to customize background images, colors, border details, and content styling.][6]{: style="max-width:30%;"}

### Step 4: Preview your landing page

You can preview your landing page in the editor's **Preview** tab. After saving your landing page as a draft, you can visit the URL by going to **Landing Pages** and selecting **Copy URL** next to your landing page. You can also share the URL with collaborators.

![A landing page with the menu open to show the "Copy URL" option.][7]{: style="max-width:90%;"}

After you're satisfied with the landing page, select **Publish Landing Page**.

{% alert important %}
The URL handle cannot be edited after the landing page is published.
{% endalert %}

## Creating a confirmation landing page {#confirmation-state}

If you include a [form](#form-block) on your landing page, don't forget to create a confirmation landing page. Create another landing page for the confirmation state and then add the link in the **Open web URL** field of the button that submits the form.

## Linking to your landing page

You can include a link to the landing page in any channel by copying and pasting the link into a Braze message or social media campaign.

## Handling form submission errors

If a user inputs an invalid form value (such as unaccepted special characters), they will see a generic error indicator that isn't customizable and won't be able to submit the form. You can view the error behavior on the preview landing page.

## Merging users created from your landing page

Each form submission on a landing page will create a new anonymous user profile in Braze. If a user with the same email address already exists, you can merge the new user profile into the existing profile using the [`/users/merge`]({{site.baseurl}}/api/endpoints/user_data/post_users_merge#merging-unidentified-user) endpoint. To learn about the different ways to deduplicate users in Braze, see [Duplicate users]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/duplicate_users).

User merging will be handled automatically via a liquid tag in the future. 

## Considerations

The landing page body size can be up to 1 MB.

## Permissions

You need either administrator permissions or all of the following permissions to access, create, and publish landing pages:

- Access Landing Pages
- Create Landing Page Drafts
- Publish Landing Pages

## Plan tiers

The number of published landing pages and custom domains you can use depends on your plan type: free or paid (incremental).

| Feature                                                                                                   | Free tier     | Paid tier (incremental)     |
| :---------------------------------------------------------------------------------------------------------------- | :--------------- | ----------------- |
| Published landing pages                                                                 | Five per company | 20 additional |
| Custom domains          | One per company | Five additional |

## Frequently asked questions

### What happens when a user submits their information on the landing page?

When a user submits a form, a new Braze user profile is created with the submitted user data.

### Are there any technical requirements to publish a landing page?

No, there aren't any technical requirements.

### Is there an HTML editor for landing pages?

You can edit the HTML of a landing page using the Custom Code block.

### Is reporting available for landing pages?

No, this isn't currently available.

### Can I create a webhook inside a landing page?

No, this isn't currently supported.

### What features are on the roadmap for landing pages? {#roadmap}

We plan to release additional features for landing pages, which are in development. These may include:

* New Liquid tag for linking a landing page in a Braze messaging channel
* Automatic user merging when a landing page is sent through a Braze channel
* Basic reporting page
* Drag-and-drop form blocks for checkboxes and dropdowns
* Standard event for tracking and retargeting based on form submissions

While these features are part of our roadmap, they are still in development, and Braze cannot guarantee that any or all of these features will be made generally available. Access to some or all of the planned features for landing pages may be subject to additional fees.

[1]: {% image_buster /assets/img/landing_pages/homepage.gif %}
[2]: {% image_buster /assets/img/landing_pages/create.png %}
[3]: {% image_buster /assets/img/landing_pages/details.png %}
[4]: {% image_buster /assets/img/landing_pages/dnd.png %}
[5]: {% image_buster /assets/img/landing_pages/form.png %}
[6]: {% image_buster /assets/img/landing_pages/page_container.png %}
[7]: {% image_buster /assets/img/landing_pages/url_handle.png %}
[8]: {% image_buster /assets/img/landing_pages/template.png %}

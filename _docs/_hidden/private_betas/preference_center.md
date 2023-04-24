---
nav_title: Drag & Drop Email Preference Center
article_title: Drag & Drop Email Preference Center
permalink: "/dnd_preference_center/"
description: "This reference page covers how to create an email preference center with the drag & drop editor."
layout: dev_guide
---

# Create an email preference center with Drag & Drop

With the Drag & Drop Editor, you can now create and customize a preference center to help manage which users receive certain types of communication. 

{% alert note %}
Drag & drop email preference center is currently in early access. Contact your Braze account manager if you're interested in participating in the early access.
{% endalert %}

## Step 1: Create an email preference center

Create a preference center by navigating to the **Subscription Group > Email Preference Center** page in the dashboard. Here, a list of custom preference centers will be displayed. Click **Create New** to create a new preference center, or click the name of an existing one to make changes.

![][1]

## Step 2: Name the email preference center

Preference center names can only contain alphanumeric characters, dashes, or underscores. The name you provide will determine the syntax of the generated Liquid tag. 

This Liquid tag can be included in any outbound email campaigns or Canvas steps and will direct users to the preference center.

![][2]

## Step 3: Add subscription groups to the preference center

Click **Launch Editor** to begin designing your preference center in the Drag & Drop Editor.

### Define available subscription groups
To determine which subscription groups should be shown in the preference center, click the **+ Add subscription groups** button to launch a modal where desired subscription groups can be selected. After selecting, click the **Add Subscription Groups** button to add them to the preference center.

You can further configure the selected subscription groups by clicking on the smart block and adjusting the block Properties.
- Adjust the order that subscription groups appear
- Add or remove additional subscription groups
- Include descriptions
- Add or remove a "Subscribe to all" checkbox
- Add or remove an "Unsubscribe from all" checkbox

![][3]{: style="max-width:38%;"} ![][4]{: style="max-width:45%;"}

## Step 4: Customize the preference center using the Drag & Drop Editor

### Set common styles
You can set certain styles to be applied across all relevant blocks in your preference center from the **Common Styles** tab. The styles set in this section are used everywhere in your message except where you override them for a specific block. For an easier design experience, we recommend setting up page-level styles before you customize styles at the block level.

![][5]{: style="max-width:45%;"}

{% alert tip %}
To return to the common styles, click the "X" button on individual block properties. Next, select the message container, message "X" button, or editor background.
{% endalert %}

## Drag & drop preference center components

The Drag & Drop Editor uses two key components to make preference center composition quick and easy: rows and blocks. All blocks must be placed in a row.

{% tabs %}
{% tab Rows %}

Rows are structural units that define the horizontal composition of a section of the message by using cells.

![]({% image_buster /assets/img/preference_center/preference_center6.png %}){: style="max-width:45%;"}

When a row is selected, you can add or remove the number of columns you need from the Column customization section to put different content elements side by side.

You can also slide to adjust the size of existing columns.

![]({% image_buster /assets/img/preference_center/preference_center7.png %}){: style="max-width:45%;"}

As a best practice, format your row and column properties before formatting any blocks inside the rows. You can adjust the spacing and alignment in many places, so starting from the foundation makes it easier to edit as you go.

{% endtab %}
{% tab Blocks %}

Blocks represent different types of content you can use in your message. Simply drag one inside an existing row segment, which will auto-adjust to the cell width.

![]({% image_buster /assets/img/preference_center/preference_center8.png %}){: style="max-width:45%;"}

Every block has its own settings, such as granular control on padding. The right-side panel automatically switches to a styling panel for the selected content element. For more information, see [Editor block properties]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/editor_blocks/).

{% endtab %}
{% endtabs %}

## Step 5: Customize your confirmation page

Don’t forget to customize the confirmation page! You can edit this page by clicking on **Confirmation Page** at the top of the **Drag & Drop Editor window**. This page will be displayed to users after updating their preferences using the preference center. The same styling capabilities above apply to this page as well.

![][9]{: style="max-width:65%;"}

## Step 6: Preview and launch your preference center

You can preview your preference center by clicking the **Preview** tab within the editor. However, testing functionality is disabled. After editing your preference center, you can close the Drag & Drop Editor by clicking the **Done** button.

You will see a preview of both the preference center and the confirmation page. Click **Save as Draft** to return to this preference center later, or if you are satisfied, click **Launch Preference Center**.

When launching the preference center, you will be prompted to confirm the name, as it cannot be edited after launching. Once confirmed, the preference center will be launched and ready for use.

## Using the preference center

To place a link to the preference center in your emails, copy the Liquid tag of the desired preference center by clicking the **Copy Liquid** icon.

![][10]{: style="max-width:75%;"}

Add the Liquid tag to the desired place in your email, similar to how [unsubscribe URLs]({{site.baseurl}}/user_guide/message_building_by_channel/email/preference_center/preference_center/#custom-footer) are inserted.

## Errors

If an error occurs when a user clicks **Save** on a preference center, they will be presented with the following default error message, which cannot be customized or styled in the editor. However, localization of the error messages is still supported on these pages. 

![An error noting "There was a problem saving your preferences. Please try again."][11]{: style="max-width:55%;"}

[1]: {% image_buster /assets/img/preference_center/preference_center1.png %} 
[2]: {% image_buster /assets/img/preference_center/preference_center2.png %} 
[3]: {% image_buster /assets/img/preference_center/preference_center3.png %} 
[4]: {% image_buster /assets/img/preference_center/preference_center4.png %} 
[5]: {% image_buster /assets/img/preference_center/preference_center5.png %} 
[6]: {% image_buster /assets/img/preference_center/preference_center6.png %} 
[7]: {% image_buster /assets/img/preference_center/preference_center7.png %} 
[8]: {% image_buster /assets/img/preference_center/preference_center8.png %} 
[9]: {% image_buster /assets/img/preference_center/preference_center9.png %} 
[10]: {% image_buster /assets/img/preference_center/preference_center10.png %} 
[11]: {% image_buster /assets/img/preference_center/preference_center11.png %} 

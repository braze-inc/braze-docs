---
nav_title: Drag-and-drop email preference center
article_title: Drag-And-Drop Email Preference Center
alias: "/dnd_preference_center/"
description: "This reference page covers how to create an email preference center with the drag-and-drop editor."
page_order: 2
---

# Create an email preference center with drag-and-drop

> Using the drag-and-drop editor, you can create and customize a preference center to help manage which users receive certain types of communication. You can have up to 50 preference centers per workspace.

{% multi_lang_include drag_and_drop/drag_and_drop_access.md variable_name='dnd editors' %}

## Step 1: Create an email preference center

Create a preference center by navigating to **Audience** > **Subscriptions** > **Email Preference Center**.

Here, a list of custom preference centers will be displayed. Select **Create New** to create a new preference center, or select the name of an existing one to make changes.

![A list of custom preference centers with the name, description, type, status, last edited date, and created by user.]({% image_buster /assets/img/preference_center/preference_center1.png %})

## Step 2: Name the email preference center

Preference center names can only contain alphanumeric characters, dashes, or underscores. The name you provide will determine the syntax of the generated Liquid tag. 

This Liquid tag can be included in any outbound email campaigns or Canvas steps and will direct users to the preference center.

![An example of Liquid for a preference center.]({% image_buster /assets/img/preference_center/preference_center2.png %})

## Step 3: Add subscription groups to the preference center

Select **Launch Editor** to begin designing your preference center in the drag-and-drop editor.

### Define available subscription groups

To determine which subscription groups should be shown in the preference center, select the **+ Add subscription groups** button to launch a modal where desired subscription groups can be selected. After selecting, select the **Add Subscription Groups** button to add them to the preference center.

You can further configure the selected subscription groups by selecting the smart block and adjusting the block properties.
- Adjust the order of subscription groups
- Add or remove additional subscription groups
- Include descriptions
- Add or remove a **Subscribe to all** checkbox which will subscribe the user to all subscription groups shown in this block
- Add or remove an **Unsubscribe from all** checkbox which will unsubscribe the user from all subscription groups shown in this block

![An example of a preference center with the options to subscribe to all messages, marketing, newsletter, and weekly emails, or to unsubscribe from all.]({% image_buster /assets/img/preference_center/preference_center3.png %}){: style="max-width:38%;"} ![]({% image_buster /assets/img/preference_center/preference_center4.png %}){: style="max-width:45%;"}

The **Unsubscribe from all** button at the bottom of the template is non-removable and will [globally unsubscribe]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#subscription-states) the user from receiving any email messages.

## Step 4: Customize the preference center using the drag-and-drop editor

### Set common styles

You can set certain styles to be applied across all relevant blocks in your preference center from the **Common Styles** tab. The styles set in this section are used everywhere in your message except where you override them for a specific block. For an easier design experience, we recommend setting up page-level styles before you customize styles at the block level.

![An example of common style settings for text, buttons, and links.]({% image_buster /assets/img/preference_center/preference_center5.png %}){: style="max-width:45%;"}

{% alert tip %}
To return to the common styles, select the "X" button on individual block properties. Next, select the message container, message "X" button, or editor background.
{% endalert %}

## Drag-and-drop preference center components

The drag-and-drop editor uses two key components to make preference center composition quick and easy: rows and blocks. All blocks must be placed in a row.

{% tabs %}
{% tab Rows %}

Rows are structural units that define the horizontal composition of a section of the message by using cells.

![Option to select the type of row in your message.]({% image_buster /assets/img/preference_center/preference_center6.png %}){: style="max-width:45%;"}

When a row is selected, you can add or remove the number of columns you need from the Column customization section to put different content elements side by side. You can also slide to adjust the size of existing columns.

![Options to customize your column properties, including background color, border style, border radius, and padding.]({% image_buster /assets/img/preference_center/preference_center7.png %}){: style="max-width:45%;"}

As a best practice, format your row and column properties before formatting any blocks inside the rows. You can adjust the spacing and alignment in many places, so starting from the foundation makes it easier to edit as you go.

{% endtab %}
{% tab Blocks %}

Blocks represent different types of content you can use in your message. Drag one inside an existing row segment, which will auto-adjust to the cell width.

![Option to select blocks, including title, paragraph, button, image, and spacer.]({% image_buster /assets/img/preference_center/preference_center8.png %}){: style="max-width:45%;"}

Every block has its own settings, such as granular control on padding. The right-side panel automatically switches to a styling panel for the selected content element. For more information, see [Editor block properties]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/editor_blocks/).

If you're using the Custom Code block in your preference center, inline frames may not generate in the custom code when delivered to your users.

{% endtab %}
{% endtabs %}

## Step 5: Customize your confirmation page

Don’t forget to customize the confirmation page! You can edit this page by selecting **Confirmation Page** at the top of the drag-and-drop editor window. This page will be displayed to users after updating their preferences using the preference center. The same styling capabilities above apply to this page as well.

![An example of a confirmation page to communicate the user's preferences have been updated.]({% image_buster /assets/img/preference_center/preference_center9.png %}){: style="max-width:65%;"}

## Step 6: Preview and launch your preference center

You can preview your preference center by selecting the **Preview** tab within the editor. However, testing functionality is disabled. After editing your preference center, you can close the editor by selecting the **Done** button.

You will see a preview of both the preference center and the confirmation page. Select **Save as Draft** to return to this preference center later, or if you are satisfied, select **Launch Preference Center**.

When launching the preference center, you will be prompted to confirm the name, as it cannot be edited after launching. After you confirm the name, the preference center will be launched and ready for use.

## Using the preference center

{% multi_lang_include alerts/important_alerts.md alert='Preference Center warning' %}

To place a link to the preference center in your emails, copy the Liquid tag of the desired preference center by selecting the **Copy Liquid** icon.

![The Copy Liquid option in the row of a preference center.]({% image_buster /assets/img/preference_center/preference_center10.png %}){: style="max-width:75%;"}

Add the Liquid tag to the desired place in your email, similar to how [unsubscribe URLs]({{site.baseurl}}/user_guide/message_building_by_channel/email/custom_email_footer/#adding-a-custom-unsubscribe-link) are inserted.

## Handling errors

If an error occurs when a user selects **Save** on a preference center, they will be presented with the following default error message, which cannot be customized or styled in the editor. However, localization of the error messages is still supported on these pages. 

![An error noting "There was a problem saving your preferences. Please try again."]({% image_buster /assets/img/preference_center/preference_center11.png %}){: style="max-width:55%;"}


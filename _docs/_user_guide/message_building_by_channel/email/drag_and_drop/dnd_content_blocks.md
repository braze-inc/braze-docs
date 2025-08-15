---
nav_title: Content blocks
article_title: Drag-and-Drop Editor Content Blocks
alias: "/dnd/content_blocks/"
channel: email
page_order: 2
description: "This reference article covers how to create and use Content Blocks in the drag-and-drop editor."
tool: Media

---

# Drag-and-drop editor Content Blocks

> The Content Blocks used exclusively in the drag-and-drop editor are similar in functionality to the [Content Blocks]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/content_blocks/) used across different channels. They're a centralized location for holding information that can be referenced in various email campaigns. This can include grouping together email headers, promotional callouts, and more all in one reusable row.

{% alert note %}
Drag-and-drop Content Blocks are only available for use in email campaigns and email messages in Canvas. 
{% endalert %}

## Creating a Content Block

To create a Content Block, do the following:

{% multi_lang_include create_content_block.md location="dnd" %}

{% alert important %}
Each drag-and-drop Content Block is limited to one row. However, you can use drag-and-drop editor blocks to build and customize the Content Block to suit your email messaging.
{% endalert %}

## Using a Content Block

There are two ways to add the Content Block to your email: using the editor or using Liquid.

### Using the editor to add a Content Block

To add a Content Block in the editor, do the following:

1. Go to the the **Rows** tab in the editor and select **Content Blocks**. 
2. Drag and drop your Content Block into the email editor. 
3. (Optional) Adjust the width of your Content Block by selecting the button in the navigation menu. The default width is 100%. <br><br>![A double-sided arrow with an option to edit the width.]({% image_buster /assets/img_archive/content_block_width.png %}){: style="max-width:30%;" }<br><br>

After adding the Content Block to the email editor, you can make edits to the Content Block that won't affect the original Content Block you created in **Templates & Media**. This is because Content Blocks added by drag and drop aren't linked to the original Content Block. To view any changes made to the original Content Block, drag it into the email editor again. 

Misalignment in the drag-and-drop editor can occur when multiple Content Blocks are added to a single row block. Try using separate row blocks to maintain alignment across your content at the row level.

### Using Liquid to add a Content Block

To add a Content Block by using Liquid, do the following:

1. Go to your email campaign and select **Edit Email Body**. 
2. Click <i class="fas fa-plus"></i> **Personalization**.
3. Locate the **Add Personalization** tab and select **Content Blocks** in the **Personalization Type** dropdown.
4. Select the name of your Content Block in the **Attribute** field. The Liquid snippet field will populate with your Content Block Liquid Tag. 
5. Copy and paste the Liquid snippet into a text editor block. <br>![The Add Personalization tab with options.]({% image_buster /assets/img_archive/dnd_content_block_personalization.png %}){: style="max-width:30%;"}

When you preview your email messaging, the Liquid snippet will display as the drag-and-drop editor Content Block. 

{% alert important %}
When a Content Block is added into the email editor with Liquid, this Content Block is linked to the original Content Block created in **Templates & Media**. This means the Content Block will be updated to reflect any changes to the original Content Block template.
{% endalert %}

## Updating Content Blocks

To update an existing Content Block, you can either edit the original Content Block from the **Content Blocks** page, or copy the HTML from the original message to your new one. Updates to a Content Block template will update in all email messages where the Content Block is added via Liquid.

To archive a Content Block, go to **Templates** > **Content Blocks**, select the <i class="fas fa-ellipsis-vertical"></i> vertical ellipsis icon for the Content Block, and click **Archive**. When you archive a Content Block, your messages will still include the content in the archived block. However, archived Content Blocks are read-only, so unarchive the Content Block before editing. 


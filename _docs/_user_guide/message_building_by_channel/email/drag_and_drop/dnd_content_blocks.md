---
nav_title: Content Blocks
article_title: Drag-and-Drop Editor Content Blocks
alias: "/dnd/content_blocks/"
channel: email
page_order: 2
description: "This reference article covers how to create and use Content Blocks in the drag-and-drop editor."
tool: Media

---

# Content Blocks

> The Content Blocks used exclusively in the drag-and-drop editor are similar in functionality to the [Content Blocks]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/content_blocks/) used across different channels. They're a centralized location for holding information that can be referenced in various email campaigns. This can include grouping together email headers, promotional callouts, and more all in one reusable row.

## Creating a Content Block

To create a Content Block, do the following:

1. Go to **Templates** > **Content Blocks** and click <i class="fas fa-plus"></i> **Create Content Block**.

{% alert note %}
If you are using the [older navigation]({{site.baseurl}}/navigation), this page is located at **Engagement** > **Templates & Media** > **Content Block Library**.
{% endalert %}

{:start="2"}
2. Enter a **Content Block Name** and an optional description.

![][1]

{% alert note %}
Drag-and-drop Content Blocks are only available for use in email campaigns and email messages in Canvas. 
{% endalert %}

{:start="3"}
3. Select **Drag-And-Drop Editor** as the Content Block type.
4. Click **Edit Content Block** in the **Content Block Preview** panel to begin editing your Content Block.
5. Drag and drop the [editor blocks]({{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/dnd_editor_blocks/) to build a drag-and-drop Content Block. 
6. Drag and drop a format block from the **Rows** tab into the editor to create the layout of your Content Block. 
7. Add drag-and-drop Content Blocks as needed to build out your email campaigns.

{% alert important %}
Each drag-and-drop Content Block is limited to one row. However, you can use drag-and-drop editor blocks to build and customize the Content Block to suit your email messaging.
{% endalert %}

## Using a Content Block

There are two ways to add the Content Block to your email: using the editor or using Liquid.

### Using the editor to add a Content Block

To add a Content Block in the editor, do the following:

1. Go to the the **Rows** tab in the editor and select **Content Blocks**. 
2. Drag and drop your Content Block into the email editor. 

After the Content Block is added to the email editor via drag and drop, you can make edits to the Content Block that won't affect the original Content Block you created in **Templates & Media**. This is because Content Blocks added via drag and drop aren't linked to the original Content Block. To view any changes made to the original Content Block, drag it into the email editor again. 

Misalignment in the drag-and-drop editor can occur when multiple Content Blocks are added to a single row block. Try using separate row blocks to maintain alignment across your content at the row level.

### Using Liquid to add a Content Block

![][2]{: style="float:right;max-width:50%;margin-left:15px;margin-top:15px;"}

To add a Content Block by using Liquid, do the following:

1. Go to your email campaign and select **Edit Email Body**. 
2. Click <i class="fas fa-plus"></i> **Personalization**.
3. Locate the **Add Personalization** tab and select **Content Blocks** in the **Personalization Type** dropdown.
4. Select the name of your Content Block in the **Attribute** field. The Liquid snippet field will populate with your Content Block Liquid Tag. 
5. Copy and paste the Liquid snippet into a text editor block. 

When you preview your email messaging, the Liquid snippet will display as the drag-and-drop editor Content Block. 

{% alert important %}
When a Content Block is added into the email editor via Liquid, this Content Block is linked to the original Content Block created in **Templates & Media**. This means the Content Block will be updated to reflect any changes to the original Content Block template.
{% endalert %}

## Updating Content Blocks

To update an existing Content Block, you can either edit the original Content Block from the **Content Blocks** page, or copy the HTML from the original message to your new one. For updates to a Content Block template, it will update in all email messages where the Content Block is added via Liquid.

To archive a Content Block, go to **Templates** > **Content Blocks**, select the <i class="fas fa-cog"></i> gear icon next to the selected Content Block, and click **Archive**. When you archive a Content Block, your messages will still include the content in the archived block.

[1]: {% image_buster /assets/img_archive/dnd_content_block_name.png %}
[2]: {% image_buster /assets/img_archive/dnd_content_block_personalization.png %}

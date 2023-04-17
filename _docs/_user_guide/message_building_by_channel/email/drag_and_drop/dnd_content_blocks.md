---
nav_title: Content Blocks
article_title: Drag & Drop Editor Content Blocks
alias: "/dnd/content_blocks/"
channel: email
page_order: 2
description: "This reference article covers how to create and use Content Blocks in the Drag & Drop Editor."
tool: Media

---

# Content Blocks

> The Content Blocks used exclusively in the Drag & Drop Editor are similar in functionality to the [Content Blocks]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/content_blocks/) used across different channels. They're a centralized location for holding information that can be referenced in various email campaigns. This can include grouping together email headers, promotional callouts, and more all in one reusable row.

## Creating a Content Block

To create a Content Block, go to **Templates & Media** under the **Engagement** section of your Braze dashboard. Select the **Content Blocks Library** tab and click <i class="fas fa-plus"></i> **Create Content Block**.

Enter a **Content Block Name** and an optional description. 

![][1]

{% alert note %}
Drag & Drop Editor Content Blocks are only available for use in email campaigns and email messages in Canvas. 
{% endalert %}

Next, select **Drag & Drop Editor** as the Content Block type. Click **Edit Content Block** in the **Content Block Preview** panel to begin editing your Content Block. 

Here, we'll make use of the [Drag & Drop editor blocks]({{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/dnd_editor_blocks/) to build a Drag & Drop Editor Content Block. First, drag and drop a format block from the **Rows** tab the editor. This will determine the layout of your Content Block. 

{% alert important %}
Each Drag & Drop Editor Content Block is limited to one row. However, you can use Drag & Drop editor blocks to build and customize the Content Block to suit your email messaging.
{% endalert %}

You can also add as many Drag & Drop Editor Content Blocks as needed to build out your email campaigns.

## Using a Content Block

There are two ways to add the Content Block to your email. 

### Rows

First, go to the the **Rows** tab the editor and select **Content Blocks**. Locate your Content Block, and drag and drop the Content Block into the email editor.

Once the Content Block is added into the email editor, you can make edits to the Content Block that will not affect the original Content Block you previously created in **Templates & Media**.

Misalignment in the Drag & Drop Editor can occur when multiple Content Blocks are added to a single row block. Try using separate row blocks to ensure alignment across your content at the row level.

### Liquid

![][2]{: style="float:right;max-width:50%;margin-left:15px;margin-top:15px;"}

Navigate to your email campaign and select **Edit Email Body**. Click the <i class="fas fa-plus"></i> **Personalization** button. 

In the **Add Personalization** tab, select **Content Blocks** in the **Personalization Type** dropdown. For the **Attribute** field, select the name of your Content Block. The Liquid snippet field will populate with your Content Block Liquid Tag. Next, copy and paste the Liquid snippet into a text editor block. 

When you preview your email messaging, the Liquid snippet will display as the Drag & Drop Editor Content Block. 

{% alert important %}
When a Content Block is added into the email editor via Liquid, this Content Block is linked to the original Content Block created in **Templates & Media**. This means the Content Block will be updated to reflect any changes to the original Content Block template.
{% endalert %}

## Updating Content Blocks

To update an existing Content Block, you can either edit the original Content Block located in **Templates & Media**, or copy the HTML from the original message to your new one. If you update a Content Block template, it will update in all email messages where the Content Block is added via Liquid.

To archive a Content Block, go to the **Templates & Media** page and select the <i class="fas fa-cog"></i> gear icon next to the selected Content Block and click **Archive**. When you archive a Content Block, your messages will still include the content in the archived block. 


[1]: {% image_buster /assets/img_archive/dnd_content_block_name.png %}
[2]: {% image_buster /assets/img_archive/dnd_content_block_personalization.png %}

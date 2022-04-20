---
nav_title: Content Blocks
article_title: Drag & Drop Editor Content Blocks
alias: "/dnd/content_blocks/"
channel: email
page_order: 2
description: "This reference article covers how to create and use Content Blocks in the Drag & Drop Editor."
tool: Media

---

# Drag & Drop Editor Content Blocks

The Content Blocks that are created for use exclusively in the Drag & Drop Editor are similar in funtionality to the [Content Blocks]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/content_blocks/) used across different channels. They're a centralized location for holding information that can be referenced in various email campaigns. This can include grouping together email headers, promotional callouts, and more all in one reusable row.

{% alert important %}
Drag & Drop Editor Content Blocks are currently in early access. Contact your Braze account manager if you're interested in participating in the early access.
{% endalert %}

## Creating a Content Block

To create a Content Block, go to **Templates & Media** under the **Engagement** section of your Braze dashboard. Select the **Content Blocks Library** tab and click <i class="fas fa-plus"></i> **Create Content Block**.

Enter a **Content Block Name** and an optional description. 

![][1]

{% alert note %}
Drag & Drop Editor Content Blocks are only available for use in email campaigns. 
{% endalert %}

Next, select **Drag & Drop Editor** as the Content Block type. Click **Edit Content Block** in the **Content Block Preview** panel to begin editing your Content Block. 

Here, we'll make use of the [Drag & Drop editor blocks]({{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/dnd_editor_blocks/) to build a Drag & Drop Editor Content Block. First, drag and drop a format block from the **Rows** tab the editor. This will determine the layout of your Content Block. Each Drag & Drop Editor Content Block is limited to one row. However, you can use Drag & Drop editor blocks to build and customize the Content Block to suite your email messaging.

You can also add as many Drag & Drop Editor Content Blocks as needed to build out your email campaigns.

## Using a Content Block

To use the Content Block, navigate to your email campaign and select **Edit Email Body**. Click the <i class="fas fa-plus"></i> **Personalization** button. 

In the **Add Personalization** tab, select **Content Blocks** in the **Personalization Type** dropdown. For the **Attribute** field, select the name of your Content Block. The Liquid snippet field will populate with your Content Block Liquid Tag. Next, copy and paste the Liquid snippet into a text editor block. 

When you preview your email messaging, the Liquid snippet will display as the Drag & Drop Editor Content Block. 

## Updating Content Blocks

To update an existing Content Block, you can either edit the original Content Block located in Templates & Media, or copy the HTML from the original message to your new one. Note that if you choose to update a Content Block, it will update in all email messages where the Content Block is used.

To archive a Content Block, go to the **Templates & Media** page and select the <i class="fas fa-cog"></i> gear icon next to the selected Content Block and click **Archive**. When you archive a Content Block, your messages will still include the content in the archived block. 


[1]: {% image_buster /assets/img_archive/dnd_content_block_name.png %}
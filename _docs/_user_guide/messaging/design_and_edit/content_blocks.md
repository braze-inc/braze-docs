---
nav_title: Content Blocks
article_title: Content Blocks
alias: "/dnd/content_blocks/"
page_order: 4
description: "Learn how to create, use, and manage reusable Content Blocks across your Braze campaigns and Canvases."
page_type: reference
tool:
  - Templates
  - Media

---

# Content Blocks

> Content Blocks allow you to manage reusable, cross-channel content in a single, centralized location. Use them to create a consistent look and feel across your campaigns, distribute the same offer codes through different channels, or build pre-defined assets for consistent messaging at scale. You can also create and manage your Content Blocks [using the API]({{site.baseurl}}/api/endpoints/templates/).

## Create a Content Block

There are two types of Content Blocks: drag-and-drop and HTML. Each type corresponds to its editor.

{% tabs %}
{% tab Drag-and-drop %}

{% multi_lang_include create_content_block.md location="dnd" %}

{% alert important %}
Each drag-and-drop Content Block is limited to one row. However, you can use drag-and-drop editor blocks to build and customize the Content Block to suit your email messaging.
{% endalert %}

{% endtab %}
{% tab HTML %}

{% multi_lang_include create_content_block.md location="html" %}

{% endtab %}
{% endtabs %}

### Content Block specifications

| Content Block attribute | Specifications |
|---|---|
| Name | Required field with a maximum of 100 characters. It cannot be renamed after the Content Block has been saved. Additionally, you cannot name a new Content Block the same name as a previous Content Block, even if the previous one has been archived. |
| Description | (optional) Maximum of 250 characters. Describe the Content Block so that other Braze users know what it's for and where it's used. |
| Content Size | Maximum of 50 KB. |
| Placement | Content Blocks cannot be used within an email footer, but you can [create a Content Block that includes a footer](#email-footers) for use in your emails. |
| Creation | HTML editor or drag-and-drop editor. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert tip %}
When creating Content Blocks, it can be beneficial to visualize HTML and Liquid by adding line breaks. If these line breaks are left in during sending, you risk having extraneous spaces that can affect how the block will render. To avoid this, use the **Capture** tag on your block along with the **&#124; strip** filter. 
{% raw %}
```
{% capture your_variable %}
{{content_blocks.${your_content_block}}}
{% endcapture %}{{your_variable | strip}}
```
{% endraw %}
{% endalert %}

## Use Content Blocks

After creating your Content Block, you can insert it in your messages using the editor or Liquid.

### Using the drag-and-drop editor {#using-the-editor}

To add a Content Block in the drag-and-drop editor:

1. Go to the **Rows** tab in the editor and select **Content Blocks**. 
2. Drag and drop your Content Block into the email editor. 
3. (Optional) Adjust the width of your Content Block by selecting the button in the navigation menu. The default width is 100% when not specified in your email global style settings; otherwise, the global settings will be honored. <br><br>![A double-sided arrow with an option to edit the width.]({% image_buster /assets/img_archive/content_block_width_updated.png %}){: style="max-width:30%;" }<br><br>

{% alert note %}
Content Blocks added by drag and drop are **not linked** to the original Content Block. To view changes made to the original, drag it into the email editor again.
{% endalert %}

Misalignment in the drag-and-drop editor can occur when multiple Content Blocks are added to a single row block. Try using separate row blocks to maintain alignment across your content at the row level.

### Using Liquid

To insert a Content Block using Liquid:

1. Copy the **Content Block Liquid Tag** from the **Content Block Details** section.
2. Insert the Content Block Liquid tag into the message. You can also begin typing the Liquid and have the tag auto-populate.

In the drag-and-drop editor, you can also add a Content Block via the **Personalization** panel:

1. Go to your email campaign and select **Edit Email Body**. 
2. Click <i class="fas fa-plus"></i> **Personalization**.
3. Select **Content Blocks** in the **Personalization Type** dropdown.
4. Select the name of your Content Block in the **Attribute** field.
5. Copy and paste the Liquid snippet into a text editor block. <br>![The Add Personalization tab with options.]({% image_buster /assets/img_archive/dnd_content_block_personalization.png %}){: style="max-width:30%;"}

{% alert important %}
Content Blocks inserted via Liquid **are linked** to the original Content Block and will reflect any changes to the template.
{% endalert %}

### Things to know

- Using HTML Content Blocks in drag-and-drop emails **or** drag-and-drop Content Blocks in HTML emails may result in unexpected rendering issues. This is because the drag-and-drop editor generates HTML and CSS that dynamically renders the content, whereas the HTML editor is more static.
- Canvas event properties are only supported in a Canvas. If you reference a Content Block with Canvas entry properties in a campaign, it won't populate.

## Preview Content Blocks

After adding a Content Block in an active campaign or Canvas, you can preview it from the Content Blocks Library by hovering over the Content Block and selecting the <i class="fa fa-eye preview-icon"></i> **Preview** icon. 

This preview includes information about the Content Block such as who created it, tags, creation date, last edited date, description, editor type, inclusion count with details (a clickable list of messages or Content Blocks that use the Content Block), and an actual preview of the Content Block.

![A preview of a Content Block "Workout_Promo" for cycling and dancing that has one inclusion.]({% image_buster /assets/img/preview_tab_content_block.png %}){: style="max-width:60%;"} 

## Nest Content Blocks

Content Blocks can be nested, but only once. You can nest Content Block A into Content Block B, but you will not be able to then nest Content Block B into Content Block C.

{% alert warning %}
Nothing will prevent you from nesting a third level of Content Block, but you will not see the content expand in nests beyond the second. The content and the Liquid snippet are removed from the message.
{% endalert %}

## Update and copy Content Blocks

If you choose to update a Content Block, it will update in all messages where the Content Block is inserted via Liquid. If the Content Block is imported using the **Content Blocks** dropdown under **Rows** in the drag-and-drop editor, it won't be updated in all messages.

If you want to update a Content Block for a single message or make a copy to use in other messages, you can either copy the HTML from the original message to your new one, or edit the original Content Block (it must have been used in a message already) and save it. You will get a prompt that allows you to save it as a new Content Block.

After making edits to a Content Block, you can save and launch the updated Content Block by selecting **Launch Content Block**. Or, you can select **More** > **Duplicate** to create a duplicate of your Content Block.

![A Content Block that reads "Welcome to our newsletter".]({% image_buster /assets/img/copy-content-block.png %})

## Use email footers in Content Blocks {#email-footers}

Content Blocks cannot be used within an email footer, but you can create a Content Block that includes footer content for use in your emails. To do so:

1. Go to **Settings** > **Email Preferences** > **Custom Footer** and create the footer.
2. Add the footer to a Content Block in the **Content Blocks Library**.
3. Add that Content Block to your email templates or messages.

## Archive Content Blocks

![Expanded Settings dropdown menu that shows three options: Archive, Duplicate, and Copy to workspace.]({% image_buster /assets/img/template_archive_cog.png %}){: style="max-width:20%;float:right;margin-left:15px;" }

Once you have finished using a Content Block, you can archive it from the **Templates** page. Archived Content Blocks are read-only, so unarchive the Content Block before editing. Content Blocks cannot be archived if they're used in any messages.

### Best practices

- When your block is only used in a few emails, we recommend archiving the outdated block and updating your live messages with a newer block that has not been archived.
- When your block only has a typo or needs a minor change, we do not recommend archiving the block. Instead, update the block and get sending!
- When your block is used in more messages than you can reasonably manage with the first suggestion in this list, we recommend removing all content from the block. This prevents the inclusion of outdated information in any messages.
- If you accidentally archive a Content Block, you can unarchive it.

![Saved Content Blocks panel where the settings dropdown menu for "Test_32" is expanded to show three options: Unarchive, Duplicate, and Copy to workspace]({% image_buster /assets/img/unarchive-content-block.png %})

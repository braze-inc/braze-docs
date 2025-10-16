---
nav_title: Content Blocks Library
article_title: Content Blocks Library
page_order: 1
page_type: reference
description: "This reference article explains how to use the Content Blocks Library to manage your reusable, cross-channel content in a single, centralized location."
tool: 
  - Templates
  - Media

---

# Content Blocks Library

> The Content Blocks Library allows you to manage your reusable, cross-channel content in a single, centralized location.

With Content Blocks, you can:

- Create a consistent look and feel for your email campaigns by using them as headers and footers.
- Distribute the same offer codes through different channels.
- Create pre-defined assets that can be used to build messages with consistent information and assets.
- Copy entire message bodies to other messages.

## Create a Content Block

There are two types of editors used to create a Content Block—classic and drag-and-drop. These two types of editors correspond to the type of Content Block: HTML and drag-and-drop. You can also create and manage your Content Blocks [using the API]({{site.baseurl}}/api/endpoints/templates/).

{% tabs %}
{% tab Drag-and-drop %}

{% multi_lang_include create_content_block.md location="dnd" %}

{% endtab %}
{% tab HTML %}

{% multi_lang_include create_content_block.md location="html" %}

{% endtab %}
{% endtabs %}

### Content Block specifications

| Content Block Attribute | Specifications |
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

## Using Content Blocks

After creating your Content Block, you can insert it in your messages by following these steps: 

1. Copy the **Content Block Liquid Tag** from the **Content Block Details** section.
2. Insert the Content Block Liquid tag into the message. You can also begin typing the Liquid and have the tag auto-populate.

### Things to know

- Using HTML Content Blocks in drag-and-drop emails **or** drag-and-drop Content Blocks in HTML emails may result in unexpected rendering issues. This is because the drag-and-drop editor is generates HTML and CSS that dynamically renders the content whereas the HTML editor is more static.
- Canvas event properties are only supported in a Canvas. If you reference a Content Block with Canvas entry properties in a campaign, it won’t populate.

### Updating and copying Content Blocks

If you choose to update a Content Block, it will update in all messages the Content Block is used if it is inserted via Liquid. If the Content Block is imported using **Content Blocks** dropdown under **Rows** in the drag-and-drop editor, it won't be updated in all messages.

If you want to update a Content Block for a single message or make a copy to use in other messages, you can either copy the HTML from the original message to your new one or edit the original Content Block (it must have been used in a message already) and save it. You will get a prompt that allows you to save it as a new Content Block.

After making edits to a Content Block, you can save and launch the updated Content Block by selecting **Launch Content Block**. Or, you can select **More** > **Duplicate** to create a duplicate of your Content Block.

![A Content Block that reads "Welcome to our newsletter".]({% image_buster /assets/img/copy-content-block.png %})

You can also [duplicate]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/managing_templates/) a Content Block. This creates a draft copy of the Content Block.

### Previewing Content Blocks

After adding a Content Block in an active campaign or Canvas, you can preview this Content Block from the Content Blocks Library by hovering over the Content Block and selecting the <i class="fa fa-eye preview-icon"></i> **Preview** icon. 

This preview includes information about the Content Block such as who created it, tags, creation date, last edited date, description, editor type, inclusion count with details, and an actual preview of the Content Block.

![A preview of a Content Block "Workout_Promo" for cycling and dancing that has six inclusions.]({% image_buster /assets/img/preview_tab_content_block.png %}){: style="max-width:60%;"} 

### Nesting Content Blocks

Content Blocks can be nested, but only once. You can nest Content Block A into Content Block B, but you will not be able to then nest Content Block B into Content Block C.

{% alert warning %}
Nothing will prevent you from nesting a third level of Content Block, but you will not see the content expand in nests beyond the second. The content and the Liquid snippet are removed from the message.
{% endalert %}

### Using email footers in Content Blocks {#email-footers}

Content Blocks cannot be used within an email footer, but you can create a Content Block that includes footer content for use in your emails. To do so, follow these steps:

1. Go to **Settings** > **Email Preferences** > **Custom Footer** and create the footer.
2. Add the footer to a Content Block in the **Content Blocks Library**.
3. Add that Content Block to your email templates or messages.

Now you can use the same footer across multiple messages!

### Archiving Content Blocks

![Expanded Settings dropdown menu that shows three options: Archive, Duplicate, and Copy to workspace.]({% image_buster /assets/img/template_archive_cog.png %}){: style="max-width:20%;float:right;margin-left:15px;" }

Once you have finished using a Content Block, you can archive it from the [Templates & Media]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/managing_templates/) page. Archived Content Blocks are read-only, so unarchive the Content Block before editing. Content Blocks cannot be archived if they're used in any messages.

#### Best practices

- When your block is only used in a few emails, we recommend archiving the outdated block and updating your live messages with a newer block that has not been archived.
- When your block only has a typo or needs a minor change, we do not recommend archiving the block. Instead, update the block and get sending!
- When your block is used in more messages than you can reasonably manage with the first suggestion in this list, we recommend removing all content from the block and archiving it. This will ensure no outdated information is included in any newly sent emails.
- If you accidentally archive a Content Block, you can unarchive it.

![Saved Content Blocks panel where the settings dropdown menu for "Test_32" is expanded to show three options: Unarchive, Duplicate, and Copy to workspace]({% image_buster /assets/img/unarchive-content-block.png %})


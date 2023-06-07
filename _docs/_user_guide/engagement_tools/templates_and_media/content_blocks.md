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

- Create a consistent look and feel to your email campaigns by using them as headers and footers.
- Distribute the same offer codes through different channels.
- Create pre-defined assets that can be used to build messages with consistent information and assets.
- Copy entire message bodies to other messages.

## Create a Content Block

Go to **Templates** > **Content Blocks**.

{% alert note %}
If you are using the [older navigation]({{site.baseurl}}/navigation), **Templates** is **Templates & Media**.
{% endalert %}

There are two types of editors used to create a Content Block—classic and drag-and-drop. These two types of editors correspond to the type of Content Block: HTML and drag-and-drop. You can also create and manage your Content Blocks [via API][5].

{% tabs %}
{% tab Drag-and-drop %}

{% alert note %}
The drag-and-drop editor is only available for Content Blocks used in email messaging.
{% endalert %}

**Steps:**

1. Enter a name for your Content Block. This name will autopopulate as part of the **Content Block Liquid Tag**.
2. (optional) Add a description.
3. Select **Drag-And-Drop Editor** as your editing experience, making this a drag-and-drop Content Block type.
4. Click **Edit Content Block** to begin editing.
4. In the editor, drag and drop the blocks in the **Content** tab to build out your Content Block. 
5. Using the **Row** tab, you can adjust details such as the row or content area background colors, alignment, padding, and more.
6. Once you've finished creating your Content Block, click **Done**.

{% endtab %}
{% tab HTML %}

**Steps:**

1. Enter a name for your Content Block. This name will autopopulate as part of the **Content Block Liquid Tag**.
2. (optional) Add a description.
3. Select **HTML Editor** as your editing experience, making this an HTML Content Block type.
4. Click **Edit Content Block** to begin editing.
4. In the editor, enter your HTML. 
5. Using the **Row** tab, you can adjust details such as the row or content area background colors, alignment, padding, and more.
6. Once you've finished creating your Content Block, click **Done**.

{% endtab %}
{% endtabs %}

### Content Block specifications

| Content Block Attribute | Specifications |
|---|---|
| Name | Required field with a maximum of 100 characters. It cannot be renamed after Content Block has been saved. Additionally, you cannot name a new Content Block the same name as a previous Content Block, even if the previous one has been archived. |
| Description | (optional) Maximum of 250 characters. Provide a description of the Content Block so that other Braze users will know what it's for and where it's used. |
| Content Size | Maximum of 50kB (kilobyte). |
| Placement | Content Blocks cannot be used within an email footer. |
| Creation | HTML editor or drag-and-drop editor. |
{: .reset-td-br-1 .reset-td-br-2}

{% alert tip %}
When creating Content Blocks, it sometimes helps to visualize HTML and Liquid by adding line breaks. If these line breaks are left in during sending, you risk having extraneous spaces that can affect how the block will render. To avoid this, utilize the **Capture** tag on your block along with the **&#124; strip** filter. 
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

### Updating and copying Content Blocks

If you choose to update a Content Block, it will update in all messages the Content Block is used. 

If you want to update a Content Block for a single message or make a copy to use in other messages, you can copy the HTML from the original message to your new one, or edit the original Content Block (it must have been used in a message already) and save it. You will then get a prompt that allows you to save it as a new Content Block.

![Save Content Block dialog that reads "Select 'Save and Update' to update this content block. This will apply changes to messages currently using this content block. Select 'Save as Copy' to save your changes as a copy of this content block. Updates will not apply to messages currently using this content block" with three buttons: Cancel, Save as Copy, and Save and Update.][2]{: height="70%" width="70%"}

You can also [duplicate]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/duplicate/) a Content Block with our Templates & Media feature. When you do this, a "draft" copy is created.

### Nesting Content Blocks

Content Blocks can be nested, but only once! You can nest Content Block A into Content Block B, but you will not be able to then nest Content Block B into Content Block C.

{% alert warning %}
Nothing will prevent you from nesting a third level of Content Block, but you will not see the content expand in nests beyond the second. The content and the Liquid snippet are removed from the message.
{% endalert %}

Additionally, Content Blocks cannot be used within an email footer, though email footers can be used within Content Blocks.

### Archiving Content Blocks

![Expanded Settings dropdown menu that shows three options: Edit, Archive, and Duplicate, where the Archive option is highlighted.][3]{: style="max-width:20%;float:right;margin-left:15px;" }

Once you have finished using a Content Block, you can archive it from the [Templates & Media]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/archive/) page.

Messages using the archived Content Block will still perform as though it was there. However, we recommend several best practices to ensure that outdated information is not accidentally included in your emails.

1. When your Block is only used in a few emails, we recommend archiving the outdated Block and updating your live messages with a newer Block that has not been archived.
2. When your Block only has a typo or needs a minor change, we do not recommend archiving the Block. Just update and get sending!
3. When your Block is used in more messages than you can reasonably manage with the first suggestion in this list, we recommend removing **all** content from the Block, then archiving it. This will ensure no outdated information makes its way into any newly sent emails.

{% alert tip %}
You can save a Content Block without content in it.
{% endalert %}

If you accidentally archive a Content Block, you can unarchive it.  

![Saved Content Blocks panel where the settings dropdown menu for "Content_Block_1" is expanded to show two options: Unarchive and Duplicate.][4]

[2]: {% image_buster /assets/img/copy-content-block.png %}
[3]: {% image_buster /assets/img/template_archive_cog.png %}
[4]: {% image_buster /assets/img/unarchive-content-block.png %}
[5]: {{site.baseurl}}/api/endpoints/templates/
[6]: {{site.baseurl}}/user_guide/engagement_tools/templates_and_media/

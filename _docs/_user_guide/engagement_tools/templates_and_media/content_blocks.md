---
nav_title: Content Blocks
page_order: 1

page_type: reference
description: "This reference article explains how to use the Content Blocks Library to manage your reusable, cross-channel content in a single, centralized location."
tool: 
- Templates
- Media
---

# Content Blocks

> The Content Blocks Library allows you to manage your reusable, cross-channel content in a single, centralized location. To access this feature please go into the __Content Blocks Library__ tab in the [Templates & Media][6] section of your Braze account.

With Content Blocks, you can:

- Create a consistent look and feel to your Email campaigns using Content Blocks as Headers and Footers.
- Distribute the same offer codes through different channels.
- Create pre-defined assets that can be used to build messages with consistent information and assets.
- Copy entire message bodies to other messages.

## Create a Content Block

Creating a Content Block is easy - go to __Templates & Media__, then the __Content Blocks Library__ tab. Then, click __Create Content Block.__

Then, create your Content Block!

![create-content-blocks][1]

Content Blocks currently have two types: `HTML` or `text`. Braze will select the type for you based on the content you inserted into the block. If Braze detects `HTML` markup in the Content Block, the block type will switch to `HTML` automatically. Otherwise, it will be considered `text`.  

{% comment %}
While there is little value to having ‘types’ today, it will become important in the future as we add additional types.  We envision better validation being done, as well as a more specific UI based on the type selected.
{% endcomment %}

You can also [create and manage your Content Blocks via API][5].

## Using Content Blocks

1. Create your Content Block.
2. Copy the Content Block Liquid Tag from your Content Block page.
3. Insert the Content Block Liquid Tag into the message. You can also begin typing the Liquid and have the tag auto-populate.

## Updating & Copying Content Blocks

If you choose to update a Content Block, it will update in all messages the Content Block is used.

If you want to update a Content Block for a single message or make a copy of a Content Block to use in other messages, you can either copy the HTML from the original message to your new one or edit the original Content Block (it must have been used in a message already) and save it. You will then get a prompt that allows you to save it as a new Content Block.

![copy-content-block][2]{: height="70%" width="70%"}

You can also [duplicate a Content Block with our Templates & Media feature]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/duplicate/). When you do this, a "draft" copy is created.

## Nesting Content Blocks

Content blocks can be nested, but only once! You can nest _Content Block A_ into _Content Block B_, but you will not be able to then nest _Content Block B_ into Content _Block C_.

{% alert warning %}
Nothing will prevent you from nesting a third level of Content Block, but you will not see the content expand in nests beyond the second. The content and the Liquid snippet are removed from the message.
{% endalert %}

Additionally, Content Blocks cannot be used within an email footer, though email footers can be used within Content Blocks.

## Archiving Content Blocks

Once you have finished using a Content Block, you can [archive it from the __Templates & Media__ page]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/archive/).

![Archive_CB][3]{: height="80%" width="80%"}

Messages using the archived Block will still perform as though it was there, though we do recommend several best practices to ensure that outdated information is not included accidentally in your emails.

1. When your Block is only used in a few emails, we recommend archiving the outdated Block and updating your live messages with a newer Block that has not been archived.
2. When your Block only has a typo or needs a minor change, we do not recommend archiving the Block. Just update and get sending!
3. When your Block is used in more messages than you can reasonably manage with the first suggestion in this list, we recommend removing __all__ content from the Block, then archiving it. This will ensure no outdated information makes its way into any newly sent emails.

{% alert tip %}
  You can save a content block without content in it.
{% endalert %}

If you made a mistake in archiving a Content Block, you can unarchive it.  

![Unarchive_CB][4]

## Content Block Specifications

| Content Block Attribute | Specifications |
|---|---|
| Name | Required field limited to 100 characters. It cannot be renamed after Content Block has been saved. Additionally, you cannot name a new Content Block the same name as a previous Content Block, even if the previous one has been archived. |
| Description | Optional field limited to 250 characters. Describe the Content Block so that others viewing it in the Braze product will know what it's for and where it's being used. |
| Content Size | Limited to 50kB (Kilobyte). |
| Placement | Content Blocks cannot be used within an email footer. |
| Creation | HTML or Text. |
{: .reset-td-br-1 .reset-td-br-2}

[1]: {% image_buster /assets/img/create-content-blocks.gif %}
[2]: {% image_buster /assets/img/copy-content-block.png %}
[3]: {% image_buster /assets/img/archive-content-block.png %}
[4]: {% image_buster /assets/img/unarchive-content-block.png %}
[5]: {{site.baseurl}}/api/endpoints/templates/
[6]: {{site.baseurl}}/user_guide/engagement_tools/templates_and_media/

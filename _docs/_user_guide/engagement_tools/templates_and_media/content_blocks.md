---
nav_title: Content Blocks
page_order: 2
---

# Content Blocks

The Content Blocks Library allows you to manage your reusable, cross-channel content in a single, centralized location. To access this feature please go into the __Content Blocks Library__ tab in the [Templates & Media][4] section of your Braze account.

With Content Blocks, you can:

- Create a consistent look and feel to your Email campaigns using Content Blocks as Headers and Footers.
- Distribute the same offer codes through different channels.
- Create pre-defined assets that can be used to build messages with consistent information and assets.
- Copy entire message bodies to other messages.

## Create a Content Block

Creating a Content Block is easy - go to __Templates & Media__, then the __Content Blocks Library__ tab. Then, click __Create Content Block.__

Then, create your Content Block!

![create-content-blocks][1]

- You can save a content block without content in it.

Content Blocks currently have two types: `HTML` or `text`. Braze will select the type for you based on the content you inserted into the block. If Braze detects `HTML` markup in the Content Block, the block type will switch to `HTML` automatically. Otherwise, it will be considered `text`.  

{% comment %}
While there is little value to having ‘types’ today, it will become important in the future as we add additional types.  We envision better validation being done, as well as more specific UI based on the type selected.
{% endcomment %}

## Using Content Blocks

1. Create your Content Block.
2. Copy the Content Block Liquid Tag from your Content Block page.
3. Insert the Content Block Liquid Tag into the message. You can also begin typing the liquid and have the tag auto-populate.

## Updating & Copying Content Blocks

If you choose to update a Content Block, it will update in all messages the Content Block is used.

If you want to update a Content Block for a single message or make a copy of a Content Block to use in other messages, you can either copy the HTML from the original message to your new one, or edit the original Content Block (it must have been used in a message already) and save it. You will then get a prompt that allows you to save it as a new Content Block.

![copy-content-block][2]

## Nesting Content Blocks

Content blocks can be nested, but only once! You can nest _Content Block A_ into _Content Block B_, but you will not be able to then nest _Content Block B_ into Content _Block C_.

{% alert warning %}
Nothing will prevent you from nesting a third level of Content Block, but you will not see the content expand in nests beyond the second. The content and the liquid snippet are removed from the message.
{% endalert %}

Additionally, Content Blocks cannot be used within an email footer, though email footers can be used within Content Blocks.

## Content Block Specifications

| Content Block Attribute | Specifications |
|---|---|
| Name | Required field limited to 100 characters. Cannot be renamed after Content Block has been saved. Additionally, you cannot name a new Content Block the same name as a previous Content Block, even if the previous one has been deleted. |
| Description | Optional field limited to 250 characters. Describe the Content Block so that others viewing it in the Braze product will know what it's for and where it's being used. |
| Content Size | Limited to 50kb. |
| Placement | Content Blocks cannot be used within an email footer. |
| Creation | HTML or Text. |

[1]: {% image_buster /assets/img/create-content-blocks.gif %}
[2]: {% image_buster /assets/img/copy-content-block.png %}

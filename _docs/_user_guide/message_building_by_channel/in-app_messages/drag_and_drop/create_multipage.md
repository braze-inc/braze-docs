---
nav_title: Creating an In-App Message
article_title: "Creating an in-app message with drag-and-drop"
description: "This reference article covers creating a multi-page in-app message with the drag-and-drop editor."
alias: "/create_dnd_iam/"
page_order: 1.5
---

# Creating a multi-page in-app message

> Use the drag-and-drop editor to create sequential multi-page in-app messages.

> IMAGE

{% alert important %}
Multi-page in-app messages are currently in early access. Contact your Braze account manager if you’re interested in participating in this early access.
{% endalert %}

## Steps

### Step 1: Set up your message and page styles

Before you start customizing your message content, you can set message-level styles for the entire message using the right-hand menu.

For example, you may want to customize the font of all the text or the color of all the links included in your message. By setting a default for the entire message, you don't need to style elements individually. 

You can also override the message level styles for individual pages, with the exception of display type and max width.

### Step 2: Add new page from template library

Add new pages from the **Build** tab, under **Pages**. You can duplicate an existing page or add one from the available Braze or custom templates.

You can delete and rename pages from this area.

### Step 3: Style your message

Here's where your message gets to strut down the runway, dressed in your brand's signature style. Check out [drag-and-drop components]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/create/#drag-and-drop-in-app-message-components) for help customizing the look and feel of your message.

### Step 4: Connect the pages together

Multi-page in-app messages are sequential, which means users interact with the message by tapping or clicking to move to the next page.

To connect pages together:

1. Select your starting page.
2. Select a button or image element.
3. Set **On-click behavior** to **Go to page**.
4. Select the page you want to link to from the starting page.
5. Continue until all pages are linked.

> IMAGE

If a page is not linked to any other page, the message can't be launched.

{% alert note %}
Users can press the close X button to exit the message at any time. This button can't be removed.
{% endalert %}



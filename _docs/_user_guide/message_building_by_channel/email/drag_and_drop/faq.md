---
nav_title: FAQ
article_title: Drag-and-Drop Editor FAQ
alias: "/dnd/faq/"
channel: email
page_order: 5
description: "This article covers various FAQ related to the drag-and-drop editor."
tool: 
  - Campaigns
  - Canvas
  
---

# Frequently asked questions

> This page provides answers to some frequently asked questions related to the drag-and-drop editor for email.

### Can I preview how my email appears in dark mode?

Yes. Go to the **Preview and Test** section of the drag-and-drop editor and turn on **Dark mode**. We recommend also previewing and testing your emails across different user platforms and using transparent images for row background images when possible. 

### How can I change the email padding on mobile without updating the padding in the web view?

You cannot edit the padding for mobile and web views exclusively, so any edits are reflected in both views. However, you can add CSS logic in the HTML editor that sets the padding based on different screen sizes. This isn't supported in the drag-and-drop editor, so you can export the HTML file and use the HTML editor instead.

### How can I optimize a row of buttons to remain horizontal on desktop and mobile?

When building an email using the drag-and-drop editor, if you create a horizontal row of call-to-action buttons, you may find that the buttons are changed to a vertical orientation on mobile. 

To retain the same format across device sizes, we recommend creating a separate row with CTA buttons that have padding optimized for mobile and are set to hide the row on a desktop device. Having two separate rows means that you can set the desired padding for the best text rendering on desktop and mobile devices.


### Can I adjust the row height in the drag-and-drop editor?

The row height auto-adjusts to the content. As an alternative, we recommend that you:
1. Add a divider block.
2. Click the toggle to turn on its transparency.
3. Adjust the height.

### Is it possible to build layers in the editor? Can I add a background image, layer on an image, and add a text layer over that?

The drag-and-drop editor currently supports two layers. You can set a row background image and customize background colors.

### Can I save my drag-and-drop email as a template after I build it within my campaign or Canvas?

No, you must recreate the email in **Email Templates** to save it.

### Can I add email attachments to the drag-and-drop editor?

No, the drag-and-drop editor does not support adding attachments to your emails.

## Best practices on handling how emails show in dark mode vs light mode (BD-4015)

Workarounds and Best Practices are provided in the KA and we can include these.


## Customizing Emails for Dark Mode and Light Mode (BD-4300)

Add: Generally, emails do not need to be sent in both Light and Dark Mode styles. However, we have seen instances where emails lack explicit background colors or look broken or not as intended when the end user receiving the email is using Dark Mode themes on their device. The prefers-color-scheme CSS media query may be a place that can help with the design emails specifically for both dark and light themes. Here is a Braze Perspectives article on Dark Mode. Add: Gmail does not support the prefers-color-scheme media query. You can read the support for this query here . In addition, Litmus has


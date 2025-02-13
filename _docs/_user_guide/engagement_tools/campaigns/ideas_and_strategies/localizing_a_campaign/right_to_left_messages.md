---
nav_title: Right-to-Left Messages
article_title: Creating Right-to-Left Messages
page_order: 1
page_type: reference
description: "This page covers best practices for crafting messages in Braze that read from right-to-left."
---

# Creating right-to-left messages

> The final appearance of right-to-left messages depends largely on how service providers (such as Apple, Android, and Google) render them. This page covers best practices for crafting right-to-left messages so that your messages display accurately as much as possible.

## How it works

There are three key areas to consider when creating a right-to-left message: 
- How the message appears in your Braze dashboard
- How the message appears when delivered
- What happens in between creation and delivery

When a message appears on a user's device, its appearance is largely determined by how providers (like Apple and Microsoft) handle it, which depends on the device’s language settings. For example, an Arabic message will look different if the device is set to English instead of Arabic. 

Apple and Android have significant control over how messages are rendered, while email service providers (ESPs) have some control. HTML email customization in Braze can be more flexible; however, the same message may still render differently on different devices based on a user’s settings.

Though Braze has limited control over the final appearance of right-to-left messages, our goal is to facilitate accurate end results as much as possible. Use the following tips and tricks as guidance while you create right-to-left messages.

## Creating a right-to-left message

The most common way to craft right-to-left messages in Braze is:

1. Create a left-to-right message in a Braze editor.
2. Copy the message text from Braze and then use a localization tool to localize it to a right-to-left message.
3. Confirm the alignment is properly formatted by using a word processor (such as Word).
- You can skip this step if you’re creating a drag-and-drop or HTML email message. The drag-and-drop editor allows you to change text direction by selecting a button, and the HTML editor allows you to customize right-to-left alignment. <br><br>![Email drag-and-drop editor menu with button to toggle text alignment between right-to-left and left-to-right.][1]{: style="max-width:50%;"}

{: start="4"}
4. Paste the formatted text into Braze.

## Special considerations for right-to-left messages
 
### Long push notifications

The copy-and-paste method for push messages can be challenging to use with longer push notifications because longer content may render into multiple lines on a mobile device. If you copy your message text from outside of Braze (such as a Word document) and directly paste it into Braze, the sentence alignment and word placement may change. To avoid this scenario, copy and paste in installments and add a line break. For example, copy and paste the first five words, add a line break, copy the next five words, add a line break, and so on.

The preview and test functions are built for left-to-right messages, so right-to-left messages won’t render properly in the **Preview & Test** section but will render properly on user devices if their settings are configured for it. We suggest sending messages to yourself in a live environment to confirm that they render properly based on device settings.

### Bi-directional text

Many users who write in right-to-left languages are actually using bi-directional text: a combination of left-to-right and right-to-left languages. For example, a marketer may send a message in Hebrew with an English company name. Braze cannot handle the formatting of bi-directional text. Two ways to avoid formatting issues are to either completely avoid bi-directional text or separate left-to-right text from right-to-left text using line breaks. 

{% alert tip %}
Proper formatting for bi-directional text is especially important when crafting messages that include promo codes; promo codes are often in a left-to-right format because the same codes may be used across markets. Two ways to accommodate promo codes are to either use an image for the promo code or add the promo code at the end of the message after a line break.
{% endalert %}

### Special characters, numbers, and emojis

Special characters (such as punctuation, mathematical symbols, and currency), numbers, bullet points, and emojis may “jump around” when crafting right-to-left messages in Braze. To work around this, write your copy with proper formatting in an external word processor, and then paste the copy into Braze. It may also help to avoid placing emojis at the beginning of your text and instead separate them (and special characters and numbers) from text with line breaks to avoid alignment issues.

[1]: {% image_buster /assets/img/rtl_button.png %}
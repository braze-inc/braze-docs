---
nav_title: Right-to-left messages
article_title: Create Right-to-Left Messages
page_order: 1
alias: /right_to_left_messages/
page_type: reference
description: "This page covers best practices for crafting messages in Braze that read from right-to-left."
---

# Create right-to-left messages

> The final appearance of right-to-left messages depends largely on how service providers (such as Apple, Android, and Google) render them. This page covers best practices for crafting right-to-left messages so that your messages display accurately as much as possible.

## Message appearance

When creating a right-to-left message, keep the following in mind:

- **Appearance in Braze dashboard:** When a message appears on a user's device, its appearance is largely determined by their device’s operating system and language settings&#8212;meaning what you see in the dashboard isn't always 100% accurate.
- **Appearance on the device:** Apple and Android have significant control over how messages are rendered, while email service providers (ESPs) have some control. HTML email customization in Braze can be more flexible; however, the same message may still render differently on different devices based on a user’s settings.

Additionally, check punctuation and emojis to determine if your message is rendering standard or right-to-left.

| Standard Western Rendering | Right-to-Left Rendering |
|------------------|------------------------|
| Displays the exclamation point and emoji at the **end** of the sentences. | Displays the exclamation point and emoji at the **beginning** of the sentence. |
| ![An example of a standard right-to-left messages.]({% image_buster /assets/img/right-to-left/standard.png %}) | ![An example of a left-to-right messages.]({% image_buster /assets/img/right-to-left/right-to-left.png %}) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

## Creating a right-to-left message

To create your right-to-left message in Braze:

1. Draft your standard message in the Braze editor.
2. Copy the message text from Braze, then use a localization tool to convert it to a right-to-left message.
3. Paste your converted message back into Braze.
4. Verify the text formatting and alignment. If you’re creating a drag-and-drop or HTML email message, you can do this within the composer. Otherwise, you'll need to use a separate wordprocessor.<br><br>![Email drag-and-drop editor menu with button to toggle text alignment between right-to-left and left-to-right.]({% image_buster /assets/img/rtl_button.png %}){: style="max-width:50%;"}

## Considerations
 
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

### Arabic messages

When composing Arabic messages, use significantly higher font point sizes for the same readability you'd achieve with other languages. We suggest using a font size about 20% larger than your usual size for languages that use the Latin or Roman alphabet. This is because Arabic fonts are made small to accommodate the vertical space taken up by diacritics (accent marks).

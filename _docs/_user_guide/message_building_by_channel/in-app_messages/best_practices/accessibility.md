---
nav_title: Accessibility
article_title: Building Accessible In-App Messages in Braze
page_order: 0
page_type: reference
description: "This article covers best practices regarding building accessible in-app messages in Braze."
channel: in-app messages

---

# Building accessible in-app messages in Braze

## Header and body text

Keep your header and body text descriptive, enticing, and short. Test your copy to make sure your text isn’t truncated—this hurts all users. Refer to our [image and text specifications]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/creative_details) for more on this topic.

Your text also needs to be readable—so choose your fonts carefully. If you’re using the newest generation of in-app messages (Generation 3), your in-app messages will use the default font for the user’s operating system (Sans Serif for iOS and Android, Helvetica for web).

## Buttons

Write button text that clearly describes the action that will happen when a user presses it (e.g., “Read the full story” rather than “Read more”). Test to ensure your button text isn’t too long. If the button can’t display all of the text, it will truncate with an ellipsis as opposed to the text wrapping to a new line.

Touch targets (the size of interactable elements) are another important consideration when designing in-app messages, but there’s no extra work needed from you!

In-app messages created in Braze have minimum widths and heights for buttons, which ensures they follow modern accessibility best practices for minimum touch targets (so that fingers of all abilities and sizes can accurately hit them). The placement and size of buttons are universal across all modal and full-screen layouts.

![Touch targets for in-app messages. Button containers have a height of ninty-five pixels, while the buttons themselves have a height of fourty-four pixels and include thirty pixels of padding below the button.]({% image_buster /assets/img_archive/iam_touch_targets.png %}){: style="border:0px;"}

## Images 

Some users aren’t able to see the images in your in-app messages. Avoid using images of text, as screenreaders can’t read text that’s contained inside an image.

## Color contrast

Having sufficient color contrast can be a quick win for accessibility. Around 1 in 12 men and 1 in 200 women have some degree of color vision deficiency, an estimated 300 million people in the world (see [NHS Colour vision deficiency](https://www.nhs.uk/conditions/colour-vision-deficiency/)).

The contrast ratio between foreground (text) and background colors should comply with the following [WCAG 2.1 AA level requirements](https://www.w3.org/TR/WCAG/#contrast-minimum):

- Contrast ratio of 4.5:1 for normal text (your in-app message body and buttons)
- Contrast ratio of 3:1 for large text (your in-app message header)

You can use the [WebAim Contrast Checker Tool](https://webaim.org/resources/contrastchecker/) to see if your text is readable against background colors.

## Animations

While you can create a [custom HTML in-app message]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/customize/#custom-html-messages) and use CSS to add animation, it’s important to provide users with a way to control their experience. This will help people with ADHD, vestibular disorders, seizure disorders, and more. Small animations can just be distracting, while larger animations can make people sick.

![Motion accessibility settings for iOS with Reduce Motion and Prefer Cross-Fade Transitions turned on.]({% image_buster /assets/img_archive/ios_reduce_motion_settings.jpg %}){: style="float:right;margin-left:15px;max-width:35%;"}

If your in-app message contains any animation, consider offering an option to turn off or reduce motion. You can so do with a button or toggle switch to reduce or turn off animation globally on your app or site (such as in user settings, if your app or site includes this). Think of it as taking the [pause controls](https://www.w3.org/WAI/WCAG21/Understanding/pause-stop-hide.html) the WCAG recommends for animations and applying them globally. This does take a little more work at the outset, but it offers an important option.

Make sure to respect device settings. If a user has “reduce motion” turned on, the animation shouldn’t play.

## Modal and full-screen considerations

Modal and full-screen in-app messages are a type of dialog—a window overlaid on the current window. Because they take over the user’s screen, there are specific guidelines you should follow to make them usable. Refer to the [WAI-ARIA Authoring Practices for dialogs](https://w3c.github.io/aria-practices/#dialog_modal) for complete guidelines, but here are some key points to consider:

- Focus should move to the in-app message.
- Focus should be trapped in this content. All other content must be blocked, so tabbing or using a screenreader stays within the in-app message.
- Pressing the <kbd>Escape</kbd> key should close the in-app message.
- When closed, focus moves back to the element that opened it. If the message appears without user interaction (i.e., the user didn’t press a button to make it appear), you can move focus to the first element on the screen after the message closes.
- There should be a visible way to dismiss the message, such as a close button.

{% alert tip %}
People can use keyboards on mobile too, so consider these key points even if you aren’t working with a desktop website!
{% endalert %}
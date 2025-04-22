---
nav_title: Building Accessible Messages
article_title: Building Accessible Messages in Braze
page_order: 3.5
page_type: reference
description: "This reference article explains why accessibility is important to consider in your marketing content, and how you can build accessible messages in Braze."
---

# Building accessible messages in Braze

> Understand why accessibility is important to consider in your marketing content, and how you can build accessible messages in Braze. For more detailed guidance, check out our [Accessible Messaging Foundations](https://learning.braze.com/accessible-messaging-foundations) course on Braze Learning.

Marketing content that excludes people with disabilities, even unintentionally, can prevent millions of people from interacting with your brand. Accessibility in marketing is about making it easy for everyone to experience your marketing, receive and understand your communication, and have the opportunity to invest in or become a fan of your product, service, or brand. When designing your messaging, take the extra time to consider how you can make your designs accessible to all your customers.

{% alert important %}
This content is intended for general guidance and doesn’t guarantee compliance with accessibility standards such as WCAG. Braze offers tools that support the creation of more accessible messaging, but it’s your responsibility to ensure that your final content meets any applicable requirements. Any recommendations provided here are meant to help you get started and reflect the current capabilities of our platform.
{% endalert %}

If you have feedback about accessibility of Braze or messages sent from Braze, we'd love to hear from you. Open the **Support** menu in the global header and select **Share feedback** to send us your thoughts.

## Areas of disability to consider

*This section is partially adapted from [W3C: Diverse Abilities and Barriers](https://www.w3.org/WAI/people-use-web/abilities-barriers/).*

{% tabs local %}
{% tab Visual %}

Visual disabilities can range from mild or moderate vision loss in one or both eyes, to substantial or complete loss of vision in both eyes. Some people have reduced or lack sensitivity to certain colors or increased sensitivity to bright colors.

To interact with your content, these users need the ability to:

- Enlarge or reduce text size and images
- Customize settings for fonts, colors, and spacing
- Listen to text-to-speech synthesis of the content (that is, use a screen reader)
- Listen to audio descriptions of video
- Read text using refreshable Braille

{% alert note %}
- Globally, at least 2.2 billion people have a near or distance vision impairment (see [WHO](https://www.who.int/news-room/fact-sheets/detail/blindness-and-visual-impairment))
- Around 1 in 12 men and 1 in 200 women have some degree of color vision deficiency, an estimated 300 million people in the world (see [NHS](https://www.nhs.uk/conditions/colour-vision-deficiency/))
{% endalert %}

{% endtab %}
{% tab Hearing %}

Hearing or auditory disabilities can include mild to moderate hearing impairment in one or both ears. Even partial loss of hearing can be problematic in regards to audio content.

To understand your content, these users rely on:

- Transcripts and captions of audio content
- Media players that display captions and provide options to adjust the text size and colors of captions
- Options to stop, pause, and adjust the volume of audio content (independent of the system volume)
- High-quality foreground audio that is clearly distinguishable from any background noise

{% alert note %}
- One in eight people in the United States (13%, or 30 million) aged 12 years or older has hearing loss in both ears, based on standard hearing examinations
- Approximately 15% of American adults (37.5 million) aged 18 and over report some trouble hearing (see [NIH](https://www.nidcd.nih.gov/health/statistics/quick-statistics-hearing))
{% endalert %}

{% endtab %}
{% tab Physical %}

Physical disabilities can include weakness and limitations of muscle control or sensation, joint disorders, pain that impedes movement, and missing limbs.

These users rely on keyboard support to activate functionality (even if they aren't using a standard keyboard). To interact with your content, these users need:

- Large clickable areas
- Enough time to complete tasks
- Visible indicators of the current focus
- Mechanisms to skip over blocks of content, like page headers or navigation bars

{% alert note %}
Almost 2 million people in the US live with limb loss (see [Amputee Coalition](https://www.amputee-coalition.org/limb-loss-resource-center/resources-filtered/resources-by-topic/limb-loss-statistics/limb-loss-statistics/#1))
{% endalert %}

{% endtab %}
{% tab Cognitive %}

Cognitive, learning, and neurological disabilities involve neurodiversity and neurological disorders, as well as behavioral and mental health disorders that aren't necessarily neurological. They may affect any part of the nervous system and impact how well people hear, move, see, speak, and understand information.

Depending on individual needs, these users rely on:

- Clearly structured content
- Consistent labeling of forms, buttons, and other content
- Predictable link targets and overall interaction
- Different ways to navigate, such as menus and search bars
- Settings to turn off blinking, flashing, or otherwise distracting content
- Simpler text that is supported by images


{% alert note %}
- One in five people in the United States have learning and attention issues (see [LDA](https://ldaamerica.org/lda_today/the-state-of-learning-disabilities-today/#:~:text=LD%20Today,have%20learning%20and%20attention%20issues.))
- Roughly 10–20% of the global population is considered neurodivergent (see [Deloitte](https://www2.deloitte.com/us/en/insights/topics/talent/neurodiversity-in-the-workplace.html))
- About 1 in 100 children has autism worldwide (see [WHO](https://www.who.int/news-room/fact-sheets/detail/autism-spectrum-disorders))
{% endalert %}

{% endtab %}
{% endtabs %}

## Best practices

### Content

#### Write short, clear sentences
Short sentences are easy for everyone to understand, especially people using screen readers or who have trouble processing complex information. Write to a United States seventh-grade reading level. You can use resources such as [Hemingway App](https://hemingwayapp.com/) to check your text's reading level.

#### Break your content into sections
Using headings, bullet points, and lists helps people quickly understand and scan your content—even when they’re in a hurry. Clearly describe each section to help readers navigate easily and understand the content structure.

#### Don't skip heading levels

Headings give your content structure, helping readers quickly understand how sections relate to each other. When you skip heading levels (for example, jumping straight from an H2 to an H4), you break this logical structure. This makes it harder for users, especially those using screen readers, to navigate and understand your message clearly.

Always follow a logical, sequential hierarchy of headings (H1 to H2 to H3, and so on) to make sure your content stays organized, accessible, and easy for everyone to follow.

#### Avoid justified text
Justified text creates uneven spacing between words, making reading difficult for people with dyslexia or cognitive disabilities. Consider making content that wraps to more than two lines aligned left for left-to-right languages or aligned right for right-to-left languages.

#### Give your text room to breathe
Extra spacing between lines (around 1.5 line-height) and paragraphs improves readability, especially for people with visual or cognitive needs.

#### Use bold, italic, and uppercase text sparingly
Emphasizing too much text makes reading difficult—especially for people with dyslexia or visual impairments. Keep it simple.

#### Clearly label links and buttons
Make sure your [link](#links) and [button](#buttons) text clearly explains what happens next. It helps people using screen readers or navigating with a keyboard know what to expect.

#### Don’t rely on color alone to communicate
Color is great, but pair it with clear text labels or symbols so no one misses important information.

#### Go easy on symbols and emojis
Special characters and emojis can make your content playful, but they can be confusing when read by screen readers. Use them sparingly, and make sure they don’t replace clear, descriptive text.

#### Test for truncation
Always test your copy by [sending a test message]({{site.baseurl}}/developer_guide/in_app_messages/sending_test_messages/) to a device to make sure your text isn't truncated. If your message is being cut off, this hurts both you and the user, since it prevents your content from reaching your users.

### Buttons

Use **buttons** to indicate an action, such as sending a form or playing a carousel. If you’re navigating to a new URL, consider using a [link](#links) instead.

#### Write clear, action-oriented text

Similar to link text, button labels should clearly describe the action. Effective button text is specific and action-oriented. For example, “Submit Order” clearly tells users what will happen when they click, whereas simply “Submit” can be ambiguous. Each label should precisely describe its intended action, so screen readers and all users can easily understand and predict the outcome when interacting with your buttons.

<table role="presentation" class="reset-td-br-1 reset-td-br-2">
  <thead>
    <tr>
      <th style="width: 50%">Good button text</th>
      <th style="width: 50%">Poor button text</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>"Submit Order"</td>
      <td>"Submit"</td>
    </tr>
    <tr>
      <td>"Create Account"</td>
      <td>"Sign Up"</td>
    </tr>
    <tr>
      <td>"Download Our Brochure"</td>
      <td>"Download"</td>
    </tr>
    <tr>
      <td>"View Product Details"</td>
      <td>"Learn More"</td>
    </tr>
    <tr>
      <td>"Subscribe for Updates"</td>
      <td>"Subscribe"</td>
    </tr>
  </tbody>
</table>

Keep button text concise to prevent truncation. If a button’s text is too long, it may be cut off with an ellipsis instead of wrapping.

#### Use sufficient color contrast

Button text must be easy to read against the button’s background color. Check that your button text meets WCAG 2.2 AA [contrast minimums](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html):

- 4.5:1 contrast ratio for normal-sized text (most buttons)
- 3:1 contrast ration for large text (typically above 18pt)

High contrast helps buttons remain readable and clickable for everyone, including users with visual impairments or viewing your message in challenging environments. For more guidance, see the [Color contrast](#color-contrast) section.

### Links

Use links for navigation, like directing users to an external page.

Write link text that clearly describes where the link will take the user. Screen reader users often skip from link to link as a way of skimming through content, so make sure your link text can stand on its own. Avoid phrases like "click here," "more," and "click for details," as they are ambiguous when read out of context.

For example, consider how you might write a link to view a weather report.

| Bad  | Better | Best |
| --- | --- | --- | 
| Click here | Click here to access today's weather | Today's weather |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

As with all content, keep it straightforward with as few extra words as possible.

#### Avoid styling links like buttons

Braze drag-and-drop editors output semantic HTML by default, so links aren’t styled like buttons there. However, if you’re working with [custom HTML](#custom-html) or making code-level changes, keep this in mind:

- **Links (`<a>`)** respond to the <kbd>Enter</kbd> key.
- **Buttons (`<button>`)** respond to both the <kbd>Enter</kbd> or <kbd>Space</kbd> keys.

Styling a link to look like a button can confuse people who navigate with a keyboard—they might try pressing <kbd>Space</kbd> and expect it to work.

Use the right element for the action:

- Use `<button>` for actions, like submitting a form or opening a modal.
- Use `<a>` for navigation, such as linking to another page or file.

{% raw %}

```html
<!-- Recommended: A true button for an action -->
<button type="button">Download report</button>

<!-- Not recommended: A link styled as a button -->
<a href="#" class="btn">Download report</a>
```

{% endraw %}

### Images

#### Provide alt text

Alternative text (alt text) is a short description of the content or function of an image that screen readers and other assistive technologies provide to users. For every meaningful image, write descriptive alt text so users who can’t see the visuals still understand your message or call to action. 

#### Avoid images of text

Whenever possible, avoid placing text inside images—screen readers can’t read image-based text, and users can’t easily adjust font size or color for better visibility. Consider these tips:

- **Remove text where you can:** Move any descriptive or promotional text from the image onto a text field in your message instead. This way, users can resize or recolor it as needed using their device or browser preferences.
- **Test for readability and contrast:** If you must keep text in the image, follow [color contrast](#color-contrast) best practices and use a [large scale font](https://www.w3.org/WAI/WCAG21/Understanding/contrast-minimum.html#dfn-large-scale). This means text should be at least 18 points (about 24 pixels) for non-bold text or 14 points (about 18 pixels) if it’s bold. Using these sizes helps text remain legible without forcing users to zoom in, and it improves the overall contrast and readability of the content. Test to confirm it’s still legible on smaller screens.
- **Provide alt text:** For essential text that must remain in the image, include alt text describing the words.

When images contain text that can’t be edited, users with visual impairments lose the flexibility to make reading adjustments. By separating text from images, you help more users read and interact with your message comfortably.

#### Tips for writing alt text

##### 1. Describe what's actually in the image

Screen reader users rely on alt text to understand the content or function of an image. Avoid generic “marketing speak” that doesn’t match what’s visually shown.

<table role="presentation" class="reset-td-br-1 reset-td-br-2">
  <thead>
    <tr>
      <th style="width: 50%">Good examples</th>
      <th style="width: 50%">Poor examples</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>"Smiling woman wearing a blue denim jacket, holding a shopping bag."</td>
      <td>"Time to treat yourself!" (No mention of what’s actually in the image)</td>
    </tr>
    <tr>
      <td>"Man wearing a black T-shirt, leaning on a bike in a city street."</td>
      <td>"Embrace your best life now!" (Ignores the bike and city setting)</td>
    </tr>
    <tr>
      <td>"Blue apartment building with a 'For Rent' sign in front."</td>
      <td>"The key to a better tomorrow!" (Doesn’t reflect the apartment or sign)</td>
    </tr>
  </tbody>
</table>

##### 2. Keep it short, yet specific

Concise alt text makes it easier for users to process. Include enough detail to convey purpose but skip any fluff. As a general rule, keep alt text to 125 characters or less. If anything more than a brief phrase or sentence is necessary, consider using one of the [long description methods](https://www.w3.org/WAI/tutorials/images/complex/) from W3C.

<table role="presentation" class="reset-td-br-1 reset-td-br-2">
  <thead>
    <tr>
      <th style="width: 50%">Good examples</th>
      <th style="width: 50%">Poor examples</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>"Red running shoes on a white background"</td>
      <td>"Running shoes that are extremely comfortable and perfect for your active lifestyle in a vibrant shade of red."</td>
    </tr>
    <tr>
      <td>"Four laptops on a display stand"</td>
      <td>"Discover the ultimate productivity booster that redefines how you work every day, in every way imaginable."</td>
    </tr>
    <tr>
      <td>"Group of friends eating ice cream on a sunny day"</td>
      <td>"Capture pure happiness with the sweetest treat—life is better with our brand of ice cream!"</td>
    </tr>
  </tbody>
</table>

##### 3. Avoid “image of” or “picture of” 

Screen readers already announce an image. Jump right into describing the subject.

<table role="presentation" class="reset-td-br-1 reset-td-br-2">
  <thead>
    <tr>
      <th style="width: 50%">Good examples</th>
      <th style="width: 50%">Poor examples</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>"Table set for brunch with pancakes, fruit, and coffee."</td>
      <td>"Image of a table set for brunch"</td>
    </tr>
    <tr>
      <td>"Roadside billboard with bold 'Grand Opening' text"</td>
      <td>"Picture of a billboard on the side of a road"</td>
    </tr>
    <tr>
      <td>"Snowy mountain landscape at sunset"</td>
      <td>"Photo of snow and mountains"</td>
    </tr>
  </tbody>
</table>

##### 4. Reflect text that appears in the image

If an image includes essential text, put that information in the alt text so users don’t miss it.

<table role="presentation" class="reset-td-br-1 reset-td-br-2">
  <thead>
    <tr>
      <th style="width: 50%">Good examples</th>
      <th style="width: 50%">Poor examples</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>"Banner reading ‘Summer Sale—50% off all swimwear.’"</td>
      <td>"Banner promoting a sale." (Fails to mention the actual discount)</td>
    </tr>
    <tr>
      <td>"Logo with the text ‘Café Toscana’ in script font"</td>
      <td>"Logo image for a café." (Doesn’t include text ‘Café Toscana’)</td>
    </tr>
    <tr>
      <td>"Ad announcing ‘Concert Tickets Available Now—Starts June 5th’"</td>
      <td>"Concert ad." (No event details)</td>
    </tr>
  </tbody>
</table>

##### 5. Stick to relevant context—no extra marketing jargon

Don’t pad alt text with SEO terms or calls to action not directly related to the image. Provide value for those who can’t see the image.

<table role="presentation" class="reset-td-br-1 reset-td-br-2">
  <thead>
    <tr>
      <th style="width: 50%">Good examples</th>
      <th style="width: 50%">Poor examples</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>"Laptop showing the Braze dashboard analytics chart"</td>
      <td>"Boost conversions and skyrocket ROI with the best platform on earth!"</td>
    </tr>
    <tr>
      <td>"Backyard patio set featuring four chairs and a glass table"</td>
      <td>"Host an incredible summer party for all your friends and family now!"</td>
    </tr>
    <tr>
      <td>"Mobile phone displaying a weather forecast app with 75°F in view"</td>
      <td>"Experience real-time innovations in weather tracking that's a game-changer"</td>
    </tr>
  </tbody>
</table>

##### 6. Consider the image's purpose

If an image is functioning like a link or call-to-action, describe the intended action (“Shop,” Link to,"“Sign up” ), not just the label or product shown.

<table role="presentation" class="reset-td-br-1 reset-td-br-2">
  <thead>
    <tr>
      <th style="width: 50%">Good examples</th>
      <th style="width: 50%">Poor examples</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>"Shop the Fall Collection"</td>
      <td>"Fall Collection"</td>
    </tr>
    <tr>
      <td>"Link to free eBook"</td>
      <td>"Free eBook"</td>
    </tr>
    <tr>
      <td>"Sign up for the mailing list"</td>
      <td>"Mailing list"</td>
    </tr>
  </tbody>
</table>

If the image doesn't have a purpose, make that known too. Decorative images, like logos, should have an empty alt tag (`alt=""`) so screen readers know to skip announcing it. Without it, usually the image file name is read instead.

### Videos

Videos are engaging, but if they’re not accessible, you risk excluding part of your audience. Use the following tips to make your video content more inclusive.

#### Provide closed captions

Include closed captions with your videos so users can follow along with the dialogue, sound effects, and other audio content. Captions help:

- People who are Deaf or hard of hearing
- Viewers watching in a sound-off environment
- Non-native speakers who prefer to read along

Closed captions can be toggled on or off, allowing users to choose what works best for them.

{% alert note %}
Braze doesn't automatically generate captions for your videos. It’s your responsibility to add accurate captions to your video files before including them in your message.
{% endalert %}

#### Provide playback controls

Make sure your embedded video includes accessible playback controls—such as play, pause, mute, and seek—so users can interact with it in the way that works best for them.

#### Avoid auto-play

Whenever possible, avoid setting videos to play automatically. Auto-play can be jarring or disorienting for:

- Users relying on screen readers or keyboard navigation
- People with motion sensitivity
- Anyone in a quiet environment (like a workplace or late-night setting)

Let users choose when to play a video by including clear controls.

#### Avoid flashing or strobing content

Don’t include videos with flashing or strobing effects, especially at a high frequency. These can trigger seizures in users with photosensitive epilepsy and cause discomfort for others.

### Color contrast

Sufficient color contrast helps ensure your messages are easy to read for everyone, including people with low vision or those viewing your content in bright or challenging conditions. Aim for contrast ratios that comply with [WCAG 2.2 AA level requirements](https://www.w3.org/TR/WCAG/#contrast-minimum):

- 4.5:1 contrast ratio for normal text (think body text, buttons, and links)
- 3:1 contrast ratio for large text (think headings and larger labels)

You can test your color choices using the [WebAim Contrast Checker Tool](https://webaim.org/resources/contrastchecker/).

{% alert note %}
Braze editors allow you to select custom color combinations. Keep in mind that certain color choices can negatively affect accessibility. Choose your colors carefully to make sure your content is readabile and compliant with accessibility standards.
{% endalert %}

### Forms

**Chunk longer forms into smaller sections** <br>To reduce cognitive load, break long forms into smaller sections. This is known as chunking, a progressive disclosure pattern used to make the information easier to consume. This benefits all users but is especially helpful for people with cognitive disabilities.

**Don't hide important content in tooltips or other hover states** <br>Content contained in hover states is less discoverable and mobile-friendly, and screen-magnifier users will struggle to view content that's only available on hover.

**Avoid blocking invalid characters in fields** <br>Don't prevent certain character types from being input in form fields. It's better to allow users to enter whatever they want and then provide an error message as to what's wrong. Blocking keyboard input poses a particular problem for assistive technology users, as they rely heavily on inline validation to determine if they've filled in the form correctly.

**Write clear error messages** <br>A good error message is made up of three parts: what's happened, what went wrong, and how they can fix it. Error messaging should be clear and easy to understand. Try to speak in simple language. There's no need for fancy jargon.
<br>

### Custom HTML

If you use any custom HTML in your messaging:

- Use [semantic HTML](https://developer.mozilla.org/en-US/docs/Learn/Accessibility/HTML). This means using the correct HTML elements for their intended purpose instead of styling one element to look like another. Most HTML elements have their own accessibility support built in.
- Set the language attribute within your HTML to identify the language that your content is in. Screen readers use different sound libraries for each language based on the pronunciation and characteristics of that language. If the language is specified, screen readers can automatically switch between language libraries as needed. For example:

{% raw %}
```html
<html lang="en-us">
```
{% endraw %}


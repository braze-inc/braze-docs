---
nav_title: Building Accessible Messages
article_title: Building Accessible Messages in Braze
page_order: 3.5
page_type: reference
description: "This reference article explains why accessibility is important to consider in your marketing content, and how you can build accessible messages in Braze."
---

# Building accessible messages in Braze

> Marketing content that excludes people with disabilities, even unintentionally, can prevent millions of people from interacting with your brand. Accessibility in marketing is about making it easy for everyone to experience your marketing, receive and understand your communication, and have the opportunity to invest in or become a fan of your product, service, or brand. When designing your messaging, take the extra time to consider how you can make your designs accessible to all your customers.

## Why accessibility matters

- **Better usability:** Accessibility encourages you to think about the usability of your app or site because you're thinking about how the user interacts with your content. That means accessibility often improves the online experience for all users, not just those with a disability.
- **Extend market reach:** The global market of people with disabilities is over 1 billion people with a spending power of nearly $7 trillion.
   > "The market of people with disabilities is large and growing as the global population ages. In the UK, where the large disability market is known as the Purple Pound, people with disabilities and their families spend at least £249 billion every year. In the US, the annual discretionary spending of people with disabilities is over $200 billion. The global estimate of the disability market is nearly $7 trillion."<br>*Source: [W3C](https://www.w3.org/WAI/business-case/)*
- **Minimize legal risk:** Many countries have laws requiring digital accessibility.

## Areas of disability to consider

*This section is partially adapted from [W3C: Diverse Abilities and Barriers](https://www.w3.org/WAI/people-use-web/abilities-barriers/).*

### Visual

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

### Hearing

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

### Physical

Physical disabilities can include weakness and limitations of muscle control or sensation, joint disorders, pain that impedes movement, and missing limbs.

These users rely on keyboard support to activate functionality (even if they aren't using a standard keyboard). To interact with your content, these users need:

- Large clickable areas
- Enough time to complete tasks
- Visible indicators of the current focus
- Mechanisms to skip over blocks of content, like page headers or navigation bars

{% alert note %}
Almost 2 million people in the US live with limb loss (see [Amputee Coalition](https://www.amputee-coalition.org/limb-loss-resource-center/resources-filtered/resources-by-topic/limb-loss-statistics/limb-loss-statistics/#1))
{% endalert %}

### Cognitive

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

## Best practices

### Content

- Keep your content on brand, but use plain language. Write to a United States seventh-grade reading level. You can use resources such as [Hemingway App](https://hemingwayapp.com/) to check your text's reading level.
- Structure your content logically, and make sure headings follow the correct hierarchy. Don't skip heading levels.
- Avoid center-aligned text for long chunks of content. This can be difficult for users with cognitive or learning disabilities to read. Content that wraps to more than two lines should be aligned left.
- Use sans-serif fonts, which are easier to read on digital devices.
- Always test your copy by [sending a test message]({{site.baseurl}}/developer_guide/in_app_messages/sending_test_messages/) to a device to make sure your text isn't truncated. If your message is being cut off, this hurts both you and the user, since it prevents your content from reaching your users.

### Links

Use links for navigation, like directing users to an external page.

{% alert tip %}
If you want something that looks and acts like a button, try to always use an actual button rather than styling a link like a button. Links and buttons may "feel" the same for average users—they can use their mouse to hover over the link or the button and click on them with their mouse—however, buttons and links have different controls (for example, buttons can be activated by pressing the <kbd>Space</kbd> key or the <kbd>Enter</kbd> key, but links can only be activated with the <kbd>Enter</kbd> key), which can lead to confusion if you style a link like a button.
{% endalert %}

Write link text that clearly describes where the link will take the user. Screen reader users often skip from link to link as a way of skimming through content, so make sure your link text can stand on its own. Avoid phrases like "click here," "more," and "click for details," as they are ambiguous when read out of context.

For example, consider how you might write a link to view a weather report.

| Bad  | Better | Best |
| --- | --- | --- | 
| Click here | Click here to access today's weather | Today's weather |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

As with all content, keep it straightforward with as few extra words as possible.

### Buttons

Use buttons for clickable actions, such as sending a form or playing a carousel.

Similar to link text, write button text that clearly describes the action that will happen when a user presses it (for example, "Read the full story" rather than "Read more"). Test to ensure your button text isn't too long. If the button can't display all of the text, it will truncate with an ellipsis as opposed to the text wrapping to a new line.

### Images

Some users aren't able to see the images in your marketing content. Without considering accessibility, images can become a barrier to all users receiving the same content.

#### Alt text

Alternative text is a short description of the content of the image that screen readers and other assistive technologies provide to their users.

- For every image, write alternative text that provides the information or function of the image.
- If the image is [decorative](https://www.w3.org/WAI/tutorials/images/decorative/) (doesn't add to the content), use an empty alt attribute (`alt=""`).
- Don't use the word "picture" or "image" in your alt text.

#### Images of text

Avoid using images of text, as screen readers can't read text that's contained inside an image. Images of text also don't resize well, and can't be customized to the user's needs and preferences. With actual text, users can customize things like color and contrast, and resize the text without losing quality. When images of text are enlarged, they become pixelated and lower quality, making them difficult to read.

### Videos

Provide closed captions for videos. They help people with vision loss, those watching in a noisy place, and those who speak a different language than the language in the video.

### Color contrast

Having sufficient color contrast can be a quick win for accessibility. The contrast ratio between foreground (text) and background colors should comply with [WCAG 2.1 AA level requirements](https://www.w3.org/TR/WCAG/#contrast-minimum):

- Contrast ratio of 4.5:1 for normal text (think body text, buttons, and links)
- Contrast ratio of 3:1 for large text (think headers)

You can use the [WebAim Contrast Checker Tool](https://webaim.org/resources/contrastchecker/) to see if your text is readable against background colors.

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


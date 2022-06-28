---
nav_title: Building Accessible Messages
article_title: Building Accessible Messages in Braze
page_order: 3.5
page_type: reference
description: "This reference article explains why accessibility is important to consider in your marketing content, and how you can build accessible messages in Braze."
---

# Building accessible messages in Braze

Marketing content that excludes people with disabilities, even unintentionally, can prevent millions of people from interacting with your brand. Accessibility in marketing is about making it easy for everyone to experience your marketing, receive and understand your communication, and have the opportunity to invest in or become a fan of your product, service, or brand. When designing your messaging, take the extra time to consider how you can make your designs accessible to all your customers.

## Why accessibility matters

- **Better usability:** Accessibility encourages you to think about the usability of your app or site because you're thinking about how the user interacts with your content. That means accessibility often improves the online experience for all users, not just those with a disability.
- **Extend market reach:** The global market of people with disabilities is over 1 billion people with a spending power of nearly $7 trillion.
   > "The market of people with disabilities is large and growing as the global population ages. In the UK, where the large disability market is known as the Purple Pound, people with disabilities and their families spend at least £249 billion every year. In the US, the annual discretionary spending of people with disabilities is over $200 billion. The global estimate of the disability market is nearly $7 trillion."<br>*Source: [W3C](https://www.w3.org/WAI/business-case/)*
- **Minimize legal risk:** Many countries have laws requiring digital accessibility, and the issue is of increased legal concern.

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

Hearing or auditory disabilities include mild to moderate hearing impairment in one or both ears. Even partial loss of hearing can be problematic in regards to audio content.

To understand your content, these users rely on:

- Transcripts and captions of audio content
- Media players that display captions and provide options to adjust the text size and colors of captions
- Options to stop, pause, and adjust the volume of audio content (independent of the system volume)
- High-quality foreground audio that is clearly distinguishable from any background noise

{% alert note %}
- 1 in 8 people in the United States (13%, or 30 million) aged 12 years or older has hearing loss in both ears, based on standard hearing examinations
- Approximately 15% of American adults (37.5 million) aged 18 and over report some trouble hearing (see [NIH](https://www.nidcd.nih.gov/health/statistics/quick-statistics-hearing))
{% endalert %}

### Physical

Physical disabilities include weakness and limitations of muscle control or sensation, joint disorders, pain that impedes movement, and missing limbs.

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
- 1 in 5 people in the United States have learning and attention issues (see [LDA](https://ldaamerica.org/lda_today/the-state-of-learning-disabilities-today/#:~:text=LD%20Today,have%20learning%20and%20attention%20issues.))
- Roughly 10–20% of the global population is considered neurodivergent (see [Deloitte](https://www2.deloitte.com/us/en/insights/topics/talent/neurodiversity-in-the-workplace.html))
- About 1 in 100 children has autism worldwide (see [WHO](https://www.who.int/news-room/fact-sheets/detail/autism-spectrum-disorders))
{% endalert %}

## Best practices

### Content

- Keep your content on brand, but use plain language. Write to a United States 7th grade reading level. You can use resources such as [Hemingway App](https://hemingwayapp.com/) to check your text’s reading level.
- Structure your content logically, and make sure headings follow the correct hierarchy. Don't skip heading levels.
- Avoid center-aligned text for long chunks of content. This can be difficult for users with cognitive or learning disabilities to read. Content that wraps to more than two lines should be aligned left.
- Use sans-serif fonts, which are easier to read on digital devices.
- Always test your copy by [sending a test message]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/sending_test_push_notifications/) to a device to make sure your text isn't truncated. If your message is being cut off, this hurts both you and the user, since it prevents your content from reaching your users.

### Links

Write link text that clearly describes where the link will take the user. Screen reader users often skip from link to link as a way of skimming through content, so make sure your link text can stand on its own. Avoid phrases like "click here," "more," and "click for details," as they are ambiguous when read out of context.

For example, consider how you might write a link to view a weather report.

| Bad  | Better | Best |
| --- | --- | --- | 
| Click here | Click here to access today's weather | Today's weather |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

As with all content, keep it straightforward with as few extra words as possible.

### Buttons

> TO DO

### Images

Some users aren’t able to see the images in your marketing content. Without considering accessibility, images can become a barrier to all users receiving the same content.

#### Alt text

Alternative text is a short description of the content of the image that screenreaders and other assistive technologies provide to their users.

- For every image, write alternative text that provides the information or function of the image.
- If the image is [decorative](https://www.w3.org/WAI/tutorials/images/decorative/) (doesn't add to the content), use an empty alt attribute (`alt=""`).
- Don't use the word "picture" or "image" in your alt text.

#### Images of text

Avoid using images of text, as screen readers can’t read text that’s contained inside an image. Images of text also don’t resize well, and can’t be customized to the user’s needs and preferences. With actual text, users can customize things like color and contrast, and resize the text without losing quality. When images of text are enlarged, they become pixelated and lower quality, making them difficult to read.

### Videos

Provide closed captions for videos. They help people with vision loss, those watching in a noisy place, and those who speak a different language than the language in the video.

### Color contrast

Having sufficient color contrast can be a quick win for accessibility. The contrast ratio between foreground (text) and background colors should comply with [WCAG 2.1 AA level requirements](https://www.w3.org/TR/WCAG/#contrast-minimum):

- Contrast ratio of 4.5:1 for normal text (think body text, buttons, and links)
- Contrast ratio of 3:1 for large text (think headers)

You can use the [WebAim Contrast Checker Tool](https://webaim.org/resources/contrastchecker/) to see if your text is readable against background colors.

### Forms

> TO DO

<br>
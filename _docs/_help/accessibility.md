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

## Why accessibility matters

- **Better usability:** Accessibility encourages you to think about the usability of your app or site because you're thinking about how the user interacts with your content. That means accessibility often improves the online experience for all users, not just those with a disability.
- **Extend market reach:** The global market of people with disabilities is over 1 billion people with a spending power of nearly $7 trillion.
   > "The market of people with disabilities is large and growing as the global population ages. In the UK, where the large disability market is known as the Purple Pound, people with disabilities and their families spend at least £249 billion every year. In the US, the annual discretionary spending of people with disabilities is over $200 billion. The global estimate of the disability market is nearly $7 trillion."<br>*Source: [W3C](https://www.w3.org/WAI/business-case/)*
- **Minimize legal risk:** Many countries have laws requiring digital accessibility.

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

Some users aren’t able to see the images in your marketing content. Without thoughtful accessibility, images can inadvertently exclude part of your audience from receiving the same message.

#### Alt text

Alternative text (alt text) is a short description of the content or function of an image that screen readers and other assistive technologies provide to users. Write descriptive alt text for every meaningful image so users who can’t see the visuals still understand your message or call to action. Refer to the section adding alt text for more.

For purely [decorative](https://www.w3.org/WAI/tutorials/images/decorative/) images (ones that don’t add information or context), use an empty alt attribute (`alt=""`). 

##### Tips for writing alt text

###### 1. Describe what's actually in the image

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

###### 2. Keep it short, yet specific

Concise alt text makes it easier for users to process. Include enough detail to convey purpose but skip any fluff.

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

###### 3. Avoid “image of” or “picture of” 

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

###### 4. Reflect text that appears in the image

If an image includes essential text, put that info in the alt text so users don’t miss it.

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

###### 5. Stick to relevant context—no extra marketing jargon

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

###### 6. Consider the image's purpose

If an image is functioning like a link or call-to-action, describe the intended action (“Shop,” “Sign up,” Learn"), not just the label or product shown.

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
      <td>"Get your free eBook"</td>
      <td>"Free eBook"</td>
    </tr>
    <tr>
      <td>"Sign up for the mailing list"</td>
      <td>"Mailing list"</td>
    </tr>
  </tbody>
</table>

##### Adding alt text in Braze

If you’re using a custom HTML or code-based editor, you’ll want to manually include the alt attribute in each `<img>` tag. For example:

{% raw %}

```html
<img src="product.jpg" alt="Red shoes on display">
```

{% endraw %}

If you're using a Braze drag-and-drop editor, you’ll find the **Alt text** field in a slightly different location depending on the editor. Here’s a quick breakdown.

{% tabs local %}
{% tab Email %}
Select the image in your email to show the **Image Properties** panel. The **Alt text** field is near the **URL** field.
{% endtab %}
{% tab In-app message %}
Select the image in your in-app message to show the **Actions** panel. **Alt text** is the first field in the panel.
{% endtab %}
{% tab Banner Card %}
Select the image in your Banner Card to show the **Actions** panel. **Alt text** is the first field in the panel.
{% endtab %}
{% tab Content Card %}
Currently, the Content Card editor doesn’t provide a way to add alt text directly. If you need alt text for your images, you can use **key-value pairs as a workaround (LINK NEEDED)** or explore other Braze channel options that do support alt text. This can help your messages remain inclusive for screen reader users and others who rely on accessibility features.
{% endtab %}
{% tab Landing page %}
Select the image in your landing page to show the **Actions** panel. **Alt text** is the first field in the panel.
{% endtab %}
{% endtabs %}

{% alert note %}
Current drag-and-drop editors are missing the option to mark an image as decorative. If you leave alt text blank, screen readers will announce the file name instead. For email and in-app messages, you can switch to the HTML or custom code editors and add `alt=""` to image tags to indicate the image is decorative and should be skipped.
{% endalert %}

Some messaging channels—like rich push, LINE, WhatsApp, and MMS— don’t allow Braze to include custom alt text. Typically, these channels provide only minimal metadata, so a screen reader may say something like “attachment” (for example, iOS VoiceOver does this for rich push images). If you need fully customized alt text, consider using channels that support it, or ensure any essential information is also included in text so everyone can access your message content.

#### Images of text

Whenever possible, avoid placing text inside images—screen readers can’t read image-based text, and users can’t easily adjust font size or color for better visibility. Consider these tips:

- **Remove text where you can:** Move any descriptive or promotional text from the image onto a text layer in your message instead. This way, users can resize or recolor it as needed using their device or browser preferences.
- **Test for readability and contrast:** If you must keep text in the image, follow color contrast best practices and use a large enough font. Test to confirm it’s still legible on smaller screens.
- **Provide alt text:** For essential text that must remain in the image, include [alt text](#alt-text) describing the words.

When images contain text that can’t be edited, users with visual impairments lose the flexibility to make reading adjustments. By separating text from images, you help more users read and interact with your message comfortably.

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


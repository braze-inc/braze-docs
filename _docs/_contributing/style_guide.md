---
nav_title: Style guides
article_title: Braze Docs Style Guide
description: "The Braze Docs Style Guide."
page_order: 7
noindex: true
---

# Braze Docs Style Guide

Refer to the following sections when contributing to Braze Docs.

## Writing style guide

### General guidelines {#general-guidelines}

#### Voice and Tone {#voice-and-tone}

The Braze brand voice is smart, conversational, and direct. We are a human voice in a world of tech buzzwords; we provide clarity and guidance to anyone interested in the craft of customer engagement; and we eschew jargon in favor of concise language that is as easy to understand as it is powerful.

To align on this brand voice in our writing and editing, we use three voice guidelines: **straightforward, empowering,** and **human**.

##### Straightforward

Clearly structure your writing and make it easy for people to find the information they need. 

* Explain complicated things simply.   
* Be concise.   
* Use consistent language for features and actions. 

###### Guidelines

✅ Use visuals to help clarify complex subjects. <br> 
**Example:** The user profile lifecycle image in the [User Profile Lifecycle article]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/#user-aliases) helps to illustrate a tricky concept.

✅ Create a clear information hierarchy. <br>
**Example:** "This is an overview for how content is managed on Braze Docs. To learn more about a specific topic, choose the dedicated topic page in the navigation."

✅ Ruthlessly cut jargon and acronyms if possible. If not possible, define them.  <br> 
**Example:** "The Short Messaging Service (SMS) is used to send and receive brief text messages."

##### Empowering

What problem are you trying to solve with your writing? Keep that problem in mind while creating any content.

* Explain the “why” and “how” to give users the confidence to take action.   
* Be specific when explaining benefits, and be clear about what is and isn’t possible.   
* Offer practical advice and sincere encouragement. 

###### Guidelines

✅ Make it easy to find the happy path. <br>
**Example:** "When you stop a Canvas, the following applies: 1. Users are prevented from entering the Canvas. 2. No further messages are sent, despite where a user is in the flow.  3. **Exception:** Email Canvases don't immediately stop." 

✅ Provide examples, use cases, and templates that simplify or elevate the user’s work. <br>
**Example:** "`IInAppMessageManagerListener` also includes delegate methods for clicks on the message itself or one of the buttons. A common use case would be intercepting a message when a button or message is clicked for further processing."

##### Human

Informational writing is inherently dry—we want readers to focus on the content, not the delivery. We can still write in a way that helps our readers process the information they’re consuming and make it more likely that they internalize the knowledge. Be human, let your personality show, and be memorable. 

* Aim for a conversational tone rather than a formal one.   
* Focus on the user; respect their situation and emotional state.   
* Actively center the human experience, not the machine state. 

###### Guidelines

✅ Thoughtfully apply brand tone and assets.  <br>
**Example:** "Integrating with Braze is a worthwhile process. But you’re smart. You’re here. Clearly, you already know that."

✅ Apply [accessibility best practices](#accessibility) for both visual and verbal content.  <br>
**Example:** Replacing idioms like "out-of-the-box" with "default" make your text more accessible to English second language speakers.

✅ Provide consistent support across the user journey. <br>
**Example:** Use the Diátaxis framework to ensure you’re meeting the needs of different users at different times.

#### Accessibility {#accessibility}

Braze aims to provide an inclusive experience. Use the following guidelines to ensure your learning content is accessible to the [1 billion people](https://www.who.int/en/news-room/fact-sheets/detail/disability-and-health) with an accessibility need.

##### General

* Avoid biased or ableist language. For more information, see the section on [Inclusive Language](#inclusive-language).  
* Use a [screen reader](https://support.apple.com/guide/mac-help/use-accessibility-features-mh35884/mac) to test your content.  
* Don’t use an [ampersand](#ampersands) (&) in place of “and” unless referencing UI elements that use an ampersand. 

##### Language and Formatting

* Use [plain language](https://www.plainlanguage.gov/guidelines/).  
* Front-load sections with the most important information. Use the journalism model of the [inverted pyramid](https://en.wikipedia.org/wiki/Inverted_pyramid_(journalism)).  
* Break up walls of text to help readers scan for information. Use paragraphs, [lists](#lists), [callouts](#heading=h.np3pri4d370t), and [images](#figures-and-other-images) to improve readability.  
* [Write short sentences and paragraphs](https://www.usability.gov/how-to-and-tools/methods/writing-for-the-web.html). As a general rule, aim for no more than 20 words per sentence, five sentences per paragraph.  
* Avoid using Latin acronyms and phrases, as they can be hard to translate. Instead, use simple words or phrases.

##### Headings

* Use unique, descriptive, and clear [headings and titles](#headings-and-titles).  
* Use an h1 for page titles.  
* Don’t skip heading levels. An h3 should follow an h2, and so on. 

##### Links

* Don’t use link text like “Learn more”, “here”, or “this document”. For more phrases to avoid, refer to the section [Writing Links](#writing-links).  
* Avoid placing two links back to back in a sentence. Put a character or word in between to separate them.  
* [Links to download files](#links-for-file-download) should indicate clicking the link downloads the file, as well as the file type (PDF, CSV, and so on)  
* If it isn’t clear from the context, links to sections in the same document should use a [standard phrase](#structuring-links) indicating this action.

##### Images, Videos, and GIFs

* Provide [alt text](#alt-text) for every image that summarizes the information presented in the image.  
* Don’t use images as the only way to show information. Always provide the steps, content, or other details presented in the image in the surrounding text.  
* Don’t use images of terminal output, code samples, or text. Instead, use actual text.   
* Provide captions for video content.  
* Don’t use flashing elements in videos or GIFs.

##### Tables {#tables-1}

* Always use an introductory sentence to describe the purpose of the table.   
* Avoid tables in the middle of a list, especially a list of steps.

#### Global Audience {#global-audience}

We write our learning content in American English. However, Braze is a global brand, and as such, we write for a global audience. Use the following guidelines to make sure customers understand your writing even when English isn’t their first language.

1. **Write with localization in mind:**  
  * Format [dates and times](#dates-and-times) in unambiguous ways.  
  * Don’t put text overlays on images, as this text can’t be translated.  
  * Avoid [slang and idioms](#slang-and-idioms).  
  * Provide context. Don’t assume the reader knows what you’re talking about.  
2. **Write short and precise sentences:**  
  * Use [plain language](https://www.plainlanguage.gov/guidelines/).  
  * Define [abbreviations](#abbreviations).  
  * Avoid [ambiguous pronouns](#ambiguous-pronouns). If a pronoun may be ambiguous, then replace it with the appropriate noun.  
3. **Be consistent:**  
  * Use the same term for a concept across all mentions of the term, including the same capitalization and text formatting.  
  * Write sentences in subject + verb + object order.  
  * If instructions depend on a condition being met, put the conditional clause first. For more information, see [clause order](#clause-order).   
4. **Be inclusive:**  
  * Use [inclusive language](#inclusive-language).  
  * Use diverse [example names](#heading=h.o9yy4y0bxgg).  
  * Avoid culturally specific humor.

#### Inclusive Language {#inclusive-language}

We may be a B2B company, but people are at the center of what we do, and ours is a global brand. Whenever we refer to a person in our content, we are mindful of being inclusive and considerate. When in doubt, consult this section or [The Diversity Style Guide](https://www.diversitystyleguide.com/).

##### Age

Unless it’s relevant to your writing, don’t refer to a subject’s age. Don’t use qualifiers like “young” or “old” to describe any subject or audience. 

If you’re representing an age group, be descriptive and specific like “Generation Z” instead of “youth.” Don’t use vague descriptors like “college-age” when you could say “college students” instead.

##### Color

Avoid including color terms in your writing unless absolutely necessary, and if necessary, include explanatory text. 

{::nomarkdown}
<table style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Do</th><th style="width: 50%;">Don't</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Press ✅ Save.</td><td style="width: 50%;">Press the green Save icon.</td></tr>
<tr><td style="width: 50%;">Press the green checkmark icon.</td><td style="width: 50%;">Press the green icon next to the red Cancel button.</td></tr>
<tr><td style="width: 50%;">Press the green icon.</td><td style="width: 50%;"></td></tr>
</tbody>
</table>
{:/}

Don’t rely on color to be the only indicator for interactive elements. For example, underline links on hover, or mark a required field with an asterisk.

Avoid relying solely on green and red for “good” and “bad” (or, more often, “do” and “don’t”) indicators. Red/green color blindness is the most common type of color blindness. If you use color to communicate do’s and don’ts, make sure to also include other text or symbols to convey the same point.

##### Condescending Language {#condescending-language}

When writing instructions or detailing steps for a reader to follow, avoid using words or phrases such as:

* simple, like “Creating a campaign is simple.”  
* simply, like “...simply add X into Y”  
* just, like “...just install X”  
* “It’s easy”

If someone has difficulty with the steps or instructions, your casual descriptors can feel condescending. You may also unintentionally exclude people from your documentation who interpret that as an indicator they are in some way not skilled enough to follow your instructions.

##### Customers vs. Clients

When referring to Braze users and their consumers, use the following terms accordingly:

* **Customers:** Brands we work with. Never refer to our customers as “clients”.  
 * **Braze users:** In the context of documentation, when it is important to distinguish between users of the platform and the end users who receive marketing messages, use "Braze users".  
* **Consumers:** Customers of a brand we work with.   
* **Users:** Generally reserved for a specific statistic that depends on “user” metrics (such as “user retention”). When referring to “users” in our content, first aim to be more specific. Think shoppers, consumers, patients, players.

##### Departments and Teams

Capitalize the names of departments or teams. Do not capitalize “team” or “department.”

{::nomarkdown}
<table style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Do</th><th style="width: 50%;">Don't</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Marketing, Business Intelligence Product team</td><td style="width: 50%;">marketing, business intelligence Product Team</td></tr>
<tr><td style="width: 50%;">Revenue department</td><td style="width: 50%;">Revenue Department</td></tr>
</tbody>
</table>
{:/}

##### Disability

Don’t refer to a person’s disability unless it’s specifically relevant to your writing. In that case, be considerate and ask whether the subject prefers identity-first or person-first language. When referring to a subject with a disability, do not use terms like “handicapped.”

Ableist language includes words or phrases such as “crazy”, “insane”, “blind to” or “blind eye to”, “cripple”, “dumb”, and others. Choose alternative words depending on the context.

##### Disease

When describing an illness, avoid words like “suffer,” “struggle,” or “victim.” Aim to be neutral and matter-of-fact. 

{::nomarkdown}
<table style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 100%;">Do</th></tr>
</thead>
<tbody>
<tr><td style="width: 100%;">She was diagnosed with cancer.</td></tr>
<tr><td style="width: 100%;">They’re living with HIV.</td></tr>
<tr><td style="width: 100%;">He recovered from his stroke.</td></tr>
</tbody>
</table>
{:/}


##### Inclusivity in Content

Highlight and represent a diverse community. Be mindful and inclusive when involving our customers, speakers, industry experts, and Braze team members. 

##### Job Titles

When it comes to job titles, we veer off-course from AP Style. In all cases, we capitalize job titles when referring to someone specifically. 

###### Job Title with Company Name

Capitalize formal job titles when they come before or after a person’s name. We format them three ways:

1. **[Formal Title]** at **[Company Name]** + **[Full Name]**

{::nomarkdown}
<table style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Do</th><th style="width: 50%;">Don't</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Creative Director at PantsLabyrinth David Bowie</td><td style="width: 50%;">creative director at PantsLabyrinth David Bowie</td></tr>
</tbody>
</table>
{:/}

{: start="2"}
2. **[Full Name]** + comma + **[Formal Title]** at **[Company Name]** 

{::nomarkdown}
<table style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Do</th><th style="width: 50%;">Don't</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">David Bowie, Creative Director at PantsLabyrinth</td><td style="width: 50%;">David Bowie, creative director at PantsLabyrinth</td></tr>
</tbody>
</table>
{:/}

{: start="3"}
3. **[Company Name]** + **[Formal Title]** + **[Full Name]** 

{::nomarkdown}
<table style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Do</th><th style="width: 50%;">Don't</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">PantsLabyrinth Creative Director David Bowie</td><td style="width: 50%;">PantsLabyrinth creative director David Bowie</td></tr>
</tbody>
</table>
{:/}

###### Job Title without Company Name

When referring to a specific person by formal title, capitalize their formal title and name like so:

1. **[Formal Title]** + **[Full Name]**

{::nomarkdown}
<table style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Do</th><th style="width: 50%;">Don't</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">CEO Robin Fenty</td><td style="width: 50%;">Chief executive officer Robyn Fenty</td></tr>
</tbody>
</table>
{:/}

{: start="2"}
2. **[Formal Title]** + comma + **[Full Name]**

{::nomarkdown}
<table style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Do</th><th style="width: 50%;">Don't</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">SVP, Product, Robin Fenty</td><td style="width: 50%;">senior vice president, product, Robyn Fenty</td></tr>
</tbody>
</table>
{:/}

###### Other

Formal titles are “at [COMPANY].” Founders and Cofounders are “of [COMPANY].” Formal titles and occupations on their own do not need to be capitalized.

{::nomarkdown}
<table style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Do</th><th style="width: 50%;">Don't</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">I wrote to their chief data officer.</td><td style="width: 50%;">I wrote to their Chief Data Officer</td></tr>
<tr><td style="width: 50%;">We spoke with several business intelligence analysts.</td><td style="width: 50%;">We spoke with several Business Intelligence Analysts.</td></tr>
<tr><td style="width: 50%;">Contact your Braze account manager.</td><td style="width: 50%;">I wrote to their Chief Data Officer Contact your Braze Account Manager.</td></tr>
</tbody>
</table>
{:/}

Adhere to gender-neutral job titles unless gender has been already established.

{::nomarkdown}
<table style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Do</th><th style="width: 50%;">Don't</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">salesperson</td><td style="width: 50%;">salesman/saleswoman</td></tr>
</tbody>
</table>
{:/}

Abbreviate titles where appropriate, such as VP or SVP, if this is how the person refers to their title. In the event of limited text space, standard abbreviations (VP, SVP, Sr., or Jr.) are acceptable. 

##### Gender

Don’t make assumptions about people’s gender. Ask subjects who appear in your content how they self-identify. 

When referring to members of the community, “queer” is acceptable. “Gay” is not. You may refer to a group of people as “LGBTQ.” Do not use this for describing an individual.

When addressing groups of people in your content, avoid gendering your audience (example: “OK, ladies!”). Use gender-neutral expressions instead (example: “Let’s dig in, everyone!”). 

“They/them/theirs” is always acceptable to use as a single or plural pronoun in all of our content.

##### Mental Health

Mental health and illness cover a broad range of conditions. Unless it’s relevant to what you are writing, don’t refer to a person’s mental health. Avoid stigmatizing words and phrases. Don’t use medical terms colloquially (example: “The depressing state of things...”).

##### Names

The first time you mention a person, use their first and full name. From there on, use either their first or last name when referring to them.

##### Pronouns

For information on appropriate use of pronouns, refer to the Language and Grammar section on [Pronouns](#pronouns).

##### Race, Religion, and Ethnicity

Don’t refer to a person’s race, religion, or ethnicity unless it’s relevant to what you are writing. In writing where race or ethnicity factors in, ask your subject how they self-identify.

Don’t use a hyphen to indicate dual heritage or religion. Instead, use a space.

{::nomarkdown}
<table style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Do</th><th style="width: 50%;">Don't</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Muslim American</td><td style="width: 50%;">Muslim-American</td></tr>
<tr><td style="width: 50%;">Cuban American</td><td style="width: 50%;">Cuban-american</td></tr>
</tbody>
</table>
{:/}

Capitalize the proper names of ethnicities, nationalities, peoples, and tribes.

{::nomarkdown}
<table style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Do</th><th style="width: 50%;">Don't</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Cambodian</td><td style="width: 50%;">cambodian</td></tr>
<tr><td style="width: 50%;">Black Americans</td><td style="width: 50%;">black Americans</td></tr>
</tbody>
</table>
{:/}

Capitalize the names of religions or religious terms.

{::nomarkdown}
<table style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Do</th><th style="width: 50%;">Don't</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Bahá’í Faith</td><td style="width: 50%;">bahá’í faith</td></tr>
<tr><td style="width: 50%;">Buddhist</td><td style="width: 50%;">buddhist</td></tr>
</tbody>
</table>
{:/}

Don’t co-opt words or turns of phrase that belong to African American Vernacular English (on fleek, bae, lit, woke). 

Don’t co-opt words or turns of phrase specific to indigenous peoples (example: spirit animal, powwow). 

#### Third-Party Sources {#third-party-sources}

Never copy content from other sites, as it may violate copyright. Content can be both text and images.

Instead of copying or quoting third-party sites, paraphrase the content or provide a link to the third-party site for more information.  For more information, refer to [Links to Other Sites](#links-to-other-sites).

### Language and grammar {#language-and-grammar}

Keeping in line with agreed-upon grammar and mechanics helps us keep our writing clear and consistent. This section covers what we try to follow in our technical documentation unless specified otherwise.

#### Abbreviations {#abbreviations}

Abbreviations, such as acronyms, initialisms, and shortened words, can hurt our clarity, voice, and SEO. 

Although some abbreviations are widely understood, others aren't well known or are familiar only to a specific group of customers. Use your best judgment, and as a general rule, it’s OK not to spell out an abbreviation if it’s listed in the [American Heritage Dictionary](https://ahdictionary.com/).

If an abbreviation isn’t well known, spell it out on the first mention, followed by the abbreviation in parentheses. For all subsequent mentions of the term, use the abbreviation.

{::nomarkdown}
<table style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Do</th><th style="width: 50%;">Don't</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Do <br><br> <em>Spell out uncommon abbreviations at the first mention</em></td><td style="width: 50%;">Don’t <br><br> <em>Spell out common abbreviations</em></td></tr>
<tr><td style="width: 50%;">Top-level domain (TLD)</td><td style="width: 50%;">Portable Document Format (PDF)</td></tr>
<tr><td style="width: 50%;">Universally unique identifier (UUID)</td><td style="width: 50%;">Universal Serial Bus (USB)</td></tr>
</tbody>
</table>
{:/}


Treat abbreviations as regular words when making them plural, and don't add an apostrophe—for example, APIs and SDKs. The same goes for which article (a or an) you use—look at how you pronounce the abbreviation. When an abbreviation begins with a vowel sound, use “an”; for consonant sounds, use “a”. 

{::nomarkdown}
<table style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 100%;">Do</th></tr>
</thead>
<tbody>
<tr><td style="width: 100%;">Do <br><br> <em>Use articles depending on how the abbreviation is pronounced, not spelled</em></td></tr>
<tr><td style="width: 100%;">an ISP</td></tr>
<tr><td style="width: 100%;">a DLL</td></tr>
<tr><td style="width: 100%;">an HTML site</td></tr>
<tr><td style="width: 100%;">a CSV file</td></tr>
</tbody>
</table>
{:/}

#### Active Voice {#active-voice}

We use the active voice at Braze when possible. Active voice is our gold standard. Avoid passive voice, in which it can be difficult to determine who or what is performing a particular action.

To see if your sentence is in a passive voice, insert “by somebody” after the verb. If the sentence makes sense—it’s most likely in the passive voice.

{::nomarkdown}
<table style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Do</th><th style="width: 50%;">Don't</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Do <br><br> <em>Use active voice</em></td><td style="width: 50%;">Don’t <br><br> <em>Use passive voice, if possible</em></td></tr>
<tr><td style="width: 50%;">Braze connects consumers to the brands they love.</td><td style="width: 50%;">Consumers are connected to the brands they love.</td></tr>
<tr><td style="width: 50%;">Braze requires employees to keep their addresses up to date.</td><td style="width: 50%;">Employees are required to keep their addresses up to date.</td></tr>
<tr><td style="width: 50%;">Company administrators can configure authentication requirements for signing into Braze.</td><td style="width: 50%;">Authentication requirements for signing into Braze can be configured by company administrators.</td></tr>
</tbody>
</table>
{:/}

##### Exceptions

It’s OK to use passive voice in the following cases:

* To de-emphasize a subject, generally to avoid blaming the reader:  
 * **Do:** Two errors were found in the email.  
 * **Don’t:** You created two errors in the email.  
* If knowing who is responsible for the action isn’t important:  
 * **Do:** This article was last updated in December 2020.

#### Articles {#articles}

Use the articles “a”, “an”, and “the” to make your writing clear and to aid in translation. Use “the” before a specific singular or plural noun, and “a” or “an” before a non-specific singular noun.

To determine if you should use “a” or “an”, look at the pronunciation of the word that follows it. Use “a” before a consonant sound, and use “an” before a vowel sound. The same guidelines apply to [Abbreviations](#abbreviations).

{::nomarkdown}
<table style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 100%;">Do</th></tr>
</thead>
<tbody>
<tr><td style="width: 100%;">Do <br><br> <em>Use articles depending on how the anteceding word is pronounced.</em></td></tr>
<tr><td style="width: 100%;">an hour</td></tr>
<tr><td style="width: 100%;">a minute</td></tr>
<tr><td style="width: 100%;">an FAQ article</td></tr>
<tr><td style="width: 100%;">a LAB course</td></tr>
</tbody>
</table>
{:/}

#### Pronouns {#pronouns}

##### Personal Pronouns

Use second-person pronouns (you) whenever possible. 

Don’t refer to Braze customers as the “user” in external-facing writing, instead speak directly to the reader using “you”. To refer to our customers’ customers, use “your consumers” or, if the situation relates to user statistics, “your users”.

Avoid first-person pronouns (I, we, us, our) except in the following cases:

* Entries in FAQs. For example, “How do I reset my password?”.  
* Using “we” to refer to Braze as an organization.   
 * If it may be unclear who “we” is referring to, first refer to Braze by name, then use “we” in subsequent mentions.

##### Gender-Neutral Pronouns

Use the pronouns your subjects use. If there is any uncertainty, use “they,” “them,” and “their” for singular pronouns. Don’t use “he/she” or “(s)he” as an alternative to the singular “they”.  

Only use gendered pronouns (he/she, him/her, his/hers) if the person you’re referring to is actually that gender.  

##### Ambiguous Pronouns {#ambiguous-pronouns}

Pronouns substitute for nouns. The word a pronoun refers to is called its antecedent. When writing instructions or learning material, be sure to make clear references between a pronoun and its antecedent. This may require repeating subjects to make the meaning clear.

{::nomarkdown}
<table style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Do</th><th style="width: 50%;">Don't</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Do <br><br> <em>Ensure a pronoun clearly references its antecedent</em></td><td style="width: 50%;">Don’t <br><br> <em>Use ambiguous pronoun references</em></td></tr>
<tr><td style="width: 50%;">If you type text in the field, the text doesn’t change.</td><td style="width: 50%;">If you type text in the field, it doesn't change.</td></tr>
<tr><td style="width: 50%;">She told Sarah that Sarah’s answer was incorrect.</td><td style="width: 50%;">She told Sarah that her answer was incorrect.</td></tr>
<tr><td style="width: 50%;">You can’t edit an archived campaign. Unarchive a campaign to edit it.</td><td style="width: 50%;">You can't edit an archived campaign. Unarchive it to edit it.</td></tr>
</tbody>
</table>
{:/}

##### Optional Pronouns

To add additional clarity to your writing and to aid in localization, use pronouns such as “that”, “which”, and “who”.

{::nomarkdown}
<table style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Do</th><th style="width: 50%;">Don't</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Do <br><br> <em>Use "that", "which", and "who" to add additional clarity.</em></td><td style="width: 50%;">Don’t</td></tr>
<tr><td style="width: 50%;">Right-click the link that you want to open.</td><td style="width: 50%;">Right-click the link you want to open.</td></tr>
<tr><td style="width: 50%;">From here, you can choose which Tinyclues cohort that you want to include.</td><td style="width: 50%;">From here, you can choose a Tinyclues cohort you want to include.</td></tr>
</tbody>
</table>
{:/}

#### Capitalization {#capitalization}

Avoid unnecessary capitalization. In most instances, use sentence case. Title case should only be used for proper nouns or feature names (unless otherwise specified, see [Glossary](https://confluence.braze.com/pages/viewpage.action?spaceKey=MAR&title=Braze+Glossary)).

{::nomarkdown}
<table style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Do</th><th style="width: 50%;">Don't</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Do <br><br> <em>Use lowercase for writing out website URLs and email addresses</em></td><td style="width: 50%;">Don’t</td></tr>
<tr><td style="width: 50%;">www.braze.com/docs</td><td style="width: 50%;">www.Braze.com/docs</td></tr>
<tr><td style="width: 50%;">sample@email.com</td><td style="width: 50%;">SAMPLE@EMAIL.COM</td></tr>
</tbody>
</table>
{:/}

{::nomarkdown}
<table style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Do</th><th style="width: 50%;">Don't</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Do <br><br> <em>Use lowercase directionals</em></td><td style="width: 50%;">Don’t</td></tr>
<tr><td style="width: 50%;">north, south, east, west</td><td style="width: 50%;">North, South, East, West</td></tr>
</tbody>
</table>
{:/}

{::nomarkdown}
<table style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Do</th><th style="width: 50%;">Don't</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Do <br><br> <em>Capitalize specific regions, and use all capitals for abbreviated regions</em></td><td style="width: 50%;">Don’t</td></tr>
<tr><td style="width: 50%;">the Northwest</td><td style="width: 50%;">the northwest</td></tr>
<tr><td style="width: 50%;">Southern Connecticut</td><td style="width: 50%;">southern Connecticut</td></tr>
<tr><td style="width: 50%;">Eastern Europe</td><td style="width: 50%;">eastern Europe</td></tr>
<tr><td style="width: 50%;">APAC, EMEA</td><td style="width: 50%;">Apac, emea</td></tr>
</tbody>
</table>
{:/}

##### Brands and Products

When referring to a brand or product, use the capitalization the brand uses. In most cases, capitalize the names of brands (Grindr, Walmart) and products (Benchmarks, Looker Blocks). It’s fine to begin a sentence with lowercase if the first word is the stylized name of a brand like eBay or iTunes. 

For intercaps, always refer to the usage preferred by the brand in print (OkCupid, YouTube). Do not use intercaps that only appear in logos or graphic design treatments (Amazon). 

#### Clause Order {#clause-order}

If you want to tell the reader to do something in a specific circumstance, try to mention the circumstance before you provide the instruction. This lets the reader skip the instruction if the circumstance doesn't apply.

{::nomarkdown}
<table style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Do</th><th style="width: 50%;">Don't</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">For troubleshooting steps, see Campaign FAQs.</td><td style="width: 50%;">See Campaign FAQs for troubleshooting steps.</td></tr>
<tr><td style="width: 50%;">To archive your campaign, click the gear icon and select Archive.</td><td style="width: 50%;">Click the gear icon and select Archive to archive your campaign.</td></tr>
</tbody>
</table>
{:/}

#### Combining Forms {#combining-forms}

[Hyphenate](#hyphens) combined forms when the phrase is used as an adjective before the noun. 

**Example:** A one-of-a-kind item

#### Contractions {#contractions}

A contraction is a shortened version of a word or phrase. Use contractions to keep an approachable and informal tone. However, do not use noun and verb contractions or double contractions, or a combination of two contractions. These can disrupt the flow and coherency of the sentence.

{::nomarkdown}
<table style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Do</th><th style="width: 50%;">Don't</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Do <br><br> <em>Use contractions</em></td><td style="width: 50%;">Don’t <br><br> <em>Use noun and verb contractions</em></td></tr>
<tr><td style="width: 50%;">If you’re an admin, you can manage your company’s contact information.</td><td style="width: 50%;">Braze’ll now support Shoptify integration.</td></tr>
<tr><td style="width: 50%;">You can’t edit an archived campaign. Do Use contractions.</td><td style="width: 50%;">You mightn’t’ve seen the restricted upload size.</td></tr>
</tbody>
</table>
{:/}

#### Dangling and Misplaced Modifiers {#dangling-and-misplaced-modifiers}

Modifiers are words of phrases that modify other words or phrases. A dangling modifier doesn’t modify any subject in the sentence. A misplaced modifier is placed far away from the subject that it’s meant to modify. Essentially, dangling and misplaced modifiers may cause confusion by connecting to the wrong part of the sentence.

Writing with an active voice helps prevent the use of dangling and misplaced modifiers. Be sure to use a modifier that clearly modifies. 

{::nomarkdown}
<table style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Do</th><th style="width: 50%;">Don't</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Do <br><br> <em>Keep sentence short and concise. Use active voice.</em></td><td style="width: 50%;">Don’t <br><br> <em>Use lengthy sentences with modifiers that can cause confusion</em></td></tr>
<tr><td style="width: 50%;">Customers must set up their SAML settings.</td><td style="width: 50%;">You may have test messages on your campaigns that can be deleted.</td></tr>
<tr><td style="width: 50%;">Make sure to save your campaign drafts.</td><td style="width: 50%;">On the way home, Sarah found a gold man’s stopwatch.</td></tr>
</tbody>
</table>
{:/}

#### Prepositions {#prepositions}

There’s nothing wrong with ending a sentence in a preposition when it improves readability. Place a preposition or prepositional phrase where it makes the most sense in a sentence. If you’re having difficulty, read the sentence out loud and see if it sounds natural.

{::nomarkdown}
<table style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Do</th><th style="width: 50%;">Don't</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Each option corresponds to the priority the notification appears in.</td><td style="width: 50%;">Each option corresponds to the priority in which the notification appears.</td></tr>
<tr><td style="width: 50%;">For details, see the SDK documentation for the platform you’re working with.</td><td style="width: 50%;">For details, see the SDK documentation for the platform with which you’re working.</td></tr>
</tbody>
</table>
{:/}

#### Present Tense {#present-tense}

Use present tense instead of future tense. Present tense conveys immediacy and demonstrates confidence. Avoid using “will” or hypothetical “would”, especially when referring to the result of user action.

{::nomarkdown}
<table style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Do</th><th style="width: 50%;">Don't</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Archived subscription groups cannot be edited and no longer appear in segment filters.</td><td style="width: 50%;">Archived subscription groups cannot be edited and no longer appear in segment filters.</td></tr>
<tr><td style="width: 50%;">Using a short code is the most reliable number type for including links.</td><td style="width: 50%;">Using a short code would be the most reliable number type for including links.</td></tr>
</tbody>
</table>
{:/}

Only use future tense when you’re actually talking about the future. Avoid predicting [future features](#describing-limitations). 

#### Profanity {#profanity}

Keep it PG. This has less to do with morality than the fact profanity can be divisive and off-putting to an audience as broad and international as ours. There’s also a case to be made that sometimes profanity is a cover-up for half-baked writing. That’s simply not our vibe. 

#### Plurals in Parentheses {#plurals-in-parentheses}

Do not use plurals in parentheses. Instead, use the plural or singular form of the word.

{::nomarkdown}
<table style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Do</th><th style="width: 50%;">Don't</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Customize your campaign with the following filters.</td><td style="width: 50%;">Customize your campaign with the following filter(s).</td></tr>
</tbody>
</table>
{:/}

#### Second Person and First Person {#second-person-and-first-person}

Use second person in your instructions instead of first person—”you” rather than “we”. 

Refer to the reader as the one doing the action. Strike a conversational tone—most readers are coming to documentation when they don’t have immediate access to a support agent. Make it feel as if the article is talking to them instead. 

{::nomarkdown}
<table style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Do</th><th style="width: 50%;">Don't</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">If you want to add a variant...</td><td style="width: 50%;">If we want to add a variant...</td></tr>
</tbody>
</table>
{:/}

If you’re telling the reader to do something, then you can omit the “you” and use the imperative.

{::nomarkdown}
<table style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Do</th><th style="width: 50%;">Don't</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Upload the CSV file.</td><td style="width: 50%;">You can upload the CSV file.</td></tr>
<tr><td style="width: 50%;">Click Submit.</td><td style="width: 50%;">You’ll need to click Submit.</td></tr>
</tbody>
</table>
{:/}

When using second person, make sure you know who the audience of the document is, and to be consistent about who you’re talking to.

#### Slang and Idioms {#slang-and-idioms}

We’re a plainspoken bunch. Avoid using trendy slang or idioms that speak too specifically to a singular audience. It can also quickly date materials, and make it difficult to localize content. 

#### Spelling {#spelling}

Use American English spelling for words that differ in British English. If you’re not sure how to spell a word, first refer to the [Glossary](#glossary). If the word isn’t listed there, then refer to [Merriam-Webster’s Collegiate Dictionary](https://www.merriam-webster.com/).

For words that are accented or contain special characters, make sure to correctly follow the dictionary spelling. In some cases, unintentionally omitting these accents can result in a different word. For example, “resume” means to begin again after stopping, whereas “résumé” is an account of one’s qualifications. 

### Punctuation {#punctuation}

#### Ampersands {#ampersands}

Don’t use an ampersand (&) in place of “and” in text or headings unless you are referring directly to the user interface.

{::nomarkdown}
<table style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Do</th><th style="width: 50%;">Don't</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Drag-And-Drop Editor</td><td style="width: 50%;">Drag & Drop Editor</td></tr>
<tr><td style="width: 50%;">SMS and MMS</td><td style="width: 50%;">SMS & MMS</td></tr>
</tbody>
</table>
{:/}

#### Apostrophes {#apostrophes}

We use an apostrophe most often to make a noun possessive. 

* For singular nouns that end in S, it’s fine to place another S after the apostrophe.  
 * **Example:** Chris’s, business’s, alias’s  
* For plural nouns that end in S, add an apostrophe but no additional S.  
 * **Example:** users’

#### Colons {#colons}

Use colons at the end of an introductory phrase that precedes a list or example. Your introductory sentence should be able to stand alone as a complete sentence. This is for both accessibility and localization purposes, as it’s difficult to translate sentence fragments.

{::nomarkdown}
<table style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Do</th><th style="width: 50%;">Don't</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">The general structure is as follows:</td><td style="width: 50%;">The general structure is:</td></tr>
</tbody>
</table>
{:/}

If the text preceding the colon is bold, bold the colon as well.

{::nomarkdown}
<table style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Do</th><th style="width: 50%;">Don't</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;"><strong>Scheduled:</strong> Time-based entry.</td><td style="width: 50%;"><strong>Scheduled</strong>: Time-based entry.</td></tr>
</tbody>
</table>
{:/}

If the text preceding the colon is code text, don’t include the colon in the code text unless it is part of the code element.

{::nomarkdown}
<table style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Do</th><th style="width: 50%;">Don't</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;"><code>user<em>alias</em>label</code>: A common label to group user aliases with.</td><td style="width: 50%;"><code>user<em>alias</em>label:</code> A common label to group user aliases with.</td></tr>
</tbody>
</table>
{:/}

You can also use a colon to join two related phrases in a sentence. However, use colons for this sparingly. Two sentences are generally more readable. 

{::nomarkdown}
<table style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 100%;">Do</th></tr>
</thead>
<tbody>
<tr><td style="width: 100%;">Coming up next week: we're going on a tour of the West Village.</td></tr>
</tbody>
</table>
{:/}


#### Commas {#commas}

Braze uses the Oxford (serial) comma when writing instructions or learning content. Use a comma before the last conjunction to separate items in a series.

Use a comma after an introductory phrase.

If a coordinating conjunction (words like “and”, “but”, “or”, “yet”, “so”) separates two independent clauses, place the comma after the first clause and before the conjunction. However, this comma is not necessary if both clauses are short.

For example, here are two independent clauses:

* “All fields are optional.”  
* “You must specify at least one field.”

The sentence when using a coordinating conjunction “but” is “All fields are optional, but you must specify at least one field.”

If an independent clause and a dependent clause are used in the same sentence, do not use a comma to separate them. Only use a comma in this scenario if the sentence can be misinterpreted without the comma placement.

{::nomarkdown}
<table style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Do</th><th style="width: 50%;">Don't</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Push subscriptions states are filters and can allow users to edit notification preferences.</td><td style="width: 50%;">Push subscriptions states are filters, and can allow users to edit notification preferences.</td></tr>
</tbody>
</table>
{:/}

#### Dashes {#dashes}

##### Em Dash

Use an em dash (—) when using a dash in a sentence to indicate a separate thought or interruption. Don’t put any spaces before or after the em dash. Don’t use an em dash where a comma or parenthesis would work just as well.

Refer to your operating system for how to type an em dash:

* **macOS:** Press Option + Shift + Hyphen.  
* **Windows:** Turn num lock on, then hold down the left Alt key and type 0151 on the num pad.

##### En Dash {#en-dash}

Use an en dash (–) to indicate a range of numbers, as a minus sign, or to indicate negative numbers. Don’t put any spaces before or after the en dash except for when it’s used as a minus sign. Don’t use a hyphen (-). 

{::nomarkdown}
<table style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Do</th><th style="width: 50%;">Don't</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Do <br><br> <em>Use an en dash for a range of numbers</em></td><td style="width: 50%;">Don’t <br><br> <em>Use a hyphen</em></td></tr>
<tr><td style="width: 50%;">2018–2021</td><td style="width: 50%;">2018-2021</td></tr>
</tbody>
</table>
{:/}

Don’t use an en dash for ranges of time. For more details, refer to the section [Dates and Times](#dates-and-times).

{::nomarkdown}
<table style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Do</th><th style="width: 50%;">Don't</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Do <br><br> <em>Use an en dash for a minus sign and include spaces surrounding the en dash</em></td><td style="width: 50%;">Don’t <br><br> <em>Use a hyphen</em></td></tr>
<tr><td style="width: 50%;">15 – 5 = 10</td><td style="width: 50%;">15-5=10</td></tr>
</tbody>
</table>
{:/}

{::nomarkdown}
<table style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Do</th><th style="width: 50%;">Don't</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Do <br><br> <em>Use an en dash for negative numbers</em></td><td style="width: 50%;">Don’t <br><br> <em>Use a hyphen</em></td></tr>
<tr><td style="width: 50%;">–30</td><td style="width: 50%;">-30</td></tr>
</tbody>
</table>
{:/}

Refer to your operating system for how to type an en dash:

* **macOS:** Press Option + Hyphen.  
* **Windows:** Turn num lock on, then hold down the left Alt key and type 0150 on the num pad.

#### Ellipses {#ellipses}

An ellipsis is a series of three periods (...) that indicates an omission of one or more words. In general, avoid using ellipses when possible while writing instructions or learning content. 

#### Exclamation Points {#exclamation-points}

An exclamation point can be used sparingly for an informal tone. However, avoid overly using exclamation points throughout text. Instead, consider using Alerts.

{::nomarkdown}
<table style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Do</th><th style="width: 50%;">Don't</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Do <br><br> <em>Use exclamation points for an informal tone for reminders and introductions</em></td><td style="width: 50%;">Don’t <br><br> <em>Use exclamation points for indicating warning or caution to readers</em></td></tr>
<tr><td style="width: 50%;">Be sure to save your changes before leaving the page!</td><td style="width: 50%;">Users must receive one or more messages from a step to be counted as a unique recipient!</td></tr>
</tbody>
</table>
{:/}

#### Hyphens {#hyphens}

Hyphens can help the reader gain more clarity in a sentence by linking words in a phrase together. Here are a few guidelines for getting it right.

Use hyphens for compound modifiers that help the reader understand the subject more clearly.

{::nomarkdown}
<table style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 100%;">Do</th></tr>
</thead>
<tbody>
<tr><td style="width: 100%;">real-time data streaming</td></tr>
</tbody>
</table>
{:/}

Use hyphens to link a phrase, with a space between the modifier and subject. 

{::nomarkdown}
<table style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 100%;">Do</th></tr>
</thead>
<tbody>
<tr><td style="width: 100%;">All-in-one solutions</td></tr>
</tbody>
</table>
{:/}

Use hyphens for a phrase that modifies a subject. There’s no need to use a hyphen if the phrase is the subject.

{::nomarkdown}
<table style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Do</th><th style="width: 50%;">Don't</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">It was a well-known fact.</td><td style="width: 50%;">That fact is well-known</td></tr>
</tbody>
</table>
{:/}

Don’t use hyphens in place of an em dash to create a pause in a sentence.

{::nomarkdown}
<table style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Do</th><th style="width: 50%;">Don't</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">...third-party integrations—such as Slack—and automate...</td><td style="width: 50%;">...third-party integrations-such as Slack-and automate...</td></tr>
</tbody>
</table>
{:/}

Don’t use a hyphen after an adverb. Keep the words separate.

{::nomarkdown}
<table style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Do</th><th style="width: 50%;">Don't</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Hastily made</td><td style="width: 50%;">Hastily-made</td></tr>
</tbody>
</table>
{:/}

#### Parentheses {#parentheses}

Use parentheses sparingly. Never put important information in parentheses, as some readers skip content in parentheses.

For less important parentheticals, consider reworking the sentence to remove the parentheses. For example, you can set off the phrase or sentence using commas, dashes, semicolons, or by adding a new sentence.

If a parentheses is part of a larger sentence, place the period outside of the parenthesis. If the parentheses contain a complete sentence, place the period inside. 

**Related section:** [Plurals in Parentheses](#plurals-in-parentheses)

#### Periods {#periods}

Use a period to end sentences. Do not use a period to end headlines, headings, subheadings, or UI elements.

For guidelines on when to use periods with list items, refer to [Lists](#lists).

#### Semicolons {#semicolons}

Semicolons are great for breaking up a longer, more complicated sentence. Use a semicolon to separate two independent clauses that are closely related in topic. 

{::nomarkdown}
<table style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 100%;">Do</th></tr>
</thead>
<tbody>
<tr><td style="width: 100%;"><em>Use a semicolon to break up a sentence with two related independent clauses</em></td></tr>
<tr><td style="width: 100%;">The cat slept through the storm; the dog cowered under the bed.</td></tr>
</tbody>
</table>
{:/}

Semicolons can be used to separate list items if one (or more) of the list items contains a comma.

{::nomarkdown}
<table style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 100%;">Do</th></tr>
</thead>
<tbody>
<tr><td style="width: 100%;"><em>Use a semicolon to break up a longer sentence</em></td></tr>
<tr><td style="width: 100%;">Jane Lang, our moderator; Simon Mayer, CEO and Cofounder of PantsLabyrinth; and Kara Seberg, CMO of Yachtr.</td></tr>
</tbody>
</table>
{:/}

#### Slashes {#slashes}

There are two types of slashes: backward (\\) and forward (/). Do not use slashes to indicate alternative words or examples (“and/or”). 

Use slashes as needed in file paths and URLs.

{::nomarkdown}
<table style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Do</th><th style="width: 50%;">Don't</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Do <br><br> <em>Use a slash for file paths</em></td><td style="width: 50%;">Don’t <br><br> <em>Use a slash to separate alternatives</em></td></tr>
<tr><td style="width: 50%;"><code>/campaigns/data_series</code></td><td style="width: 50%;">you/your customers</td></tr>
</tbody>
</table>
{:/}

#### Quotation Marks {#quotation-marks}

There are two types of quotation marks: straight (" ") and curly (“ ”). Periods and commas go inside the quotation marks. An exception is when the quotation marks include exact information such as a string. Use quotation marks when directing users to input a specific string of text into a text field.

{% alert note %}

When describing search syntax, quotation marks are often used to signify searching for exact text. In this case, use brackets around the string of text and quotation marks as required by the search syntax. For example: <br><br>

*Put quotes around any word or phrase, such as [“test segment”], and we show results that contain only those exact words or phrases.* 

{% endalert %}

Code examples must use straight quotation marks. For more information about formatting code in text, refer to [Code in Text](#code-in-text).

### Technical documentation {#technical-documentation}

#### API Endpoints {#api-endpoints}

In general, documentation for API endpoints should follow the guidelines in this style guide. However, there are niche topics that may require different content guidelines listed in this document. For more information on how to format and reference endpoints, refer to [API Endpoint Documentation Guidelines](https://docs.google.com/document/d/1PotRvG7A4JS6hGaH1knMF1HPEM-HkwBo3O90q1Zul-4/edit?usp=sharing). 

#### Avoid Guarantees {#avoid-guarantees}

Our documentation must refrain from making commitments that could potentially result in legal implications. Avoid using definitive terms such as "guarantee" or "ensure." Instead, employ forward-looking statements like "Designed to" or "Intended to" to accurately convey the product's capabilities and intentions.

#### Describing Interactions with the UI {#describing-interactions-with-the-ui}

When referring to UI elements, match the capitalization as it appears in the UI. However, If a label is all caps, use sentence case (exception: short labels, like AND or OR operators). 

When instructing a reader to interact with the UI, bold the UI element they are interacting with. For strings that a user would enter into a field, use quotation marks. 

For guidance on what verbs to use when describing interactions with the UI, refer to the following table:

{::nomarkdown}
<table style="table-layout: fixed; width: 100%;">
<colgroup>
<col style="width: 20%;">
<col style="width: 40%;">
<col style="width: 40%;">
</colgroup>
<thead>
<tr><th>Verb</th><th>Usage</th><th>Example</th></tr>
</thead>
<tbody>
<tr><td>Open</td><td><ul><li>Opening apps</li><li>Opening files and folders</li></ul></td><td><ul><li>Open Droidboy.</li><li>Open the braze.xml file.</li></ul></td></tr>
<tr><td>Close</td><td><ul><li>Closing apps</li><li>Closing files and folders</li></ul></td><td><ul><li>Close Droidboy.</li><li>Close the braze.xml file.</li></ul></td></tr>
<tr><td>Go to</td><td><ul><li>Going to a specific page in the UI (tab, page, section)</li><li>Going to a webpage</li></ul></td><td><ul><li>Go to the <strong>Segments</strong> page, and click…</li><li>Go to example.com to sign up.</li></ul></td></tr>
<tr><td>&gt;</td><td>Following a sequence of steps when all steps are of the same type.</td><td>Go to <strong>Segments</strong> &gt; <strong>Segment Insights</strong>.</td></tr>
<tr><td>Choose</td><td>Making a decision that is subjective, strategic, open-ended, or complex.</td><td>Choose a campaign strategy.</td></tr>
<tr><td>Select</td><td><ul><li>Selecting a checkbox</li><li>Selecting items from a dropdown</li><li>Selecting a tab</li><li>Making a simple decision</li></ul></td><td><ul><li>Select <strong>Show Password</strong>.</li><li>Select a data type from the dropdown.</li><li>On the <strong>Manage Settings</strong> page, select the <strong>Custom Events</strong> tab.</li><li>Select an image.</li></ul></td></tr>
<tr><td>Clear</td><td>Clearing the selection from a checkbox.</td><td>Clear the <strong>Show Password</strong> checkbox.</td></tr>
<tr><td>Click</td><td>Clicking an element in the UI.</td><td>Add a custom attribute and click <strong>Save</strong>.</td></tr>
<tr><td>Turn on</td><td>Enabling a toggle option</td><td>Turn on the <strong>List-Unsubscribe header</strong>.</td></tr>
<tr><td>Turn off</td><td>Disabling a toggle option</td><td>Turn off <strong>Inline CSS on New Emails by Default</strong>.</td></tr>
<tr><td>Enter</td><td>Typing a value.</td><td><ul><li>In the text field, enter the name of your custom attribute.</li><li>Enter "Braze" as the source name.</li></ul></td></tr>
</tbody>
</table>
{:/}

#### Describing Limitations {#describing-limitations}

Write candidly about the product's limitations, without distortion or manipulation. Readers react in an intense fashion to being manipulated, hoodwinked, and otherwise bamboozled, and this jeopardizs the documentation's efficacy as a source of utilitarian truth. Customers rely on documentation to understand the limits of the system to which they are building so that they can use Braze successfully.

At the same time, support the intentionality of the product's development by framing limitations with appropriate, positive context.

* If there is a soft limitation (for example, an API rate limit), frame the limitation by talking about the **default limit** or **starting allotment.**  
* Provide a meaningful path forward to navigate soft limits. Provide examples of these workarounds as appropriate.  
 * For example, Braze uses sizing exercises during onboarding to help customers understand how things such as data points are used by other businesses of a similar size. When discussing data points, it is appropriate to talk about the sizing exercise at the same time.  
* It is better to describe a path forward in a positive way than as a mitigation.   
 * For example, instead of saying "Braze does not allow customers to do this on their own. The Support team must activate this feature for you," say, "To activate this feature, contact the Support team."  
* Do not over-rely on the same stock phrases to navigate soft limits. If a user reads "Talk to your customer service representative" over and over, the advice becomes meaningless.  
* If there is a hard limitation, try to describe the rationale behind this limit.  
 * For example: "There is a limit of 200 active, action-based in-app message campaigns per app group to optimize the speed of message delivery and to prevent timeouts. …The average Braze customer has a total of 26 campaigns active at once—so it's unlikely that this limitation impacts you."  
* Do not describe [planned functionality or future features](#heading=h.4wvw32nz50ee) as a way to explain current limitations.  
* When referring to limits around custom data, use the term "capacity" instead of limits.   
 * For example: By default, you can have 20 segmentable event properties per workspace. Contact your Braze account manager to increase your capacity. 

#### Future Features {#future-features}

Avoid references to future features, or suggestions that something may be supported in the future.

Don’t use words and phrases that anchor your writing to a point in time, as they make content become quickly outdated. Focus on how the product works right now, not on what has changed (except for time-focused content, such as in release notes).

Specifically avoid the following list of words and phrases, taken from Google’s [developer documentation style guide](https://developers.google.com/style/timeless-documentation):

* as of this writing  
* currently  
* does not yet  
* eventually  
* future, in the future  
* latest   
* new, newer  
* now  
* old, older  
* presently, at present  
* soon

#### Features Deprecations {#features-deprecations}

Before including information about feature deprecations, be sure you have a general time frame of when readers can expect the feature to be deprecated (for example, late 2025).

After you have a general time frame, communicate the feature deprecation early. Be clear in writing about deprecations so that readers can clearly understand what to expect.

Don't use phrases that might incite fear, uncertainty, or doubt with readers. Provide a clear path forward, such as what the deprecated feature is being replaced by or an alternative solution.

#### General vs Specific {#general-vs-specific}

As a best practice, write articles that discuss functionality in a generally applicable way. If more detail is needed for specific cases or exceptions, create a separate section (or separate article if the content is web article length, ~500 words) that outlines this outlier. Create cross-references from the general article to the specific to help users connect these concepts.

Avoid creating duplicated or repetitious content for different channels or features. If repetition is needed, use `includes` files and other [reusable content best practices]({{site.baseurl}}/contributing/content_management/reusing_content).

**As an example:** A common use case for Braze customers is to retarget users who have previously interacted with their messaging. Retargeting users can be done through many engagement tools, including campaigns, Canvases, landing pages, and segments. Retargeting users can be done through many channels: WhatsApp, SMS, Content Cards, email, push notifications, and more. Often, customers try to reengage a user through a separate channel than one previously used.  
Instead of creating one article for each engagement tool and each channel, create a single article that discusses strategies for retargeting users and outlines all the options available. If there are special considerations for specific channels/tools, create a separate article that outlines those considerations and house it within that documentation section. Create cross-references between the general article and the specific article.

#### Metadata and YAML {#metadata-and-yaml}

Articles in Braze documentation require certain metadata for search and index purposes. For information on what metadata is required, refer to the GitHub page on [YAML and Metadata Layouts](https://github.com/braze-inc/braze-docs/wiki/YAML-%26-Metadata-Layouts).

#### Naming Conventions {#naming-conventions}

When naming articles and filenames, make sure to describe the general topic in the title. Always include a keyword and brief description that readers easily understand, especially with article titles. 

For filenames, keep the name brief and avoid using articles (a, an, the). Separate each word with an underscore (_).

{::nomarkdown}
<table style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 100%;">Do</th></tr>
</thead>
<tbody>
<tr><td style="width: 100%;">Targeting users</td></tr>
<tr><td style="width: 100%;">Creating an email campaign</td></tr>
<tr><td style="width: 100%;">API errors and responses</td></tr>
<tr><td style="width: 100%;">sms<em>historical</em>performance.png</td></tr>
<tr><td style="width: 100%;">push<em>notification</em>test.png</td></tr>
</tbody>
</table>
{:/}

In general, for articles and image files, use the same spelling and capitalization as the referenced article and files. For guidelines on article title styling, refer to [Headings and Titles](#headings-and-titles).

When referring to a specific file, use the same spelling of the filename and code font. For formatting details, refer to the GitHub page on [Special Formatting](https://github.com/braze-inc/braze-docs/wiki/Special-Formatting). 

#### Procedures and Instructions {#procedures-and-instructions}

This section covers some guidelines to keep in mind when writing instructions for procedures in the Braze dashboard. 

General guidelines:

* **Use the right tone.** For instructions, keep your writing short, to the point, and task-oriented. Your writing doesn’t need to be terse or dry, but it should be direct. When introducing tasks or subtasks, you can use a more informal tone to add variety. Avoid using “please” to keep the tone informal. Make liberal use contractions to keep your tone approachable.   
* **Follow parallel heading format.** Pick one format for your headings and stick to it. Keep your content scannable and predictable. In general, use gerunds (ing-words) for page titles, and imperative verbs for task-based headings. 

Before instructions:

* **Use introductions and prerequisites.** Don’t jump straight into the steps. Instead, give context on what your article or section covers, and provide any information the reader needs to know before they scan the instructions. Make sure any prerequisites are listed at the top of the document.  
* **Start at the beginning of the procedure.** Don’t assume the reader has reached this page after completing a previous step. If the instructions for a task pick up where another left off, give an overview of where the reader is in the procedure, and what they must complete before this step. Include links to any previous steps.

Writing instructions:

* **Use actionable language.** Structure documentation around what the user can do, not what the product can do. Avoid language like “This feature [does xyz]”. Instead, think in terms of “Use this feature to [do xyz]”.  
* **Provide location steps when needed.** Make sure the reader is looking in the right place with brief phrases such as “On the **Settings** page, click **Edit**.” If that may not be clear enough, provide an introductory step. For example, “Go to **Manage Settings** and select the **Settings** tab.”   
* **Preface conditional statements**. Put [conditional clauses](#clause-order) first. For conditional instructions, preface the step with “if” so the reader knows they can skip the step if the condition doesn’t apply to them. For example, “If you need X, then do A > B > C.”  
* **Reinforce task order.** For progress within a series of steps, use the phrase “When you’ve” or “After you’ve”. For progress between tasks, begin a section with “Now that you’ve” or “After you’ve”. Avoid the phrase “Once you’ve”, as that specific use of “once” doesn’t translate well. 

#### Tabs {#tabs}

Tabs can be used in technical documentation as a way to organize grouped information.

A tab refers to an element that can be used when writing instructions to demonstrate a workflow summary or to organize grouped information. This is similar to a table or list, but the information is grouped into panels.

Consider using tabs when information can be grouped together to avoid duplication or to visualize a workflow for readers. Ensure that the tabs include parallel information, and are not used for when the reader must follow sequential steps in a workflow. 

For example, you can use tabs to show code examples in different programming languages. In this case, a reader would toggle between the examples based on the tab labels as opposed to scrolling through the article.

For formatting details, refer to the GItHub page on [Special Formatting](https://github.com/braze-inc/braze-docs/wiki/Special-Formatting). Alternatively, you can also use a [list](#lists) or [table](#tables-1) to organize information.

### Formatting and organizing {#formatting-and-organizing}

#### Addresses {#addresses}

Use the numeral followed by the street name like so: 

*330 W. 34th St.*

To display a full address, use the numeral, followed by the street name, followed by the city, state, and zip code. There’s no need for a comma between the state and zip code.

*330 W. 34th St., New York, NY 10001*

#### Buttons Labels {#buttons-labels}

Button labels should be clear and predictable—the user should know what action occurs upon clicking the button. Use sentence case for button labels, and lead with a strong verb. If it may be unclear what the verb is referring to, use the format [verb] + [noun]. 

{::nomarkdown}
<table style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Do</th><th style="width: 50%;">Don't</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Sign up</td><td style="width: 50%;">Sign Up</td></tr>
<tr><td style="width: 50%;">Log in</td><td style="width: 50%;">Log In</td></tr>
<tr><td style="width: 50%;">Subscribe</td><td style="width: 50%;">SUBSCRIBE</td></tr>
<tr><td style="width: 50%;">Learn more</td><td style="width: 50%;">More</td></tr>
</tbody>
</table>
{:/}

Omit unnecessary words and articles, such as “a”, “an,” or “the”.

#### Callouts and Alerts {#callouts-and-alerts}

Alerts, also known as callouts, are used to draw attention to information that is helpful to the reader. There are four alerts types that are used in our documentation:

* Important  
* Note  
* Tip  
* Warning

Use alerts sparingly throughout articles. For more information, refer to [Best Practices for Alerts]({#alerts}).

#### Code in Text {#code-in-text}

There are a few scenarios where you should use code font to format text within a sentence. Here is an incomplete list of items that should be in code font:

* Attribute names and values  
* API request parameters  
* Filenames  
* File paths  
* Method, variable, or parameter names  
* HTML and XML element names  
* HTTP status codes  
* Text input into a terminal

To create in-line code text in Braze documentation, surround the text in backticks (`). 

#### Code Samples {#code-samples}

Code samples refer to blocks of code text that display a sample snippet of code. For accessibility purposes, introduce the code sample with an expository sentence where possible.

To make sure your code samples are legible, indent each line by two spaces per indentation level. If you’re having trouble formatting your code samples, try prettifying your code using a pretty print formatter, such as [JSON Formatter](https://jsonformatter.org/json-pretty-print).

To create code blocks in Braze documentation, refer to [Code Snippet Test](https://github.com/braze-inc/braze-docs/blob/develop/_docs/_home/styling_test_page.md#code-snippet-test). Remember that code blocks should specify the language type to ensure proper syntax highlighting.

#### Dates and Times {#dates-and-times}

Spell out the month and days of the week. Avoid abbreviations when possible. For instances when abbreviating months are required, only abbreviate the following: 

* Jan.  
* Feb.  
* Aug.  
* Sept.  
* Oct.  
* Nov.  
* Dec.

Use a [comma](#commas) to separate the date from the year. If a day of the week is used with the date, add it before the month.

{::nomarkdown}
<table style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 100%;">Do</th></tr>
</thead>
<tbody>
<tr><td style="width: 100%;"><em>Use the preferred date format.</em></td></tr>
<tr><td style="width: 100%;">September 2021</td></tr>
<tr><td style="width: 100%;">September 15, 2021</td></tr>
<tr><td style="width: 100%;">Wednesday, September 15, 2021</td></tr>
</tbody>
</table>
{:/}

For date ranges, use an [en dash](#en-dash).

{::nomarkdown}
<table style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 100%;">Do</th></tr>
</thead>
<tbody>
<tr><td style="width: 100%;">2010–2021</td></tr>
</tbody>
</table>
{:/}

Use an en dash for date ranges.

Use numerals with am or pm, followed by a space, followed by the time of day (am or pm). Remove the minutes from on-the-hour time.

{::nomarkdown}
<table style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Do</th><th style="width: 50%;">Don't</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Do <br><br> <em>Use numerals with am or pm.</em></td><td style="width: 50%;">Don’t <br><br> <em>Use minutes for on-the-hour time (unless it's a range).</em></td></tr>
<tr><td style="width: 50%;">12 pm</td><td style="width: 50%;">12:00 P.M.</td></tr>
</tbody>
</table>
{:/}

For ranges of time, use an en dash to separate. Do not add spaces before or after the en dash.

{::nomarkdown}
<table style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Do</th><th style="width: 50%;">Don't</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Do <br><br> <em>Use an en dash for range of time.</em></td><td style="width: 50%;">Don’t <br><br> <em>Use minutes for ranges of time.</em></td></tr>
<tr><td style="width: 50%;">12:45–2:30 pm</td><td style="width: 50%;"></td></tr>
</tbody>
</table>
{:/}

For reference in instances where parties from other time zones are included (like webinars, meetings, or events), indicate the time zone as noted below:

* Eastern Standard Time: EST  
* Central Standard Time: CST  
* Mountain Standard Time: MST  
* Pacific Standard Time: PST  
* Greenwich Mean Time: GMT  
* Coordinated Universal Time: UTC  
* Central European Time: CET  
* Eastern Europe Time: EET  
* Western Europe Time: WET  
* Singapore Time: SGT  
* China Standard Time: CST

#### Emojis {#emojis}

While we’re a casual bunch, avoid using emojis in learning content as they can be interpreted in different ways and often come off as unprofessional. 

Exceptions include the following scenarios:

* When using ✅ and ❌ in tables to denote content that is supported versus unsupported, or recommended versus not recommended  
* When used in example copy for a campaign or Canvas message

#### Example Names {#example-names}

Never use real names, email addresses, or any other personally identifiable information (PII). Instead, use fictional examples or [placeholder text](#placeholder-text). 

When you need to include names in your writing, refer to Wikipedia’s list of [Unisex names](https://en.wikipedia.org/wiki/Unisex_name). Use the pronouns “they”, “their”, and “theirs” when possible, and avoid using examples that are limited to a specific gender.

##### Example Email Addresses

Use the format “name@example.com” for generic email addresses. Replace “name” with an example name. For example:

* alex@example.com  
* lee@example.com  
* yuri@example.com

#### Figures and Other Images {#figures-and-other-images}

When creating figures and images, refer to the [Image Copy Style Guide]({#image_style_guide}). Never include personally identifiable information (PII) in figures or images.

##### Alt Text {#alt-text}

Always include alt text with images. Screen readers announce alt text to explain images to people with loss of vision. As such, your alt text must convey all the key information depicted in the image.  
Use the following guidelines when writing alt text:

* Use [plain language](https://www.plainlanguage.gov/guidelines/).  
* Write in complete sentences, and use sentence case.  
* Omit unnecessary words.  
* Don’t include “image of” or “picture of”. It’s already understood that you are referring to an image.   
* Don’t include special characters. For example, instead of ampersands (&), use the word “and” written out.

{::nomarkdown}
<table style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Do</th><th style="width: 50%;">Don't</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Custom Events settings page in the Braze dashboard with Add Report highlighted.</td><td style="width: 50%;">A screenshot of the Manage Settings > Custom Events page in the Braze dashboard with the option to add a report highlighted.</td></tr>
</tbody>
</table>
{:/}

Leave alt tags explicitly blank (alt="") if the image is adding a redundant visual component to what is explained in the text. 

Adding alt text to every image does not automatically make webpage content easy to navigate and consume. Redundant visuals are powerful for sighted users because visual information is easy to understand and remember. However, alt text describing redundant images can be unnecessary for users who can’t see the image because every page element demands equal attention from screen-reader users to determine if it’s useful for their task.

##### Example company names

If possible, take screenshots from [dashboard-06](https://dashboard-06.braze.com/) so that you’re using one of the FakeBrandz company names.

#### File Types and Filenames {#file-types-and-filenames}

When you’re referring to a file type, use the standard name of the type. If the file type is an acronym, refer to the file type in all caps. 

{::nomarkdown}
<table style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Do</th><th style="width: 50%;">Don't</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Do <br><br> <em>Use the standard name of the file type</em></td><td style="width: 50%;">Don’t <br><br> <em>Use the file extension</em></td></tr>
<tr><td style="width: 50%;">CSV</td><td style="width: 50%;">.csv</td></tr>
<tr><td style="width: 50%;">executable file</td><td style="width: 50%;">.exe</td></tr>
<tr><td style="width: 50%;">GIF</td><td style="width: 50%;">.gif</td></tr>
<tr><td style="width: 50%;">JAR</td><td style="width: 50%;">.jar</td></tr>
<tr><td style="width: 50%;">JPEG</td><td style="width: 50%;">.jpg, .jpeg</td></tr>
<tr><td style="width: 50%;">JSON</td><td style="width: 50%;">.json</td></tr>
<tr><td style="width: 50%;">PDF</td><td style="width: 50%;">.pdf</td></tr>
<tr><td style="width: 50%;">PNG</td><td style="width: 50%;">.png</td></tr>
<tr><td style="width: 50%;">Python file</td><td style="width: 50%;">.py</td></tr>
<tr><td style="width: 50%;">Bash file</td><td style="width: 50%;">.sh</td></tr>
<tr><td style="width: 50%;">text file</td><td style="width: 50%;">.txt</td></tr>
<tr><td style="width: 50%;">YAML</td><td style="width: 50%;">.yaml</td></tr>
<tr><td style="width: 50%;">ZIP</td><td style="width: 50%;">.zip</td></tr>
</tbody>
</table>
{:/}

When you’re referring to the name of a file, format the filename as code text. For more information, see the section [Code in Text](#code-in-text).

When naming files in Braze documentation, such as article or image files, use all lowercase and separate words with underscores, not hyphens. For more information, refer to [Creating Files and Folders](https://github.com/braze-inc/braze-docs/wiki/Creating-Files-&-Folders) on GitHub. 

#### Footnotes {#footnotes}

Footnotes are annotations that provide additional information and are usually placed at the end of a page. Because of the formatting of our text, footnotes are not optimal for most use cases. The following describes when to use footnotes versus other attribution methods:

* If you are presenting a list of statistics or other dense information that all need to be attributed to sources, use footnotes.  
* If you are presenting one or two pieces of information, use a link or an alert.  
* If you need to provide additional information to items in a table, use an asterisk (*) symbol next to the table item and present the information after the table.

#### Formatting Text in Instructions {#formatting-text-in-instructions}

Use consistent text formatting to help readers find and interpret information. This section provides guidelines on what formatting to use when describing or referring to different text elements in your instructions.

This section covers the following elements:

* [Buttons](#buttons)  
* [Checkboxes](#checkboxes)  
* [Command-line commands and options](#command-line-commands-and-options)  
* [Dialog boxes](#dialog-boxes-(modals))  
* [Error messages](#error-messages)  
* [Filter and operator names](#filter-and-operator-names)  
* [Folder and filenames](#folder-and-filenames)  
* [Key names and combinations](#key-names-and-combinations)  
* [Metrics](#metrics)  
* [Pages](#metrics)  
* [Permission names](#permission-names)  
* [Tabs](#tabs-1)  
* [Text input](#text-input)

##### Buttons {#buttons}

When referring to a button, use bold text for the button label. In most cases, match the capitalization of the UI. For buttons where the label is in all caps (except OK buttons), use sentence case instead. 

To refer to a button, use only the button’s label. Do not refer to a button as “the [label] button”.

{::nomarkdown}
<table style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Do</th><th style="width: 50%;">Don't</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Click <strong>Add Languages</strong>.</td><td style="width: 50%;">Click the <strong>Add Language</strong>s button. <br><br> Click “Add Languages”.</td></tr>
</tbody>
</table>
{:/}

If the label ends with a colon or ellipsis, omit the ending punctuation. 

{::nomarkdown}
<table style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Do</th><th style="width: 50%;">Don't</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Click <strong>Save as</strong></td><td style="width: 50%;">Click <strong>Save as…</strong></td></tr>
</tbody>
</table>
{:/}

If a button is an icon, include the name of the button as shown in the tooltip. If a button with an icon doesn't include a tooltip, submit a request that a tooltip be added.

{::nomarkdown}
<table style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Do</th><th style="width: 50%;">Don't</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Click ➕ <strong>Add</strong>.</td><td style="width: 50%;">Click the ➕ icon.</td></tr>
</tbody>
</table>
{:/}

##### Checkboxes {#checkboxes}

When referring to a checkbox, use bold text for the checkbox label. Don’t include the word “checkbox” unless clarity is needed. Prefer the terms “select/clear” versus “check/uncheck”.

{::nomarkdown}
<table style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Do</th><th style="width: 50%;">Don't</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Select <strong>Send campaign to users in their local time zone</strong>.</td><td style="width: 50%;">Check <strong>Send campaign to users in their local time zone</strong>.</td></tr>
<tr><td style="width: 50%;">Clear the <strong>Exit</strong> checkbox.</td><td style="width: 50%;">Uncheck the <strong>Exit</strong> checkbox.</td></tr>
</tbody>
</table>
{:/}

##### Command-line commands and options {#command-line-commands-and-options}

When referring to command-line commands or options, use code formatting. Match capitalization to how it appears, or how it must be typed. 

##### Dialog boxes (Modals) {#dialog-boxes-(modals)}

Avoid referring to dialog boxes by name unless clarity is needed. Instead, describe what the reader needs to do. If you refer to a dialog box, use bold text for the name of the dialog box and match the capitalization of the UI.

{::nomarkdown}
<table style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Do</th><th style="width: 50%;">Don't</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Click <strong>Upload</strong> then select a file to upload.</td><td style="width: 50%;">Click <strong>Upload</strong> and use the <strong>File Upload</strong> dialog box to select a file to upload.</td></tr>
</tbody>
</table>
{:/}

##### Error messages {#error-messages}

When referring to error messages that a reader may encounter, encapsulate the error message in quotation marks. For longer error messages, use a block quote.

{::nomarkdown}
<table style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Do</th><th style="width: 50%;">Don't</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">“Push Bounced: MismatchSenderId”</td><td style="width: 50%;"><em>Push Bounced: MismatchSenderID</em><br><br><code>Push Bounced: MismatchSenderID</code></td></tr>
</tbody>
</table>
{:/}

##### Filter and operator names {#filter-and-operator-names}

When referring to the names of filters and operators for segments or other areas of the dashboard, use code text. Match the case of the UI, including elements that are in all caps such as `OR` and `AND` operators. 

{::nomarkdown}
<table style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Do</th><th style="width: 50%;">Don't</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Select the <code>First Used App</code> filter and…</td><td style="width: 50%;">Select the <strong>First Used App</strong> filter and…</td></tr>
<tr><td style="width: 50%;">Combine filters with the <code>OR</code> operator.</td><td style="width: 50%;">Combine filters with the “OR” operator.</td></tr>
</tbody>
</table>
{:/}

##### Folder and Filenames {#folder-and-filenames}

When referring to folder names and filenames, use code text. 

{::nomarkdown}
<table style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Do</th><th style="width: 50%;">Don't</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Open the <code>braze.xml</code> file.</td><td style="width: 50%;">Open the <strong>braze.xml</strong> file.</td></tr>
</tbody>
</table>
{:/}

##### Key names and combinations {#key-names-and-combinations}

When referring to key names or key combinations, use the [HTML `<kbd>` tag](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/kbd). This denotes textual user input from a keyboard, voice input, or any other text entry device. If you’re working in an editor that doesn’t support custom HTML, use [code text](#code-in-text) instead.

Spell out the names of keys such as Command, Control, Option, and Shift. Don't use symbols for those keys.

{::nomarkdown}
<table style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Do</th><th style="width: 50%;">Don't</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Press <strong>Option</strong>.</td><td style="width: 50%;">Press ⌥.</td></tr>
</tbody>
</table>
{:/}

For key combinations, use a plus (+) sign between keys, but omit the plus from any special formatting. 

{::nomarkdown}
<table style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Do</th><th style="width: 50%;">Don't</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Press <strong>Option + F12</strong>.</td><td style="width: 50%;">Press ⌥ + F12.</td></tr>
</tbody>
</table>
{:/}

For example, this is how keyboard tags appear in Braze documentation:  
To stop the command, press **Control + C**.

##### Metrics {#metrics}

When referring to a metric in a table or glossary entry, use initial caps with no special formatting. When referring to a metric in a sentence, use initial caps with italics (such as *Machine Opens*).

##### Pages

Use the term page when referring to a web page in general, or a specific page on the Braze dashboard. When referring to a page name, use the format “the [label] page” and bold the name of the page.

{::nomarkdown}
<table style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Do</th><th style="width: 50%;">Don't</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Go to the Segments page.</td><td style="width: 50%;">Go to the “Segments” page.</td></tr>
</tbody>
</table>
{:/}

##### Permission names {#permission-names}

When referring to names of user permissions within the dashboard, enclose the permission name in quotes.

{% alert note %}

Currently we are using title case to match the formatting of the dashboard. There is a plan to update the permission names within the UI to sentence case to match our standards. 

{% endalert %}

##### Tabs {#tabs-1}

When referring to a tab, use the format “the [label] tab” and bold the name of the tab.

{::nomarkdown}
<table style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Do</th><th style="width: 50%;">Don't</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Go to the <strong>Manage Settings</strong> page and select the <strong>Tags</strong> tab.</td><td style="width: 50%;">Go to the “Manage Settings” page and select the “Tags” tab.</td></tr>
</tbody>
</table>
{:/}

##### Text input {#text-input}

When instructing a reader to type a specific string of text, enclose the text in quotes.

{::nomarkdown}
<table style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Do</th><th style="width: 50%;">Don't</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">In the <strong>Name</strong> field, enter “Lapsing Users”</td><td style="width: 50%;"></td></tr>
</tbody>
</table>
{:/}

#### Frequently Asked Questions (FAQs) {#frequently-asked-questions-(faqs)}

Order the FAQs by starting with the information that people most want or need to know, and then organize the FAQs by issue category if there are multiple ones.

For each FAQ, start by directly answering the question, then go into detail. Use real questions that match typical search queries and user vocabulary, which helps with FAQ findability. Include links to resources that the user may find helpful, such as related articles, instructions for contacting support, and teaching materials (how to guides, tutorials, and others) when available. 

#### Geography {#geography}

##### Cities

Spell out all city names on the first mention in the copy. After that, it’s fine to abbreviate well-known city names like NYC or LA.

**First mention:** San Francisco  
**Second mention:** SF

For well-known cities like London or Tokyo, it’s fine to introduce them without a comma followed by the state, province, or country. 

For cities or towns that may be unfamiliar to your audience, include the state, province, or country.

{::nomarkdown}
<table style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 100%;">Do</th></tr>
</thead>
<tbody>
<tr><td style="width: 100%;">Biloxi, Mississippi</td></tr>
<tr><td style="width: 100%;">New Bedford, MA</td></tr>
<tr><td style="width: 100%;">Antwerp, Belgium</td></tr>
</tbody>
</table>
{:/}

##### Countries

Capitalize the names of all countries. To abbreviate a country name, spell the first mention out in full, followed by the initials moving forward.

**First mention:** United States  
**Second mention:** US  
		  
Don’t place periods between abbreviated country names.

{::nomarkdown}
<table style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Do</th><th style="width: 50%;">Don't</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">UK</td><td style="width: 50%;">U.K.</td></tr>
<tr><td style="width: 50%;">Washington, DC</td><td style="width: 50%;">Washington, D.C.</td></tr>
</tbody>
</table>
{:/}

##### Regions

Capitalize both the region and the directional modifying it.

**Example:** Northern California, Eastern Europe

Capitalize proper nouns describing a specific region or place.

**Example:** West Midlands, South America, South Chicago

##### States and Provinces

Capitalize all states and provinces. 

**Example:** New York, Quebec

#### Headings and Titles {#headings-and-titles}

For article headings and titles, use sentence case capitalization. Be descriptive when writing headings and titles, and focus on the main purpose of the content based on the article type. 

For article titles, use gerunds (verbs ending in *-ing*) to begin the title when applicable. Keep the article titles concise and make sure it is appropriate for the content. For example, a reference article about SMS messages could be titled “About SMS”.

For article headings, be concise and consistent across heading titles. For example, if the article’s Heading 1 style defines each step (ex. **Step 1: Create a new push campaign**), then keep this format across the article headings for consistency.

For styling help in Braze Docs, refer to the Contributing page for [Styling examples]({{site.baseurl}}/contributing/styling_examples/?tab=markdown). 

##### Numeric subtasks

For headers that describe ordered steps, use numerals in the subtask headers.

{::nomarkdown}
<table style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Do</th><th style="width: 50%;">Don't</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Step 2: Create an SMS campaign <br><br> Step 2.1: Compose your message <br><br> Step 2.2: Schedule the delivery</td><td style="width: 50%;">Step 2: Create an SMS campaign <br><br> Step 2a: Compose your message <br><br> Step 2b: Schedule the delivery</td></tr>
</tbody>
</table>
{:/}

#### Introductions {#introductions}

Introductions serve as a quick check for users asking:

* Am I in the right document? Is this relevant to me?  
* What will I learn if I invest the time in reading this doc?  
* Do I feel like I am following a clear integration or setup journey for SMS, email, IAM, or other. (despite not spelling out which doc a user should go to next)?

The following are general guidelines for introductions. Refer to section-specific guidelines for more niche use cases.

* Introductions can be anywhere from 1-5 sentences  
* Introductions should give an overview of the doc's content or be an opener for the topic  
* Use block quotes  
* Place introductions under the H1 header of the article

##### Partners

Include an overview of the partner and a brief company description. Also, include a link to the partner site.

##### API

Include only the "Use this endpoint..." sentence in the intro. We want to keep the API endpoints as easy to navigate as possible.

##### User guide and developer guide

Intro paragraphs should be written in one of two ways:

1. With a lead-in paragraph or opener for the topic  
2. A statement of what the article contains. This often looks like "This reference article....".

While the steps in the user guide and developer guide have users relying heavily on clues from the navigation throughout their customer journey, while sometimes redundant, it is helpful to explicitly say the value of the doc right at the beginning. 

For example, if a user were going through the developer guide integrating unity. This page with the title “Integration” would not be enough to go on without including the intro sentence.

#### Lists {#lists}

Lists are best used to format related information. Don't use a list to show only one item. If you want to set a single item off from surrounding text, then use some other formatting.

There are three types of lists: bulleted, lettered, and numbered. Include an introductory complete sentence that can end with a colon or period.

* Bulleted lists organize information that does not need to be in a specific order.   
* Lettered lists are used to define mutually exclusive options.   
* Numbered lists indicate a sequence of ordered steps. 

Use the same syntax for all list items if possible. 

For list item capitalization, start each list item with a capital letter. For list item ending punctuation, do not use ending punctuation in the following scenarios:

* If the list item is a single word or incomplete sentence  
* If the list item doesn’t include a verb  
* If the list item is in code font  
* If the list item is a link or document title

#### Media Formatting {#media-formatting}

This section includes general guidelines for formatting images and GIFs in your content. For more information, including example screenshots, refer to the [Image Copy Style Guide]({#image_style_guide}).

| **Do** | {::nomarkdown}<ul><li>Do tightly crop to the feature or component of mention.</li><li>Do take high-quality screenshots, preferably on a retina monitor (MacBook display).</li><li>Do create a GIF of an interaction or workflow.</li><li>Keep in mind that users cannot pause or scrub through a GIF to see details.</li><li>Do run images through an optimizer to reduce file size (ImageOptim, TinyPNG, or Ezgif).</li><li>Do aim for high contrast between elements for accessibility.</li><li>Do resize images by height percentages rather than distinct pixel values.</li></ul>{:/} |
| **Don't** | {::nomarkdown}<ul><li>Don't include the header or sidebar of the dashboard, as these can be explained in a simple sentence.</li><li>Don't include the entire dashboard.</li><li>Don't include Personally Identifiable Information (unless blurred, or that of a demo user).</li><li>Don't include the browser frame (URL field, bookmarks, tabs, and so on.).</li><li>Don't include dashboards of Technology Partners.</li><li>Don't add a border or drop shadow to images.</li></ul>{:/} |

#### Numbers {#numbers}

Never start a sentence with a numeral. The exception is when referring to a year (example: “2019 was one for the books). 

Spell out numerals up to nine. For units of measurement or numbers 10 or higher, use the numeral. For numbers over three digits, use a comma. Write out larger numbers. 

{::nomarkdown}
<table style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Do</th><th style="width: 50%;">Don't</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">1,000</td><td style="width: 50%;">1000</td></tr>
<tr><td style="width: 50%;">200,000</td><td style="width: 50%;">200000</td></tr>
<tr><td style="width: 50%;">1,000,000</td><td style="width: 50%;">1000000</td></tr>
<tr><td style="width: 50%;">9 billion</td><td style="width: 50%;">9000000000</td></tr>
<tr><td style="width: 50%;">5 MB</td><td style="width: 50%;">five MB</td></tr>
</tbody>
</table>
{:/}

##### Currency

Always indicate what currency you’re referring to by using the currency symbol before the amount or spell it out (example: pesos, euros, pounds, and so on.).

Use the decimal for amounts where the number of cents is greater than zero. For sums greater than three digits, use a comma. Don’t include “.00” in sums of money.

{::nomarkdown}
<table style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Do</th><th style="width: 50%;">Don't</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">US $20</td><td style="width: 50%;">$20</td></tr>
</tbody>
</table>
{:/}

##### Telephone Numbers

When a phone number is referenced, place hyphens between the digits. Do not place the area code within parentheses. 

When formatting phone numbers with a country code, use a plus sign (+) before the country code and place the area code within parentheses. 

Provide a number with a country code like so: +1 (504) 327-7269

{::nomarkdown}
<table style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Do</th><th style="width: 50%;">Don't</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">123-456-7890</td><td style="width: 50%;">(123)-456-7890</td></tr>
<tr><td style="width: 50%;">+1 (123) 456-7890</td><td style="width: 50%;">1 234-567-9012</td></tr>
</tbody>
</table>
{:/}

##### Fractions

Spell out fractions and use a hyphen between the numerator and the denominator. Do not use numerals separated by a slash. 

In some cases when expressing a fraction as a decimal is necessary, add a zero before the decimal point for fractions less than one.   

When expressing rating systems using fractions, use numerals to spell out the ranking.

{::nomarkdown}
<table style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Do</th><th style="width: 50%;">Don't</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">0.5</td><td style="width: 50%;">1/2</td></tr>
<tr><td style="width: 50%;">one-third</td><td style="width: 50%;">one third</td></tr>
<tr><td style="width: 50%;">9 out of 10</td><td style="width: 50%;">nine out of ten</td></tr>
</tbody>
</table>
{:/}

##### Percentages

Use numerals and a percent sign (%) without a space in between them. However, if the percent starts the sentence, then spell out the entire percentage (number and percent).

{::nomarkdown}
<table style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Do</th><th style="width: 50%;">Don't</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">10%</td><td style="width: 50%;">10 %</td></tr>
<tr><td style="width: 50%;">Twenty percent of Braze users are...</td><td style="width: 50%;">20% of Braze users are...</td></tr>
</tbody>
</table>
{:/}

##### Ranges

Use a hyphen to indicate a range of numbers. Do not use an en dash to separate numbers in a range. 

For ranges of numbers with units, repeat the unit of measurement after the number. This does not include repeating nouns. Use the word “to” between the numbers in the range to avoid confusion.

{::nomarkdown}
<table style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Do</th><th style="width: 50%;">Don't</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">5 to 100</td><td style="width: 50%;">5–100</td></tr>
<tr><td style="width: 50%;">-10°C to 50°C</td><td style="width: 50%;">-10°C-50°C Don't</td></tr>
</tbody>
</table>
{:/}

#### Placeholder Text  {#placeholder-text}

Use placeholder text to signify where the reader should supply the relevant value. Placeholder text should indicate the content that’s being represented. For example *YOUR_API_KEY* indicates the reader’s API key.

##### Writing Placeholders

When creating placeholder text, refer to the following guidelines:

| Guideline | Example |
| :---- | :---- |
| Use uppercase letters and separate words with underscores (_). | PLACEHOLDER_VARIABLE |
| ​​For inline placeholder text, use italics. | *PLACEHOLDER_VARIABLE* |
| For API code block placeholder text (where you can’t use italics), enclose the placeholders in curly brackets ({}).  | <string name="com_appboy_api_key">{YOUR_APP_IDENTIFIER_API_KEY}</string> |
| For Liquid code block placeholder text (where you can’t use italics), use uppercase letters. | {% raw %}{%- connected_content YOUR-API-URL :save items -%}{% endraw %}  |
{::nomarkdown}
<table style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Do</th><th style="width: 50%;">Don't</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Don’t sacrifice clarity for brevity. Use as many words as needed to represent a placeholder.</td><td style="width: 50%;"><strong>Do:</strong> <em>CAMPAIGN_NAME</em> <strong>Don’t:</strong> <em>NAME</em></td></tr>
</tbody>
</table>
{:/}

##### Using Placeholders

When introducing or explaining a placeholder, refer to the following guidelines:

| Guideline | Example |
| :---- | :---- |
| Call out placeholders immediately after the placeholder. | Replace `<YOUR_APP_IDENTIFIER_API_KEY>` with your [App Identifier API Key]({{site.baseurl}}/api/api_key/#the-app-identifier-api-key), which you can find on the **Settings** page. |
| To call out two or more placeholders at once, use a bulleted list. List each placeholder in the order they appear in the code. | Replace the following: {::nomarkdown}<ul><li><code>PLACEHOLDER_VARIABLE</code>: a description of what the placeholder represents</li><li><code>PLACEHOLDER_VARIABLE</code>: a description of what the placeholder represents</li></ul>{:/} |
| Refer to the placeholder in the same formatting that it’s shown in the text or code. | {::nomarkdown}<code>target &lt;YOUR_APP_TARGET&gt; do pod 'Appboy-iOS-SDK' end</code>{:/} <br><br> Replace `<YOUR_APP_TARGET>` with the name of your target app. |

#### Products {#products}

When referring to Braze and its features, use full product and feature names, and capitalize them according to the UI. Don’t capitalize templates or common features. For a list of product names and their spelling, refer to the [Glossary](#glossary). 

Don’t abbreviate product or feature names except in the following cases:

* To match the UI  
* To meet limited space constraints

Never use product or feature names as verbs. 

Never use an apostrophe after Braze (example:“Braze’s.”) It sounds awkward. Instead, form possessives using a preposition (“to, of, from”) followed by the company name.

{::nomarkdown}
<table style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Do</th><th style="width: 50%;">Don't</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">The newest product update from Braze</td><td style="width: 50%;">Braze’s newest product update</td></tr>
<tr><td style="width: 50%;">That’s one of the defining features of Braze.</td><td style="width: 50%;">That’s one of Braze’s defining features</td></tr>
</tbody>
</table>
{:/}

Refer to “Braze” as “we/our/ours.” Never “it/its/they/their.”

#### Tables  {#tables}

Using tables can be a helpful and organized way to display information. Make sure to have clear, descriptive headers and relevant data within the respective columns and rows. 

Always use an introductory sentence to describe the purpose of the table. Avoid using tables in the middle of numbered procedures. Instead, consider using a list. 

#### Units of Measurement {#units-of-measurement}

For HTML and Markdown, use a nonbreaking space (&nbsp) between the number and the unit when specifying a unit of measurement. This includes most units of measurement such as distance, pixels, points, weight, and degrees of temperature (between the degree and unit of measurement). 

For currency, percent, or degrees of an angle, don’t use a space between the number and unit.

For ranges of numbers with units, repeat the unit for each number. Similarly, for rates, use “per” instead of a slash (/). 

### Linking {#linking}

#### Cross-reference Links {#cross-reference-links}

Use cross-references to guide users to additional resources. In Braze documentation, use site-root-relative URLs to link to other Braze docs (replace “www.braze.com/docs” with “{{site.baseurl}}”).

Avoid adding multiple links to the same document within a given page, as this can cause link fatigue. Duplicate links are fine in moderation if you’re linking to a specific section on another page, or if the page you’re linking from is long.

#### Embedding Videos {#embedding-videos}

Similar to images, use videos to create variety in your learning materials. Most people learn best with a combination of mediums, so make sure that any content you include in a video is also covered in the article or lesson.

To embed a video in Braze documentation, refer to [Embedded Video Test]({{site.baseurl}}/home/styling_test_page/#embedded-video-test).

#### Headings as Link Targets {#headings-as-link-targets}

In Braze documentation, anchors are automatically created for headings. However, you may want to add a custom anchor to a heading if:

* Your auto-generated anchor is very long.  
* Your heading may be frequently linked to. Adding a custom anchor reduces the likelihood of breaking links if the heading text is changed later.

To add an anchor to a heading in Braze documentation, refer to [Custom Anchors]({{site.baseurl}}/home/styling_test_page/#custom-header-anchor).

#### Link Text {#link-text}

Effective link text helps to improve the findability, discoverability, and accessibility of your content. 

##### Structuring Links {#structuring-links}

Use one of the following formats when writing links:

* Match the link text to the title or heading of the link destination.  
* Use a description of the link destination as the link text.

{::nomarkdown}
<table style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Do</th><th style="width: 50%;">Don't</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Do <br><br> <em>Match the link text to the title or heading of the link destination.</em></td><td style="width: 50%;">Do <br><br> <em>Use a description of the link destination as the link text.</em></td></tr>
<tr><td style="width: 50%;">Get started with the Braze [Web SDK]({{site.baseurl}}).</td><td style="width: 50%;">To find out your specific cluster or endpoint, [contact Support]({{site.baseurl}}).</td></tr>
<tr><td style="width: 50%;">For more information, see [Aborting Liquid Messages]({{site.baseurl}}).</td><td style="width: 50%;">When in doubt, you can always [reset your password]({{site.baseurl}}). Do Use a description of the link destination as the link text.</td></tr>
</tbody>
</table>
{:/}

You may need to rephrase a sentence to make good link text.

If you’re linking to a section on the same page, use a standard phrase that indicates this action. For example:

* On this page, see [heading].  
* In this document, refer to [heading].  
* For more information, refer to the section [heading].

##### Writing Links {#writing-links}

Apply the following guidelines when writing link text:

* Put the link in the relevant key words.  
* If you are writing a complete sentence that refers the reader to another article, use the phrase “For more information, see” or “For more information about [topic], see”.   
* Only add a "Learn more…" sentence is the help text addresses more than one concept, each of which could be linked to their own help doc. In this situation, pick the most appropriate link and contextualize it with "Learn more…"  
* To keep an informal tone, don’t use “please” to introduce link text. For example, avoid the phrase “Please refer to”, “Please see”, and “Please contact”.  
* Write unique, descriptive link text that makes sense without the surrounding text. Research by the [Nielsen Norman Group](https://www.nngroup.com/articles/link-promise/#links-should-stand-alone) (NN/g) shows that readers scan for salient information on a page, so make sure links can stand alone.  
* Don’t use the following words or phrases for link text. They’re bad for accessibility and scannability.  
 * Learn more (on its own)  
 * Click here  
 * here  
 * this document  
 * this article

{::nomarkdown}
<table style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Do</th><th style="width: 50%;">Don't</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Do <br><br> <em>Make sure the link text makes sense without the surrounding text</em></td><td style="width: 50%;">Don't <br><br> <em>Use vague or non-descriptive link text</em></td></tr>
<tr><td style="width: 50%;">For more information on importing customer data, see [User Import]({{site.baseurl}}).</td><td style="width: 50%;">For more information, [click here]({{site.baseurl}}).</td></tr>
<tr><td style="width: 50%;">This feature connects to the [Track users]({{site.baseurl}}) endpoint.</td><td style="width: 50%;">See [this article]({{site.baseurl}}).</td></tr>
<tr><td style="width: 50%;">Learn more about [what’s new in Android SDK 16.0.0]({{site.baseurl}}).</td><td style="width: 50%;">Follow the instructions [here]({{site.baseurl}}).</td></tr>
<tr><td style="width: 50%;">Learn more about the [Braze platform](https://www.braze.com/product).</td><td style="width: 50%;">For steps, refer to [this document]({{site.baseurl}}). [Learn more]({{site.baseurl}}).</td></tr>
<tr><td style="width: 50%;">Storefront API keys are unique per Hydrogen storefront, but their permission scopes are shared by all Hydrogen storefronts. Learn more about [Storefront API tokens.]({{site.baseurl}})</td><td style="width: 50%;">[Storefront API tokens]({{site.baseurl}}) are unique per [Hydrogen storefront]({{site.baseurl}}), but their [permission scopes]({{site.baseurl}}) are shared across all Hydrogen storefronts.</td></tr>
</tbody>
</table>
{:/}

#### Links for Endpoints {#links-for-endpoints}

When referencing endpoint articles, be sure to use [meaningful link text](https://docs.google.com/document/d/e/2PACX-1vTluyDFO3ZEV7V6VvhXE4As_hSFwmnFFdU9g6_TrAYTgH1QmbRoEDDdn5GzKAB9vdBbIdyiFdoaJcNk/pub#h.79ujl0qtumog) that can make sense out of context. If you’re using the endpoint’s path as a link, be sure to provide details in the surrounding text as the path may not clearly communicate the endpoint’s function.    

{::nomarkdown}
<table style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Do</th><th style="width: 50%;">Don't</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Delete user profiles using the Braze [Delete user endpoint]({{site.baseurl}}/api/endpoints/user<em>data/post</em>user_delete/).</td><td style="width: 50%;">Delete user profiles using the Braze [Delete user]({{site.baseurl}}/api/endpoints/user<em>data/post</em>user_delete/) endpoint.</td></tr>
<tr><td style="width: 50%;">[<code>/users/export/id</code> endpoint]({{site.baseurl}}/api/endpoints/export/user<em>data/post</em>users_identifier/)</td><td style="width: 50%;">[<code>/users/export/id</code>]({{site.baseurl}}/api/endpoints/export/user<em>data/post</em>users_identifier/) endpoint</td></tr>
</tbody>
</table>
{:/}

#### Links for File Download {#links-for-file-download}

If a link downloads a file, then make that clear in the link text, and mention the file type.

{::nomarkdown}
<table style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Do</th><th style="width: 50%;">Don't</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Do <br><br> <em>Make sure the link text communicates that clicking it downloads a file</em></td><td style="width: 50%;">Don't</td></tr>
<tr><td style="width: 50%;">For tips, download the [Regex Cheat Sheet PDF]({{site.baseurl}})</td><td style="width: 50%;">Check out our [RegEx Cheat Sheet]({{site.baseurl}}).</td></tr>
<tr><td style="width: 50%;">For more information, download the [Success and Support Services Handbook PDF]({{site.baseurl}})</td><td style="width: 50%;">[Success and Support Services Handbook]({{site.baseurl}})</td></tr>
</tbody>
</table>
{:/}

#### Links to Other Sites {#links-to-other-sites}

As a general rule, don’t link to another site if you can cover the information with a brief explanation. We can’t keep track of when the content on another site changes. 

If you do link to an external site, make sure that the site you link to is high quality, reliable, and respectable. If possible, link to the most relevant heading on a page.

Use an external link icon to indicate that the link goes to a different domain. For Braze documentation, this is automatically applied to external links.

#### URLs for Images {#urls-for-images}

In Braze documentation, use site-root-relative URLs to link to images. For more information, refer to [Adding and Editing Images](https://github.com/braze-inc/braze-docs/wiki/Editing-Content#adding-and-editing-images).

### Glossary {#glossary}

⚠️ = Use caution, refer to relevant notes  
⛔️ = Don’t use 

#### A

**A/B testing**

⚠️ **abort**  
Avoid using unless referring to a specifically named process. Instead, use words like “stop”, “exit”, “cancel”, or “end”.

**AccuWeather (partner)**

**action buttons**

**action-based delivery**  
Lowercase except when referring to a UI element that is capitalized. 

**Adjust (partner)**

⛔️ **ad hoc**

Don’t use. Use “one-time” or similar.

**Airbridge (partner)**

**AI item recommendation**

**Alloys / Braze Alloys**  
Always capitalized.

**alphanumeric**  
Don’t hyphenate.

**⛔️ app group**  
Don't use. App group has been renamed to workspace.

**Amazon Web Services (AWS)**  
Always capitalized. Spell out at the first mention, then it’s fine to use the acronym.

#### B

**beta**

**Bonfire / Bonfire community / Braze Bonfire community**  
Use “Braze Bonfire community” on the first mention, then it’s fine to use just “Bonfire” or “Bonfire community”.

**boolean**

⛔️ **blacklist**  
Don’t use. Instead, use “blocklist” or “denylist”. For the verb form of these words, consider rewording the sentence to remove the problematic term. For example:

✅ **Recommended:** To block an existing property from being used in new messages, click **Manage Properties**.

⛔️ **Not recommended:** To blocklist an existing property, click **Manage Properties**. 

**Bluedot (partner)**

**Branch (partner)**

**Braze-to-Braze webhook**

#### C

**California Consumer Privacy Act (CCPA)**  
Spell out at the first mention, then it’s fine to use the acronym.

**can**  
Use “can” to refer to an optional action or outcome. For example:

✅ **Recommended:** You can also upload and update user profiles via CSV files.

✅ **Recommended:** The import process can take a few minutes.

Don’t use “can” for directions. Instead, prefer the imperative verb. For examples, see [Second Person and First Person](#second-person-and-first-person).

**Canvas**  
Always capitalized. Plural is “Canvases”.

**Canvas Flow**  
Use when differentiating between the original Canvas editor and Canvas Flow. Otherwise, use “Canvas”.

**campaign**  
Lowercase except when referring to a UI element that is capitalized.

**capacity**  
Use when referring to custom data limits instead of the word "limit."

**catalog**  
Lowercase except when referring to a UI element that is capitalized.

**CCPA compliance (noun) / CCPA-compliant (adjective)**

**Census (partner)**

**Certona (partner)**

**churn**  
Use to refer to customer turnover or loss.

**churn prediction**  
Lowercase except when referring to the UI.

**Content Blocks**

**conversion group analysis**  
Lowercase.

**Currents / Braze Currents**  
Always capitalized.

**custom attributes**  
Lowercase except when referring to a UI element that is capitalized.

**custom events**  
Lowercase except when referring to a UI element that is capitalized.

**customer data platform (CDP)**  
Lowercase.

#### D

**dashboard / Braze dashboard**  
Use to refer to Braze as a platform. Use lowercase (dashboard not Dashboard).

**Digioh (partner)**

**drag and drop (verb)  / drag-and-drop (adjective)**  
Use when referring to dragging files into an upload zone.

**Drag-And-Drop Editor**  
Use title case when referring to the feature in the UI. Otherwise, use lowercase (drag-and-drop editor). Use the verb when referencing how customers can [drag and drop](#bookmark=id.neca78oj4s04) elements in the editor.

**drill down (verb) / drilldown (noun or adjective)**  
Use in content about data and the reports generated from them. 

**Dyspatch (partner)**

#### E

**early access**

⛔️ **e.g.**  
Don't use. Use the phrases “for example,“ "such as,” "like" or similar.

**eCommerce**  
Not “ecommerce” or “e-commerce”.  
*Note: Updated from "ecommerce" to "eCommerce" Feb 4, 2025*

**email**  
Not “Email” or “e-mail”.

**end user (noun) / end-user  (adjective)**  
Prefer “your users” over “end users”.

⚠️ **ensure**  
Avoid using when talking about what a feature does. Refer to [Avoid Guarantees](#bookmark=id.wcu941yo2mda) for more information.

**event prediction**

**event properties / custom event properties**  
Lowercase except when referring to a UI element that is capitalized.

**extract**  
Use “extract” instead of “unzip” to refer to extracting files from a compressed folder.

**external ID**  
Not "External ID". When referencing code snippets, use external_id. 

#### F

**Fullscreen**   
When used as an adjective (for example, "Fullscreen in-app messages"), render without the hyphen.

#### G

**GitHub**  
Not “Github” or “github”.

#### H

**High-Value Actions**

#### I

⛔️ **i.e.**  
Don't use. Use the phrase “that is” or similar.

**integer**

**Intelligence Suite**  
Use title case.

**Intelligent Channel**  
Use title case.

**Intelligent Selection**  
Use title case.

**Intelligent Timing**  
Use title case.

⛔️ **Internet of things**  
Don’t use.

#### J

#### K

⚠️ **kill**  
Avoid using unless referring to a specifically named process. Instead, use words like “stop”, “exit”, “cancel”, or “end”.

#### L

**Liquid**  
Always capitalized.

#### M

**maximum**  
Not “max”.

**media library**  
Lowercase except when referring to a UI element that is capitalized.

**multichannel campaign**  
Lowercase except when referring to a UI element that is capitalized. No hyphen.

**multi-language support**

#### N

**N/A**  
Not “NA”. Use “N/A” as needed in tables to denote column or row content that does apply to a particular cell. In inline text, prefer the spelled out “not available” or “not applicable” for clarity.

⚠️ **new**  
Avoid using in product documentation and learning material, as this can quickly date your content. For more information, see [Future Features](#describing-limitations).

#### O

**once**  
Use to refer to performing an action a single time. Don’t use “once” in place of “after”.

⛔️ **out-of-the-box**  
Don’t use. Instead, use an alternative like “default”.

#### P

**personally identifiable information (PII)**

**Personalized Path**  
Use title case.

**Personalized Variant**  
Use title case.

**preceding**

**prediction**  
Lowercase unless preceded by “Braze”, such as “A Braze Prediction is…”.

**Predictive Churn**  
Use title case. Predictive Churn is the product name, whereas customers create a [churn prediction](#bookmark=id.kjerefdp1c6z).

**Predictive Events**  
Use title case.

**Predictive Purchases**  
Use title case. Predictive Purchases is the product name, whereas customers create a [purchase prediction](#bookmark=id.ois2wxwpvgp0).

**Predictive Suite**  
Use title case.

**preference center**  
Lowercase except when referring to a UI element that is capitalized.

**promotion code**  
Lowercase except when referring to a UI element that is capitalized. Don’t use “promo code”.

**purchase prediction**  
Lowercase except when referring to a UI element that is capitalized.

**purchase properties**  
Lowercase except when referring to a UI element that is capitalized.

**push action buttons**

**Push Max**  
Use title case.

**Push Stories**  
Use title case.

#### Q

**Q&A**

⛔️ **QA (quality assurance)**  
Do not use the acronym as a verb. Instead, rewrite as “perform quality assurance”.

**Quiet Hours**

⚠️ **quick / quickly**  
Avoid using. What is quick for you may not be quick for others. For related guidelines, refer to [Condescending Language](#condescending-language).

#### R

**re-engagement**

⚠️ **regular expression / regex**  
Prefer the spelled-out version over its abbreviated “regex”. Don’t use “RegEx”.

#### S

⛔️ **sanity check**  
Don’t use. Instead, use a term like “quick check” or “preliminary check”. Alternatively, introduce check-in instructions with a phrase like “Let's check to make sure everything is working”.

**scheduled delivery**  
Lowercase except when referring to a UI element that is capitalized.

**segment (audience)**

**Segment (partner)**  
Always capitalized.

**Segment Extensions**  
Use title case.

**Segment Insights**  
Use title case.

**selection**  
As in, the feature within catalogs. Lowercase except when referring to a UI element that is capitalized.

**simple survey**

**Snowflake (partner)**

**software as a service (SaaS)**   
Spell out at the first mention, then it’s fine to use the acronym.

**SQL Segment Extensions**  
Use title case.

**stickiness**

**string**  
For non-technical audiences, define a string as text that contains “alphanumeric characters”. For technical audiences, it’s fine not to define this term.

**subscription group**

#### T

⚠️ **terminate**  
Avoid using unless referring to a specifically named process. Instead, use words like “stop”, “exit”, “cancel”, or “end”.

**time zone**  
Not "timezone".

#### U

⛔️ **unzip**  
Don’t use. Instead, use “extract”.

**URL**  
Pronounced as the individual letters U-R-L, so write “a URL” rather than “an URL”. Use all caps. For plurals, use URLs.

**user attributes / default user attributes**  
Use to refer to user data automatically captured by Braze.

⚠️ **utilize**  
Don’t use “utilize” when you mean “use”. Use “utilize” to refer to something being used beyond its original intended purpose. 

#### V

**variant**

⛔️ **via**  
Don’t use. Instead, use terms like “through” or phrases like “by means of” or “by way of”.

⛔️ **vice versa**  
Don’t use. Instead, use terms like “conversely” or a phrase like “the other way around”. 

**view-only**

**Vizbee (partner)**

**Voucherify (partner)**

⚠️ **vs.**  
Don’t use “vs.” as an abbreviation for “versus”. Instead, spell out the word.

#### W

**web messaging**

**web push**

**webhook**

**whitelabel**

⛔️ **whitelist**  
Don’t use unless referring to the UI. Instead, use “allowlist” or “safelist”. For the verb form of these words, consider rewording the sentence to remove the problematic term. For examples, see [blacklist](#bookmark=id.6p79y0jm7jt9).

⚠️ **Wi-Fi**  
Don’t use “WiFi”, “wi-fi”, or “wifi”.

**will**  
Avoid using “will” or “would”. See [Present Tense](#present-tense).

**Winning Path**  
Use title case.

**Winning Variant**  
Use title case.

⛔️ **wizard**  
Don't use. Instead, use "composer".

**workspace**

#### X

**Xamarin (partner)**

#### Y

**YAML**  
Don’t use a file extension to refer to the type of file. For example, use “YAML file” instead of “.yaml file”.

**YouTube**

#### Z

**Zapier (partner)**

**Zendesk (partner)**

**zip code**

**ZIP**  
Don’t use a file extension to refer to the type of file. For example, use “ZIP file” instead of “.zip file”.

## Image copy style guide {#image_style_guide}

**Image Styling Tools:** Use [Skitch](https://evernote.com/products/skitch) (available free through Evernote) for applying image styling (blurring, emphasizing image components, cropping).

**Don’t embed important text inside images:** Avoid embedding text inside images as not all users can read English text (and page translation tools do not translate images). This text should be provided in the article. Provide alt text for images for maximum accessibility for users.

{::nomarkdown}
<table style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Do</th><th style="width: 50%;">Don't</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">![Example of correctly not embedding text in an image.]({% image_buster /assets/img/contributing/style_guide/embed_text_do.png %})</td><td style="width: 50%;">![Example of incorrectly embedding text in an image.]({% image_buster /assets/img/contributing/style_guide/embed_text_dont.png %})</td></tr>
</tbody>
</table>
{:/}

**Optimize placement and sizing:** Whenever possible, place images near relevant text and be mindful to use image styling markdown to resize larger images. For some content, this should be done by [anchoring text to the left or right side of the page]({{site.baseurl}}/home/styling_test_page/#image-test) depending on the image and the space available. 

{::nomarkdown}
<table style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Do</th><th style="width: 50%;">Don't</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">![Example of correctly optimizing image placement.]({% image_buster /assets/img/contributing/style_guide/optimize_placement_do.png %})</td><td style="width: 50%;">![Example of incorrectly optimizing image placement.]({% image_buster /assets/img/contributing/style_guide/optimize_placement_dont.png %})</td></tr>
</tbody>
</table>
{:/}

**Cropping**: Crop relevant sections closely. Unless necessary, do not include the left navigation bar and instead include navigation directions in the article. This limits the number of images that need to be changed when UI changes occur. 

{% alert note %}

If you are going to capture a dashboard element, crop without including the border. See [Cropping Images continued]({#cropping_continued}) for expanded examples.

{% endalert %}

{::nomarkdown}
<table style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Do</th><th style="width: 50%;">Don't</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">![Example of a properly cropped image.]({% image_buster /assets/img/contributing/style_guide/cropping_do_1.png %})</td><td style="width: 50%;">![Example of an incorrectly copped image.]({% image_buster /assets/img/contributing/style_guide/cropping_dont_1.png %})</td></tr>
<tr><td style="width: 50%;">![Example of a properly cropped image.]({% image_buster /assets/img/contributing/style_guide/cropping_do_2.png %})</td><td style="width: 50%;">![Example of an incorrectly cropped image.]({% image_buster /assets/img/contributing/style_guide/cropping_dont_2.png %})</td></tr>
</tbody>
</table>
{:/}

**Censorship**: Blur sensitive information like names, emails, and API keys. Blurring can be done through Skitch.

{::nomarkdown}
<table style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Do</th><th style="width: 50%;">Don't</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">![Example of correct blurring.]({% image_buster /assets/img/contributing/style_guide/censorship_do.png %})</td><td style="width: 50%;">![Example of incorrect blurring.]({% image_buster /assets/img/contributing/style_guide/censorship_dont.png %})</td></tr>
</tbody>
</table>
{:/}

**Emphasizing Components of Images:** Do not emphasize components of images unless necessary. Use blue squares (the most colorblind-friendly option) with a thin-medium thickness to highlight different components of images, this can be done through skitch. Make sure the “highlighted sections” do not obstruct the normal UI. Absolutely no skitch arrows

{::nomarkdown}
<table style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Do</th><th style="width: 50%;">Don't</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">![Example of correctly emphasizing components in an image.]({% image_buster /assets/img/contributing/style_guide/emphasis_do_1.png %})</td><td style="width: 50%;">![Example of incorrectly emphasizing components in an image.]({% image_buster /assets/img/contributing/style_guide/emphasis_dont_1.png %})</td></tr>
<tr><td style="width: 50%;">![Example of correctly emphasizing components in an image.]({% image_buster /assets/img/contributing/style_guide/emphasis_do_2.png %})</td><td style="width: 50%;">![Example of incorrectly emphasizing components in an image.]({% image_buster /assets/img/contributing/style_guide/emphasis_dont_2.png %})</td></tr>
</tbody>
</table>
{:/}

**Cropping Explanation continued** {#cropping-continued}
Because Braze docs already add a border to each image, omit borders in a section screenshot. We are looking for a clean crop. The border can be left in if there are components that live outside or within the border, see the third image for example.

**Do:**
![Example of correctly cropping an image.]({% image_buster /assets/img/contributing/style_guide/cropping_do_3.png %})

**Don’t:**  
![Example of incorrectly cropping an image.]({% image_buster /assets/img/contributing/style_guide/cropping_dont_3.png %})
  
**Do:**  
![Example of correctly cropping an image.]({% image_buster /assets/img/contributing/style_guide/cropping_do_4.png %})

## Alerts (best practices) {#alerts}

### Best Practices for Alerts {#best-practices-for-alerts}

This document contains information, general guidelines, and examples for alert types used in Braze documentation. 

### Alert Types {#alert-types}

Alerts categorize information that a reader should be aware of. There are four alert types that can be used in our documentation:

* Important  
* Note  
* Tip  
* Warning

### When to Use an Alert {#when-to-use-an-alert}

Use alerts to draw a reader’s attention to important information. Keep the content short and to the point. We want to make sure that information sticks with the reader.

Refer to the following table for definitions of each alert:

| Alert Type | Definition |
| :---- | :---- |
| Important | Includes essential information that **should** be addressed by the reader, such as: {::nomarkdown}<ul><li>Deprecated features</li><li>Impacts on billing</li><li>Information pertaining to relevant updates</li><li>Pressing feature caveats (ex: beta features)</li><li>Other important tidbits of information</li></ul>{:/} |
| Note | Includes one-off information that the reader should know, such as: {::nomarkdown}<ul><li>Feature caveats</li><li>Formatting guidance</li><li>Helpful callouts</li><li>Information that is demoted from an Important alert due to the alert’s content dropping in severity (ex: a long-standing important alert shifting to a standard note)</li></ul>{:/} |
| Tip | Includes supplementary knowledge and recommendations for the reader to be aware of, such as: {::nomarkdown}<ul><li>Additional troubleshooting articles</li><li>Steps and shortcuts that help increase usability (ex: additional customization for in-app messages)</li></ul>{:/} |
| Warning | Includes essential information that a reader must address and can include: {::nomarkdown}<ul><li>Irreversible consequences (ex: Campaign and Canvas deletion)</li><li>Feature-breaking behavior</li><li>Loss of data</li><li>Other crucial warnings</li></ul>{:/} |

**Alert Best Practices**  
Here are general guidelines and best practices for alerts. 

As a general rule of thumb, avoid using alerts for content that is essential to the article structure (like feature introductions, setup instructions, and steps to use a feature.). When in doubt, consult with the team during peer review.

| Guideline | Example |
| :---- | :---- |
| Explain the information in the alert in a clear, concise statement.  | ![An alert with a clear, concise statement.]({% image_buster /assets/img/contributing/style_guide/alert_1.png %}) <br><br> [Note alert in Step 4: Add Filters to Your Segment Section]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/#step-4-add-filters-to-your-segment) |
| For alerts that apply to different sections of the same article, consider creating a new section that captures these details to avoid repetitive content. | ![Example of a new section instead of an alert.]({% image_buster /assets/img/contributing/style_guide/alert_2.png %}) <br><br> [Property Details header in Push Send Events Section]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/message_engagement_events) |
| Separate the information into short paragraphs or lists within the alert. | ![Example of separating the information into short paragraphs.]({% image_buster /assets/img/contributing/style_guide/alert_3.png %}) <br><br> [Important alert in Canvas Persistent Entry Properties]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_persistent_entry_properties/#using-entry-properties) |
| Consider any additional formatting that may impact how the alert displays (code snippets, steps, surrounding images, and more.). | ![An alert code styling.]({% image_buster /assets/img/contributing/style_guide/alert_4.png %}) <br><br> [Important alert in Step 2: Add Code Snippet to Email Body]({{site.baseurl}}/partners/message_orchestration/channel_extensions/loyalty/voucherify/#step-2-add-code-snippet-to-email-body) |
| Include a line break for alerts that begin an article. | ![Example of an alert beginning an article.]({% image_buster /assets/img/contributing/style_guide/alert_5.png %}) <br><br> [Content Card Implementation Guide]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/implementation_guide/) |
| When writing about beta features, include an Important alert that calls out the beta status and related Braze contact information.  Place this beta alert after the overview text and before the first main heading. | ![Example of an important alert for a beta feature.]({% image_buster /assets/img/contributing/style_guide/alert_6.png %}) <br><br> [Canvas Persistent Entry Properties]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_persistent_entry_properties/)  |
| Avoid using two or more alerts in a row if possible. Instead, reorganize or include the information as part of the text instead. | ![An example of two alerts next to each other, which you should avoid.]({% image_buster /assets/img/contributing/style_guide/alert_7.png %}) <br><br> [Setting User IDs]({{site.baseurl}}/developer_guide/platform_integration_guides/fireos/analytics/setting_user_ids/) |
| If you find your alert is lengthy, consider creating a new section that includes the information as a list. For example, instead of including troubleshooting steps in an alert, consider creating a troubleshooting section or providing a link to a related article.  | ![Example of a new section of content.]({% image_buster /assets/img/contributing/style_guide/alert_8.png %}) <br><br> [Tip alert in Canvas and Campaign Tag Differences Section]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/) |

### Alert Examples {#alert-examples}

Refer to the following examples for how and why each alert type is used in our documentation. 

### Important Alert  {#important-alert}

{% include alerts/important_alerts.md alert='Web push private browsing' %}

* **Article:** [Push for Web]({{site.baseurl}}/user_guide/message_building_by_channel/push/web/)
* **Use Case:** Includes essential feature caveat that the reader should know as they set up their web push.
* **Alert Reasoning:** Use an Important alert as opposed to a Note alert because the content's importance is greater for a reader to know as they set up their web push.

{% include alerts/important_alerts.md alert='BCC address billable emails' %}

* **Article:** [Email Settings]({{site.baseurl}}/user_guide/administrative/app_settings/email_settings/)
* **Use Case:**
  - Provides important feature caveat about the possibility of doubling billable emails
  - Redirects reader to contact their Customer Success Manager as needed
* **Alert Reasoning:** The Important alert is used here to communicate details about the BCC addresses in their email settings. This information is best presented using an Important alert as opposed to a Warning alert because omitting this information does not impact the feature irreversibly (feature breaking, permanent data loss, etc.).

{% multi_lang_include alerts/important_alerts.md alert='Android notification priority' %}

* **Article:** [Advanced Campaign Settings]({{site.baseurl}}/user_guide/message_building_by_channel/push/android/advanced_campaign_settings/#notification-display-priority)
* **Use Case:** Includes pressing feature caveat about the Notification Priority. Redirects the reader to new information that's available.
* **Alert Reasoning:** The Important alert is best used here to redirect the reader to current information and to highlight that the section is applicable only to certain users. It's also placed after the section header, which forces the user to address the important alert before reading the rest of the section.

### Note Alert {#note-alert}

{% include alerts/note_alerts.md alert='Content Cards frequency capping' %}

* **Article:** [Create a Content Card]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/create/)
* **Use Case:** Includes additional information that a reader should be aware of as they learn more about Content Cards.
* **Alert Reasoning:** This Note alert provides background information on how Braze cycles older Content Cards for users. This is helpful, supplemental information for the reader to be aware of and does not require the use of an Important or Tip alert.

{% include alerts/note_alerts.md alert='Custom Attributes time attribute' %}

* **Article:** [Custom Attributes]({{site.baseurl}}/user_guide/data/activation/custom_data/custom_attributes/)
* **Use Case:** Includes general information that a reader should be aware of. Provides an article to learn more about related content (time attributes).
* **Alert Reasoning:** This information is best relayed using a Note alert as opposed to an Important alert because the content is directed to provide general information. Disregarding this information would not impact the ease of use for this feature.

{% include alerts/note_alerts.md alert='Manage custom data storage' %}

* **Article:** [Manage Custom Data]({{site.baseurl}}/user_guide/data/activation/custom_data/managing_custom_data/#managing-properties)
* **Use Case:** Includes general information that a reader should be aware of. Redirects to Braze contact for further information.
* **Alert Reasoning:** This Note alert provides additional information about data storage that would be helpful for a reader to know as they manage their custom attributes. However, the content does not require a stronger indication of importance to the reader, so a Note alert is acceptable here.

### Tip Alert {#tip-alert}

{% include alerts/tip_alerts.md alert='SMS segment calculator' %}

* **Article:** [SMS and RCS Billing Calculators]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/segments/)
* **Use Case:** Includes tool for the reader to understand their message length and SMS segment count. Provides information that may be helpful for the reader in their understanding of copy limits.
* **Alert Reasoning:** This is a lengthy Tip alert because it provides a space for entering the copy to see how many segments a message dispatches. The Tip alert is the best option here because this is a helpful generator for the reader to use in the process of setting up their SMS messages.

#### Example 2
{% include alerts/tip_alerts.md alert='Export troubleshooting' %}

* **Article:** [Export KPIs for Daily App Uninstalls by Date]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_uninstalls_date/)
* **Use Case:** Provides troubleshooting advice when using this endpoint.
* **Alert Reasoning:** The Tip alert provides additional support for the reader. Use a Tip alert as opposed to a Note alert because the focus of the content is to assist the reader by providing the troubleshooting article.

### Warning Alert {#warning-alert}

{% include alerts/warning_alerts.md alert='User profile external_id' %}

* **Article:** [User Profile Lifecycle]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle/)
* **Use Case:** Indicates something that the reader should not do when creating their user profiles in Braze.
* **Alert Reasoning:** The Warning alert is used to caution the reader against assigning an external_id before uniquely identifying them. This information is best relayed using a Warning alert as opposed to an Important alert because it includes irreversible consequences for the user profile.

{% include alerts/warning_alerts.md alert='Segment Currents multiple connectors' %}

* **Article:** [Segment for Currents]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/segment/segment_for_currents/)
* **Use Case:** Cautions the reader when creating Currents connectors. Includes the consequence of incorrectly creating these connectors.
* **Alert Reasoning:** The Warning alert is best used here to describe the limitations of the Braze Segment Currents integration. Use a Warning alert as opposed to an Important alert because creating more than one of the same Currents connectors incorrectly may result in losing data.

{% include alerts/warning_alerts.md alert='Canvas race condition audience trigger' %}

* **Article:** [Create a Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/)
* **Use Case:** Lists the information that may cause the feature to not work. Details how the intended audience may not receive the campaign or enter the Canvas.
* **Alert Reasoning:** The Warning alert is used here to note how the feature may work incorrectly. This information is best relayed using a Warning alert as opposed to an Important alert because the information is critical and may result in breaking the Canvas delivery.

## Braze API endpoint documentation guidelines {#api-endpoint-documentation-guidelines}

In general, documentation for API endpoints should follow the guidelines indicated in the [General guidelines](#general-guidelines). However, there are niche topics that may require different content guidelines listed in this document. 

Braze supports the following REST API methods:

* GET  
* DELETE  
* PATCH  
* POST  
* PUT

### Creating a new endpoint article

When creating a new endpoint article, be sure to also add this endpoint into the [Braze API guide]({{site.baseurl}}/api/home) so that the endpoint is searchable. Navigate to  **`_docs`** folder  **`> _api`** folder **`> home.md`** file to add the endpoint by its path and a one-sentence description.

### Referencing endpoints

In general, there isn't a clear convention for referring to endpoints in documentation. When referring to Braze endpoints, use your best judgment to determine how to refer to an endpoint depending on your use case. 

You can refer to an endpoint by its path (for example, `/users/track`) or by the endpoint's name appended with the word "endpoint" (for example, the track user endpoint). If you find that your path is especially long, refer to the endpoint name instead. 

Use sentence styling when referring to the endpoint by its name. Use code text when referring to the endpoint by its path.

Don't capitalize the word "endpoint" unless directly referring to a section name. Don't include the word "API" when directly referencing an endpoint. 

There are instances where an endpoint is referred to as an API. For example, this is an accurate statement: "Braze uses a REST API with many endpoints" when speaking generally about Braze endpoints.

Don't put quotation marks around the endpoint name. Don't use plain text when referring to the path.

{::nomarkdown}
<table style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Do</th><th style="width: 50%;">Don't</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Use the Generate preference center URL endpoint to complete the next steps.</td><td style="width: 50%;">Use <code>/preference_center/v1/{preferenceCenterExternalId}/url/{userId}</code> to complete the next steps.</td></tr>
<tr><td style="width: 50%;">Use the <code>/users/track</code> endpoint.</td><td style="width: 50%;">Use the "Users Track" API endpoint.</td></tr>
</tbody>
</table>
{:/}

#### Linking to endpoint articles

When referencing endpoint articles, be sure to use [meaningful link text](#writing-links) that can make sense out of context. If you're using the endpoint's path as a link, be sure to provide details in the surrounding text as the path may not clearly communicate the endpoint's function.    

{::nomarkdown}
<table style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Do</th><th style="width: 50%;">Don't</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Delete user profiles using the Braze <a href="{{site.baseurl}}/api/endpoints/user_data/post_user_delete/">Delete user endpoint</a>.</td><td style="width: 50%;">Delete user profiles using the Braze <a href="{{site.baseurl}}/api/endpoints/user_data/post_user_delete/">Delete user</a> endpoint.</td></tr>
<tr><td style="width: 50%;"><a href="{{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/"><code>/users/export/id</code> endpoint</a></td><td style="width: 50%;"><a href="{{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/"><code>/users/export/id</code></a> endpoint</td></tr>
</tbody>
</table>
{:/}

### Headings

The introduction of an endpoint article must include the following information:

* Request type and endpoint path URL  
* A brief description of the endpoint, starting with "Use this endpoint to…"  
* "See me in Postman" link  
* A note alert with the required REST API key permission

Use this checklist to ensure that the proper headings (and content) are included in each endpoint article and in the listed sequence. Note that there may be subheadings unique to an endpoint, such as different types of example requests.

* Rate limit  
* Path parameters  
* Request body  
* Request parameters  
* Example request  
* Response parameters  
* Example response  
* Troubleshooting (if applicable)

Refer to [Headings and Titles](#headings-and-titles) for formatting guidelines. 

#### Path parameters

If there are path parameters for the endpoint, include a Path parameters header and table (similar to the Request parameters table)

If there are no path parameters for the endpoint, include a Path parameters header and the following callout: "There are no path parameters for this endpoint."

If there are no path or request parameters for the endpoint, merge the caveat into the same section as shown below.

{% raw %}
{::nomarkdown}
<div style="margin-left: 2em;">
## Path and request parameters <br>
There are no path or request parameters for this endpoint.
</div>
{:/}
{% endraw %}

### Naming conventions

Start each endpoint name with an active verb after its method. This lets users know the function of the endpoint immediately. 

Don't use the API method as the leading verb for the endpoint name.

{::nomarkdown}
<table style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Do</th><th style="width: 50%;">Don't</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">POST: Create new user alias</td><td style="width: 50%;">POST: New user alias</td></tr>
<tr><td style="width: 50%;">GET: Look up an existing dashboard user account</td><td style="width: 50%;">GET: Existing dashboard user account</td></tr>
</tbody>
</table>
{:/}

Exceptions to this naming convention are the endpoints in the [Export section]({{site.baseurl}}/api/endpoints/export) as the section name is a verb that indicates that the listed information can be exported.

### API key permissions

API key permissions are permissions you can assign a user or group to limit their access to certain API calls. For each endpoint documentation, include the following callout after the Postman documentation link: 

> To use this endpoint, you must generate an API key with the `permission_name_here` permission.

To find the full list of API key permissions, go to **Settings > API Keys** under **Setup and Testing** in the Braze dashboard. Select an API key with full access (the key name usually includes the phrase "full access"). Each permission name should generally match the endpoint name.

Note that SCIM endpoints do not have listed API key permissions since they're specific to the SCIM integration that occurs outside of the developer console. 

### Rate limits

In general, your rate limit should specify the number of requests and the allotted time. 

Be mindful of endpoints that share a total rate limit. For example, all asynchronous catalog item endpoints share a total rate limit, so it's important to indicate that in the respective articles.

#### How to update rate limit file

If your endpoint documentation requires updating or listing a new rate limit, go to **_docs > _api > api_limits.md** to make edits to the rate limit.

### Parameters

Define both the request and response parameters in two separate tables.  These tables should contain the following columns:

* **Parameter**  
* **Required**  
* **Data Type**  
* **Description**

When directly referring to an endpoint's parameters and when listing the values in the **Parameters** column, use code text. When listing the values in the **Required**, **Data Type**, and **Description** columns, use initial caps. 

#### Placeholder text

For placeholder text, use curly brackets with a brief description of what the user should include. 

For API key placeholders, use YOUR_REST_API_KEY, not YOUR-REST-API-KEY.

{::nomarkdown}
<table style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Do</th><th style="width: 50%;">Don't</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;"><code>/preference_center/v1/{preferenceCenterExternalId}/url/{userId}</code></td><td style="width: 50%;"><code>/preference_center/v1/[preferenceCenterExternalId]</code></td></tr>
<tr><td style="width: 50%;"><code>/scim/v2/Users/{userId}</code></td><td style="width: 50%;"><code>/url/[userId]/scim/v2/Users/userID</code></td></tr>
</tbody>
</table>
{:/}

For API key placeholders, use `YOUR_REST_API_KEY` (with underscores), not `YOUR-REST-API-KEY` (with hyphens).

### Requests and responses

An API request includes the header and request parameters. The request parameters should be formatted like this:

```bash
parameter": (required/optional, data type) A brief description
```

Here's an example of a request body for the [Create new user alias endpoint]({{site.baseurl}}/api/endpoints/user_data/post_user_alias/):

```bash
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
{
  "user_aliases": (required, array of new user alias object)
}
```

Use double straight quotation marks (" ") to identify parameters that are strings or arrays in an example request. Ensure that all open brackets and parentheses are closed.

An API response includes the response body, headers, and the HTTP status code. Always include an example response. This example must include a simple text example that describes the parameter. Here's an example response for the [Update user alias endpoint]({{site.baseurl}}/api/endpoints/user_data/post_users_alias_update/#example-request).

```bash
curl --location --request POST 'https://rest.iad-01.braze.com/users/alias/update' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
  "alias_updates" :[
    {
      "alias_label": "example_alias_label",
      "old_alias_name" : "example_old_alias_name",
      "new_alias_name" : "example_new_alias_name"
    }
  ]
}'
```

#### Status and error codes 

Status codes indicate whether a user's specific request has been successfully completed. It can be helpful to include the status codes for users to know what's considered a success. For example, 400 and 404 can be indicators of an error response for the endpoint.

If your endpoint documentation requires listing out error codes, link out to the [API Error and Responses]({{site.baseurl}}/api/errors/) article instead at **_docs** folder  **> _api** folder **> errors.md** file

### Sample code

Sample code, like sample requests and responses, should be able to be copied and used with minimal work. With the exception of placeholder text (for example, the API key in the header), example requests should work as-is. Use Postman to ensure that your request is formatted correctly. 

#### Beautify vs. minified code

If the endpoint's request contains a body, beautify the example in Postman. This makes it easier for developers learning Braze conventions to understand each piece of the request.  

If the endpoint's request body is very short or does not contain a body, minify the request so that unnecessary whitespace is removed. Use a tool like [JSON Minifier](https://codebeautify.org/jsonminifier) to do this. 

#### Inline comments

Use two forward slashes (//) to indicate single-line comments in example code. 

Inline comments are valuable tools to call a user's attention to a specific section of code, explain the function of a code block, or provide additional context. 

Use inline comments to quickly show where a user's logic layer would be placed and how it would reference the SDK code. Use simple but realistic examples. For example, an example attribute of "favorite_movie" is stronger than "example_attribute." Even if the user's business doesn't track or care about an end user's favorite movie, this example shows the *sorts* of use cases that might be tracked through this attribute. Generic examples fail to elicit the same intuitive understanding.

Avoid inline comments that simply restate human-readable code or method names. Instead, use a variety of synonyms for the Braze-specific methods and parameters to provide scaffolding for non-native English speakers. 

In general, adhere to standard English conventions when providing inline comments. For example, begin sentences with a capital letter, spell out words completely, and so on.

### Additional resources

* [Google developer documentation style guide](https://developers.google.com/style)  
  * [API reference code and comments](https://developers.google.com/style/api-reference-comments)
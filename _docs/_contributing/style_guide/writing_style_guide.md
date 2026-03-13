---
nav_title: Braze Docs Style Guide
article_title: Braze Docs Style Guide
description: "Writing style guide for Braze Docs."
page_order: 0
noindex: true
---

# Braze Docs style guide

## Writing style guide

<style>
.style-guide-table td {
  overflow-wrap: break-word;
  word-break: break-word;
  min-width: 0;
}
</style>

### General guidelines {#general-guidelines}

#### Voice and tone {#voice-and-tone}

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

##### Language and formatting

* Use [plain language](https://www.plainlanguage.gov/guidelines/).  
* Front-load sections with the most important information. Use the journalism model of the [inverted pyramid](https://en.wikipedia.org/wiki/Inverted_pyramid_(journalism)).  
* Break up walls of text to help readers scan for information. Use paragraphs, [lists](#lists), [callouts](#callouts-and-alerts), and [images](#figures-and-other-images) to improve readability.  
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

##### Images, videos, and GIFs

* Provide [alt text](#alt-text) for every image that summarizes the information presented in the image.  
* Don’t use images as the only way to show information. Always provide the steps, content, or other details presented in the image in the surrounding text.  
* Don’t use images of terminal output, code samples, or text. Instead, use actual text.   
* Provide captions for video content.  
* Don’t use flashing elements in videos or GIFs.

##### Tables {#tables-1}

* Always use an introductory sentence to describe the purpose of the table.   
* Avoid tables in the middle of a list, especially a list of steps.

#### Global audience {#global-audience}

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
  * Use diverse [example names](#example-names).  
  * Avoid culturally specific humor.

#### Inclusive language {#inclusive-language}

We may be a B2B company, but people are at the center of what we do, and ours is a global brand. Whenever we refer to a person in our content, we are mindful of being inclusive and considerate. When in doubt, consult this section or [The Diversity Style Guide](https://www.diversitystyleguide.com/).

##### Age

Unless it’s relevant to your writing, don’t refer to a subject’s age. Don’t use qualifiers like “young” or “old” to describe any subject or audience. 

If you’re representing an age group, be descriptive and specific like “Generation Z” instead of “youth.” Don’t use vague descriptors like “college-age” when you could say “college students” instead.

##### Color

Avoid including color terms in your writing unless absolutely necessary, and if necessary, include explanatory text. 

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
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

##### Condescending language {#condescending-language}

When writing instructions or detailing steps for a reader to follow, avoid using words or phrases such as:

* simple, like “Creating a campaign is simple.”  
* simply, like “...simply add X into Y”  
* just, like “...just install X”  
* “It’s easy”

If someone has difficulty with the steps or instructions, your casual descriptors can feel condescending. You may also unintentionally exclude people from your documentation who interpret that as an indicator they are in some way not skilled enough to follow your instructions.

##### Customers versus clients

When referring to company users and their consumers, use the following terms accordingly:

* **Customers:** Brands we work with. Never refer to our customers as “clients”.  
 * **Company users:** In the context of documentation, when it is important to distinguish between users of the platform and the end users who receive marketing messages, use "company users".  
* **Consumers:** Customers of a brand we work with.   
* **Users:** Generally reserved for a specific statistic that depends on “user” metrics (such as “user retention”). When referring to “users” in our content, first aim to be more specific. Think shoppers, consumers, patients, players.

##### Departments and teams

Capitalize the names of departments or teams. Do not capitalize “team” or “department.”

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
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
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
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


##### Inclusivity in content

Highlight and represent a diverse community. Be mindful and inclusive when involving our customers, speakers, industry experts, and Braze team members. 

##### Job titles

When it comes to job titles, we veer off-course from AP Style. In all cases, we capitalize job titles when referring to someone specifically. 

###### Job title with company name

Capitalize formal job titles when they come before or after a person’s name. We format them three ways:

1. **[Formal Title]** at **[Company Name]** + **[Full Name]**

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
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
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
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
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Do</th><th style="width: 50%;">Don't</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">PantsLabyrinth Creative Director David Bowie</td><td style="width: 50%;">PantsLabyrinth creative director David Bowie</td></tr>
</tbody>
</table>
{:/}

###### Job title without company name

When referring to a specific person by formal title, capitalize their formal title and name like so:

1. **[Formal Title]** + **[Full Name]**

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
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
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
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
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
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
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
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

##### Mental health

Mental health and illness cover a broad range of conditions. Unless it’s relevant to what you are writing, don’t refer to a person’s mental health. Avoid stigmatizing words and phrases. Don’t use medical terms colloquially (example: “The depressing state of things...”).

##### Names

The first time you mention a person, use their first and full name. From there on, use either their first or last name when referring to them.

##### Pronouns

For information on appropriate use of pronouns, refer to the Language and Grammar section on [Pronouns](#pronouns).

##### Race, religion, and ethnicity

Don’t refer to a person’s race, religion, or ethnicity unless it’s relevant to what you are writing. In writing where race or ethnicity factors in, ask your subject how they self-identify.

Don’t use a hyphen to indicate dual heritage or religion. Instead, use a space.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
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
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
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
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
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

#### Third-party sources {#third-party-sources}

Never copy content from other sites, as it may violate copyright. Content can be both text and images.

Instead of copying or quoting third-party sites, paraphrase the content or provide a link to the third-party site for more information.  For more information, refer to [Links to Other Sites](#links-to-other-sites).

### Language and grammar {#language-and-grammar}

Keeping in line with agreed-upon grammar and mechanics helps us keep our writing clear and consistent. This section covers what we try to follow in our technical documentation unless specified otherwise.

#### Abbreviations {#abbreviations}

Abbreviations, such as acronyms, initialisms, and shortened words, can hurt our clarity, voice, and SEO. 

Although some abbreviations are widely understood, others aren't well known or are familiar only to a specific group of customers. Use your best judgment, and as a general rule, it’s OK not to spell out an abbreviation if it’s listed in the [American Heritage Dictionary](https://ahdictionary.com/).

If an abbreviation isn’t well known, spell it out on the first mention, followed by the abbreviation in parentheses. For all subsequent mentions of the term, use the abbreviation.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Do: <em>Spell out uncommon abbreviations at the first mention</em></th><th style="width: 50%;">Don't: <em>Spell out common abbreviations</em></th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Top-level domain (TLD)</td><td style="width: 50%;">Portable Document Format (PDF)</td></tr>
<tr><td style="width: 50%;">Universally unique identifier (UUID)</td><td style="width: 50%;">Universal Serial Bus (USB)</td></tr>
</tbody>
</table>
{:/}


Treat abbreviations as regular words when making them plural, and don't add an apostrophe—for example, APIs and SDKs. The same goes for which article (a or an) you use—look at how you pronounce the abbreviation. When an abbreviation begins with a vowel sound, use “an”; for consonant sounds, use “a”. 

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 100%;">Do: <em>Use articles depending on how the abbreviation is pronounced, not spelled</em></th></tr>
</thead>
<tbody>
<tr><td style="width: 100%;">an ISP</td></tr>
<tr><td style="width: 100%;">a DLL</td></tr>
<tr><td style="width: 100%;">an HTML site</td></tr>
<tr><td style="width: 100%;">a CSV file</td></tr>
</tbody>
</table>
{:/}

#### Active voice {#active-voice}

We use the active voice at Braze when possible. Active voice is our gold standard. Avoid passive voice, in which it can be difficult to determine who or what is performing a particular action.

To see if your sentence is in a passive voice, insert “by somebody” after the verb. If the sentence makes sense—it’s most likely in the passive voice.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Do: <em>Use active voice</em></th><th style="width: 50%;">Don't: <em>Use passive voice, if possible</em></th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Braze connects consumers to the brands they love.</td><td style="width: 50%;">Consumers are connected to the brands they love.</td></tr>
<tr><td style="width: 50%;">Braze requires employees to keep their addresses up to date.</td><td style="width: 50%;">Employees are required to keep their addresses up to date.</td></tr>
<tr><td style="width: 50%;">Company administrators can configure authentication requirements for signing into Braze.</td><td style="width: 50%;">Authentication requirements for signing into Braze can be configured by company administrators.</td></tr>
</tbody>
</table>
{:/}

##### Exceptions

It’s OK to use passive voice in the following cases:

* To de-emphasize a subject, generally to avoid blaming the reader:  
  - **Do:** Two errors were found in the email.  
  - **Don’t:** You created two errors in the email.  
* If knowing who is responsible for the action isn’t important:  
  - **Do:** This article was last updated in December 2020.

#### Articles {#articles}

Use the articles “a”, “an”, and “the” to make your writing clear and to aid in translation. Use “the” before a specific singular or plural noun, and “a” or “an” before a non-specific singular noun.

To determine if you should use “a” or “an”, look at the pronunciation of the word that follows it. Use “a” before a consonant sound, and use “an” before a vowel sound. The same guidelines apply to [Abbreviations](#abbreviations).

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 100%;">Do: <em>Use articles depending on how the anteceding word is pronounced.</em></th></tr>
</thead>
<tbody>
<tr><td style="width: 100%;">an hour</td></tr>
<tr><td style="width: 100%;">a minute</td></tr>
<tr><td style="width: 100%;">an FAQ article</td></tr>
<tr><td style="width: 100%;">a LAB course</td></tr>
</tbody>
</table>
{:/}

#### Pronouns {#pronouns}

##### Personal pronouns

Use second-person pronouns (you) whenever possible. 

Don’t refer to Braze customers as the “user” in external-facing writing, instead speak directly to the reader using “you”. To refer to our customers’ customers, use “your consumers” or, if the situation relates to user statistics, “your users”.

Avoid first-person pronouns (I, we, us, our) except in the following cases:

* Entries in FAQs. For example, “How do I reset my password?”.  
* Using “we” to refer to Braze as an organization.   
 * If it may be unclear who “we” is referring to, first refer to Braze by name, then use “we” in subsequent mentions.

##### Gender-neutral pronouns

Use the pronouns your subjects use. If there is any uncertainty, use “they,” “them,” and “their” for singular pronouns. Don’t use “he/she” or “(s)he” as an alternative to the singular “they”.  

Only use gendered pronouns (he/she, him/her, his/hers) if the person you’re referring to is actually that gender.  

##### Ambiguous pronouns {#ambiguous-pronouns}

Pronouns substitute for nouns. The word a pronoun refers to is called its antecedent. When writing instructions or learning material, be sure to make clear references between a pronoun and its antecedent. This may require repeating subjects to make the meaning clear.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Do: <em>Ensure a pronoun clearly references its antecedent</em></th><th style="width: 50%;">Don't: <em>Use ambiguous pronoun references</em></th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">If you type text in the field, the text doesn’t change.</td><td style="width: 50%;">If you type text in the field, it doesn't change.</td></tr>
<tr><td style="width: 50%;">She told Sarah that Sarah’s answer was incorrect.</td><td style="width: 50%;">She told Sarah that her answer was incorrect.</td></tr>
<tr><td style="width: 50%;">You can’t edit an archived campaign. Unarchive a campaign to edit it.</td><td style="width: 50%;">You can't edit an archived campaign. Unarchive it to edit it.</td></tr>
</tbody>
</table>
{:/}

##### Optional pronouns

To add additional clarity to your writing and to aid in localization, use pronouns such as “that”, “which”, and “who”.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Do: <em>Use "that", "which", and "who" to add additional clarity.</em></th><th style="width: 50%;">Don't</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Right-click the link that you want to open.</td><td style="width: 50%;">Right-click the link you want to open.</td></tr>
<tr><td style="width: 50%;">From here, you can choose which Tinyclues cohort that you want to include.</td><td style="width: 50%;">From here, you can choose a Tinyclues cohort you want to include.</td></tr>
</tbody>
</table>
{:/}

#### Capitalization {#capitalization}

Avoid unnecessary capitalization. In most instances, use sentence case. Title case should only be used for proper nouns or feature names (unless otherwise specified, see [Glossary](https://confluence.braze.com/pages/viewpage.action?spaceKey=MAR&title=Braze+Glossary)).

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Do: <em>Use lowercase for writing out website URLs and email addresses</em></th><th style="width: 50%;">Don't</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">www.braze.com/docs</td><td style="width: 50%;">www.Braze.com/docs</td></tr>
<tr><td style="width: 50%;">sample@email.com</td><td style="width: 50%;">SAMPLE@EMAIL.COM</td></tr>
</tbody>
</table>
{:/}

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Do: <em>Use lowercase directionals</em></th><th style="width: 50%;">Don't</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">north, south, east, west</td><td style="width: 50%;">North, South, East, West</td></tr>
</tbody>
</table>
{:/}

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Do: <em>Capitalize specific regions, and use all capitals for abbreviated regions</em></th><th style="width: 50%;">Don't</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">the Northwest</td><td style="width: 50%;">the northwest</td></tr>
<tr><td style="width: 50%;">Southern Connecticut</td><td style="width: 50%;">southern Connecticut</td></tr>
<tr><td style="width: 50%;">Eastern Europe</td><td style="width: 50%;">eastern Europe</td></tr>
<tr><td style="width: 50%;">APAC, EMEA</td><td style="width: 50%;">Apac, emea</td></tr>
</tbody>
</table>
{:/}

##### Brands and products

When referring to a brand or product, use the capitalization the brand uses. In most cases, capitalize the names of brands (Grindr, Walmart) and products (Benchmarks, Looker Blocks). It’s fine to begin a sentence with lowercase if the first word is the stylized name of a brand like eBay or iTunes. 

For intercaps, always refer to the usage preferred by the brand in print (OkCupid, YouTube). Do not use intercaps that only appear in logos or graphic design treatments (Amazon). 

#### Clause order {#clause-order}

If you want to tell the reader to do something in a specific circumstance, try to mention the circumstance before you provide the instruction. This lets the reader skip the instruction if the circumstance doesn't apply.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Do</th><th style="width: 50%;">Don't</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">For troubleshooting steps, see Campaign FAQs.</td><td style="width: 50%;">See Campaign FAQs for troubleshooting steps.</td></tr>
<tr><td style="width: 50%;">To archive your campaign, click the gear icon and select Archive.</td><td style="width: 50%;">Click the gear icon and select Archive to archive your campaign.</td></tr>
</tbody>
</table>
{:/}

#### Combining forms {#combining-forms}

[Hyphenate](#hyphens) combined forms when the phrase is used as an adjective before the noun. 

**Example:** A one-of-a-kind item

#### Contractions {#contractions}

A contraction is a shortened version of a word or phrase. Use contractions to keep an approachable and informal tone. However, do not use noun and verb contractions or double contractions, or a combination of two contractions. These can disrupt the flow and coherency of the sentence.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Do: <em>Use contractions</em></th><th style="width: 50%;">Don't: <em>Use noun and verb contractions</em></th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">If you’re an admin, you can manage your company’s contact information.</td><td style="width: 50%;">Braze’ll now support Shoptify integration.</td></tr>
<tr><td style="width: 50%;">You can’t edit an archived campaign.</td><td style="width: 50%;">You mightn’t’ve seen the restricted upload size.</td></tr>
</tbody>
</table>
{:/}

#### Dangling and misplaced modifiers {#dangling-and-misplaced-modifiers}

Modifiers are words of phrases that modify other words or phrases. A dangling modifier doesn’t modify any subject in the sentence. A misplaced modifier is placed far away from the subject that it’s meant to modify. Essentially, dangling and misplaced modifiers may cause confusion by connecting to the wrong part of the sentence.

Writing with an active voice helps prevent the use of dangling and misplaced modifiers. Be sure to use a modifier that clearly modifies. 

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Do: <em>Keep sentence short and concise. Use active voice.</em></th><th style="width: 50%;">Don't: <em>Use lengthy sentences with modifiers that can cause confusion</em></th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Customers must set up their SAML settings.</td><td style="width: 50%;">You may have test messages on your campaigns that can be deleted.</td></tr>
<tr><td style="width: 50%;">Make sure to save your campaign drafts.</td><td style="width: 50%;">On the way home, Sarah found a gold man’s stopwatch.</td></tr>
</tbody>
</table>
{:/}

#### Prepositions {#prepositions}

There’s nothing wrong with ending a sentence in a preposition when it improves readability. Place a preposition or prepositional phrase where it makes the most sense in a sentence. If you’re having difficulty, read the sentence out loud and see if it sounds natural.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Do</th><th style="width: 50%;">Don't</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Each option corresponds to the priority the notification appears in.</td><td style="width: 50%;">Each option corresponds to the priority in which the notification appears.</td></tr>
<tr><td style="width: 50%;">For details, see the SDK documentation for the platform you’re working with.</td><td style="width: 50%;">For details, see the SDK documentation for the platform with which you’re working.</td></tr>
</tbody>
</table>
{:/}

#### Present tense {#present-tense}

Use present tense instead of future tense. Present tense conveys immediacy and demonstrates confidence. Avoid using “will” or hypothetical “would”, especially when referring to the result of user action.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Do</th><th style="width: 50%;">Don't</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Archived subscription groups cannot be edited and no longer appear in segment filters.</td><td style="width: 50%;">Archived subscription groups cannot be edited and will no longer appear in segment filters.</td></tr>
<tr><td style="width: 50%;">Using a short code is the most reliable number type for including links.</td><td style="width: 50%;">Using a short code would be the most reliable number type for including links.</td></tr>
</tbody>
</table>
{:/}

Only use future tense when you’re actually talking about the future. Avoid predicting [future features](#describing-limitations). 

#### Profanity {#profanity}

Keep it PG. This has less to do with morality than the fact profanity can be divisive and off-putting to an audience as broad and international as ours. There’s also a case to be made that sometimes profanity is a cover-up for half-baked writing. That’s simply not our vibe. 

#### Plurals in parentheses {#plurals-in-parentheses}

Do not use plurals in parentheses. Instead, use the plural or singular form of the word.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Do</th><th style="width: 50%;">Don't</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Customize your campaign with the following filters.</td><td style="width: 50%;">Customize your campaign with the following filter(s).</td></tr>
</tbody>
</table>
{:/}

#### Second person and first person {#second-person-and-first-person}

Use second person in your instructions instead of first person—”you” rather than “we”. 

Refer to the reader as the one doing the action. Strike a conversational tone—most readers are coming to documentation when they don’t have immediate access to a support agent. Make it feel as if the article is talking to them instead. 

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
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
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
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

#### Slang and idioms {#slang-and-idioms}

We’re a plainspoken bunch. Avoid using trendy slang or idioms that speak too specifically to a singular audience. It can also quickly date materials, and make it difficult to localize content. 

#### Spelling {#spelling}

Use American English spelling for words that differ in British English. If you’re not sure how to spell a word, first refer to the [Glossary](#glossary). If the word isn’t listed there, then refer to [Merriam-Webster’s Collegiate Dictionary](https://www.merriam-webster.com/).

For words that are accented or contain special characters, make sure to correctly follow the dictionary spelling. In some cases, unintentionally omitting these accents can result in a different word. For example, “resume” means to begin again after stopping, whereas “résumé” is an account of one’s qualifications. 

### Punctuation {#punctuation}

#### Ampersands {#ampersands}

Don’t use an ampersand (&) in place of “and” in text or headings unless you are referring directly to the user interface.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
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
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
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
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
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
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Do</th><th style="width: 50%;">Don't</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;"><code>user_alias_label</code>: A common label to group user aliases with.</td><td style="width: 50%;"><code>user_alias_label:</code> A common label to group user aliases with.</td></tr>
</tbody>
</table>
{:/}

You can also use a colon to join two related phrases in a sentence. However, use colons for this sparingly. Two sentences are generally more readable. 

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
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
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Do</th><th style="width: 50%;">Don't</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Push subscriptions states are filters and can allow users to edit notification preferences.</td><td style="width: 50%;">Push subscriptions states are filters, and can allow users to edit notification preferences.</td></tr>
</tbody>
</table>
{:/}

#### Dashes {#dashes}

##### Em dash

Use an em dash (—) when using a dash in a sentence to indicate a separate thought or interruption. Don’t put any spaces before or after the em dash. Don’t use an em dash where a comma or parenthesis would work just as well.

Refer to your operating system for how to type an em dash:

* **macOS:** Press Option + Shift + Hyphen.  
* **Windows:** Turn num lock on, then hold down the left Alt key and type 0151 on the num pad.

##### En dash {#en-dash}

Use an en dash (–) to indicate a range of numbers, as a minus sign, or to indicate negative numbers. Don’t put any spaces before or after the en dash except for when it’s used as a minus sign. Don’t use a hyphen (-). 

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Do: <em>Use an en dash for a range of numbers</em></th><th style="width: 50%;">Don't: <em>Use a hyphen</em></th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">2018–2021</td><td style="width: 50%;">2018-2021</td></tr>
</tbody>
</table>
{:/}

Don’t use an en dash for ranges of time. For more details, refer to the section [Dates and Times](#dates-and-times).

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Do: <em>Use an en dash for a minus sign and include spaces surrounding the en dash</em></th><th style="width: 50%;">Don't: <em>Use a hyphen</em></th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">15 – 5 = 10</td><td style="width: 50%;">15-5=10</td></tr>
</tbody>
</table>
{:/}

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Do: <em>Use an en dash for negative numbers</em></th><th style="width: 50%;">Don't: <em>Use a hyphen</em></th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">–30</td><td style="width: 50%;">-30</td></tr>
</tbody>
</table>
{:/}

Refer to your operating system for how to type an en dash:

* **macOS:** Press Option + Hyphen.  
* **Windows:** Turn num lock on, then hold down the left Alt key and type 0150 on the num pad.

#### Ellipses {#ellipses}

An ellipsis is a series of three periods (...) that indicates an omission of one or more words. In general, avoid using ellipses when possible while writing instructions or learning content. 

#### Exclamation points {#exclamation-points}

An exclamation point can be used sparingly for an informal tone. However, avoid overly using exclamation points throughout text. Instead, consider using [Alerts](#callouts-and-alerts).

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Do: <em>Use exclamation points for an informal tone for reminders and introductions</em></th><th style="width: 50%;">Don't: <em>Use exclamation points for indicating warning or caution to readers</em></th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Be sure to save your changes before leaving the page!</td><td style="width: 50%;">Users must receive one or more messages from a step to be counted as a unique recipient!</td></tr>
</tbody>
</table>
{:/}

#### Hyphens {#hyphens}

Hyphens can help the reader gain more clarity in a sentence by linking words in a phrase together. Here are a few guidelines for getting it right.

Use hyphens for compound modifiers that help the reader understand the subject more clearly.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
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
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
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
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
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
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
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
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
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
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 100%;">Do: <em>Use a semicolon to break up a sentence with two related independent clauses</em></th></tr>
</thead>
<tbody>
<tr><td style="width: 100%;">The cat slept through the storm; the dog cowered under the bed.</td></tr>
</tbody>
</table>
{:/}

Semicolons can be used to separate list items if one (or more) of the list items contains a comma.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 100%;">Do: <em>Use a semicolon to break up a longer sentence</em></th></tr>
</thead>
<tbody>
<tr><td style="width: 100%;">Jane Lang, our moderator; Simon Mayer, CEO and Cofounder of PantsLabyrinth; and Kara Seberg, CMO of Yachtr.</td></tr>
</tbody>
</table>
{:/}

#### Slashes {#slashes}

There are two types of slashes: backward (\\) and forward (/). Do not use slashes to indicate alternative words or examples (“and/or”). 

Use slashes as needed in file paths and URLs.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Do: <em>Use a slash for file paths</em></th><th style="width: 50%;">Don't: <em>Use a slash to separate alternatives</em></th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;"><code>/campaigns/data_series</code></td><td style="width: 50%;">you/your customers</td></tr>
</tbody>
</table>
{:/}

#### Quotation marks {#quotation-marks}

There are two types of quotation marks: straight (" ") and curly (“ ”). Periods and commas go inside the quotation marks. An exception is when the quotation marks include exact information such as a string. Use quotation marks when directing users to input a specific string of text into a text field.

{% alert note %}

When describing search syntax, quotation marks are often used to signify searching for exact text. In this case, use brackets around the string of text and quotation marks as required by the search syntax. For example: <br><br>

*Put quotes around any word or phrase, such as [“test segment”], and we show results that contain only those exact words or phrases.* 

{% endalert %}

Code examples must use straight quotation marks. For more information about formatting code in text, refer to [Code in Text](#code-in-text).

### Technical documentation {#technical-documentation}

#### API endpoints {#api-endpoints}

In general, documentation for API endpoints should follow the guidelines in this style guide. However, there are niche topics that may require different content guidelines listed in this document. For more information on how to format and reference endpoints, refer to [API endpoint documentation guidelines]({{site.baseurl}}/contributing/style_guide/api_endpoint_guidelines/). 

#### Avoid guarantees {#avoid-guarantees}

Our documentation must refrain from making commitments that could potentially result in legal implications. Avoid using definitive terms such as "guarantee" or "ensure". Instead, employ forward-looking statements like "Designed to" or "Intended to" to accurately convey the product's capabilities and intentions.

#### Describing interactions with the UI {#describing-interactions-with-the-ui}

When referring to UI elements, match the capitalization as it appears in the UI. However, If a label is all caps, use sentence case (exception: short labels, like AND or OR operators). 

When instructing a reader to interact with the UI, bold the UI element they are interacting with. For strings that a user would enter into a field, use quotation marks. 

For guidance on what verbs to use when describing interactions with the UI, refer to the following table:

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
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

#### Describing limitations {#describing-limitations}

Write candidly about the product's limitations, without distortion or manipulation. Readers react in an intense fashion to being manipulated, hoodwinked, and otherwise bamboozled, and this jeopardizes the documentation's efficacy as a source of utilitarian truth. Customers rely on documentation to understand the limits of the system to which they are building so that they can use Braze successfully.

At the same time, support the intentionality of the product's development by framing limitations with appropriate, positive context.

* If there is a soft limitation (for example, an API rate limit), frame the limitation by talking about the **default limit** or **starting allotment.**  
* Provide a meaningful path forward to navigate soft limits. Provide examples of these workarounds as appropriate.  
 * For example, Braze uses sizing exercises during onboarding to help customers understand how things such as data points are used by other businesses of a similar size. When discussing data points, it is appropriate to talk about the sizing exercise at the same time.  
* It is better to describe a path forward in a positive way than as a mitigation.   
 * For example, instead of saying "Braze does not allow customers to do this on their own. The Support team must activate this feature for you," say, "To activate this feature, contact the Support team."  
* Do not over-rely on the same stock phrases to navigate soft limits. If a user reads "Talk to your customer service representative" over and over, the advice becomes meaningless.  
* If there is a hard limitation, try to describe the rationale behind this limit.  
 * For example: "There is a limit of 200 active, action-based in-app message campaigns per app group to optimize the speed of message delivery and to prevent timeouts. …The average Braze customer has a total of 26 campaigns active at once—so it's unlikely that this limitation impacts you."  
* Do not describe [planned functionality or future features](#future-features) as a way to explain current limitations.  
* When referring to limits around custom data, use the term "capacity" instead of limits.   
 * For example: By default, you can have 20 segmentable event properties per workspace. Contact your Braze account manager to increase your capacity. 

#### Future features {#future-features}

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

#### Feature deprecations {#features-deprecations}

Before including information about feature deprecations, be sure you have a general time frame of when readers can expect the feature to be deprecated (for example, late 2025).

After you have a general time frame, communicate the feature deprecation early. Be clear in writing about deprecations so that readers can clearly understand what to expect.

Don't use phrases that might incite fear, uncertainty, or doubt with readers. Provide a clear path forward, such as what the deprecated feature is being replaced by or an alternative solution.

#### General versus specific {#general-vs-specific}

As a best practice, write articles that discuss functionality in a generally applicable way. If more detail is needed for specific cases or exceptions, create a separate section (or separate article if the content is web article length, ~500 words) that outlines this outlier. Create cross-references from the general article to the specific to help users connect these concepts.

Avoid creating duplicated or repetitious content for different channels or features. If repetition is needed, use `includes` files and other [reusable content best practices]({{site.baseurl}}/contributing/content_management/reusing_content).

**As an example:** A common use case for Braze customers is to retarget users who have previously interacted with their messaging. Retargeting users can be done through many engagement tools, including campaigns, Canvases, landing pages, and segments. Retargeting users can be done through many channels: WhatsApp, SMS, Content Cards, email, push notifications, and more. Often, customers try to reengage a user through a separate channel than one previously used.  
Instead of creating one article for each engagement tool and each channel, create a single article that discusses strategies for retargeting users and outlines all the options available. If there are special considerations for specific channels/tools, create a separate article that outlines those considerations and house it within that documentation section. Create cross-references between the general article and the specific article.

#### Metadata and YAML {#metadata-and-yaml}

Articles in Braze documentation require certain metadata for search and index purposes. For information on what metadata is required, refer to the GitHub page on [YAML and Metadata Layouts](https://github.com/braze-inc/braze-docs/wiki/YAML-%26-Metadata-Layouts).

#### Naming conventions {#naming-conventions}

When naming articles and filenames, make sure to describe the general topic in the title. Always include a keyword and brief description that readers easily understand, especially with article titles. 

For filenames, keep the name brief and avoid using articles (a, an, the). Separate each word with an underscore (_).

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 100%;">Do</th></tr>
</thead>
<tbody>
<tr><td style="width: 100%;">Targeting users</td></tr>
<tr><td style="width: 100%;">Creating an email campaign</td></tr>
<tr><td style="width: 100%;">API errors and responses</td></tr>
<tr><td style="width: 100%;">sms_historical_performance.png</td></tr>
<tr><td style="width: 100%;">push_notification_test.png</td></tr>
</tbody>
</table>
{:/}

In general, for articles and image files, use the same spelling and capitalization as the referenced article and files. For guidelines on article title styling, refer to [Headings and Titles](#headings-and-titles).

When referring to a specific file, use the same spelling of the filename and code font. For formatting details, refer to the GitHub page on [Special Formatting](https://github.com/braze-inc/braze-docs/wiki/Special-Formatting). 

#### Procedures and instructions {#procedures-and-instructions}

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

For formatting details, refer to the GitHub page on [Special Formatting](https://github.com/braze-inc/braze-docs/wiki/Special-Formatting). Alternatively, you can also use a [list](#lists) or [table](#tables-1) to organize information.

### Formatting and organizing {#formatting-and-organizing}

#### Addresses {#addresses}

Use the numeral followed by the street name like so: 

*330 W. 34th St.*

To display a full address, use the numeral, followed by the street name, followed by the city, state, and zip code. There’s no need for a comma between the state and zip code.

*330 W. 34th St., New York, NY 10001*

#### Button labels {#buttons-labels}

Button labels should be clear and predictable—the user should know what action occurs upon clicking the button. Use sentence case for button labels, and lead with a strong verb. If it may be unclear what the verb is referring to, use the format [verb] + [noun]. 

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
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

#### Callouts and alerts {#callouts-and-alerts}

Alerts, also known as callouts, are used to draw attention to information that is helpful to the reader. There are four alerts types that are used in our documentation:

* Important  
* Note  
* Tip  
* Warning

Use alerts sparingly throughout articles. For more information, refer to [Alerts best practices]({{site.baseurl}}/contributing/style_guide/alerts/).

#### Code in text {#code-in-text}

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

#### Code samples {#code-samples}

Code samples refer to blocks of code text that display a sample snippet of code. For accessibility purposes, introduce the code sample with an expository sentence where possible.

To make sure your code samples are legible, indent each line by two spaces per indentation level. If you’re having trouble formatting your code samples, try prettifying your code using a pretty print formatter, such as [JSON Formatter](https://jsonformatter.org/json-pretty-print).

To create code blocks in Braze documentation, refer to [Code Snippet Test](https://github.com/braze-inc/braze-docs/blob/develop/_docs/_home/styling_test_page.md#code-snippet-test). Remember that code blocks should specify the language type to ensure proper syntax highlighting.

#### Dates and times {#dates-and-times}

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
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 100%;">Do: <em>Use the preferred date format.</em></th></tr>
</thead>
<tbody>
<tr><td style="width: 100%;">September 2021</td></tr>
<tr><td style="width: 100%;">September 15, 2021</td></tr>
<tr><td style="width: 100%;">Wednesday, September 15, 2021</td></tr>
</tbody>
</table>
{:/}

For date ranges, use an [en dash](#en-dash).

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
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
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Do: <em>Use numerals with am or pm.</em></th><th style="width: 50%;">Don't: <em>Use minutes for on-the-hour time (unless it's a range).</em></th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">12 pm</td><td style="width: 50%;">12:00 P.M.</td></tr>
</tbody>
</table>
{:/}

For ranges of time, use an en dash to separate. Do not add spaces before or after the en dash.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 100%;">Do: <em>Use an en dash for range of time.</em></th></tr>
</thead>
<tbody>
<tr><td style="width: 100%;">12:45–2:30 pm</td></tr>
</tbody>
</table>
{:/}

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 100%;">Do: <em>Use minutes for ranges of time.</em></th></tr>
</thead>
<tbody>
<tr><td style="width: 100%;">8:00 am–2:30 pm</td></tr>
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

#### Example names {#example-names}

Never use real names, email addresses, or any other personally identifiable information (PII). Instead, use fictional examples or [placeholder text](#placeholder-text). 

When you need to include names in your writing, refer to Wikipedia’s list of [Unisex names](https://en.wikipedia.org/wiki/Unisex_name). Use the pronouns “they”, “their”, and “theirs” when possible, and avoid using examples that are limited to a specific gender.

##### Example email addresses

Use the format “name@example.com” for generic email addresses. Replace “name” with an example name. For example:

* alex@example.com  
* lee@example.com  
* yuri@example.com

#### Figures and other images {#figures-and-other-images}

When creating figures and images, refer to the [Image copy style guide]({{site.baseurl}}/contributing/style_guide/image_style_guide/). Never include personally identifiable information (PII) in figures or images.

##### Alt text {#alt-text}

Always include alt text with images. Screen readers announce alt text to explain images to people with loss of vision. As such, your alt text must convey all the key information depicted in the image.  
Use the following guidelines when writing alt text:

* Use [plain language](https://www.plainlanguage.gov/guidelines/).  
* Write in complete sentences, and use sentence case.  
* Omit unnecessary words.  
* Don’t include “image of” or “picture of”. It’s already understood that you are referring to an image.   
* Don’t include special characters. For example, instead of ampersands (&), use the word “and” written out.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
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

#### File types and filenames {#file-types-and-filenames}

When you’re referring to a file type, use the standard name of the type. If the file type is an acronym, refer to the file type in all caps. 

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Do: <em>Use the standard name of the file type</em></th><th style="width: 50%;">Don't: <em>Use the file extension</em></th></tr>
</thead>
<tbody>
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

#### Formatting text in instructions {#formatting-text-in-instructions}

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
* [Pages](#pages)  
* [Permission names](#permission-names)  
* [Tabs](#tabs-1)  
* [Text input](#text-input)

##### Buttons {#buttons}

When referring to a button, use bold text for the button label. In most cases, match the capitalization of the UI. For buttons where the label is in all caps (except OK buttons), use sentence case instead. 

To refer to a button, use only the button’s label. Do not refer to a button as “the [label] button”.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
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
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
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
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
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
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
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

##### Dialog boxes (modals) {#dialog-boxes-(modals)}

Avoid referring to dialog boxes by name unless clarity is needed. Instead, describe what the reader needs to do. If you refer to a dialog box, use bold text for the name of the dialog box and match the capitalization of the UI.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
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
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
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
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Do</th><th style="width: 50%;">Don't</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Select the <code>First Used App</code> filter and…</td><td style="width: 50%;">Select the <strong>First Used App</strong> filter and…</td></tr>
<tr><td style="width: 50%;">Combine filters with the <code>OR</code> operator.</td><td style="width: 50%;">Combine filters with the “OR” operator.</td></tr>
</tbody>
</table>
{:/}

##### Folder and filenames {#folder-and-filenames}

When referring to folder names and filenames, use code text. 

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
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
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
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
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
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
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
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
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
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
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Do</th><th style="width: 50%;">Don't</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">In the <strong>Name</strong> field, enter “Lapsing Users”</td><td style="width: 50%;">In the <strong>Name</strong> field, enter <code>Lapsing Users</code>.</td></tr>
</tbody>
</table>
{:/}

#### Frequently asked questions (FAQs) {#frequently-asked-questions-faqs}

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
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
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
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
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

##### States and provinces

Capitalize all states and provinces. 

**Example:** New York, Quebec

#### Headings and titles {#headings-and-titles}

For article headings and titles, use sentence case capitalization. Be descriptive when writing headings and titles, and focus on the main purpose of the content based on the article type. 

For article titles, use gerunds (verbs ending in *-ing*) to begin the title when applicable. Keep the article titles concise and make sure it is appropriate for the content. For example, a reference article about SMS messages could be titled “About SMS”.

For article headings, be concise and consistent across heading titles. For example, if the article’s Heading 1 style defines each step (ex. **Step 1: Create a new push campaign**), then keep this format across the article headings for consistency.

For styling help in Braze Docs, refer to the Contributing page for [Styling examples]({{site.baseurl}}/contributing/styling_examples/?tab=markdown). 

##### Numeric subtasks

For headers that describe ordered steps, use numerals in the subtask headers.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
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

Include only the "Use this endpoint..." sentence in the intro. We want to keep the API endpoints as easy to navigate as possible. For more on API endpoint structure and formatting, see the [API endpoint documentation guidelines]({{site.baseurl}}/contributing/style_guide/api_endpoint_guidelines/).

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

#### Media formatting {#media-formatting}

This section includes general guidelines for formatting images and GIFs in your content. For more information, including example screenshots, refer to the [Image copy style guide]({{site.baseurl}}/contributing/style_guide/image_style_guide/).

| **Do** | {::nomarkdown}<ul><li>Do tightly crop to the feature or component of mention.</li><li>Do take high-quality screenshots, preferably on a retina monitor (MacBook display).</li><li>Do create a GIF of an interaction or workflow.</li><li>Keep in mind that users cannot pause or scrub through a GIF to see details.</li><li>Do run images through an optimizer to reduce file size (ImageOptim, TinyPNG, or Ezgif).</li><li>Do aim for high contrast between elements for accessibility.</li><li>Do resize images by height percentages rather than distinct pixel values.</li></ul>{:/} |
| **Don't** | {::nomarkdown}<ul><li>Don't include the header or sidebar of the dashboard, as these can be explained in a simple sentence.</li><li>Don't include the entire dashboard.</li><li>Don't include Personally Identifiable Information (unless blurred, or that of a demo user).</li><li>Don't include the browser frame (URL field, bookmarks, tabs, and so on.).</li><li>Don't include dashboards of Technology Partners.</li><li>Don't add a border or drop shadow to images.</li></ul>{:/} |

#### Numbers {#numbers}

Never start a sentence with a numeral. The exception is when referring to a year (example: “2019 was one for the books). 

Spell out numerals up to nine. For units of measurement or numbers 10 or higher, use the numeral. For numbers over three digits, use a comma. Write out larger numbers. 

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
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
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Do</th><th style="width: 50%;">Don't</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">US $20</td><td style="width: 50%;">$20</td></tr>
</tbody>
</table>
{:/}

##### Telephone numbers

When a phone number is referenced, place hyphens between the digits. Do not place the area code within parentheses. 

When formatting phone numbers with a country code, use a plus sign (+) before the country code and place the area code within parentheses. 

Provide a number with a country code like so: +1 (504) 327-7269

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
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
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
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
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Do</th><th style="width: 50%;">Don't</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">10%</td><td style="width: 50%;">10 %</td></tr>
<tr><td style="width: 50%;">Twenty percent of company users are...</td><td style="width: 50%;">20% of company users are...</td></tr>
</tbody>
</table>
{:/}

##### Ranges

Use a hyphen to indicate a range of numbers. Do not use an en dash to separate numbers in a range. 

For ranges of numbers with units, repeat the unit of measurement after the number. This does not include repeating nouns. Use the word “to” between the numbers in the range to avoid confusion.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Do</th><th style="width: 50%;">Don't</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">5 to 100</td><td style="width: 50%;">5–100</td></tr>
<tr><td style="width: 50%;">-10°C to 50°C</td><td style="width: 50%;">-10°C-50°C Don't</td></tr>
</tbody>
</table>
{:/}

#### Placeholder text  {#placeholder-text}

Use placeholder text to signify where the reader should supply the relevant value. Placeholder text should indicate the content that’s being represented. For example *YOUR_API_KEY* indicates the reader’s API key.

##### Writing placeholders

When creating placeholder text, refer to the following guidelines:

| Guideline | Example |
| :---- | :---- |
| Use uppercase letters and separate words with underscores (_). | `PLACEHOLDER_VARIABLE` |
| ​​For inline placeholder text, use italics. | *`PLACEHOLDER_VARIABLE`* |
| For API code block placeholder text (where you can’t use italics), enclose the placeholders in curly brackets ({}).  | `<string name="com_appboy_api_key">{YOUR_APP_IDENTIFIER_API_KEY}</string>` |
| For Liquid code block placeholder text (where you can’t use italics), use uppercase letters. | `{% raw %}{%- connected_content YOUR-API-URL :save items -%}{% endraw %}`  |
| Don't sacrifice clarity for brevity. Use as many words as needed to represent a placeholder. | **Do:** `CAMPAIGN_NAME` <br> **Don't**: _`NAME`_|

##### Using placeholders

When introducing or explaining a placeholder, refer to the following guidelines:

| Guideline | Example |
| :---- | :---- |
| Call out placeholders immediately after the placeholder. | Replace `<YOUR_APP_IDENTIFIER_API_KEY>` with your [App Identifier API Key]({{site.baseurl}}/api/api_key/#the-app-identifier-api-key), which you can find on the **Settings** page. |
| To call out two or more placeholders at once, use a bulleted list. List each placeholder in the order they appear in the code. | Replace the following: {::nomarkdown}<ul><li><code>PLACEHOLDER_VARIABLE</code>: a description of what the placeholder represents</li><li><code>PLACEHOLDER_VARIABLE</code>: a description of what the placeholder represents</li></ul>{:/} |
| Refer to the placeholder in the same formatting that it’s shown in the text or code. | `target <YOUR_APP_TARGET> do pod 'Appboy-iOS-SDK' end` <br><br> Replace `<YOUR_APP_TARGET>` with the name of your target app. |

#### Products {#products}

When referring to Braze and its features, use full product and feature names, and capitalize them according to the UI. Don’t capitalize templates or common features. For a list of product names and their spelling, refer to the [Glossary](#glossary). 

Don’t abbreviate product or feature names except in the following cases:

* To match the UI  
* To meet limited space constraints

Never use product or feature names as verbs. 

Never use an apostrophe after Braze (example:“Braze’s.”) It sounds awkward. Instead, form possessives using a preposition (“to, of, from”) followed by the company name.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
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

#### Units of measurement {#units-of-measurement}

For HTML and Markdown, use a nonbreaking space (&nbsp) between the number and the unit when specifying a unit of measurement. This includes most units of measurement such as distance, pixels, points, weight, and degrees of temperature (between the degree and unit of measurement). 

For currency, percent, or degrees of an angle, don’t use a space between the number and unit.

For ranges of numbers with units, repeat the unit for each number. Similarly, for rates, use “per” instead of a slash (/). 

### Linking {#linking}

#### Cross-reference links {#cross-reference-links}

Use cross-references to guide users to additional resources. In Braze documentation, use site-root-relative URLs to link to other Braze docs (replace “www.braze.com/docs” with “{{site.baseurl}}”).

Avoid adding multiple links to the same document within a given page, as this can cause link fatigue. Duplicate links are fine in moderation if you’re linking to a specific section on another page, or if the page you’re linking from is long.

#### Embedding videos {#embedding-videos}

Similar to images, use videos to create variety in your learning materials. Most people learn best with a combination of mediums, so make sure that any content you include in a video is also covered in the article or lesson.

To embed a video in Braze documentation, refer to [Embedded Video Test]({{site.baseurl}}/home/styling_test_page/#embedded-video-test).

#### Headings as link targets {#headings-as-link-targets}

In Braze documentation, anchors are automatically created for headings. However, you may want to add a custom anchor to a heading if:

* Your auto-generated anchor is very long.  
* Your heading may be frequently linked to. Adding a custom anchor reduces the likelihood of breaking links if the heading text is changed later.

To add an anchor to a heading in Braze documentation, refer to [Custom Anchors]({{site.baseurl}}/home/styling_test_page/#custom-header-anchor).

#### Link text {#link-text}

Effective link text helps to improve the findability, discoverability, and accessibility of your content. 

##### Structuring links {#structuring-links}

Use one of the following formats when writing links:

* Match the link text to the title or heading of the link destination.  
* Use a description of the link destination as the link text.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Do: <em>Match the link text to the title or heading of the link destination.</em></th><th style="width: 50%;">Do: <em>Use a description of the link destination as the link text.</em></th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Get started with the Braze <a href="{{site.baseurl}}/user_guide/getting_started/web_sdk/">Web SDK</a>.</td><td style="width: 50%;">To find out your specific cluster or endpoint, <a href="{{site.baseurl}}/braze_support/">contact Support</a>.</td></tr>
<tr><td style="width: 50%;">For more information, see <a href="{{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/aborting_messages/">Aborting Liquid Messages</a>.</td><td style="width: 50%;">When in doubt, you can always <a href="{{site.baseurl}}/user_guide/administrative/access_braze/accessing_your_account/#resetting-your-password">reset your password</a>.</td></tr>
</tbody>
</table>
{:/}

You may need to rephrase a sentence to make good link text.

If you’re linking to a section on the same page, use a standard phrase that indicates this action. For example:

* On this page, see [heading].  
* In this document, refer to [heading].  
* For more information, refer to the section [heading].

##### Writing links {#writing-links}

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
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Do: <em>Make sure the link text makes sense without the surrounding text</em></th><th style="width: 50%;">Don't: <em>Use vague or non-descriptive link text</em></th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">For more information on importing customer data, see <a href="{{site.baseurl}}">User Import</a>.</td><td style="width: 50%;">For more information, <a href="{{site.baseurl}}">click here</a>.</td></tr>
<tr><td style="width: 50%;">This feature connects to the <a href="{{site.baseurl}}">Track users</a> endpoint.</td><td style="width: 50%;">See <a href="{{site.baseurl}}">this article</a>.</td></tr>
<tr><td style="width: 50%;">Learn more about <a href="{{site.baseurl}}">what’s new in Android SDK 16.0.0</a>.</td><td style="width: 50%;">Follow the instructions <a href="{{site.baseurl}}">here</a>.</td></tr>
<tr><td style="width: 50%;">Learn more about the <a href="https://www.braze.com/product">Braze platform</a>.</td><td style="width: 50%;">For steps, refer to <a href="{{site.baseurl}}">this document</a>. <a href="{{site.baseurl}}">Learn more</a>.</td></tr>
<tr><td style="width: 50%;">Storefront API keys are unique per Hydrogen storefront, but their permission scopes are shared by all Hydrogen storefronts. Learn more about <a href="{{site.baseurl}}">Storefront API tokens.</a></td><td style="width: 50%;"><a href="{{site.baseurl}}">Storefront API tokens</a> are unique per <a href="{{site.baseurl}}">Hydrogen storefront</a>, but their <a href="{{site.baseurl}}">permission scopes</a> are shared across all Hydrogen storefronts.</td></tr>
</tbody>
</table>
{:/}

#### Links for endpoints {#links-for-endpoints}

When referencing endpoint articles, be sure to use [meaningful link text](https://docs.google.com/document/d/e/2PACX-1vTluyDFO3ZEV7V6VvhXE4As_hSFwmnFFdU9g6_TrAYTgH1QmbRoEDDdn5GzKAB9vdBbIdyiFdoaJcNk/pub#h.79ujl0qtumog) that can make sense out of context. If you’re using the endpoint’s path as a link, be sure to provide details in the surrounding text as the path may not clearly communicate the endpoint’s function.    

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Do</th><th style="width: 50%;">Don't</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Delete user profiles using the Braze <a href="{{site.baseurl}}/api/endpoints/user_data/post_user_delete/">Delete user endpoint</a>.</td><td style="width: 50%;">Delete user profiles using the Braze <a href="{{site.baseurl}}/api/endpoints/user_data/post_user_delete/">Delete user</a> endpoint.</td></tr>
<tr><td style="width: 50%;"><a href="{{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/"><code>/users/export/id</code> endpoint</a></td><td style="width: 50%;"><a href="{{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/"><code>/users/export/id</code></a> endpoint</td></tr>
</tbody>
</table>
{:/}

#### Links for file download {#links-for-file-download}

If a link downloads a file, then make that clear in the link text, and mention the file type.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Do: <em>Make sure the link text communicates that clicking it downloads a file</em></th><th style="width: 50%;">Don't</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">For tips, download the <a href="{{site.baseurl}}">Regex Cheat Sheet PDF</a>.</td><td style="width: 50%;">Check out our <a href="{{site.baseurl}}">RegEx Cheat Sheet</a>.</td></tr>
<tr><td style="width: 50%;">For more information, download the <a href="{{site.baseurl}}">Success and Support Services Handbook PDF</a>.</td><td style="width: 50%;"><a href="{{site.baseurl}}">Success and Support Services Handbook</a></td></tr>
</tbody>
</table>
{:/}

#### Links to other sites {#links-to-other-sites}

As a general rule, don’t link to another site if you can cover the information with a brief explanation. We can’t keep track of when the content on another site changes. 

If you do link to an external site, make sure that the site you link to is high quality, reliable, and respectable. If possible, link to the most relevant heading on a page.

Use an external link icon to indicate that the link goes to a different domain. For Braze documentation, this is automatically applied to external links.

#### URLs for images {#urls-for-images}

In Braze documentation, use site-root-relative URLs to link to images. For more information, refer to [Adding and Editing Images](https://github.com/braze-inc/braze-docs/wiki/Editing-Content#adding-and-editing-images).

### Glossary {#glossary}

⚠️ = Use caution, refer to relevant notes  
⛔️ = Don’t use 

#### Numerals

**24/7**  
Hyphenate (24-7) only when used as a modifier before a noun.

**2D / two-dimensional**

**3D / three-dimensional**

#### A

**A/B testing**

⚠️ **abort**  
Avoid using unless referring to a specifically named process. Instead, use words like “stop”, “exit”, “cancel”, or “end”.

**action buttons**

**action-based delivery**  
Lowercase except when referring to a UI element that is capitalized. 

⛔️ **ad hoc**
Don’t use. Use “one-time” or similar.

**AI**  
Preferred over "artificial intelligence" after the first mention.

**AI item recommendation**

**Alloys / Braze Alloys**  
Always capitalized.

**alphanumeric**  
Don't hyphenate.

**always-on**

**am**  
Lowercase when used for time (for example, "10 am"). See also [pm](#glossary).

**Amazon S3**

**Amazon Web Services (AWS)**  
Always capitalized. Spell out at the first mention, then it's fine to use the acronym.

**AMP for Email / Braze AMP for Email**

**Android**

**API / Application Programming Interface**  
Spell out at the first mention, then it's fine to use the acronym.

**API key**

**APNs / Apple Push Notification service**

**⛔️ app group**  
Don't use. App group has been renamed to workspace.

**Apple iOS platform**

**AppleWatch**

**.avro**

#### B

**behavior, behaviors**

**Benchmarks**

**beta**

**BI Insights**

**bingeing**

**Binge-watch**

**Bonfire / Bonfire community / Braze Bonfire community**  
Use “Braze Bonfire community” on the first mention, then it’s fine to use just “Bonfire” or “Bonfire community”.

**boolean**

⛔️ **blacklist**  
Don’t use. Instead, use “blocklist” or “denylist”. For the verb form of these words, consider rewording the sentence to remove the problematic term. For example:

>✅ **Recommended:** To block an existing property from being used in new messages, click **Manage Properties**. <br>
>⛔️ **Not recommended:** To blocklist an existing property, click **Manage Properties**. 

**Braze-to-Braze webhook**

**Business Intelligence (BI)**  
Spell out at the first mention, then it's fine to use the acronym.

#### C

**California Consumer Privacy Act (CCPA)** 
Spell out at the first mention, then it’s fine to use the acronym. See also [CCPA compliance (noun) / CCPA-compliant (adjective)](#ccpa-compliance)

**can**  
Use “can” to refer to an optional action or outcome. For example:

> ✅ **Recommended:** You can also upload and update user profiles with CSV files.
> ✅ **Recommended:** The import process can take a few minutes.

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

**CCPA compliance (noun) / CCPA-compliant (adjective)** {#ccpa-compliance}

**CEO, CFO, CMO, COO, CTO**

**churn**  
Use to refer to customer turnover or loss.

**churn prediction**  
Lowercase except when referring to the UI.

**checkbox**

**Check-in (noun) / check in (verb)**

**City x City**

**Cofounder**

**Content Cards / Braze Content Cards**

**Content Blocks**

**control group**

**conversion**

**conversion group analysis**  
Lowercase.

**Cordova**

**Currents / Braze Currents**  
Always capitalized.

**CRM / customer relationship management**  
Spell out at the first mention, then it's fine to use the acronym.

**cross-channel messaging / cross-channel personalization**

**C-suite**

**CSV / comma-separated values**

**custom attributes**  
Lowercase except when referring to a UI element that is capitalized.

**custom events**  
Lowercase except when referring to a UI element that is capitalized.

**customer attributes**

**customer behavior**

**customer data platform (CDP)**  
Lowercase.

**customer engagement**

**customer events**

**customer journey**

**customer permissions**

**customer retention**

#### D

**Dark Mode**

**dashboard / Braze dashboard**  
Use to refer to Braze as a platform. Use lowercase (dashboard not Dashboard).

**data-driven (adjective)**

**data privacy**

**data sheet**

**data streaming**

**DAU / Daily Active Users**

**Decision Splits**

**deep linking**

**Delay Messages**

**Downtime**

**drag and drop (verb) / drag-and-drop (adjective)** {#drag-and-drop}
Use when referring to dragging files into an upload zone.

**Drag-And-Drop Editor**  
Use title case when referring to the feature in the UI. Otherwise, use lowercase (drag-and-drop editor). Use the verb when referencing how customers can [drag and drop](#drag-and-drop) elements in the editor.

**drill down (verb) / drilldown (noun or adjective)**  
Use in content about data and the reports generated from them. 

**DTC / direct to consumer**

**dynamic content**

#### E

**early access**

⛔️ **e.g.**  
Don't use. Use the phrases “for example,“ "such as,” "like", or similar.

**eBook**

**eCommerce**  
Not “ecommerce” or “e-commerce”.  

**ecosystem**

**email**  
Not “Email” or “e-mail”.

**email deliverability**

**email reputation**

**EMEA (Europe, Middle East, and Asia)**

**emoji**  
Singular and plural form.

**end user (noun) / end-user  (adjective)**  
Prefer “your users” over “end users”.

⚠️ **ensure**  
Avoid using when talking about what a feature does. Refer to [Avoid guarantees](#avoid-guarantees) for more information.

**ESP / email service provider**

**event prediction**

**event properties / custom event properties**  
Lowercase except when referring to a UI element that is capitalized.

**exception events**

**extract**  
Use “extract” instead of “unzip” to refer to extracting files from a compressed folder.

**external ID**  
Not "External ID". When referencing code snippets, use external_id. 

#### F

**Facebook**

**FCM / Firebase Cloud Messaging**

**Firebrand / Firebrands**

**Forge [YEAR]**

**frequency capping**

**Fullscreen**   
When used as an adjective (for example, "Fullscreen in-app messages"), render without the hyphen.

#### G

**GDPR / General Data Protection Regulation**  
Spell out at the first mention, then it's fine to use the acronym.

**GDPR compliance (noun) / GDPR-compliant (adjective)**

**geofence**

**GIF**

**GitHub**  
Not “Github” or “github”.

**Google / google-able**

#### H

**High-performance**

**High-Value Actions**

**HQ / headquarters**

**HTML Email Editor**

**HTTP**

#### I

⛔️ **i.e.**  
Don't use. Use the phrase “that is” or similar.

**in-app messages**

**in-browser message (IBM)**

**infographic**

**install attribution**

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

**iOS**

**IP warming**

**iPad**

**iPhone**

**IT**

#### J

**JavaScript**

**JPEG / JPG**

**JSON / JavaScript Object Notation**

#### K

**Keynote (program) / keynote (noun)**

**kick off (verb) / kickoff (noun)**

⚠️ **kill**  
Avoid using unless referring to a specifically named process. Instead, use words like “stop”, “exit”, “cancel”, or “end”.

**KPI / key performance indicator**

#### L

**landing page**

**lifecycle**

**Lift-rate**

**LinkedIn**

**Liquid**  
Always capitalized.

**Live Preview**

**long term (noun) / long-term (adjective)**

**LTV / Lifetime Value**

#### M

**marketing technology**  
Preferred over "martech".

**MAU / Monthly Active Users**

**maximum**  
Not “max”.

**media library**  
Lowercase except when referring to a UI element that is capitalized.

**Microsoft**

**Microsoft Azure**

**ML / machine learning**

**mobile marketing**

**mobile marketing automation**

**mobile moment**

**mobile phone**

**multichannel campaign**  
Lowercase except when referring to a UI element that is capitalized. No hyphen.

**multi-language support**

**multivariate testing**

#### N

**N/A**  
Not “NA”. Use “N/A” as needed in tables to denote column or row content that does apply to a particular cell. In inline text, prefer the spelled out “not available” or “not applicable” for clarity.

⚠️ **new**  
Avoid using in product documentation and learning material, as this can quickly date your content. For more information, see [Future Features](#describing-limitations).

**NRT / near real-time (adjective) / near real time (noun)**

**NYC / New York City**

#### O

**on demand**

**onboarding**

**once**  
Use to refer to performing an action a single time. Don’t use “once” in place of “after” or "when".

**open rate (OR)**

**opt-in prompt**

**orchestration**

**OS / Operating System**

**OTT / Over-the-top media services**

⛔️ **out-of-the-box**  
Don’t use. Instead, use an alternative like “default”.

#### P

**partner, partners, partnership**

**persona (singular) / personas (plural)**

**personalization**

**personally identifiable information (PII)**

**Personalized Path**  
Use title case.

**Personalized Variant**  
Use title case.

**PhD / PhDs**

**pm**  
Lowercase when used for time (for example, "10 pm"). See also [am](#glossary).

**preceding**

**prediction**  
Lowercase unless preceded by “Braze”, such as “A Braze Prediction is…”.

**predictive analytics**

**Predictive Churn**  
Use title case. Predictive Churn is the product name, whereas customers create a [churn prediction](#glossary).

**Predictive Events**  
Use title case.

**Predictive Purchases**  
Use title case. Predictive Purchases is the product name, whereas customers create a [purchase prediction](#glossary).

**Predictive Suite**  
Use title case.

**preference center**  
Lowercase except when referring to a UI element that is capitalized.

**priming for location**

**priming for push**

**promotion code**  
Lowercase except when referring to a UI element that is capitalized. Don’t use “promo code”.

**purchase prediction**  
Lowercase except when referring to a UI element that is capitalized.

**purchase properties**  
Lowercase except when referring to a UI element that is capitalized.

**push action buttons**

**Push Max**  
Use title case.

**push notification**

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

**rate limiting**

**real time (noun) / real-time (adjective)**

**re-engagement**

⚠️ **regular expression / regex**  
Prefer the spelled-out version over its abbreviated “regex”. Don’t use “RegEx”.

**relationship marketing**

**retargeting**

**retention**

**rich push**

**right-click**

**right-swipe**

**ROI / return on investment**

#### S

**Sage AI by Braze™**

⛔️ **sanity check**  
Don’t use. Instead, use a term like “quick check” or “preliminary check”. Alternatively, introduce check-in instructions with a phrase like “Let's check to make sure everything is working”.

**scheduled delivery**  
Lowercase except when referring to a UI element that is capitalized.

**screencap**

**screengrab**

**SDK / Software Developer Kit**

**segment (audience)**

**Segment Extensions**  
Use title case.

**Segment Insights**  
Use title case.

**Segmentation**

**selection**  
As in, the feature within catalogs. Lowercase except when referring to a UI element that is capitalized.

**SF / San Francisco**

**Silicon Valley**

**silo, silos, siloed**

**simple survey**

**slideshow**

**Smartphone**

**Smartwatch**

**SMS**

**software as a service (SaaS)**   
Spell out at the first mention, then it’s fine to use the acronym.

**spam testing**

**SQL / structured query language**

**SQL Segment Extensions**  
Use title case.

**stickiness**

**streaming**

**string**  
For non-technical audiences, define a string as text that contains “alphanumeric characters”. For technical audiences, it’s fine not to define this term.

**subscription group**

**sunset, sunsetting**

#### T

**targeted response**

⚠️ **terminate**  
Avoid using unless referring to a specifically named process. Instead, use words like “stop”, “exit”, “cancel”, or “end”.

**third-party**

**time zone**  
Not "timezone".

**timestamp**

**touchscreen**

**triggered message**

**Twitter**

#### U

**UK / United Kingdom**

⛔️ **unzip**  
Don’t use. Instead, use “extract”.

**URL**  
Pronounced as the individual letters U-R-L, so write “a URL” rather than “an URL”. Use all caps. For plurals, use URLs.

**US / USA**  
No periods.

**use cases**

**user attributes / default user attributes**  
Use to refer to user data automatically captured by Braze.

**user profile**

**username**

⚠️ **utilize**  
Don’t use “utilize” when you mean “use”. Use “utilize” to refer to something being used beyond its original intended purpose. 

#### V

**variant**

⛔️ **via**  
Don’t use. Instead, use terms like “through” or phrases like “by means of” or “by way of”.

⛔️ **vice versa**  
Don’t use. Instead, use terms like “conversely” or a phrase like “the other way around”. 

**view-only**

⚠️ **vs.**  
Don’t use “vs.” as an abbreviation for “versus”. Instead, spell out the word.

#### W

**web messaging**

**web push**

**webhook**

**webinar**

**whitelabel**

⛔️ **whitelist**  
Don’t use unless referring to the UI. Instead, use “allowlist” or “safelist”. For the verb form of these words, consider rewording the sentence to remove the problematic term. For examples, see [blacklist](#glossary).

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

**WordPress**

**workspace**

**www**

#### Y

**YAML**  
Don’t use a file extension to refer to the type of file. For example, use “YAML file” instead of “.yaml file”.

**YouTube**

#### Z

**zip code**

**zip file / zipped files**

**ZIP**  
Don’t use a file extension to refer to the type of file. For example, use “ZIP file” instead of “.zip file”.
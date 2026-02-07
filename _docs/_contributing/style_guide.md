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

✅ Use visuals to help clarify complex subjects.  
**Example:** The user profile lifecycle image in the [User Profile Lifecycle article]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/#user-aliases) helps to illustrate a tricky concept.

✅ Create a clear information hierarchy.

**Example:** "This is an overview for how content is managed on Braze Docs. To learn more about a specific topic, choose the dedicated topic page in the navigation."

✅ Ruthlessly cut jargon and acronyms if possible. If not possible, define them.   
**Example:** "The Short Messaging Service (SMS) is used to send and receive brief text messages."

##### Empowering

What problem are you trying to solve with your writing? Keep that problem in mind while creating any content.

* Explain the “why” and “how” to give users the confidence to take action.   
* Be specific when explaining benefits, and be clear about what is and isn’t possible.   
* Offer practical advice and sincere encouragement. 

###### Guidelines

✅ Make it easy to find the happy path. 

**Example:** "When you stop a Canvas, the following applies: 1. Users will be prevented from entering the Canvas. 2. No further messages will be sent out, despite where a user is in the flow.  3. **Exception:** Email Canvases won't immediately stop." 

✅ Provide examples, use cases, and templates that simplify or elevate the user’s work. 

**Example:** "`IInAppMessageManagerListener` also includes delegate methods for clicks on the message itself or one of the buttons. A common use case would be intercepting a message when a button or message is clicked for further processing."

##### Human

Informational writing is inherently dry—we want readers to focus on the content, not the delivery. We can still write in a way that will help our readers process the information they’re consuming and make it more likely that they’ll internalize the knowledge. Be human, let your personality show, and be memorable. 

* Aim for a conversational tone rather than a formal one.   
* Focus on the user; respect their situation and emotional state.   
* Actively center the human experience, not the machine state. 

###### Guidelines

✅ Thoughtfully apply brand tone and assets.   
**Example:** "Integrating with Braze is a worthwhile process. But you’re smart. You’re here. Clearly, you already know that."

✅ Apply [accessibility best practices](#accessibility) for both visual and verbal content.   
**Example:** Replacing idioms like "out-of-the-box" with "default" make your text more accessible to English second language speakers.

✅ Provide consistent support across the user journey.  
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
* [Links to download files](#links-for-file-download) should indicate clicking the link will download the file, as well as the file type (PDF, CSV, etc.)  
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

| Do | Don’t |
| :---- | :---- |
| Press ✅ Save. | Press the green Save icon. |
| Press the green checkmark icon. | Press the green icon next to the red Cancel button. 
| Press the green icon. | |

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
* **Users:** Generally reserved for a specific statistic that depends on “user” metrics (such as “user retention”). When referring to “users” in our content, first aim to be more specific. Think shoppers, consumers, patients, players, etc.

##### Departments and Teams

Capitalize the names of departments or teams. Do not capitalize “team” or “department.”

| Do | Don’t |
| :---- | :---- |
| Marketing, Business Intelligence Product team | marketing, business intelligence Product Team |
| Revenue department |  Revenue Department |

##### Disability

Don’t refer to a person’s disability unless it’s specifically relevant to your writing. In that case, be considerate and ask whether the subject prefers identity-first or person-first language. When referring to a subject with a disability, do not use terms like “handicapped.”

Ableist language includes words or phrases such as “crazy”, “insane”, “blind to” or “blind eye to”, “cripple”, “dumb”, and others. Choose alternative words depending on the context.

##### Disease

When describing an illness, avoid words like “suffer,” “struggle,” or “victim.” Aim to be neutral and matter-of-fact. 

| Do | 
| :---- |
| She was diagnosed with cancer. |
| They’re living with HIV. |
| He recovered from his stroke. |


##### Inclusivity in Content

Highlight and represent a diverse community. Be mindful and inclusive when involving our customers, speakers, industry experts, and Braze team members. 

##### Job Titles

When it comes to job titles, we veer off-course from AP Style. In all cases, we capitalize job titles when referring to someone specifically. 

###### Job Title with Company Name

Capitalize formal job titles when they come before or after a person’s name. We format them three ways:

1. **[Formal Title]** at **[Company Name]** + **[Full Name]**

| Do | Don’t |
| :---- | :---- |
| Creative Director at PantsLabyrinth David Bowie  | creative director at PantsLabyrinth David Bowie |

{: start="2"}
2. **[Full Name]** + comma + **[Formal Title]** at **[Company Name]** 

| Do | Don’t |
| :---- | :---- |
| David Bowie, Creative Director at PantsLabyrinth | David Bowie, creative director at PantsLabyrinth |

{: start="3"}
3. **[Company Name]** + **[Formal Title]** + **[Full Name]** 

| Do | Don’t |
| :---- | :---- |
| PantsLabyrinth Creative Director David Bowie | PantsLabyrinth creative director David Bowie |

###### Job Title without Company Name

When referring to a specific person by formal title, capitalize their formal title and name like so:

1. **[Formal Title]** + **[Full Name]**

| Do | Don’t |
| :---- | :---- |
| CEO Robin Fenty | Chief executive officer Robyn Fenty |

{: start="2"}
2. **[Formal Title]** + comma + **[Full Name]**

| Do | Don’t |
| :---- | :---- |
| SVP, Product, Robin Fenty | senior vice president, product, Robyn Fenty |

###### Other

Formal titles are “at [COMPANY].” Founders and Cofounders are “of [COMPANY].” Formal titles and occupations on their own do not need to be capitalized.

| Do | Don’t |
| :---- | :---- |
|  I wrote to their chief data officer. | I wrote to their Chief Data Officer |
| We spoke with several business intelligence analysts. | We spoke with several Business Intelligence Analysts. |
| Contact your Braze account manager.  |  I wrote to their Chief Data Officer Contact your Braze Account Manager. |

Adhere to gender-neutral job titles unless gender has been already established.

| Do | Don’t |
| :---- | :---- |
| salesperson  | salesman/saleswoman |

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

| Do | Don’t |
| :---- | :---- |
| Muslim American | Muslim-American |
| Cuban American  | Cuban-american |

Capitalize the proper names of ethnicities, nationalities, peoples, and tribes.

| Do | Don’t |
| :---- | :---- |
| Cambodian | cambodian |
| Black Americans | black Americans |

Capitalize the names of religions or religious terms.

| Do | Don’t |
| :---- | :---- |
| Bahá’í Faith | bahá’í faith
| Buddhist | buddhist |

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

| Do | Don’t |
| :---- | :---- |
| _Spell out uncommon abbreviations at the first mention_ | _Spell out common abbreviations_ |
|  Top-level domain (TLD) |  Portable Document Format (PDF)
| Universally unique identifier (UUID) | Universal Serial Bus (USB) |


Treat abbreviations as regular words when making them plural, and don't add an apostrophe—for example, APIs and SDKs. The same goes for which article (a or an) you use—look at how you pronounce the abbreviation. When an abbreviation begins with a vowel sound, use “an”; for consonant sounds, use “a”. 

| Do |
| :---- | 
| _Use articles depending on how the abbreviation is prounounced, not spelled_ |
| an ISP |
| a DLL | 
| an HTML site |
| a CSV file |

#### Active Voice {#active-voice}

We use the active voice at Braze when possible. Active voice is our gold standard. Avoid passive voice, in which it can be difficult to determine who or what is performing a particular action.

To see if your sentence is in a passive voice, insert “by somebody” after the verb. If the sentence makes sense—it’s most likely in the passive voice.

| Do | Don’t |
| :---- | :---- |
| _Use active voice_ | _Use passive voice, if possible_ |
| Braze connects consumers to the brands they love. | Consumers are connected to the brands they love. |
| Braze requires employees to keep their addresses up to date. | Employees are required to keep their addresses up to date. |
| Company administrators can configure authentication requirements for signing into Braze. |  Authentication requirements for signing into Braze can be configured by company administrators. |

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

| Do | Don’t |
| :---- | :---- |
| _Use articles depending on how the anteceding word is pronounced._ |
| an hour |
| a minute |
| an FAQ article |
| a LAB course |

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

| Do | Don’t |
| :---- | :---- |
| _Ensure a pronoun clearly references its antecedent_ | _Use ambigous pronoun references_ |
| If you type text in the field, the text doesn’t change. | If you type text in the field, it doesn't change. |
| She told Sarah that Sarah’s answer was incorrect. | She told Sarah that her answer was incorrect. |
| You can’t edit an archived campaign. Unarchive a campaign to edit it. | You can't edit an archived campaign. Unarchive it to edit it. |

##### Optional Pronouns

To add additional clarity to your writing and to aid in localization, use pronouns such as “that”, “which”, and “who”.

| Do | Don’t |
| :---- | :---- |
| _Use "that", "which", and "who" to add additional clarity._ |  |
|  Right-click the link that you want to open. | Right-click the link you want to open. |
| From here, you can choose which Tinyclues cohort that you want to include. | From here, you can choose a Tinyclues cohort you want to include. |

#### Capitalization {#capitalization}

Avoid unnecessary capitalization. In most instances, use sentence case. Title case should only be used for proper nouns or feature names (unless otherwise specified, see [Glossary](https://confluence.braze.com/pages/viewpage.action?spaceKey=MAR&title=Braze+Glossary)).

| Do | Don’t |
| :---- | :---- |
| _Use lowercase for writing out website URLs and email addresses_ ||
|  www.braze.com/docs | www.Braze.com/docs |
|  sample@email.com | SAMPLE@EMAIL.COM |

| Do | Don’t |
| :---- | :---- |
| _Use lowercase directionals_ ||
|  north, south, east, west |  North, South, East, West |

| Do | Don’t |
| :---- | :---- |
| _Capitalize specific regions, and use all capitals for abbreviated regions_ ||
|  the Northwest | the northwest |
| Southern Connecticut | southern Connecticut |
| Eastern Europe | eastern Europe |
| APAC, EMEA |  Apac, emea |

##### Brands and Products

When referring to a brand or product, use the capitalization the brand uses. In most cases, capitalize the names of brands (Grindr, Walmart) and products (Benchmarks, Looker Blocks). It’s fine to begin a sentence with lowercase if the first word is the stylized name of a brand like eBay or iTunes. 

For intercaps, always refer to the usage preferred by the brand in print (OkCupid, YouTube). Do not use intercaps that only appear in logos or graphic design treatments (Amazon). 

#### Clause Order {#clause-order}

If you want to tell the reader to do something in a specific circumstance, try to mention the circumstance before you provide the instruction. This lets the reader skip the instruction if the circumstance doesn't apply.

| Do | Don’t |
| :---- | :---- |
|  For troubleshooting steps, see Campaign FAQs. | See Campaign FAQs for troubleshooting steps. |
| To archive your campaign, click the gear icon and select Archive. | Click the gear icon and select Archive to archive your campaign. |

#### Combining Forms {#combining-forms}

[Hyphenate](#hyphens) combined forms when the phrase is used as an adjective before the noun. 

**Example:** A one-of-a-kind item

#### Contractions {#contractions}

A contraction is a shortened version of a word or phrase. Use contractions to keep an approachable and informal tone. However, do not use noun and verb contractions or double contractions, or a combination of two contractions. These can disrupt the flow and coherency of the sentence.

| Do | Don’t |
| :---- | :---- |
| _Use contractions_ | _Use noun and verb contractions_ |
|  If you’re an admin, you can manage your company’s contact information. | Braze’ll now support Shoptify integration.
| You can’t edit an archived campaign. Do Use contractions. | You mightn’t’ve seen the restricted upload size. |

#### Dangling and Misplaced Modifiers {#dangling-and-misplaced-modifiers}

Modifiers are words of phrases that modify other words or phrases. A dangling modifier doesn’t modify any subject in the sentence. A misplaced modifier is placed far away from the subject that it’s meant to modify. Essentially, dangling and misplaced modifiers may cause confusion by connecting to the wrong part of the sentence.

Writing with an active voice will help prevent the use of dangling and misplaced modifiers. Be sure to use a modifier that clearly modifies. 

| Do | Don’t |
| :---- | :---- |
| _Keep sentence short and concise. Use active voice._ | _Use lengthy sentences with modifiers that can cause confusion_ |
|  Customers must set up their SAML settings. | You may have test messages on your campaigns that can be deleted. |
| Make sure to save your campaign drafts. | On the way home, Sarah found a gold man’s stopwatch. |

#### Prepositions {#prepositions}

There’s nothing wrong with ending a sentence in a preposition when it improves readability. Place a preposition or prepositional phrase where it makes the most sense in a sentence. If you’re having difficulty, read the sentence out loud and see if it sounds natural.

| Do | Don’t |
| :---- | :---- |
| Each option corresponds to the priority the notification will be displayed in. | Each option corresponds to the priority in which the notification will be displayed. |
| For details, see the SDK documentation for the platform you’re working with. | For details, see the SDK documentation for the platform with which you’re working. |

#### Present Tense {#present-tense}

Use present tense instead of future tense. Present tense conveys immediacy and demonstrates confidence. Avoid using “will” or hypothetical “would”, especially when referring to the result of user action.

| Do | Don’t |
| :---- | :---- |
| Archived subscription groups cannot be edited and no longer appear in segment filters. | Archived subscription groups cannot be edited and will no longer appear in segment filters. |
| Using a short code is the most reliable number type for including links. | Using a short code would be the most reliable number type for including links. |

Only use future tense when you’re actually talking about the future. Avoid predicting [future features](#describing-limitations). 

#### Profanity {#profanity}

Keep it PG. This has less to do with morality than the fact profanity can be divisive and off-putting to an audience as broad and international as ours. There’s also a case to be made that sometimes profanity is a cover-up for half-baked writing. That’s simply not our vibe. 

#### Plurals in Parentheses {#plurals-in-parentheses}

Do not use plurals in parentheses. Instead, use the plural or singular form of the word.

| Do | Don’t |
| :---- | :---- |
| Customize your campaign with the following filters. | Customize your campaign with the following filter(s). |

#### Second Person and First Person {#second-person-and-first-person}

Use second person in your instructions instead of first person—”you” rather than “we”. 

Refer to the reader as the one doing the action. Strike a conversational tone—most readers are coming to documentation when they don’t have immediate access to a support agent. Make it feel as if the article is talking to them instead. 

| Do | Don’t |
| :---- | :---- |
| If you want to add a variant... | If we want to add a variant... |

If you’re telling the reader to do something, then you can omit the “you” and use the imperative.

| Do | Don’t |
| :---- | :---- |
| Upload the CSV file. | You can upload the CSV file. |
| Click Submit. | You’ll need to click Submit. |

When using second person, make sure you know who the audience of the document is, and to be consistent about who you’re talking to.

#### Slang and Idioms {#slang-and-idioms}

We’re a plainspoken bunch. Avoid using trendy slang or idioms that speak too specifically to a singular audience. It can also quickly date materials, and make it difficult to localize content. 

#### Spelling {#spelling}

Use American English spelling for words that differ in British English. If you’re not sure how to spell a word, first refer to the [Glossary](#glossary). If the word isn’t listed there, then refer to [Merriam-Webster’s Collegiate Dictionary](https://www.merriam-webster.com/).

For words that are accented or contain special characters, make sure to correctly follow the dictionary spelling. In some cases, unintentionally omitting these accents can result in a different word. For example, “resume” means to begin again after stopping, whereas “résumé” is an account of one’s qualifications. 

### Punctuation {#punctuation}

#### Ampersands {#ampersands}

Don’t use an ampersand (&) in place of “and” in text or headings unless you are referring directly to the user interface.

| Do | Don’t |
| :---- | :---- |
| Drag-And-Drop Editor | Drag & Drop Editor |
| SMS and MMS | SMS & MMS |

#### Apostrophes {#apostrophes}

We use an apostrophe most often to make a noun possessive. 

* For singular nouns that end in S, it’s fine to place another S after the apostrophe.  
 * **Example:** Chris’s, business’s, alias’s  
* For plural nouns that end in S, add an apostrophe but no additional S.  
 * **Example:** users’

#### Colons {#colons}

Use colons at the end of an introductory phrase that precedes a list or example. Your introductory sentence should be able to stand alone as a complete sentence. This is for both accessibility and localization purposes, as it’s difficult to translate sentence fragments.

| Do | Don’t |
| :---- | :---- |
| The general structure is as follows: | The general structure is: |

If the text preceding the colon is bold, bold the colon as well.

| Do | Don’t |
| :---- | :---- |
| **Scheduled:** Time-based entry. | **Scheduled**: Time-based entry. |

If the text preceding the colon is code text, don’t include the colon in the code text unless it is part of the code element.

| Do | Don’t |
| :---- | :---- |
| `user_alias_label`: A common label to group user aliases with. | `user_alias_label:` A common label to group user aliases with. |

You can also use a colon to join two related phrases in a sentence. However, use colons for this sparingly. Two sentences are generally more readable. 

| Do |
| :---- |
| Coming up next week: we're going on a tour of the West Village. |


#### Commas {#commas}

Braze uses the Oxford (serial) comma when writing instructions or learning content. Use a comma before the last conjunction to separate items in a series.

Use a comma after an introductory phrase.

If a coordinating conjunction (words like “and”, “but”, “or”, “yet”, “so”) separates two independent clauses, place the comma after the first clause and before the conjunction. However, this comma is not necessary if both clauses are short.

For example, here are two independent clauses:

* “All fields are optional.”  
* “You must specify at least one field.”

The sentence when using a coordinating conjunction “but” is “All fields are optional, but you must specify at least one field.”

If an independent clause and a dependent clause are used in the same sentence, do not use a comma to separate them. Only use a comma in this scenario if the sentence can be misinterpreted without the comma placement.

| Do | Don’t |
| :---- | :---- |
| Push subscriptions states are filters and can allow users to edit notification preferences. | Push subscriptions states are filters, and can allow users to edit notification preferences. |

#### Dashes {#dashes}

##### Em Dash

Use an em dash (—) when using a dash in a sentence to indicate a separate thought or interruption. Don’t put any spaces before or after the em dash. Don’t use an em dash where a comma or parenthesis would work just as well.

Refer to your operating system for how to type an em dash:

* **macOS:** Press Option + Shift + Hyphen.  
* **Windows:** Turn num lock on, then hold down the left Alt key and type 0151 on the num pad.

##### En Dash {#en-dash}

Use an en dash (–) to indicate a range of numbers, as a minus sign, or to indicate negative numbers. Don’t put any spaces before or after the en dash except for when it’s used as a minus sign. Don’t use a hyphen (-). 

| Do | Don’t |
| :---- | :---- |
| _Use an en dash for a range of numbers_ | _Use a hyphen_ |
| 2018–2021 | 2018-2021 |

Don’t use an en dash for ranges of time. For more details, refer to the section [Dates and Times](#dates-and-times).

| Do | Don’t |
| :---- | :---- |
| _Use an en dash for a minus sign and include spaces surrounding the en dash_ | _Use a hyphen_ |
| 15 – 5 = 10 | 15-5=10 |

| Do | Don’t |
| :---- | :---- |
| _Use an en dash for negative numbers_ | _Use a hyphen_ |
| –30 | -30 |

Refer to your operating system for how to type an en dash:

* **macOS:** Press Option + Hyphen.  
* **Windows:** Turn num lock on, then hold down the left Alt key and type 0150 on the num pad.

#### Ellipses {#ellipses}

An ellipsis is a series of three periods (...) that indicates an omission of one or more words. In general, avoid using ellipses when possible while writing instructions or learning content. 

#### Exclamation Points {#exclamation-points}

An exclamation point can be used sparingly for an informal tone. However, avoid overly using exclamation points throughout text. Instead, consider using Alerts.

| Do | Don’t |
| :---- | :---- |
| _Use exclamation points for an informal tone for reminders and introductions_ | _Use exclamation points for indicating warning or caution to readers_ |
|  Be sure to save your changes before leaving the page! | Users must receive one or more messages from a step to be counted as a unique recipient! |

#### Hyphens {#hyphens}

Hyphens can help the reader gain more clarity in a sentence by linking words in a phrase together. Here are a few guidelines for getting it right.

Use hyphens for compound modifiers that will help the reader understand the subject more clearly.

| Do | 
| :---- | 
| real-time data streaming |

Use hyphens to link a phrase, with a space between the modifier and subject. 

| Do | 
| :---- | 
| All-in-one solutions |

Use hyphens for a phrase that modifies a subject. There’s no need to use a hyphen if the phrase is the subject.

| Do | Don’t |
| :---- | :---- |
| It was a well-known fact. | That fact is well-known |

Don’t use hyphens in place of an em dash to create a pause in a sentence.

| Do | Don’t |
| :---- | :---- |
| ...third-party integrations—such as Slack—and automate... | ...third-party integrations-such as Slack-and automate... |

Don’t use a hyphen after an adverb. Keep the words separate.

| Do | Don’t |
| :---- | :---- |
| Hastily made | Hastily-made |

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

| Do | 
| :---- | 
| _Use a semicolon to break up a sentence with two related independent clauses_ |
| The cat slept through the storm; the dog cowered under the bed. |

Semicolons can be used to separate list items if one (or more) of the list items contains a comma.

| Do |
| :---- |
| _Use a semicolon to break up a longer sentence_ |
| Jane Lang, our moderator; Simon Mayer, CEO and Cofounder of PantsLabyrinth; and Kara Seberg, CMO of Yachtr. |

#### Slashes {#slashes}

There are two types of slashes: backward (\\) and forward (/). Do not use slashes to indicate alternative words or examples (“and/or”). 

Use slashes as needed in file paths and URLs.

| Do | Don’t |
| :---- | :---- |
| _Use a slash for file paths_ | _Use a slash to separate alternatives_ |
| `/campaigns/data_series` | you/your customers |

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

| Verb | Usage | Example |
| :---- | :---- | :---- |
| Open | {::nomarkdown}<ul><li>Opening apps</li><li>Opening files and folders</li></ul>{:/} | {::nomarkdown}<ul><li>Open Droidboy.</li><li>Open the braze.xml file.</li></ul>{:/} |
| Close | {::nomarkdown}<ul><li>Closing apps</li><li>Closing files and folders</li></ul>{:/} | {::nomarkdown}<ul><li>Close Droidboy.</li><li>Close the braze.xml file.</li></ul>{:/} |
| Go to | {::nomarkdown}<ul><li>Going to a specific page in the UI (tab, page, section)</li><li>Going to a webpage</li></ul>{:/} | {::nomarkdown}<ul><li>Go to the <strong>Segments</strong> page, and click…</li><li>Go to example.com to sign up.</li></ul>{:/} |
| >  | Following a sequence of steps when all steps are of the same type. | Go to **Segments** > **Segment Insights**. |
| Choose | Making a decision that is subjective, strategic, open-ended, or complex. | Choose a campaign strategy. |
| Select | {::nomarkdown}<ul><li>Selecting a checkbox</li><li>Selecting items from a dropdown</li><li>Selecting a tab</li><li>Making a simple decision</li></ul>{:/} | {::nomarkdown}<ul><li>Select <strong>Show Password</strong>.</li><li>Select a data type from the dropdown.</li><li>On the <strong>Manage Settings</strong> page, select the <strong>Custom Events</strong> tab.</li><li>Select an image.</li></ul>{:/} |
| Clear | Clearing the selection from a checkbox. | Clear the **Show Password** checkbox. |
| Click | Clicking an element in the UI. | Add a custom attribute and click **Save**. |
| Turn on | Enabling a toggle option | Turn on the **List-Unsubscribe header**. |
| Turn off | Disabling a toggle option | Turn off **Inline CSS on New Emails by Default**. |
| Enter | Typing a value. | {::nomarkdown}<ul><li>In the text field, enter the name of your custom attribute.</li><li>Enter "Braze" as the source name.</li></ul>{:/} |

#### Describing Limitations {#describing-limitations}

Write candidly about the product's limitations, without distortion or manipulation. Readers will react in an intense fashion to being manipulated, hoodwinked, and otherwise bamboozled, and this will jeopardize the documentation's efficacy as a source of utilitarian truth. Customers rely on documentation to understand the limits of the system to which they are building so that they can use Braze successfully.

At the same time, support the intentionality of the product's development by framing limitations with appropriate, positive context.

* If there is a soft limitation (for example, an API rate limit), frame the limitation by talking about the **default limit** or **starting allotment.**  
* Provide a meaningful path forward to navigate soft limits. Provide examples of these workarounds as appropriate.  
 * For example, Braze uses sizing exercises during onboarding to help customers understand how things such as data points are used by other businesses of a similar size. When discussing data points, it is appropriate to talk about the sizing exercise at the same time.  
* It is better to describe a path forward in a positive way than as a mitigation.   
 * For example, instead of saying "Braze does not allow customers to do this on their own. The Support team must activate this feature for you," say, "To activate this feature, contact the Support team."  
* Do not over-rely on the same stock phrases to navigate soft limits. If a user reads "Talk to your customer service representative" over and over, the advice becomes meaningless.  
* If there is a hard limitation, try to describe the rationale behind this limit.  
 * For example: "There is a limit of 200 active, action-based in-app message campaigns per app group to optimize the speed of message delivery and to prevent timeouts. …The average Braze customer has a total of 26 campaigns active at once—so it's unlikely that this limitation will impact you."  
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

Don't use phrases that might incite fear, uncertainty, or doubt with readers. Provide a clear path forward, such as what the deprecated feature will be replaced by or an alternative solution.

#### General vs Specific {#general-vs-specific}

As a best practice, write articles that discuss functionality in a generally applicable way. If more detail is needed for specific cases or exceptions, create a separate section (or separate article if the content is web article length, ~500 words) that outlines this outlier. Create cross-references from the general article to the specific to help users connect these concepts.

Avoid creating duplicated or repetitious content for different channels or features. If repetition is needed, use `includes` files and other [reusable content best practices]({{site.baseurl}}/contributing/content_management/reusing_content).

**As an example:** A common use case for Braze customers is to retarget users who have previously interacted with their messaging. Retargeting users can be done through many engagement tools, including campaigns, Canvases, landing pages, and segments. Retargeting users can be done through many channels: WhatsApp, SMS, Content Cards, email, push notifications, etc. Often, customers will try to reengage a user through a separate channel than one previously used.  
Instead of creating one article for each engagement tool and each channel, create a single article that discusses strategies for retargeting users and outlines all the options available. If there are special considerations for specific channels/tools, create a separate article that outlines those considerations and house it within that documentation section. Create cross-references between the general article and the specific article.

#### Metadata and YAML {#metadata-and-yaml}

Articles in Braze documentation require certain metadata for search and index purposes. For information on what metadata is required, refer to the GitHub page on [YAML and Metadata Layouts](https://github.com/braze-inc/braze-docs/wiki/YAML-%26-Metadata-Layouts).

#### Naming Conventions {#naming-conventions}

When naming articles and filenames, make sure to describe the general topic in the title. Always include a keyword and brief description that will be easily understood by readers, especially with article titles. 

For filenames, keep the name brief and avoid using articles (a, an, the). Separate each word with an underscore (_).

| Do |
| :---- |
| Targeting users |
| Creating an email campaign |
| API errors and responses |
| sms_historical_performance.png |
| push_notification_test.png |

In general, for articles and image files, use the same spelling and capitalization as the referenced article and files. For guidelines on article title styling, refer to [Headings and Titles](#headings-and-titles).

When referring to a specific file, use the same spelling of the filename and code font. For formatting details, refer to the GitHub page on [Special Formatting](https://github.com/braze-inc/braze-docs/wiki/Special-Formatting). 

#### Procedures and Instructions {#procedures-and-instructions}

This section covers some guidelines to keep in mind when writing instructions for procedures in the Braze dashboard. 

General guidelines:

* **Use the right tone.** For instructions, keep your writing short, to the point, and task-oriented. Your writing doesn’t need to be terse or dry, but it should be direct. When introducing tasks or subtasks, you can use a more informal tone to add variety. Avoid using “please” to keep the tone informal. Make liberal use contractions to keep your tone approachable.   
* **Follow parallel heading format.** Pick one format for your headings and stick to it. Keep your content scannable and predictable. In general, use gerunds (ing-words) for page titles, and imperative verbs for task-based headings. 

Before instructions:

* **Use introductions and prerequisites.** Don’t jump straight into the steps. Instead, give context on what your article or section will cover, and provide any information the reader needs to know before they scan the instructions. Make sure any prerequisites are listed at the top of the document.  
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

Button labels should be clear and predictable—the user should know what action will occur upon clicking the button. Use sentence case for button labels, and lead with a strong verb. If it may be unclear what the verb is referring to, use the format [verb] + [noun]. 

| Do | Don’t |
| :---- | :---- |
| Sign up | Sign Up
| Log in | Log In
| Subscribe | SUBSCRIBE 
| Learn more | More |

Omit unnecessary words and articles, such as “a”, “an,” or “the”.

#### Callouts and Alerts {#callouts-and-alerts}

Alerts, also known as callouts, are used to draw attention to information that is helpful to the reader. There are four alerts types that are used in our documentation:

* Important  
* Note  
* Tip  
* Warning

Use alerts sparingly throughout articles. For more information, refer to [Best Practices for Alerts](https://docs.google.com/document/d/1AhUhMvCZJLsIZjw52MyPJTBc8ewKAtne3XB1fsO_PoU/edit).

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

| Do |
| :---- |
| _Use the preferred date format._ | 
| September 2021 |
| September 15, 2021 |
| Wednesday, September 15, 2021 |

For date ranges, use an [en dash](#en-dash).

| Do | 
| :---- |
| 2010–2021 |

Use an en dash for date ranges.

Use numerals with am or pm, followed by a space, followed by the time of day (am or pm). Remove the minutes from on-the-hour time.

| Do | Don’t |
| :---- | :---- |
| _Use numerals with am or pm._ | _Use minutes for on-the-hour time (unless it's a range)._ |
| 12 pm | 12:00 P.M. |

For ranges of time, use an en dash to separate. Do not add spaces before or after the en dash.

| Do | Don’t |
| :---- | :---- |
| _Use an en dash for range of time._ | _Use minutes for ranges of time._ |
| 12:45–2:30 pm |  | 8:00 am–2:30 pm |

For reference in instances where parties from other time zones will be included (like webinars, meetings, or events), indicate the time zone as noted below:

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

When creating figures and images, refer to the [Image Copy Style Guide](https://docs.google.com/document/d/e/2PACX-1vRJSkwcjmjrTfLDagZccLpOMMyh5NN5SXRZSjz12cRAHbX4OrUmhvCmYpf_p5YB-9r4_jSOQLkicQIH/pub). Never include personally identifiable information (PII) in figures or images.

##### Alt Text {#alt-text}

Always include alt text with images. Screen readers announce alt text to explain images to people with loss of vision. As such, your alt text must convey all the key information depicted in the image.  
Use the following guidelines when writing alt text:

* Use [plain language](https://www.plainlanguage.gov/guidelines/).  
* Write in complete sentences, and use sentence case.  
* Omit unnecessary words.  
* Don’t include “image of” or “picture of”. It’s already understood that you are referring to an image.   
* Don’t include special characters. For example, instead of ampersands (&), use the word “and” written out.

| Do | Don’t |
| :---- | :---- |
| Custom Events settings page in the Braze dashboard with Add Report highlighted. | A screenshot of the Manage Settings > Custom Events page in the Braze dashboard with the option to add a report highlighted. |

Leave alt tags explicitly blank (alt="") if the image is adding a redundant visual component to what is explained in the text. 

Adding alt text to every image does not automatically make webpage content easy to navigate and consume. Redundant visuals are powerful for sighted users because visual information is easy to understand and remember. However, alt text describing redundant images can be unnecessary for users who can’t see the image because every page element demands equal attention from screen-reader users to determine if it’s useful for their task.

##### Example company names

If possible, take screenshots from [dashboard-06](https://dashboard-06.braze.com/) so that you’re using one of the FakeBrandz company names.

#### File Types and Filenames {#file-types-and-filenames}

When you’re referring to a file type, use the standard name of the type. If the file type is an acronym, refer to the file type in all caps. 

| Do | Don’t |
| :---- | :---- |
| _Use the standard name of the file type_ | _Use the file extension_ |
| CSV | .csv |
| executable file | .exe |
| GIF | .gif |
| JAR | .jar |
| JPEG | .jpg, .jpeg |
| JSON | .json |
| PDF | .pdf |
| PNG | .png |
| Python file | .py |
| Bash file | .sh |
| text file | .txt |
| YAML | .yaml |
| ZIP | .zip |

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

| Do | Don’t |
| :---- | :---- |
| Click **Add Languages**. | Click the **Add Language**s button. <br><br> Click “Add Languages”. |

If the label ends with a colon or ellipsis, omit the ending punctuation. 

| Do | Don’t |
| :---- | :---- |
| Click **Save as** | Click **Save as…** |

If a button is an icon, include the name of the button as shown in the tooltip. If a button with an icon doesn't include a tooltip, submit a request that a tooltip be added.

| Do | Don’t |
| :---- | :---- |
| Click ➕ **Add**. | Click the ➕ icon.  |

##### Checkboxes {#checkboxes}

When referring to a checkbox, use bold text for the checkbox label. Don’t include the word “checkbox” unless clarity is needed. Prefer the terms “select/clear” versus “check/uncheck”.

| Do | Don’t |
| :---- | :---- |
| Select **Send campaign to users in their local time zone**. | Check **Send campaign to users in their local time zone**. | 
| Clear the **Exit** checkbox. | Uncheck the **Exit** checkbox. |

##### Command-line commands and options {#command-line-commands-and-options}

When referring to command-line commands or options, use code formatting. Match capitalization to how it appears, or how it must be typed. 

##### Dialog boxes (Modals) {#dialog-boxes-(modals)}

Avoid referring to dialog boxes by name unless clarity is needed. Instead, describe what the reader needs to do. If you refer to a dialog box, use bold text for the name of the dialog box and match the capitalization of the UI.

| Do | Don’t |
| :---- | :---- |
| Click **Upload** then select a file to upload. | Click **Upload** and use the **File Upload** dialog box to select a file to upload. |

##### Error messages {#error-messages}

When referring to error messages that a reader may encounter, encapsulate the error message in quotation marks. For longer error messages, use a block quote.

| Do | Don’t |
| :---- | :---- |
| “Push Bounced: MismatchSenderId” | *Push Bounced: MismatchSenderID*<br><br>`Push Bounced: MismatchSenderID` |

##### Filter and operator names {#filter-and-operator-names}

When referring to the names of filters and operators for segments or other areas of the dashboard, use code text. Match the case of the UI, including elements that are in all caps such as `OR` and `AND` operators. 

| Do | Don’t |
| :---- | :---- |
| Select the `First Used App` filter and… | Select the **First Used App** filter and… |
| Combine filters with the `OR` operator. |  Combine filters with the “OR” operator. |

##### Folder and Filenames {#folder-and-filenames}

When referring to folder names and filenames, use code text. 

| Do | Don’t |
| :---- | :---- |
| Open the `braze.xml` file. | Open the **braze.xml** file. |

##### Key names and combinations {#key-names-and-combinations}

When referring to key names or key combinations, use the [HTML `<kbd>` tag](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/kbd). This denotes textual user input from a keyboard, voice input, or any other text entry device. If you’re working in an editor that doesn’t support custom HTML, use [code text](#code-in-text) instead.

Spell out the names of keys such as Command, Control, Option, and Shift. Don't use symbols for those keys.

| Do | Don’t |
| :---- | :---- |
| Press **Option**. | Press ⌥. |

For key combinations, use a plus (+) sign between keys, but omit the plus from any special formatting. 

| Do | Don’t |
| :---- | :---- |
| Press **Option + F12**. | Press ⌥ + F12. |

For example, this is how keyboard tags appear in Braze documentation:  
To stop the command, press **Control + C**.

##### Metrics {#metrics}

When referring to a metric in a table or glossary entry, use initial caps with no special formatting. When referring to a metric in a sentence, use initial caps with italics (such as *Machine Opens*).

##### Pages

Use the term page when referring to a web page in general, or a specific page on the Braze dashboard. When referring to a page name, use the format “the [label] page” and bold the name of the page.

| Do | Don’t |
| :---- | :---- |
| Go to the Segments page. | Go to the “Segments” page. |

##### Permission names {#permission-names}

When referring to names of user permissions within the dashboard, enclose the permission name in quotes.

{% alert note %}

Currently we are using title case to match the formatting of the dashboard. There is a plan to update the permission names within the UI to sentence case to match our standards. 

{% endalert %}

##### Tabs {#tabs-1}

When referring to a tab, use the format “the [label] tab” and bold the name of the tab.

| Do | Don’t |
| :---- | :---- |
| Go to the **Manage Settings** page and select the **Tags** tab. | Go to the “Manage Settings” page and select the “Tags” tab. |

##### Text input {#text-input}

When instructing a reader to type a specific string of text, enclose the text in quotes.

| Do | Don’t |
| :---- | :---- |
| In the **Name** field, enter “Lapsing Users” |  | In the **Name** field, enter `Lapsing Users`. |

#### Frequently Asked Questions (FAQs) {#frequently-asked-questions-(faqs)}

Order the FAQs by starting with the information that people most want or need to know, and then organize the FAQs by issue category if there are multiple ones.

For each FAQ, start by directly answering the question, then go into detail. Use real questions that match typical search queries and user vocabulary, which will help with FAQ findability. Include links to resources that the user may find helpful, such as related articles, instructions for contacting support, and teaching materials (how to guides, tutorials, and others) when available. 

#### Geography {#geography}

##### Cities

Spell out all city names on the first mention in the copy. After that, it’s fine to abbreviate well-known city names like NYC or LA.

**First mention:** San Francisco  
**Second mention:** SF

For well-known cities like London or Tokyo, it’s fine to introduce them without a comma followed by the state, province, or country. 

For cities or towns that may be unfamiliar to your audience, include the state, province, or country.

| Do |
| :---- | 
| Biloxi, Mississippi |
| New Bedford, MA 
| Antwerp, Belgium |

##### Countries

Capitalize the names of all countries. To abbreviate a country name, spell the first mention out in full, followed by the initials moving forward.

**First mention:** United States  
**Second mention:** US  
		  
Don’t place periods between abbreviated country names.

| Do | Don’t |
| :---- | :---- |
| UK | U.K. |
| Washington, DC | Washington, D.C. |

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

| Do | Don’t |
| :---- | :---- |
| Step 2: Create an SMS campaign <br><br> Step 2.1: Compose your message <br><br> Step 2.2: Schedule the delivery | Step 2: Create an SMS campaign <br><br> Step 2a: Compose your message <br><br> Step 2b: Schedule the delivery |

#### Introductions {#introductions}

Introductions serve as a quick check for users asking:

* Am I in the right document? Is this relevant to me?  
* What will I learn if I invest the time in reading this doc?  
* Do I feel like I am following a clear integration/setup journey for SMS/email/IAM etc. (despite not spelling out which doc a user should go to next)?

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
2. A statement of what the article contains. This will often look like "This reference article....".

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

This section includes general guidelines for formatting images and GIFs in your content. For more information, including example screenshots, refer to the [Image Copy Style Guide](https://docs.google.com/document/d/e/2PACX-1vRJSkwcjmjrTfLDagZccLpOMMyh5NN5SXRZSjz12cRAHbX4OrUmhvCmYpf_p5YB-9r4_jSOQLkicQIH/pub).

| **Do** | {::nomarkdown}<ul><li>Do tightly crop to the feature or component of mention.</li><li>Do take high-quality screenshots, preferably on a retina monitor (MacBook display).</li><li>Do create a GIF of an interaction or workflow.</li><li>Keep in mind that users cannot pause or scrub through a GIF to see details.</li><li>Do run images through an optimizer to reduce file size (ImageOptim, TinyPNG, or Ezgif).</li><li>Do aim for high contrast between elements for accessibility.</li><li>Do resize images by height percentages rather than distinct pixel values.</li></ul>{:/} |
| **Don't** | {::nomarkdown}<ul><li>Don't include the header or sidebar of the dashboard, as these can be explained in a simple sentence.</li><li>Don't include the entire dashboard.</li><li>Don't include Personally Identifiable Information (unless blurred, or that of a demo user).</li><li>Don't include the browser frame (URL field, bookmarks, tabs, etc.).</li><li>Don't include dashboards of Technology Partners.</li><li>Don't add a border or drop shadow to images.</li></ul>{:/} |

#### Numbers {#numbers}

Never start a sentence with a numeral. The exception is when referring to a year (example: “2019 was one for the books). 

Spell out numerals up to nine. For units of measurement or numbers 10 or higher, use the numeral. For numbers over three digits, use a comma. Write out larger numbers. 

| Do | Don't |
| :---- | :---- |
| 1,000 | 1000 |
| 200,000 | 200000 |
| 1,000,000 | 1000000 |
|9 billion | 9000000000 |
| 5 MB | five MB |

##### Currency

Always indicate what currency you’re referring to by using the currency symbol before the amount or spell it out (example: pesos, euros, pounds, etc.).

Use the decimal for amounts where the number of cents is greater than zero. For sums greater than three digits, use a comma. Don’t include “.00” in sums of money.

| Do | Don't |
| :---- | :---- |
| US $20 | $20 |

##### Telephone Numbers

When a phone number is referenced, place hyphens between the digits. Do not place the area code within parentheses. 

When formatting phone numbers with a country code, use a plus sign (+) before the country code and place the area code within parentheses. 

Provide a number with a country code like so: +1 (504) 327-7269

| Do | Don't |
| :---- | :---- |
| 123-456-7890 | (123)-456-7890 |
| +1 (123) 456-7890 | 1 234-567-9012 |

##### Fractions

Spell out fractions and use a hyphen between the numerator and the denominator. Do not use numerals separated by a slash. 

In some cases when expressing a fraction as a decimal is necessary, add a zero before the decimal point for fractions less than one.   

When expressing rating systems using fractions, use numerals to spell out the ranking.

| Do | Don't |
| :---- | :---- |
| 0.5 | 1/2 |
| one-third | one third |
| 9 out of 10 | nine out of ten |

##### Percentages

Use numerals and a percent sign (%) without a space in between them. However, if the percent starts the sentence, then spell out the entire percentage (number and percent).

| Do | Don't |
| :---- | :---- |
| 10% | 10 %
| Twenty percent of Braze users are... | 20% of Braze users are... |

##### Ranges

Use a hyphen to indicate a range of numbers. Do not use an en dash to separate numbers in a range. 

For ranges of numbers with units, repeat the unit of measurement after the number. This does not include repeating nouns. Use the word “to” between the numbers in the range to avoid confusion.

| Do | Don't |
| :---- | :---- |
| 5 to 100 | 5–100
| -10°C to 50°C |  -10°C-50°C Don't |

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
| Don’t sacrifice clarity for brevity. Use as many words as needed to represent a placeholder. | **Do:** *CAMPAIGN_NAME* **Don’t:** *NAME* |

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

| Do | Don't |
| :---- | :---- |
| The newest product update from Braze | Braze’s newest product update |
| That’s one of the defining features of Braze. | That’s one of Braze’s defining features |

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

* Your auto-generated anchor will be very long.  
* Your heading may be frequently linked to. Adding a custom anchor reduces the likelihood of breaking links if the heading text is changed later.

To add an anchor to a heading in Braze documentation, refer to [Custom Anchors]({{site.baseurl}}/home/styling_test_page/#custom-header-anchor).

#### Link Text {#link-text}

Effective link text helps to improve the findability, discoverability, and accessibility of your content. 

##### Structuring Links {#structuring-links}

Use one of the following formats when writing links:

* Match the link text to the title or heading of the link destination.  
* Use a description of the link destination as the link text.

| Do <br><br> *Match the link text to the title or heading of the link destination.* | Do <br><br> *Use a description of the link destination as the link text.* |
| :---- | :---- |
|  Get started with the Braze [Web SDK]({{site.baseurl}}). | To find out your specific cluster or endpoint, [contact Support]({{site.baseurl}}). |
| For more information, see [Aborting Liquid Messages]({{site.baseurl}}). | When in doubt, you can always [reset your password]({{site.baseurl}}). Do Use a description of the link destination as the link text. |

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

| Do <br><br> *Make sure the link text makes sense without the surrounding text* | Don't <br><br> *Use vague or non-descriptive link text* |
| :---- | :---- |
|  For more information on importing customer data, see [User Import]({{site.baseurl}}). | For more information, [click here]({{site.baseurl}}). |
| This feature connects to the [Track users]({{site.baseurl}}) endpoint. | See [this article]({{site.baseurl}}). |
| Learn more about [what’s new in Android SDK 16.0.0]({{site.baseurl}}). | Follow the instructions [here]({{site.baseurl}}). |
| Learn more about the [Braze platform](https://www.braze.com/product). | For steps, refer to [this document]({{site.baseurl}}). [Learn more]({{site.baseurl}}). |
| Storefront API keys are unique per Hydrogen storefront, but their permission scopes are shared by all Hydrogen storefronts. Learn more about [Storefront API tokens.]({{site.baseurl}}) | [Storefront API tokens]({{site.baseurl}}) are unique per [Hydrogen storefront]({{site.baseurl}}), but their [permission scopes]({{site.baseurl}}) are shared across all Hydrogen storefronts. |

#### Links for Endpoints {#links-for-endpoints}

When referencing endpoint articles, be sure to use [meaningful link text](https://docs.google.com/document/d/e/2PACX-1vTluyDFO3ZEV7V6VvhXE4As_hSFwmnFFdU9g6_TrAYTgH1QmbRoEDDdn5GzKAB9vdBbIdyiFdoaJcNk/pub#h.79ujl0qtumog) that can make sense out of context. If you’re using the endpoint’s path as a link, be sure to provide details in the surrounding text as the path may not clearly communicate the endpoint’s function.    

| Do | Don't |
| :---- | :---- |
| Delete user profiles using the Braze [Delete user endpoint]({{site.baseurl}}/api/endpoints/user_data/post_user_delete/). | Delete user profiles using the Braze [Delete user]({{site.baseurl}}/api/endpoints/user_data/post_user_delete/) endpoint. |
| [`/users/export/id` endpoint]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/) | [`/users/export/id`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/) endpoint |

#### Links for File Download {#links-for-file-download}

If a link downloads a file, then make that clear in the link text, and mention the file type.

| Do <br><br> *Make sure the link text communicates that clicking it downloads a file* | Don't |
| :---- | :---- |
| For tips, download the [Regex Cheat Sheet PDF]({{site.baseurl}}) | Check out our [RegEx Cheat Sheet]({{site.baseurl}}). |
| For more information, download the [Success and Support Services Handbook PDF]({{site.baseurl}}) | [Success and Support Services Handbook]({{site.baseurl}}) |

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

## Image copy style guide

**Image Styling Tools:** Use [Skitch](https://evernote.com/products/skitch) (available free through Evernote) for applying image styling (blurring, emphasizing image components, cropping).

**Don’t embed important text inside images:** Avoid embedding text inside images as not all users will be able to read English text (and page translation tools will not translate images). This text should be provided in the article. Provide alt text for images for maximum accessibility for users.

| Do  | Don’t |
| :---- | :---- |
| ![Example of correctly not embedding text in an image.]({% image_buster /assets/img/contributing/style_guide/embed_text_do.png %}) | ![Example of incorrectly embedding text in an image.]({% image_buster /assets/img/contributing/style_guide/embed_text_dont.png %}) |

**Optimize placement and sizing:** Whenever possible, place images near relevant text and be mindful to use image styling markdown to resize larger images. For some content, this should be done by [anchoring text to the left or right side of the page]({{site.baseurl}}/home/styling_test_page/#image-test) depending on the image and the space available. 

| Do  | Don’t |
| :---- | :---- |
| ![Example of correctly optimizing image placement.]({% image_buster /assets/img/contributing/style_guide/optimize_placement_do.png %}) | ![Example of incorrectly optimizing image placement.]({% image_buster /assets/img/contributing/style_guide/optimize_placement_dont.png %}) |

**Cropping**: Crop relevant sections closely. Unless necessary, do not include the left navigation bar and instead include navigation directions in the article. This will limit the number of images that need to be changed when UI changes to the dashboard occur. 

Note: If you are going to capture a dashboard element, crop without including the border. Please visit the end of the style guide for expanded examples.

| Do | Don’t |
| :---- | :---- |
|    |    |

**Censorship**: Blur sensitive information like names, emails, API keys, etc. Blurring can be done through Skitch.

| Do | Don’t |
| :---- | :---- |
|  |  |

**Emphasizing Components of Images:** Do not emphasize components of images unless necessary. Use blue squares (the most colorblind-friendly option) with a thin-medium thickness to highlight different components of images, this can be done through skitch. Make sure the “highlighted sections” do not obstruct the normal UI. Absolutely no skitch arrows

| Do | Don’t |
| :---- | :---- |
|      |    |

**Cropping Explanation Cont.**  
Because Braze docs already add a border to each image, omit borders in a section screenshot. We are looking for a clean crop. The border can be left in if there are components that live outside or within the border, see the third image for example.

**Do:**



**Don’t:**  
  
**Do:**  




## Alerts (best practices)

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
| Important | Includes essential information that **should** be addressed by the reader, such as: Deprecated features  Impacts on billing Information pertaining to relevant updates Pressing feature caveats (ex: beta features) Other important tidbits of information |
| Note | Includes one-off information that the reader should know, such as: Feature caveats Formatting guidance Helpful callouts Information that is demoted from an Important alert due to the alert’s content dropping in severity (ex: a long-standing important alert shifting to a standard note) |
| Tip | Includes supplementary knowledge and recommendations for the reader to be aware of, such as: Additional troubleshooting articles Steps and shortcuts that help increase usability (ex: additional customization for in-app messages) |
| Warning | Includes essential information that **must** be addressed by the reader and can include: Irreversible consequences (ex: Campaign and Canvas deletion) Feature-breaking behavior Loss of data Other crucial warnings |

**Alert Best Practices**  
Here are general guidelines and best practices for alerts. 

As a general rule of thumb, avoid using alerts for content that is essential to the article structure (feature introductions, setup instructions, steps to use a feature, etc.). When in doubt, consult with the team during peer review.

| Guideline | Example |
| :---- | :---- |
| Explain the information in the alert in a clear, concise statement.  |  [Note alert in Step 4: Add Filters to Your Segment Section]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/#step-4-add-filters-to-your-segment) |
| For alerts that apply to different sections of the same article, consider creating a new section that captures these details to avoid repetitive content. |  [Property Details header in Push Send Events Section]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/message_engagement_events) |
| Separate the information into short paragraphs or lists within the alert. |  [Important alert in Canvas Persistent Entry Properties]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_persistent_entry_properties/#using-entry-properties) |
| Consider any additional formatting that may impact how the alert displays (code snippets, steps, surrounding images, etc.). |  [Important alert in Step 2: Add Code Snippet to Email Body]({{site.baseurl}}/partners/message_orchestration/channel_extensions/loyalty/voucherify/#step-2-add-code-snippet-to-email-body) |
| Include a line break for alerts that begin an article.  |  [Content Card Implementation Guide]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/implementation_guide/) |
| When writing about beta features, include an Important alert that calls out the beta status and related Braze contact information.  Place this beta alert after the overview text and before the first main heading.  |  [Canvas Persistent Entry Properties]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_persistent_entry_properties/)  |
| Avoid using two or more alerts in a row if possible. Instead, reorganize or include the information as part of the text instead.  | [Setting User IDs]({{site.baseurl}}/developer_guide/platform_integration_guides/fireos/analytics/setting_user_ids/) |
| If you find your alert is lengthy, consider creating a new section that includes the information as a list. For example, instead of including troubleshooting steps in an alert, consider creating a troubleshooting section or providing a link to a related article.  |  [Tip alert in Canvas and Campaign Tag Differences Section]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/) |

### Alert Examples {#alert-examples}

Refer to the examples below for how and why each alert type is used in our documentation. 

### Important Alert  {#important-alert}

|  |  |
| :---- | :---- |
| **Article:** [Push for Web]({{site.baseurl}}/user_guide/message_building_by_channel/push/web/) |  |
| **Use Case** Includes essential feature caveat that the reader should know as they set up their web push | **Alert Reasoning** Use an Important alert as opposed to a Note alert because the content’s importance is greater for a reader to know as they set up their web push.  |

|  |  |
| :---- | :---- |
| **Article:** [Email Settings]({{site.baseurl}}/user_guide/administrative/app_settings/manage_app_group/email_settings/) |  |
| **Use Case** Provides important feature caveat about the possibility of doubling billable emails  Redirects reader to contact their Customer Success Manager as needed | **Alert Reasoning** The Important alert is used here to communicate details about the BCC addresses in their email settings.  This information is best presented using an Important alert as opposed to a Warning alert because omitting this information does not impact the feature irreversibly (feature breaking, permanent data loss, etc.) |

|  |  |
| :---- | :---- |
| **Article:** [Advanced Settings]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/advanced_settings/?redirected=true) |  |
| **Use Case** Includes pressing feature caveat about the Notification Priority Redirects the reader to new information that’s available | **Alert Reasoning** The Important alert is best used here to redirect the reader to current information and to highlight that the section is applicable only to certain users. It’s also placed after the section header, which forces the user to address the important alert before reading the rest of the section. |

### Note Alert {#note-alert}

|  |  |
| :---- | :---- |
| **Article:** [Create a Content Card]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/create/) |  |
| **Use Case** Includes additional information that a reader should be aware of as they learn more about Content Cards | **Alert Reasoning** This Note alert provides background information on how Braze cycles older Content Cards for users.  This is helpful, supplemental information for the reader to be aware of and does not require the use of an Important or Tip alert. |

|  |  |
| :---- | :---- |
| **Article:** [Custom Attributes]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/) |  |
| **Use Case** Includes general information that a reader should be aware of Provides an article to learn more about related content (time attributes) | **Alert Reasoning** This information is best relayed using a Note alert as opposed to an Important alert because the content is directed to provide general information. Disregarding this information would not impact the ease of use for this feature. |

|  |  |
| :---- | :---- |
| **Article:** [Custom Events and Attribute Management]({{site.baseurl}}/user_guide/administrative/app_settings/manage_app_group/custom_event_and_attribute_management/#managing-properties) |  |
| **Use Case** Includes general information that a reader should be aware of Redirects to Braze contact for further information | **Alert Reasoning** This Note alert provides **additional** information about data storage that would be helpful for a reader to know as they manage their custom attributes.  However, the content does not require a stronger indication of importance to the reader, so a Note alert is acceptable here. |

### Tip Alert {#tip-alert}

|  |  |
| :---- | :---- |
| **Article:** [SMS Message Segments and Copy Limits]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/segments/) |  |
| **Use Case** Includes tool for the reader to understand their message length and SMS segment count Provides information that may be helpful for the reader in their understanding of copy limits | **Alert Reasoning** This is a lengthy Tip alert because it provides a space for entering the copy to see how many segments a message will dispatch.  The Tip alert is the best option here because this is a helpful generator for the reader to use in the process of setting up their SMS messages. |

|  |  |
| :---- | :---- |
| **Article:** [Daily App Uninstalls by Date Endpoint]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_uninstalls_date/) |  |
| **Use Case** Provides troubleshooting advice when using this endpoint | **Alert Reasoning** The Tip alert provides additional support for the reader. Use a Tip alert as opposed to a Note alert because the focus of the content is to assist the reader by providing the troubleshooting article. |

### Warning Alert {#warning-alert}

|  |  |
| :---- | :---- |
| **Article:** [User Profile Lifecycle]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/) |  |
| **Use Case** Indicates something that the reader should not do when creating their user profiles in Braze | **Alert Reasoning** The Warning alert is used to caution the reader against assigning an external_id before uniquely identifying them. This information is best relayed using a Warning alert as opposed to an Important alert because it includes irreversible consequences for the user profile. |

|  |  |
| :---- | :---- |
| **Article:** [Segments for Currents]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/segment/segment_for_currents/) |  |
| **Use Case** Cautions the reader when creating Currents connectors Includes the consequence of incorrectly creating these connectors | **Alert Reasoning** The Warning alert is best used here to describe the limitations of the Braze Segment Currents integration. Use a Warning alert as opposed to an Important alert because creating more than one of the same Currents connectors incorrectly may result in losing data. |

|  |  |
| :---- | :---- |
| **Article:** [Creating a Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/) |  |
| **Use Case** Lists the information that may cause the feature to not work Details how the intended audience may not receive the campaign or enter the Canvas | **Alert Reasoning** The Warning alert is used here to note how the feature may work incorrectly. This information is best relayed using a Warning alert as opposed to an Important alert because the information is critical and may result in breaking the Canvas delivery. |
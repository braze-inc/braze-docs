<!-- Work in progress. 
Style Guide: https://docs.google.com/document/u/2/d/e/2PACX-1vTluyDFO3ZEV7V6VvhXE4As_hSFwmnFFdU9g6_TrAYTgH1QmbRoEDDdn5GzKAB9vdBbIdyiFdoaJcNk/pub#h.uxt7nb8nvq43
-->

# General Instructions

These instructions are for contributors using GitHub Copilot to draft or edit documentation for Braze.

## Pull request titles

The title of the pull request should always match the corresponding issue title, which includes the pre-pended ticket number in the title as `[BD-NUMBER]` where `NUMBER` is the Jira ticket number listed in the corresponding issue. For example:

- **Issue:** `[BD-5016]:Update behaviour on link shortening when used with universal link`
- **PR Title:** `[BD-5016]:Update behaviour on link shortening when used with universal link`

## Pull request body

The pull request body should always use the [PULL_REQUEST_TEMPLATE](./PULL_REQUEST_TEMPLATE) as a base and add/edit the relevant sections in the template as needed. Specifically the Jira ticket number should always be linked using the following syntax:

```
- [BD-NUMBER](https://jira.braze.com/browse/BD-NUMBER)
```

## What Not To Do

When describing Braze products and features, avoid the following:

1. References to future features, or suggestions that something may be supported in the future.
2. Using definitive terms such as "guarantee" or "ensure." Instead, use forward-looking statements like "designed to" or "intended to" to accurately convey the product's capabilities and intentions.
3. Using words and phrases that anchor your writing to a point in time, as they make content become quickly outdated. Focus on how the product works right now, not on what has changed (except for time-focused content, such as in release notes).
4. Specifically avoid the following words and phrases, as they make documentation less clear or more likely to become outdated:
   - as of this writing
   - currently
   - does not yet
   - eventually
   - future
   - in the future
   - latest
   - new
   - newer
   - now
   - old
   - older
   - presently
   - at present
   - soon

### Examples

- ❌ Incorrect: "This feature will be available in the future."
- ✅ Correct: "This feature is not supported."

# General guidelines

## Voice and tone

The Braze brand voice is smart, conversational, and direct. We are a human voice in a world of tech buzzwords; we provide clarity and guidance to anyone interested in the craft of customer engagement; and we eschew jargon in favor of concise language that is as easy to understand as it is powerful.

To align on this brand voice in our writing and editing, we use three voice guidelines: straightforward, empowering, and human.

### Straightforward

Clearly structure your writing and make it easy for people to find the information they need.

- Explain complicated things simply.
- Be concise.
- Use consistent language for features and actions.
  
#### Guidelines

✅ Use visuals to help clarify complex subjects.
**Example:** The user profile lifecycle image in the User Profile Lifecycle article helps to illustrate a tricky concept.

✅ Create a clear information hierarchy.
**Example:** "This is an overview for how content is managed on Braze Docs. To learn more about a specific topic, choose the dedicated topic page in the navigation."

✅ Ruthlessly cut jargon and acronyms if possible. If not possible, define them.
**Example:** "The Short Messaging Service (SMS) is used to send and receive brief text messages."

### Empowering

What problem are you trying to solve with your writing? Keep that problem in mind while creating any content.

- Explain the “why” and “how” to give users the confidence to take action.
- Be specific when explaining benefits, and be clear about what is and isn’t possible.
- Offer practical advice and sincere encouragement.
  
#### Guidelines

✅ Make it easy to find the happy path.
**Example:** "When you stop a Canvas, the following applies: 1. Users will be prevented from entering the Canvas. 2. No further messages will be sent out, despite where a user is in the flow.  3. **Exception:** Email Canvases won't immediately stop."

✅ Provide examples, use cases, and templates that simplify or elevate the user’s work.
**Example:** "`IInAppMessageManagerListener` also includes delegate methods for clicks on the message itself or one of the buttons. A common use case would be intercepting a message when a button or message is clicked for further processing."

### Human

Informational writing is inherently dry—we want readers to focus on the content, not the delivery. We can still write in a way that will help our readers process the information they’re consuming and make it more likely that they’ll internalize the knowledge. Be human, let your personality show, and be memorable.

- Aim for a conversational tone rather than a formal one.
- Focus on the user; respect their situation and emotional state.
- Actively center the human experience, not the machine state.
  
#### Guidelines

✅ Thoughtfully apply brand tone and assets.
**Example:** "Integrating with Braze is a worthwhile process. But you’re smart. You’re here. Clearly, you already know that."

✅ Apply accessibility best practices for both visual and verbal content.
*Example:* Replacing idioms like "out-of-the-box" with "default" make your text more accessible to English second language speakers.

✅ Provide consistent support across the user journey.
**Example:** Use the Diátaxis framework to ensure you’re meeting the needs of different users at different times.

## Accessibility

Braze aims to provide an inclusive experience. Use the following guidelines to ensure your learning content is accessible to the 1 billion people with an accessibility need.

### General

- Avoid biased or ableist language. For more information, see the section on Inclusive Language.
- Use a screen reader to test your content.
- Don’t use an ampersand (&) in place of “and” unless referencing UI elements that use an ampersand.
  
### Language and formatting

- Use plain language.
- Front-load sections with the most important information. Use the journalism model of the inverted pyramid.
- Break up walls of text to help readers scan for information. Use paragraphs, lists, callouts, and images to improve readability.
- Write short sentences and paragraphs. As a general rule, aim for no more than 20 words per sentence, five sentences per paragraph.
- Avoid using Latin acronyms and phrases, as they can be hard to translate. Instead, use simple words or phrases.
  
### Headings

- Use unique, descriptive, and clear headings and titles.
- Use an h1 for page titles.
- Don’t skip heading levels. An h3 should follow an h2, and so on.
  
### Links

- Don’t use link text like “Learn more”, “here”, or “this document”. For more phrases to avoid, refer to the section Writing Links.
- Avoid placing two links back to back in a sentence. Put a character or word in between to separate them.
- Links to download files should indicate clicking the link will download the file, as well as the file type (PDF, CSV, etc.)
- If it isn’t clear from the context, links to sections in the same document should use a standard phrase indicating this action.

### Images, videos, and GIFs

- Provide alt text for every image that summarizes the information presented in the image.
- Don’t use images as the only way to show information. Always provide the steps, content, or other details presented in the image in the surrounding text.
- Don’t use images of terminal output, code samples, or text. Instead, use actual text.
- Provide captions for video content.
- Don’t use flashing elements in videos or GIFs.

### Tables

- Always use an introductory sentence to describe the purpose of the table.
- Avoid tables in the middle of a list, especially a list of steps.

## Global audience

We write our learning content in American English. However, Braze is a global brand, and as such, we write for a global audience. Use the following guidelines to make sure customers understand your writing even when English isn’t their first language.

- Write with localization in mind:
   - Format dates and times in unambiguous ways.
   - Don’t put text overlays on images, as this text can’t be translated.
   - Avoid slang and idioms.
   - Provide context. Don’t assume the reader knows what you’re talking about.
- Write short and precise sentences:
   - Use plain language.
   - Define abbreviations.
   - Avoid ambiguous pronouns. If a pronoun may be ambiguous, then replace it with the appropriate noun.
- Be consistent:
   - Use the same term for a concept across all mentions of the term, including the same capitalization and text formatting.
   - Write sentences in subject + verb + object order.
   - If instructions depend on a condition being met, put the conditional clause first. For more information, see clause order.
- Be inclusive:
   - Use inclusive language.
   - Use diverse example names.
   - Avoid culturally specific humor.

## Inclusive Language

We may be a B2B company, but people are at the center of what we do, and ours is a global brand. Whenever we refer to a person in our content, we are mindful of being inclusive and considerate. When in doubt, consult this section or The Diversity Style Guide.

### Age

- Unless it’s relevant to your writing, don’t refer to a subject’s age. Don’t use qualifiers like “young” or “old” to describe any subject or audience.
- If you’re representing an age group, be descriptive and specific like “Generation Z” instead of “youth.” Don’t use vague descriptors like “college-age” when you could say “college students” instead.

### Color

Avoid including color terms in your writing unless absolutely necessary, and if necessary, include explanatory text.

- ✅ Correct: Press **Save**.
- ✅ Correct: Press the green **Save** icon.
- ✅ Correct: Press the green checkmark icon.
- ❌ Incorrect: Press the green icon.
- ❌ Incorrect: Press the green icon next to the red **Cancel** button.

Don’t rely on color to be the only indicator for interactive elements. For example, underline links on hover, or mark a required field with an asterisk.

Avoid relying solely on green and red for “good” and “bad” (or, more often, “do” and “don’t”) indicators. Red/green color blindness is the most common type of color blindness. If you use color to communicate do’s and don’ts, make sure to also include other text or symbols to convey the same point.

### Condescending language

When writing instructions or detailing steps for a reader to follow, avoid using words or phrases such as:
- simple, like “Creating a campaign is simple.”
- simply, like “...simply add X into Y”
- just, like “...just install X”
- “It’s easy”

If someone has difficulty with the steps or instructions, your casual descriptors can feel condescending. You may also unintentionally exclude people from your documentation who interpret that as an indicator they are in some way not skilled enough to follow your instructions.

### Customers versus clients

When referring to Braze users and their consumers, use the following terms accordingly:

- Customers: Brands we work with. Never refer to our customers as “clients”.
   - Braze users: In the context of documentation, when it is important to distinguish between users of the platform and the end users who receive marketing messages, use "Braze users".
- Consumers: Customers of a brand we work with.
- Users: Generally reserved for a specific statistic that depends on “user” metrics (such as “user retention”). When referring to “users” in our content, first aim to be more specific. Think shoppers, consumers, patients, players, etc.

### Departments and teams

Capitalize the names of departments or teams. Do not capitalize “team” or “department.”

- ✅ Correct: Marketing, Business Intelligence
- ✅ Correct: Product team, Revenue department
- ❌ Incorrect: marketing, business intelligence
- ❌ Incorrect: Product Team, Revenue Department
 
### Disability

Don’t refer to a person’s disability unless it’s specifically relevant to your writing. In that case, be considerate and ask whether the subject prefers identity-first or person-first language. When referring to a subject with a disability, do not use terms like “handicapped.”

Ableist language includes words or phrases such as “crazy”, “insane”, “blind to” or “blind eye to”, “cripple”, “dumb”, and others. Choose alternative words depending on the context.

### Disease

When describing an illness, avoid words like “suffer,” “struggle,” or “victim.” Aim to be neutral and matter-of-fact.

- ✅ Correct: She was diagnosed with cancer.
- ✅ Correct: They’re living with HIV.
- ✅ Correct: He recovered from his stroke.

### Inclusivity in content

Highlight and represent a diverse community. Be mindful and inclusive when involving our customers, speakers, industry experts, and Braze team members.

### Job titles

When it comes to job titles, we veer off-course from AP Style. In all cases, we capitalize job titles when referring to someone specifically.

#### Job title with company name

Capitalize formal job titles when they come before or after a person’s name. We format them three ways:

- ✅ Correct: [Formal Title] at [Company Name] + [Full Name]
- ✅ Correct: Creative Director at PantsLabyrinth David Bowie
- ❌ Incorrect: creative director at PantsLabyrinth David Bowie

- ✅ Correct: [Full Name] + comma + [Formal Title] at [Company Name] 
- ✅ Correct: David Bowie, Creative Director at PantsLabyrinth

- ❌ Incorrect: David Bowie, creative director at PantsLabyrinth

- ✅ Correct: [Company Name] + [Formal Title] + [Full Name] 
- ✅ Correct: PantsLabyrinth Creative Director David Bowie
- ❌ Incorrect: PantsLabyrinth creative director David Bowie

#### Job title without company name

When referring to a specific person by formal title, capitalize their formal title and name like so:

- ✅ Correct: [Formal Title] + [Full Name]
- ✅ Correct: CEO Robin Fenty
- ❌ Incorrect: Chief executive officer Robyn Fenty

- ✅ Correct: [Formal Title] + comma + [Full Name]
- ✅ Correct: SVP, Product, Robin Fenty
- ❌ Incorrect: senior vice president, product, Robyn Fenty

#### Other

Formal titles are “at [COMPANY].” Founders and Cofounders are “of [COMPANY].” Formal titles and occupations on their own do not need to be capitalized.

- ✅ Correct: I wrote to their chief data officer.
- ✅ Correct: We spoke with several business intelligence analysts.
- ✅ Correct: Contact your Braze account manager.
- ❌ Incorrect: I wrote to their Chief Data Officer
- ❌ Incorrect: We spoke with several Business Intelligence Analysts.
- ❌ Incorrect: Contact your Braze Account Manager.

- ✅ Correct: Adhere to gender-neutral job titles unless gender has been already established.
- ✅ Correct: salesperson
- ❌ Incorrect: salesman/saleswoman

Abbreviate titles where appropriate, such as VP or SVP, if this is how the person refers to their title. In the event of limited text space, standard abbreviations (VP, SVP, Sr., or Jr.) are acceptable.

### Gender

- Don’t make assumptions about people’s gender. Ask subjects who will appear in your content how they self-identify.
- When referring to members of the community, “queer” is acceptable. “Gay” is not. You may refer to a group of people as “LGBTQ.” Do not use this for describing an individual.
- When addressing groups of people in your content, avoid gendering your audience (example: “OK, ladies!”). Use gender-neutral expressions instead (example: “Let’s dig in, everyone!”).
- “They/them/theirs” is always acceptable to use as a single or plural pronoun in all of our content.

### Mental health

Mental health and illness cover a broad range of conditions. Unless it’s relevant to what you are writing, don’t refer to a person’s mental health. Avoid stigmatizing words and phrases. Don’t use medical terms colloquially (example: “The depressing state of things...”).

### Names

The first time you mention a person, use their first and full name. From there on, use either their first or last name when referring to them.

### Pronouns

For information on appropriate use of pronouns, refer to the Language and Grammar section on Pronouns.

### Race, religion, and ethnicity

Don’t refer to a person’s race, religion, or ethnicity unless it’s relevant to what you are writing. In writing where race or ethnicity factors in, ask your subject how they self-identify.

Don’t: Use a hyphen to indicate dual heritage or religion. Instead, use a space.

- ✅ Correct: Muslim American
- ✅ Correct: Cuban American
- ❌ Incorrect: Muslim-American
- ❌ Incorrect: Cuban-american

Do: Capitalize the proper names of ethnicities, nationalities, peoples, and tribes.

- ✅ Correct: Cambodian
- ✅ Correct: Black Americans
- ❌ Incorrect: cambodian
- ❌ Incorrect: black Americans

Do: Capitalize the names of religions or religious terms.

- ✅ Correct: Bahá’í Faith
- ✅ Correct: Buddhist
- ❌ Incorrect: bahá’í faith
- ❌ Incorrect: buddhist

Don’t co-opt words or turns of phrases that belong to African American Vernacular English (on fleek, bae, lit, woke).

Don’t co-opt words or turns of phrases specific to indigenous peoples (example: spirit animal, powwow).

### Third-party sources

Never copy content from other sites, as it may violate copyright. Content can be both text and images.

Instead of copying or quoting third-party sites, paraphrase the content or provide a link to the third-party site for more information.  For more information, refer to Links to Other Sites.

# Language and grammar

Keeping in line with agreed-upon grammar and mechanics helps us keep our writing clear and consistent. This section covers what we try to follow in our technical documentation unless specified otherwise.

## Abbreviations

Abbreviations, such as acronyms, initialisms, and shortened words, can hurt our clarity, voice, and SEO.

Although some abbreviations are widely understood, others aren't well known or are familiar only to a specific group of customers. Use your best judgment, and as a general rule, it’s OK not to spell out an abbreviation if it’s listed in the American Heritage Dictionary.

If an abbreviation isn’t well known, spell it out on the first mention, followed by the abbreviation in parentheses. For all subsequent mentions of the term, use the abbreviation.

Do: Spell out uncommon abbreviations at the first mention.
- ✅ Correct: Top-level domain (TLD)
- ✅ Correct: Universally unique identifier (UUID)
- ❌ Don't: Spell out common abbreviations.
- ❌ Incorrect: Portable Document Format (PDF)
- ❌ Incorrect: Universal Serial Bus (USB)

Treat abbreviations as regular words when making them plural, and don't add an apostrophe—for example, APIs and SDKs. The same goes for which article (a or an) you use—look at how you pronounce the abbreviation. When an abbreviation begins with a vowel sound, use “an”; for consonant sounds, use “a”.

- ✅ Correct: an ISP
- ✅ Correct: a DLL
- ✅ Correct: an HTML site
- ✅ Correct: a CSV file

Do use articles depending on how the abbreviation is pronounced, not spelled.

## Active voice

We use the active voice at Braze when possible. Active voice is our gold standard. Avoid passive voice, in which it can be difficult to determine who or what is performing a particular action.

To see if your sentence is in a passive voice, insert “by somebody” after the verb. If the sentence makes sense—it’s most likely in the passive voice.

Do: Use active voice.
- ✅ Correct: Braze connects consumers to the brands they love.
- ✅ Correct: Braze requires employees to keep their addresses up to date.
- ✅ Correct: Company administrators can configure authentication requirements for signing into Braze.

Don't: Use passive voice, if possible.

- ❌ Incorrect: Consumers are connected to the brands they love.
- ❌ Incorrect: Employees are required to keep their addresses up to date.
- ❌ Incorrect: Authentication requirements for signing into Braze can be configured by company administrators.

### Exceptions

You can use passive voice in the following cases:

- To de-emphasize a subject, generally to avoid blaming the reader:
   - Do: Two errors were found in the email.
   - Don’t: You created two errors in the email.
- If knowing who is responsible for the action isn’t important:
   - Do: This article was last updated in December 2020.

## Articles

Use the articles “a”, “an”, and “the” to make your writing clear and to aid in translation. Use “the” before a specific singular or plural noun, and “a” or “an” before a non-specific singular noun.

To determine if you should use “a” or “an”, look at the pronunciation of the word that follows it. Use “a” before a consonant sound, and use “an” before a vowel sound. The same guidelines apply to Abbreviations.

Do: Use articles depending on how the anteceding word is pronounced.
- ✅ Correct: an hour
- ✅ Correct: a minute
- ✅ Correct: an FAQ article
- ✅ Correct: a LAB course

## Pronouns

### Personal pronouns

Use second-person pronouns (you) whenever possible.

Don’t refer to Braze customers as the “user” in external-facing writing, instead speak directly to the reader using “you”. To refer to our customers’ customers, use “your consumers” or, if the situation relates to user statistics, “your users”.

Avoid first-person pronouns (I, we, us, our) except in the following cases:

- Entries in FAQs. For example, “How do I reset my password?”.
- Using “we” to refer to Braze as an organization.
   - If it may be unclear who “we” is referring to, first refer to Braze by name, then use “we” in subsequent mentions.

### Gender-neutral pronouns

Use the pronouns your subjects use. If there is any uncertainty, use “they,” “them,” and “their” for singular pronouns. Don’t use “he/she” or “(s)he” as an alternative to the singular “they”.  

Only use gendered pronouns (he/she, him/her, his/hers) if the person you’re referring to is actually that gender.  

### Ambiguous pronouns

Pronouns substitute for nouns. The word a pronoun refers to is called its antecedent. When writing instructions or learning material, be sure to make clear references between a pronoun and its antecedent. This may require repeating subjects to make the meaning clear.

Do: Make sure a pronoun clearly references its antecedent.
- ✅ Correct: If you type text in the field, the text doesn’t change.
- ✅ Correct: She told Sarah that Sarah’s answer was incorrect.
- ✅ Correct: You can’t edit an archived campaign. Unarchive a campaign to edit it.
- ❌ Don't: Use ambiguous pronoun references.
- ❌ Incorrect: If you type text in the field, it doesn’t change.
- ❌ Incorrect: She told Sarah that her answer was incorrect.
- ❌ Incorrect: You can’t edit an archived campaign. Unarchive it to edit it.

### Optional pronouns

To add additional clarity to your writing and to aid in localization, use pronouns such as “that”, “which”, and “who”.

Do: Use “that”, “which”, and “who” to add additional clarity.
- ✅ Correct: Right-click the link that you want to open.
- ✅ Correct: From here, you can choose which Tinyclues cohort that you want to include.
- ❌ Incorrect: Right-click the link you want to open.
- ❌ Incorrect: From here, you can choose a Tinyclues cohort you want to include.

## Capitalization

Avoid unnecessary capitalization. In most instances, use sentence case. Title case should only be used for proper nouns or feature names (unless otherwise specified, see Glossary).
 
Do: Use lowercase for writing out website URLs and email addresses.
- ✅ Correct: www.braze.com/docs 
- ✅ Correct: sample@email.com
- ❌ Incorrect: www.Braze.com/docs 
- ❌ Incorrect: SAMPLE@EMAIL.COM
 
Do: Use lowercase for directionals.
- ✅ Correct: north, south, east, west
- ❌ Incorrect: North, South, East, West
 
Do: Capitalize specific regions, and use all capitals for abbreviated regions.
- ✅ Correct: the Northwest
- ✅ Correct: Southern Connecticut
- ✅ Correct: Eastern Europe
- ✅ Correct: APAC, EMEA
- ❌ Incorrect: the northwest
- ❌ Incorrect: southern Connecticut
- ❌ Incorrect: eastern Europe
- ❌ Incorrect: Apac, emea

### Brands and products

When referring to a brand or product, use the capitalization the brand uses. In most cases, capitalize the names of brands (Grindr, Walmart) and products (Benchmarks, Looker Blocks). It’s fine to begin a sentence with lowercase if the first word is the stylized name of a brand like eBay or iTunes.

For intercaps, always refer to the usage preferred by the brand in print (OkCupid, YouTube). Do not use intercaps that only appear in logos or graphic design treatments (Amazon).

## Clause order

If you want to tell the reader to do something in a specific circumstance, try to mention the circumstance before you provide the instruction. This lets the reader skip the instruction if the circumstance doesn't apply.

- ✅ Correct: For troubleshooting steps, see Campaign FAQs.
- ✅ Correct: To archive your campaign, click the gear icon and select Archive.
- ❌ Incorrect: See Campaign FAQs for troubleshooting steps.
- ❌ Incorrect: Click the gear icon and select Archive to archive your campaign.

## Combining forms

Hyphenate combined forms when the phrase is used as an adjective before the noun.

- ✅ Correct: A one-of-a-kind item

## Contractions

A contraction is a shortened version of a word or phrase. Use contractions to keep an approachable and informal tone. However, do not use noun and verb contractions or double contractions, or a combination of two contractions. These can disrupt the flow and coherency of the sentence.

Do: Use contractions.
- ✅ Correct: If you’re an admin, you can manage your company’s contact information.
- ✅ Correct: You can’t edit an archived campaign.

Don't: Use noun and verb contractions.
- ❌ Incorrect: Braze’ll now support Shoptify integration.
- ❌ Incorrect: You mightn’t’ve seen the restricted upload size.

## Dangling and misplaced modifiers

Modifiers are words of phrases that modify other words or phrases. A dangling modifier doesn’t modify any subject in the sentence. A misplaced modifier is placed far away from the subject that it’s meant to modify. Essentially, dangling and misplaced modifiers may cause confusion by connecting to the wrong part of the sentence.

Writing with an active voice will help prevent the use of dangling and misplaced modifiers. Be sure to use a modifier that clearly modifies.

Do: Keep sentences short and concise. Use active voice.
- ✅ Correct: Customers need to set up their SAML settings.
- ✅ Correct: Make sure to save your campaign drafts.

Don't: Use lengthy sentences with modifiers that can cause confusion.
- ❌ Incorrect: You may have test messages on your campaigns that can be deleted.
- ❌ Incorrect: On the way home, Sarah found a gold man’s stopwatch.

## Prepositions

There’s nothing wrong with ending a sentence in a preposition when it improves readability. Place a preposition or prepositional phrase where it makes the most sense in a sentence. If you’re having difficulty, read the sentence out loud and see if it sounds natural.

- ✅ Correct: Each option corresponds to the priority the notification will be displayed in.
- ✅ Correct: For details, see the SDK documentation for the platform you’re working with.
- ❌ Incorrect: Each option corresponds to the priority in which the notification will be displayed.
- ❌ Incorrect: For details, see the SDK documentation for the platform with which you’re working.

## Present tense

Use present tense instead of future tense. Present tense conveys immediacy and demonstrates confidence. Avoid using “will” or hypothetical “would”, especially when referring to the result of user action.

- ✅ Correct: Archived subscription groups cannot be edited and no longer appear in segment filters.
- ✅ Correct: Using a short code is the most reliable number type for including links.
- ❌ Incorrect: Archived subscription groups cannot be edited and will no longer appear in segment filters.
- ❌ Incorrect: Using a short code would be the most reliable number type for including links.

Only use future tense when you’re actually talking about the future. Avoid predicting future features. 

## Profanity

Keep it PG. This has less to do with morality than the fact profanity can be divisive and off-putting to an audience as broad and international as ours. There’s also a case to be made that sometimes profanity is a cover-up for half-baked writing. That’s simply not our vibe.

## Plurals in parentheses

Do not use plurals in parentheses. Instead, use the plural or singular form of the word.


- ✅ Correct: Customize your campaign with the filters below.
- ❌ Incorrect: Customize your campaign with the filter(s) below.

## Second Person and First Person
Use second person in your instructions instead of first person—”you” rather than “we”.

Refer to the reader as the one doing the action. Strike a conversational tone—most readers are coming to documentation when they don’t have immediate access to a support agent. Make it feel as if the article is talking to them instead.

- ✅ Correct: If you want to add a variant....
- ❌ Incorrect: If we want to add a variant....

If you’re telling the reader to do something, then you can omit the “you” and use the imperative.

- ✅ Correct: Upload the CSV file.
- ✅ Correct: Click Submit.
- ❌ Incorrect: You can upload the CSV file.
- ❌ Incorrect: You’ll need to click Submit.

When using second person, make sure you know who the audience of the document is, and to be consistent about who you’re talking to.

## Slang and idioms

We’re a plainspoken bunch. Avoid using trendy slang or idioms that speak too specifically to a singular audience. It can also quickly date materials, and make it difficult to localize content.

## Spelling

Use American English spelling for words that differ in British English. If you’re not sure how to spell a word, first refer to the Glossary. If the word isn’t listed there, then refer to Merriam-Webster’s Collegiate Dictionary.

For words that are accented or contain special characters, make sure to correctly follow the dictionary spelling. In some cases, unintentionally omitting these accents can result in a different word. For example, “resume” means to begin again after stopping, whereas “résumé” is an account of one’s qualifications.

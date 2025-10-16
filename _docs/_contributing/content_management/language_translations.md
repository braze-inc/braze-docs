---
nav_title: Language translations
article_title: Language translations for Braze Docs
description: "Learn how to create a Jekyll collection so you can add a new primary section on Braze Docs."
page_order: 6.1
---

# Language translations

> Learn about the systems used for translating Braze Docs into various languages.

{% alert important %}
It's unlikely that you'll need to manage these systems, but this information can be useful if you plan on creating new custom Liquid components for Braze Docs, so you can avoid breaking how other languages are translated.
{% endalert %}

## Translation lifecycle

We use Phrase, a translation management system (TMS), alongside GitHub to translate Braze Docs into a variety of languages. For each language, Phrase translates the English files stored in `_docs`, and then stores the translated files within the corresponding subdirectory in `_lang`.

At regular intervals, we manually trigger Phrase so new content on Braze Docs can be translated into each language. Updates are compiled into a single pull request, then reviewed by our team and merged into the `develop` branch when ready.

## About pattern-matching rules

To ensure that sample code, feature names, table names, and other fixed terms are not altered during translation, we use regular expressions (regex) to skip these words. This preserves accuracy and consistency across all languages.

Here's a few examples of the kind of patterns skip for translation:

| Pattern | Description |  
|---------|-------------|  
| Fenced code blocks | Any content contained within a Markdown code block using \`\`\`...\`\`\` or \~\~\~...\~\~\~. |  
| HTML tags | Any content contained within HTML tags, such as `<div>` or `<span>`. |  
| Hex colors | Hexadecimal color values, such as `#FFFFFF` or `#000000`. |  
| Dotted identifiers | Namespaced identifiers such as `Braze.iOS.BrazeLocation`. |  
| Liquid tags | Template tags in Liquid, such as {% raw %}`{% include %}`{% endraw %} or {% raw %}`{%- if -%}`{% endraw %}. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{% alert tip %}
For the full list of patterns, see [`translation_regex.json`](https://github.com/braze-inc/braze-docs/blob/develop/scripts/tests/utils/translation_regex.json) in GitHub.
{% endalert %}

## Updating Phrase regular expressions

Phrase TMS supports only Java regular expressions, and you must enter the list of regular expressions as a single string, similar to the following:

{% raw %}
```plaintext
(?:^|\n)[ \t]*([`~]{3,})[^\n]*\n[\s\S]*?\n(?:^|\n)[ \t]*\1[ \t]*(?=\n|$)|(?<!\\)(`+)[^\r\n]*?\1|\{:[^}]+\}|<[^>]+>|#(?:[A-Fa-f0-9]{6})|\b[A-Za-z]++(?:\.[A-Za-z0-9]++)++\b|\]\([^)]*\)|\{#[^}]*\}|\{%-?\s*[\w-]+(?:%(?!})|[^%])*?-?%}|\{\{-?\s*[^}]*?-?}}|(?<!\S)\S*_\S*(?!\S)
```
{% endraw %}

Before modifying the list of regular expressions, keep the following in mind:

- **Rule order matters.** Earlier rules take priority. For example, fenced code blocks are matched before inline code.  
- **Whole matches are protected.** Write each pattern so it covers the entire element you want skipped.  
- **Keep patterns simple.** Phrase rejects overly complex regex (such as nested quantifiers).  
- **Line endings.** Use `\n` for newlines. Add `\r?` only if Windows line breaks must be supported.  
- **Tag safely.** Over-tagging is acceptable; under-tagging can lead to mistranslations.  

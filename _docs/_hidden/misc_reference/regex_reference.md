---
nav_title: Regex reference sheet
permalink: /regex_cheat_sheet/
hidden: true
---

# Regex reference sheet

This page serves as a quick reference guide for regular expression, including common tokens, meta sequences, general tokens, group constants, and more.

{% tabs %}
{% tab Common tokens %}

| Common tokens |
| ------------- |
| A single character of: a, b, or c | `[abc]` |
| A character except: a, b, or c | `[^abc]` |
| A character in the range: a-z | `[a-z]` |
| A character not in range: a-z | `[^a-z]` |
| A character in the range: a-z or A-Z | `[a-zA-Z]` |
| Any single character | `.` |
| Any whitespace character | `\s` |
| Any non-whitespace character | `\S` |
| Any digit | `\d` |
| Any non-digit | `\D` |
| Any word character | `\w` |
| Any non-word character | `\W` |
| Capture enclosed | `(...)` |
| Match either a or b | `(a|b)` |
| Zero or one of a | `a?` |
| Zero or more of a | `a*` |
| One or more of a | `a+` |
| Exactly 3 of a | `a{3}` |
| Between 3 and 6 of a | `a{3,6}` |
| Start of string | `^` |
| End of string | `$` |
| A word boundary | `\n` |
| None-word boundary | `\B` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }
{% endtab %}
{% tab Meta sequence %}

| Meta sequence |
| ------------- |
| Any Unicode sequences, line breaks included | `\X` |
| Match one data unit | `\C` |
| Unicode newlines | `\R` |
| Vertical whitespace character | `\v` |
| Negation of \v | `\V` |
| Horizontal whitespace character | `\h` |
| Negation of \h | `\H` |
| Reset match | `\K` |
| Match nth sub-pattern | `\n` |
| Unicode property X | `\pX` |
| Negation of \pX | `\PX` |
| Unicode property or script category | `\p{...}` |
| Negation of \p | `\P{...}` |
| Quote; treat as liberals | `\Q...|E` |
| Match sub-pattern 'name' | `\k<name>` | 
| Match sub-pattern 'name' | `\k'name'` | 
| Match sub-pattern 'name' | `\k{name}` |
| Match nth sub-pattern | `\gn` | 
| Match nth sub-pattern | `\g{n}` |
| Recurse nth capture group | `\g<n>` |
| Recurse nth capture group | `\g'n'` |
| Match nth relative previous sub-pattern | `\g{-n}` |
| Recurse nth relative upcoming sub-pattern | `\g<+n>` |
| Match nth relative upcoming submitter | `\g'+n'` |
| Recursive names capture group | `'letter'` |
| Match previously-named capture group 'letter' | `\g{letter}` |
| Recurses names capture group 'letter' | `\g<letter>` |
| Hex character YY | `\xYY` |
| Hex character YYYY | `\x{YYYY}` |
| Octal character ddd | `\ddd` |
| Control character Y | `\cY` |
| Backspace character | `[\b]` |
| Makes any character literal | `\` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }
{% endtab %}
{% tab General tokens %}

| General tokens |
| -------------- |
| Newline | `\n` |
| Carriage return | `\r` |
| Tab | `\t` |
| Null character | `\0` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab Character class modifiers %}

| Character class modifiers |
| ------------------------- |
| A single character of: a, b, or c | `[abc]` |
| A character except\: a, b, or c | `[^abc]` |
| A character in the range: a-z | `[a-z]` |
| A character not in range: a-z | `[^a-z]` |
| A character in the range: a-z or A-Z | `[a-zA-Z]` |
| Letters and digits | `[:alnum:]` |
| Letters | `[:alpha:]` |
| ASCII codes 0-127 | `[:ascii:]` |
| Space or tab only | `[:blank:]` |
| Control characters | `[:cntrl:]` |
| Digits | `[:digit:]` |
| Visible characters (not space) | `[:word:]` |
| Lowercase letters | `[:xdigit:]` |
| Uppercase letters | `[:<:]` |
| Word characters | `[:>:]` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }
{% endtab %}
{% tab Group constants %}

| Group constants |
| --------------- |
| Capture everything enclosed | `(...)` |
| Match either a or b | `(a|b)` |
| Match everything enclosed | `(?:...)` |
| Atomic grouping (non-capturing) | `(?>...)` |
| Duplicate sub-pattern group number | `(?|...)` |
| Comment | `(?#...)` |
| For case insensitivity | `(?i)` |
| Named capturing group | `(?'name'...)` |
| Named capturing group | `(?<name>...)` |
| Named capturing group | `(?P<name>...)` |
| Inline modifiers | `(?imsxXU)` |
| Conditional statements | `(?(1)yes|no)` |
| Recursive conditional statements | `(?(R#)yes|no)` |
| Conditional statement | `(?(R&name)yes|no)` |
| Lookahead conditional | `(?(?=...)yes|no)` |
| Lookbehind conditional | `(?(?<=...)yes|no)` |
| Recurse entire pattern | `(?R)` |
| Recurse first sub-pattern | `(?1)` |
| Recurse first relative subpattern | `(?+1)` |
| Recurse subpattern 'name' | `(?&name)` |
| Match subpattern 'name' | `(?P=name)` |
| Recurse subpattern 'name' | `(?P>name)` |
| Pre-define patterns before use | `(?(DEFINE)...)` |
| Positive lookahead | `(?=...)` |
| Negative lookahead | `(?!...)` |
| Positive lookbehind | `(?<=...)` |
| Negative lookbehind | `(?<!...)` |
| Control verb | `(*ACCEPT)` |
| Control verb | `(*FAIL)` |
| Control verb | `(*MARK:NAME)` |
| Control verb | `(*COMMIT)` |
| Control verb | `(*PRUNE)` |
| Control verb | `(*SKIP)` |
| Control verb | `(*THEN)` |
| Pattern modifier | `(*UTF)` |
| Pattern modifier | `(*UTF8)` |
| Pattern modifier | `(*UTF16)` |
| Pattern modifier | `(*UTF32)` |
| Pattern modifier | `(*UCP)` |
| Line break modifier | `(*CR)` |
| Line break modifier | `(*LF)` |
| Line break modifier | `(*CRLF)` |
| Line break modifier | `(*ANYCRLF)` |
| Line break modifier | `(*ANY)` |
| Line break modifier | `\R` |
| Line break modifier | `(*BSR_ANYCRLF)` |
| Line break modifier | `(*BSR_UNICODE)` |
| Regex engine modifier | `(*LIMIT_MATCH=x)` |
| Regex engine modifier | `(*LIMIT_RECURSION=d)` |
| Regex engine modifier | `(*NO_AUTO_POSSESS)` |
| Regex engine modifier | `(*NO_START_OPT)` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }
{% endtab %}
{% tab Quantifiers %}

| Quantifiers |
| ----------- |
| Zero or one of a | `a?` |
| Zero or more of a | `a*` |
| One or more of a | `a+` |
| Exactly 3 of a | `a{3}` |
| 3 or more of a | `a{3,}` |
| Between 3 and 6 of a | `a{3,6}` |
| Greedy quantifier | `a*` |
| Lazy quantifier | `a*?` |
| Possessive quanitifer | `a*+` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }
{% endtab %}
{% tab Anchors %}

| Anchors |
| ------- |
| Start of match | `\G` |
| Start of string | `^` |
| End of string | `$` |
| Start of string | `\A` |
| End of string | `\Z` |
| Absolute end of string | `\z` |
| A word boundary | `\b` |
| A non-word boundary | `\B` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }
{% endtab %}

{% tab Flags and modifiers %}

| Flags and modifiers |
| ------------------- | 
| Global | `g` |
| Multiline | `m` |
| Case-sensitive | `l` |
| Ignore whitespace | `x` |
| Single line | `s` |
| Unicode | `u` |
| Extended | `X` |
| Ungreedy | `U` |
| Anchor | `A` |
| Duplicate group names | `J` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab Substitution %}

| Substitution |
| ------------ |
| Complete match contents | `\0` |
| Contents in capture group 1 | `\1 or $1` |
| Contents in capture group `foo` | `${foo}` |
| Hexidecimal replacement values | `\x20, \x{06fa}` |
| Tab | `\t` |
| Carriage return | `\r` |
| Newline | `\n` |
| Form-feed | `\f` |
| Uppercase transformation | `\U` |
| Lowercase transformation | `\L` |
| Terminate any transformation | `\E` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }
{% endtab %}
{% endtabs %}


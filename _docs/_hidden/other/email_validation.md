---
nav_title: Email Validation 
title: Email Validation
permalink: "/email_validation/"
hide_toc: true
hidden: true
description: ""
---

# Email Technical Guidelines & Notes

## Email Validation

{% alert important %}
This validation is done for both user email addresses and the from-address of an email message.
{% endalert %}

Braze validates the email address using the following Ruby Gem: https://github.com/afair/email_address.  
The Gem is set to relaxed mode and configured to accept UTF-8 character.

Email Validation looks at both the Local and Host Domain part of an address.
Local part is anything before the @ symbol
Host Domain part is anything after the @ symbol


### Local part Validation Rules
#### Microsoft Domains
If the host domain is has “msn, hotmail, outlook, live” then the following is allowed for the local part

Regex: \A[a-z][\-\w]*(?:\.[\-\w]+)*\z

**Regex explanation:**
1. Local part must start with a character (a-z)
2. Local part can contain any alphanumeric character (a-z or 0-9) or an underscore (**_**)
3. can also contain the following characters (**.**) or (**-**)
4. can not end with a period (**.**)
5. cannot contain two or more consecutive periods (**.**)


##### All other domains
For all other domains, Braze allows the following for the local part

Regex: /\A [\p\{L}\p\{N}_]+ (?: [\.\-\+\'_]+ [\p\{L}\p\{N}_]+ )* \z/x

**Regex explanation:**
1. Local part can contain any letter, number or underscore, including Unicode letters and numbers
2. can contain but may not start or end with the following characters: (**.**) (**-**) (**+**) or (**'**)

{% alert important %}
If the domain part is a Gmail address, the local part needs to be at least 5 characters long
This is an addition to the regex validation specified above under "All other domains"
{% endalert %}


### Host part validation Rules
ipv4 or ipv6 addresses are not allowed in the host domain part of the email address

Regex: /^[\w\d](?:[\w\d-]{0,61}[\w\d])?(?:\.[\w\d](?:[\w\d-]{0,61}[\w\d])?)+$/i

**Regex explanation:**
1. host domain must start with a alphanumeric character (a-z or 0-9)
2. host domain can only contain one period “.”
3. Host domain cannot contain two or more consecutive periods
4. host domain must end with a top level domain
5. the top level domain is determined by anything after the ‘.’ and can only contain alphanumeric characters (a-z or 0-9)
6. can contain the following characters: (**.**) or (**?**)

{% alert important %}
Unicode is accepted for both the local and host domain part of the email address.
{% endalert %}

This validation is done for user email addresses, the from-address as well as the reply-to address  of an email message.

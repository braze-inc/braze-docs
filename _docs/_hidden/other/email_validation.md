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
2. Local part can contain any character or number (a-z or 0-9)
3. can contain the following characters (**.**) or (**-**)
4. can not end with a period (**.**)
5. cannot contain two or more consecutive periods (**.**)


##### All other domains
For all other domains, Braze allows the following for the local part

Regex: /\A [\p\{L}\p\{N}_]+ (?: [\.\-\+\'_]+ [\p\{L}\p\{N}_]+ )* \z/x

**Regex explanation:**
1. Local part can contain any letter, number or underscore, including Unicode letters and numbers
2. can contain but may not start or end with the following characters: (**.**) (**-**) (**+**) or (**'**)


### Host part validation Rules
ipv4 or ipv6 addresses are not allowed in the host domain part of the email address

Regex: / [\p{L}\p{N}]+ (?: (?: \-{1,2} &#94; \.) [\p{L}\p{N}]+ )*/x

**Regex explanation:**
1. host domain must start with a alphanumeric character (a-z or 0-9)
2. host domain can only contain one period “.”
3. host domain must end with a top level domain
4. the top level domain is determined by anything after the ‘.’ and can only contain alphanumeric characters (a-z or 0-9)
5. can contain the following characters: (**.**) or (**?**)

{% alert important %}
Unicode is accepted for both the local and host domain part of the email address.
{% endalert %}
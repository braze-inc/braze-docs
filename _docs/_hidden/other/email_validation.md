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
This validation is used for dashboard email addresses, end-user email addresses (your customers), from and reply-to addresses done of an email message .
{% endalert %}

Braze validates the email address using the following Ruby Gem: https://github.com/afair/email_address.  
The Gem is set to relaxed mode and configured to accept UTF-8 character.

Email Validation looks at both the Local and Host Domain part of an address.
Local part is anything before the @ symbol
Host Domain part is anything after the @ symbol


### Local part Validation Rules
#### Microsoft Domains
If the host domain is has “msn, hotmail, outlook, live” then the following is allowed for the local part

Regex: /\A[a-z][\-\w]*(?:\.[\-\w]+)*\z/

**Regex explanation:**
- Local part must start with a character (a-z)
- Local part can contain any alphanumeric character (a-z or 0-9) or an underscore (**_**)
- Can also contain the following characters (**.**) or (**-**)
- Can not start or end with a period (**.**) or dash (**-**)
- Cannot contain two or more consecutive periods (**.**)


##### All other domains
For all other domains, Braze allows the following for the local part

Regex: /\A[\p\{L}\p\{N}_]+(?:[\.\-\+\']+[\p\{L}\p\{N}_]+)*\z/

**Regex explanation:**
- Local part can contain any letter, number or underscore, including Unicode letters and numbers
- Can contain but may not start or end with the following characters: (**.**) (**-**) (**+**) or (**'**)

{% alert important %}
If the domain part is a Gmail address, the local part needs to be at least 5 characters long
This is an addition to the regex validation specified above under "All other domains"
{% endalert %}


### Host part validation Rules
- ipv4 or ipv6 addresses are not allowed in the host domain part of the email address
- The TLD (Top Level Domain - i.e. the final part of the domain, e.g.  com, gov) may not be fully numeric
The domain must match the regex: 

Regex: /^[a-z\d](?:[a-z\d-]{0,61}[a-z\d])?(?:\.[a-z\d](?:[a-z\d-]{0,61}[a-z\d])?)+$/i

**Regex explanation:**

- Host consists of two or more period-separated parts. 
-- Host domain must contain at least one period “.”
-- Host domain cannot contain two or more consecutive periods
- Each part must start with an alphanumeric character (a-z or 0-9)
- Each part must end with an alphanumeric character (a-z or 0-9)
- Intermediate characters may include a dash (**-**)
- Each part contains from 1 to 63 characters

**Additional validation required** 
- The final part must be a valid top level domain (TLD)top level domain which is determined by anything after the final ‘.’ and must contain at least one alphabetic character
-- The TLD should be in ICANN’s TLD list 


{% alert important %}
Unicode is accepted for only for the local part of the email address.
Unicode is not accepted for the domain part, but may be punycode-encoded and will be accepted. 
{% endalert %}

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

**Please note that this is a beta feature.**
This validation is used for dashboard email addresses, end-user email addresses (your customers), from and reply-to addresses done of an email message .
{% endalert %}


This new email validation process is an enhancement to Braze's existing email validation process. Email validation is done when a user’s email address has been updated or is being imported into Braze via API, CSV Upload or modified in the dashboard. Braze validates email addresses using [this Ruby gem][1]—the gem is set to relaxed mode and configured to accept UTF-8 character.  This validation is not to be confused with a validation service like Briteverify.  This is a check to verify that the syntax of an email address complies with RFC standards.

If Braze receives a request to add a user and the email address is considered invalid, you would see an error response in the API.  When uploading via CSV, the user would be created, but the email address will not be added.

Email Validation looks at both the Local part and Host part of an email address—the local part is anything before the @ symbol, and the host part is anything after the @ symbol. Note that this process is only validating the syntax of the email address, and does not take into account whether the domain has a valid MX server or if the user exists on the domain listed. 


# Local Part Validation Rules
## Microsoft Domains
If the host domain has "msn, hotmail, outlook, or live", then the following regex is allowed for the local part:


`/\A[a-z][\-\w]*(?:\.[\-\w]+)*\z/`

The regex must follow these parameters:

- Can start with a character (a-z), an underscore (*_*) or a number (0-9).  If starting with a number, the local-part must contain atleast one other character
- Can contain any alphanumeric character (a-z or 0-9) or an underscore (*_*)
- Can  contain the following characters (*.*) or (*-*)
- Can not start or end with a period (*.*) or hyphen (*-*)
- Cannot contain two or more consecutive periods (*.*)
- Can end with a hyphen (*-*)


## All Other Domains
For all other domains, Braze allows the following regex for the local part:


`/\A[\p\{L}\p\{N}_]+(?:[\.\-\+\']+[\p\{L}\p\{N}_]+)*\z/`

The regex must follow these parameters:
- Can contain any letter, number or underscore, including Unicode letters and numbers
- Can contain but may not start or end with the following characters: (*.*) (*-*) (*+*) or (*'*)

{% alert important %}
If the domain part is a Gmail address, the local part needs to be at least 5 characters long. This is in addition to the regex validation specified above under "All other domains".
{% endalert %}


# Host Part Validation Rules
IPv4 or IPv6 addresses are now allowed in the host part of an email address. Also, the top level domain (e.g. .com, .org, .net, etc.) may not be fully numeric.

The following regex is allowed for the host part: 

`/^[a-z\d](?:[a-z\d-]{0,61}[a-z\d])?(?:\.[a-z\d](?:[a-z\d-]{0,61}[a-z\d])?)+$/i`

The regex must also follow these parameters:

- Consists of two or more period-separated parts. 
- Must contain at least one period (*.*)
- Cannot contain two or more consecutive periods
- Must start with an alphanumeric character (a-z or 0-9)
- Must end with an alphanumeric character (a-z or 0-9)
- Intermediate characters may include a dash (*-*)
- Contains from 1 to 63 characters
- Can end with a hyphen (*-*)

**Additional validation required** 
- The final part must be a valid top level domain (TLD) which is determined by anything after the final ‘.’ and must contain at least one alphabetic character.
- The TLD should be in [ICANN’s TLD list][2].


{% alert important %}
Unicode is accepted for only for the local part of the email address.
Unicode is not accepted for the domain part, but it may be punycode-encoded. 
{% endalert %}

[1]: https://github.com/afair/email_address
[2]: https://data.iana.org/TLD/tlds-alpha-by-domain.txt
[3]: {{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#managing-user-subscriptions

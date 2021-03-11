---
nav_title: Email Validation 
alias: "/email_validation/"
page_order: 4.5
description: "This article covers local and host part validation rules for email addresses"
---

# Email Technical Guidelines & Notes

## Email Validation

{% alert important %}
This validation is used for dashboard email addresses, end-user email addresses (your customers), and from and reply-to addresses done of an email message.
{% endalert %}

> This new email syntax validation process is an enhancement to Braze's existing email syntax validation process. Email validation is done when a user’s email address has been updated or is being imported into Braze via API, CSV Upload, or modified in the dashboard. This validation is not to be confused with a validation service like Briteverify. This is a check to verify that the syntax of an email address is correct (for example: has an @ symbol). One of the main drivers to use this new validation process is to provide support for international characters (i.e. UTF-8) in the local part of the email address.

Email Syntax Validation looks at both the Local and Host part of an email address. The local part is anything before the @ symbol, and the host part is anything after the @ symbol. Note that this process is only validating the syntax of the email address, and does not take into account whether the domain has a valid MX server or if the user exists on the domain listed.

__Note: If the domain part contains any non-ASCII characters, it will need to be punycode-encoded before being supplied to Braze__

If Braze receives a request to add a user and the email address is considered invalid, you would see an error response in the API. When uploading via CSV, a user would be created, but the email address would not be added.


# Local Part Validation Rules
## Microsoft Domains
If the host domain includes "msn, hotmail, outlook, or live", then the following regex will be used to validate the local part:


`/\A\w[\-\w]*(?:\.[\-\w]+)*\z/i`

The microsoft address local part must follow these parameters:

- Can start with a character (a-z), an underscore (_), or a number (0-9).  
- Can contain any alphanumeric character (a-z or 0-9) or an underscore (_)
- Can contain the following characters (.) or (-)
- Can not start with a period (.) or hyphen (-)
- Can not contain two or more consecutive periods (.)
- Can not end with a period (.)


## All Other Domains
For all other domains, Braze allows email addresses matching the following regex for the local part:


`\A[\p{L}\p{N}_](?:[\.\+\'\p{L}\p{N}_&#\/\-]*[\p{L}\p{N}_\-])?\z`

The local part must follow these parameters:
- Can contain any letter, number or underscore, including Unicode letters and numbers
- Can contain but may not start or end with the following characters: (.) (+) (&) (#) (/) or (`'`)
- Can contain and end with, but may not start with the following character: (-)

{% alert important %}
If the domain part is a Gmail address, the local part needs to be at least 5 characters long. This is in addition to the regex validation specified above under "All other domains".
{% endalert %}


# Host Part Validation Rules
IPv4 or IPv6 addresses are not allowed in the host part of an email address. Also, the top-level domain (e.g. .com, .org, .net, etc.) may not be fully numeric.

The following regex is used to validate the domain:

`/^[a-z\d](?:[a-z\d-]{0,61}[a-z\d])?(?:\.[a-z\d](?:[a-z\d-]{0,61}[a-z\d])?)+$/i`

The domain name must follow these parameters:

- Consists of two or more period-separated labels.
	- (Each part of a domain name is referred to as a "label". e.g. the domain name "example.com", consists of the "example" label and the "com" label.)
- Must contain at least one period (.)
- Cannot contain two or more consecutive periods
- Each period-separated label must:
	- Start with an alphanumeric character (a-z or 0-9)
	- End with an alphanumeric character (a-z or 0-9)
	- Only contain alphanumeric character (a-z or 0-9) and the hyphen (-)
	- Contain from 1 to 63 characters

**Additional validation required** 
- The final label of the domain must be a valid top-level domain (TLD) which is determined by anything after the final period (.)
- The TLD should be in [ICANN’s TLD list][2].

{% alert important %}
Unicode is accepted only for the local part of the email address.
Unicode is not accepted for the domain part, but it may be punycode-encoded. 
{% endalert %}

[2]: https://data.iana.org/TLD/tlds-alpha-by-domain.txt

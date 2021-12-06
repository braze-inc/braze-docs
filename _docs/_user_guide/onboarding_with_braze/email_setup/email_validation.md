---
nav_title: Email Validation 
article_title: Email Validation
alias: "/email_validation/"
page_order: 4.5
page_type: reference
description: "This reference article covers local and host part validation rules for email addresses."
channel: email

---

# Email technical guidelines and notes

> This reference article covers local and host part validation rules for email addresses.

## Email validation

{% alert important %}
Validation is used for dashboard email addresses, end-user email addresses (your customers), and from and reply-to addresses done of an email message.
{% endalert %}

Email validation is done when a user's email address has been updated or is being imported into Braze via API, CSV Upload, or modified in the dashboard. Braze automatically adjusts inputted email addresses to trim any whitespace. Email addresses targeted via the Braze servers must be validated per [RFC 2822](http://tools.ietf.org/html/rfc2822) standards. In addition to these standards, Braze does not accept certain characters (noted below) and recognizes them as invalid.

{% details Unaccepted characters outside of RFC Standards %}
- *
- /
- ?
- !
- $
- #
- %
- &#94;
- &
- (
- )
- {
- }
- [
- ]
- ~
- ,
{% enddetails %}

This validation is not to be confused with a validation service like Briteverify. This is a check to verify that the syntax of an email address is correct. One of the main drivers to use this new validation process is to support international characters (i.e., UTF-8) in the local part of the email address.

Email syntax validation looks at both the local and host part of an email address. The local part is anything before the @ symbol, and the host part is anything after the @ symbol. Note that this process is only validating the syntax of the email address and does not consider whether the domain has a valid MX server or if the user exists on the domain listed.

{% alert note %}
If the domain part contains any non-[ASCII](https://en.wikipedia.org/wiki/ASCII) characters, it will need to be [Punycode-encoded](https://www.punycoder.com/) before being supplied to Braze.
{% endalert %}

If Braze receives a request to add a user and the email address is considered invalid, you would see an error response in the API. When uploading via CSV, a user would be created, but the email address would not be added.

## Local part validation rules

### Microsoft domains

If the host domain includes "msn", "hotmail", "outlook", or "live", then the following regex will be used to validate the local part:<br>
`/\A\w[\-\w]*(?:\.[\-\w]+)*\z/i`

The Microsoft address local part must follow these parameters:

- Can start with a character (a-z), an underscore (_), or a number (0-9).  
- Can contain any alphanumeric character (a-z or 0-9) or an underscore (_)
- Can contain the following characters (.) or (-)
- Cannot start with a period (.) or hyphen (-)
- Cannot contain two or more consecutive periods (.)
- Cannot end with a period (.)

### All other domains

For all other domains, Braze allows email addresses matching the following regex for the local part:<br>
`\A[\p{L}\p{N}_](?:[\.\+\'\p{L}\p{N}_&#\/\-]*[\p{L}\p{N}_\-])?\z`

The local part must follow these parameters:
- Can contain any letter, number, or underscore, including Unicode letters and numbers
- Can contain but may not start or end with the following characters: (.) (+) (&) (#) (/) or (")
- Can contain and end with, but may not start with the following character: (-)

{% alert important %}
If the domain part is a Gmail address, the local part needs to be at least five characters long. This is in addition to the regex validation specified above under "All other domains".
{% endalert %}

## Host part validation rules

IPv4 or IPv6 addresses are not allowed in the host part of an email address. Also, the top-level domain (e.g. .com, .org, .net, etc.) may not be fully numeric.

The following regex is used to validate the domain:<br>
`/^[a-z\d](?:[a-z\d-]{0,61}[a-z\d])?(?:\.[a-z\d](?:[a-z\d-]{0,61}[a-z\d])?)+$/i`

The domain name must follow these parameters:

- Consists of two or more period-separated labels
	- (Each part of a domain name is referred to as a "label". e.g., the domain name "example.com" consists of the "example" label and the "com" label.)
- Must contain at least one period (.)
- Cannot contain two or more consecutive periods
- Each period-separated label must:
	- Only contain alphanumeric character (a-z or 0-9) and the hyphen (-)
	- Start with an alphanumeric character (a-z or 0-9)
	- End with an alphanumeric character (a-z or 0-9)
	- Contain 1 to 63 characters

**Additional Validation Required:**<br>
The final label of the domain must be a valid top-level domain (TLD) which is determined by anything after the final period (.). This TLD should be in [ICANN's TLD list][2]. The Braze email validator only ensures the syntax of the email is correct according to the regex listed above. It does not catch typos or addresses that don't exist.

{% alert important %}
Unicode is accepted only for the local part of the email address.<br>
Unicode is not accepted for the domain part, but it may be Punycode-encoded. 
{% endalert %}

[2]: https://data.iana.org/TLD/tlds-alpha-by-domain.txt

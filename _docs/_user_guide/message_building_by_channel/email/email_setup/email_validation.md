---
nav_title: Email Validation 
article_title: Email Validation
alias: "/email_validation/"
page_order: 3
page_type: reference
description: "This reference article covers local and host part validation rules for email addresses."
channel: email

---

# Email validation

> This reference article covers local and host part validation rules for email addresses. Validation is used for dashboard email addresses, end-user email addresses (your customers), and from and reply-to addresses of an email message.

## How it works

Email validation is performed when a user's email address has been updated or is being imported into Braze via API, CSV upload, or SDK, or modified in the dashboard. Note that your email addresses cannot include whitespaces. If you're using the API, whitespaces will result in a `400` error.

Braze does not accept certain characters and recognizes them as invalid. If an email is bounced, Braze marks the email as invalid and the subscription status is not changed.  

{% details Accepted characters %}
- Letters (A-Z)
- Numbers (0-9)
- Symbols
	- -
	- &#94;
	- +
	- $
	- '
	- &
	- #
	- /
	- %
	- *
	- =
	- `
	- |
	- ~
	- !
	- ?
	- . (only between letters or other characters)
{% enddetails %}

{% details Unaccepted characters %}
- Whitespaces (ASCII and Unicode)
{% enddetails %}

This validation is not to be confused with a validation service like Briteverify. This is a check to verify that the syntax of an email address is correct. One of the main drivers to use this validation process is to support international characters (such as UTF-8) in the local part of the email address.

Email syntax validation looks at both the local and host part of an email address. The local part is anything before the asperand (@), and the host part is anything after the asperand. For example, this local part of an email address may start and end with any of the allowed characters except for a period (.). Note that this process is only validating the syntax of the email address and does not consider whether the domain has a valid MX server or if the user exists on the domain listed.

{% alert note %}
If the domain part contains any non-[ASCII](https://en.wikipedia.org/wiki/ASCII) characters, it will need to be [Punycode-encoded](https://www.punycoder.com/) before being supplied to Braze.
{% endalert %}

If Braze receives a request to add a user and the email address is considered invalid, you'll see an error response in the API. When uploading via CSV, a user would be created, but the email address would not be added.

## Local part validation rules

### General email validation

For most domains, the local part must follow these parameters:
- Can contain any letter, number, including Unicode letters and numbers as well as the following characters: (+) (&) (#) (_) (-) (^) or (/)
- Can contain but may not start or end with the following character: (.)
- Cannot contain double quotes (")
- Must be between 1 and 64 characters in length


The following regular expression can be used to validate if an email address will be considered valid:
```
/\A([a-zA-Z0-9_\-\^+$'\&#\/!%\*=\?`\|~]|[[^\p{ASCII}\p{Space}]&&\p{Alnum}\p{Punct}\p{S}])(([a-zA-Z0-9_\-\^+$'\&#\/!%\*=\?`\|~\.]|[[^\p{ASCII}\p{Space}]&&\p{Alnum}\p{Punct}\p{S}])*([a-zA-Z0-9_\-\^+$'\&#\/!%\*=\?`\|~]|[[^\p{ASCII}\p{Space}]&&\p{Alnum}\p{Punct}\p{S}]))?\z/
```

### Gmail addresses

If the domain part is a Gmail address, the local part needs to be at least two characters long and must follow the regular expression validation listed above.

### Microsoft domains

If the host domain includes "msn", "hotmail", "outlook", or "live", then the following regular expression will be used to validate the local part: `/\A\w[\-\w]*(?:\.[\-\w]+)*\z/i`

The Microsoft address local part must follow these parameters:

- Can start with a character (a-z), an underscore (_), or a number (0-9).  
- Can contain any alphanumeric character (a-z or 0-9) or an underscore (_)
- Can contain the following characters: (.) or (-)
- Cannot start with a period (.)
- Cannot contain two or more consecutive periods (.)
- Cannot end with a period (.)

Note that the validation test checks if the local part, preceding the "+", matches the regular expression.

## Host part validation rules

IPv4 or IPv6 addresses are not allowed in the host part of an email address. The top-level domain (such as .com, .org, .net, etc.) may not be fully numeric.

The following regular expression is used to validate the domain:<br>
`/^[a-z\d](?:[a-z\d-]{0,61}[a-z\d])?(?:\.[a-z\d](?:[a-z\d-]{0,61}[a-z\d])?)+$/i`

The domain name must follow these parameters:

- Consists of two or more period-separated labels
	- Each part of a domain name is referred to as a "label". For example, the domain name "example.com" consists of the "example" label and the "com" label.
- Must contain at least one period (.)
- Cannot contain two or more consecutive periods
- Each period-separated label must:
	- Only contain alphanumeric character (a-z or 0-9) and the hyphen (-)
	- Start with an alphanumeric character (a-z or 0-9)
	- End with an alphanumeric character (a-z or 0-9)
	- Contain 1 to 63 characters

### Additional validation required

The final label of the domain must be a valid top-level domain (TLD) which is determined by anything after the final period (.). This TLD should be in [ICANN's TLD list](https://data.iana.org/TLD/tlds-alpha-by-domain.txt). The Braze email validator only checks that the syntax of the email is correct according to the regular expression listed in this section. It does not catch typos or addresses that don't exist.

{% alert important %}
Unicode is accepted only for the local part of the email address. Unicode is not accepted for the domain part, but it may be Punycode-encoded. 
{% endalert %}


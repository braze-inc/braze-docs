---
nav_title: Email validation
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

Braze validates an email address when it is updated, imported via API, CSV upload, SDK, or modified in the dashboard. Email addresses cannot include whitespace. If you use the API, whitespace returns a `400` error.

Braze rejects certain characters and marks the address invalid. If an email bounces, Braze marks the address invalid and does not change subscription status. If the email body contains non-standard [ASCII](https://en.wikipedia.org/wiki/ASCII) characters, Braze doesn't send the email.

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

This validation is a syntax check, not a validation service. One goal of this process is to support international characters (such as UTF-8) in the local part of the email address.

Braze validates syntax for both the local and host parts of an email address. The local part is anything before the asperand (@); the host part is anything after. The local part may start and end with any allowed character except a period (.). This process doesn't consider whether the domain has a valid MX server or if a user exists on that domain.

{% alert important %}
If the domain part contains any non-standard ASCII characters, it will need to be [Punycode-encoded](https://www.punycoder.com/) before being supplied to Braze.
{% endalert %}

If Braze receives a request to add a user with an invalid email address, the API returns an error. For a CSV upload, Braze creates the user but omits the invalid email address.

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

If the domain part is Gmail, the local part must be at least two characters long and follow the regular expression validation listed above.

### Microsoft domains

If the host domain includes "msn", "hotmail", "outlook", or "live", Braze uses the following regular expression to validate the local part: `/\A\w[\-\w]*(?:\.[\-\w]+)*\z/i`

The Microsoft address local part must follow these parameters:

- Can start with a character (a-z), an underscore (_), or a number (0-9).  
- Can contain any alphanumeric character (a-z or 0-9) or an underscore (_)
- Can contain the following characters: (.) or (-)
- Cannot start with a period (.)
- Cannot contain two or more consecutive periods (.)
- Cannot end with a period (.)

The validation test checks whether the local part preceding the "+" matches the regular expression.

## Host part validation rules

The host part cannot be an IPv4 or IPv6 address. The top-level domain (such as .com, .org, .net) can't be fully numeric.

The following regular expression is used to validate the domain:<br>
`/^[a-z\d](?:[a-z\d-]{0,61}[a-z\d])?(?:\.[a-z\d](?:[a-z\d-]{0,61}[a-z\d])?)+$/i`

The domain name must meet these parameters:

- Consists of two or more period-separated labels
	- Each part of a domain name is referred to as a "label". For example, the domain name "example.com" consists of the "example" label and the "com" label.
- Must contain at least one period (.)
- Cannot contain two or more consecutive periods
- Each period-separated label must:
	- Only contain alphanumeric characters (a-z or 0-9) and the hyphen (-)
	- Start with an alphanumeric character (a-z or 0-9)
	- End with an alphanumeric character (a-z or 0-9)
	- Contain 1 to 63 characters

### Additional validation required

The final label of the domain must be a valid top-level domain (TLD), determined by anything after the final period (.). This TLD should appear in [ICANN's TLD list](https://data.iana.org/TLD/tlds-alpha-by-domain.txt). The Braze validator only checks syntax. It doesn't catch typos or non-existent addresses.

{% alert important %}
Unicode is accepted only for the local part of the email address. Unicode is not accepted for the domain part, but it may be Punycode-encoded. 
{% endalert %}


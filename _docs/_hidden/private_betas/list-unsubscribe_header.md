---
nav_title: List-Unsubscribe Header
article_title: List-Unsubscribe Header
permalink: /list-unsubscribe/
hidden: true
---

### Customizing the list-unsubscribe header

#### Requirements

If you're sending emails using your own custom unsubscribe functionality, you must meet the following requirements to make sure the one-click unsubscribe URL that you set up is in accordance with RFC 8058.

* The URL must be able to handle unsubscribe POST requests
* The URL must be HTTPS
* The URL must not return an HTTPS redirect. One-click unsubscribe links that go to a landing or other type of web page don't comply with RFC 8058
* The message must have a valid DKIM signature

Select **Custom list-unsubscribe header** to add your own configured one-click unsubscribe endpoint, and an optional "mailto:". Braze requires an input for URL to support a custom list-unsubscribe header because the one-click unsubscribe HTTP is a requirement from Yahoo and Gmail for bulk senders.

![]({% image_buster /assets/img/email_settings/email_unsubscribe_header_custom.png %}){: style="max-width:80%;"}
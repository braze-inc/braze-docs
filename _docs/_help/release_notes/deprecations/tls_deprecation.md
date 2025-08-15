---
nav_title: TLS 10 & 11 deprecation
page_order: 2

page_type: update
description: "This article describes Braze's deprecation of TLS 1.0 and TLS 1.1, completed in May 2018."
---
# TLS 1.0 & 1.1 deprecation

{% alert update %}
Braze has removed support for Transport Layer Security (TLS) ciphers in both TLS 1.0 and 1.1, in accordance with recommendations made by the PCI Security Standards Council. We performed this deprecation of support in two phases, completed in May 2018.
{% endalert %} 

## Background

Braze is deprecating known weak Transport Layer Security (TLS) ciphers in both TLS 1.0 and 1.1, in accordance with recommendations made by the PCI Security Standards Council in two phases concluding in May 2018.

This change is not being made in response to any breach or issue related to Braze's platform, but as a precautionary measure to maintain our best-in-class security and data standards, and to proactively safeguard our clients and their customers.

In recent years, a number of systematic security issues associated with both TLS and its predecessor, Secure Sockets Layer (SSL), including [POODLE](https://www.us-cert.gov/ncas/alerts/TA14-290A), [Heartbleed](https://en.wikipedia.org/wiki/Heartbleed), [LOGJAM](https://en.wikipedia.org/wiki/Logjam_(computer_security)), and others, threatened encrypted web traffic and exposed portions of the internet to security breaches. Along with other technology companies, Braze has previously taken action to disable weak encryption protocols and ciphers as attacks are discovered—for instance, by removing support for SSLv3 in 2014.

More recently, the PCI Security Standards Council released encryption-related guidance in April 2015 for the [Payment Card Industry Data Security Standard](https://en.wikipedia.org/wiki/Payment_Card_Industry_Data_Security_Standard) (PCI-DSS). The guidance excludes SSL 3.0, TLS 1.0, and some of the cipher suites supported by TLS 1.1 from their protocol list of strong cryptographic ciphers, and encourages companies from discontinuing support for those protocols or ciphers to ensure the security of internet users.

A cipher suite is a combination of algorithms that provide encryption, authentication, and communications integrity when negotiating a secure SSL or TLS connection. When it's discovered that it's possible for a given cipher to be broken—whether or not there are any current known attacks—the cipher is considered to have "weaknesses" that could enable future attacks. By excluding these TLS ciphers from PCI DSS compliance requirements, the PCI DSS Council is requiring service providers to support only best-in-class encryption standards. The PCI DSS Council has set a deadline of June 30, 2018 for compliance with the encryption requirement to drop support for TLS 1.0 and TLS 1.1.

## Braze's deprecation plan
In order to comply with the PCI DSS Council's recommendations, Braze will be raising the minimum versions of TLS that we support on our Services. To give you a better idea about our compliance plan and its potential impact on your brand and your users, there are two main phases to our plan to be aware of:

### Phase 1: October 1, 2017

Braze will remove the ability to use the following ciphers from Braze's Web dashboard and REST APIs:

- `TLS_RSA_WITH_AES_256_CBC_SHA`
- `TLS_RSA_WITH_AES_128_CBC_SHA`
- `TLS_RSA_WITH_AES_256_CBC_SHA256`
- `TLS_RSA_WITH_AES_256_GCM_SHA384`
- `TLS_RSA_WITH_AES_128_CBC_SHA256`
- `TLS_RSA_WITH_AES_128_GCM_SHA256`
- `TLS_RSA_WITH_3DES_EDE_CBC_SHA`

This change should not impact customers accessing the Braze dashboard, as all modern web browsers support more secure ciphers. However, if you do experience a SSL encryption error when accessing the web dashboard after October 1, you will be able to fix the issue by simply upgrading to the latest version of your web browser.

Your engineering team should ensure that they aren't using any of these ciphers for server-to-server communication with Braze's REST APIs. If they are, they'll need to update their code to use more secure encryption ciphers prior to October 1 in order to continue making use of Braze's APIs. However, in order to maintain support for old and outdated mobile devices which may be using weak ciphers, Braze will continue to support these ciphers on the APIS that received data from our SDKs.

### Phase 2: May 31, 2018

Braze will be disabling support for TLS 1.0 and TLS 1.1 across all Braze Services on May 31, 2018—including the Braze dashboard, REST APIs, and APIs that communicate with our SDKs. We'll also remove support for the ciphers listed in the preceding section in connection with the APIs that receive SDK data. That means that all TLS 1.0 and 1.1 communication to and from Braze will not be supported by our network as of this date.

As a result of this change, some old or outdated mobile devices—likely ones running early versions of Android—may lose the ability to communicate with Braze, barring them from sending data to Braze or receiving in-app messages from Braze. However, we anticipate that the change will affect only a small number of devices. Any devices that are affected will also lose the ability to communicate with any PCI-compliant website or service a month later on June 30, 2018, the date set by the PCI DSS Council for removal of TLS 1.0 and TLS 1.1 ciphers.

## Action plan
If your brand is making use of Braze's REST APIs, speak to your engineering team to ensure that all server-to-server calls to Braze s using TLS 1.2 by the listed above in order to avoid an interruption of service. Be aware that some programming languages—such as Java 7—use older versions of TLS by default, so your engineering team may need to take some code changes to support the upgraded encryption requirements.

Apple devices will not be affected by Braze's planned deprecation because Apple has required TLS 1.2 since the end of 2016. The same is true of modern web browsers, so we do not anticipate that these changes will have any impact on Web SDK usage. However, Android devices running Android 4.4 (KitKat) or lower may not use TLS 1.2 by default, so take steps to upgrade any of your Android integrations to at least Braze SDK version 2.0.3 (which uses TLS 1.2 by default, if a given device can support it) by May 31, 2018.

Finally, because of the known weaknesses in TLS 1.0 and the TLS 1.1 cipher suite, it's possible that attacks could arise in the future which would require Braze to speed up our deprecation plan, in order to safeguard the security of all our customers. Braze will monitor the state of security and any relevant attacks associated with TLS 1.0 and 1.1 protocols, and will keep you in the loop if we learn of any attacks that will alter the timeline laid out in the preceding sections. But because of this potential impact, we highly recommend that you work with your engineering team to ensure that your API calls to Braze are secured with TLS 1.2, and that you plan to upgrade to the latest Android SDK in the coming months.



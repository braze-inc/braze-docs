{% alert important %}
Do not send legally required transactional emails to SMS gateways as there's a strong likelihood that those emails will not be delivered.
<br><br>
Although emails you send using a phone number and the provider’s gateway domain (known as an MM3) can result in the email being received as an SMS (text) message, some of our email providers do not support this behavior. For example, if you send an email to a T-Mobile phone number (such as "9999999999@tmomail.net"), your SMS message would be sent to whoever owns that phone number on the T-Mobile network.
<br><br>
Keep in mind that even though these emails may not be delivered to the SMS gateway, they will still count towards your email billing. To avoid sending emails to unsupported gateways, review the [list of unsupported gateway domain names](https://www.fcc.gov/consumer-governmental-affairs/about-bureau/consumer-policy-division/can-spam/domain-name-downloads).
{% endalert %}

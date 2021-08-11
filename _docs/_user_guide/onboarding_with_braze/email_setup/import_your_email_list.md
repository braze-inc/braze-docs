---
nav_title: Importing Your Email List into Braze
page_order: 4
page_type: reference
description: "This reference article covers best practices for importing your email list into Braze."
channel: email

---

# Importing Your Email List into Braze {#importing-email-lists}

An important step in setting yourself as a successful email sender is ensuring that you have a high-quality email list. Proper email list management can improve your deliverability and give you more accurate and clean campaign results.

1. __Validate your list to ensure you're only importing genuine email addresses.__<br>A high bounce rate can damage your email sender reputation. Email list cleaning services can do this for you by determining if the email address follows the correct syntax and has the physical properties of an email address, verifying the email domain, and connecting to the email server to authenticate if the email address exists there.<br><br>
2. __Remove deeply lapsed users.__<br>It is a best practice to not email users who have not engaged with an email in over six months as this can damage your email sender reputation. When importing your email list, ensure you don't import users who have not opened an email from you in the last six months. Long term, you should also consider implementing a [sunset policy][60].<br><br>
3. __Don't import any suppression lists.__<br>If you are transitioning off an existing email provider, make certain that you do not import users from a suppression list. Suppression lists feature email addresses that have either unsubscribed, marked your emails as spam, or hard bounced.

[60]: {{site.baseurl}}/help/best_practices/email/sunset_policies

---
nav_title: SMS Set Up
layout: featured
page_order: 4
guide_top_header: "Email Set Up"
guide_top_text: "Braze has just launched SMS! "

guide_featured_title: "Section Articles"
guide_featured_list:
- name: Terms to Know
  link: /docs/user_guide/onboarding_with_braze/sms/terms_to_know/
  fa_icon: fas fa-bookmark
- name: Create User Profiles
  link: /docs/user_guide/onboarding_with_braze/sms/importing_numbers/
  fa_icon: fas fa-user-circle
- name: Number Formatting
  link: /docs/user_guide/onboarding_with_braze/sms/number_formatting/
  fa_icon: far fa-comment
- name: Short Code Application
  link: /docs/user_guide/onboarding_with_braze/sms/short_code_application/
  fa_icon: far fa-address-card
- name: Requirements
  link: /docs/user_guide/onboarding_with_braze/sms/#requirements/
  fa_icon: far fa-check-square
- name: Compliance
  link: /docs/help/best_practices/sms/compliance/
  fa_icon: fas fa-gavel
---

## Requirements

Before you start sending sms, there are some things you need. Refer to the basic chart below to learn more.

|Requirement | Description | Acquirement |
|---|---|---|
| A Dedicated Phone Number (Short Code or Long Code, see below.) | A dedicated IP is a unique Internet address provided exclusively to a single hosting account. | Braze handles this application process on your behalf. It may take up to 12 weeks to receive approval for a Short Code. If you already have a dedicated number, please tell your Braze representative during your onboarding and integration process to plan it's transfer. |
|Short Code | Either a short or a long code are required. <br><br> This is a short, memorable 5-6 digit sequences that allows senders to send more messages at more consistent rates than long numbers (1 message per second). | Braze will apply and acquire this for you. You must let us know that you want one, as there are requirements beyond what is listed here. <br> <br>Getting a short code takes some time - you can expect a delay before you are assigned an approved short code. These are also subject to upfront and other charges. If you already have a short code and want to keep it after transferring service to Braze, please let your Braze representative know before your onboarding process begins. |
| Long Code | Either a short or a long code are required. <br><br> This is your standard, 10-digit phone number which allows senders to send 1 message per second. |
| List of Users with Phone Numbers | Before you can start sending messages, you must add users to your account. Additionally, you must know the approximate size of your audience.  | Users are initially added to Braze through our backend. You must pass this list to us to upload for you. Phone numbers must be formatted as 10-digit number, as well as a country area code. [Learn more here]({{ site.baseurl }}/user_guide/onboarding_with_braze/sms/importing_phone_numbers/). |
| Keyword Templates | Certain keywords must have responses attributed to it before you can begin messaging - specifically all  | You should list these out and send them to your Braze representative or onboarding manager during your onboarding process. You can check out some templates for that here. |

---
nav_title: Field-Level Encryption
article_title: Field-Level Encryption
permalink: "/field_level_encryption/"
description: "This reference article covers how to encrypt email addresses to minimize PII shared in Braze."
page_type: reference
---

# Field-level encryption

> Using field-level encryption, you can seamlessly encrypt email addresses with AWS Key Management Solution (KMS) and comply with industry regulations to minimize PII shared in Braze. Encryption replaces sensitive data with ciphertext, which is unreadable encrypted information.

{% alert important %}
Field-level encryption is currently available as a beta feature. Contact your Braze account manager if you're interested in participating in this beta.
{% endalert %}

## How it works

Email addresses must be hashed and encrypted before they’re added to Braze. When a message is sent, a call will be made to AWS KMS for the decrypted email address. Next, the hashed email address will be inserted into the metadata for delivery and engagement events to be linked to the original user. This is how Braze can track email analytics, and any plaintext email addresses are redacted if they’re included. Braze does not store the plaintext email address for the user.

## Prerequisites

To use field-level encryption, you must have access to AWS KMS to encrypt and hash email addresses **before** sending them to Braze. 

Follow these steps to set up your AWS secret key authentication method.

1. To retrieve your access key ID and secret access key, create an IAM user and administrators group in AWS.
2. Select **Show User Security Credentials** to reveal your access key ID and secret access key. Next, note these credentials somewhere or select the **Download Credentials** button as you'll need to input these when connecting your AWS KMS keys.
3. 
4. 

## Step 1: Connect your AWS KMS keys

For your AWS KMS settings, enter the following:

- Access key ID
- Secret access key
- HMAC key ID (this cannot be updated after saving)

## Step 2: Select your encryption fields

Next, select Email address to encrypt the field. 

When encryption is enabled for a field, it can’t be reverted to a decrypted field. This means encryption is a permanent setting. When setting up encryption for email address, please ensure that no users have email addresses in the workspace. This ensures that no plaintext email addresses are stored in Braze when enabling the feature for the workspace.

![]({% image_buster /assets/img/field_level_encryption.png %})

## Step 3: Import and update users

When field-level encryption is enabled, you must hash and encrypt the email address before adding to Braze. Be sure to downcase the email address before hashing it. See [user attributes object](#user-attributes-object) for more details.

When updating email address in Braze, you should use the hashed email value wherever `email` is included. This includes:

- REST endpoints:
    - `/users/track`
    - `/campaigns/trigger/send`
    - `/canvas/trigger/send`
    - `/transactional/v1/campaigns/{campaign_id}/send`
- Adding or updating users via CSV

{% alert note %}
When creating a new user, you must add `encrypted_email` with the user's encrypted email value. Otherwise, the user will not be created.
{% endalert %}

## Considerations

These features are not supported with field-level encryption

- SDK
- Audience sync
- In-app message email capture forms
- Email address filter by regular expression

### User attributes object

When using field-level encryption with the `/users/track` endpoint, note these field details for the [user attributes object]({{site.baseurl}}/api/objects_filters/user_attributes_object):

- The `email` field must be the hashed value of the email.
- The `encrypted_email` field must be the encrypted value for the email.

## Frequently asked questions

### What is the difference between encrypting and hashing?

Encryption is a two-way function where it’s possible to encrypt and decrypt data. If the same plaintext value is encrypted multiple times, AWS’s encryption algorithm (AES-256-GCM) will yield different encrypted values. Hashing is a one-way function where the plaintext is scrambled in a way that can’t be decrypted. Hashing yields the same value each time. This enables us to support maintaining subscription states across multiple users that share the same email address.

### What email address should I use in my test send?
Plaintext email addresses are supported in test sending. To see how an email looks for a specific user, do the following:

1. Select **Preview message as a user**.
2. In **Test Send**, select **Override recipients attributes with current preview user’s attributes**.

### What happens if I add this email address Liquid {{${email_address}}} in Braze?

Braze will render the plaintext email address when sending the email. In previews, we’d display the encrypted version of the email. We recommend using the user's external ID if you’re referencing a user in a custom one-click URL.

{%raw%}`{{${email_address}}}`{%endraw%} is not currently supported in the preference center and unsubscribe pages.

### What email address should I expect to see in Currents?

The hashed email address is included in email delivery and engagement events.

### What email address should I expect to see in Message Archiving?

The plaintext email address is included in Messaging Archiving. These are sent directly to the customer’s cloud storage provider and there may be other personal data included in the email bodies.

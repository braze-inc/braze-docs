---
nav_title: Identifier field-level encryption
article_title: Identifier Field-Level Encryption
page_order: 2
alias: "/field_level_encryption/"
description: "This reference article covers how to encrypt email addresses to minimize personally identifiable information (PII) shared in Braze."
page_type: reference
---

# Identifier field-level encryption

> Using identifier field-level encryption, you can seamlessly encrypt email addresses with AWS Key Management Service (KMS) to minimize personally identifiable information (PII) shared in Braze. Encryption replaces sensitive data with ciphertext, which is unreadable encrypted information.

{% alert important %}
Identifier field-level encryption is available as an add-on feature. To get started with identifier field-level encryption, contact your Braze account manager.
{% endalert %}

## How it works

Email addresses must be hashed and encrypted before they’re added to Braze. When a message is sent, a call will be made to AWS KMS for the decrypted email address. Next, the hashed email address will be inserted into the metadata for delivery and engagement events to be linked to the original user. This is how Braze can track email analytics. Braze will redact any plaintext email addresses that are included and won't store the plaintext email address for the user.

## Prerequisites

To use identifier field-level encryption, you must have access to AWS KMS to [encrypt](https://docs.aws.amazon.com/kms/latest/APIReference/API_Encrypt.html) and [hash](https://docs.aws.amazon.com/kms/latest/APIReference/API_GenerateMac.html) email addresses **before** sending them to Braze. 

Follow these steps to set up your AWS secret key authentication method.

1. To retrieve your access key ID and secret access key, [create an IAM user and administrators group](https://docs.aws.amazon.com/IAM/latest/UserGuide/getting-set-up.html#create-an-admin) in AWS with a permissions policy for AWS Key Management Service. The IAM user must have the [kms:Decrypt](https://docs.aws.amazon.com/kms/latest/APIReference/API_Decrypt.html) and [kms:GenerateMac](https://docs.aws.amazon.com/kms/latest/APIReference/API_GenerateMac.html) permissions. For more details, refer to [AWS KMS permissions](https://docs.aws.amazon.com/kms/latest/developerguide/kms-api-permissions-reference.html).
2. Select **Show User Security Credentials** to reveal your access key ID and secret access key. Note these credentials somewhere or select the **Download Credentials** button as you'll need to input these when connecting your AWS KMS keys.
3. You must set up KMS in the following AWS regions:
    - **Braze US clusters:** `us-east-1`
    - **Braze EU clusters:** `eu-central-1`
4. In AWS Key Management Service, create two keys and make sure that the IAM user is added in key usage permissions:
    - **[Encrypt/decrypt](https://docs.aws.amazon.com/kms/latest/developerguide/create-keys.html#create-symmetric-cmk):** Select **Symmetric** key type and **Encrypt and Decrypt** key usage.
    - **[Hash](https://docs.aws.amazon.com/kms/latest/developerguide/hmac-create-key.html):** Select **Symmetric** key type and **Generate and Verify MAC** key usage. The key spec should be **HMAC_256**. After creating the key, note the HMAC key ID somewhere as you’ll need to input this in Braze.

![]({% image_buster /assets/img/field_level_encryption_aws_prereq.png %})

## Step 1: Connect your AWS KMS keys

In the Braze dashboard, go to **Data Settings** > **Field-Level Encryption**. For your AWS KMS settings, enter the following:

- Access key ID
- Secret access key
- HMAC key ID (this cannot be updated after saving)

## Step 2: Select your encrypted fields

Next, select **Email address** to encrypt the field. 

When encryption is turned on for a field, it can’t be reverted to a decrypted field. This means encryption is a permanent setting. When setting up encryption for email address, confirm that no users have email addresses in the workspace. This makes sure that no plaintext email addresses are stored in Braze when turning on the feature for the workspace.

![]({% image_buster /assets/img/field_level_encryption.png %})

## Step 3: Import and update users

When identifier field-level encryption is turned on, you must hash and encrypt the email address before adding to Braze. Be sure to downcase the email address before hashing it. See [user attributes object](#user-attributes-object) for more details.

When updating email address in Braze, you should use the hashed email value wherever `email` is included. This includes:

- REST endpoints:
    - `/users/track`
    - `/campaigns/trigger/send`
    - `/canvas/trigger/send`
    - `/transactional/v1/campaigns/{campaign_id}/send`
- Adding or updating users via CSV

{% alert note %}
When creating a new user with an email address, you must add `email_encrypted` with the user's encrypted email value. Otherwise, the user will not be created. Similarly, if you're adding an email address to an existing user who doesn't have an email, you must add `email_encrypted`. Otherwise, the user will not be updated.
{% endalert %}

## Considerations

These features are not supported with identifier field-level encryption:

- Identifying and capturing email address via SDK
- In-app message email capture forms
- Reporting on recipient domain, including Email Insights mailbox provider charts
- Email address filter by regular expression
- Audience sync
- Shopify integration

### User attributes object

When using identifier field-level encryption with the `/users/track` endpoint, note these field details for the [user attributes object]({{site.baseurl}}/api/objects_filters/user_attributes_object):

- The `email` field must be the hashed value of the email.
- The `email_encrypted` field must be the encrypted value for the email.

## Frequently asked questions

### What is the difference between encrypting and hashing?

Encryption is a two-way function where it’s possible to encrypt and decrypt data. If the same plaintext value is encrypted multiple times, AWS’s encryption algorithm (AES-256-GCM) will yield different encrypted values. Hashing is a one-way function where the plaintext is scrambled in a way that can’t be decrypted. Hashing yields the same value each time. This allows us to support maintaining subscription states across multiple users that share the same email address.

### What email address should I use in my test send?

Plaintext email addresses are supported in test sending. To see how an email looks for a specific user, do the following:

1. Select **Preview message as a user**.
2. In **Test Send**, select **Override recipients attributes with current preview user’s attributes**.

{%raw%}
### What happens if I add this email address Liquid `{{${email_address}}}` in Braze?

Braze will render the plaintext email address when sending the email. In previews, we’ll display the encrypted version of the email. We recommend using the user's external ID if you’re referencing a user in a custom one-click URL.

`{{${email_address}}}` is not currently supported in the preference center and unsubscribe pages.
{%endraw%}

### What email address should I expect to see in Currents?

The hashed email address is included in email delivery and engagement events.

### What email address should I expect to see in message archiving?

The plaintext email address is included in messaging archiving. These are sent directly to the customer’s cloud storage provider and there may be other personal data included in the email bodies.

### Can I use mail-to list-unsubscribe for subscription management with identifier field-level encryption?

No. Using mail-to list-unsubscribe would send the plaintext decrypted email address to Braze. With identifier field-level encryption turned on, we support the URL-based HTTP: method, including one-click. We also recommend including a one-click unsubscribe link in your email body.

### Does identifier field-level encryption support other identifiers like phone?

No. Currently, identifier field-level encryption is supported for email addresses only.

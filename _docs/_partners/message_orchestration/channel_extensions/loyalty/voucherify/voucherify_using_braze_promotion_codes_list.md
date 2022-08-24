---
nav_title: Voucherify and Promotion Codes List
article_title: Voucherify and Braze Promotion Codes List
page_order: 4
alias: /partners/voucherify/promotion/
description: "This article outlines the how you can share Voucherify codes using Braze Promo Codes snippet. First, export codes from Voucherify, then import codes to Braze and finally add an email code snippet to pull codes from the promotion list."
page_type: partner
search_tag: Partner
---

# Voucherify and Braze Promotion Codes List

> In addition to the Connected Content and Custom Attributes, you can share Voucherify codes using Braze Promo Codes snippet. First, export codes from Voucherify, then import codes to Braze and finally add an email code snippet to pull codes from the promotion list. Read on to learn more.

## Contents

- [Step 1: Export Unique Codes from Voucherify Campaign.](#step-1-export-unique-codes-from-voucherify-campaign)
- [Step 2: Create a Promotion Codes List in Braze.](#step-2-create-a-promotion-codes-list-in-braze)
- [Step 3: Upload CSV file](#step-3-upload-csv-file)
- [Step 4: Use Code Snippet in Braze Campaign](#step-4-use-code-snippet-in-braze-campaign)

---

## Step 1: Export Unique Codes from Voucherify Campaign.

![Export codes]({% image_buster /assets/img/voucherify/voucherify_promotion_export_codes.png %}){: style="margin-top:15px;"}

Edit the CSV file and remove the name of the column to leave the list of codes only.

![Exported codes]({% image_buster /assets/img/voucherify/voucherify_promotion_code_list_created.png %})

---

## Step 2: Create a Promotion Codes List in Braze.

![Create Promotion Code List]({% image_buster /assets/img/voucherify/voucherify_promotion_create_list.png %}){: style="float:right;max-width:40%;margin-left:15px;margin-top:30px;"}

Go to the Promotion Codes in the Braze Integrations section and click **Create Promotion Code List**.

You can use the Voucherify campaign name to name the list and ensure data consistency.

![Campaign Name]({% image_buster /assets/img/voucherify/voucherify_promotion_code_list.png %}){: style="max-width:50%;"}

Besides the name, add the code snippet that refers to the codes from the list, it will be populated with a unique code once the message is sent.

You can set attributes for codes such as List Expiration and Threshold Alerts; however, note that Voucherify manages logic behind your codes regardless of list settings.

![List expiration]({% image_buster /assets/img/voucherify/voucherify_promotion_list_expiration.png %})

---

## Step 3: Upload CSV file

Upload the CSV file with Voucherify codes.

![Import Codes]({% image_buster /assets/img/voucherify/voucherify_promotion_import_codes.png %})

Confirm that the list only contains codes (and not column header) and click **Start Upload**.

![Upload CSV]({% image_buster /assets/img/voucherify/voucherify_promotion_upload_csv.png %}){: style="max-width:50%;"}

When the import is done, click **Save List** to confirm the list details.

---

## Step 4: Use Code Snippet in Braze Campaign

To use codes from the list in a Braze campaign, Copy Snippet and add it to the email body.

![Copy snippet]({% image_buster /assets/img/voucherify/voucherify_promotion_code_snippet.png %}){: style="max-width:50%;"}

Add the code snippet to display a code from the list.

![Braze email code snippet]({% image_buster /assets/img/voucherify/voucherify_promotion_liquid_email.png %})

Once the message with code is sent, the same code won’t be used ever again.

If you need help on any of the steps above, visit this detailed [Promo Codes User Guide]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/promotion_codes).

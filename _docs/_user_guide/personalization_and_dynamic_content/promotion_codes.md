---
nav_title: Promotion codes
article_title: Promotion Codes
page_order: 5
toc_headers: h2
alias: "/promotion_codes/"
description: "This reference article covers how to create promotion code lists and add them to your campaigns and Canvases."
---

# Promotion codes

> This page covers how to create promotion code lists and add them to your campaigns and Canvases.

## About promotion codes

Promotion codes let you insert unique, time-limited values into messages to drive conversions. Each list can hold up to 20 million codes, and every code can last up to six months before expiring.

When Braze sends a message with a promotion code, the code is deducted before the message goes out. To ensure codes are consistent, unique, and never reused:

- A failed message still consumes the code.
- In multichannel sends, the same code is applied across all channels.
- With conditional Liquid, all referenced lists have codes deducted, even if only one branch is shown.
- Entering or re-entering a Canvas step consumes a new code.

If you place multiple snippets from the same list in one message, Braze will apply the same code across all snippets. To avoid running out, we recommend uploading more codes than you expect to use.

{% tabs local %}
{% tab Example %}
Think of promotion codes like coupons at a post office. Once the clerk pulls a coupon from the stack for your letter, it’s gone—even if the letter never arrives.  

For example, in the following conditional Liquid, codes from both lists (`vip-deal` and `regular-deal`) are deducted, even though each user only sees one branch:

{% raw %}
```liquid
{% if user.is_vip %}
  {% promotion('vip-deal') %}
{% else %}
  {% promotion('regular-deal') %}
{% endif %}
```
{% endraw %}
{% endtab %}
{% endtabs %}

## Next steps



## Frequently asked questions (FAQ) {#faq}

### Which messaging channels can I use with promotion codes?

Promotion codes are currently supported for email, mobile push, web push, Content Cards, webhook, SMS, and WhatsApp. Braze Transactional Email campaigns and in-app messages do not currently support promotion codes.

### Do test and seed sends count towards usage?

By default, test sends and seed group email sends will use promotion codes per user, per test send. However, you can reach out to your Braze account manager to update this behavior to not use promotion codes during testing.

### Can I use multiple Liquid snippets to reference the same promotion code list in one message?

Yes. Braze will apply the same promotion code across all instances of that snippet in the message, ensuring the user only receives one unique code.

### What happens when a promotion code list is expired or empty?

Expired codes are deleted after six months.

If the message should have contained a promotion code from an empty or expired list, the message will be canceled. 

If the message contains Liquid logic that conditionally inserts a promotion code, the message will only be canceled if it should have contained a promotion code. If the message shouldn't have contained a promotion code, the message will send normally.

### I uploaded and saved the wrong promotion codes. How can I update my promotion codes?

If you've uploaded a CSV file with the incorrect promotion codes and selected **Save list**, you can resolve this by either method:

- Deprecate the entire list: Stop using the current promotion code list in any campaigns, Canvases, or templates. Then, upload the CSV file with the correct codes and use them in your messaging.
- Use the incorrect codes: Create a campaign that sends promotion codes from the incorrect promotion code list to a placeholder until all of the incorrect codes are used. Then, upload the correct promotion codes to the same list.

### How do I save a promotion code to a user's profile so it can be used in subsequent messages?

Yes. You can resolve this by deprecating the entire list or using a placeholder to delete the list. For more information, see [Updating promotion codes](#update).

### Can I save a promotion code to a user's profile for future messages?

- **Attribute Name:** Promo Code
- **Action:** Update
- **Key Value:** The promotion code's Liquid code snippet, such as {% raw %}`{% promotion('spring25') %}`{% endraw %}

Second, add the custom attribute (in this example, {% raw %}`{{custom_attribute.${Promo Code}}`{% endraw %}) to a message. The discount code will be templated in.

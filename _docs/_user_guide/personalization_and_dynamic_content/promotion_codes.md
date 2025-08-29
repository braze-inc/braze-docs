---
nav_title: Promotion codes
article_title: Promotion Codes
page_order: 5
toc_headers: h2
alias: "/promotion_codes/"
description: "Learn about promotion code lists, so you can add them to your campaigns and Canvases."
---

# Promotion codes

> Learn about promotion code lists, so you can add them to your campaigns and Canvases.

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

Looking for next steps? Start here:

- [Creating a promotion code list]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/promotion_codes/manage/#create)
- [Using promotion codes]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/promotion_codes/manage/#using-promotion-codes)
- [Viewing promotion code usage]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/promotion_codes/manage/#viewing-promotion-code-usage)

## Frequently asked questions

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

### If I uploaded the wrong promotion codes, can I update them?

Yes. You can resolve this by deprecating the entire list or using a placeholder to delete the list. For more information, see [Updating promotion codes]({[site.baseurl}}/user_guide/personalization_and_dynamic_content/promotion_codes/manage/#update).

### Can I save a promotion code to a user's profile for future messages?

Yes. You can save promotion codes to a user's profile through a User Update step. For more information, see [Saving promotion codes to user profiles]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/promotion_codes/manage/#save-to-profile).

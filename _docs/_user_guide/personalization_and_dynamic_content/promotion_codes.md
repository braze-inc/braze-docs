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

## How it works

Promotion codes—also called promo codes—are a great way to keep users engaged by driving interactions with a heavy emphasis on purchases. You can create messages that pull from your list of promotion codes. 

Each promotion code has an expiration date of up to six months and can be deleted before expiry by contacting [Support]({{site.baseurl}}/user_guide/administrative/access_braze/support/). You can store and manage up to 20 million codes per list. By managing and analyzing the performance of your promotion codes, you can make targeted decisions for your promotional strategies and messaging.

{% alert important %}
Promotion codes can't be sent in in-app messages in Canvas. If you're participating in the [early access](#promotion-codes-iam-campaigns), promotion codes can be sent in in-app message campaigns.
{% endalert %}

## Creating a promotion code list

### Step 1: Go to the Promotion Code section

![Button to create a promotion code.]({% image_buster /assets/img/promocodes/promocode1.png %}){: style="float:right;max-width:30%;margin-left:15px;"}

1. From the dashboard, go to **Data Settings** > **Promotion Codes**.
2. Select **Create Promotion Code List**.

### Step 2: Name the promotion code

1. Name your promotion code list and add an optional description.
2. Next, create a code snippet for the promotion code. 

Here are some details to consider when creating a code snippet:

- Once saved, code snippets can’t be edited.
- Snippets are case-sensitive. For example, "Birthday_promo" and "birthday_promo" will be recognized as two different snippets.
- Use the snippet name in Liquid to reference this set of promotion codes.
- Make sure the code snippet isn't already being used in another list.

![A promotion code list named "SpringSale2025" with the code snippet "spring25".]({% image_buster /assets/img/promocodes/promocode3.png %}){: style="max-width:80%"}

### Step 3: Choose promotion code options

Each promotion code list has a corresponding expiration date and time that gets set upon creation. The maximum expiration length is six months into the future from the day you're creating or editing your list. 

Within that time, you can change and update the expiration date repeatedly. This expiration date will apply to all codes added to this list. Upon expiration, the codes will be deleted from the Braze system, and any messages calling that list's code snippet will not be sent.

![List expiration settings that all remaining codes will expire on April 30, 2025 at 12 am.]({% image_buster /assets/img/promocodes/promocode4.png %}){: style="max-width:80%"}

You also have the option to set up optional and customized threshold alerts. If set up, these alerts will email the designated recipient either when the list is running low on available promotion codes in this list or when your promotion code list is close to expiration. The recipient will be notified once a day.

![An example of a threshold alert to notify "marketing@abc.com" when the promotion code list expires in 5 days.]({% image_buster /assets/img/promocodes/promocode5.png %}){: style="max-width:80%"}

### Step 4: Upload promotion codes

Braze doesn't manage code creation or redemption, meaning you must generate your promotion codes to a CSV file and upload them to Braze. 

Make sure your CSV file follows these guidelines:

- Includes a column for promotion codes.
- Has one promotion code per row.

You can use our built-in integration with [Voucherify]({{site.baseurl}}/partners/ecommerce/loyalty/voucherify/) or [Talon.One]({{site.baseurl}}/partners/ecommerce/loyalty/talonone/) to create and export promotion codes.

{% alert important %}
The maximum file size is 100&nbsp;MB and the maximum list size is 20MM of unused codes. If you find the wrong file was uploaded, upload a new one, and the previous one will be replaced.
{% endalert %}

1. After the upload is complete, select **Save List** to save all the details and codes you just entered.

![CSV file named "springsale" that was successfully uploaded.]({% image_buster /assets/img/promocodes/promocode7.png %})

{:start="2"}
2. After selecting save, a new row will appear in the **Import History**. 
3. To refresh the table to see if your import has finished, select <span style="font-size: 14px;margin-bottom: .5rem;height: 16px;width: 16px;" class="fas fa-sync" ></span> **Sync** at the top of the table.

![Promotion codes in the process of being uploaded.]({% image_buster /assets/img/promocodes/promocode8.png %})

{% alert note %}
Larger files will take a few minutes to import. While you wait, you can leave the page and work on something while the import is in progress. When the import finishes, the status will change to **Complete** in the table.
{% endalert %}

#### Updating a promotion code list

To update a list, select one of your existing lists. You can change the name, description, list expiration, and threshold alerts. You can also add more codes to the list by uploading new files and selecting **Update List**.

All codes in the list will have the same expiration, regardless of the date of import.

### Step 5: Use promotion codes

To send promotion codes in messages:

1. Select **Copy Snippet** to copy the code snippet you set when creating your promotion code list.

![An option to copy the snippet to paste into your message.]({% image_buster /assets/img/promocodes/promocode9.png %}){: style="max-width:70%"}

{:start="2"}
2. From there, you can paste this code into a message within the dashboard.

![An example message "Treat yourself to something nice this spring with our exclusive offer" followed by the code snippet.]({% image_buster /assets/img/promocodes/promocode10.png %}){: style="max-width:70%"}

Using [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/), you can insert one of the unique promotion codes from the uploaded CSV file into a message. That code will be marked as sent on the Braze backend to ensure no other message sends that same code.

#### Sending promotion codes to users

When a code snippet is used in a campaign or Canvas with multichannel messages, each user always receives a unique code. If a Canvas has multiple different steps that reference a promotion code, a user will always receive a new code for each step that they enter. If you want to assign one promotion code in a Canvas and reference the assigned value in multiple steps, we recommend doing the following:

- Assign the promotion code as a custom attribute as a first step (User Update step)
- Use Liquid in the subsequent steps to refer to the value of that custom attribute (not the promotion code)

If a user is eligible to receive a code through more than one channel, they'll receive the same code for each channel. For example, if a user receives two messages through email and push notifications, they'll receive only one code. The same applies for reporting purposes: one code will be sent, and the user will receive this code through the two channels.

{% alert important %}
If there are no remaining promotion codes available when sending test or live messages from a campaign that pulls in promotion codes, the message will not be sent.
{% endalert %}

#### Sending test messages with promotion codes

Test sends and seed group email sends will use up promotion codes unless requested otherwise. Contact your Braze account manager to update this feature behavior so promotion codes aren't used during test sends and seed group email sends.

## Determining how many codes have been used

You can find the remaining code count in the **Remaining** column of the promotion code list on the **Promotion Codes** page.

![An example of a promotion code with unused codes.]({% image_buster /assets/img/promocodes/promocode11.png %})

This code count can also be found when revisiting a pre-existing promotion code list page. You can also export unused codes as a CSV file. 

![A promotion code named "Black Friday Sale" with 992 remaining codes.]({% image_buster /assets/img/promocodes/promocode12.png %}){: style="max-width:70%"}

### Using promotion codes in in-app message campaigns {#promotion-codes-iam-campaigns}

{% alert important %}
Using promotion codes in in-app message campaigns is currently in early access. Contact your Braze account manager if you're interested in participating in this early access.
{% endalert %}

After creating an [in-app message campaign]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages), you can insert a [promotion code list snippet]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/promotion_codes#creating-a-promotion-code-list) into your in-app message message body. 

Promotion codes in in-app messages will be deducted and used only when a user triggers the display of the in-app message.

## Multichannel and single-channel sends

For multichannel and single-send campaigns and Canvases, all promotion codes referenced in a message’s Liquid are deducted to be used **before** the message is sent to make sure the following occurs:

- The same promotion codes are used across channels in a multichannel message.
- Extra promotion codes are not used if a message fails or aborts.

If a user has two promotion code lists referenced in one message that is split by a Liquid conditional logic tag, all promotion codes will still be deducted, regardless of which conditional flow the user follows.

If a user enters a new Canvas step or re-enters a Canvas, and the promotion code Liquid snippet is applied again for a message to that user, a new promotion code will be used.

### Use case

For the following example, both promotion code lists `vip-deal` and `regular-deal` will be deducted. Here's the Liquid:

{% raw %}
```
{% if user.is_vip %}
  {% promotion('vip-deal') %}
{% else %}
  {% promotion('regular-deal') %}
{% endif %} 
```
{% endraw %}

Braze recommends uploading more promotion codes than what you estimate will be used. If a promotion code list expires or runs out of promotion codes, the subsequent messages will be aborted.

{% alert tip %}
**Here's an analogy for how promotion codes are used up in Braze.** <br><br>Imagine that sending your message is like sending a letter at the post office. You give the letter to a clerk, and they see that your letter should include a coupon. The clerk pulls the first coupon from the stack and adds it to the envelope. The clerk sends the letter, but for some reason, the letter gets lost in the mail (and the coupon is also now lost). <br><br>In this scenario, Braze is the postal clerk, and your promotion code is the coupon. We can't get it back after it's been pulled from the stack of promotion codes, regardless of the webhook result.
{% endalert %}

## Frequently asked questions

### Which messaging channels can I use with promotion codes?

Promotion codes are currently supported for email, mobile push, web push, Content Cards, webhook, SMS, and WhatsApp. Braze Transactional Email campaigns and in-app messages do not currently support promotion codes.

### Will test sends and seed sends use up my promotion codes?

By default, test sends and seed group email sends will use promotion codes per user, per test send. However, you can reach out to your Braze account manager to update this behavior to not use promotion codes during testing.

### How do promotion codes work in a multichannel campaign or Canvas step?

Promotion codes are deducted before the message is sent. If the messaging channels in the campaign or Canvas send, this may cause the promotion code to be used for reasons including Quiet Hours, rate limits, frequency capping, exit criteria, and more. However, if any of the message channels are sent, one promotion code will be used.

### What happens if I have multiple Liquid snippets that reference the same promotion code list in my message?

The same promotion code will be templated for all instances of the Liquid snippet in your message.

### What happens when a promotion code list is expired or empty?

Expired codes are deleted after six months.

If the message should have contained a promotion code from an empty or expired list, the message will be canceled. 

If the message contains Liquid logic that conditionally inserts a promotion code, the message will only be canceled if it should have contained a promotion code. If the message shouldn't have contained a promotion code, the message will send normally.

### How do I save a promotion code to a user's profile so it can be used in subsequent messages?

To reference the same promotion code in subsequent messages, the code must be saved to the user profile as a custom attribute. This can be done through a [User Update step]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/user_update/) that assigns the discount code to a custom attribute, like “Promo Code”, directly before a Message step.

First, select the following for each field in the User Update step:

- **Attribute Name:** Promo Code
- **Action:** Update
- **Key Value:** The promotion code's Liquid code snippet, such as {% raw %}`{% promotion('spring25') %}`{% endraw %}

Second, add the custom attribute (in this example, {% raw %}`{{custom_attribute.${Promo Code}}`{% endraw %}) to a message. The discount code will be templated in.
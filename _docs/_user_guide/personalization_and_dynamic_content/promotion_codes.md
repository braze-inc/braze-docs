---
nav_title: Promotion Codes
article_title: Promotion Codes
page_order: 5
alias: "/promotion_codes/"
description: "This reference article covers how to create promotion code lists and add them to your campaigns and Canvases."

---

# Promotion codes

> Promotion codes—also called promo codes—are a great way to keep users engaged by driving interactions with a heavy emphasis on purchases.<br><br>This page covers how to create promotion code lists and add them to your campaigns and Canvases.

With Braze Liquid functionality, we offer a way to make widespread promotion code usage a snap, allowing messages to now pull from the promotion list you provided, automatically and intuitively. The promotion codes feature offers expiry dates of up to six months and support for up to 20MM individual codes per list.

{% alert important %}
Promotion codes can't be sent in in-app messages.
{% endalert %}

## Creating a promotion code list

### Step 1: Navigate to the Promotion Code section

![][1]{: style="float:right;max-width:30%;margin-left:15px;"}

From the dashboard, go to **Data Settings** > **Promotion Codes**, then select **Create Promotion Code List**.

{% alert note %}
If you are using the [older navigation]({{site.baseurl}}/navigation), you can find **Promotion Codes** under **Integrations**.
{% endalert %}

### Step 2: Naming and creating your promotion code

Name your promotion code list and add an optional description.

![][2]{: style="max-width:90%"}

Next, create a code snippet for the promotion code. This code snippet will be what you will reference in Liquid to display this specific set of promotion codes. Make sure that it is a code snippet that is not already being used in another list.

{% alert important %}
Snippets are case-sensitive. For example, "Birthday_promo" and "birthday_promo" will be recognized as two different snippets.
{% endalert %}

![][3]{: style="max-width:90%"}

{% alert warning %}
You can't change the code snippet after saving!
{% endalert %}

### Step 3: Promotion code options

Each promotion code list has a corresponding expiration date and time that gets set upon creation. The maximum expiration length is six months into the future from the day you're creating or editing your list. Within that time, you can change and update the expiration date repeatedly. This expiration date will apply to all codes added to this list. Upon expiration, the codes will be deleted from the Braze system and any messages calling that list's code snippet will not be sent.

![][4]{: style="max-width:90%"}

You also have the option to set up optional and customized threshold alerts. If set up, these alerts will email the designated recipient either when the list is running low on available promotion codes in this list, or when your promotion code list is close to expiration. The recipient will be notified once a day.

![][5]

### Step 4: Promotion code upload

Braze doesn't manage code creation or redemption, meaning you must generate your promotion codes to a CSV file and upload them to Braze. Make sure the CSV file follows these guidelines:

- Includes a column for promotion codes.
- Has one promotion code per row.

You can use our built-in integration with [Voucherify]({{site.baseurl}}/partners/message_orchestration/channel_extensions/loyalty/voucherify/) or [Talon.One]({{site.baseurl}}/partners/message_orchestration/channel_extensions/loyalty/talonone/) to create and export promotion codes.

{% alert note %}
The maximum file size is 100&nbsp;MB and the maximum list size is 20MM of unused codes. If you find the wrong file was uploaded, upload a new one, and the previous one will be replaced.
{% endalert %}

![][6]

After the upload is complete, select **Save List** to save all the details and codes you just entered.

![][7]

After selecting save, a new row will appear in the **Import History**. To refresh the table to see if your import has finished, select <span style="font-size: 14px;margin-bottom: .5rem;height: 16px;width: 16px;" class="fas fa-sync" ></span> **Sync** at the top of the table.

![][8]

{% alert note %}
Larger files will take a few minutes to import. While you wait, you can leave the page and work on something while the import is in progress. When the import finishes, the status will change to **Complete** in the table.
{% endalert %}

#### Updating a promotion code list

To update a list, select one of your existing lists. You can change the name, description, list expiration, and threshold alerts. You can also add more codes to the list by uploading new files and selecting **Update List**.

All codes in the list will have the same expiration, regardless of the date of import.

### Step 5: Use promotion codes

To send promotion codes in messages, select **Copy Snippet** to copy the code snippet you set when creating your promotion code list.

![][9]{: style="max-width:70%"}

From there, you can paste this code into a message within the dashboard.

![][10]{: style="max-width:70%"}

Using [Liquid][11], you can insert one of the unique promotion codes from the uploaded CSV file into a message. That code will be marked as sent on the Braze backend to ensure no other message sends that same code. 

When a code snippet is used in a multichannel campaign or Canvas step, each user always receives a unique code. For different steps in a Canvas, each user receives several promotion codes.

If a particular user is eligible to receive a code through more than one channel, this user will receive the same code through each channel. For example, if a user receives two messages through two channels, they will receive only one code. The same applies for reporting purposes: one code will be sent, and the user will receive this code through the two channels. For example, for a multichannel Canvas step, only one code would be used by the user.

{% alert important %}
If there are no remaining promotion codes available when sending test or live messages from a campaign that pulls in promotion codes, the message will not be sent.
{% endalert %}

#### Sending test messages with promotion codes

Test sends and seed group email sends will use up promotion codes unless requested otherwise. Contact your Braze account manager to update this feature behavior so promotion codes aren't used during test sends and seed group email sends.

## Determining how many codes have been used

You can find the remaining code count in the **Remaining** column of the promotion code list, located on the **Promotion Codes** page.

![][12]{: style="max-width:90%"}

This code count can also be found when revisiting a pre-existing promotion code list page. 

![][13]{: style="max-width:50%"}

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

Braze recommends to uploading more promotion codes than what you estimate will be used. If a promotion code list expires or runs out of promotion codes, the subsequent messages will be aborted.

{% alert tip %}
**Here's an analogy for how promotion codes are used up in Braze.** <br><br>Imagine that sending your message is like sending a letter at the post office. You give the letter to a clerk, and they see that your letter should include a coupon. The clerk pulls the first coupon from the stack and adds it to the envelope. The clerk sends the letter, but for some reason, the letter gets lost in the mail (and the coupon is also now lost). <br><br>In this scenario, Braze is the postal clerk and your promotion code is the coupon. We can't get it back after it's been pulled from the stack of promotion codes, regardless of the webhook result.
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

If the message should have contained a promotion code from an empty or expired list, the message will be canceled.

If the message contains Liquid logic that conditionally inserts a promotion code, the message will only be canceled if it should have contained a promotion code. If the message shouldn't have contained a promotion code, message will send normally.

### How do I save a promotion code to a user's profile so it can be used in follow up messages?

To reference the same promotion code in subsequent messages, the code must be saved to the user profile as a custom attribute. This can be done by attaching a [Braze-to-Braze webhook]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/braze_to_braze_webhooks/) to the same campaign or Canvas Message step.

[1]:{% image_buster /assets/img/promocodes/promocode1.png %}
[2]:{% image_buster /assets/img/promocodes/promocode2.png %}
[3]:{% image_buster /assets/img/promocodes/promocode3.png %}
[4]:{% image_buster /assets/img/promocodes/promocode4.png %}
[5]:{% image_buster /assets/img/promocodes/promocode5.png %}
[6]:{% image_buster /assets/img/promocodes/promocode6.png %}
[7]:{% image_buster /assets/img/promocodes/promocode7.png %}
[8]:{% image_buster /assets/img/promocodes/promocode8.png %}
[9]:{% image_buster /assets/img/promocodes/promocode9.png %}
[10]:{% image_buster /assets/img/promocodes/promocode10.png %}
[11]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/
[12]: {% image_buster /assets/img/promocodes/promocode11.png %}
[13]: {% image_buster /assets/img/promocodes/promocode12.png %}

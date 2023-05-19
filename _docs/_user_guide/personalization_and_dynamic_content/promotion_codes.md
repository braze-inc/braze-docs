---
nav_title: Promotion Codes
article_title: Promotion Codes
page_order: 5
alias: "/promotion_codes/"
description: "This reference article covers how to create promotion code lists and add them into your campaigns and Canvases."

---

# Promotion codes

> Promotion codes—also called promo codes—are a great way to keep users engaged by driving interactions with a heavy emphasis on purchases.

With Braze's Liquid functionality, we offer a way to make widespread promotion code usage a snap, allowing messages to now pull from the promotion list you provided, automatically and intuitively. The promotion codes feature offers expiry dates of up to six months and support for up to 20MM individual codes per list.

{% alert important %}
Promotion codes can't be sent in in-app messages.
{% endalert %}

## Creating a promotion code list

### Step 1: Navigate to the Promotion Code section

![][1]{: style="float:right;max-width:30%;margin-left:15px;"}

From the dashboard, go to **Promotion Codes**, located under the **Integrations** section, then select **Create Promotion Code List**.

{% alert note %}
If you are using our [updated navigation]({{site.baseurl}}/navigation), you can find **Promotion Codes** under **Data Settings**.
{% endalert %}

### Step 2: Naming and creating your promotion code

Name your promotion code list and add an optional description.

![][2]{: style="max-width:90%"}

Next, create a code snippet for the promotion code. This code snippet will be what you will reference in Liquid to display this specific set of promotion codes. Make sure that it is a code snippet that is not already being used in another list.

{% alert important %}
Snippets are case sensitive. For example, "Birthday_promo" and "birthday_promo" will be recognized as two different snippets.
{% endalert %}

![][3]{: style="max-width:90%"}

{% alert warning %}
You can't change the code snippet after saving!
{% endalert %}

### Step 3: Promotion code options

Each promotion code list has a corresponding expiration date and time that get set upon creation. The max expiration length is six months into the future from the day you're creating or editing your list. Within that time, you can change and update the expiration date repeatedly. This expiration date will apply to all codes added to this list. Upon expiration, the codes will be deleted from the Braze system and any messages calling that list's code snippet will not be sent.

![][4]{: style="max-width:90%"}

You also have the option to set up optional and customizable threshold alerts. If set up, these alerts will email the designated recipient either when the list is running low on available promotion codes in this list, or when your promotion code list is close to expiration. The recipient will be notified once a day.

![][5]

### Step 4: Promotion code upload

Braze does not manage code creation or redemption. As a result, you'll have to generate your promo codes to a CSV file and upload them to Braze. You can use our built-in integration with [Voucherify]({{site.baseurl}}/partners/channel_extensions/loyalty/voucherify/) or [Talon.One]({{site.baseurl}}/partners/channel_extensions/loyalty/talonone/) to create and export promo codes. Make sure that there is only one code on each row.

{% alert note %}
Max file size is 100&nbsp;MB and the max list size is 20MM of unused codes. If you find the wrong file was uploaded, simply upload a new file and the previous file will be replaced.
{% endalert %}

![][6]

After the upload is complete, click **Save List** to save all the details and codes you just entered.

![][7]

Upon clicking save, you will see that a new row appears in the **Import History**. To refresh the table to see if your import has finished, click <span style="font-size: 14px;margin-bottom: .5rem;height: 16px;width: 16px;" class="fas fa-sync" ></span> **Sync** at the top of the table.

![][8]

{% alert note %}
Larger files will take a few minutes to import. While you wait, you are free to leave the page and work on something while the import is in progress. When the import is finished, you will see the status change to **Complete** in the table.
{% endalert %}

#### Updating a promotion code list

To update a list, simply open up one of your existing lists. You can change the Name, Description, List Expiration, Threshold Alerts, and add more codes to the list by uploading new files and clicking **Update List**.
All codes in the list will have the same expiration, regardless of the date of import.

### Step 5: Use promotion codes

To send promotion codes in messages, click **Copy Snippet** to copy the code snippet you set when creating your promotion code list.

![][9]{: style="max-width:70%"}

From there, you can paste this code into a message within the dashboard.

![][10]{: style="max-width:70%"}

Using [Liquid][11], you can insert one of the unique promotion codes from the uploaded CSV file into a message. That code will be marked as sent on the Braze backend to ensure no other message sends that same code. When a code snippet is used in a multichannel campaign or Canvas component, each user always receives a unique code. If a particular user is eligible to receive a code through more than one channel, this user will receive the same code through each channel. 

If the user receives two messages through two channels, only one code will be shown and used in both messages. The same applies for reporting purposes: one code will be sent, and the user will receive this code through the two channels. For example, for a multichannel Canvas step, only one code would be used by the user.

{% alert important %}
If there are no remaining promotion codes available when sending test or live messages from a campaign that pulls in promo codes, the message will not send.
{% endalert %}

## Determining how many codes have been used

You can find the remaining code count in the **Remaining** column of the promotion code list, located on the **Promotion Codes** page.

![][12]{: style="max-width:90%"}

This code count can also be found when revisited a pre-existing promotion code list page. 

![][13]{: style="max-width:50%"}

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

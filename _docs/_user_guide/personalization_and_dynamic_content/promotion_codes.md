---
nav_title: Promotion Codes
page_order: 5
alias: "/promotion_codes/"
description: "This reference article covers how to create promotion code lists and add them into your Campaigns and Camvases."
Tool:
  - Dashboard
  - Campaigns
  - Canvas
---

# Promotion Codes

> Promotion codes—also called promo codes—are a great way to keep users engaged by driving interactions with a heavy emphasis on purchases. <br><br>With Braze's Liquid functionality, we offer a way to make widespread promotion code usage a snap, allowing messages to now pull from the promotion list you provided, automatically and intuitively. The promotion codes feature offers expiry dates of up to six months and support for up to 20MM individual codes per list.

{% alert important %}

__Please note that promotion codes cannot be sent in In-App Messages.__
<br><br>

{% endalert %}

## Creating a Promotion Code List

![Promo Codes 1][1]{: style="float:right;max-width:30%;margin-left:15px;"}
### Step 1: Navigate to the Promotion Code Section

Click on the “Promotion Codes” link on the Dashboard’s side navigation located under the Integrations section, then select “Create Promotion Code List”.

### Step 2: Naming and Creating your Promotion Code
![Promo Codes 2][2]{: style="float:right;max-width:40%;margin-left:15px;margin-bottom:15px;"}
Name your promotion code list and add an optional description.

Next, create a code snippet for the promotion code. This code snippet will be what you will reference in Liquid to display this specific set of promotion codes. __Make sure that it is a code snippet that is not already being used in another list.__<br><br> Snippets are __case sensitive__, so for example, “Birthday_promo” and “birthday_promo” will be recognized as two different snippets. <br>Note that you __will not__ be able to change the code snippet after saving.

![Promo Codes 3][3]{: style="max-width:90%"}

### Step 3: Promotion Code Options

Each promotion code list has a corresponding expiration date and time that get set upon creation. The max expiration length is six months into the future from the day you’re creating or editing your list. Within that time, you can change and update the expiration date repeatedly. This expiration date will apply to all codes added to this list. Upon expiration, the codes will be deleted from the Braze system and any messages calling that list’s code snippet will not be sent.

![Promo Codes 4][4]{: style="max-width:90%"}

You also have the option to set up optional and customizable threshold alerts. If set up, these alerts will email the designated recipient either when the list is running low on available promotion codes in this list, or when your promotion code list is close to expiration. The recipient will be notified once a day.

![Promo Codes 5][5]

### Step 4: Promotion Code Upload

Braze does not manage code creation or redemption, so as a result, you’ll have to generate your promo codes to a CSV file and upload them to Braze. You can use our built-in integration with [Voucherify]({{site.baseurl}}/partners/channel_extensions/loyalty/voucherify/) or [Talon.One]({{site.baseurl}}/partners/channel_extensions/loyalty/talonone/) to create and export promo codes. Make sure that there is only one code on each row.

Note that the max file size is 100MB and the max list size is 20MM of unused codes. If you find the wrong file was uploaded, simply upload a new file and the previous file will be replaced.

![Promo Codes 6][6]

After the upload is complete, click on Save List to save all the details and codes you just entered.

![Promo Codes 7][7]

Upon clicking save, you will see that a new row appears in the Import History below. To refresh the table to see if your import has finished, click on the double arrow icon at the top of the table. 

Please note that larger files will take a few minutes to import. While you wait, you are free to leave the page and work on something while the import is in progress. When the import is finished, you will see Complete status in the table.

![Promo Codes 8][8]

#### Updating a Promotion Code List

To update a list, simply open up one of your existing lists. You can change the Name, Description, List Expiration, Threshold Alerts, and add more codes to the list by uploading new files and clicking on Update List to save and import.
All codes in the list will have the same expiration, regardless of the date of import.

### Step 5: Use Promotion Codes

To send promotion codes in messages, copy the code snippet you set when creating your promotion code list by clicking the Copy Snippet button.

![Promo Codes 9][9]{: style="max-width:70%"}

From there, this code can be pasted into a message within the Dashboard.

![Promo Codes 10][10]{: style="max-width:70%"}

Now, using [Liquid][11], you can insert one of the unique promotion codes from the uploaded CSV file, into a message. That code will be marked as sent on the Braze backend to ensure no other message sends that same code. When a code snippet is used a multi-channel campaign or Canvas step, the same unique code will be sent to each user across the channels.

{% alert important %}

__Please note that promotion codes cannot be sent in In-App Messages.__
<br><br>

{% endalert %}

## How Many Codes have been Used?

Remaining code count can be found in the "Remaining" column of the promotion code list located on the promotion code page.

![Promo Codes 12][12]{: style="max-width:90%"}

This code count can also be found when revisited a pre-existing promotion code list page. 

![Promo Codes 13][13]{: style="max-width:50%"}

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







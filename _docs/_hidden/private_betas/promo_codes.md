---
nav_title: Promotion Codes
title: Promotion Code
description: ""
permalink: "/promotion_codes/"
hidden: true
---
{% alert note %}
This Promotion Codes feature is currently in Beta. Please reach out to your Braze account manager for more information.
{% endalert %}

# Promotion Codes

> Promotional codes or Promo Codes are a great way to keep users engaged and interested in your application and service. Incentives like these drive user interaction with a heavy emphasis on purchases. <br><br>With Braze's Liquid Logic functionality, we offer a simple and easy way to make widespread promotion code usage a snap, allowing messages to now pull from the promotion list you provided, automatically and intuitively. <br><br>The promotion codes feature offers expiry dates of up to six months and support for up to 10MM individual codes per list.

## Creating a Promotion Code Lists

### Step 1: Navigate to the Promotion Code Section

Click on the “Promotion Codes” link on the Dashboard’s side navigation located under the Integrations section, then select “Create Promotion Code List”.

![Promo Codes 1][1]{:height="100px"}

### Step 2: Naming and Creating your Promotion Code

Name your promotion code list and add an optional description.

![Promo Codes 2][2]{:height="250px"}

Next, create a code snippet for the promotion code. This code snippet will be what you will reference in your Liquid Logic to display this specific set of promotion codes. __Make sure that it is a code snippet that is not already being used in another list.__<br> Snippets are __case sensitive__, so for example, “Birthday_promo” and “birthday_promo” will be recognized as two different snippets. <br>Note that you __will not__ be able to change the code snippet after saving.

![Promo Codes 3][3]{:height="200px"}

### Step 3: Promotion Code Options

Because promotion codes generally don't last forever, we need to set up an expiration date and time for these codes. The max expiration length is six months into the future from the day you’re creating or editing your list. You can change the expiration date repeatedly. This expiration date will apply to all codes added to this list.

![Promo Codes 4][4]{:height="200px"}

You also have the option to set up optional and customizable threshold alerts. If set up, these alerts will email the designated recipient either when the list is running low on available promotion codes in this list, or when your promotion code list is close to expiration.

![Promo Codes 5][5]

### Step 3: Promotion Code Upload

You will now need to supply the promotion codes. To do this, you can upload a CSV file of promotion codes with one code on each row. <br>Note that max file size is 10MB and the total number of codes allowed in one list is 10MM codes. 
If you find the wrong file was uploaded, simply upload a new file and the previous file will be replaced.

![Promo Codes 6][6]

After the upload is complete, click on Save List to save all the details and codes you just entered.

![Promo Codes 7][7]

Upon clicking save, you will see that a new row appears in the Import History below. To refresh the table to see if your import has finished, click on the double arrow icon at the top of the table. 

Please note that larger files will take a few minutes to import. While you wait, you are free to leave the page and work on something while the import is in progress. When the import is finished, you will see Complete status in the table.

![Promo Codes 8][8]

## Updating a Promotion Code List

To update a list, simply open up one of your existing lists. You can change the Name, Description, List Expiration, Threshold Alerts, and add more codes to the list by uploading new files and clicking on Update List to save and import.
All codes in the list will have the same expiration, regardless of the date of import.

## Use Promotion Codes

To send promotion codes in messages, copy the code snippet you set when creating your promotion code list by clicking the Copy Snippet button.

![Promo Codes 9][9]{:height="200px"}

From there, this code can be pasted into a message within the Dashboard.

![Promo Codes 10][10]{:height="200px"}

Now, using Liquid Logic, you can insert one of the unique promotion codes from the uploaded CSV file, into a message. That code will be marked as used on the Braze backend to ensure no other message receives that same code.

__Please note that promotion codes cannot be sent in In-App Messages.__

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








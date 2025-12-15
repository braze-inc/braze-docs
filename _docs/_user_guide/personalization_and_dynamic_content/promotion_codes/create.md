---
nav_title: Creating codes
article_title: Creating promotion codes
page_order: 0.1
description: "Learn how to create promotion codes in your campaigns and Canvases."
---

# Creating promotion codes

> Learn how to create promotion codes in your campaigns and Canvases.

## Creating a promotion code list {#create}

### Step 1: Create a new list

In the dashboard, go to **Data Settings** > **Promotion Codes**, then select **Create Promotion Code List**.

![Button to create a promotion code.]({% image_buster /assets/img/promocodes/promocode1.png %})

### Step 2: Enter the details

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

## Updating a promotion code list

To update a list, select one of your existing lists. You can change the name, description, list expiration, and threshold alerts. You can also add more codes to the list by uploading new files and selecting **Update List**. All codes in the list will have the same expiration, regardless of the date of import.

{% alert important %}
Promotion codes can't be deleted.
{% endalert %}

### Modifying an incorrect promotion code list 

If you've uploaded a CSV file with the incorrect promotion codes and selected **Save list**, you can resolve this by either method:

- Deprecate the entire list: Stop using the current promotion code list in any campaigns, Canvases, or templates. Then, upload the CSV file with the correct codes and use them in your messaging.
- Use the incorrect codes: Create a campaign that sends promotion codes from the incorrect promotion code list to a placeholder until all of the incorrect codes are used. Then, upload the correct promotion codes to the same list.

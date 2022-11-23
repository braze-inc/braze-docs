---
nav_title: Dynamic Yield
article_title: Dynamic Yield
description: "This article outlines the partnership between Braze and Ada, an AI-powered platform that automates and personalizes customer interactions. This integration allows you to augment user profiles with data collected from your automated Ada conversations."
alias: /partners/dynamic_yield/
page_type: partner
search_tag: Partner

---

# Dynamic Yield

> Dynamic Yield, a Mastercard company, helps businesses across industries deliver digital customer experiences that are personalized, optimized, and synchronized. With Dynamic Yield's [Experience OS](http://www.dynamicyield.com/experience-os), marketers, product managers, developers, and digital teams can algorithmically match content, products, and offers to each customer for the acceleration of revenue and customer loyalty.

The Braze and Dynamic yield partnership allows you to leverage Dynamic Yield's recommendation and segmentation engine, dynamic content with affinity-based targeting, and AI-driven algorithms to create triggered emails.

Dynamic Yield's Experience Email lets you transform static emails into fully personalized experiences using a visual editor with drag-and-drop capabilities. Create your own, or select from various preconfigured responsive templates that enable you to easily build your email message without any coding while retaining full control over the merchandising and personalization algorithms. 

## Prerequisites

| Requirement | Description |
| ----------- | ----------- |
| Dynamic Yield account | A [Dynamic Yield](https://adm.dynamicyield.com/users/sign_in#/r/dashboard) account is required to take advantage of this partnership. |
{: .reset-td-br-1 .reset-td-br-2}

## Integration

### Step 1: Create an Experience Block

To create an Experience Block in Dynamic Yield, navigate to **Email > Experience Emails > Create New**.

![][2]

Next, select **Create Experience Block** to design a Dynamic Content or Recommendations block to embed inside a Braze email template.

![][8]

The following image shows an email from scratch in the builder. You can select the device view in the upper left corner of the builder. 

![][6]

1. Enter a campaign name, note, and labels for the campaign in the heading area.
2. Insert an Experience Block. These blocks include:
	- [Recommendations](https://support.dynamicyield.com/hc/en-us/articles/4404013832465-Experience-Email#h_01FQBRAK3MEJCQ9MVGDZ32RA2T): A widget offering users fully-personalized recommendations.
	- [Dynamic Content](https://support.dynamicyield.com/hc/en-us/articles/4404013832465-Experience-Email#h_01FQBRAZ76DCD881CTC1MCJ2AM): Target different promotions and messages to different audiences.
3. Update settings.
  - Use the URL parameters to track clicks within your analytics software (optional). Add parameters to the default displays as needed.
  - Select an attribute window, either seven days (default) or one day.
4. Save and exit. You can return to edit all elements of your email at any time before the code is generated. After the code is generated, you can edit anything that [does not affect the code](https://support.dynamicyield.com/hc/en-us/articles/4404013832465-Experience-Email#h_01FAZPXB6MH094J1MWS5N86FXH).


### Configure a Recommendations block

The recommendations block enables you to set algorithms and filtering to source users' personalized content that propagates when the email is opened. 

1. Drag a Recommendations block from the editing pane into the body of your email.<br>![][4]
2. Select your desired algorithm (popularity, user affinity, similarity, and more).
  - Depending on the algorithm selected, additional options are displayed. 
  - If your recommendation is based on popularity, you can shuffle the results to avoid serving the same recommendation from different emails the viewer opens.
  - Other algorithms, such as similarity, rely on context to serve recommendations requiring that you select items to include. These items can be added in the builder or [add a merge tag to the embed code](https://support.dynamicyield.com/hc/en-us/articles/4404013832465-Experience-Email#advanced) to make it dynamic, for example, to add similar items into shipping confirmation emails. 
3. You can exclude products the user has already purchased to avoid recommending these products.<br>![][5]
4. You can add a [custom filer rule](https://support.dynamicyield.com/hc/en-us/articles/4404013832465-Experience-Email#h_01FAZP4ZWZX1JJ2SH61MB3HVXD) to pin specific products to slots, or include and exclude products by product properties. For example, do not show products that code less than $5 or only products from the shorts category.
5. Configure the recommendation block design: select an item template, set the number of items to display, and in how many rows. 


### Configure a Dynamic Content block
Use Dynamic Content to target different promotions and messages to different users. Targeting can be based on either affinity or audience. Dynamic Yield determines which personalized experience to serve when the email is opened. 

1. Drag a Dynamic Content block from the editing pane into the body of your email. 
2. Select a template for the first variation. You can now define design and content variables.
3. Save the variation.
4. In the Dynamic Content pane, set the audience.
5. Add another variation to target another specific audience or all users. Repeat as needed.
6. Set the priorities for your variations using the up and down arrows. 
7. Priorities determine which variation is served when a user is eligible for more than one experience.
8. Define general block settings (padding, alt-text). testing the app

## Step 2: Integrate your Email with Braze

This integration allows you to add personalized [recommendation widgets](https://support.dynamicyield.com/hc/en-us/articles/360022547394) and [dynamic content](https://support.dynamicyield.com/hc/en-us/articles/360022547994) powered by Dynamic Yield into your Braze email campaigns. Embedding these campaigns into Braze campaigns is done with a simple embed code that you paste into the Braze email editor.

1. Click the ESP Integration icon on the Experience Email list page.
2. Enter the relevant token from Braze that inserts the user's CUID and Email ID.<br>![][3]
  
When satisfied with your email, the next step is to generate the code to embed in Braze.
1. In Experience Emails, click **Generate Code**. <br>![][7]
2. Next, click **Copy to Clipboard**.<br>![][1]
3. Paste the code into your Braze email campaign, and then continue to design, test, and publish your email campaign.


[1]: {% image_buster /assets/img/dynamic_yield/dynamic_yield.png %}
[2]: {% image_buster /assets/img/dynamic_yield/dynamic_yield1.png %}
[3]: {% image_buster /assets/img/dynamic_yield/dynamic_yield2.png %}
[4]: {% image_buster /assets/img/dynamic_yield/dynamic_yield3.png %}
[5]: {% image_buster /assets/img/dynamic_yield/dynamic_yield4.png %}
[6]: {% image_buster /assets/img/dynamic_yield/dynamic_yield5.png %}
[7]: {% image_buster /assets/img/dynamic_yield/dynamic_yield6.png %}
[8]: {% image_buster /assets/img/dynamic_yield/dynamic_yield7.png %}
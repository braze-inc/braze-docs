---
nav_title: Dynamic Yield
article_title: Dynamic Yield
description: "This reference article outlines the partnership between Braze and Dynamic Yield. This partnership allows you to leverage Dynamic Yield's recommendation and segmentation engine to create Experience Blocks that can be embedded into Braze messages."
alias: /partners/dynamic_yield/
page_type: partner
search_tag: Partner

---

# Dynamic Yield

> [Dynamic Yield](https://www.dynamicyield.com/), a Mastercard company, helps businesses across industries deliver digital customer experiences that are personalized, optimized, and synchronized. With Dynamic Yield's [Experience OS](http://www.dynamicyield.com/experience-os), marketers, product managers, developers, and digital teams can algorithmically match content, products, and offers to each customer for the acceleration of revenue and customer loyalty.

_This integration is maintained by Dynamic Yield._

## About the integration

The Braze and Dynamic Yield partnership allows you to leverage Dynamic Yield's recommendation and segmentation engine to create Experience Blocks that can be embedded into Braze messages. Experience blocks can be made of:
- **Recommendations blocks**: Set algorithms and filtering to source users' personalized content that propagates when the email is opened. 
- **Dynamic Content Blocks**: Target different promotions and messages to different users. Targeting can be based on either affinity or audience. Dynamic Yield determines which personalized experience to serve when the email is opened. 

## Prerequisites

| Requirement | Description |
| ----------- | ----------- |
| Dynamic Yield account | A [Dynamic Yield](https://adm.dynamicyield.com/users/sign_in#/r/dashboard) account is required to take advantage of this partnership. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integration

### Step 1: Create an Experience Block

To create an Experience Block in Dynamic Yield, navigate to **Email > Experience Emails > Create New**.

Next, select **Create Experience Block** to design a Dynamic Content or Recommendations block to embed inside a Braze email template.<br>![]({% image_buster /assets/img/dynamic_yield/dynamic_yield7.png %})

### Step 2: Draft your messaging

The following image shows an email from scratch in the builder.<br>![]({% image_buster /assets/img/dynamic_yield/dynamic_yield5.png %})

1. Enter a campaign name, note, and labels for the campaign in the heading area.<br><br>
2. Insert an Experience Block. These blocks include:
  - [Recommendations](#configure-a-recommendations-block): A widget offering users fully-personalized recommendations.
  - [Dynamic Content](#configure-a-dynamic-content-block): Target different promotions and messages to different audiences.<br><br>
3. Update settings:
  - Use the URL parameters to track clicks within your analytics software (optional). Add parameters to the default displays as needed.
  - Select an attribute window, either seven days (default) or one day.<br><br>
4. Save and exit. You can return to edit all elements of your email at any time before the code is generated. After the code is generated, you can edit anything that [does not affect the code](https://support.dynamicyield.com/hc/en-us/articles/4404013832465-Experience-Email#h_01FAZPXB6MH094J1MWS5N86FXH).

### Configure a Recommendations block

The recommendations block enables you to set algorithms and filtering to source users' personalized content that propagates when the email is opened. 

1. Drag a Recommendations block from the editing pane into the body of your email.<br><br>
2. Select your desired algorithm (popularity, user affinity, similarity, and more). Depending on the algorithm selected, additional options are displayed: 
  - If your recommendation is based on popularity, you can shuffle the results to avoid serving the same recommendation from different emails the viewer opens.
  - Other algorithms, such as similarity, rely on context to serve recommendations requiring that you select items to include. These items can be added in the builder or [add a merge tag to the embed code](https://support.dynamicyield.com/hc/en-us/articles/4404013832465-Experience-Email#advanced) to make it dynamic, for example, to add similar items into shipping confirmation emails. <br><br>
3. You can exclude products the user has already purchased to avoid recommending these products.<br><br>
4. You can add a [custom filer rule](https://support.dynamicyield.com/hc/en-us/articles/4404013832465-Experience-Email#h_01FAZP4ZWZX1JJ2SH61MB3HVXD) to pin specific products to slots, or include and exclude products by product properties. For example, do not show products that code less than $5 or only products from the shorts category.<br><br>
5. Lastly, configure the recommendation block design. To do this, select an item template, set the number of items to display, and in how many rows. 

### Configure a Dynamic Content Block
Use Dynamic Content to target different promotions and messages to different users. Targeting can be based on either affinity or audience. Dynamic Yield determines which personalized experience to serve when the email is opened. 

1. Drag a Dynamic Content Block from the editing pane into the body of your email.<br><br> 
2. Select a template for the first variation. You can now define design and content variables. Save the variation when complete. <br>![]({% image_buster /assets/img/dynamic_yield/dynamic_yield3.png %})<br><br> 
3. Set the audience in the Dynamic Content pane.<br>![]({% image_buster /assets/img/dynamic_yield/dynamic_yield4.png %})<br><br> 
4. Add another variation to target another specific audience or all users. Repeat as needed.<br><br> 
5. Set the priorities for your variations using the up and down arrows. <br><br> 
6. Priorities determine which variation is served when a user is eligible for more than one experience.

### Step 3: Integrate your Email with Braze

This integration allows you to add personalized recommendation widgets and dynamic content powered by Dynamic Yield into your Braze email campaigns. Embedding these campaigns into Braze campaigns is done with a simple embed code that you paste into the Braze email editor.

1. Click the ESP Integration icon on the Experience Email list page.<br><br> 
2. Enter the relevant token from Braze that inserts the user's CUID and Email ID.<br>![]({% image_buster /assets/img/dynamic_yield/dynamic_yield2_new.png %})
  
When satisfied with your email, the next step is to generate the code to embed in Braze.
1. In **Experience Emails**, click **Generate Code**.<br><br> 
2. Next, click **Copy to Clipboard**.<br>![]({% image_buster /assets/img/dynamic_yield/dynamic_yield.png %})<br><br> 
3. Paste the code into your Braze email campaign, and then continue to design, test, and publish your email campaign.



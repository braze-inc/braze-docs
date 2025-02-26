---
nav_title: Embedded Signup
article_title: WhatsApp Embedded Signup
page_order: 0
description: "This reference article provides a step-by-step walkthrough for the WhatsApp embedded signup workflow in Braze."
page_type: reference
channel:
  - WhatsApp
---

# WhatsApp embedded signup

> This reference article provides a step-by-step walkthrough for the WhatsApp embedded signup workflow in Braze.

The WhatsApp embedded signup workflow is accessed when you first [integrate WhatsApp]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/) into your Braze workspace, and when you [add a WhatsApp Business account]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/multiple_subscription_groups/) to an existing WhatsApp integration.

## Accessing the workflow

Go to **Partner Integrations** > **Technology Partners**, then search for and select **WhatsApp**. Your next selection depends on your use case:

- If you're integrating WhatsApp into your workspace, select **Begin Integration**. <br><br>![][10]{: style="max-width:80%;"}<br><br>
- If you're adding a WhatsApp Business account to an existing WhatsApp integration, select **Add WhatsApp Business Account**. <br><br>![][11]{: style="max-width:80%;"}

The workflow from here is the same for both use cases.

## WhatsApp embedded signup workflow

1. On the Meta (Facebook) login window, select **Login as** or **Continue**. <br><br>![Meta login window.][1]{: style="max-width:60%;"}<br><br>
2. Read the permissions that you'll share with Braze, then select **Get Started**. <br><br>![List of permissions that you'll share with Braze for the integration.][2]{: style="max-width:50%;"}<br><br>
3. In the **Business portfolio** dropdown, select your business portfolio and then select **Next**. This connects to your WhatsApp Business account, so if you don't see your expected business portfolio, check your permissions.<br><br>![A window with fields to enter your business information, including your business portfolio name.][3]{: style="max-width:50%;"}<br><br>
4. Select the following for the dropdown fields, then select **Next**.
- **Choose a WhatsApp Business account**: Create a WhatsApp business account
- **Create or select a WhatsApp Business profile**: Create a new WhatsApp business profile <br><br>![Fields to specify if you're choosing or creating a WhatsApp Business account and profile.][4]{: style="max-width:50%;"}<br><br>
5. Provide the following, then select **Next**.
- WhatsApp business account name
- WhatsApp business display name
- Category <br><br>![Fields to provide details for the new WhatsApp Business account.][5]{: style="max-width:50%;"}<br><br>
6. Enter your phone number and choose either **Text message** or **Phone call**. This number must follow all the requirements of any WhatsApp phone number, including not being registered to any other WhatsApp accounts. <br><br>![Fields to add a phone number.][6]{: style="max-width:50%;"}<br><br>
7. Enter your two-factor authentication code, then select **Next**. <br><br>![An input field for a two-factor authentication code.][7]{: style="max-width:50%;"}<br><br>
8. Review the permissions that your WhatsApp Business account will receive, then select **Continue**. <br><br>![List of permissions requested by the WhatsApp Business account.][8]{: style="max-width:50%;"}<br><br>
9. You're done! <br><br>![Window saying you're ready to start messaging people.][9]{: style="max-width:50%;"}

[1]: {% image_buster /assets/img/whatsapp/login_screen.png %}
[2]: {% image_buster /assets/img/whatsapp/get_started.png %}
[3]: {% image_buster /assets/img/whatsapp/business_info.png %}
[4]: {% image_buster /assets/img/whatsapp/create_select_waba.png %}
[5]: {% image_buster /assets/img/whatsapp/waba_details.png %}
[6]: {% image_buster /assets/img/whatsapp/add_phone_number.png %}
[7]: {% image_buster /assets/img/whatsapp/two_factor.png %}
[8]: {% image_buster /assets/img/whatsapp/permissions.png %}
[9]: {% image_buster /assets/img/whatsapp/finish.png %}
[10]: {% image_buster /assets/img/whatsapp/whatsapp1.png %} 
[11]: {% image_buster /assets/img/whatsapp/multiple_wabas.png %} 
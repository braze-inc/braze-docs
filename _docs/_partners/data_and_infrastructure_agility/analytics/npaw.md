---
nav_title: NPAW
page_order: 0
alias: /partners/npaw/

description: "This article outlines the partnership between Braze and NPAW, an intelligent data analytics platform that provides actionable insights to leading online media professionals."
page_type: partner
hidden: true
---

# NPAW

> [NPAW](https://nicepeopleatwork.com/), also knows as _Nice People at Work_, is an intelligent data analytics platform that provides actionable insights to leading online media professionals. With NPAW's YOUBORA tool suite, Braze customers can now leverage a predictive and robust AI to greater understand customer behavior and drive engagement accross platforms.

# Prerequisites

| Requirement   |Origin| Description |
| --------------|------|-------------|
| YOUBORA API Key |[YOUBORA Settings](https://youbora.nicepeopleatwork.com/users/login)|An API Key generated on user sign up and can be located under **Settings** |
| ID |[Braze Settings](https://dashboard.braze.com/sign_in) | YOUBORA gives you the options of whether to link the software to Braze via a ***Braze ID***, an ***external User ID***, or a ***User ID*** |
| Endpoint |[Braze Settings](https://dashboard.braze.com/sign_in)| A fully customizable URL endpoint configurable through your **Braze Dashboard** |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

# Analytics Integration

## Accessing the Integrations page

After logging into your YOUBORA tool suite account, navigate to the Intgrations page by selecting **Integrations** option from the drop-down account menu found at the top right corner of the screen as shown below.

![NPAW DROP DOWN]({% image_buster /assets/img/npaw_dropdown.png %})

## Configuring Your Integration

Once you have accessed the Integration page, scroll down until you
see the **Braze** integration option. After clicking on this, it will expand and offer a number of required parameters to fill out as shown below:

![NPAW INTEGRATION]({% image_buster /assets/img/npaw_integration.png %})

Fill in the details with the appropriate information gathered from the prequisites section, where:
* **Connector Name** is an **alphanumeric** string that will be used to reffer to this integration in the future. This value can be set to anything you like as long as it contains **only** letters and numbers.
* **User ID** is the ID previously chosen to link your YOUBORA software with your Braze account. For example, if you choose to perform the link via your **Braze ID**, select **Braze ID** from the dropdown to assign the value to the proper field.
* **API Key** is your YOUBORA tools suite API Key found previously within the **API** section under **Settings** .
* **Endpoint** is the customizable URL endpoint previously setup within your **Braze Dashboard**.

Once all the fields have been filled out, simply click on the **Connect** button to establish a connection and save the changes made.

## Using Your NPAW Integration

Once you have finished configuring your integration with Braze, navivate to the **Users** product and select the **Sample Manager** within the **Sections Manager**.

![NPAW SECTIONS MANAGER]({% image_buster /assets/img/npaw_sections_manager.png %})

After creating a sample within the **Sample Manger**, you will now be able to click on the triple dot icon on the right-hand side to send all users within your sample to Braze.

![NPAW SAMPLE MANAGER]({% image_buster /assets/img/npaw_sample_manager.png %})

Now, once you send your users to Braze, you can take action and focus campaigns on user segments to re-engage inactive users, contact your most loyal users or any action on any user segment!

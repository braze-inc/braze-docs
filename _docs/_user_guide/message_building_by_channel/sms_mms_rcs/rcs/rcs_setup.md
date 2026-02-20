---
nav_title: "RCS setup"
article_title: RCS Setup
page_order: 1
alias: /rcs_setup/
description: "This reference article covers the requirements needed to get RCS up and running."
page_type: reference
channel:
  - RCS
---

# Set up RCS

> This article covers the requirements needed to get your RCS channel up and running.

Setting up RCS is as straightforward as setting up SMS. Keep reading to learn how you can begin sending rich and interactive messages.

## Step 1: Meet the eligibility criteria

To be eligible for sending RCS with Braze, your business must meet three criteria upfront:

1. Your current Braze contract must include Message Credits. 
2. You must send your RCS messages to one of the following Braze-supported countries:
- United States
- United Kingdom
- Germany
- Mexico
- Sweden
- Spain
- Singapore
- Brazil
- France
- Italy
- Colombia
3. You must procure a $0 RCS SKU(s) in your contract.

## Step 2: Register an RCS-verified sender

Before you can send RCS messages, you must register an RCS-verified sender. This is the representation of your brand that users will see on their mobile devices, which includes your brand’s name, logo, a verification badge, and an optional tagline. The RCS-verified sender reinforces customer trust and confirms your messages come from an authenticated source. 

![An example RCS-verified sender in an RCS message called "Cat Failz Cafe".]({% image_buster /assets/img/rcs/rcs_sender.png %}){: style="max-width:60%;"}

After you have added the RCS SKU(s) to your order form, Braze will be notified and will contact you with RCS sender registration information. The format of these will depend on the countries you wish to send RCS messages to. 

When you've submitted your completed forms to Braze, we will complete the registration process on your behalf. 

### Step 2.1: Set up SMS fallbacks for RCS subscription groups

Because current carrier coverage varies by country, and user hardware and software support vary by individual, SMS fallback is a key component of having a successful RCS program today. We recommend setting up SMS fallback. If a carrier doesn’t support RCS or a user’s device is unable to receive RCS messages, SMS fallback will send your message regardless, so that you never miss an important moment with your users.

We highly recommend reviewing your current SMS opt-in experience, subscription groups, and audience segmentation before deploying your first RCS campaign. If needed, your customer success manager is always available to provide guidance and help you navigate the setup process.

### Timeline for carrier approval

The timeline for carrier approval varies by country and can also vary within a country. Keep in mind that the RCS market is still in its infancy, so carrier and aggregator processes are rapidly evolving. In the United States, Braze estimates that carrier approval turnaround time for an RCS-verified sender typically falls within the 4—6 week range, with a test sender typically approved within one week.

When your RCS-verified sender is approved, our operations team will update your subscription groups as needed to confirm they have the RCS sender included in them. 

## Step 3: Set up subscription groups

RCS is typically used in two ways: 
- To upgrade existing SMS traffic 
- To enable new use cases that are only possible with the richer functionality provided by RCS

Depending on your integration, Braze can add RCS-verified senders to your existing SMS subscription groups or set up new subscription groups for you. In either case, your Braze team will guide you through a seamless and compliant SMS traffic upgrade. For more information, refer to [SMS and RCS subscription groups]({{site.baseurl}}/sms_rcs_subscription_groups/).

For new use cases that are not possible with SMS, consider setting up dedicated RCS subscription groups to align with your program goals.
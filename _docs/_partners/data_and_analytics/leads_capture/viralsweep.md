---
nav_title: ViralSweep
article_title: ViralSweep
alias: /partners/viralsweep/
description: "This reference article outlines the partnership between Braze and ViralSweep, a software service that allows brands to build, run, and manage digital marketing promotions like sweepstakes, contests, instant win, waitlists, referral promotions, and more."
page_type: partner
search_tag: Partner

---

# ViralSweep

> [ViralSweep](https://viralsweep.com) is a software service that allows brands to build, run, and manage digital marketing promotions like sweepstakes, contests, instant win, waitlists, referral promotions, and more. 

_This integration is maintained by ViralSweep._

## About the integration

The Braze and ViralSweep integration allows you to hold sweepstakes and contests on the ViralSweep platform (growing your email and SMS lists) and then send sweepstakes or contest entry information into Braze to use in campaigns or Canvases. 

## Prerequisites

| Requirement | Description |
| ----------- | ----------- |
| ViralSweep account | A ViralSweep account utilizing the business plan is required to take advantage of this partnership. |
| Braze REST API key | A Braze REST API key with all user data and email permissions. <br><br> This can be created in the Braze dashboard from **Settings** > **API Keys**. |
|Braze REST endpoint | Your REST endpoint URL. Your endpoint will depend on the Braze URL for [your instance]({{site.baseurl}}/api/basics/#endpoints). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integration

### Step 1 : Connect to Braze within ViralSweep

In ViralSweep, navigate to **Integrations > Email & SMS > Add Service** and select **Braze**. 

![]({% image_buster /assets/img/viralsweep/connect.gif %})

### Step 2 : Add Braze Credentials

In the integrations configuration window, provide your Braze REST API key and REST endpoint. Make sure the endpoint you provide does not include `https://`, for example, `dashboard-03.braze.com`. 

![ViralSweep service integration page prompting the user for the Braze API key and Braze dashboard URL.]({% image_buster /assets/img/viralsweep/connect2.png %}){: style="max-width:40%;"}

Click **Connect**.

### Step 3 : Add Braze Credentials
You're connected! The promotion is now connected to Braze, and all entries collected by ViralSweep will be sent into Braze automatically.

## Frequently asked questions

### What fields does ViralSweep pass to Braze?
- First name
- Last name
- Email address
- Address
- Address 2
- City
- State
- Zip
- Country
- Birthdate
- Phone
- Promotion ID
- Referral link
- Tracking campaign name

### Does ViralSweep update subscribers?
Yes. If you run a promotion and ViralSweep passes someone to Braze, then you run another promotion in the future and the same person enters, that person's information will automatically be updated in Braze (if any new information is provided). Mainly, the referral URL will be updated with the newest URL for each promotion they enter, and the promotion ID field will contain the ID of all the promotions they have entered.

## Troubleshooting

If you have connected to Braze and data is not being added to your account, it may be because:

- **Email already exists in Braze**<br>
The email address entered into the promotion may already be in your Braze account, so it will not be added again; it will only be updated if new information is provided for that contact.<br><br>
- **Email already entered into ViralSweep**<br>
The email address entered into the promotion has already been entered previously, so it is not passed to Braze again. This can happen if you set up your Braze integration after you have already entered the promotion.



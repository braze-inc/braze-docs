---
nav_title: "Idle Campaigns"
permalink: "/idle_campaigns/"
hidden: true
layout: dev_guide
---

# Idle campaigns

> This reference article explains the idle status for campaigns and provides answers to frequently asked questions.

When a campaign is no longer sending messages, Braze will assign an idle status to these campaigns to help sort and manage your list of campaigns. Using this new filter, you can filter through your campaigns and see which campaigns will be automatically stopped and the associated stop date. On an ongoing basis, the idle campaigns that meet the following criteria will be stopped:
 
- Action-based and scheduled campaigns with end dates seven days after the end date
- Scheduled one-time campaigns seven days after the send date 
- Action-based and scheduled campaigns without end dates that have not sent messages in one year
- API-triggered campaigns that have not sent messages in one year

Campaigns will be stopped at the later of the default stop date and one day after their last occurring conversion deadline. Sends that are a result of a winning or personalized variant are treated as scheduled sends, and will be stopped seven days after the winning or personalized variant is sent. All campaigns will be stopped at 4am UTC every day for all Braze users.

For recurring campaigns without end dates, if a message is sent or the campaign is updated, the one-year countdown for stopping the campaign will be reset. When campaigns are stopped, Braze will notify customers in their dashboard and via email. If you have an idle campaign that you want to remain active, resume the campaign, then update the end date for the campaign. For idle campaigns without end dates, you can make any edit to keep the campaign active.

## Frequently asked questions

#### What campaigns does this apply to?

This will apply to campaigns that already meet the previously listed criteria, and campaigns that will meet the criteria moving forward.

#### How do I know if a campaign is idle?

Idle campaigns will be displayed in campaign list under category **Idle**. The date on which the campaign will be stopped is listed next to each campaign. Campaigns with end dates and one-time sends will be idle for seven days prior to auto-stopping. Campaigns that have not sent a message in 11 months will be idle for one month prior to auto-stopping. 

#### What happens if an idle campaign is updated?

If a campaign that hasn't sent a message is updated, the 12-month countdown will reset. 

#### What happens to campaigns that haven't sent a message in one year, but have an end date in the future?

We will stop these campaign seven days after the end date.

#### How can I keep an idle campaign active?

To make a campaign no longer Idle and ensure it remains active, update the campaign so it does not meet the above criteria for being Idle. Reference this table for steps to make idle campaigns active, depending on your use case.

| Reason for idle campaign status | Steps to make campaign active |
| --- | --- |
| Action-based campaigns with end dates seven days after the end date | Extend the end date |
| Scheduled campaigns with end dates seven days after the end date | Extend the end date |
| Scheduled one-time send campaigns with end dates seven days after the end date | Schedule a future send |
| Action-based campaigns (without end dates) that have not sent messages in one year | Send one message or make any edit to the campaign | 
| Scheduled campaigns (without end dates) that have not sent messages in one year | Send one message or make any edit to the campaign | 
| API-triggered campaigns that have not sent messages in one year | Send one message or make any edit to the campaign |
| Campaigns will be stopped at the later of the idle status criteria and 1 day after their last-occurring conversion deadline | Update the criteria above or extend the conversion deadline, depdending on which occurs later |
| Sends as the result of a winning or personalized variant are treated as scheduled sends and disabled seven days after the winning or personalized variant is sent | Update when the variant will send to a later date |
{: .reset-td-br-1 .reset-td-br-2}

#### What happens if I want to continue running a campaign that hasn't sent a message or been edited in over 12 months?

To continue running an idle campaign, resume the campaign. In this case, the 12-month countdown will reset. 

#### What happens if I want to continue running a campaign that's past its end date?

To resume a campaign that's past its end date, update the campaign's end date to the desired date. 

#### Who will receive email notifications about stopped campaigns?

By default, all users with administrator permissions are opted into email notifications about auto-stopping campaigns. The creator of the campaign will always be notified when it is stopped. Users can manage email notification preferences by going to **Company Settings > Notification Preferences**, then adding or removing recipients from the notification **Campaign Automatically Stopped**.

#### Is there any action required?

No additional action is required. Please reach out to your Braze customer success manager if you have any questions.

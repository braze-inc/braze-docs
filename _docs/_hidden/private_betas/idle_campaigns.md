---
nav_title: "Idle Category for Campaigns"
permalink: "/idle_campaigns/"
hidden: true
---

# Idle status for campaigns

> This reference article explains the idle status for campaigns and provides answers to frequently asked questions.

Braze will automatically stop Campaigns that are no longer sending messages. These changes will keep your digest free of clutter. On an ongoing basis, we will stop:

- Action-based campaigns with end dates 7 days after the end date
- Scheduled campaigns with end dates 7 days after the end date 
- Scheduled one-time sends 7 days after the entry date 
- Action-based campaigns (without end dates) that have not sent messages in 1 year
- Scheduled campaigns (without end dates) that have not sent messages in 1 year
- API-triggered campaigns that have not sent messages in 1 year
- Campaigns will be stopped at the later of the above and 1 day after their last-occurring conversion deadline
- Sends as the result of a winning/personalized variant are treated as scheduled sends and disabled 7 days after the winning/personalized variant is sent
- They will be stopped at 4am UTC every day for all companies

For recurring Campaigns without end dates, if a message is sent or the Campaign is updated, the one-year countdown to stopping the Campaign will reset. When Campaigns are stopped, we will notify customers in their dashboard and via email (details below). For those campaigns that meet the criteria but you wish to remain active, resume the Campaign by selecting its corresponding gear icon in the Campaigns digest, and selecting “resume.” You will need to update the end date for Campaigns that have them. Otherwise, no additional action is required.

We have created a new “Idle” category in the Campaigns digest where users can view which Campaigns will be automatically stopped, including the stop date.

## Frequently asked questions

#### What campaigns does this apply to?

This will apply to campaigns that already meet the above criteria, and campaigns that will meet the criteria moving forward.

#### How do I know if a campaign is idle?

Idle campaigns will be displayed in the Campaign digest under the "Idle" category pictured below. The date on which the campaign will be stopped will be listed below each campaign. Campaigns with end dates and one-time sends will be idle for 7 days prior to auto-stopping. Campaigns that have not sent a message in 11 months will be idle for 1 month prior to auto-stopping. 

#### What happens if an idle campaign is updated?

If a campaign that hasn't sent a message is updated, the 12-month countdown will reset. 

#### What happens if I want to continue running a campaign that hasn't sent a message or been edited in over 12 months?

Select the campaign's corresponding gear icon, and choose **Resume**. In this case, the 12-month countdown will reset. 

#### What happens if I want to continue running a campaign that's past its end date?

To resume a campaign that's past its end date, update the campaign's end date to the desired date. 

#### What happens to campaigns that haven't sent a message in 1 year, but have an end date in the future?

We will stop these campaign seven days after its end date.

#### How can I keep an idle campaign active?



#### Who will receive email notifications about stopped campaigns?

By default, all users with administrator permissions are opted into email notifications about auto-stopping campaigns. The creator of the campaign will always be notified when it is stopped. Users can manage email notification preferences by going to **Company Settings > Notification Preferences**, then adding or removing recipients from the notification **Campaign Automatically Stopped**.

#### Is there any action required?

No additional action is required. Please reach out to your Braze customer success manager if you have any questions.
---
nav_title: "Idle Campaigns and Canvases"
permalink: "/idle_campaigns_canvases/"
hidden: true
---

# Idle campaigns and Canvases

> This reference article explains the idle status for campaigns and Canvases and provides answers to frequently asked questions.

{% alert note %}
In 2024, Canvases will be marked **Idle** and stopped, similar to campaigns. When Canvases are idle or stopped, they will follow the logic in this document.
{% endalert %}

Campaigns and Canvases are assigned an idle status when they have not sent messages or entered users in some time. These campaigns and Canvases will be automatically stopped at their associated stop dates. You can filter for idle campaigns and Canvases to help you sort and manage your list of campaigns and Canvases.

## Idle campaigns

On an ongoing basis, the idle campaigns that meet the following criteria will be stopped:
 
- Action-based and scheduled campaigns with end dates seven days after the send date
- Scheduled one-time campaigns seven days after the send date 
- Action-based and scheduled campaigns without end dates that have not sent messages in one year
- API-triggered campaigns that have not sent messages in one year

Campaigns will be stopped at the later of the default stop date and one day after their last occurring conversion deadline. Sends that are a result of a Winning or Personalized Variant are treated as scheduled sends, and will be stopped seven days after the winning or Personalized Variant is sent. All campaigns will be stopped at 4am UTC every day for all Braze users.

For recurring campaigns without end dates, if a message is sent or the campaign is updated, the one-year countdown for stopping the campaign will be reset. When campaigns are stopped, Braze will notify customers in their dashboard and via email. If you have an idle campaign that you want to remain active, resume the campaign, then update the end date for the campaign. For idle campaigns without end dates, you can make any edit to keep the campaign active.

Content Cards will not be stopped until their expiration deadline, and will also abide by the aforementioned criteria as well as the conversion deadline rule.

## Idle Canvases

On an ongoing basis, idle Canvases will be stopped.

- Idle Canvases with end dates will be stopped seven days after the end date, plus the maximum duration of the Canvas
    - Action-based and scheduled Canvases with end dates
    - Scheduled one-time Canvases
- Idle Canvases without end dates will be stopped seven days after the end date, plus the maximum duration of the Canvas 
    - Action-based Canvases without end dates
    - API-triggered Canvases without end dates
    - Scheduled Canvases without end dates

The maximum duration of the Canvas is a duration that includes Content Card and in-app message expiries.

## Frequently asked questions

#### What campaigns or Canvases does this apply to?

This will apply to campaigns and Canvases that already meet the previously listed criteria, and campaigns and Canvases that will meet the criteria moving forward.

#### How do I know if a campaign or Canvas is idle?

Idle campaigns and Canvases will be displayed in the campaign and Canvas list pages under the category Idle. The date on which the campaign or Canvas will be stopped is listed as a column in the list.

#### What happens if an idle campaign or Canvas is updated?

If a campaign that hasn’t sent a message or a Canvas that hasn’t entered users is updated, the countdown will reset.

#### What happens to campaigns that haven’t sent a message in one year (or Canvases that haven’t entered users in one year), but have an end date in the future?

We will stop these campaign and Canvases seven days after the end date.

#### How can I keep an idle campaign active?

To keep a campaign active, update the campaign so it does not meet the above criteria for having an idle status. Reference this table for steps to make idle campaigns active, depending on your use case.

##### Idle campaigns

| Reason for idle status | Steps to make campaign active |
| --- | --- |
| Action-based campaigns with end dates seven days after the send date | Extend the end date |
| Scheduled campaigns with end dates seven days after the send date | Extend the end date |
| Scheduled one-time send campaigns with end dates seven days after the last send date | Schedule a future send |
| Action-based campaigns (without end dates) that have not sent messages in one year | Send one message or make any edit to the campaign | 
| Scheduled campaigns (without end dates) that have not sent messages in one year | Send one message or make any edit to the campaign | 
| API-triggered campaigns that have not sent messages in one year | Send one message or make any edit to the campaign |
| Campaigns will be stopped at the later of the idle status criteria and 1 day after their last-occurring conversion deadline | Update the criteria above or extend the conversion deadline, depending on which occurs later |
| Sends as the result of a Winning or Personalized Variant are treated as scheduled sends and disabled seven days after the Winning or Personalized Variant is sent | Update when the variant will send to a later date |
{: .reset-td-br-1 .reset-td-br-2}

##### Idle Canvases

| Reason for idle status | Steps to make Canvas active |
| --- | --- |
| Action-based Canvases with end dates seven days and maximum duration after the end date | Extend the end date |
| Scheduled Canvases with end dates seven days and maximum duration after the end date | Extend the end date |
| Scheduled one-time send Canvases with end dates seven days and maximum duration after the end date | Schedule a future send |
| Action-based Canvases without end dates that have not entered users in one year and maximum duration | Enter one user or make any edit to the Canvas | 
| Scheduled Canvases (without end dates) that have not entered users in one year and maximum duration | Enter one user or make any edit to the Canvas | 
| API-triggered Canvases that have not sent entered users in one year | Enter one user or make any edit to the Canvas |
{: .reset-td-br-1 .reset-td-br-2}

#### How can I keep an idle Canvas active?

To keep a Canvas active, update the Canvas so it does not meet the above criteria for having an idle status. Reference this table for steps to make idle campaigns active, depending on your use case.

#### Who will receive email notifications about stopped campaigns?

By default, all users with administrator permissions are opted into email notifications about auto-stopping campaigns. The creator of the campaign will always be notified when it is stopped. Users can manage email notification preferences by going to **Company Settings > Notification Preferences**, then adding or removing recipients from the notification **Campaign Automatically Stopped**.

#### How does stopping Content Cards work?

Content Cards in campaigns will not be stopped until their expiration deadline and the appropriate buffer period. They will be stopped at the later of the buffer period (corresponding to whether the campaign is a one-time send, has an end date, or does not have an end date) and the expiration deadline. 

For example, if a Content Card expires on April 1, is a one-time send, and has a conversion deadline of 10 days, it will be stopped on April 12 (10 days after the conversion deadline, plus one day). If a Content Card expires on April 1, is API-triggered, and has not sent messages since March 15, it will expire on March 15 of next year.

Canvases are only stopped after the Content Cards are stopped, meaning their maximum duration has passed.
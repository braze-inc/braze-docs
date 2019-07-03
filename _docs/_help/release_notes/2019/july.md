---
nav_title: July
page_order: 6
---

# July 2019

## User Profile Image Removal

We are removing the user profile pictures displayed on the Braze dashboard.

## Connected Content in Content Cards

You can now use [Connected Content]({{ site.baseurl }}) strings and functionality in Content Cards.

Connected Content calls to external servers will happen when a Card is actually sent, __not__ when the Card is viewed by the User. Similar to Email, dynamic content will be calculated and determined at sending time, rather than when a Card is actually viewed.

## Null 'Reply-to' Address

Customers can set a 'null' value for the reply-to address.  When used, internet providers (gmail/yahoo/etc...) will reply back to the from address.  This is useful for customers who personalize the 'from-address' field as 'dan@braze.com'.  Now they will have the ability to reply back immediately to dan.

Dashboard users can set to exclude the 'reply-to' field in email settings
API support to pass in a 'null' value - `NO_REPLY_TO`

UPDATE IN DOCS?

## Campaign Retention Report

User retention is one of the most important metrics to any marketer. Keeping engaged users coming back for more indicates that business is healthy.

Retention Reports asses user engagement over a specified period of time. The report measures how many visitors completed an initial action and returned to complete an important subsequent action over time. The basic question answered is, "For how long do my customers who did X keep coming back to do Y?"

In this first iteration of Retention Reports, we're measuring how many users received the campaign as the initial action, and then how many of those users subsequently started a session. In future iterations, we aim to allow clients to specify the retention event (i.e. - made a purchase, completed custom event, etc.) so that they can measure the type of engagement and retention that is important to their marketing efforts.

Clients need only to open their campaign analytics and scroll down to see their retention report. As this first iteration is only measuring users who received a campaign and then started a session, there are no variables to adjust. The client can, however, adjust the report to show the percentage of user engagement or the number of users engaged.


## Campaign Comparisons

Clients have given us feedback indicating that they're faced with the problem of looking at multiple campaigns at a time for the purposes of comparing relative performance. The workaround for some was to open their campaigns in multiple tabs (browser or Dashboard) and flip back and forth. For others, it was to have multiple windows open next to each other. And even other still were cutting and pasting numbers into spreadsheets or making use of Engagement Reports. All of them told us we could do better. So we are.

This is the first iteration of Campaign Comparisons, and thus has relatively limited functionality as an MVP, but enough to accomplish the task of looking at high-level campaign performance side by side on the Dashboard. We intend to listen carefully to clients' feedback and hear their needs, and continue to iterate toward the best possible solution here. Note that this is only available for Campaigns at this time.

https://www.braze.com/docs/user_guide/engagement_tools/campaigns/testing_and_more/comparing_campaigns


## Template `dispatch_id` into messages with Liquid

Team

Ingestion & Reporting

Summary

For clients who wish to track the dispatch of a message from within the message (i.e. - in a URL), they can now template in the `dispatch_id`.

How it works

This behaves just like `api_id`, in that since the `api_id` isn't available at campaign creation time, it's templated in as a placeholder and will preview as `dispatch_id_for_unsent_campaign`. The id is generated before the message is sent, and will be included in as send time.

Note that this does not work with IAMs since IAMs don't have `dispatch_id`.


## "Show only Mine" setting persists

Team

Ingestion & Reporting

Summary

We're seeing great usage on "Show only Mine" on the Campaign grid, but clients currently need to check it every time they visit the Campaigns page.

## A/B Testing Updates

Send a one-time A/B test with up to 8 variants (and optional control) to a user-specified percentage of a Campaign's audience, and then send the best variant to the remaining audience at a pre-scheduled time.

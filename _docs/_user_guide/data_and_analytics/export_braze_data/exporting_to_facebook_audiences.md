---
nav_title: Export Segment Data to Facebook Audiences
page_order: 10
---
# Exporting to Facebook Audiences

Braze provides Facebook marketing integration, allowing you to export segments as Facebook marketing audiences and target those users for ad campaigns. Here are instructions on setting up this feature.

In order to export custom audiences from the dashboard, your Facebook App must be configured to allow Braze to make requests to Facebook through the [Facebook Marketing API][29] on behalf of the members of your team. Common use cases for exporting custom audiences include:

- Retargeting Campaigns
- Seed audiences for lookalike targeting

## Before You Begin...

In order to configure your Facebook App’s settings, ensure the following:

- Your organization has connected your app or apps within the [Facebook App Dashboard][30]
- Your organization’s administrator has granted you either Developer or Admin access through the Facebook App Dashboard
- You have set up [Facebook Login][31]
- You have admin access to the Facebook Ad Account you’d like to export audiences to
  - You will need to have full admin access and will not be able to test this functionality as a [Test User][32].

## Configuring Facebook App Settings

Due to Facebook’s increased security policies, you will need to whitelist OAuth Redirect URIs from Braze in order to send custom audiences.

- From the Facebook App Dashboard, select the Facebook App that you’d like to export audiences to
- From the left-hand side of the Facebook App Dashboard, select “Facebook Login” and then “Settings”
- Within “Settings” you should be able to see Client OAuth Settings.

![FB Settings][33]

- Append “/auth/facebook/callback” to the end of your dashboard url and then add it to the “Valid OAuth redirect URIs” field.
 - Example: [https://dashboard-01.braze.com/auth/facebook/callback][41]
- Save your changes in the bottom right-hand corner.

Before you proceed to the Braze dashboard, you’ll need to have your Facebook App ID and App Secret on hand.

- From the Facebook App Dashboard, select “Settings” then “Basic.”

![FB App ID][34]

## Configuring Integration {#configuring-braze-3rd-party-integration}

Once your Facebook app has been correctly configured, you’ll need to add your credentials to the appropriate App Group in Braze.

- Within the Braze dashboard, head to the “Technology Partners” section, and click on the [Facebook][35] tab. Make sure you’ve selected the correct App Group.
- Enter your Facebook App ID and App Secret in the “Facebook Marketing App ID” and “Facebook Marketing App Secret” fields.

![Braze FB][36]

  - The “Facebook App ID” field is optional. If users authenticate with Facebook in your app and you are providing Facebook data to the Braze SDK, you will have the option to export those users to Facebook using their Facebook User ID. If you’d like to do this, save the Facebook app ID that you use to authenticate your users in the “Facebook App ID” field.
- Save your changes.

## Exporting Your Users

The Facebook Audience Export link will be in the settings menu of each segment in an app group that has Facebook credentials.

- While this link will be present for all members of your app group, only users with permissions in your Facebook App will be able to successfully export a segment.

![Facebook Export 1][37]

- When you click on this link for the first time, a modal will appear to connect your Facebook credentials. During this process, you must accept [Facebook's Custom Audience Terms of Service][38].
- Once you have connected your Facebook credentials, a modal will appear to let you select which data type you'd like to export.
  - There are 4 possible user data types we can use for the export: email, device IDFA, Facebook UID, and phone number. If you haven’t entered a Facebook App ID in your Technology Partner Integration settings, you won’t be able to select Facebook UID.
  - If you choose more than 1 data type, Braze will create a separate custom audience for each.
- Click on export. As with CSV exports, you will receive an email when the segment has finished exporting.
- You can view the custom audience on the [Facebook Ads Manager][39].

## Facebook Audience Export FAQ

Can I see the exact users that were successfully added to a Custom Audience?

- Facebook does **not** allow this for user privacy reasons. Learn more [here][43].

Why can't I see the Custom Audience size?

- Due to recent user privacy implications, Facebook announced that they will [stop showing audience reach estimates using Custom Audience targeting][42].

Why can’t I select Google Advertising IDs or Android IDs data types?

- Due to Google Play’s Terms of Service, we do not collect and store an Android identifier in a way that allows you to link the ID to PII. For more see [here][44].

### Lookalike Audiences

Once you've successfully exported a segment as a Facebook Audience, you can create additional groups using Facebook's [Lookalike Audiences][17]. This feature looks at demographics, interests, and other attributes of your chosen audience and creates a new audience of people with similar attributes.



[17]: https://www.facebook.com/business/a/online-sales/lookalike-audiences
[29]: https://developers.facebook.com/docs/marketing-api/overview#configure-app
[30]: https://developers.facebook.com/apps/
[31]: https://developers.facebook.com/docs/facebook-login/
[32]: https://developers.facebook.com/docs/apps/test-users/
[33]: {% image_buster /assets/img_archive/fb_oauth.png %}
[34]: {% image_buster /assets/img_archive/fb_app_id.png %}
[35]: https://dashboard-01.braze.com/app_settings/integration/facebook_credentials/
[36]: {% image_buster /assets/img_archive/fbk_3.png %}
[37]: {% image_buster /assets/img_archive/fbk_4.png %}
[38]: https://www.facebook.com/ads/manage/customaudiences/tos.php
[39]: https://www.facebook.com/ads/manager/audiences/manage/
[40]: {{ site.baseurl }}/user_guide/data_and_analytics/exporting_dashboard_data/#exporting-to-csv
[41]: https://dashboard-01.braze.com/auth/facebook/callback
[42]: https://marketingland.com/exclusive-facebook-will-no-longer-show-audience-reach-estimates-for-custom-audiences-after-vulnerability-detected-236923
[43]: https://www.facebook.com/business/help/112061095610075
[44]: https://developer.android.com/training/articles/user-data-ids.html

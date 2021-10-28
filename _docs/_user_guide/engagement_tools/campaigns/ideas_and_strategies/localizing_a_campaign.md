---
nav_title: Localizing a Campaign
article_title: Localizing a Campaign
page_order: 3
page_type: reference
description: "This reference article goes over how user locale is retrieved and accessed by the Braze platform."
tool:
  - Campaigns

---
# Localizing a campaign

> This reference article briefly goes over the information Braze collects from SDK integration and how it is used to classify locale and customize a user's experience. 

Braze automatically collects relevant data to help you localize campaigns. Our customers send localized content on a daily basis to their audience to keep content relevant and accessible.

## Technical details

Braze automatically collects locale information from user devices after the SDK has been integrated. The locale contains a language and region identifier.

For example, a user who has set their device to English (US) will have a language `EN`. The users' country is collected from their device IP address. These filters will be available in Braze's segmentation tool under Country and Language.

![Filter Select Screenshot][7]

More technical details on how locale is retrieved can be accessed by platform:

- [iOS][1]
- [Android][2]
- [Windows Store][3]
- [Windows Phone][4]

## Internationalize campaigns

You can take advantage of this language identifier and our personalization capabilities to internationalize campaigns. For more information on internationalization, see [Campaigns in Multiple Languages][12]

Braze automatically collects the most recent location of users' devices (if location permission is granted to your app). You can use this information to run a localized campaign that is targeted at users within a specific geographic area. For more information, see [Location Targeting][13].

[1]: https://developer.apple.com/library/ios/documentation/MacOSX/Conceptual/BPInternational/LanguageandLocaleIDs/LanguageandLocaleIDs.html
[2]: http://developer.android.com/reference/java/util/Locale.html
[3]: http://msdn.microsoft.com/en-us/library/windows/apps/dd373814.aspx
[4]: http://msdn.microsoft.com/en-us/library/windowsphone/develop/dd373814(v=vs.85).aspx
[7]: {% image_buster /assets/img_archive/language-filter-select.png %}
[12]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/campaigns_in_multiple_languages/#campaigns-in-multiple-languages
[13]: {{site.baseurl}}/user_guide/engagement_tools/segments/location_targeting/#location-targeting

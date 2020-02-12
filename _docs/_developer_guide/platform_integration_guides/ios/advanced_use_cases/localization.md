---
nav_title: Localization
platform: iOS
page_order: 2

---
# Localization

In addition to English, Braze supports 29 languages in our built-in SDK messages. These pertain to the default messages displayed in applications integrated with Braze, such as places in the app when there are connectivity issues ("Cannot establish network connection. Please try again later.") See below for a full list of messages (strings). If the phone language is set to one of the supported languages, any of the Braze default strings triggered within an integrated application will automatically appear in that language.

If you are looking for a complete list of supported languages you may attribute to your users in their profiles, please see our [User Language List][1].

## Languages Supported
1. Arabic
2. Burmese
3. Chinese - Simplified
4. Chinese - Traditional
5. Danish
6. Dutch
7. Estonian
8. Finnish
9. French
10. German
11. Hindi
12. Indonesian
13. Italian
14. Japanese
15. Khmer
16. Korean
17. Lao
18. Malay
19. Norwegian
20. Polish
21. Portuguese - Brazil
22. Portuguese - Portugal
23. Russian
24. Spanish - Latin America
25. Spanish - Spain
26. Swedish
27. Tagalog
28. Thai
29. Vietnamese

## List of Localized Strings

- Connection Error
- We have no updates. Please check again later.
- Cannot establish network connection. Please try again later.
- Done
- OK
- Accept
- Decline
- Confirm
- Cancel
- Yes
- No
- More
- Next
- Go To App

## Technical Details

For your convenience our CocoaPod integrates the `.strings` files for the aforementioned languages. Note that each open-sourced UI component has its own `.strings` file. If you do not wish to use one or more of these languages, you can feel free to delete these files from your project.

Optionally, you can also override any of the following Key / String pairs within your app's `Localizable.strings` file much like a CSS override.

## Localization String File Example

```objc
/*News Feed Default Labels*/
"Appboy.feed.done-button.title" = "Done";
"Appboy.feed.no-card.text" = "We have no updates.\nPlease check again later.";
"Appboy.feed.no-connection.title" = "Connection Error";
"Appboy.feed.no-connection.message" = "Cannot establish network connection.\nPlease try again later.";
/* Content Cards Context Labels */
"Appboy.content-cards.done-button.title" = "Done";
"Appboy.content-cards.no-card.text" = "We have no updates.\nPlease check again later.";
"Appboy.content-cards.no-connection.title" = "Connection Error";
"Appboy.content-cards.no-connection.message" = "Cannot establish network connection.\nPlease try again later.";
/*Web View Default Button Labels*/
"Appboy.slideup.webview.done-button.title" = "Done";
/* General Braze Alarm Messages */
"Appboy.alert.cancel-button.title" = "OK";
/* Default Push Action Category Button Title */
"Appboy.push.action.accept" = "Accept";
"Appboy.push.action.decline" = "Decline";
"Appboy.push.action.confirm" = "Confirm";
"Appboy.push.action.cancel" = "Cancel";
"Appboy.push.action.yes" = "Yes";
"Appboy.push.action.no" = "No";
"Appboy.push.action.more" = "More";
"Appboy.push.action.next" = "Next";
"Appboy.push.action.gotoapp" = "Go To App";
```

For more information see the [Apple Localization Developer Docs][3] as well as the [LOC standard language list][4].

[1]: {{ site.baseurl }}/user_guide/data_and_analytics/user_data_collection/language_codes/
[3]: https://developer.apple.com/library/ios/documentation/CoreFoundation/Reference/CFLocaleRef/
[4]: http://www.loc.gov/standards/iso639-2/php/English_list.php

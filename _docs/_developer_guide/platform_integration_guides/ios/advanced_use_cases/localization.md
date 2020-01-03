---
nav_title: Localization
platform: iOS
page_order: 2

---
# Localization

In addition to English, Braze supports 29 languages in our built-in SDK messages. These pertain to the default messages displayed in applications integrated with Braze, such as places in the app when there are connectivity issues ("Cannot establish network connection. Please try again later.") See below for a full list of messages (strings). If the phone language is set to one of the supported languages, any of the Braze default strings triggered within an integrated application will automatically appear in that language.

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

- Free
- Reporting an Issue?
- Message
- Email
- An email address is required.
- Cancel
- Please enter a feedback message.
- Empty Feedback Message
- Feedback
- Send
- Invalid Email Address
- Please enter a valid email address and try again.
- We have no updates. Please check again later.
- Connection Error
- Cannot establish network connection. Please try again later.
- Cannot establish network connection.
- Please try again later.
- Provide contact info from:
- or
- Done
- Enable Facebook Connection
- To re-enable Facebook, go to Settings > Facebook.
- Enable Twitter Connection
- To re-enable Twitter, go to Settings > Twitter.
- OK
- Hh: mm (hour:minute format)
- $%.2f (price format)

## Technical Details

For your convenience our CocoaPod integrates the `LocalizedAppboyUIString.strings` files for the aforementioned languages. If you do not wish to use one or more of these languages, you can feel free to delete these files from your project.

Optionally, you can also override any of the following Key / String pairs within your app's `Localizable.strings` file much like a CSS override.

## Localization String File Example

```objc
/*General Braze Alarm Messages*/
"Appboy.alert.connect-facebook.title" = "Enable Facebook Connection";
"Appboy.alert.connect-facebook.message" = "To re-enable Facebook, go to Settings -> Privacy -> Facebook.";
"Appboy.alert.connect-twitter.title" = "Enable Twitter Connection";
"Appboy.alert.connect-twitter.message" = "To re-enable Twitter, go to Settings -> Privacy -> Twitter.";
"Appboy.alert.cancel-button.title" = "OK";
/*Feedback No Connection Messages*/
"Appboy.feedback.no-connection.title" = "Unable to Establish\n Network Connection";
"Appboy.feedback.no-connection.message" = "Please try again later.";
/* Feedback Alert Invalid Email Messages */
"Appboy.feedback.alert.invalid-email.title" = "Invalid Email Address";
"Appboy.feedback.alert.invalid-email.message" = "Please enter a valid email address and try again.";
/*Feedback Alert Empty Feedback Labels*/
"Appboy.feedback.alert.empty-feedback.title" = "Empty Feedback Message";
"Appboy.feedback.alert.empty-feedback.message" = "Please enter a feedback message.";
/*Feedback Modal Context Labels*/
"Appboy.feedback.modal-context.title" = "Feedback";
"Appboy.feedback.cancel-button.title" = "Cancel";
"Appboy.feedback.send-button.title" = "Send";
"Appboy.feedback.label.message" = "Message";
"Appboy.feedback.label.required" = "Required";
"Appboy.feedback.label.report-issue" = "Reporting an Issue?";
"Appboy.feedback.label.provide-contact-info" = "Provide contact info from:";
"Appboy.feedback.label.contact-info-required" = "Required";
"Appboy.feedback.label.contack-info-or" = "or";
"Appboy.feedback.email-text-field-place-hold" = "Email (Required)";
/*News Feed Default Labels*/
"Appboy.feed.done-button.title" = "Done";
"Appboy.feed.no-card.text" = "We have no updates.\nPlease check again later.";
"Appboy.feed.no-connection.title" = "Connection Error";
"Appboy.feed.no-connection.message" = "Cannot establish network connection.\nPlease try again later.";
/*Web View Default Button Labels*/
"Appboy.slideup.webview.done-button.title" = "Done";
```

For more information see the [Apple Localization Developer Docs][3] as well as the [LOC standard language list][4].

[3]: https://developer.apple.com/library/ios/documentation/CoreFoundation/Reference/CFLocaleRef/
[4]: http://www.loc.gov/standards/iso639-2/php/English_list.php

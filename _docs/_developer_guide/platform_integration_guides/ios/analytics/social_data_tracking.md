---
nav_title: Social Data Tracking
platform: iOS
page_order: 5
search_rank: 5
---
## Social Data Tracking

### Collecting Social Account Data

The Braze iOS SDK no longer automatically collects Facebook user data starting with version 2.10, and does not collect Twitter user data automatically with version 2.13. If you want to integrate Facebook user data in Braze user profiles, you need to fetch the user's data and pass it to Braze.

You can get a user's Facebook and Twitter data from the iOS system. You can also refer to the sample code for accessing Facebook accounts in [class FacebookViewController][11], and Twitter account in [class TwitterViewController][12] in our Stopwatch sample application. If you were previously relying on the deprecated `promptUserForAccessToSocialNetwork:` method, see `promptUserToConnectFacebookAccountOnDeviceAndFetchAccountData` and `promptUserToConnectTwitterAccountOnDeviceAndFetchAccountData` for sample code on manually prompting your users for access to their social account data.

Another way to get a user's Facebook data is from Facebook's iOS SDK. For more information about integrating the Facebook SDK, follow the steps in [Facebook SDK documentation][2].

### Passing Facebook Data To Braze

Initialize `ABKFacebookUser` objects with the Facebook data you have collected and pass it to Braze:

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
ABKFacebookUser *facebookUser = [[ABKFacebookUser alloc] initWithFacebookUserDictionary:self.facebookUserProfile numberOfFriends:self.numberOfFacebookFriends likes:self.facebookLikes];
  [Appboy sharedInstance].user.facebookUser = facebookUser;
```

{% endtab %}
{% tab swift %}

```swift
var facebookUser : ABKFacebookUser = ABKFacebookUser(facebookUserDictionary: facebookUserDictionary, numberOfFriends: numberOfFriends, likes: likes);
Appboy.sharedInstance().user.facebookUser = facebookUser;
```

{% endtab %}
{% endtabs %}

>  In ABKFacebookUser's init method `initWithFacebookUserDictionary:numberOfFriends:likes:`, all the parameters should be dictionaries and arrays returned directly from Facebook:

| Parameter | Definition |
| --------- | ---------- |
|`facebookUserProfile`| The dictionary returned from the endpoint "/me".|
| `numberOfFriends`| The length of the friends array returned from the endpoint "/me/friends".|
| `likes` | The array of user's Facebook likes from the endpoint "/me/likes". |

>  For additional information regarding the Facebook Graph API, please refer to [the Facebook Graph API Developer Documentation][10].

Additionally, you can tailor what Facebook data you're sending to Braze, in case you don't want to include the entire basic profile. For example:

```objc
ABKFacebookUser *facebookUser = [[ABKFacebookUser alloc] initWithFacebookUserDictionary:facebookUserPublicProfile numberOfFriends:-1 likes:nil];  
```

### Passing Twitter Data To Braze

Initialize `ABKTwitterUser` objects, set up the Twitter data you have collected and pass it to Braze:

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
ABKTwitterUser *twitterUser = [[ABKTwitterUser alloc] init];
twitterUser.userDescription = self.userDescription;
twitterUser.twitterID = self.twitterID;
[Appboy sharedInstance].user.twitterUser = twitterUser;
```

{% endtab %}
{% tab swift %}

```swift
var twitterUser : ABKTwitterUser = ABKTwitterUser();
twitterUser.userDescription = twitterDserDescription;
twitterUser.twitterID = twitterID;
Appboy.sharedInstance().user.twitterUser = twitterUser;
```

{% endtab %}
{% endtabs %}

#### Recording Social Network Shares

As of SDK v.2.16, `logSocialShare:` has been deprecated. If you were relying on this method to log social shares, you can use `logCustomEvent:` instead.

[2]: https://developers.facebook.com/docs/ios "facebook ios sdk docs"
[3]: https://developers.facebook.com/docs/getting-started/facebook-sdk-for-ios/ "create a facebook app"
[4]: https://github.com/Appboy/appboy-ios-sdk/blob/master/Example/Stopwatch/SocialNetworkViewController.m
[7]: {{ site.baseurl }}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/
[8]: {{ site.baseurl }}/developer_guide/platform_integration_guides/ios/advanced_use_cases/manual_sdk_integration/
[9]: {{ site.baseurl }}/developer_guide/platform_integration_guides/ios/analytics/social_data_tracking/#social-data-tracking
[10]: https://developers.facebook.com/docs/graph-api/reference/v2.2/user "facebook graph api docs"
[11]: https://github.com/Appboy/appboy-ios-sdk/blob/master/Samples/Feedback/AppboyFeedbackSample/AppboyFeedbackSample/CustomAppboyFeedbackViewController.m
[12]: https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyUI/ABKContentCardsViewController/ContentCardsViewController/ABKContentCardsViewController.m

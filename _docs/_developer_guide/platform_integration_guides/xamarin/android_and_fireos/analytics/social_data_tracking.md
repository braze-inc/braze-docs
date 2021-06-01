---
nav_title: Social Data Tracking
platform: Xamarin
subplatform: Android and FireOS
page_order: 4

---

# Social Data Tracking

See [the Android integration instructions][1] for in depth discussion of social data best practices and interfaces.

You can see the Xamarin binding accessing these interfaces in the `HomeFragment.cs` of our sample app.  The sample code logs a social share and populates the Braze user with data from the social networks.  The code looks like:

```csharp```
// Record Facebook Data
FacebookUser facebookUser = new FacebookUser("708379", "Test", "User", "test@braze.com", "Test", "Testtown", Gender.Male, new Java.Lang.Integer(100), new String[]{"Cats", "Dogs"}, "06/17/1987");
Appboy.GetInstance(context).CurrentUser.SetFacebookData(facebookUser);

// Record Twitter Data
TwitterUser twitterUser = new TwitterUser(6253282, "Test", "User", "Tester",  new Java.Lang.Integer(100), new Java.Lang.Integer(100), new Java.Lang.Integer(100), "https://si0.twimg.com/profile_images/2685532587/fa47382ad67a0135acc62d4c6b49dbdc_bigger.jpeg");
Appboy.GetInstance(context).CurrentUser.SetTwitterData(twitterUser);
```

[1]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/social_data_tracking/

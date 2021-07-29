---
nav_title: Apteligent
alias: /partners/apteligent/

description: "This article outlines the partnership between Braze and Apteligent, which details crash reporting, allowing you to log critical data into your existing Braze solution."
page_type: partner
platform: ios

---
# Apteligent Integration

> Braze is dedicated to creating partner integrations that provide data-driven approaches to improving your application's user experience. The [Apteligent][1] and Braze partnership combines Braze's multichannel engagement automation with Apteligent's detailed crash reporting, allowing you to log critical data into your existing Braze solution. Together, Apteligent and Braze can help you segment, understand, and engage with your users who have experienced application crashes.

{% alert warning %}
This integration is currently only supported on iOS.
{% endalert %}

## iOS Integration {#apteligent-ios-integration}

To integrate Apteligent with Braze on iOS, do the following:

### Step 1

Register an observer. Ensure that this is done before you initialize Apteligent.

```objc
[[NSNotificationCenter defaultCenter] addObserver:self
                                         selector:@selector(crashDidOccur:)
                                             name:@"CRCrashNotification"
                                           object:nil];
```

### Step 2

The Apteligent SDK will fire a notification when the user loads the application after a crash occurs. The notification will contain the crash name, reason, and date of occurrence.

Upon receiving the notification, log a custom crash event and update user attributes with Apteligent's crash reporting analytics:

```objc
- (void)crashDidOccur:(NSNotification*)notification {
  NSDictionary *crashInfo = notification.userInfo;
  [[Appboy sharedInstance] logCustomEvent:@"ApteligentCrashEvent" withProperties:crashInfo];
  [[Appboy sharedInstance].user setCustomAttributeWithKey:@"lastCrashName" andStringValue:crashInfo[@"crashName"]];
  [[Appboy sharedInstance].user setCustomAttributeWithKey:@"lastCrashReason" andStringValue:crashInfo[@"crashReason"]];
  [[Appboy sharedInstance].user setCustomAttributeWithKey:@"lastCrashDate" andDateValue:crashInfo[@"crashDate"]];
}
```

That's it! Now you'll be able to harness the power of Braze's segmentation, analytics, and engagement using the crash information that Apteligent provides.

[1]: https://www.apteligent.com/

---
nav_title: Apteligent
article_title: Apteligent
alias: /partners/apteligent/
description: "This article outlines the partnership between Braze and Apteligent, a mobile application that details crash reporting, allowing you to log critical data into your existing Braze solution."
page_type: partner
search_tag: Partner

---

# Apteligent

> [Apteligent](https://kb.vmtestdrive.com/hc/en-us/articles/360001544114-Apteligent-by-VMware-Walkthrough) is a mobile application performance platform providing tools and insights for developers and product managers. 

The Braze and Apteligent integration provides detailed iOS crash reporting, allowing you to log critical data into your existing Braze solution as well as  segment, understand, and engage with users who have experienced application crashes.

## Prerequisites 

| Requirement | Description |
|---|---|
| TestDrive account | A [TestDrive account](https://kb.vmtestdrive.com/hc/en-us/articles/360001372254-Getting-Started-with-TestDrive) is required to take advantage of this partnership. |
{: .reset-td-br-1 .reset-td-br-2}

{% alert warning %}
This integration is currently only supported on iOS.
{% endalert %}

## Integration {#apteligent-ios-integration}

### Step 1: Register an observer

First, you must register an observer. Ensure that this is done before you initialize Apteligent.

```objc
[[NSNotificationCenter defaultCenter] addObserver:self
                                         selector:@selector(crashDidOccur:)
                                             name:@"CRCrashNotification"
                                           object:nil];
```

### Step 2: Log custom crash analytics

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

Once completed, you'll be able to harness the power of Braze's segmentation and engagement analytics using the crash information found in the Apteligent platform.
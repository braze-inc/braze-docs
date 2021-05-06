---
nav_title: Setting User IDs
platform: Xamarin
subplatform: iOS
page_order: 0
---
# Setting User IDs

See [the iOS integration instructions][1] for an in depth discussion of when and how to set and change a user ID.

**Xamarin C#**

```csharp
Appboy.SharedInstance().ChangeUser("YOUR_USER_ID");
```

[1]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/analytics/setting_user_ids/

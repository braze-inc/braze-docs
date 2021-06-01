---
nav_title: Setting User IDs
platform: Xamarin
subplatform: Android and FireOS
page_order: 0

---

# Setting User IDs

See [the Android integration instructions][1] for an in depth discussion of when and how to set and change a user ID.

```csharp
Appboy.GetInstance(context).ChangeUser("YOUR_USER_ID");
```

[1]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/setting_user_ids/

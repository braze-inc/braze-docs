---
nav_title: Release Notes
article_title: Release Notes
page_order: 4
layout: dev_guide
guide_top_header: "Release Notes"
guide_top_text: "This is where you can find all updates to the Braze platform, with the following <a href='/docs/help/release_notes/#most-recent'>most recent platform updates</a>. You can also check out our <a href='/docs/developer_guide/platform_integration_guides/sdk_changelogs/'>SDK Changelogs</a>."
page_type: landing
search_rank: 1
description: "This landing page is home to Braze Release Notes. This is where you can find all updates to the Braze platform and SDKs, as well as a list of deprecated features."

guide_featured_title: "Release Notes"
guide_featured_list:
  - name: 2023
    link: /docs/help/release_notes/2023/
    fa_icon: fas fa-calendar-alt
  - name: 2022
    link: /docs/help/release_notes/2022/
    fa_icon: fas fa-calendar-alt
  - name: 2021
    link: /docs/help/release_notes/2021/
    fa_icon: fas fa-calendar-alt
  - name: 2020
    link: /docs/help/release_notes/2020/
    fa_icon: fas fa-calendar-alt
  - name: 2019
    link: /docs/help/release_notes/2019/
    fa_icon: fas fa-calendar-alt
  - name: 2018
    link: /docs/help/release_notes/2018/
    fa_icon: fas fa-calendar-alt
  - name: 2017
    link: /docs/help/release_notes/2017/
    fa_icon: fas fa-calendar-alt
  - name: 2016
    link: /docs/help/release_notes/2016/
    fa_icon: fas fa-calendar-alt
  - name: Deprecations
    link: /docs/help/release_notes/deprecations/
    fa_icon: far fa-calendar-times
  - name: SDK Changelogs
    link: /docs/developer_guide/platform_integration_guides/sdk_changelogs/
    fa_icon: fas fa-file-code

---

# Most recent Braze release notes {#most-recent}

> Braze releases information on product updates on a monthly cadence, aligning with major Product Releases, though the product is updated with miscellaneous improvements week to week.
> <br>
> <br>
> For more information on any of the updates listed in this section, reach out to your account manager or [open a support ticket]({{site.baseurl}}/help/support/). You can also check out [our SDK Changelogs]({{site.baseurl}}/developer_guide/platform_integration_guides/sdk_changelogs/) to see more information on our monthly SDK releases, updates, and improvements.

## October 17, 2023 release
### Copying to workspaces

[Copying campaigns across a workspace]({{site.baseurl}}/user_guide/engagement_tools/campaigns/managing_campaigns/copying_to_workspace/) allows you to get a jumpstart on your message composition by starting with a copy of a campaign in a different workspace. This copy will remain as a draft until you edit and launch, helping you keep and build off your successful messaging strategies.

### Test Currents connectors

[Test Currents connectors]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/setting_up_currents/#test-currents-connectors) are free versions of our existing connectors that can be used for testing and trying out different destinations. Test Currents have:

- No limit to the number of Test Currents connectors you may build.
- An aggregate maximum of 10,000 events per 30-day rolling period. This event total is updated hourly on the dashboard.

### Feature flags

[Feature flags]({{site.baseurl}}/developer_guide/platform_wide/feature_flags/about/) allow you to remotely enable or disable functionality for a specific or random selection of users. Importantly, they let you turn a feature on and off in production without additional code deployment or app store updates. This allows you to safely roll out new features with confidence.

### Feature flag experiments

[Feature flag experiments]({{site.baseurl}}/developer_guide/platform_wide/feature_flags/experiments/) let you A/B test changes to your applications to optimize conversion rates. Marketers can use feature flags to determine whether a new feature positively or negatively impacts conversion rates, or which set of feature flag properties is most optimal.

### Merging user profiles

If your search on the **Search Users** page returns multiple user profiles, you can [merge user profiles]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles#merge-profiles) by clicking the **Merge duplicates** button. You can select which user profile to keep, meaning this profile will be kept and will gain attributes from the merged profile.

### Performance data by segment

You can now use Query Builder report templates to [break down performance data]({{site.baseurl}}/user_guide/data_and_analytics/reporting/viewing_and_understanding_segment_data/#performance-data-by-segment) by segments for campaigns, Canvas, variants, and steps.

### Updating user profiles

You can now use the [`/users/track` endpoint]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) to update a user profile by phone number or email.

## SDK updates
 
The following SDK updates have been released. Breaking updates are listed below; all other updates can be found by checking the corresponding SDK changelogs.
 
- [Braze Segment Swift Plugin v2.1.0](https://github.com/braze-inc/braze-segment-swift/blob/main/CHANGELOG.md)
- [Web SDK v4.10.0](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md)
- [Web SDK v5.0.0](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md)
    - The [`subscribeToFeatureFlagsUpdates()`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#subscribetofeatureflagsupdates) callback will now always be called, regardless of refresh success/failure. If there is a failure in receiving updates, the callback will be called with currently cached feature flags.
    - The [`getFeatureFlag()`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#getfeatureflag) method now returns a null if the feature flag does not exist, or if feature flags are disabled.
    - Removed `logContentCardsDisplayed()` method that was previously deprecated in 4.0.4.
    - Removed the deprecated initialization option `enableHtmlInAppMessages`. This should be replaced with the `allowUserSuppliedJavascript` option instead.
    - Removed Banner class that was previously deprecated in 4.9.0 in favor of [`ImageOnly`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.imageonly.html).
    - Removed `ab-banner` CSS classname as part of `Banner` class removal. CSS customizations should instead target the `ab-image-only` class.
    - The SDK no longer throws runtime errors anywhere. If Braze methods are called prior to initialization, a warning will be logged to the console instead.
    - The SDK no longer adds default Braze in-app message styles to custom HTML in-app messages. These styles were previously used by legacy in-app message types.
- [Android SDK 29.0.0](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md)
    - Renamed `BannerImageCard`, `BannerImageCardView`, and `BannerImageContentCardView` to `ImageOnlyCard`, `ImageOnlyCardView`, and `ImageOnlyContentCardView`.
    - All styles used for Banner Cards have been updated to Image Only Cards. All keys with the word `banner` should be replaced with `image_only`.
    - Device brand information is now sent. If you want to block this, see Blocking data collection.
- [Flutter SDK 7.0.0](https://pub.dev/packages/braze_plugin/changelog)
    - Updates the native Android bridge [from Braze Android SDK 26.1.1 to 27.0.1](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#2701).
    - Adds support for Gradle 8.
- [Swift SDK 7.0.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md)
    - The `useUUIDAsDeviceId` configuration is now enabled by default.
        - For more details on the impacts, refer to this [Collecting IDFV - Swift]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/swift_idfv/).
    - The Banner Content Card type and corresponding UI elements have been renamed to `ImageOnly`. All member methods and properties remain the same.
        - `Braze.ContentCard.Banner` → `Braze.ContentCard.ImageOnly`
        - `BrazeContentCardUI.BannerCell` → `BrazeContentCardUI.ImageOnlyCell`
    - Refactors some text layout logic in BrazeUI into a new Braze.ModalTextView class.
    - Updates the behavior for Feature Flags methods.
        - `FeatureFlags.featureFlag(id:)` now returns nil for an ID that does not exist.
        - `FeatureFlags.subscribeToUpdates(:)` will trigger the callback when any refresh request completes with a success or failure.
            - The callback will also trigger immediately upon initial subscription if previously cached data exists.
- [AppboyKit iOS SDK 4.6.0](https://github.com/Appboy/appboy-ios-sdk/releases/tag/4.6.0)
    - This release requires Xcode `14.x`.
    - Drops support for iOS 9 and iOS 10.
    - Removes support for the outdated `.framework` assets when importing via Carthage in favor of the modern `.xcframework` assets.
        - Use the command `carthage update --use-xcframeworks` to import the appropriate Braze asset.
        - Removes support for `appboy_ios_sdk_full.json` in favor of using `appboy_ios_sdk.json`

<br><br>

---
nav_title: Banner Cards
article_title: Banner Cards
page_order: 1
description: "This reference article covers Banner Cards and how to integrate this feature in the Braze SDK."
platform:
  - iOS
  - Android
  - Web
  
---

# Banner Cards

(intro)


This feature is available as of the following [SDK versions]({{ site.baseurl }}/user_guide/engagement_tools/campaigns/ideas_and_strategies/new_features/#filtering-by-most-recent-app-versions):

{% sdk_min_versions  %}

## Dashboard Prerequisites

### Define Placements {#define-placements}

todo

### Launch a Banner Campaign

todo

## Refresh Placements in your app {#requestBannersRefresh}


{% tabs %}
{% tab JavaScript %}

```javascript
import * as braze from "@braze/web-sdk";

braze.requestBannersRefresh(["global_banner", "navigation_square_banner"])
```

{% endtab %}
{% tab Swift %}

```swift
todo
```
{% endtab %}
{% tab Java %}
```java
todo
```

{% endtab %}
{% tab Kotlin %}

```kotlin
todo
```

{% endtab %}
{% tab React Native %}

```javascript
This feature is not currently supported on React Native
```

{% endtab %}
{% tab Unity %}
```csharp
This feature is not currently supported on Unity.
```
{% endtab %}

{% tab Cordova %}
```javascript
This feature is not currently supported on Cordova.
```
{% endtab %}
{% tab Flutter %}
```dart
This feature is not yet available in Flutter.
```
{% endtab %}

{% tab Roku %}
```brightscript
This feature is not currently supported on Roku.
```
{% endtab %}
{% endtabs %}

## Listen for updates {#subscribeToBannersUpdates}


{% tabs %}
{% tab JavaScript %}

```javascript
import * as braze from "@braze/web-sdk";

braze.subscribeToBannersUpdates((banners) => {
    console.log(`Banners were updated`);
})
```

{% endtab %}
{% tab Swift %}

```swift
todo
```
{% endtab %}
{% tab Java %}
```java
todo
```

{% endtab %}
{% tab Kotlin %}

```kotlin
todo
```

{% endtab %}
{% tab React Native %}

```javascript
This feature is not currently supported on React Native
```

{% endtab %}
{% tab Unity %}
```csharp
This feature is not currently supported on Unity.
```
{% endtab %}

{% tab Cordova %}
```javascript
This feature is not currently supported on Cordova.
```
{% endtab %}
{% tab Flutter %}
```dart
This feature is not yet available in Flutter.
```
{% endtab %}

{% tab Roku %}
```brightscript
This feature is not currently supported on Roku.
```
{% endtab %}
{% endtabs %}

## Get and Insert a Banner by placement ID {#}


{% tabs %}
{% tab JavaScript %}

```javascript
import * as braze from "@braze/web-sdk";

// get this placement's banner. If it's `null` the user did not qualify for one.
const globalBanner = braze.getBanner("global_banner");

// choose where in the DOM you want to insert the banner HTML
const container = document.getElementById("global-banner-container");

// Insert the banner which replacees the innerHTML of that container
braze.insertBanner(globalBanner, container);

// Special handling if the user is part of a Control Variant
if (globalBanner.isControl) {
    // hide or collapse the container
    container.style.display = 'none';
}

```

{% endtab %}
{% tab Swift %}

```swift
todo
```
{% endtab %}
{% tab Java %}
```java
todo
```

{% endtab %}
{% tab Kotlin %}

```kotlin
todo
```

{% endtab %}
{% tab React Native %}

```javascript
This feature is not currently supported on React Native
```

{% endtab %}
{% tab Unity %}
```csharp
This feature is not currently supported on Unity.
```
{% endtab %}

{% tab Cordova %}
```javascript
This feature is not currently supported on Cordova.
```
{% endtab %}
{% tab Flutter %}
```dart
This feature is not yet available in Flutter.
```
{% endtab %}

{% tab Roku %}
```brightscript
This feature is not currently supported on Roku.
```
{% endtab %}
{% endtabs %}

## Analytics

Braze will automatically handle all impression logging when using the SDK methods to insert banners.

If for some reason you need to parse and render the HTML yourself, you can use the following method to track impressions:


{% tabs %}
{% tab JavaScript %}

```javascript
import * as braze from "@braze/web-sdk";

const banner = braze.getBanner("global_banner");
if (banner?.html) {
    // do something with the html
    // then log an impression when the HTML is in view
    braze.logBannerImpressions([banner.id]);
}
```

{% endtab %}
{% tab Swift %}

```swift
todo
```
{% endtab %}
{% tab Java %}
```java
todo
```

{% endtab %}
{% tab Kotlin %}

```kotlin
todo
```

{% endtab %}
{% tab React Native %}

```javascript
This feature is not currently supported on React Native
```

{% endtab %}
{% tab Unity %}
```csharp
This feature is not currently supported on Unity.
```
{% endtab %}

{% tab Cordova %}
```javascript
This feature is not currently supported on Cordova.
```
{% endtab %}
{% tab Flutter %}
```dart
This feature is not yet available in Flutter.
```
{% endtab %}

{% tab Roku %}
```brightscript
This feature is not currently supported on Roku.
```
{% endtab %}
{% endtabs %}

## Best Practices

#### Banner Dimensions and Sizing

#### Connected Content

## Roadmap {#roadmap}

#### Sorting banners in priority order

#### Dismissing or collapsing banners

#### Custom Properties or Key-Value Pairs

#### Promo Codes and Catalogs

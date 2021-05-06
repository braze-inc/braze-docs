---
nav_title: Location Tracking
platform: Web
page_order: 5

---
# Location Tracking

To enable location tracking via the Braze Web SDK, call

```
appboy.trackLocation();
```

This will cause the Braze Web SDK to continuously collect the user's location (in browsers that support it), whenever your site is visible in the foreground of the user's browser. This location collection will continue for the duration of the page load (you should call this method for each page on which you want the location to be tracked). Note that calling this will immediately request permission from the user unless they have already granted or denied permission. See the [JSDocs][0] for more information.

## Logging A Single Location

To manually set a user's last known location yourself, you can use

```
appboy.getUser().setLastKnownLocation(latitude, longitude, accuracy, altitude, altitudeAccuracy);
```

See the [JSDocs][1] for more information.

Additionally, when the Web SDK sends data to Braze servers, the user's country will be automatically detected from their IP Address if it has not been manually set by your application.

[0]: https://js.appboycdn.com/web-sdk/latest/doc/module-appboy.html#.trackLocation
[1]: https://js.appboycdn.com/web-sdk/latest/doc/ab.User.html#setLastKnownLocation

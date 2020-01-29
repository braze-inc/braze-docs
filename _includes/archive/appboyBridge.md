|Method (click each method for its documentation) | Description |
|:------ |:------------|
|`appboyBridge.closeMessage()`|Closes this in-app message.|
|[`appboyBridge.requestImmediateDataFlush()`](https://js.appboycdn.com/web-sdk/latest/doc/module-appboy.html#.requestImmediateDataFlush)||
|**TODO**[`appboyBridge.logClick(buttonId)`](https://js.appboycdn.com/web-sdk/latest/doc/module-appboy.html#.logClick)|Log a button click for a given `buttonId` string. When `buttonId` is left blank, a body-click will be logged instead. This method was introduced in Android SDK v5.0.0 and iOS SDK v3.23.0.|
|[`appboyBridge.logCustomEvent(eventName, eventProperties)`](https://js.appboycdn.com/web-sdk/latest/doc/module-appboy.html#.logCustomEvent)| Log a custom event.|
|[`appboyBridge.logPurchase(productId, price, currencyCode, quantity, purchaseProperties)`](https://js.appboycdn.com/web-sdk/latest/doc/module-appboy.html#.logPurchase)||
|[`appboyBridge.display.showFeed()`](https://js.appboycdn.com/web-sdk/latest/doc/module-display.html#.showFeed)||
|[`appboyBridge.getUser().addToCustomAttributeArray(key, value)`](https://js.appboycdn.com/web-sdk/latest/doc/ab.User.html#addToCustomAttributeArray)||
|[`appboyBridge.getUser().setFirstName(firstName)`](https://js.appboycdn.com/web-sdk/latest/doc/ab.User.html#setFirstName)||
|[`appboyBridge.getUser().setLastName(lastName)`](https://js.appboycdn.com/web-sdk/latest/doc/ab.User.html#setLastName)||
|[`appboyBridge.getUser().setEmail(email)`](https://js.appboycdn.com/web-sdk/latest/doc/ab.User.html#setEmail)||
|[`appboyBridge.getUser().setGender(gender)`](https://js.appboycdn.com/web-sdk/latest/doc/ab.User.html#setGender)||
|[`appboyBridge.getUser().setDateOfBirth(year, month, day)`](https://js.appboycdn.com/web-sdk/latest/doc/ab.User.html#setDateOfBirth)||
|[`appboyBridge.getUser().setCountry(country)`](https://js.appboycdn.com/web-sdk/latest/doc/ab.User.html#setCountry)||
|[`appboyBridge.getUser().setHomeCity(city)`](https://js.appboycdn.com/web-sdk/latest/doc/ab.User.html#setHomeCity)||
|[`appboyBridge.getUser().setEmailNotificationSubscriptionType(notificationSubscriptionType)`](https://js.appboycdn.com/web-sdk/latest/doc/ab.User.html#setEmailNotificationSubscriptionType)||
|[`appboyBridge.getUser().setPushNotificationSubscriptionType(notificationSubscriptionType)`](https://js.appboycdn.com/web-sdk/latest/doc/ab.User.html#setPushNotificationSubscriptionType)||
|[`appboyBridge.getUser().setPhoneNumber(phoneNumber)`](https://js.appboycdn.com/web-sdk/latest/doc/ab.User.html#setPhoneNumber)||
|[`appboyBridge.getUser().setCustomUserAttribute(key, value)`](https://js.appboycdn.com/web-sdk/latest/doc/ab.User.html#setCustomUserAttribute)||
|[`appboyBridge.getUser().removeFromCustomAttributeArray(key, value)`](https://js.appboycdn.com/web-sdk/latest/doc/ab.User.html#removeFromCustomAttributeArray)||
|[`appboyBridge.getUser().incrementCustomUserAttribute(key, incrementValue)`](https://js.appboycdn.com/web-sdk/latest/doc/ab.User.html#incrementCustomUserAttribute)||
|[`appboyBridge.getUser().setLanguage(language)`](https://js.appboycdn.com/web-sdk/latest/doc/ab.User.html#setLanguage)|Introduced in Android SDK v5.0.0 and iOS SDK v3.23.0.|
|[`appboyBridge.getUser().setCustomLocationAttribute(key, latitude, longitude)`](https://js.appboycdn.com/web-sdk/latest/doc/ab.User.html#setCustomLocationAttribute)|Introduced in Android SDK v5.0.0 and iOS SDK v3.23.0.|
|[`appboyBridge.getUser().appboyBridge.web.trackLocation()`](https://js.appboycdn.com/web-sdk/latest/doc/ab.User.html#incrementCustomUserAttribute)|This method is a no-op when called in a non-web environment. Introduced in Android SDK v5.0.0 and iOS SDK v3.23.0.|
|[`appboyBridge.web.registerAppboyPushMessages(successCallback, deniedCallback)`](https://js.appboycdn.com/web-sdk/latest/doc/module-appboy.html#.registerAppboyPushMessages)| Register for web push. This method is a no-op when called in a non-web environment Introduced in Android SDK v5.0.0 and iOS SDK v3.23.0.|

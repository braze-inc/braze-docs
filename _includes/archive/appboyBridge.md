```javascript
// Closes this in-app message
appboyBridge.closeMessage()

// Has the same behavior and arguments as https://js.appboycdn.com/web-sdk/latest/doc/module-appboy.html#.logCustomEvent
appboyBridge.logCustomEvent(eventName, eventProperties)

// Has the same behavior and arguments as https://js.appboycdn.com/web-sdk/latest/doc/module-appboy.html#.logPurchase
appboyBridge.logPurchase(productId, price, currencyCode, quantity, purchaseProperties)

// Has the same behavior and arguments as https://js.appboycdn.com/web-sdk/latest/doc/module-appboy.html#.requestImmediateDataFlush
appboyBridge.requestImmediateDataFlush()

// Has the same behavior and arguments as https://js.appboycdn.com/web-sdk/latest/doc/module-display.html#.showFeed
appboyBridge.display.showFeed()

// Has the same behavior and arguments as https://js.appboycdn.com/web-sdk/latest/doc/ab.User.html#setFirstName
appboyBridge.getUser().setFirstName(firstName)

// Has the same behavior and arguments as https://js.appboycdn.com/web-sdk/latest/doc/ab.User.html#setLastName
appboyBridge.getUser().setLastName(lastName)

// Has the same behavior and arguments as https://js.appboycdn.com/web-sdk/latest/doc/ab.User.html#setEmail
appboyBridge.getUser().setEmail(email)

// Has the same behavior and arguments as https://js.appboycdn.com/web-sdk/latest/doc/ab.User.html#setGender
appboyBridge.getUser().setGender(gender)

// Has the same behavior and arguments as https://js.appboycdn.com/web-sdk/latest/doc/ab.User.html#setDateOfBirth
appboyBridge.getUser().setDateOfBirth(year, month, day)

// Has the same behavior and arguments as https://js.appboycdn.com/web-sdk/latest/doc/ab.User.html#setCountry
appboyBridge.getUser().setCountry(country)

// Has the same behavior and arguments as https://js.appboycdn.com/web-sdk/latest/doc/ab.User.html#setHomeCity
appboyBridge.getUser().setHomeCity(city)

// Has the same behavior and arguments as https://js.appboycdn.com/web-sdk/latest/doc/ab.User.html#setEmailNotificationSubscriptionType
appboyBridge.getUser().setEmailNotificationSubscriptionType(notificationSubscriptionType)

// Has the same behavior and arguments as https://js.appboycdn.com/web-sdk/latest/doc/ab.User.html#setPushNotificationSubscriptionType
appboyBridge.getUser().setPushNotificationSubscriptionType(notificationSubscriptionType)

// Has the same behavior and arguments as https://js.appboycdn.com/web-sdk/latest/doc/ab.User.html#setPhoneNumber
appboyBridge.getUser().setPhoneNumber(phoneNumber)

// Has the same behavior and arguments as https://js.appboycdn.com/web-sdk/latest/doc/ab.User.html#setCustomUserAttribute
appboyBridge.getUser().setCustomUserAttribute(key, value)

// Has the same behavior and arguments as https://js.appboycdn.com/web-sdk/latest/doc/ab.User.html#addToCustomAttributeArray
appboyBridge.getUser().addToCustomAttributeArray(key, value)

// Has the same behavior and arguments as https://js.appboycdn.com/web-sdk/latest/doc/ab.User.html#removeFromCustomAttributeArray
appboyBridge.getUser().removeFromCustomAttributeArray(key, value)

// Has the same behavior and arguments as https://js.appboycdn.com/web-sdk/latest/doc/ab.User.html#incrementCustomUserAttribute
appboyBridge.getUser().incrementCustomUserAttribute(key, incrementValue)
{% if include.platform == 'web' %}
// Has the same behavior and arguments as https://js.appboycdn.com/web-sdk/latest/doc/module-appboy.html#.registerAppboyPushMessages
appboyBridge.web.registerAppboyPushMessages(successCallback, deniedCallback)
{% endif %}```

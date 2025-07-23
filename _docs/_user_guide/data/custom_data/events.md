---
nav_title: Events
article_title: Events
page_order: 0
page_type: reference
description: "This article describes the different events in Braze—standard events, purchase events, and custom events—and their purpose."
---

# Events 

> This page covers the different events in Braze and their purpose.

Braze uses a few different event types to provide a comprehensive understanding of user behavior and engagement with your brand. Each type of event serves a unique purpose:

- [Standard events](#standard-events): Provide a basic understanding of user engagement with your app or site.
- [Purchase events](#purchase-events): Crucial for understanding user purchasing behavior and for tracking revenue. 
- [Custom events](#custom-events): Provide deeper insight into user behaviors that are unique to your app or business.

By tracking these different types of events, you can gain a deeper understanding of your users, which can inform your marketing strategies, help you optimize your app, and empower you to provide a more personalized user experience. Let's dive in!

## Standard events

In Braze, standard events are predefined actions that users can take within your app that Braze automatically tracks after you integrate the Braze SDK. Here are a few examples of standard events:

- App launch
- [Purchase](#purchase-events)
- Session start
- Session end
- Clicked push notification
- Opened email

As a marketer, you can use these standard events to understand user behavior and engagement with your app. For example, you can see how often users are launching your app or how many purchases are being made. This information can be invaluable when it comes to creating targeted marketing campaigns.

It's important to note that while standard events are automatically tracked by Braze, purchase events, custom events, and custom attributes need to be set up by your development team based on your specific needs and goals.

## Purchase events

Purchase events are a way to record and track purchases made by your users. They are a type of standard event that is available by default after you integrate the Braze SDK. Because of this, when you use purchase events to track purchases, you can monitor your revenue over time and across different revenue sources directly from Braze.

Purchase events record the following key information about a purchase:

- Product ID (typically the product name or category)
- Currency
- Price
- Quantity

You can then use this data to segment your users based on their lifetime value, purchase frequency, specific purchases, and more.

Braze also supports purchases in multiple currencies. If a purchase is reported in a currency other than USD, it will be shown in the Braze dashboard in USD, based on the exchange rate at the date the purchase was reported.

To learn more, visit our dedicated [purchase events]({{site.baseurl}}/user_guide/data/custom_data/purchase_events/) article.

{% details Example implementation %}

Note that the actual implementation of purchase events will require some technical knowledge as it involves integrating the Braze SDK with your app. Your customer success manager will walk your team through this process as part of your onboarding, but the general steps are as follows:

1. **Integrate the Braze SDK:** Before logging any events, you need to integrate the Braze SDK into your app.
2. **Log the purchase event:** After the SDK is integrated, you can log a purchase event whenever a user makes a purchase in your app. This is typically done in the function or method called when a purchase is completed.

Here's an example of how to log a purchase event in an iOS app using Swift:

```swift
Appboy.sharedInstance()?.logPurchase("product_name", inCurrency: "USD", atPrice: NSDecimalNumber(string: "1.99"), withQuantity: 1)
```

In this example, "product_name" is the name of the product that was purchased, "USD" is the currency of the purchase, "1.99" is the price of the product, and "1" is the quantity purchased.

{:start="3"}
3. **View the purchase event in the Braze dashboard:** After the purchase event is logged, you can view it in the Braze dashboard. You can use this data to analyze your revenue, segment your users, and more.

Remember, the exact implementation may vary depending on the platform (iOS, Android, Web) and the specific requirements of your app. 

{% enddetails %}

## Custom events

Custom events are events that you define based on the specific actions you want to track within your app or site. Braze doesn't automatically track them—you must manually set up these events in your Braze SDK implementation. Custom events can be anything from a user completing a level in a game to a user updating their profile information.

Here's an example of how to log a custom event in an iOS app using Swift:

```swift
Appboy.sharedInstance()?.logCustomEvent("completed_level")
```

In this example, "completed_level" is the name of the custom event that gets logged when a user completes a level in a game. That custom event is then recorded on their user profile in Braze, which you can use to trigger campaigns and personalize messaging.

To learn more, visit our dedicated [custom events]({{site.baseurl}}/user_guide/data/custom_data/custom_events/) article.

{% details Example implementation %}

Similar to purchase events, custom events require additional setup. Here's a general process for implementing custom events in Braze:

1. **Integrate the Braze SDK:** Before you can log any events, you need to integrate the Braze SDK into your app.
2. **Define your custom event:** Decide what action in your app you want to track as a custom event. This could be anything that's significant to your app, such as a user completing a level in a game, a user updating their profile, or a user making a specific type of purchase.
3. **Log the custom event:** After you've defined your custom event, you can log it in your app's code. This is typically done in the function or method that gets called when the action occurs.

Here's an example of how to log a custom event in an iOS app using Swift:

```swift
Appboy.sharedInstance()?.logCustomEvent("updated_profile")
```

In this example, "updated_profile" is the name of the custom event that gets logged when a user updates their profile.

{:start="4"}
4. **Add properties to your custom event (optional):** If you want to capture additional details about the custom event, you can add properties to it. This is done by passing a dictionary of properties when you log the event.

Here's an example of how to log a custom event with properties in an iOS app using Swift:

```swift
let properties: [AnyHashable: Any] = ["Property Name": "Property Value"]
Appboy.sharedInstance()?.logCustomEvent("updated_profile", withProperties: properties)
```

In this example, the custom event has a property called "Property Name" with a value of "Property Value".

{:start="5"}
5. **View the custom event in the Braze dashboard:** After the custom event is logged, you can view it in the Braze dashboard. You can use this data to analyze user behavior, segment your users, and more.

{% enddetails %}

<!--

### Using custom events instead of purchase events to track purchases

You might prefer to use custom events to track purchases if you need to capture more specific or additional information about the purchase that the standard purchase event doesn't cover. Here's what you can do with custom events that you can't accomplish with purchase events:

- **Custom definitions:** Custom events can be defined based on any significant action within your app. This level of customization is not available with standard purchase events, which are predefined and specifically designed to track purchases.
- **Additional properties:** You can log additional properties to custom events that provide more context about the event. For example, you could log a custom event when a user makes a purchase and include properties such as the product category or the payment method. This is not possible with standard purchase events, which have a fixed schema that only tracks the product name, currency, price, and quantity.
- **Event frequency:** Custom events allow you to track the frequency of specific actions. With purchase events, you can only track the occurrence of purchases, not other types of actions.

#### Use case 1

Let's say you have an eCommerce app, and you want to track the purchase itself and the product category. The standard purchase event in Braze does not capture this level of detail, so you could use a custom event instead.

Here's an example of how you might do this in an iOS app using Swift:

```swift
let properties: [AnyHashable: Any] = ["Product Category": "Electronics"]
Appboy.sharedInstance()?.logCustomEvent("Purchase", withProperties: properties)
```

In this example, "Purchase" is the name of the custom event, and the properties dictionary contains additional information about the event. In this case, the product category is "Electronics". Now you can segment your users based on the product categories they purchase from.

#### Use case 2

Consider a fitness app where users can purchase personal training sessions or premium workout plans. In this case, you might want to track these purchases as custom events to capture additional details about the purchase.

Here's an example of how you might do this in an iOS app using Swift:

```swift
let properties: [AnyHashable: Any] = ["Workout Plan": "10 Sessions Personal Training"]
Appboy.sharedInstance()?.logCustomEvent("Purchase", withProperties: properties)
```

In this example, "Purchase" is the name of the custom event, and the properties dictionary contains additional information about the event. In this case, the workout plan is "10 Sessions Personal Training". Now you can segment your users based on the types of workout plans they purchase.

-->



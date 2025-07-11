# Braze React Native SDK Integration Guide

## Overview

The Braze React Native SDK is a comprehensive customer engagement platform that provides analytics, push notifications, in-app messages, and content cards functionality for both iOS and Android with a single codebase.

## Key Features

- **Cross-platform**: Single codebase for both iOS and Android
- **Push Notifications**: Rich notifications with deep linking support
- **In-App Messages**: Four types (slideup, modal, full, HTML full)
- **Content Cards**: Dynamic content delivery
- **Analytics**: User tracking and event logging
- **New Architecture Compatible**: Supports React Native's New Architecture

## Prerequisites

- **React Native Version**: 0.71 or later
- **Minimum SDK Version**: 2.0.1+ for New Architecture compatibility
- **Braze Account**: API keys and endpoint configuration
- **Platform-specific Setup**: iOS/Android native configuration

## Installation

### Step 1: Install the SDK

```bash
# Using npm
npm install @braze/react-native-sdk

# Using yarn
yarn add @braze/react-native-sdk
```

### Step 2: Choose Your Setup Method

You have two main options:

#### Option A: Expo Plugin (Recommended for Expo projects)

```bash
expo install @braze/expo-plugin
```

#### Option B: Native Setup (For bare React Native projects)

Configure iOS and Android separately with native code.

## Configuration

### Expo Plugin Configuration

Add to your `app.json`:

```json
{
  "expo": {
    "plugins": [
      [
        "@braze/expo-plugin",
        {
          "androidApiKey": "YOUR-ANDROID-API-KEY",
          "iosApiKey": "YOUR-IOS-API-KEY", 
          "baseUrl": "YOUR-SDK-ENDPOINT",
          "sessionTimeout": 60,
          "enableGeofence": false,
          "enableBrazeIosPush": true,
          "enableFirebaseCloudMessaging": true,
          "firebaseCloudMessagingSenderId": "YOUR-FCM-SENDER-ID",
          "logLevel": 0
        }
      ]
    ]
  }
}
```

### Native Setup Configuration

For Android, create `android/app/src/main/res/values/braze.xml`:

```xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
  <string name="com_braze_api_key">YOUR_ANDROID_API_KEY</string>
  <string name="com_braze_custom_endpoint">YOUR_CUSTOM_ENDPOINT</string>
</resources>
```

For iOS, configure in `AppDelegate.swift`:

```swift
import BrazeKit

func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {
    let configuration = Braze.Configuration(
        apiKey: "YOUR_IOS_API_KEY",
        endpoint: "YOUR_CUSTOM_ENDPOINT"
    )
    let braze = BrazeReactBridge.perform(
        #selector(BrazeReactBridge.initBraze(_:)),
        with: configuration
    ).takeUnretainedValue() as! Braze
    
    AppDelegate.braze = braze
    return true
}
```

## Core SDK Usage

### Initialize and Import

```javascript
import Braze from "@braze/react-native-sdk";

// Set user ID
Braze.changeUser("user123");
```

### User Tracking and Analytics

#### Setting User Attributes

```javascript
// Default attributes
Braze.setFirstName("John");
Braze.setLastName("Doe");
Braze.setEmail("john.doe@example.com");
Braze.setCountry("US");
Braze.setHomeCity("New York");
Braze.setPhoneNumber("+1234567890");
Braze.setDateOfBirth(1990, 1, 1); // year, month, day

// Custom attributes
Braze.setCustomUserAttribute("subscription_type", "premium");
Braze.setCustomUserAttribute("loyalty_points", 1250);
Braze.setCustomUserAttribute("is_vip", true);

// Array attributes
Braze.addToCustomUserAttributeArray("interests", "sports");
Braze.addToCustomUserAttributeArray("interests", "technology");
```

#### Logging Custom Events

```javascript
// Simple event
Braze.logCustomEvent("made_purchase");

// Event with properties
Braze.logCustomEvent("product_viewed", {
    product_id: "abc123",
    category: "electronics",
    price: 299.99
});
```

#### Logging Purchases

```javascript
Braze.logPurchase("product_id", "USD", 29.99, 2, {
    product_name: "Premium Subscription",
    discount_applied: true
});
```

## Push Notifications

### Basic Setup

```javascript
// Request push permissions
const permissionOptions = {
    alert: true,
    sound: true,
    badge: true,
    provisional: false
};

Braze.requestPushPermission(permissionOptions);
```

### Listen for Push Events

```javascript
// Listen for push notifications
Braze.addListener(Braze.Events.PUSH_NOTIFICATION_EVENT, data => {
    console.log(`Push received: ${data.title}`);
    console.log(`Action: ${data.payload_type}`);
    console.log(`Deep link: ${data.url}`);
});
```

### Push Notification Properties

| Property | Type | Description |
|----------|------|-------------|
| `payload_type` | String | Either `push_opened` or `push_received` |
| `title` | String | Notification title |
| `body` | String | Notification body |
| `url` | String | Deep link URL |
| `use_webview` | Boolean | Whether to open URL in webview |
| `is_silent` | Boolean | Whether it's a silent notification |
| `braze_properties` | Object | Campaign properties |

### Deep Linking

```javascript
// Handle deep links from push notifications
Braze.getInitialPushPayload(pushPayload => {
    if (pushPayload && pushPayload.url) {
        // Handle the deep link
        handleDeepLink(pushPayload.url);
    }
});
```

## In-App Messages

### Message Types

1. **Slideup**: Small notifications at screen edge
2. **Modal**: Center screen with overlay
3. **Full**: Full screen takeover
4. **HTML Full**: Custom HTML content

### Listening for In-App Messages

```javascript
// Listen for in-app message events
Braze.addListener(Braze.Events.IN_APP_MESSAGE_RECEIVED, (message) => {
    console.log("In-app message received:", message);
    
    // Custom handling logic
    if (message.extras.custom_action) {
        handleCustomAction(message.extras.custom_action);
    }
});
```

### Message Properties

| Property | Type | Description |
|----------|------|-------------|
| `message` | String | Message text |
| `header` | String | Message header |
| `uri` | String | Click action URI |
| `imageUrl` | String | Image URL |
| `duration` | Number | Display duration |
| `clickAction` | String | Click action type |
| `dismissType` | String | Dismissal method |
| `messageType` | String | Message type |
| `extras` | Object | Additional properties |

## Content Cards

### Displaying Default UI

```javascript
// Launch default Content Cards UI
Braze.launchContentCards();
```

### Custom Content Cards Implementation

```javascript
import React, { useState, useEffect } from 'react';

const CustomContentCards = () => {
    const [cards, setCards] = useState([]);

    useEffect(() => {
        // Listen for card updates
        Braze.addListener(Braze.Events.CONTENT_CARDS_UPDATED, (update) => {
            setCards(update.cards);
        });

        // Request fresh cards
        Braze.requestContentCardsRefresh();
    }, []);

    const handleCardClick = (cardId) => {
        // Log analytics
        Braze.logContentCardClicked(cardId);
        // Process click action
        Braze.processContentCardClickAction(cardId);
    };

    const handleCardImpression = (cardId) => {
        Braze.logContentCardImpression(cardId);
    };

    return (
        <div>
            {cards.filter(card => !card.isControl).map(card => (
                <div key={card.id} onClick={() => handleCardClick(card.id)}>
                    {card.title && <h3>{card.title}</h3>}
                    {card.cardDescription && <p>{card.cardDescription}</p>}
                    {card.image && <img src={card.image} alt={card.title} />}
                </div>
            ))}
        </div>
    );
};
```

### Content Card Types

1. **Classic**: Title, description, optional image
2. **Captioned Image**: Full-sized image with text
3. **Image Only**: Full-sized clickable image
4. **Control**: For A/B testing (don't display)

## Advanced Features

### Session Tracking

```javascript
// Sessions are automatically tracked, but you can manually control them
Braze.openSession();
Braze.closeSession();
```

### Location Tracking

```javascript
// Set user location
Braze.setLocationCustomAttribute("last_known_location", {
    latitude: 40.7128,
    longitude: -74.0060
});
```

### Feature Flags

```javascript
// Get feature flag
Braze.getFeatureFlag("new_checkout_flow", (featureFlag) => {
    if (featureFlag.enabled) {
        // Show new checkout flow
    }
});
```

### SDK Authentication

```javascript
// Set up SDK authentication for enhanced security
Braze.setSdkAuthenticationSignature("your_jwt_signature");
```

## Best Practices

### Performance Optimization

1. **Lazy Loading**: Only load cards when needed
2. **Image Caching**: Cache images locally
3. **Background Processing**: Handle analytics in background
4. **Memory Management**: Remove listeners when components unmount

### Analytics Best Practices

1. **Consistent Naming**: Use consistent event/attribute names
2. **Meaningful Properties**: Include relevant context
3. **User Privacy**: Respect user privacy settings
4. **Data Validation**: Validate data before sending

### Error Handling

```javascript
// Handle SDK errors gracefully
Braze.setCustomUserAttribute("key", "value", (error) => {
    if (error) {
        console.error("Failed to set attribute:", error);
        // Implement retry logic or fallback
    }
});
```

## Testing and Debugging

### Test Integration

```javascript
// Test user identification
Braze.changeUser("test_user_123");

// Verify in Braze dashboard under User Search
// Look for user with ID "test_user_123"
```

### Debug Logging

```javascript
// Enable verbose logging during development
// Set logLevel: 0 in configuration for detailed logs
```

### Testing Push Notifications

1. Set up test user with `Braze.changeUser()`
2. Create push campaign in Braze dashboard
3. Add test user ID to campaign test
4. Send test notification

## Common Integration Patterns

### E-commerce Integration

```javascript
// Track product views
Braze.logCustomEvent("product_viewed", {
    product_id: "SKU123",
    category: "electronics",
    price: 299.99,
    brand: "TechBrand"
});

// Track purchases
Braze.logPurchase("SKU123", "USD", 299.99, 1, {
    category: "electronics",
    brand: "TechBrand",
    discount_code: "SAVE20"
});

// Update user attributes
Braze.setCustomUserAttribute("total_purchases", 5);
Braze.setCustomUserAttribute("lifetime_value", 1249.95);
```

### Social Media Integration

```javascript
// Track social engagement
Braze.logCustomEvent("content_shared", {
    content_type: "article",
    content_id: "article_123",
    platform: "facebook"
});

// Track profile completion
Braze.logCustomEvent("profile_completed", {
    completion_percentage: 100,
    missing_fields: []
});
```

## Migration and Maintenance

### SDK Updates

```bash
# Check current version
npm list @braze/react-native-sdk

# Update to latest version
npm update @braze/react-native-sdk
```

### Version Compatibility

- Check [GitHub repository](https://github.com/braze-inc/braze-react-native-sdk) for compatibility matrix
- Review [changelog](https://github.com/braze-inc/braze-react-native-sdk/blob/master/CHANGELOG.md) before updating
- Test thoroughly after updates

## Troubleshooting

### Common Issues

1. **Push notifications not working**: Check API keys and permissions
2. **Deep links not opening**: Verify URL scheme configuration
3. **Analytics not appearing**: Check user ID and API endpoint
4. **Cards not displaying**: Verify card campaign targeting
5. **iOS build errors**: Check CocoaPods and Xcode configuration

### Debug Steps

1. Enable verbose logging (`logLevel: 0`)
2. Check network connectivity
3. Verify API keys and endpoints
4. Test with known working campaigns
5. Check device permissions

## Resources

- [Official Documentation](https://www.braze.com/docs/developer_guide/platform_integration_guides/react_native/)
- [GitHub Repository](https://github.com/braze-inc/braze-react-native-sdk)
- [Sample Project](https://github.com/braze-inc/braze-react-native-sdk/tree/master/BrazeProject)
- [API Reference](https://braze-inc.github.io/braze-react-native-sdk/)
- [Changelog](https://github.com/braze-inc/braze-react-native-sdk/blob/master/CHANGELOG.md)

This comprehensive guide covers everything you need to integrate the Braze React Native SDK successfully. Start with the basic setup, then gradually implement the advanced features as needed for your specific use case.
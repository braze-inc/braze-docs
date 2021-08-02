---
nav_title: Content Cards
platform: React Native
page_order: 3

page_type: reference
description: "This article covers how to get started with Content Cards for React Native apps."

---

# Content Cards for React Native Integration

To get started with Content Cards, the Braze SDKs include a default card feed. To show the card feed you can use the `ReactAppboy.launchContentCards()` method.

The default card feed included with the Braze SDK will handle all analytics tracking, dismissals, and rendering for a user's Content Cards. Follow the respective guides below for integration.

## Integration

### Android

Follow [the Android integration instructions][2].

### iOS

Follow [the iOS integration instructions][3].

### Example to use following methods using React Hooks
```javascript
useEffect(() => {
    ReactAppboy.getContentCards();
    ReactAppboy.requestContentCardsRefresh();
    ReactAppboy.logContentCardsDisplayed();
}, []);
``` 

## Customization

You can use these additional methods to build a custom Content Cards Feed within your app:

|Method | Description |
|---|---|
|`ReactAppboy.requestContentCardsRefresh()`|Requests the latest Content Cards from the Braze SDK server.|
|`ReactAppboy.getContentCards()`|Retrieves Content Cards from the Braze SDK. This will return the latest list of cards from the server.|
|`ReactAppboy.logContentCardsDisplayed()`|Logs a Content Content feed displayed event.|
|`ReactAppboy.logContentCardClicked(cardId)`|Logs a click for the given Content Card ID.|
|`ReactAppboy.logContentCardImpression(cardId)`|Logs an impression for the given Content Card ID.|
|`ReactAppboy.logContentCardDismissed(cardId)`|Logs a dismissal for the given Content Card ID.|

## Test Displaying Sample Content Card

Follow the steps below to test a sample content card.

1. Set an active user in the React application by calling `ReactAppboy.changeUserId('your-user-id')` method.
2. Head to **Campaigns** and follow [this guide][4] to create a new **Content Card** campaign.
3. Compose your test content card campaign and head over to the **Test** tab. Add the same *user-id* as the test user and `Send Test`. You should be able to launch a content card on your device shortly.

![Content Card Campaign Test][5]

A sample implementation of this is contained in AppboyProject, within the [React SDK][1].

[1]: https://github.com/Appboy/appboy-react-sdk
[2]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/content_cards/data_models/
[3]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/content_cards/data_model/
[4]: {{site.baseurl}}user_guide/message_building_by_channel/content_cards/create
[5]: {% image_buster /assets/img/react-native/content-card-test.png %} "Content Card Campaign Test"

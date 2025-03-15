{% multi_lang_include developer_guide/prerequisites/react_native.md %}

## Accessing message data

In most cases, you can use the `Braze.addListener` method to register event listeners to handle data coming from in-app messages. 

Additionally, you can access the in-app message data in the JavaScript layer by calling the `Braze.subscribeToInAppMessage` method to have the SDKs publish an `inAppMessageReceived` event when an in-app message is triggered. Pass a callback to this method to execute your own code when the in-app message is triggered and received by the listener.

## Logging methods

You can use these methods by passing your `BrazeInAppMessage` instance to log analytics and perform actions:

| Method                                                    | Description                                                                           |
| --------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| `logInAppMessageClicked(inAppMessage)`                    | Logs a click for the provided in-app message data.                                    |
| `logInAppMessageImpression(inAppMessage)`                 | Logs an impression for the provided in-app message data.                              |
| `logInAppMessageButtonClicked(inAppMessage, buttonId)`    | Logs a button click for the provided in-app message data and button ID.               |
| `hideCurrentInAppMessage()`                               | Dismisses the currently displayed in-app message.                                     |
| `performInAppMessageAction(inAppMessage)`                 | Performs the action for an in-app message.                                            |
| `performInAppMessageButtonAction(inAppMessage, buttonId)` | Performs the action for an in-app message button.                                     |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}
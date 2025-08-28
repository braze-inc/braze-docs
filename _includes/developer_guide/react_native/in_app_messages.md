{% multi_lang_include developer_guide/prerequisites/react_native.md %}

## Message types

{% tabs %}
{% multi_lang_include developer_guide/_shared/in_app_messages/message_types/android.md %}
{% multi_lang_include developer_guide/_shared/in_app_messages/message_types/swift.md %}
{% endtabs %}

## Data model

The in-app message model is available in the React Native SDK. Braze has four in-app message types that share the same data model: **slideup**, **modal**, **full** and **HTML full**.

### Messages

The in-app message model provides the base for all in-app messages.

|Property          | Description                                                                                                            |
|------------------|------------------------------------------------------------------------------------------------------------------------|
|`inAppMessageJsonString` | The message JSON representation.                                                                                |
|`message`         | The message text.                                                                                                      |
|`header`          | The message header.                                                                                                    |
|`uri`             | The URI associated with the button click action.                                                                       |
|`imageUrl`        | The message image URL.                                                                                                 |
|`zippedAssetsUrl` | The zipped assets prepared to display HTML content.                                                                    |
|`useWebView`      | Indicates whether the button click action should redirect using a web view.                                            |
|`duration`        | The message display duration.                                                                                          |
|`clickAction`     | The button click action type. The types are: `URI`, and `NONE`.                                     |
|`dismissType`     | The message close type. The two types are: `SWIPE` and `AUTO_DISMISS`.                                                 |
|`messageType`     | The in-app message type supported by the SDK. The four types are: `SLIDEUP`, `MODAL`, `FULL` and `HTML_FULL`.          |
|`extras`          | The message extras dictionary. Default value: `[:]`.                                                                   |
|`buttons`         | The list of buttons on the in-app message.                                                                             |
|`toString()`      | The message as a String representation.                                                                                |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

For a full reference of the in-app message model, see the [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/index.html) and [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage) documentation.

### Buttons

Buttons can be added to in-app messages to perform actions and log analytics. The button model provides the base for all in-app message buttons.

|Property          | Description                                                                                                                 |
|------------------|-----------------------------------------------------------------------------------------------------------------------------|
|`text`            | The text on the button.                                                                                                     |
|`uri`             | The URI associated with the button click action.                                                                            |
|`useWebView`      | Indicates whether the button click action should redirect using a web view.                                                 |
|`clickAction`     | The type of click action processed when the user clicks on the button. The types are: `URI`, and `NONE`. |
|`id`              | The button ID on the message.                                                                                               |
|`toString()`      | The button as a String representation.                                                                                      |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

For a full reference of button model, see the [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-message-button/index.html) and [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage/button) documentation.

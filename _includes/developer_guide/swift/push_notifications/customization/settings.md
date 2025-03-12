## About advanced settings

When creating a push campaign through the dashboard, click the **Settings** tab on the **Compose** step to view the advanced settings available.

![]({% image_buster /assets/img_archive/ios_advanced_settings.png %})

## Key-value pairs

Braze allows you to send custom-defined string key-value pairs, known as `extras`, along with a push notification to your application. Extras can be defined via the dashboard or API and will be available as key-value pairs within the `notification` dictionary passed to your push delegate implementations.

## Alert options

Select the **Alert Options** checkbox to see a dropdown of key-values available to adjust how the notification appears on devices.

## Adding content-available flag

Check the **Add Content-Available Flag** checkbox to instruct devices to download new content in the background. Most commonly, this can be checked if you are interested in sending [silent notifications]({{site.baseurl}}/developer_guide/platforms/swift/push_notifications/silent/).

## Adding mutable-content flag

Check the **Add Mutable-Content Flag** checkbox to enable advanced receiver customization. This flag will automatically be sent when composing a [rich notification]({{site.baseurl}}/developer_guide/platforms/swift/push_notifications/rich/), regardless of the value of this checkbox.

## Update app badge count

Enter the number that you want to update your badge count to or use Liquid syntax to set custom conditions. You can also update a message badge count programmatically: refer to our dedicated [badge count]({{site.baseurl}}/developer_guide/platforms/swift/push_notifications/customization/badges/) article.

## Sounds

If you want your push notification to be accompanied by a custom sound when it is received, use the **Sound** field to specify the protocol URL of your sound file. For more on customization, refer to our [custom sounds]({{site.baseurl}}/developer_guide/platforms/swift/push_notifications/customization/sounds/) article.

## Collapse ID

Specify a collapse ID to coalesce similar notifications. If you send multiple notifications with the same collapse ID, the device will only show the most recently received notification. Refer to Apple's documentation on [coalesced notifications](https://developer.apple.com/library/content/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/APNSOverview.html#//apple_ref/doc/uid/TP40008194-CH8-SW1).

## Expiry

Checking the **Expiry** checkbox will allow setting an expiration time for your message. Should a user's device lose connectivity, Braze will continue to try and send the message until the specified time. If this is not set, the platform will default to an expiration of 30 days. Note that push notifications that expire before delivery are not considered failed and will not be recorded as a bounce.


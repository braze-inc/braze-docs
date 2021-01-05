---
nav_title: Customization
platform: Web
page_order: 3

---

## Customization {#in-app-message-customization}

All of Braze’s in-app message types are highly customizable across messages, images, [Font Awesome][15]  icons, click actions, analytics, editable styling, custom display options, and custom delivery options. Multiple options can be configured on a per in-app message basis from [within the dashboard]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/create/). Braze additionally provides multiple levels of advanced customization to satisfy a variety of use cases and needs.

### Key Value Pair Extras

In-app message objects may carry key value pairs as their `extras` property. These are specified on the dashboard under "Additional Message Settings" when creating an in-app message campaign. These can be used to send data down along with an in-app message for further handling by your site. For example:

```javascript
appboy.subscribeToInAppMessage(function(inAppMessage) {
  if (inAppMessage instanceof appboy.InAppMessage) {
    var extras = inAppMessage.extras;
    for (var key in extras) {
      if (data.hasOwnProperty(key)) {
         console.log("key: " + key + ", value: " + extras[key]);
      }
    }
  }

  appboy.display.showInAppMessage(inAppMessage);
});
```

### Custom Styling

Braze UI elements come with a default look and feel that create a neutral in-app message experience and aims for consistency with other Braze mobile platforms. Braze's default styles are defined in CSS within the Braze SDK. By overriding selected styles in your application, it is possible to customize our standard in-app message types with your own background images, font families, styles, sizes, animations, and more. For instance, the following is an example override that will cause an in-app message's headers to appear italicized:

```css
  body .ab-in-app-message .ab-message-header {
    font-style: italic;
  }
```

See the [JSDocs][2] for more information.

### Open Message Link in New Tab

To set your in-app message links to open in a new tab, set the `openInAppMessagesInNewTab` option to `true` to force all links from in-app message clicks open in a new tab or window.

```javascript
appboy.initialize('api-key', { openInAppMessagesInNewTab: true} );
```



[1]: https://github.com/Appboy/appboy-web-sdk#getting-started
[2]: https://js.appboycdn.com/web-sdk/latest/doc/ab.InAppMessage.html
[3]: https://js.appboycdn.com/web-sdk/latest/doc/ab.SlideUpMessage.html
[4]: {{site.baseurl}}//help/best_practices/in-app_messages/in-app_message_behavior/#in-app-message-behavior
[5]: #display-in-app
[6]: https://js.appboycdn.com/web-sdk/latest/doc/ab.ModalMessage.html
[7]: https://js.appboycdn.com/web-sdk/latest/doc/ab.FullScreenMessage.html
[8]: https://js.appboycdn.com/web-sdk/latest/doc/ab.ControlMessage.html
[9]: https://js.appboycdn.com/web-sdk/latest/doc/module-appboy.html#.initialize
[10]: {{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/tracking_sessions/#session-lifecycle
[11]: #inapp-customization
[12]: https://js.appboycdn.com/web-sdk/latest/doc/ab.HtmlMessage.html
[13]: {{site.baseurl}}/developer_guide/platform_integration_guides/web/in_app_messaging/#slideup-in-app-messages
[14]: #key-value
[15]: https://fontawesome.com/?from=io
[17]: {{site.baseurl}}/developer_guide/platform_integration_guides/web/in_app_messaging/#modal-in-app-messages
[30]: {% image_buster /assets/img_archive/trigger-iam-composer.png %}
[32]: #in-app-messages-triggered
[33]: #original-in-app-messages-deprecated
[35]: #styling
[40]: #message-types
[41]: {{site.baseurl}}/developer_guide/platform_integration_guides/web/in_app_messaging/#full-in-app-messages
[42]: {{site.baseurl}}/developer_guide/platform_integration_guides/web/in_app_messaging/#html-in-app-messages
[46]: #inapp-control
[47]: {% image_buster /assets/img_archive/In-App_Full.png %}
[48]: {% image_buster /assets/img_archive/In-App_Modal.png %}
[50]: https://github.com/carlsednaoui/ouibounce
[51]: {% image_buster /assets/img_archive/ios-html-full-iam.gif %}
[52]: {{site.baseurl}}/help/best_practices/in-app_messages/web_browsers_only/#web-html-messages

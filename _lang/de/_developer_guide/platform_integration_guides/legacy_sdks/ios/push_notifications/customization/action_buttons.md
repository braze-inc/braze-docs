---
nav_title: Aktions-Buttons
article_title: Push Action-Buttons für iOS
platform: iOS
page_order: 1
description: "In diesem Referenzartikel erfahren Sie, wie Sie Aktions-Buttons in Ihren iOS Push-Benachrichtigungen implementieren."
channel:
  - push

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Aktions-Buttons {#push-action-buttons-integration}

Das Braze iOS SDK unterstützt die standardmäßigen Push-Kategorien, einschließlich URLs für jeden Push-Action-Button. Die Standard-Kategorien verfügen derzeit über vier Sets von Push-Action-Buttons: `Accept`/`Decline`, `Yes`/`No`, `Confirm`/`Cancel`, und `More`. 

![Ein GIF einer Push-Nachricht, die nach unten gezogen wird, um zwei anpassbare Aktions-Buttons anzuzeigen.]({% image_buster /assets/img_archive/iOS8Action.gif %})

Um unsere Standard-Push-Kategorien zu registrieren, folgen Sie den Anweisungen zur Integration:

## Schritt 1: Hinzufügen von Braze Standard Push-Kategorien

Verwenden Sie den folgenden Code, um sich für unsere Standard Push-Kategorien zu registrieren, wenn Sie [sich für Push anmelden]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/integration/#step-4-register-push-tokens-with-braze):

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
// For UserNotification.framework (iOS 10+ only)
NSSet *appboyCategories = [ABKPushUtils getAppboyUNNotificationCategorySet];
[[UNUserNotificationCenter currentNotificationCenter] setNotificationCategories:appboyCategories];

// For UIUserNotificationSettings (before iOS 10)
NSSet *appboyCategories = [ABKPushUtils getAppboyUIUserNotificationCategorySet];
UIUserNotificationSettings *settings = [UIUserNotificationSettings settingsForTypes:UIUserNotificationTypeBadge
                                                                         categories:appboyCategories];
[[UIApplication sharedApplication] registerUserNotificationSettings:settings];
```

{% endtab %}
{% tab schnell %}

```swift
// For UserNotification.framework (iOS 10+ only)
let appboyCategories = ABKPushUtils.getAppboyUNNotificationCategorySet()
UNUserNotificationCenter.current().setNotificationCategories(appboyCategories)

// For UIUserNotificationSettings (before iOS 10)
let appboyCategories = ABKPushUtils.getAppboyUIUserNotificationCategorySet()
let settings = UIUserNotificationSettings.init(types: .badge, categories: appboyCategories)
UIApplication.shared.registerUserNotificationSettings(settings)
```

{% endtab %}
{% endtabs %}

Wenn Sie auf Push-Action-Buttons mit Hintergrundaktivierung klicken, wird nur die Benachrichtigung verworfen und die App nicht geöffnet. Wenn der Nutzer die App das nächste Mal öffnet, werden die Analytics für die Klicks auf diese Aktionen auf den Server übertragen.

Wenn Sie Ihre eigenen angepassten Benachrichtigungskategorien erstellen möchten, sehen Sie sich die [Anpassung der Aktions-Buttons an]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/customization/action_buttons/#push-category-customization).

## Schritt 2: Enablement der interaktiven Push-Bearbeitung

Wenn Sie das `UNNotification` Framework verwenden und Braze [Delegates]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/integration/#step-5-enable-push-handling) implementiert haben, sollten Sie diese Methode bereits integriert haben. 

Um den Umgang mit Push-Action-Buttons, einschließlich Click Analytics und URL-Routing, zu aktivieren, fügen Sie den folgenden Code in die Delegate-Methode Ihrer App `(void)userNotificationCenter:didReceiveNotificationResponse:withCompletionHandler:` ein:

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[[Appboy sharedInstance] userNotificationCenter:center
                           didReceiveNotificationResponse:response
                               withCompletionHandler:completionHandler];
```

{% endtab %}
{% tab schnell %}

```swift
Appboy.sharedInstance()?.userNotificationCenter(center,
                                                didReceive: response,
                                                withCompletionHandler: completionHandler)
```

{% endtab %}
{% endtabs %}

Wenn Sie das UNNotification Framework nicht verwenden, müssen Sie den folgenden Code in Ihre App `application:handleActionWithIdentifier:forRemoteNotification:completionHandler:` einfügen, um die Handhabung unserer Push-Action-Buttons zu aktivieren:

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[[Appboy sharedInstance] getActionWithIdentifier:identifier
                           forRemoteNotification:userInfo
                               completionHandler:completionHandler];
```

{% endtab %}
{% tab schnell %}

```swift
Appboy.sharedInstance()?.getActionWithIdentifier(identifier,
                                                 forRemoteNotification: userInfo,,
                                                 completionHandler: completionHandler)
```

{% endtab %}
{% endtabs %}

{% alert important %}
Wir empfehlen bei Verwendung von `handleActionWithIdentifier` dringend, mit dem `UNNotification`-Framework zu beginnen. Wir empfehlen dies aufgrund der Veralterung von [`handleActionWithIdentifier`](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1623068-application?language=objc).
{% endalert %}

## Anpassung der Push-Kategorie

Braze bietet nicht nur eine Reihe von [Standard Push-Kategorien]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/customization/action_buttons/), sondern unterstützt auch angepasste Benachrichtigungskategorien und Aktionen. Nachdem Sie Kategorien in Ihrer Anwendung registriert haben, können Sie das Braze-Dashboard verwenden, um Benachrichtigungskategorien an Ihre Nutzer:innen zu senden.

Wenn Sie nicht das `UserNotifications`-Framework verwenden, lesen Sie die Dokumentation zu den [alternativen Kategorien](https://developer.apple.com/documentation/usernotifications/unnotificationcategory).

Diese Kategorien können dann über unser Dashboard Push-Benachrichtigungen zugewiesen werden, um die Aktion-Button-Konfigurationen Ihres Designs zu triggern. Hier ist ein Beispiel, das die `LIKE_CATEGORY` nutzt, die auf dem Gerät angezeigt wird:

![Eine Push Nachricht, die zwei Push-Action-Buttons "unlike" und "like" anzeigt.]({% image_buster /assets/img_archive/push_example_category.png %})



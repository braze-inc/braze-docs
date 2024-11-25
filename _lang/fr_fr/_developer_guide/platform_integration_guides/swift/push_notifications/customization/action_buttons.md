---
nav_title: Boutons d’action
article_title: Boutons d’action push pour iOS
platform: Swift
page_order: 1
description: "Cet article explique comment implémenter des boutons d'action dans vos notifications push iOS pour le SDK Swift."
channel:
  - push

---

# Boutons d’action {#push-action-buttons-integration}

> Le SDK Braze Swift offre une prise en charge de la gestion des URL pour les boutons d'action push. 

Il existe quatre ensembles de boutons d'action par défaut pour les catégories de notification push par défaut de Braze : `Accept/Decline`, `Yes/No`, `Confirm/Cancel` et `More`. 

![GIF d'un message push tiré vers le bas pour afficher deux boutons d'action personnalisables.]({% image_buster /assets/img_archive/iOS8Action.gif %}){: style="max-width:60%"}

Si vous souhaitez créer vos propres catégories de notifications personnalisées, consultez la [personnalisation des boutons d'action](#push-category-customization).

## Intégration automatique (recommandé)

Lors de l'intégration de la notification push en utilisant l'option de configuration `configuration.push.automation`, Braze enregistre automatiquement les boutons d'action pour les catégories de notification push par défaut et gère les analyses de clics sur les boutons d'action de notification push ainsi que le routage des URL.

## Intégration manuelle

Pour activer manuellement ces boutons d'action push, enregistrez d'abord les catégories push par défaut. Ensuite, utilisez la méthode de délégué `didReceive(_:completionHandler:)` pour activer les boutons d'action push.

### Étape 1 : Ajout des catégories de notification push par défaut de Braze {#registering}

Utilisez le code suivant pour vous inscrire aux catégories push par défaut lorsque vous [vous inscrivez à push :]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/#step-4-register-push-tokens-with-braze)

{% tabs %}
{% tab swift %}

```swift
UNUserNotificationCenter.current().setNotificationCategories(Braze.Notifications.categories)
```

{% endtab %}
{% tab OBJECTIF-C %}

```objc
[[UNUserNotificationCenter currentNotificationCenter] setNotificationCategories:BRZNotifications.categories];
```

{% endtab %}
{% endtabs %}

{% alert note %}
Cliquer sur les boutons d’action push avec le mode d’activation en arrière-plan ne fera que rejeter la notification et n’ouvrira pas l’application. Lorsque l’utilisateur ouvrira à nouveau l’application, l’analyse de clics de bouton pour ces actions sera transmise au serveur.
{% endalert %}

### Étape 2 : Activer la gestion interactive des notifications push {#enable-push-handling}

Pour activer la gestion de notre bouton d'action push, y compris l'analyse des clics et le routage des URL, ajoutez le code suivant à la méthode de délégation de votre application `didReceive(_:completionHandler:)` :

{% tabs %}
{% tab swift %}

```swift
AppDelegate.braze?.notifications.handleUserNotification(response: response, withCompletionHandler: completionHandler)
```

{% endtab %}
{% tab OBJECTIF-C %}

```objc
[AppDelegate.braze.notifications handleUserNotificationWithResponse:response
                                              withCompletionHandler:completionHandler];
```

{% endtab %}
{% endtabs %}

Si vous utilisez le framework `UNNotification` et que vous avez implémenté les [méthodes de notification de]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/#step-5-enable-push-handling) Braze, vous devriez déjà avoir intégré cette méthode. 

## Personnalisation de la catégorie de notifications push

En plus de fournir un ensemble de catégories de push par défaut, Braze prend en charge les catégories et actions de notification personnalisées. Après avoir enregistré des catégories dans votre application, vous pouvez utiliser le tableau de bord Braze pour envoyer ces catégories de notification personnalisées à vos utilisateurs.

Ces catégories peuvent ensuite être affectées aux notifications push via notre tableau de bord pour déclencher les configurations des boutons d’action de votre conception. 

### Exemple de catégorie de notification personnalisée

Voici un exemple qui tire parti du `LIKE_CATEGORY` affiché sur l’appareil :

![Un message envoyant deux boutons d'action push "unlike" et "like".]({% image_buster /assets/img_archive/push_example_category.png %})

#### Étape 1 : Enregistrer une catégorie

Pour enregistrer une catégorie dans votre application, utilisez une approche similaire à la suivante :

{% tabs %}
{% tab swift %}

```swift
Braze.Notifications.categories.insert(
  .init(identifier: "LIKE_CATEGORY",
        actions: [
          .init(identifier: "LIKE_IDENTIFIER", title: "Like", options: [.foreground]),
          .init(identifier: "UNLIKE_IDENTIFIER", title: "Unlike", options: [.foreground])
        ],
        intentIdentifiers: []
       )
)
UNUserNotificationCenter.current().setNotificationCategories(Braze.Notifications.categories)
```

{% endtab %}
{% tab OBJECTIF-C %}

```objc
NSMutableSet<UNNotificationCategory *> *categories = [BRZNotifications.categories mutableCopy];

UNNotificationAction *likeAction = [UNNotificationAction actionWithIdentifier:@"LIKE_IDENTIFIER"
                                                                        title:@"Like"
                                                                      options:UNNotificationActionOptionForeground];

UNNotificationAction *unlikeAction = [UNNotificationAction actionWithIdentifier:@"UNLIKE_IDENTIFIER"
                                                                          title:@"Unlike"
                                                                        options:UNNotificationActionOptionForeground];

UNNotificationCategory *likeCategory = [UNNotificationCategory categoryWithIdentifier:@"LIKE_CATEGORY"
                                                                              actions:@[likeAction, unlikeAction]
                                                                    intentIdentifiers:@[]
                                                                              options:UNNotificationCategoryOptionNone];

[categories addObject:likeCategory];
[UNUserNotificationCenter.currentNotificationCenter setNotificationCategories:categories];
```

{% endtab %}
{% endtabs %}

{% alert note %}
Lorsque vous créez une `UNNotificationAction`, vous pouvez spécifier une liste d'options d'action. Par exemple, `UNNotificationActionOptions.foreground` permet à vos utilisateurs d'ouvrir votre application après avoir appuyé sur le bouton d'action. Ceci est nécessaire pour les comportements de navigation au clic, tels que « Ouvrir l'application » et « Lien profond dans l'application ». Pour plus d'informations, voir [`UNNotificationActionOptions`](https://developer.apple.com/documentation/usernotifications/unnotificationactionoptions).
{% endalert %}

#### Étape 2 : Sélectionnez vos catégories

Après avoir enregistré une catégorie, utilisez le tableau de bord Braze pour envoyer des notifications de ce type aux utilisateurs.

{% alert tip %}
Vous n'avez besoin de définir des catégories de notification personnalisées que pour les boutons d'action avec _actions spéciales_, telles que le lien profond dans votre application ou l'ouverture d'une URL. Vous n'avez pas besoin de les définir pour les boutons d'action qui ne font que rejeter une notification.
{% endalert %}

1. Dans le tableau de bord Braze, sélectionnez **Messagerie** > **Notifications Push**, puis choisissez votre [campagne push]({{site.baseurl}}/docs/user_guide/message_building_by_channel/push/creating_a_push_message) iOS.
2. Sous **Composer une notification push**, activez les **Boutons d'action**.
3. Dans le menu déroulant **Catégorie de notification iOS**, sélectionnez **Entrez la catégorie iOS personnalisée préenregistrée**.
4. Enfin, entrez l'une des catégories que vous avez créées plus tôt. L'exemple suivant utilise la catégorie personnalisée : `LIKE_CATEGORY`.

![Le tableau de bord de la campagne de notification push avec la configuration des catégories personnalisées.]({% image_buster /assets/img_archive/ios-notification-category.png %})


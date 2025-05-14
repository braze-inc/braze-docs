{% multi_lang_include developer_guide/prerequisites/swift.md %} Vous devrez également [configurer les notifications push]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift).

## Personnaliser les boutons d'action {#push-action-buttons-integration}

Le SDK Braze Swift offre une prise en charge de la gestion des URL pour les boutons d'action push. Il existe quatre ensembles de boutons d'action par défaut pour les catégories de notification push par défaut de Braze : `Accept/Decline`, `Yes/No`, `Confirm/Cancel` et `More`.

![GIF d'un message push tiré vers le bas pour afficher deux boutons d'action personnalisables.]({% image_buster /assets/img_archive/iOS8Action.gif %}){: style="max-width:60%"}

### Enregistrement manuel des boutons d'action

{% alert important %}
L'enregistrement manuel des boutons d'action push n'est pas recommandé.
{% endalert %}

Si vous configurez [les notifications push]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift) à l'aide de l'option de configuration `configuration.push.automation`, Braze enregistre automatiquement les boutons d'action pour les catégories de push par défaut et gère l'analyse/analytique des clics sur les boutons d'action push et le routage des URL.

Toutefois, vous pouvez choisir d'enregistrer manuellement les boutons d'action push à la place.

#### Étape 1 : Ajout des catégories de notification push par défaut de Braze {#registering}

Utilisez le code suivant pour vous inscrire aux catégories push par défaut lorsque vous [vous inscrivez à push :]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/#step-4-register-push-tokens-with-braze)

{% tabs %}
{% tab swift %}
a
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

#### Étape 2 : Activer la gestion interactive des notifications push {#enable-push-handling}

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

## Personnalisation des catégories de poussée {#customizing-push-categories}

En plus de fournir un ensemble de catégories de push par défaut, Braze prend en charge les catégories et actions de notification personnalisées. Après avoir enregistré des catégories dans votre application, vous pouvez utiliser le tableau de bord Braze pour envoyer ces catégories de notification personnalisées à vos utilisateurs.

Voici un exemple qui tire parti du `LIKE_CATEGORY` affiché sur l’appareil :

![Un message envoyant deux boutons d'action push "unlike" et "like".]({% image_buster /assets/img_archive/push_example_category.png %})

### Étape 1 : Enregistrer une catégorie

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

### Étape 2 : Sélectionnez vos catégories

Après avoir enregistré une catégorie, utilisez le tableau de bord Braze pour envoyer des notifications de ce type aux utilisateurs.

{% alert tip %}
Vous n'avez besoin de définir des catégories de notification personnalisées que pour les boutons d'action avec _actions spéciales_, telles que le lien profond dans votre application ou l'ouverture d'une URL. Vous n'avez pas besoin de les définir pour les boutons d'action qui ne font que rejeter une notification.
{% endalert %}

1. Dans le tableau de bord Braze, sélectionnez **Messagerie** > **Notifications Push**, puis choisissez votre [campagne push]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message) iOS.
2. Sous **Composer une notification push**, activez les **Boutons d'action**.
3. Dans le menu déroulant **Catégorie de notification iOS**, sélectionnez **Entrez la catégorie iOS personnalisée préenregistrée**.
4. Enfin, entrez l'une des catégories que vous avez créées plus tôt. L'exemple suivant utilise la catégorie personnalisée : `LIKE_CATEGORY`.

![Le tableau de bord de la campagne de notification push avec la configuration des catégories personnalisées.]({% image_buster /assets/img_archive/ios-notification-category.png %})

## Personnalisation des badges

Les badges sont de petites icônes idéales pour attirer l'attention d'un utilisateur. Vous pouvez spécifier un nombre de badges dans la rubrique [**Paramètres**]({{site.baseurl}}/developer_guide/push_notifications/customization/?sdktab=swift#swift_settings) lorsque vous composez une notification push à l'aide du tableau de bord de Braze. Vous pouvez également mettre à jour le nombre de badges manuellement par l'intermédiaire de la propriété [`applicationIconBadgeNumber`](https://developer.apple.com/library/ios/documentation/UIKit/Reference/UIApplication_Class/index.html#//apple_ref/occ/instp/UIApplication/applicationIconBadgeNumber) de votre application ou par le biais de la [notification à distance](https://developer.apple.com/library/content/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/CreatingtheNotificationPayload.html#//apple_ref/doc/uid/TP40008194-CH10-SW1). 

Braze efface automatiquement le décompte des badges lorsqu'une notification Braze est reçue alors que l'application est au premier plan. Le fait de régler manuellement le numéro de badge sur 0 permet également d'effacer les notifications dans le centre de notification. 

Si vous n’avez pas planifié une stratégie pour effacer les badges dans le cadre du fonctionnement normal de l’application ou en envoyant des notifications push qui effacent le badge, vous devez effacer le badge lorsque l’application devient active en ajoutant le code suivant à la méthode de délégation`applicationDidBecomeActive:` de votre application :

{% tabs %}
{% tab swift %}

```swift
// For iOS 16.0+
let center = UNUserNotificationCenter.current()
do {
  try await center.setBadgeCount(0)
} catch {
  // Handle errors
}

// Prior to iOS 16. Deprecated in iOS 17+.
UIApplication.shared.applicationIconBadgeNumber = 0
```

{% endtab %}
{% tab OBJECTIF-C %}

```objc
// For iOS 16.0+
UNUserNotificationCenter *center = [UNUserNotificationCenter currentNotificationCenter];
[center setBadgeCount:0 withCompletionHandler:^(NSError * _Nullable error) {
    if (error != nil) {
        // Handle errors
    }
}];

// Prior to iOS 16. Deprecated in iOS 17+.
[UIApplication sharedApplication].applicationIconBadgeNumber = 0;
```

{% endtab %}
{% endtabs %}

## Personnalisation des sons

### Étape 1 : Héberger le son dans votre application

Les sons de notification push personnalisés doivent être hébergés localement dans le bundle principal de votre application. Les formats de données audio suivants sont acceptés :

- Linear PCM
- MA4
- µLaw
- aLaw

Vous pouvez regrouper les données audio dans un fichier AIFF, WAV ou CAF. Dans Xcode, ajoutez le fichier audio à votre projet comme ressource non localisée du lot d’applications.

{% alert note %}
Les sons personnalisés doivent durer moins de 30 secondes lorsqu’ils sont joués. Si un son personnalisé dépasse cette limite, le son système par défaut est joué à la place.
{% endalert %}

#### Conversion de fichiers audio

Vous pouvez utiliser l'outil afconvert pour convertir les sons. Par exemple, pour convertir le système PCM linéaire 16 bits Submarine.aiff en audio IMA4 dans un fichier CAF, utilisez la commande suivante dans le terminal :

```bash
afconvert /System/Library/Sounds/Submarine.aiff ~/Desktop/sub.caf -d ima4 -f caff -v
```

{% alert tip %}
Vous pouvez inspecter un son pour déterminer son format de données en l'ouvrant dans QuickTime Player et en choisissant **Afficher l'inspecteur de film** dans le menu **Film.**
{% endalert %}

### Étape 2 : Fournissez une URL de protocole pour le son

Vous devez spécifier une URL de protocole qui dirige vers l'emplacement/localisation du fichier son dans votre application. Il existe deux méthodes pour ce faire :

* Utilisez le paramètre `sound` de l'[objet Apple push]({{site.baseurl}}/api/objects_filters/messaging/apple_object#apple-push-object) pour transmettre l'URL à Braze.
* Spécifiez l'URL dans le tableau de bord. Dans le [compositeur push]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/#step-3-select-notification-type-ios-and-android), sélectionnez **Paramètres** et saisissez l'URL du protocole dans le champ **Son.**  

![Le compositeur poussé dans le tableau de bord de Braze]({% image_buster /assets/img_archive/sound_push_ios.png %})

Si le fichier son spécifié n’existe pas ou si le mot-clé « default » est saisi, Braze utilisera le son d’alerte par défaut du appareil. En dehors de notre tableau de bord, le son peut également être configuré via notre [API d’envoi de messages][12].

Pour plus d'informations, consultez la documentation du développeur Apple concernant [la préparation de sons d'alerte personnalisés](https://developer.apple.com/library/content/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/SupportingNotificationsinYourApp.html).

## Paramètres

Lorsque vous créez une campagne push via le tableau de bord, cliquez sur l'onglet **Paramètres** à l'étape **Composer** pour afficher les paramètres avancés disponibles.

![]({% image_buster /assets/img_archive/ios_advanced_settings.png %})

### Paires clé-valeur

Braze vous permet d’envoyer des paires clé-valeur définies de manière personnalisée sous forme de chaînes de caractères, appelées `extras`, ainsi qu’une notification push à votre application. Des éléments supplémentaires peuvent être définis via le tableau de bord ou l’API et seront disponibles en tant que paires clé-valeur dans le dictionnaire `notification` transmis à vos implémentations de délégué de notification push.

### Options d’alerte

Sélectionnez la case à cocher **Options d'alerte** pour voir une liste déroulante des paires clé-valeur disponibles pour ajuster l'apparence de la notification sur les appareils.

### Ajouter un indicateur de contenu disponible

Cochez la case **Ajouter un indicateur de contenu disponible** pour indiquer aux appareils de télécharger le nouveau contenu en arrière-plan. Le plus souvent, vous pouvez cocher cette case si vous souhaitez envoyer des [notifications silencieuses]({{site.baseurl}}/developer_guide/push_notifications/silent/?sdktab=swift).

### Ajouter un indicateur de contenu mutable

Cochez la case **Ajouter un indicateur de contenu mutable** pour activer la personnalisation avancée du récepteur. Cet indicateur sera automatiquement envoyé lors de la composition d'une [notification enrichie]({{site.baseurl}}/developer_guide/push_notifications/rich/?sdktab=swift), quelle que soit la valeur de cette case à cocher.

### ID de réduction

Spécifiez un ID de réduction pour fusionner les notifications similaires. Si vous envoyez plusieurs notifications avec le même ID de réduction, l’appareil affichera uniquement la notification la plus récemment reçue. Reportez-vous à la documentation d'Apple sur les [notifications groupées](https://developer.apple.com/library/content/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/APNSOverview.html#//apple_ref/doc/uid/TP40008194-CH8-SW1).

### Expiration

Cocher la case **Expiration** permettra de définir une durée d'expiration pour votre message. Si l’appareil d’un utilisateur perd sa connexion, Braze continuera d’essayer d’envoyer le message jusqu’à l’heure spécifiée. Si cette option n’est pas définie, la plateforme établit par défaut un délai d’expiration de 30 jours. Notez que les notifications push expirant avant la livraison ne sont pas considérées comme ayant échoué et ne seront pas enregistrées comme une non-remise.

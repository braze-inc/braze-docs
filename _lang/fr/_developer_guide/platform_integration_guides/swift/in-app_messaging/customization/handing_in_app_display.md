---
hidden: true
nav_title: Gestion des affichages personnalisés
article_title: Personnalisation de la gestion des affichages de messages in-app pour iOS
platform: iOS
page_order: 4
description: "Cet article de référence couvre la gestion de l’affichage personnalisé de la messagerie dans l’application pour votre application iOS."
channel:
  - messages In-App

---

# Gestion personnalisée de l’affichage des messages in-app

Lorsque le [`ABKInAppMessageControllerDelegate`][16] est défini, la méthode de délégation suivante sera appelée avant que les messages in-app ne soient affichés :

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
- (ABKInAppMessageDisplayChoice) beforeInAppMessageDisplayed:(ABKInAppMessage *)inAppMessage;
```

{% endtab %}
{% tab swift %}

```swift
func beforeInAppMessageDisplayed(inAppMessage: ABKInAppMessage!) -> ABKInAppMessageDisplayChoice
```

{% endtab %}
{% endtabs %}

Si vous n’avez implémenté que [`ABKInAppMessageUIDelegate`][34], la méthode de délégation de l’IU suivante sera appelée plutôt :

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
- (ABKInAppMessageDisplayChoice) beforeInAppMessageDisplayed:(ABKInAppMessage *)inAppMessage withKeyboardIsUp:(BOOL)keyboardIsUp;
```

{% endtab %}
{% tab swift %}

```swift
func beforeInAppMessageDisplayed(inAppMessage: ABKInAppMessage!, withKeyboardIsUp keyboardIsUp: Bool) -> ABKInAppMessageDisplayChoice
```

{% endtab %}
{% endtabs %}

Vous pouvez personnaliser la gestion des messages in-app en implémentant cette méthode de délégation et en renvoyant l’une des valeurs suivantes pour `ABKInAppMessageDisplayChoice` :

| `ABKInAppMessageDisplayChoice` | Comportement |
| -------------------------- | -------- |
| Objectif-C : `ABKDisplayInAppMessageNow`<br>Swift : `displayInAppMessageNow` | Le message s’affichera immédiatement |
| Objectif-C : `ABKDisplayInAppMessageLater`<br>Swift : `displayInAppMessageLater` | Le message ne s’affichera pas et sera replacé sur le dessus de la pile. |
| Objectif-C : `ABKDiscardInAppMessage`<br>Swift : `discardInAppMessage`| Le message sera supprimé et ne sera pas affiché. |
{: .reset-td-br-1 .reset-td-br-2}

Vous pouvez utiliser la méthode de délégation `beforeInAppMessageDisplayed:` pour ajouter une logique d’affichage des messages in-app, personnaliser les messages in-app avant que Braze ne les affiche, ou désactiver la logique d’affichage des messages in-app et l’interface utilisateur de Braze.

Consultez [notre exemple d’application][36] pour un exemple d’implémentation.

## Remplacer les messages in-app avant l’affichage

Si vous souhaitez modifier le comportement d’affichage des messages in-app, vous devez ajouter toutes les logiques d’affichage nécessaires à votre méthode de délégation `beforeInAppMessageDisplayed:`. Par exemple, vous pouvez afficher le message in-app en haut de l’écran si le clavier est actuellement affiché, ou prendre le modèle de données de message in-app et afficher vous-même le message in-app.

Si la campagne de messages in-app ne s’affiche pas lorsque la session a été lancée, assurez-vous que la logique d’affichage nécessaire soit ajoutée à votre méthode de délégation `beforeInAppMessageDisplayed:`. Cela permet à la campagne de messages in-app d’afficher en haut de l’écran même si le clavier est affiché.

## Masquer la barre d’état pendant l’affichage

Pour les messages `Full` et `HTML` dans l’application, le SDK tentera par défaut de placer le message sur la barre d’état. Cependant, dans certains cas, la barre d’état peut toujours apparaître en haut du message in-app. À partir de la version [3.21.1](https://github.com/Appboy/appboy-ios-sdk/blob/master/CHANGELOG.md#3211) du SDK iOS, vous pouvez forcer à masquer la barre d’état lors de l’affichage des messages in-app `Full` et `HTML` en paramétrant `ABKInAppMessageHideStatusBarKey` sur `YES` dans le `appboyOptions` transmis à `startWithApiKey:`.

## Enregistrement des impressions et des clics

La journalisation des impressions et des clics de message in-app n’est pas automatique lorsque vous implémentez une gestion entièrement personnalisée (c.-à-d. que vous contournez l’affichage du message in-app de Braze en renvoyant `ABKDiscardInAppMessage` dans votre `beforeInAppMessageDisplayed:`). Si vous choisissez d’implémenter votre propre interface utilisateur à l’aide de nos modèles de messages in-app, vous devez enregistrer les analytiques avec les méthodes suivantes sur la classe `ABKInAppMessage` :

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
// Registers that a user has viewed an in-app message with the Braze server.
- (void) logInAppMessageImpression;
// Registers that a user has clicked on an in-app message with the Braze server.
- (void) logInAppMessageClicked;
```

{% endtab %}
{% tab swift %}

```swift
// Registers that a user has viewed an in-app message with the Braze server.
func logInAppMessageImpression()
// Registers that a user has clicked on an in-app message with the Braze server.
func logInAppMessageClicked()
```

{% endtab %}
{% endtabs %}

De plus, vous devriez consigner les clics sur les boutons des sous-classes de`ABKInAppMessageImmersive` (*c.-à-d.*, messages in-app `Modal` et `Full`) :

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
// Logs button click analytics
- (void)logInAppMessageClickedWithButtonID:(NSInteger)buttonID;
```

{% endtab %}
{% tab swift %}

```swift
// Logs button click analytics
func logInAppMessageClickedWithButtonID(buttonId: NSInteger)
```

{% endtab %}
{% endtabs %}

## Déclarations de méthode

Pour plus d’informations, voir les fichiers d’en-tête suivants :

- [`ABKInAppMessage.h`][14]
- [`ABKInAppMessageControllerDelegate.h`][16]

## Exemples d’implémentation

Voir l’exemple d’application de message in-app [`AppDelegate.m`][36].


[16]: https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/ABKInAppMessageControllerDelegate.h
[36]: https://github.com/Appboy/appboy-ios-sdk/blob/master/Samples/InAppMessage/BrazeInAppMessageSample/BrazeInAppMessageSample/AppDelegate.m
[34]: https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyUI/ABKInAppMessage/ABKInAppMessageUIDelegate.h
[14]: https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/ABKInAppMessage.h


---
nav_title: Gestion des affichages personnalisés
article_title: Personnalisation de la gestion des affichages de messages in-app pour iOS
platform: iOS
page_order: 4
description: "Cet article de référence couvre la gestion de l’affichage personnalisé de la messagerie dans l’application pour votre application iOS."
channel:
  - in-app messages

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Gestion personnalisée de l’affichage des messages in-app

Lorsque l'option [`ABKInAppMessageControllerDelegate`](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/ABKInAppMessageControllerDelegate.h) est définie, la méthode de délégation suivante sera appelée avant l'affichage des messages in-app :

{% tabs %}
{% tab OBJECTIF-C %}

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

Si vous n'avez implémenté que [`ABKInAppMessageUIDelegate`](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyUI/ABKInAppMessage/ABKInAppMessageUIDelegate.h)la méthode suivante du délégué de l'interface utilisateur sera appelée à la place :

{% tabs %}
{% tab OBJECTIF-C %}

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
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Vous pouvez utiliser la méthode de délégation `beforeInAppMessageDisplayed:` pour ajouter une logique d'affichage des messages in-app, personnaliser les messages in-app avant qu'ils ne soient affichés par Braze, ou vous désengager complètement de la logique d'affichage des messages in-app et de l'interface utilisateur de Braze.

Consultez notre [exemple d'application](https://github.com/Appboy/appboy-ios-sdk/blob/master/Samples/InAppMessage/BrazeInAppMessageSample/BrazeInAppMessageSample/AppDelegate.m) pour un exemple de mise en œuvre.

## Remplacer les messages in-app avant l’affichage

Si vous souhaitez modifier le comportement d'affichage des messages in-app, vous devez ajouter toute logique d'affichage nécessaire à votre méthode de délégation `beforeInAppMessageDisplayed:`. Par exemple, vous pouvez afficher le message in-app en haut de l’écran si le clavier est actuellement affiché, ou prendre le modèle de données de message in-app et afficher vous-même le message in-app.

Si la campagne de messages in-app ne s’affiche pas lorsque la session a été lancée, assurez-vous que la logique d’affichage nécessaire soit ajoutée à votre méthode de délégation `beforeInAppMessageDisplayed:`. Cela permet à la campagne de messages in-app d’afficher en haut de l’écran même si le clavier est affiché.

## Désactivation du mode sombre

Pour empêcher les messages in-app d'adopter le style du mode sombre lorsque l'appareil de l'utilisateur a activé le mode sombre, utilisez la propriété [`ABKInAppMessage.enableDarkTheme`](https://appboy.github.io/appboy-ios-sdk/docs/interface_a_b_k_in_app_message.html#ae89df6090bed623099ab0ecc0a74ad5d). Depuis la méthode `ABKInAppMessageControllerDelegate.beforeInAppMessageDisplayed:` ou la méthode `ABKInAppMessageUIDelegate.beforeInAppMessageDisplayed:`, définissez la propriété `enableDarkTheme` du paramètre `inAppMessage` de la méthode sur `NO`.

{% tabs %}
{% tab OBJECTIF-C %}

```objc
// ABKInAppMessageControllerDelegate
- (ABKInAppMessageDisplayChoice)beforeInAppMessageDisplayed:(ABKInAppMessage *)inAppMessage {
  ...
  inAppMessage.enableDarkTheme = NO;
  ...
  return ABKDisplayInAppMessageNow;
}

// ABKInAppMessageUIDelegate
- (ABKInAppMessageDisplayChoice)beforeInAppMesssageDisplayed:(ABKInAppMessage *)inAppMessage
                                            withKeyboardIsUp:(BOOL)keyboardIsUp {
  ...
  inAppMessage.enableDarkTheme = NO;
  ...
  return ABKDisplayInAppMessageNow;
}
```

{% endtab %}
{% tab swift %}

```swift
// ABKInAppMessageControllerDelegate
func before(inAppMessageDisplayed inAppMessage: ABKInAppMessage) -> ABKInAppMessageDisplayChoice {
  ...
  inAppMessage.enableDarkTheme = false
  ...
  return ABKInAppMessageDisplayChoice.displayInAppMessageNow
}

// ABKInAppMessageUIDelegate
func before(inAppMessageDisplayed inAppMessage: ABKInAppMessage, withKeyboardIsUp keyboardIsUp: Bool) -> ABKInAppMessageDisplayChoice {
  ...
  inAppMessage.enableDarkTheme = false
  ...
  return ABKInAppMessageDisplayChoice.displayInAppMessageNow
}
```

{% endtab %}
{% endtabs %}

## Masquer la barre d’état pendant l’affichage

Pour les messages `Full` et `HTML` dans l’application, le SDK tentera par défaut de placer le message sur la barre d’état. Cependant, dans certains cas, la barre d’état peut toujours apparaître en haut du message in-app. À partir de la version [3.21.1](https://github.com/Appboy/appboy-ios-sdk/blob/master/CHANGELOG.md#3211) du SDK iOS, vous pouvez forcer le masquage de la barre d'état lors de l'affichage des messages in-app `Full` et `HTML` en définissant `ABKInAppMessageHideStatusBarKey` sur `YES` dans les `appboyOptions` transmises à `startWithApiKey:`.

## Enregistrement des impressions et des clics

L’enregistrement des impressions et des clics de messages in-app n’est pas automatique lorsque vous implémentez une gestion entièrement personnalisée (c.-à-d. que vous contournez l’affichage des messages in-app de Braze en renvoyant `ABKDiscardInAppMessage` dans votre `beforeInAppMessageDisplayed:`). Si vous choisissez de déployer votre propre interface utilisateur à l’aide de nos modèles de messages in-app, vous devez enregistrer les analyses à l'aide des méthodes suivantes sur la classe `ABKInAppMessage` :

{% tabs %}
{% tab OBJECTIF-C %}

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

De plus, vous devriez enregistrer les clics sur les boutons des sous-classes de `ABKInAppMessageImmersive` (*i.e*., messages in-app `Modal` et `Full`) :

{% tabs %}
{% tab OBJECTIF-C %}

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

- [`ABKInAppMessage.h`](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/ABKInAppMessage.h)
- [`ABKInAppMessageControllerDelegate.h`](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/ABKInAppMessageControllerDelegate.h)

## Exemples d’implémentation

Voir l’exemple d’application de messages in-app [`AppDelegate.m`](https://github.com/Appboy/appboy-ios-sdk/blob/master/Samples/InAppMessage/BrazeInAppMessageSample/BrazeInAppMessageSample/AppDelegate.m).




---
nav_title: Comportement du clic personnalisé
article_title: Personnalisation du comportement lors du clic sur les messages in-app pour iOS
platform: Swift
page_order: 5
description: "Cet article de référence porte sur la personnalisation du comportement lors du clic sur les messages in-app pour iOS dans le cadre du SDK Swift."
channel:
  - in-app messages
---

# Comportement personnalisé en cas de clic

> Chaque objet `Braze.InAppMessage` contient une [`ClickAction`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage/clickaction) correspondante qui définit le comportement en cas de clic. 

Pour personnaliser ce comportement, vous pouvez modifier la propriété `clickAction` en vous référant à l'exemple suivant :

{% tabs %}
{% tab swift %}

```swift
func inAppMessage(
  _ ui: BrazeInAppMessageUI, 
  prepareWith context: inout BrazeInAppMessageUI.PresentationContext
) {
  if let newUrl = URL(string: "{your-url}") {
    context.message.clickAction = .url(newUrl, useWebView: true)
  }
}
```

{% endtab %}
{% tab OBJECTIF-C %}

La méthode `inAppMessage(_:prepareWith:)` n'est pas disponible en Objective-C.

{% endtab %}
{% endtabs %}

## Cliquez sur les types d'action

La propriété `clickAction` de votre `Braze.InAppMessage` est par défaut `.none` mais peut être définie sur l'une des valeurs suivantes :

| `ClickAction` | Comportement au clic |
| -------------------------- | -------- |
| `.url(URL, useWebView: Bool)` | Ouvre l'URL donné dans un navigateur externe. Si `useWebView` est définie sur `true`, elle s'ouvrira dans une vue Web. |
| `.newsFeed` | Le fil d’actualité s’affiche lorsque l’on clique sur le message, et le message est rejeté.<br><br>**Remarque :** Le fil d'actualité est supprimé. Consultez le [guide de migration]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/migrating_from_news_feed/) pour plus de détails. |
| `.none` | Le message sera rejeté lorsque vous cliquerez. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert important %}
Pour les messages in-app contenant des boutons, le message `clickAction` sera également inclus dans la charge utile finale si l'action de clic est ajoutée avant l'ajout du texte du bouton.
{% endalert %}

## Personnalisation des messages in-app et des clics sur les boutons

La méthode de délégation [`BrazeInAppMessageUIDelegate`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate) suivante est appelée en cas de clic sur un message in-app. Pour les clics sur les boutons de messages in-app et les boutons de messages in-app HTML (liens), un ID de bouton est fourni en tant que paramètre facultatif.

{% tabs %}
{% tab swift %}

```swift
func inAppMessage(
  _ ui: BrazeInAppMessageUI,
  shouldProcess clickAction: Braze.InAppMessage.ClickAction,
  buttonId: String?,
  message: Braze.InAppMessage,
  view: InAppMessageView
) -> Bool
```

{% endtab %}
{% tab OBJECTIF-C %}

```objc
- (BOOL)inAppMessage:(BrazeInAppMessageUI *)ui
       shouldProcess:(enum BRZInAppMessageRawClickAction)clickAction
                 url:(NSURL *)uri
            buttonId:(NSString *)buttonId
             message:(BRZInAppMessageRaw *)message
                view:(UIView *)view;
```

{% endtab %}
{% endtabs %}

Cette méthode renvoie une valeur booléenne indiquant si Braze doit continuer à exécuter l'action de clic.


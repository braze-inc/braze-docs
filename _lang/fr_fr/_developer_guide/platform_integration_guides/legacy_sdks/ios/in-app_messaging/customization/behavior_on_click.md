---
nav_title: Comportement du clic personnalisé
article_title: Personnaliser le comportement des messages in-app au clic pour iOS
platform: iOS
page_order: 5
description: "Cet article de référence couvre le comportement au clic personnalisé du message in-app pour votre application iOS."
channel:
  - in-app messages
noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Personnaliser le comportement au clic du message in-app

{% alert note %}
Cet article comprend des informations sur les fils d’actualité, qui deviennent obsolètes. Braze recommande aux clients qui utilisent notre outil de fil d’actualités de passer à notre canal de communication de cartes de contenu : il est plus flexible, plus personnalisable et plus fiable. Consultez le [guide de migration]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/migrating_from_news_feed/) pour en savoir plus.
{% endalert %}

La propriété de `inAppMessageClickActionType` sur le `ABKInAppMessage` définit le comportement d’action après avoir cliqué sur le message in-app. Cette propriété est en lecture seule. Si vous souhaitez modifier le comportement de clic du message in-app, vous pouvez employer la méthode suivante sur `ABKInAppMessage` :

{% tabs %}
{% tab OBJECTIF-C %}

```objc
[inAppMessage setInAppMessageClickAction:clickActionType withURI:uri];
```

{% endtab %}
{% tab swift %}

```swift
inAppMessage.setInAppMessageClickAction(clickActionType: clickActionType, withURI: uri)
```

{% endtab %}
{% endtabs %}

Le `inAppMessageClickActionType` peut être défini sur l’une des valeurs suivantes :

| `ABKInAppMessageClickActionType` | Comportement au clic |
| -------------------------- | -------- |
| `ABKInAppMessageDisplayNewsFeed` | Le fil d’actualité s’affiche lorsque l’on clique sur le message, et le message est rejeté. Notez que le paramètre `uri` sera ignoré, et la propriété `uri` sur le `ABKInAppMessage` sera définie sur nul. |
| `ABKInAppMessageRedirectToURI` | L’URI donné s’affiche lorsque l’on clique sur le message, et le message est rejeté. Notez que le paramètre `uri` ne peut pas être nul. |
| `ABKInAppMessageNoneClickAction` | Le message sera rejeté lorsque vous cliquerez. Notez que le paramètre `uri` sera ignoré, et la propriété `uri` sur le `ABKInAppMessage` sera définie sur nul. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert important %}
Pour les messages in-app contenant des boutons, le message `clickAction` sera également inclus dans la charge utile finale si l'action de clic est ajoutée avant l'ajout du texte du bouton.
{% endalert %}

## Personnaliser les clics sur le corps du message in-app

La méthode de délégation [`ABKInAppMessageUIDelegate`](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyUI/ABKInAppMessage/ABKInAppMessageUIDelegate.h) suivante est appelée lorsque l’on clique sur un message in-app :

{% tabs %}
{% tab OBJECTIF-C %}

```objc
- (BOOL) onInAppMessageClicked:(ABKInAppMessage *)inAppMessage;
```

{% endtab %}
{% tab swift %}

```swift
func onInAppMessageClicked(inAppMessage: ABKInAppMessage!) -> Bool
```

{% endtab %}
{% endtabs %}

## Personnaliser les clics sur le bouton du message in-app

Pour les clics sur les boutons de message in-app et les boutons de message in-app HTML (par exemple, des liens), [`ABKInAppMessageUIDelegate`](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyUI/ABKInAppMessage/ABKInAppMessageUIDelegate.h) inclut les méthodes de délégation suivantes :

{% tabs %}
{% tab OBJECTIF-C %}

```objc
- (BOOL)onInAppMessageButtonClicked:(ABKInAppMessageImmersive *)inAppMessage
                             button:(ABKInAppMessageButton *)button;

- (BOOL)onInAppMessageHTMLButtonClicked:(ABKInAppMessageHTML *)inAppMessage
                             clickedURL:(nullable NSURL *)clickedURL
                               buttonID:(NSString *)buttonID;
```

{% endtab %}
{% tab swift %}

```swift
func onInAppMessageButtonClicked(inAppMessage: ABKInAppMessageImmersive!,
                                 button: ABKInAppMessageButton) -> Bool

func onInAppMessageHTMLButtonClicked(inAppMessage: ABKInAppMessageHTML!,
                                     clickedURL: URL, buttonID: String) -> Bool
```

{% endtab %}
{% endtabs %}

Chaque méthode renvoie une valeur `BOOL` pour indiquer si Braze doit continuer à exécuter l’action de clic.

Pour accéder au type d’action du clic d’un bouton dans une méthode de délégation, vous pouvez utiliser le code suivant :

{% tabs %}
{% tab OBJECTIF-C %}

```objc
if ([inAppMessage isKindOfClass:[ABKInAppMessageImmersive class]]) {
      ABKInAppMessageImmersive *immersiveIAM = (ABKInAppMessageImmersive *)inAppMessage;
      NSArray<ABKInAppMessageButton *> *buttons = immersiveIAM.buttons;
      for (ABKInAppMessageButton *button in buttons) {
         // Button action type is accessible via button.buttonClickActionType
      }
   }
```

{% endtab %}
{% tab swift %}

```swift
if inAppMessage is ABKInAppMessageImmersive {
      let immersiveIAM = inAppMessage as! ABKInAppMessageImmersive;
      for button in inAppMessage.buttons as! [ABKInAppMessageButton]{
        // Button action type is accessible via button.buttonClickActionType
      }
    }
```

{% endtab %}
{% endtabs %}

Lorsqu’un message in-app comporte des boutons, les seules actions de clic qui seront exécutées sont celles du modèle `ABKInAppMessageButton`. Le corps du message in-app ne sera pas cliquable même si le modèle `ABKInAppMessage` aura l’action de clic par défaut (« News Feed ») affectée.

## Déclarations de méthode

Pour plus d’informations, voir les fichiers d’en-tête suivants :

- [`ABKInAppMessage.h`](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/ABKInAppMessage.h)


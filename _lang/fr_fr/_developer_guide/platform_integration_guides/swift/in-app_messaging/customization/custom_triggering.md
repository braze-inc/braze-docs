---
nav_title: Déclenchement personnalisé
article_title: Personnaliser la fonction de déclenchement de message in-app pour iOS
platform: Swift
page_order: 6
description: "Cet article de référence traite du déclenchement personnalisé des messages in-app d'iOS pour le SDK Swift."
channel:
  - in-app messages
---

# Déclenchement personnalisé

> Par défaut, les messages in-app sont déclenchés par des événements enregistrés par le SDK. Vous pouvez également déclencher des messages in-app par des événements envoyés par le serveur.

Pour déclencher des messages in-app à l'aide d'événements côté serveur, envoyez une notification push silencieuse à l'appareil pour lui permettre d'enregistrer un événement basé sur le SDK. Cet événement SDK peut ensuite déclencher le message in-app destiné à l'utilisateur.

## Étape 1 : Gérer les paires clé-valeur et les notifications push silencieuses

Implémentez la fonction suivante et appelez-la dans la méthode [`application(_:didReceiveRemoteNotification:fetchCompletionHandler:)`](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1623013-application/) :

{% tabs %}
{% tab swift %}

```swift
func handleExtras(userInfo: [AnyHashable : Any]) {
  print("A push was received")
  if userInfo != nil && (userInfo["IS_SERVER_EVENT"] as? String) != nil && (userInfo["CAMPAIGN_NAME"] as? String) != nil {
    AppDelegate.braze?.logCustomEvent("IAM Trigger", properties: ["campaign_name": userInfo["CAMPAIGN_NAME"]])
  }
}
```

{% endtab %}
{% tab OBJECTIF-C %}

```objc
- (void)handleExtrasFromPush:(NSDictionary *)userInfo {
  NSLog(@"A push was received.");
  if (userInfo !=nil && userInfo[@"IS_SERVER_EVENT"] !=nil && userInfo[@"CAMPAIGN_NAME"]!=nil) {
    [AppDelegate.braze logCustomEvent:@"IAM Trigger" properties:@{@"campaign_name": userInfo[@"CAMPAIGN_NAME"]}];
  }
};
```

{% endtab %}
{% endtabs %}

Lorsque la notification push silencieuse est reçue, un événement enregistré par le SDK « in-app message trigger » sera enregistré par rapport au profil utilisateur. 

{% alert important %}
En raison d’un message push utilisé pour enregistrer un événement personnalisé, Braze devra stocker un jeton de notification push pour chaque utilisateur afin de permettre cette solution. Pour les utilisateurs d’iOS, Braze ne stocke un jeton qu’à partir du point où un utilisateur a été invité à l’invite de notification push de l’iOS. Avant cela, l’utilisateur ne sera pas joignable par notification push, et la solution précédente ne sera pas possible.
{% endalert %}

## Étape 2 : Créez une campagne de push silencieuse

Créez une [campagne de push silencieuse]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/silent_push_notifications/) déclenchée par l'événement envoyé par le serveur. 

![Une campagne de messages in-app de livraison par action qui sera délivrée aux utilisateurs dont les profils utilisateurs ont l'événement personnalisé "server_event".]({% image_buster /assets/img_archive/iosServerSentPush.png %})

La campagne de notification push doit inclure des extras de paires clé-valeur, qui indiquent que cette campagne de notification push est envoyée pour enregistrer un événement personnalisé SDK. Cet événement sera utilisé pour déclencher le message in-app.

![Une campagne de messages in-app de réception/distribution basée sur des actions qui comporte deux paires clé-valeur. "CAMPAIGN_NAME" devient "Exemple de nom de message in-app" et IS_SERVER_EVENT" devient "true".]({% image_buster /assets/img_archive/iOSServerPush.png %})

Le code de la méthode `application(_:didReceiveRemoteNotification:fetchCompletionHandler:)` vérifie la clé `IS_SERVER_EVENT` et enregistrera un événement personnalisé SDK s’il existe.

Vous pouvez modifier le nom de l’événement ou les propriétés d’événement en envoyant la valeur souhaitée dans les options de paires clé-valeur de la charge utile de notification push. Lors de la journalisation de l’événement personnalisé, ces extras peuvent être utilisés comme paramètre du nom de l’événement ou comme propriété de l’événement.

## Étape 3 : Créer une campagne de communication in-app

Créez votre campagne de messages in-app visibles par l'utilisateur dans le tableau de bord de Braze. Cette campagne doit avoir une livraison par événement et être déclenchée par l’événement personnalisé enregistré à partir de la méthode `application(_:didReceiveRemoteNotification:fetchCompletionHandler:)`.

Dans l’exemple suivant, le message in-app spécifique à déclencher a été configuré en envoyant la propriété de l’événement dans le cadre de la première notification push silencieuse.

![Une campagne de messages in-app basée sur une action qui sera délivrée aux utilisateurs qui effectuent l'événement personnalisé "In-app message trigger" où "campaign_name" est égal à "IAM Campaign Name Example".]({% image_buster /assets/img_archive/iosIAMeventTrigger.png %})

{% alert note %}
Notez que ces messages in-app ne se déclencheront que si la notification push silencieuse est reçue pendant que l’application se trouve au premier plan.
{% endalert %}


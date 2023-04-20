---
hidden: true
nav_title: Déclenchement personnalisé
article_title: Personnaliser la fonction de déclenchement de message in-app pour iOS
platform: iOS
page_order: 7
description: "Cet article de référence couvre le déclenchement de messagerie in-app personnalisée pour votre application iOS."
channel:
  - messages In-App
---

# Déclenchement personnalisé de messages in-app

Par défaut, les messages in-app sont déclenchés par des types d’événements enregistrés par le SDK. Si vous souhaitez déclencher des messages in-app par des événements envoyés par le serveur, vous pouvez également y parvenir.

Pour activer cette fonction, vous enverrez une notification push silencieuse au périphérique, ce qui lui permet de consigner un événement basé sur un SDK. Cet événement SDK déclencherait ensuite le message in-app orienté utilisateur.

## Étape 1 : Gérer les paires clé-valeur et les notifications push silencieuses

Ajoutez le code suivant à la méthode `application(_:didReceiveRemoteNotification:fetchCompletionHandler:)` :

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
- (void)handleExtrasFromPush:(NSDictionary *)userInfo {
  NSLog(@"A push was received.");
  if (userInfo !=nil && userInfo[@"IS_SERVER_EVENT"] !=nil && userInfo[@"CAMPAIGN_NAME"]!=nil) {
    [[Appboy sharedInstance] logCustomEvent:@"IAM Trigger" withProperties:@{@"campaign_name": userInfo[@"CAMPAIGN_NAME"]}];
  }
 };
```

{% endtab %}
{% tab swift %}

```swift
func handleExtras(userInfo: [AnyHashable : Any]) {
  NSLog("A push was received");
  if userInfo != nil && (userInfo["IS_SERVER_EVENT"] as? String) != nil && (userInfo["CAMPAIGN_NAME"] as? String) != nil {
    Appboy.sharedInstance()?.logCustomEvent("IAM Trigger", withProperties: ["campaign_name": userInfo["CAMPAIGN_NAME"]])
  }
}
```

{% endtab %}
{% endtabs %}

Lorsque la notification push silencieuse est reçue, un événement enregistré par le SDK « in-app message trigger » sera enregistré par rapport au profil utilisateur. Notez que ces messages in-app ne se déclencheront que si la notification push silencieuse est reçue pendant que l’application se trouve au premier plan.

## Étape 2 : Créer une campagne de notification push

Créer une campagne de notification push silencieuse déclenchée par l’événement envoyé par le serveur. Pour plus de détails sur la création d’une campagne de notification push silencieuse, reportez-vous à [notifications push silencieuses][39].

![Une campagne de messages in-app de livraison par événement sera envoyée aux utilisateurs qui exécutent l’événement personnalisé « server_event ».][40]

La campagne de notification push doit inclure des extras de paires clé-valeur, qui indiquent que cette campagne de notification push est envoyée pour enregistrer un événement personnalisé SDK. Cet événement sera utilisé pour déclencher le message in-app.

![Une campagne de messages in-app à livraison par événement qui a deux paires clé-valeur. "CAMPAIGN_NAME" défini comme « Exemple de nom de message in-app » et "IS_SERVER_EVENT" défini sur « true ».][41]

Le code de la méthode `application(_:didReceiveRemoteNotification:fetchCompletionHandler:)` vérifie la clé `IS_SERVER_EVENT` et enregistrera un événement personnalisé SDK s’il existe.

Vous pouvez modifier le nom de l’événement ou les propriétés d’événement en envoyant la valeur souhaitée dans les options de paires clé-valeur de la charge utile de notification push. Lors de la journalisation de l’événement personnalisé, ces extras peuvent être utilisés comme paramètre du nom de l’événement ou comme propriété de l’événement.

## Étape 3 : Créer une campagne de communication In-App

Créez votre campagne de messages in-app visibles par l’utilisateur dans le tableau de bord de Braze. Cette campagne doit avoir une livraison par événement et être déclenchée par l’événement personnalisé enregistré à partir de la méthode `application(_:didReceiveRemoteNotification:fetchCompletionHandler:)`.

Dans l’exemple suivant, le message in-app spécifique à déclencher a été configuré en envoyant la propriété de l’événement dans le cadre de la première notification push silencieuse.

![Une campagne de messages in-app à livraison par événement sera envoyée aux utilisateurs qui exécutent l’événement personnalisé « déclenchement de message in-app » où « campaign_name » correspond à « exemple de nom de message in-app ».][42]

En raison d’un message push utilisé pour enregistrer un événement personnalisé, Braze devra stocker un jeton de notification push pour chaque utilisateur afin de permettre cette solution. Pour les utilisateurs d’iOS, Braze ne stocke un jeton qu’à partir du point où un utilisateur a été invité à l’invite de notification push de l’iOS. Avant cela, l’utilisateur ne sera pas joignable par notification push, et la solution précédente ne sera pas possible.

[39]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/silent_push_notifications/
[40]: {% image_buster /assets/img_archive/iosServerSentPush.png %}
[41]: {% image_buster /assets/img_archive/iOSServerPush.png %}
[42]: {% image_buster /assets/img_archive/iosIAMeventTrigger.png %}
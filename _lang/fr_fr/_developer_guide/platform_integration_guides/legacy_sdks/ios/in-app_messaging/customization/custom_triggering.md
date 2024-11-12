---
nav_title: Déclenchement personnalisé
article_title: Personnaliser la fonction de déclenchement de message in-app pour iOS
platform: iOS
page_order: 7
description: "Cet article de référence couvre le déclenchement de messagerie in-app personnalisée pour votre application iOS."
channel:
  - in-app messages
noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Déclenchement personnalisé de messages in-app

Par défaut, les messages in-app sont déclenchés par des types d’événements enregistrés par le SDK. Si vous souhaitez déclencher des messages in-app par des événements envoyés par le serveur, vous pouvez également le faire.

Pour activer cette fonction, vous enverrez une notification push silencieuse à l’appareil, ce qui lui permet de consigner un événement basé sur un SDK. Cet événement SDK déclencherait ensuite le message in-app orienté utilisateur.

## Étape 1 : Gérer les paires clé-valeur et les notifications push silencieuses

Ajoutez le code suivant à la méthode `application(_:didReceiveRemoteNotification:fetchCompletionHandler:)` :

{% tabs %}
{% tab OBJECTIF-C %}

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

Créer une campagne de notification push silencieuse déclenchée par l’événement envoyé par le serveur. Pour plus de détails sur la création d'une campagne de notification push silencieuse, reportez-vous aux [notifications push silencieuses]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/silent_push_notifications/).

![Une campagne de messages in-app basée sur une livraison par action qui sera délivrée aux utilisateurs qui effectuent l'événement personnalisé "server_event".]({% image_buster /assets/img_archive/iosServerSentPush.png %})

La campagne de notification push doit inclure des extras de paires clé-valeur, qui indiquent que cette campagne de notification push est envoyée pour enregistrer un événement personnalisé SDK. Cet événement sera utilisé pour déclencher le message in-app.

![Une campagne de messages in-app à la livraison par événement qui comporte deux paires clé-valeur. "CAMPAIGN_NAME" devient "Exemple de nom de message in-app" et IS_SERVER_EVENT" devient "true".]({% image_buster /assets/img_archive/iOSServerPush.png %})

Le code de la méthode `application(_:didReceiveRemoteNotification:fetchCompletionHandler:)` vérifie la clé `IS_SERVER_EVENT` et enregistrera un événement personnalisé SDK s’il existe.

Vous pouvez modifier le nom de l’événement ou les propriétés d’événement en envoyant la valeur souhaitée dans les options de paires clé-valeur de la charge utile de notification push. Lors de la journalisation de l’événement personnalisé, ces extras peuvent être utilisés comme paramètre du nom de l’événement ou comme propriété de l’événement.

## Étape 3 : Créer une campagne de communication in-app

Créez votre campagne de messages in-app visibles par l’utilisateur dans le tableau de bord de Braze. Cette campagne doit avoir une livraison par événement et être déclenchée par l’événement personnalisé enregistré à partir de la méthode `application(_:didReceiveRemoteNotification:fetchCompletionHandler:)`.

Dans l’exemple suivant, le message in-app spécifique à déclencher a été configuré en envoyant la propriété de l’événement dans le cadre de la première notification push silencieuse.

![Une campagne de messages in-app basée sur une action qui sera délivrée aux utilisateurs qui effectuent l'événement personnalisé "In-app message trigger" où "campaign_name" est égal à "In-app message name example".]({% image_buster /assets/img_archive/iosIAMeventTrigger.png %})

En raison d’un message push utilisé pour enregistrer un événement personnalisé, Braze devra stocker un jeton de notification push pour chaque utilisateur afin de permettre cette solution. Pour les utilisateurs d’iOS et d’Android, Braze ne stocke un jeton qu’à partir du point où un utilisateur a reçu un notification push de l’OS. Avant cela, l’utilisateur ne sera pas joignable par notification push, et la solution précédente ne sera pas possible.


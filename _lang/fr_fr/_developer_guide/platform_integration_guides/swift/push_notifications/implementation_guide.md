---
nav_title: Implémentation avancée (facultatif)
article_title: Implémentation avancée de notifications push pour iOS (facultatif)
platform: Swift
page_order: 30
description: "Ce guide d’implémentation avancée traite des moyens d’exploiter les extensions d’application de contenu de notification push iOS pour tirer le meilleur parti des messages push avec le SDK Swift."
channel:
  - push
---

<br>
{% alert important %}
Vous recherchez le guide d’intégration de base du développeur de notifications push ? Trouvez-le [ici]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/).
{% endalert %}

# Guide d’implémentation avancé

> Ce guide de mise en œuvre facultatif et avancé traite des moyens d'exploiter les extensions d'apps de contenu de notification pour tirer le meilleur parti de vos messages push. 

Ce guide fournit trois exemples d'implémentation d'extensions d'applications de contenu de notification, chacun avec une présentation du concept, des cas d'utilisation potentiels et un aperçu de la façon dont les variables de notification push peuvent se présenter et être utilisées dans le bord de Braze :
- [Notification push interactive](#interactive-push-notification)
- [Notifications push personnalisées](#personalized-push-notifications)
- [Notifications push pour le recueil d'informations](#information-capture-push-notification)

Cet article fournit également des [conseils sur l'enregistrement des analyses](#logging-analytics) pour ces implémentations personnalisées.

Notez que ce guide d’implémentation est centré autour d’une implémentation Swift, mais les extraits de code Objective-C sont fournis aux personnes intéressées.

## Extensions d’application de contenu de notification

![Deux messages de notification push affichés côte à côte. Le message de gauche montre à quoi ressemble un envoi avec l'interface utilisateur par défaut. Le message de droite montre une carte perforée de café poussée par la mise en œuvre d'une interface utilisateur personnalisée.]({% image_buster /assets/img/push_implementation_guide/push1.png %}){: style="max-width:65%;border:0;margin-top:10px"}

Les extensions d'applications de contenu de notification constituent une excellente option de personnalisation des notifications push. Les extensions d'apps de contenu de notification affichent une interface personnalisée pour les notifications de votre app lorsqu'une notification push est développée. 

Les notifications push peuvent être étendues de trois manières différentes :
- Un appui long sur la bannière de notification push
- Faire glisser sur la bannière de notification push
- Faire glisser la bannière vers la gauche et sélectionner « Afficher » 

Ces vues personnalisées offrent des moyens intelligents d'engager les clients en affichant des types de contenu distincts, notamment des notifications interactives, des notifications alimentées par des données utilisateur et même des messages push qui peuvent capturer des informations telles que des numéros de téléphone et des e-mails. L'une de nos fonctionnalités bien connues chez Braze, [Push Stories]({{site.baseurl}}/user_guide/message_building_by_channel/push/advanced_push_options/push_stories/), est un excellent exemple de ce à quoi peut ressembler une extension d'application de contenu par notification push !

### Conditions
![]({% image_buster /assets/img/push_implementation_guide/push15.png %}){: style="float:right;max-width:50%;margin-left:10px; border:0;margin-top:10px"}
- [Les notifications push]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/) intégrées avec succès dans votre app.
- Les fichiers suivants générés par Xcode en fonction de votre langue de codage :

**Swift**<br>
- `NotificationViewController.swift`
- `MainInterface.storyboard`

**Objectif-C**<br>
- `NotificationViewController.h`
- `NotificationViewController.m`
- `MainInterface.storyboard`

## Notification push interactive

Les notifications push peuvent répondre aux actions de l'utilisateur à l'intérieur d'une extension d'application de contenu. Pour les utilisateurs exécutant iOS 12 ou une version ultérieure, cela signifie que vous pouvez transformer vos notifications push en messages entièrement interactifs ! Il s'agit d'une option intéressante pour introduire de l'interactivité dans vos promotions et applications. Par exemple, votre notification push peut inclure un jeu pour les utilisateurs, une roue à faire tourner pour gagner des réductions, ou un bouton « J’aime » pour enregistrer une annonce ou une chanson.

L'exemple suivant montre une notification push dans laquelle les utilisateurs peuvent jouer à un jeu de match à l'intérieur de la notification élargie.

![Un schéma de ce à quoi pourraient ressembler les phases d’une notification push interactive. Une séquence montre un utilisateur appuyant sur une notification push qui affiche un jeu d'association interactif.]({% image_buster /assets/img/push_implementation_guide/push12.png %}){: style="border:0"}

### Configuration du tableau de bord

Pour créer une notification push interactive, vous devez définir une vue personnalisée dans votre tableau de bord. 

1. Dans la page **Campagnes**, cliquez sur **Créer une campagne** pour lancer une nouvelle campagne de notification push.
2. Dans l'onglet **Composer**, basculez sur les **boutons de notification.** 
3. Saisissez une catégorie iOS personnalisée dans le champ **Catégorie de notification iOS.**  
4. Dans la `.plist` de votre cible d'extension de contenu de notification, définissez l'attribut `UNNotificationExtensionCategory` sur votre catégorie iOS personnalisée. La valeur indiquée ici doit correspondre à celle définie dans le tableau de bord de Braze sous **Catégorie de notification iOS.** 
5. Définissez la clé `UNNotificationExtensionInteractionEnabled` sur `true` pour activer les interactions avec l'utilisateur dans une notification push.

![Les options du bouton de notification se trouvent dans les paramètres du compositeur de messages push.]({% image_buster /assets/img/push_implementation_guide/push16.png %}){: style="max-width:75%;border:0;margin-top:10px"}
![]({% image_buster /assets/img/push_implementation_guide/push17.png %}){: style="max-width:75%;border:0;margin-top:10px"}

### Prêt à enregistrer l’analyse ?
Consultez la [section Enregistrer les analyses](#logging-analytics) pour mieux comprendre à quoi doit ressembler le flux de données.

## Notifications push personnalisées
![Deux iPhone affichés côte à côte. Le premier iPhone affiche la vue non étendue du message push. Le deuxième iPhone montre la version élargie du message push, qui affiche une photo de la progression du cours, le nom de la prochaine session et la date à laquelle elle doit être terminée.]({% image_buster /assets/img/push_implementation_guide/push6.png %}){: style="float:right;max-width:40%;margin-left:15px;border:0"}

Les notifications push peuvent afficher des informations spécifiques à l’utilisateur dans une extension de contenu. Cela vous permet de créer du contenu push axé sur l'utilisateur, comme l'ajout de l'option de partage de votre progression sur différentes plateformes, l'affichage des réalisations déverrouillées ou l'affichage des listes de contrôle d'onboarding. Cet exemple montre une notification push affichée à un utilisateur après qu'il a terminé une tâche spécifique dans le cours d'apprentissage de Braze. En développant la notification, l'utilisateur peut voir sa progression dans son parcours d'apprentissage. Les informations fournies ici sont spécifiques à l'utilisateur et peuvent être déclenchées à la fin d'une session ou lors d'une action spécifique de l'utilisateur en utilisant un déclencheur de l'API. 

### Configuration du tableau de bord

Pour créer une notification push personnalisée, vous devez définir une vue personnalisée dans votre tableau de bord. 

1. Dans la page **Campagnes**, cliquez sur **Créer une campagne** pour lancer une nouvelle campagne de notification push.
2. Dans l'onglet **Composer**, basculez sur les **boutons de notification.** 
3. Saisissez une catégorie iOS personnalisée dans le champ **Catégorie de notification iOS.**  
4. Dans l'onglet **Paramètres**, créez des paires clé-valeur à l'aide de Liquid standard. Définissez les attributs utilisateur appropriés que vous souhaitez voir apparaître dans le message. Ces vues peuvent être personnalisées sur la base des attributs utilisateur spécifiques d’un profil utilisateur donné.
5. Dans la `.plist` de votre cible d'extension de contenu de notification, définissez l'attribut `UNNotificationExtensionCategory` sur votre catégorie iOS personnalisée. La valeur indiquée ici doit correspondre à celle définie dans le tableau de bord de Braze sous **Catégorie de notification iOS.** 

![Quatre ensembles de paires clé-valeur, où "next_session_name" et "next_session_complete_date" sont définis en tant que propriété de déclencheur API à l'aide de Liquid, et "completed_session count" et "total_session_count" sont définis en tant qu'attribut utilisateur personnalisé à l'aide de Liquid.]({% image_buster /assets/img/push_implementation_guide/push5.png %}){: style="max-width:60%;"}

### Gérer les paires clé-valeur

La méthode `didReceive` est appelée lorsque l'extension de l'application de contenu de notification a reçu une notification. Cette méthode est disponible dans le `NotificationViewController`. Les paires clé-valeur fournies dans le tableau de bord sont représentées dans le code par l’utilisation d’un dictionnaire `userInfo`.

#### Analyser des paires clé-valeur à partir de notifications push

{% tabs %}
{% tab Swift %}
``` swift 
func didReceive(_ notification: UNNotification) {
  let userInfo = notification.request.content.userInfo
     
  guard let value = userInfo["YOUR-KEY-VALUE-PAIR"] as? String,
        let otherValue = userInfo["YOUR-OTHER-KEY-VALUE-PAIR"] as? String,
  else { fatalError("Key-Value Pairs are incorrect.")}
 
  ...
}
```
{% endtab %}
{% tab Objectif-C %}
```objc
- (void)didReceiveNotification:(nonnull UNNotification *)notification {
  NSDictionary *userInfo = notification.request.content.userInfo;
   
  if (userInfo[@"YOUR-KEY-VALUE-PAIR"] && userInfo[@"YOUR-OTHER-KEY-VALUE-PAIR"]) {
 
  ...
 
  } else {
    [NSException raise:NSGenericException format:@"Key-Value Pairs are incorrect"];
  }
}
```
{% endtab %}
{% endtabs %}

### Prêt à enregistrer l’analyse ?
Consultez la [section Enregistrer les analyses](#logging-analytics) pour mieux comprendre à quoi doit ressembler le flux de données.

## Notification push de recueil d’informations

Les notifications push peuvent capturer les informations de l'utilisateur à l'intérieur d'une extension d'app de contenu, repoussant ainsi les limites de ce qu'il est possible de faire avec un push. Demander la contribution des utilisateurs par le biais de notifications push vous permet non seulement de demander des informations de base comme le nom ou l'e-mail, mais aussi d'inciter les utilisateurs à soumettre leurs commentaires ou à compléter un profil utilisateur inachevé. 

Dans le flux suivant, la vue personnalisée est en mesure de répondre aux changements d'état. Ces composants de changement d’état sont représentés dans chaque image. 

1. L’utilisateur reçoit une notification push.
2. La notification push est ouverte. Une fois élargie, la notification push invite l'utilisateur à fournir des informations. Dans cet exemple, l'adresse e-mail de l'utilisateur est demandée, mais vous pourriez demander n'importe quel type d'information.
3. Les informations sont fournies et, si elles sont dans le format attendu, le bouton d'enregistrement s'affiche.
3. La vue de confirmation s’affiche et la notification push est rejetée. 

![]({% image_buster /assets/img/push_implementation_guide/push8.png %}){: style="border:0;"}

### Configuration du tableau de bord

Pour créer une notification push de capture d'informations, vous devez définir une vue personnalisée dans votre tableau de bord. 

1. Dans la page **Campagnes**, cliquez sur **Créer une campagne** pour lancer une nouvelle campagne de notification push.
2. Dans l'onglet **Composer**, basculez sur les **boutons de notification.** 
3. Saisissez une catégorie iOS personnalisée dans le champ **Catégorie de notification iOS.**  
4. Dans l'onglet **Paramètres**, créez des paires clé-valeur à l'aide de Liquid standard. Définissez les attributs utilisateur appropriés que vous souhaitez voir apparaître dans le message. 
5. Dans la `.plist` de votre cible d'extension de contenu de notification, définissez l'attribut `UNNotificationExtensionCategory` sur votre catégorie iOS personnalisée. La valeur indiquée ici doit correspondre à celle définie dans le tableau de bord de Braze sous **Catégorie de notification iOS.** 

Comme le montre l'exemple, vous pouvez également inclure une image dans votre notification push. Pour ce faire, vous devez intégrer les [notifications riches]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/customization/rich_notifications/), définir le style de notification de votre campagne sur Notification riche et inclure une image push riche.

![Une notification push avec trois ensembles de paires clé-valeur. 1\. "Braze_id" défini comme un appel liquide pour récupérer l'ID de Braze. 2\. "cert_title" défini comme "Braze Marketer Certification". 3\. "Cert_description" est défini comme "Entraînement certifié des marketeurs Braze...".]({% image_buster /assets/img/push_implementation_guide/push9.png %})

### Gérer les actions des boutons

Chaque bouton d’action est identifié de manière unique. Le code vérifie si votre identifiant de réponse est égal à `actionIndentifier`, et, si c’est le cas, sait que l’utilisateur a cliqué sur le bouton d’action.

**Gestion des réponses aux boutons d'action des notifications push**<br>

{% tabs %}
{% tab Swift %}
``` swift 
func didReceive(_ response: UNNotificationResponse, completionHandler completion: @escaping (UNNotificationContentExtensionResponseOption) -> Void) {
  if response.actionIdentifier == "YOUR-REGISTER-IDENTIFIER" {
    // do something
  } else {
    // do something else
  }
}
```
{% endtab %}
{% tab Objectif-C %}
```objc
- (void)didReceiveNotificationResponse:(UNNotificationResponse *)response completionHandler:(void (^)(UNNotificationContentExtensionResponseOption))completion {
  if ([response.actionIdentifier isEqualToString:@"YOUR-REGISTER-IDENTIFIER"]) {
    completion(UNNotificationContentExtensionResponseOptionDismiss);
  } else {
    completion(UNNotificationContentExtensionResponseOptionDoNotDismiss);
  }
}
```
{% endtab %}
{% endtabs %}

### Rejet des notifications push

Les notifications push peuvent être automatiquement rejetées en appuyant sur un bouton d’action. Nous vous recommandons de choisir parmi trois options prédéfinies pour le rejet de la notification push :

1. `completion(.dismiss)` - Rejet de la notification
2. `completion(.doNotDismiss)` - La notification reste ouverte
3. `completion(.dismissAndForward)` - La commande push est rejetée et l'utilisateur est redirigé vers l'application.

### Prêt à enregistrer l’analyse ?
Consultez la [section suivante](#logging-analytics) pour mieux comprendre à quoi doit ressembler le flux de données. 

## Enregistrer les analyses

### Enregistrer avec l’API Braze (recommandé)

L'enregistrement de l’analyse peut être effectué en temps réel à l'aide de [l'endpoint `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) de l'API Braze. Pour enregistrer l’analyse, envoyez la valeur `braze_id` dans le champ des paires clé-valeur (comme indiqué dans la capture d’écran suivante) pour identifier le profil utilisateur à mettre à jour.

![Une notification push avec trois ensembles de paires clé-valeur. 1\. "Braze_id" défini comme un appel liquide pour récupérer l'ID de Braze. 2\. "cert_title" défini comme "Braze Marketer Certification". 3\. "Cert_description" est défini comme "Entraînement certifié des marketeurs Braze...".]({% image_buster /assets/img/push_implementation_guide/push18.png %}){: style="max-width:80%;"}

### Enregistrement manuel

L’enregistrement manuel exigera la configuration préalable des espaces de travail dans Xcode, puis la création, l’enregistrement et la récupération des analyses. Cela nécessitera un travail de développeur personnalisé de votre côté. Les extraits de code suivants vous aideront à résoudre ce problème. 

Il est important de noter que les analyses ne seront pas envoyées à Braze tant que l’application mobile n’aura pas été lancée subséquemment. Cela signifie que, selon vos paramètres de rejet, il existe souvent une période indéterminée entre le moment où une notification push est rejetée et l’application mobile est lancée et que les analyses sont récupérées. Même si cette période tampon n’affecte pas tous les cas d’utilisation, vous devez prendre en compte l’impact et, si nécessaire, ajuster votre parcours utilisateur afin d’inclure l’ouverture de l’application pour répondre à ce problème. 

![Un graphique décrivant la manière dont les analyses sont traitées par Braze. 1\. Les données d'analyse sont créées. 2\. Les données d'analyse sont enregistrées. 3\. La notification push est rejetée. 4\. Période indéterminée entre le moment où la notification push est rejetée et l’application mobile est lancée. 5\. L’application mobile est lancée. 6\. Les données d'analyse sont reçues. 7\. Les données analytiques sont envoyées à Braze.]({% image_buster /assets/img/push_implementation_guide/push13.png %})

#### Étape 1 : Configurer les groupes d’applications dans Xcode
Dans Xcode, ajoutez la capacité `App Groups`. Si vous n'avez pas d'espace de travail dans votre application, allez dans la capacité de la cible d’application principale, activez `App Groups`, puis cliquez sur le bouton **+** Ajouter. Ensuite, utilisez l'ID du bundle de votre application pour créer l'espace de travail. Par exemple, si l'ID du bundle de votre application est `com.company.appname`, vous pouvez nommer votre espace de travail `group.com.company.appname.xyz`. Assurez-vous que les `App Groups` sont activés pour la cible de votre application principale et la cible de l’extension de contenu.

![]({% image_buster /assets/img/swift/push_story/add_app_groups.png %})

#### Étape 2 : Intégrer les extraits de code
Les extraits de code suivants sont une référence utile sur la façon d’enregistrer et d’envoyer des événements personnalisés, des attributs personnalisés et des attributs utilisateur. Dans ce guide, nous parlerons en termes de `UserDefaults`, mais le code sera représenté sous la forme du fichier d'aide `RemoteStorage`. Il existe des fichiers d'aide supplémentaires, `UserAttributes` et `EventName Dictionary`, qui sont utilisés pour envoyer et enregistrer les attributs de l'utilisateur.

{% tabs local %}
{% tab Custom Events (Événements personnalisés) %}

##### Enregistrement des événements personnalisés

Pour enregistrer des événements personnalisés, vous devez créer l’analyse à partir de zéro. Pour ce faire, créez un dictionnaire, renseignez-le avec des métadonnées et enregistrez les données via l’utilisation d’un fichier d’aide.

1. Initialiser un dictionnaire avec des métadonnées d’événement
2. Initialiser `userDefaults` pour récupérer et stocker les données d’événements
3. Si un tableau existe déjà, ajoutez-y de nouvelles données et enregistrez
4. S’il n’y a pas de tableau existant, enregistrez le nouveau tableau sur `userDefaults`

{% subtabs global %}
{% subtab Swift %}
``` swift 
func saveCustomEvent(with properties: [String: Any]? = nil) {
  // 1
  let customEventDictionary = Dictionary(eventName: "YOUR-EVENT-NAME", properties: properties)
  
  // 2
  let remoteStorage = RemoteStorage(storageType: .suite)
  
  // 3   
  if var pendingEvents = remoteStorage.retrieve(forKey: .pendingCustomEvents) as? [[String: Any]] {
    pendingEvents.append(contentsOf: [customEventDictionary])
    remoteStorage.store(pendingEvents, forKey: .pendingCustomEvents)
  } else {
  // 4
    remoteStorage.store([customEventDictionary], forKey: .pendingCustomEvents)
  }
}
```
{% endsubtab %}
{% subtab Objective-C %}
```objc
- (void)saveCustomEvent:(NSDictionary<NSString *, id> *)properties {
  // 1 
  NSDictionary<NSString *, id> *customEventDictionary = [[NSDictionary alloc] initWithEventName:@"YOUR-EVENT-NAME" properties:properties];
  
  // 2
  RemoteStorage *remoteStorage = [[RemoteStorage alloc] initWithStorageType:StorageTypeSuite];
  NSMutableArray *pendingEvents = [[remoteStorage retrieveForKey:RemoteStorageKeyPendingCustomEvents] mutableCopy];
  
  // 3 
  if (pendingEvents) {
    [pendingEvents addObject:customEventDictionary];
    [remoteStorage store:pendingEvents forKey:RemoteStorageKeyPendingCustomAttributes];
  } else {
  // 4
    [remoteStorage store:@[ customEventDictionary ] forKey:RemoteStorageKeyPendingCustomAttributes];
  }
}
```
{% endsubtab %}
{% endsubtabs %}

##### Envoi d’événements personnalisés à Braze

Le meilleur moment pour enregistrer une analyse sauvegardée à partir d'une extension d'application de contenu de notification est juste après l'initialisation du SDK. Pour ce faire, vous pouvez parcourir en boucle tous les événements en attente, vérifier la présence de la touche "Nom de l'événement", définir les valeurs appropriées dans Braze, puis effacer la mémoire pour la prochaine fois que cette fonction sera nécessaire.

1. Passez en revue la série d’événements en attente
2. Passez en revue chaque paire clé-valeur dans le dictionnaire `pendingEvents`
3. Vérifiez explicitement la clé pour « Nom de l'événement » afin de définir la valeur en conséquence
4. Toutes les autres clés-valeurs seront ajoutées au dictionnaire `properties`
5. Consigner un événement personnalisé individuel 
6. Supprimer tous les événements en attente du stockage

{% subtabs global %}
{% subtab Swift %}
``` swift 
func logPendingCustomEventsIfNecessary() {
  let remoteStorage = RemoteStorage(storageType: .suite)
  guard let pendingEvents = remoteStorage.retrieve(forKey: .pendingCustomEvents) as? [[String: Any]] else { return }
  
  // 1    
  for event in pendingEvents {
    var eventName: String?
    var properties: [AnyHashable: Any] = [:]
    
  // 2
    for (key, value) in event {
      if key == PushNotificationKey.eventName.rawValue {
  // 3      
        if let eventNameValue = value as? String {
          eventName = eventNameValue
        } else {
          print("Invalid type for event_name key")
        }
      } else {
  // 4 
        properties[key] = value
      }
    }
  // 5    
    if let eventName = eventName {
      AppDelegate.braze?.logCustomEvent(eventName, properties: properties)
    }
  }

  // 6    
  remoteStorage.removeObject(forKey: .pendingCustomEvents)
}
```
{% endsubtab %}
{% subtab Objective-C %}
```objc
- (void)logPendingEventsIfNecessary {
  RemoteStorage *remoteStorage = [[RemoteStorage alloc] initWithStorageType:StorageTypeSuite];
  NSArray *pendingEvents = [remoteStorage retrieveForKey:RemoteStorageKeyPendingCustomEvents];
  
  // 1 
  for (NSDictionary<NSString *, id> *event in pendingEvents) {
    NSString *eventName = nil;
    NSMutableDictionary *properties = [NSMutableDictionary dictionary];
    
  // 2 
    for (NSString* key in event) {
      if ([key isEqualToString:@"event_name"]) {
  // 3       
        if ([[event objectForKey:key] isKindOfClass:[NSString class]]) {
          eventName = [event objectForKey:key];
        } else {
          NSLog(@"Invalid type for event_name key");
        }
      } else {
  // 4 
        properties[key] = event[key];
      }
    }
  // 5  
    if (eventName != nil) {
      [AppDelegate.braze logCustomEvent:eventName properties:properties];
    }
  }

  // 6  
  [remoteStorage removeObjectForKey:RemoteStorageKeyPendingCustomEvents];
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Attributs personnalisés %}

##### Enregistrer des attributs personnalisés

Pour enregistrer des attributs personnalisés, vous devez créer l’analyse à partir de zéro. Pour ce faire, créez un dictionnaire, renseignez-le avec des métadonnées et enregistrez les données via l’utilisation d’un fichier d’aide.

1. Initialiser un dictionnaire avec des attributs de métadonnées
2. Initialiser `userDefaults` pour récupérer et stocker les données d’attributs
3. Si un tableau existe déjà, ajoutez-y de nouvelles données et enregistrez
4. S’il n’y a pas de tableau existant, enregistrez le nouveau tableau sur `userDefaults`

{% subtabs global %}
{% subtab Swift %}
``` swift 
func saveCustomAttribute() {
  // 1 
  let customAttributeDictionary: [String: Any] = ["YOUR-CUSTOM-ATTRIBUTE-KEY": "YOUR-CUSTOM-ATTRIBUTE-VALUE"]
  
  // 2 
  let remoteStorage = RemoteStorage(storageType: .suite)
  
  // 3 
  if var pendingAttributes = remoteStorage.retrieve(forKey: .pendingCustomAttributes) as? [[String: Any]] {
    pendingAttributes.append(contentsOf: [customAttributeDictionary])
    remoteStorage.store(pendingAttributes, forKey: .pendingCustomAttributes)
  } else {
  // 4 
    remoteStorage.store([customAttributeDictionary], forKey: .pendingCustomAttributes)
  }
}
```
{% endsubtab %}
{% subtab Objective-C %}
``` objc
- (void)saveCustomAttribute {
  // 1 
  NSDictionary<NSString *, id> *customAttributeDictionary = @{ @"YOUR-CUSTOM-ATTRIBUTE-KEY": @"YOUR-CUSTOM-ATTRIBUTE-VALUE" };
  
  // 2  
  RemoteStorage *remoteStorage = [[RemoteStorage alloc] initWithStorageType:StorageTypeSuite];
  NSMutableArray *pendingAttributes = [[remoteStorage retrieveForKey:RemoteStorageKeyPendingCustomAttributes] mutableCopy];
  
  // 3
  if (pendingAttributes) {
    [pendingAttributes addObject:customAttributeDictionary];
    [remoteStorage store:pendingAttributes forKey:RemoteStorageKeyPendingCustomAttributes];
  } else {
  // 4 
    [remoteStorage store:@[ customAttributeDictionary ] forKey:RemoteStorageKeyPendingCustomAttributes];
  }
}
```
{% endsubtab %}
{% endsubtabs %}

##### Envoyer des attributs personnalisés à Braze

Le meilleur moment pour enregistrer une analyse sauvegardée à partir d'une extension d'application de contenu de notification est juste après l'initialisation du SDK. Pour ce faire, vous pouvez parcourir tous les attributs en attente, en définissant l’attribut personnalisé approprié dans Braze, puis en effaçant l’enregistrement pour la prochaine fois que cette fonction sera nécessaire.

1. Passez en revue la série d’attributs en attente
2. Passez en revue chaque paire clé-valeur dans le dictionnaire `pendingAttributes`
3. Enregistrer les attributs personnalisés individuels avec la clé et la valeur correspondantes
4. Supprimer tous les attributs en attente du stockage

{% subtabs global %}
{% subtab Swift %}
``` swift 
func logPendingCustomAttributesIfNecessary() {
  let remoteStorage = RemoteStorage(storageType: .suite)
  guard let pendingAttributes = remoteStorage.retrieve(forKey: .pendingCustomAttributes) as? [[String: Any]] else { return }
     
  // 1
  pendingAttributes.forEach { setCustomAttributesWith(keysAndValues: $0) }
  
  // 4 
  remoteStorage.removeObject(forKey: .pendingCustomAttributes)
}
   
func setCustomAttributesWith(keysAndValues: [String: Any]) {
  // 2 
  for (key, value) in keysAndValues {
  // 3
    if let value = value as? [String] {
      setCustomAttributeArrayWithKey(key, andValue: value)
    } else {
      setCustomAttributeWithKey(key, andValue: value)
    }
  }
}
```
{% endsubtab %}
{% subtab Objective-C %}
```objc
- (void)logPendingCustomAttributesIfNecessary {
  RemoteStorage *remoteStorage = [[RemoteStorage alloc] initWithStorageType:StorageTypeSuite];
  NSArray *pendingAttributes = [remoteStorage retrieveForKey:RemoteStorageKeyPendingCustomAttributes];
   
  // 1
  for (NSDictionary<NSString*, id> *attribute in pendingAttributes) {
    [self setCustomAttributeWith:attribute];
  }

  // 4 
  [remoteStorage removeObjectForKey:RemoteStorageKeyPendingCustomAttributes];
}
 
- (void)setCustomAttributeWith:(NSDictionary<NSString *, id> *)keysAndValues {
  // 2
  for (NSString *key in keysAndValues) {
  // 3 
    [self setCustomAttributeWith:key andValue:[keysAndValues objectForKey:key]];
  }
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Attributs de l'utilisateur %}

##### Enregistrer des attributs utilisateur

Lorsque vous enregistrez des attributs utilisateur, nous vous recommandons de créer un objet personnalisé pour déterminer le type d'attribut mis à jour (`email`, `first_name`, `phone_number`, etc.). L’objet doit être compatible avec ce qui a été stocké/récupéré dans `UserDefaults`. Voir le fichier d’aide `UserAttribute` pour un exemple de la manière d’y parvenir.

1. Initialiser un objet `UserAttribute` encodé avec le type correspondant
2. Initialiser `userDefaults` pour récupérer et stocker les données d’événements
3. Si un tableau existe déjà, ajoutez-y de nouvelles données et enregistrez
4. S’il n’y a pas de tableau existant, enregistrez le nouveau tableau sur `userDefaults`

{% subtabs global %}
{% subtab Swift %}
``` swift 
func saveUserAttribute() {
  // 1 
  guard let data = try? PropertyListEncoder().encode(UserAttribute.userAttributeType("USER-ATTRIBUTE-VALUE")) else { return }
  
  // 2       
  let remoteStorage = RemoteStorage(storageType: .suite)
  
  // 3    
  if var pendingAttributes = remoteStorage.retrieve(forKey: .pendingUserAttributes) as? [Data] {
    pendingAttributes.append(contentsOf: [data])
    remoteStorage.store(pendingAttributes, forKey: .pendingUserAttributes)
  } else {
  // 4 
    remoteStorage.store([data], forKey: .pendingUserAttributes)
  }
}
```
{% endsubtab %}
{% subtab Objective-C %}
```objc
- (void)saveUserAttribute {
  // 1 
  UserAttribute *userAttribute = [[UserAttribute alloc] initWithUserField:@"USER-ATTRIBUTE-VALUE" attributeType:UserAttributeTypeEmail];
   
  NSError *error;
  NSData *data = [NSKeyedArchiver archivedDataWithRootObject:userAttribute requiringSecureCoding:YES error:&error];

  if (error != nil) {
    // log error
  }
  // 2  
  RemoteStorage *remoteStorage = [[RemoteStorage alloc] initWithStorageType:StorageTypeSuite];
  NSMutableArray *pendingAttributes = [[remoteStorage retrieveForKey:RemoteStorageKeyPendingUserAttributes] mutableCopy];
  
  // 3 
  if (pendingAttributes) {
    [pendingAttributes addObject:data];
    [remoteStorage store:pendingAttributes forKey:RemoteStorageKeyPendingUserAttributes];
  } else {
  // 4 
    [remoteStorage store:@[data] forKey:RemoteStorageKeyPendingUserAttributes];
  }
}
```
{% endsubtab %}
{% endsubtabs %}

##### Envoyer des attributs utilisateur à Braze

Le meilleur moment pour enregistrer une analyse sauvegardée à partir d'une extension d'application de contenu de notification est juste après l'initialisation du SDK. Pour ce faire, vous pouvez parcourir tous les attributs en attente, en définissant l’attribut personnalisé approprié dans Braze, puis en effaçant l’enregistrement pour la prochaine fois que cette fonction sera nécessaire.

1. Parcourir le tableau de données `pendingAttributes`
2. Initialiser un objet `UserAttribute` encodé à partir des données d’attribut
3. Définir un champ utilisateur spécifique basé sur le type d’attribut utilisateur (e-mail)
4. Supprimer tous les attributs utilisateur en attente du stockage

{% subtabs global %}
{% subtab Swift %}
``` swift 
func logPendingUserAttributesIfNecessary() {
  let remoteStorage = RemoteStorage(storageType: .suite)
  guard let pendingAttributes = remoteStorage.retrieve(forKey: .pendingUserAttributes) as? [Data] else { return }
  
  // 1    
  for attributeData in pendingAttributes {
  // 2 
    guard let userAttribute = try? PropertyListDecoder().decode(UserAttribute.self, from: attributeData) else { continue }
    
  // 3    
    switch userAttribute {
    case .email(let email):
      user?.email = email
    }
  }
  // 4   
  remoteStorage.removeObject(forKey: .pendingUserAttributes)
}
```
{% endsubtab %}
{% subtab Objective-C %}
```objc
- (void)logPendingUserAttributesIfNecessary {
  RemoteStorage *remoteStorage = [[RemoteStorage alloc] initWithStorageType:StorageTypeSuite];
  NSArray *pendingAttributes = [remoteStorage retrieveForKey:RemoteStorageKeyPendingUserAttributes];
  
  // 1  
  for (NSData *attributeData in pendingAttributes) {
    NSError *error;
  
  // 2 
    UserAttribute *userAttribute = [NSKeyedUnarchiver unarchivedObjectOfClass:[UserAttribute class] fromData:attributeData error:&error];

    if (error != nil) {
      // log error
    }
    
  // 3  
    if (userAttribute) {
      switch (userAttribute.attributeType) {
        case UserAttributeTypeEmail:
          [self user].email = userAttribute.userField;
          break;
      }
    }
  }
  // 4 
  [remoteStorage removeObjectForKey:RemoteStorageKeyPendingUserAttributes];
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Fichiers d'aide %}

##### Fichiers d’aide

{% details Fichier d'aide RemoteStorage %}
{% subtabs global %}
{% subtab Swift %}
```swift
enum RemoteStorageKey: String, CaseIterable {
   
  // MARK: - Notification Content Extension Analytics
  case pendingCustomEvents = "pending_custom_events"
  case pendingCustomAttributes = "pending_custom_attributes"
  case pendingUserAttributes = "pending_user_attributes"
}
 
enum RemoteStorageType {
  case standard
  case suite
}
 
class RemoteStorage: NSObject {
  private var storageType: RemoteStorageType = .standard
  private lazy var defaults: UserDefaults = {
    switch storageType {
    case .standard:
      return .standard
    case .suite:
      return UserDefaults(suiteName: "YOUR-DOMAIN-IDENTIFIER")!
    }
  }()
   
  init(storageType: RemoteStorageType = .standard) {
    self.storageType = storageType
  }
   
  func store(_ value: Any, forKey key: RemoteStorageKey) {
    defaults.set(value, forKey: key.rawValue)
  }
   
  func retrieve(forKey key: RemoteStorageKey) -> Any? {
    return defaults.object(forKey: key.rawValue)
  }
   
  func removeObject(forKey key: RemoteStorageKey) {
    defaults.removeObject(forKey: key.rawValue)
  }
   
  func resetStorageKeys() {
    for key in RemoteStorageKey.allCases {
      defaults.removeObject(forKey: key.rawValue)
    }
  }
}
```
{% endsubtab %}
{% subtab Objective-C %}
```objc
@interface RemoteStorage ()
 
@property (nonatomic) StorageType storageType;
@property (nonatomic, strong) NSUserDefaults *defaults;
 
@end
 
@implementation RemoteStorage
 
- (id)initWithStorageType:(StorageType)storageType {
  if (self = [super init]) {
    self.storageType = storageType;
  }
  return self;
}
 
- (void)store:(id)value forKey:(RemoteStorageKey)key {
  [[self defaults] setValue:value forKey:[self rawValueForKey:key]];
}
 
- (id)retrieveForKey:(RemoteStorageKey)key {
  return [[self defaults] objectForKey:[self rawValueForKey:key]];
}
 
- (void)removeObjectForKey:(RemoteStorageKey)key {
  [[self defaults] removeObjectForKey:[self rawValueForKey:key]];
}
 
- (void)resetStorageKeys {
  [[self defaults] removeObjectForKey:[self rawValueForKey:RemoteStorageKeyPendingCustomEvents]];
  [[self defaults] removeObjectForKey:[self rawValueForKey:RemoteStorageKeyPendingCustomAttributes]];
  [[self defaults] removeObjectForKey:[self rawValueForKey:RemoteStorageKeyPendingUserAttributes]];
}
 
- (NSUserDefaults *)defaults {
  if (!self.defaults) {
    switch (self.storageType) {
      case StorageTypeStandard:
        return [NSUserDefaults standardUserDefaults];
        break;
      case StorageTypeSuite:
        return [[NSUserDefaults alloc] initWithSuiteName:@"YOUR-DOMAIN-IDENTIFIER"];
    }
  } else {
    return self.defaults;
  }
}
 
- (NSString*)rawValueForKey:(RemoteStorageKey)remoteStorageKey {
    switch(remoteStorageKey) {
    case RemoteStorageKeyPendingCustomEvents:
      return @"pending_custom_events";
    case RemoteStorageKeyPendingCustomAttributes:
      return @"pending_custom_attributes";
    case RemoteStorageKeyPendingUserAttributes:
      return @"pending_user_attributes";
    default:
      [NSException raise:NSGenericException format:@"Unexpected FormatType."];
  }
}
```
{% endsubtab %}
{% endsubtabs %}
{% enddetails %}
{% details Fichier d'aide UserAttribute %}
{% subtabs global %}
{% subtab Swift %}
```swift
enum UserAttribute: Hashable {
  case email(String?)
}
 
// MARK: - Codable
extension UserAttribute: Codable {
  private enum CodingKeys: String, CodingKey {
    case email
  }
   
  func encode(to encoder: Encoder) throws {
    var values = encoder.container(keyedBy: CodingKeys.self)
     
    switch self {
    case .email(let email):
      try values.encode(email, forKey: .email)
    }
  }
   
  init(from decoder: Decoder) throws {
    let values = try decoder.container(keyedBy: CodingKeys.self)
     
    let email = try values.decode(String.self, forKey: .email)
    self = .email(email)
  }
}
```
{% endsubtab %}
{% subtab Objective-C %}
```objc
@implementation UserAttribute
 
- (id)initWithUserField:(NSString *)userField attributeType:(UserAttributeType)attributeType {
  if (self = [super init]) {
    self.userField = userField;
    self.attributeType = attributeType;
  }
  return self;
}
 
- (void)encodeWithCoder:(NSCoder *)encoder {
  [encoder encodeObject:self.userField forKey:@"userField"];
  [encoder encodeInteger:self.attributeType forKey:@"attributeType"];
}
 
- (id)initWithCoder:(NSCoder *)decoder {
  if (self = [super init]) {
    self.userField = [decoder decodeObjectForKey:@"userField"];
     
    NSInteger attributeRawValue = [decoder decodeIntegerForKey:@"attributeType"];
    self.attributeType = (UserAttributeType) attributeRawValue;
  }
  return self;
}
 
@end
```
{% endsubtab %}
{% endsubtabs %}
{% enddetails %}
{% details Fichier d'aide du dictionnaire EventName %}
{% subtabs global %}
{% subtab Swift %}
```swift
extension Dictionary where Key == String, Value == Any {
  init(eventName: String, properties: [String: Any]? = nil) {
    self.init()
    self[PushNotificationKey.eventName.rawValue] = eventName
     
    if let properties = properties {
      for (key, value) in properties {
        self[key] = value
      }
    }
  }
}
```
{% endsubtab %}
{% subtab Objective-C %}
```objc
@implementation NSDictionary (Helper)
 
- (id)initWithEventName:(NSString *)eventName properties:(NSDictionary *)properties {
  self = [self init];
  if (self) {
    dict[@"event_name"] = eventName;
     
    for(id key in properties) {
      dict[key] = properties[key];
    }
  }
  return self;
}
 
@end
```
{% endsubtab %}
{% endsubtabs %}
{% enddetails %}
<br>
{% endtab %}
{% endtabs %}


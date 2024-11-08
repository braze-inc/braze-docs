---
nav_title: Implémentation avancée (facultatif)
article_title: Implémentation avancée de notifications push pour iOS (facultatif)
platform: iOS
page_order: 28
description: "Ce guide d’implémentation avancée traite des moyens d’exploiter les extensions d’application de contenu de notification push iOS pour tirer le meilleur parti des messages push. Il contient également un exemple de trois cas d’usage créés par notre équipe, les extraits de code l’accompagnant et des directives concernant l’enregistrement des analyses."
channel:
  - push
noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

<br>
{% alert important %}
Vous recherchez le guide d’intégration de base du développeur de notifications push ? Trouvez-le [ici]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/integration/).
{% endalert %}

# Guide d’implémentation des notifications push

> Ce guide d’implémentation avancé et facultatif traite des moyens d’exploiter les extensions d’application de contenu de notification push pour tirer le meilleur parti des messages push. Il contient également trois cas d’usage personnalisés créés par notre équipe, les extraits de code l’accompagnant et des directives concernant l’enregistrement des analyses. Visitez notre dépôt de démonstrations Braze [ici](https://github.com/braze-inc/braze-growth-shares-ios-demo-app)! Notez que ce guide d’implémentation est centré autour d’une implémentation Swift, mais les extraits de code Objective-C sont fournis aux personnes intéressées.

## Extensions d’application de contenu de notification

![Deux messages de notification push affichés côte à côte. Le message de droite montre à quoi ressemble une notification push avec l’interface utilisateur par défaut. Le message de droite montre une carte perforée de café poussée par la mise en œuvre d'une interface utilisateur personnalisée.]({% image_buster /assets/img/push_implementation_guide/push1.png %}){: style="max-width:65%;border:0;margin-top:10px"}

Les notifications push, en apparence standard sur différentes plateformes, offrent de très nombreuses options de personnalisation, au-delà de ce qui est normalement implémenté dans l’interface utilisateur par défaut. Lorsqu’une notification push est étendue, les extensions de notification de contenu permettent un affichage personnalisé de la notification push agrandie. 

Les notifications push peuvent être étendues de trois manières différentes : <br>\- Un appui long sur la bannière de notification push<br>\- Faire glisser sur la bannière de notification push<br>\- Faire glisser la bannière vers la gauche et sélectionner « View (Visualiser) » 

Ces vues personnalisées offrent des moyens astucieux d’engager les clients en vous permettant d’afficher de nombreux types de contenu différents, y compris des notifications interactives, des notifications push incluant des données utilisateur, et même des messages push qui peuvent recueillir des informations telles que les numéros de téléphone et l’e-mail. Bien que la mise en œuvre du push de cette manière puisse être peu familière à certains, l'une de nos fonctionnalités bien connues chez Braze, les [Push Stories]({{site.baseurl}}/user_guide/message_building_by_channel/push/advanced_push_options/push_stories/), sont un excellent exemple de ce à quoi peut ressembler une vue personnalisée pour une extension d'app de contenu de notification !

#### Conditions
![]({% image_buster /assets/img/push_implementation_guide/push15.png %}){: style="float:right;max-width:50%;margin-left:10px; border:0;margin-top:10px"}
- [Les notifications push]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/integration/) intégrées avec succès dans votre app.
- iOS 10 ou supérieur
- Les fichiers suivants générés par Xcode en fonction de votre langue de codage :

Swift<br>
- `NotificationViewController.swift`<br>
- `MainInterface.storyboard`<br><br>
Objectif-C<br>
- `NotificationViewController.h`<br>
- `NotificationViewController.m`<br>
- `MainInterface.storyboard`

### Configuration de catégorie personnalisée

Pour configurer un affichage personnalisé dans le tableau de bord, vous devez activer les boutons de notification et saisir votre catégorie personnalisée. La catégorie iOS personnalisée pré-enregistrée que vous fournissez est ensuite vérifiée par rapport à `UNNotificationExtensionCategory` dans le `.plist` de votre cible d’extension de contenu de notification. La valeur donnée ici doit correspondre à ce qui est défini dans le tableau de bord de Braze.

![Les options du bouton de notification se trouvent dans les paramètres du compositeur de messages push.]({% image_buster /assets/img/push_implementation_guide/push16.png %}){: style="max-width:75%;border:0;margin-top:10px"}
![]({% image_buster /assets/img/push_implementation_guide/push17.png %}){: style="max-width:75%;border:0;margin-top:10px"}

{% alert tip %}
Étant donné que les notifications push avec des extensions de contenu ne sont pas toujours apparentes, il est recommandé d’inclure un appel à l’action pour inciter vos utilisateurs à développer leurs notifications push.
{% endalert %}

## Cas d’utilisation et guide d’implémentation

Trois types d’extensions d’application de contenu de notification push sont fournis. Chaque type a une conception conceptuelle, des cas d’utilisation potentiels et un aperçu de la façon dont les variables de notification push peuvent ressembler et être utilisées dans le tableau de bord de Braze :
- [Notification push interactive](#interactive-push-notification)
- [Notifications push personnalisées](#personalized-push-notifications)
- [Notifications push pour le recueil d'informations](#information-capture-push-notification)

### Notification push interactive

Les notifications push peuvent répondre aux actions de l’utilisateur dans une extension de contenu. Pour les utilisateurs exécutant iOS 12 ou une version ultérieure, cela signifie que vous pouvez transformer vos messages push en notifications push entièrement interactives ! Cette interactivité offre de nombreuses possibilités pour impliquer vos utilisateurs au travers de vos notifications. L’exemple suivant montre une notification push dans laquelle les utilisateurs peuvent participer à un jeu sous forme de match une fois la notification étendue.

![Un schéma de ce à quoi pourraient ressembler les phases d’une notification push interactive. Les images montrent un utilisateur appuyant sur une notification push qui affiche un jeu d'association interactif.]({% image_buster /assets/img/push_implementation_guide/push12.png %}){: style="border:0"}

#### Configuration du tableau de bord

Pour configurer une vue personnalisée dans le tableau de bord, dans les paramètres du bouton de notification, entrez la catégorie spécifique que vous souhaitez afficher. Ensuite, dans la `.plist` de votre extension de contenu de notification, vous devez également définir la catégorie personnalisée dans l’attribut `UNNotificationExtensionCategory`. La valeur donnée ici doit correspondre à ce qui est défini dans le tableau de bord de Braze. Enfin, pour activer les interactions utilisateur dans une notification push, définissez la clé `UNNotificationExtensionInteractionEnabled` sur « true ».

![]({% image_buster /assets/img/push_implementation_guide/push3.png %}){: style="float:right;max-width:45%;"}

![Les options du bouton de notification se trouvent dans les paramètres du compositeur de messages push.]({% image_buster /assets/img/push_implementation_guide/push14.png %}){: style="max-width:50%;"}

#### Autres cas d’utilisation
Les extensions de contenu de notifications push sont une option intéressante pour introduire de l’interactivité dans vos promotions et vos applications. Certains exemples incluent un jeu auquel les utilisateurs peuvent jouer, une roue pour gagner des réductions ou un bouton « J’aime » pour enregistrer une liste ou une chanson.

##### Prêt à enregistrer l’analyse ?
Consultez la [section suivante](#logging-analytics) pour mieux comprendre à quoi doit ressembler le flux de données.

### Notifications push personnalisées
![Deux iPhone affichés côte à côte. Le premier iPhone affiche la vue non étendue du message push. Le deuxième iPhone montre la version élargie du message push, qui affiche un aperçu de la progression du cours, de la prochaine session et de la date d'échéance de la prochaine session.]({% image_buster /assets/img/push_implementation_guide/push6.png %}){: style="float:right;max-width:40%;margin-left:15px;border:0"}

Les notifications push peuvent afficher des informations spécifiques à l’utilisateur dans une extension de contenu. L’exemple à droite montre une notification push après qu’un utilisateur a terminé une tâche spécifique (cours d’apprentissage de Braze) et est maintenant encouragé à développer cette notification pour vérifier ses progrès. Les informations fournies ici sont spécifiques à l’utilisateur et peuvent être lancées à la fin de la session ou après une action spécifique de l’utilisateur en tirant parti d’un déclencheur API. 

#### Configuration du tableau de bord

Pour configurer un push personnalisé dans le tableau de bord, vous devez enregistrer la catégorie spécifique que vous souhaitez voir s'afficher, puis, dans les paires clé-valeur à l'aide de Liquid standard, définir les attributs utilisateur appropriés que vous souhaitez voir apparaître dans le message. Ces vues peuvent être personnalisées sur la base des attributs utilisateur spécifiques d’un profil utilisateur donné.

![Quatre ensembles de paires clé-valeur, où "next_session_name" et "next_session_complete_date" sont définis en tant que propriété de déclencheur API à l'aide de Liquid, et "completed_session count" et "total_session_count" sont définis en tant qu'attribut utilisateur personnalisé à l'aide de Liquid.]({% image_buster /assets/img/push_implementation_guide/push5.png %}){: style="max-width:60%;"}

#### Gérer les paires clé-valeur

La méthode suivante, `didReceive` est appelée lorsque l’extension de contenu a reçu une notification, elle est disponible dans le `NotificationViewController`. Les paires clé-valeur fournies dans le tableau de bord sont représentées dans le code par l’utilisation d’un dictionnaire `userInfo`.

**Analyser des paires clé-valeur à partir de notifications push**<br>

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

#### Autres cas d’utilisation

Les idées d’extensions de contenu push basées sur la progression et axées utilisateur sont infinies, certains exemples incluent l’ajout de l’option de partage de votre progression sur différentes plateformes, l’expression de réalisations débloquées, de cartes perforées ou même de listes de contrôle d’intégration. 

##### Prêt à enregistrer l’analyse ?
Consultez la [section suivante](#logging-analytics) pour mieux comprendre à quoi doit ressembler le flux de données.

### Notification push de recueil d’informations

Les notifications push peuvent capturer des informations utilisateur à l’intérieur d’une extension de contenu, ce qui vous permet de repousser les limites de ce qui est possible avec une notification push. En examinant le flux suivant illustré, la vue est en mesure de répondre aux changements d’état. Ces composants de changement d’état sont représentés dans chaque image. 

1. L’utilisateur reçoit une notification push.
2. La notification push est ouverte et invite l’utilisateur à communiquer des informations.
3. Des informations sont fournies et, si elles sont valides, le bouton d’enregistrement s’affiche.
3. La vue de confirmation s’affiche et la notification push est rejetée. 

![]({% image_buster /assets/img/push_implementation_guide/push8.png %}){: style="border:0;"}

Notez que les informations demandées ici peuvent être très variables, comme le recueil de numéros de SMS par ex., et ne doivent pas forcément être en relation avec l’e-mail.

#### Configuration du tableau de bord

Pour configurer une notification push de capture d’information dans le tableau de bord, vous devez enregistrer et définir votre catégorie personnalisée et fournir les paires clé-valeur nécessaires. Comme illustré par l’exemple, vous pouvez également inclure une image dans votre notification push. Pour ce faire, vous devez intégrer les [notifications riches]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/customization/rich_notifications/), définir le style de notification de votre campagne sur Notification riche et inclure une image push riche.

![Une notification push avec trois ensembles de paires clé-valeur. 1\. "Braze_id" défini comme un appel liquide pour récupérer l'ID de Braze. 2\. "cert_title" défini comme "Braze Marketer Certification". 3\. "Cert_description" est défini comme "Entraînement certifié des marketeurs Braze...".]({% image_buster /assets/img/push_implementation_guide/push9.png %})

#### Gérer les actions des boutons

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

##### Rejet des notifications push

Les notifications push peuvent être automatiquement rejetées en appuyant sur un bouton d’action. Il existe trois options de rejet des notifications push prédéfinies recommandées :

1. `completion(.dismiss)` - Rejet de la notification
2. `completion(.doNotDismiss)` - La notification reste ouverte
3. `completion(.dismissAndForward)` - La notification push est rejetée et l’utilisateur est redirigé vers l’application.

#### Autres cas d’utilisation

Demander la contribution des utilisateurs via des notifications push est une formidable opportunité dont de nombreuses entreprises ne profitent pas. Dans ces messages push, vous pouvez non seulement demander des informations de base comme le nom, l’adresse e-mail ou le numéro, mais vous pouvez également inviter les utilisateurs à compléter un profil d’utilisateur s’il ne l’est pas déjà, ou même à soumettre des commentaires. 

##### Prêt à enregistrer l’analyse ?
Consultez la [section suivante](#logging-analytics) pour mieux comprendre à quoi doit ressembler le flux de données. 

## Enregistrer les analyses

### Enregistrer avec l’API Braze (recommandé)

L'enregistrement des analyses peut uniquement se faire en temps réel avec l'aide du serveur du client qui utilise notre endpoint [`/users/track`.]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) Pour enregistrer l’analyse, envoyez la valeur `braze_id` dans le champ des paires clé-valeur (comme indiqué dans la capture d’écran suivante) pour identifier le profil utilisateur à mettre à jour.

![Une notification push avec trois ensembles de paires clé-valeur. 1\. "Braze_id" défini comme un appel liquide pour récupérer l'ID de Braze. 2\. "cert_title" défini comme "Braze Marketer Certification". 3\. "Cert_description" est défini comme "Entraînement certifié des marketeurs Braze...".]({% image_buster /assets/img/push_implementation_guide/push18.png %}){: style="max-width:80%;"}

### Enregistrement manuel

La journalisation manuelle exigera la configuration préalable des groupes d’applications dans Xcode, puis la création, l’enregistrement et la récupération des analyses. Cela nécessitera un travail de développeur personnalisé de votre côté. Les extraits de code suivants vous aideront à résoudre ce problème. 

Il est également important de noter que les analyses ne seront pas envoyées à Braze tant que l’application mobile n’aura pas été lancée subséquemment. Cela signifie que, selon vos paramètres de rejet, il existe souvent une période indéterminée entre le moment où une notification push est rejetée et l’application mobile est lancée et que les analyses sont récupérées. Bien que cette période tampon n’affecte pas tous les cas d’utilisation, les utilisateurs doivent prendre en compte l’impact et, si nécessaire, ajuster leur parcours utilisateur pour inclure l’ouverture de l’application pour répondre à ce problème. 

![Un graphique décrivant la manière dont les analyses sont traitées par Braze. 1\. Les données d'analyse sont créées. 2\. Les données d'analyse sont enregistrées. 3\. La notification push est rejetée. 4\. Période indéterminée entre le moment où la notification push est rejetée et l’application mobile est lancée. 5\. L’application mobile est lancée. 6\. Les données d'analyse sont reçues. 7\. Les données analytiques sont envoyées à Braze.]({% image_buster /assets/img/push_implementation_guide/push13.png %})

#### Étape 1 : Configurer les groupes d'applications dans Xcode
Ajouter une capacité `App Groups`. Si vous n’avez pas de groupe d'applications dans votre application, allez sur Capacité de la cible de l’application principale, activez `App Groups`, et cliquez sur le bouton « + ». Utilisez l’ID de l’ensemble de votre application pour créer le groupe d'applications. Par exemple, si l’ID de l’ensemble de votre application est `com.company.appname`, vous pouvez nommer votre groupe d'applications `group.com.company.appname.xyz`. Assurez-vous que les `App Groups` sont activés pour la cible de votre application principale et la cible de l’extension de contenu.

![]({% image_buster /assets/img/ios/push_story/add_app_groups.png %})

#### Étape 2 : Intégrer les extraits de code
Les extraits de code suivants sont une référence utile sur la façon d’enregistrer et d’envoyer des événements personnalisés, des attributs personnalisés et des attributs utilisateur. Ce guide sera en cours de conversation par défaut d’utilisateur, mais la représentation du code sera sous la forme d’un fichier d’aide `RemoteStorage`. Il existe également des fichiers auxiliaires supplémentaires `UserAttributes` et `EventName Dictionary` utilisés lors de l’envoi et de l’enregistrement des attributs utilisateur. Tous les fichiers d’aide sont disponibles à la fin de ce guide.

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

Une fois le SDK initialisé, c’est le bon moment pour consigner toutes les analyses enregistrées à partir d’une extension d’application de contenu de notification. Pour ce faire, vous pouvez parcourir tous les événements en attente, en vérifiant la clé « Event Name », en définissant les valeurs appropriées dans Braze, puis en effaçant l’enregistrement pour la prochaine fois que cette fonction sera nécessaire.

1. Passez en revue la série d’événements en attente
2. Passez en revue chaque paire clé-valeur dans le dictionnaire `pendingEvents`
3. En vérifiant explicitement la clé pour « Event Name » afin de définir la valeur en conséquence
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
      logCustomEvent(eventName, withProperties: properties)
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
      [[Appboy sharednstance] logCustomEvent:eventName withProperties:properties];
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

Une fois le SDK initialisé, c’est le bon moment pour consigner toutes les analyses enregistrées à partir d’une extension d’application de contenu de notification. Pour ce faire, vous pouvez parcourir tous les attributs en attente, en définissant l’attribut personnalisé approprié dans Braze, puis en effaçant l’enregistrement pour la prochaine fois que cette fonction sera nécessaire.

1. Passez en revue la série d’attributs en attente
2. Passez en revue chaque paire clé-valeur dans le dictionnaire `pendingAttributes`
3. Enregistrer l’attribut personnalisé individuel avec la clé et la valeur correspondantes
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

Lors de l’enregistrement des attributs utilisateur, il est recommandé de créer un objet personnalisé pour déchiffrer le type d’attribut en cours de mise à jour (`email`, `first_name`, `phone_number`, etc.). L’objet doit être compatible avec ce qui a été stocké/récupéré dans `UserDefaults`. Voir le fichier d’aide `UserAttribute` pour un exemple de la manière d’y parvenir.

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

Une fois le SDK initialisé, c’est le bon moment pour consigner toutes les analyses enregistrées à partir d’une extension d’application de contenu de notification. Pour ce faire, vous pouvez parcourir tous les attributs en attente, en définissant l’attribut personnalisé approprié dans Braze, puis en effaçant l’enregistrement pour la prochaine fois que cette fonction sera nécessaire.

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


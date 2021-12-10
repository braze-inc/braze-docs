---
nav_title: Implémentation avancée (facultatif)
article_title: Implémentation avancée des notifications Push pour iOS (facultatif)
platform: iOS
page_order: 29
description: "Ce guide de mise en œuvre avancé explique comment tirer parti des extensions des applications de notification push iOS pour tirer le meilleur parti de vos messages push. On y trouve également trois cas d'utilisation construits par notre équipe, des extraits de code accompagnateurs et des conseils sur les analyses de log."
channel:
  - Pousser
---

<br>
{% alert important %}
Vous recherchez le guide d'intégration des développeurs Push ? Trouvez-le [ici]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/integration/).
{% endalert %}

# Guide d'implémentation des notifications push

> Ce guide de mise en œuvre optionnel et avancé couvre les moyens d'exploiter les extensions des applications de contenu de notification push pour tirer le meilleur parti de vos messages push. Il y a trois cas d'utilisation personnalisée construits par notre équipe, des extraits de code accompagnateurs et des conseils sur les analyses de log. Visitez notre Dépôt de Démo de Braze [ici](https://github.com/braze-inc/braze-growth-shares-ios-demo-app)! Veuillez noter que ce guide de mise en œuvre est centré sur une implémentation Swift, mais des extraits Objective-C sont fournis pour ceux qui sont intéressés.

## Extensions du contenu des applications de notification

!\[Extension de Contenu Push\]\[1\]{: style="max-width:65%;border:0;margin-top:10px"}

Les notifications push alors qu'elles semblent standard sur différentes plateformes, offrent d'immenses options de personnalisation au-delà de ce qui est normalement implémenté dans l'interface par défaut. Lorsqu'une notification push est étendue, les extensions de notification de contenu activent une vue personnalisée de la notification push étendue.

Les notifications push peuvent être étendues de trois manières différentes : <br>- Un appui long sur la bannière push<br>- Glisser vers le bas sur la bannière push<br>- Glisser la bannière vers la gauche et sélectionner "Voir"

Ces vues personnalisées offrent des moyens intelligents d'impliquer les clients vous permettant d'afficher de nombreux types de contenu distincts, y compris des notifications interactives, des notifications remplies de données utilisateur et même de messages push qui peuvent capturer des informations telles que les numéros de téléphone et les courriels. Alors que l'implémentation de la poussée de cette manière peut ne pas être familière à certains, l'une de nos caractéristiques bien connues au Brésil, [Les Histoires Push]({{site.baseurl}}/user_guide/message_building_by_channel/push/advanced_push_options/push_stories/), sont un excellent exemple de ce à quoi une vue personnalisée pour une extension de contenu de notification peut ressembler !

#### Exigences:
!\[Push Content Extension\]\[15\]{: style="float:right;max-width:50%;margin-left:10px; border:0;margin-top:10px"}
- [Notifications Push]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/integration/) intégrées avec succès dans votre application
- iOS 10 ou supérieur
- Les fichiers suivants générés par Xcode en fonction de votre langage de codage :

Swift<br> &#45; `NotificationViewController.swift`<br> &#45; `Interface principale. tableau de bord`<br><br> Objective-C<br> &#45; `NotificationViewController.`<br> &#45; `NotificationViewController.m`<br> &#45; `PrincipInterface.storyboard`

### Configuration de la catégorie personnalisée

Pour configurer une vue personnalisée dans le tableau de bord, vous devez basculer sur les boutons de notification et entrer votre catégorie personnalisée. La catégorie iOS personnalisée préenregistrée que vous fournissez est ensuite vérifiée avec la `UNNotificationExtensionCategory` dans le `. liste` de votre cible d'extension de contenu de notification. La valeur donnée ici doit correspondre à ce qui est défini dans le tableau de bord Braze.

!\[Push Content Extension\]\[16\]{: style="max-width:75%;border:0;margin-top:10px"} !\[Push Content Extension\]\[17\]{: style="max-width:75%;border:0;margin-top:10px"}

{% alert tip %}
Puisque les pushes avec des extensions de contenu ne sont pas toujours apparentes, il est recommandé d'inclure un appel à l'action pour inciter vos utilisateurs à étendre leurs notifications push.
{% endalert %}

## Utiliser le cas et la mise en œuvre

Il y a trois types d'extension pour les applications de notification push. Chaque type a un concept walkthrough, cas d'utilisation potentiels, et voir comment les variables de notification push peuvent être utilisées dans le tableau de bord Braze :
- [Notification Push interactive](#interactive-push-notification)
- [Notifications Push personnalisées](#personalized-push-notifications)
- [Notifications de capture d'informations](#information-capture-push-notification)

### Notification push interactive

Les notifications push peuvent répondre aux actions de l'utilisateur dans une extension de contenu. Pour les utilisateurs utilisant iOS 12 ou plus récent, cela signifie que vous pouvez transformer vos messages push en notifications push entièrement interactives ! Cette interactivité offre de nombreuses possibilités pour que vos utilisateurs s'engagent dans vos notifications. L'exemple ci-dessous montre un push où les utilisateurs sont en mesure de jouer un match dans la notification étendue.

!\[Extension de Contenu Push\]\[12\]{: style="border:0"}

#### Configuration du tableau de bord

Pour configurer une vue personnalisée dans le tableau de bord, dans les paramètres du bouton de notification, entrez la catégorie spécifique que vous souhaitez afficher. Ensuite, dans le `.plist` de votre extension de contenu de notification, vous devez également définir la catégorie personnalisée à l'attribut `UNNotificationExtensionCategory`. La valeur donnée ici doit correspondre à ce qui est défini dans le tableau de bord Braze. Enfin, pour activer les interactions utilisateur dans une notification push, définissez la touche `UNNotificationExtensionInteractionEnabled` à true.

!\[Exemple\]\[3\]{: style="float:right;max-width:45%;"}

!\[Exemple\]\[14\]{: style="max-width:50%;"}

#### Autres cas d'utilisation
Les extensions de contenu Push sont une option excitante pour introduire l'interactivité dans vos promotions et applications. Quelques exemples incluent un jeu pour les utilisateurs à jouer, une roue spin-to-win pour les remises, ou un bouton « like » pour enregistrer une annonce ou une chanson.

##### Prêt à enregistrer des analyses ?
Visitez la section [suivante](#logging-analytics) pour mieux comprendre à quoi devrait ressembler le flux de données.

### Notifications push personnalisées
!\[Exemple\]\[6\]{: style="float:right;max-width:40%;margin-left:15px;border:0"}

Les notifications push peuvent afficher des informations spécifiques à l'utilisateur dans une extension de contenu. L'exemple à droite montre une notification push après qu'un utilisateur a terminé une tâche spécifique (Braze LAB cours) et est maintenant encouragé à étendre cette notification pour vérifier leur progression. Les informations fournies ici sont spécifiques à l'utilisateur et peuvent être désactivées au moment où une session est terminée ou une action spécifique de l'utilisateur est prise en utilisant un déclencheur d'API.

#### Configuration du tableau de bord

Pour configurer un push personnalisé dans le tableau de bord, vous devez enregistrer la catégorie spécifique que vous souhaitez afficher, puis dans les paires clé-valeur en utilisant Liquid standard, définissez les attributs utilisateur appropriés que vous voulez voir dans le message. Ces vues peuvent être personnalisées en fonction des attributs spécifiques d'un utilisateur d'un profil utilisateur spécifique.

!\[Exemple de tableau de bord Push personnalisé\]\[5\]{: style="max-width:60%;"}

#### Manipulation des paires clé-valeur

La méthode ci-dessous, `didReceive` est appelée lorsque l'extension de contenu a reçu une notification, il peut être trouvé dans le `NotificationViewController`. Les paires clé-valeur fournies dans le tableau de bord sont représentées dans le code à travers l'utilisation d'un dictionnaire `userInfo`.

__Parsing Key-Value Pairs from Push Notifications__<br>

{% tabs %}
{% tab Swift %}
``` swift 
func didReceive(_ notification: UNNotification) {
  let userInfo = notification.request.content.userInfo

  garde let value = userInfo["VOTRE-KEY-VALUE-PAIR"] comme? String,
        let otherValue = userInfo["VOTRE-AUTRE-VALUE-PAIR"] comme? Chaîne,
  else { fatalError("Les paires de valeurs sont incorrectes.")}

  ...
}
```
{% endtab %}
{% tab Objective-C %}
```objc
- (void)didReceiveNotification:(nonnull UNNotification *)notification {
  NSDictionary *userInfo = notification.request.content.userInfo;

  if (userInfo[@"YOUR-KEY-VALUE-PAIR"] && userInfo[@"VOTRE-KEY-VALUE-PAIR"]) {



  } else {
    [NSException raise:NSGenericException format:@"Key-Value Pairs are incorrect"];
  }
}
```
{% endtab %}
{% endtabs %}

#### Autres cas d'utilisation

Les idées d'extensions de contenu push axées sur les progrès et les utilisateurs sont infinies, quelques exemples incluent l'ajout de l'option de partager vos progrès sur différentes plateformes, d'exprimer des réalisations débloquées, des cartes de punch ou même des listes de contrôle d'intégration.

##### Prêt à enregistrer des analyses ?
Visitez la section [suivante](#logging-analytics) pour mieux comprendre à quoi devrait ressembler le flux de données.

### Notification de capture d'informations push

Les notifications push peuvent capturer les informations de l'utilisateur à l'intérieur d'une extension de contenu, vous permettant de pousser les limites de ce qui est possible avec une push. En examinant le flux affiché ci-dessous, la vue est en mesure de répondre aux changements d'état. Ces composants de changement d'état sont représentés dans chaque image.

1. L'utilisateur reçoit une notification push.
2. Push est ouvert et invite l'utilisateur à s'informer.
3. Les informations sont fournies et, si elles sont valides, le bouton d'enregistrement est affiché.
3. La vue de confirmation est affichée, et le push est rejeté.

!\[Information Capture Push Dashboard Example\]\[8\]{: style="border:0;"}

Notez que les informations demandées ici peuvent être un large éventail de choses telles que la capture de numéros de SMS, il ne doit pas être spécifique à l'e-mail.

#### Configuration du tableau de bord

Pour configurer une capture d'informations capable de pousser dans le tableau de bord, vous devez enregistrer et définir votre catégorie personnalisée et fournir les paires clé-valeur qui sont nécessaires. Comme on le voit dans l’exemple, vous pouvez aussi inclure une image dans votre push. Pour cela, vous devez intégrer [les notifications riches]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/rich/), définissez le style de notification de votre campagne à Rich Notification, et incluez une image poussée riche.

!\[Information Capture Push Dashboard Exemple\]\[9\]

#### Gestion des actions des boutons

Chaque bouton d'action est identifié de manière unique. Le code vérifie si votre identifiant de réponse est égal au `actionIndentifier`, et si oui, sait que l'utilisateur a cliqué sur le bouton d'action.

__Manipulation des réponses des boutons de notification__<br>

{% tabs %}
{% tab Swift %}
``` swift 
func didReceive(_ response: UNNotificationResponse, completionHandler completion: @escaping (UNNotificationContentExtensionResponseOption) -> Void) {
  si réponse. ctionIdentifier == "VOTRE REGISTRE-IDENTIFIER" {
    // fait quelque chose
  } else {
    // fait autre chose
  }
 } } } }
```
{% endtab %}
{% tab Objective-C %}
```objc
- (void)didReceiveNotificationResponse:(UNNotificationResponse *)response completionHandler:(void (^)(UNNotificationContentExtensionResponseOption))completion {
  if ([response.actionIdentifier isEqualToString:@"YOUR-REGISTER-IDENTIFIER"]) {
    completion(UNNotificationContentExtensionResponseOptionDismiss);
  } else {
    completion(UNNotificationContentExtensionResponseOptionDoNotDismiss);
  }

```
{% endtab %}
{% endtabs %}

##### Refuser les poussées

Les notifications push peuvent être automatiquement rejetées à partir d'un appui sur un bouton d'action. Il existe trois options de rejet push pré-compilées qui sont recommandées :

1. `completion(.dismis)` - Rejette la notification
2. `completion(.doNotDismiss)` - La notification reste ouverte
3. `completion(.dismissAndForward)` - Pousser rejette et l'utilisateur est transféré dans l'application.

#### Autres cas d'utilisation

Demander des commentaires par le biais de notifications push est une occasion passionnante dont beaucoup d'entreprises ne profitent pas. Dans ces messages push, vous ne pouvez pas seulement demander des informations de base comme le nom, l'e-mail ou le numéro, mais vous pouvez également demander aux utilisateurs de compléter un profil utilisateur si inachevé, ou même de soumettre des commentaires.

##### Prêt à enregistrer des analyses ?
Visitez la section ci-dessous pour mieux comprendre à quoi devrait ressembler le flux de données.

## Analyses de la journalisation

### Journalisation avec l'API Braze (recommandé)

L'analyse de journalisation ne peut être effectuée en temps réel qu'avec l'aide du serveur du client qui touche l'API [utilisateurs/suivi]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) du point de terminaison de l'API de Braze. Pour enregistrer les analyses, envoyer vers le bas la valeur `braze_id` dans le champ des paires clé-valeur (comme vu dans la capture d'écran ci-dessous) pour identifier quel profil utilisateur mettre à jour.

!\[Exemple de tableau de bord Push personnalisé\]\[18\]{: style="max-width:80%;"}

### Logs manuellement

La journalisation manuelle vous demandera d’abord de configurer les groupes d’applications dans Xcode, puis de créer, enregistrer et récupérer les analyses. Cela nécessitera un travail de développement personnalisé de votre côté. Les extraits de code affichés ci-dessous vous aideront à résoudre ce problème.

Il est également important de noter que les analyses ne sont pas envoyées à Braze tant que l'application mobile n'est pas lancée par la suite. Cela signifie que, selon vos paramètres de licenciement, il existe souvent une période de temps indéterminée entre le moment où une notification push est rejetée et l'application mobile est lancée et les analyses sont récupérées. Bien que ce tampon de temps ne puisse pas affecter tous les cas d'utilisation, les utilisateurs devraient tenir compte de l'impact et, si nécessaire, ajuster leur parcours utilisateur pour inclure l'ouverture de l'application pour répondre à cette préoccupation.

!\[Logging Push\]\[13\]

#### Étape 1 : Configurer les groupes d'applications dans Xcode
Ajouter une capacité `Groupes d'applications`. Si vous n'avez pas eu de groupe d'applications dans votre application, allez à la capacité de la cible principale de l'application, activez les `Groupes d'applications`, et cliquez sur le « + ». Utilisez l'ID du bundle de votre application pour créer le groupe d'applications. Par exemple, si l'ID du bundle de votre application est `com.company.appname`, vous pouvez nommer votre groupe d'application `group.com.company.appname.xyz`. Assurez-vous que les `Groupes d'application` sont activés à la fois pour la cible de votre application principale et la cible de l'extension de contenu.

!\[Ajouter des groupes d'applications\]\[19\]

#### Étape 2 : Intégrer des extraits de code
Les extraits de code suivants sont une référence utile sur la façon d'enregistrer et d'envoyer des événements personnalisés, des attributs personnalisés et des attributs utilisateurs. Ce guide parlera en termes de valeurs par défaut, mais la représentation de code sera sous la forme d'un fichier d'aide  `Remote Storage`. Il existe également des fichiers d'aide supplémentaires `UserAttributes` et `EventName Dictionary` qui sont utilisés lors de l'envoi et de l'enregistrement des attributs de l'utilisateur. Tous les fichiers d'aide se trouvent ci-dessous.

{% tabs local %}
{% tab Custom Events %}

##### Enregistrement des événements personnalisés

Pour enregistrer des événements personnalisés, vous devez créer les analytiques à partir de zéro. Cela se fait en créant un dictionnaire, en le remplissant avec des métadonnées, et en sauvegardant les données à l'aide d'un fichier d'aide.

1. Initialiser un dictionnaire avec les métadonnées de l'événement
2. Initialiser `userDefaults` pour récupérer et stocker les données de l'événement
3. S'il y a un tableau existant, ajoutez de nouvelles données au tableau existant et enregistrez
4. S'il n'y a pas de tableau existant, enregistrez le nouveau tableau dans `userDefaults`

{% subtabs global %}
{% subtab Swift %}
``` swift 
func saveCustomEvent(avec properties: [String: Any]? = nil) {
  // 1
  let customEventDictionary = Dictionary(eventName: "VOTRE EVENT-NOM", properties: properties)

  // 2
  let remoteStorage = RemoteStorage(storageType: . uite)

  // 3   
  if var pendingEvents = remoteStorage.retrieve(forKey: .pendingCustomEvents) as? [[String: Any]] {
    pendingEvents.append(contentsOf: [customEventDictionary])
    remoteStorage.store(pendingEvents, forKey: . endingCustomEvents)
  } else {
  // 4
    remoteStorage. tore([customEventDictionary], forKey : .pendingCustomEvents)
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

##### Envoi d'événements personnalisés à Braze

Une fois le SDK initialisé est le meilleur moment pour enregistrer toutes les analyses enregistrées depuis une extension de contenu de notification. Cela peut être fait en bouclant les événements en attente, en vérifiant la clé "Nom de l'événement", définissant les valeurs appropriées au Brésil, puis vider le stockage pour la prochaine fois que cette fonction est nécessaire.

1. Boucler le tableau des événements en attente
2. Faites défiler chaque paire clé-valeur dans le dictionnaire `pendingEvents`
3. Vérification explicite de la clé pour "Nom de l'événement" pour définir la valeur en conséquence
4. Toute autre valeur de clé sera ajoutée au dictionnaire `propriétés`
5. Journaliser un événement personnalisé
6. Supprimer tous les événements en attente du stockage

{% subtabs global %}
{% subtab Swift %}
``` swift 
func logPendingCustomEventsIfNecessary() {
  let remoteStorage = RemoteStorage(storageType: .suite)
  guard let pendingEvents = remoteStorage.retrieve(forKey: .pendingCustomEvents) comme? [[String: Any]] else { return }

  // 1    
  for event in pendingEvents {
    var eventName: String?
    Propriétés de var : [AnyHashable: Any] = [:]

  // 2
    pour (key, valeur) dans l'éventualité {
      if key == PushNotificationKey. 

 ventName. awValue {
  // 3      
        si vous laissez eventNameValue = value comme? String {
          eventName = eventNameValue
        } else {
          print("Type non valide pour event_name key")
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


  // 6    
  remoteStorage. emoveObject(forKey: .pendingCustomEvents)
}
```
{% endsubtab %}
{% subtab Objective-C %}
```objc
- (void)logPendingEventsIfNecessary {
  RemoteStorage *remoteStorage = [[RemoteStorage alloc] initWithStorageType:StorageTypeSuite];
  NSArray *pendingEvents = [remoteStorage retrieveForKey:RemoteStorageKeyPendingCustomEvents];

  // 1 
  pour (NSDictionary<NSString *, id> *event in pendingEvents) {
    NSString *eventName = nil;
    NSMutableDictionary *Propriétés = [NSMutableDictionary dictionary] ;

  // 2 
    pour la clé (NSString* en événement) {
      if ([key isEqualToString:@"event_name"]) {
  // 3       
        if ([[event objectForKey:key] isKindOfClass:[NSString class]]) {
          eventName = [event objectForKey:key];
        } else {
          NSLog(@"Type non valide pour la clé event_name");
        }
      } else {
  // 4 
        properties[key] = event[key];
      }
    }
  // 5  
    if (eventName ! nil) {
      [[Appboy sharednstance] logCustomEvent:eventName withProperties:properties];
    }
  }

  // 6  
  [remoteStorage remoteObjectForKey:RemoteStorageKeyPendingCustomEvents];
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Custom Attributes %}

##### Enregistrement des attributs personnalisés

Pour enregistrer des attributs personnalisés, vous devez créer les analytiques à partir de zéro. Cela se fait en créant un dictionnaire, en le remplissant avec des métadonnées, et en sauvegardant les données à l'aide d'un fichier d'aide.

1. Initialiser un dictionnaire avec les métadonnées d'attribut
2. Initialiser `userDefaults` pour récupérer et stocker les données de l'attribut
3. S'il y a un tableau existant, ajoutez de nouvelles données au tableau existant et enregistrez
4. S'il n'y a pas de tableau existant, enregistrez le nouveau tableau dans `userDefaults`

{% subtabs global %}
{% subtab Swift %}
``` swift 
func saveCustomAttribute() {
  // 1 
  let customAttributeDictionary: [String: Any] = ["YOUR-CUSTOM-ATTRIBUTE-KEY": "YOUR-CUSTOM-ATTRIBUTE-VALUE"]

  // 2 
  let remoteStorage = RemoteStorage(storageType: . uite)

  // 3 
  if var pendingAttributes = remoteStorage.retrieve(forKey: .pendingCustomAttributes) as? [[String: Any]] {
    pendingAttributes.append(contentsOf: [customAttributeDictionary])
    remoteStorage.store(pendingAttributes, forKey: . endingCustomAttributes)
  } else {
  // 4 
    remoteStorage. tore([customAttributeDictionary], forKey : .pendingCustomAttributes)
  }
}
```
{% endsubtab %}
{% subtab Objective-C %}
``` objc
- (void)saveCustomAttribute {
  // 1 
  NSDictionary<NSString *, id> *customAttributeDictionary = @{ @"YOUR-CUSTOM-ATTRIBUTE-KEY": @"YOUR-CUSTOM-VALUE" };

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

##### Envoi d'attributs personnalisés à Braze

Une fois le SDK initialisé est le meilleur moment pour enregistrer toutes les analyses enregistrées depuis une extension de contenu de notification. Cela peut être fait en bouclant les attributs en attente, en définissant l'attribut personnalisé approprié en Brésil, puis vider le stockage pour la prochaine fois que cette fonction est nécessaire.

1. Boucler le tableau des attributs en attente
2. Faites défiler chaque paire clé-valeur dans le dictionnaire `pendingAttributes`
3. Loguer chaque attribut personnalisé avec la clé et la valeur correspondantes
4. Supprimer tous les attributs en attente du stockage

{% subtabs global %}
{% subtab Swift %}
``` swift 
func logPendingCustomAttributesIfNecessary() {
  let remoteStorage = RemoteStorage(storageType: .suite)
  guard let pendingAttributes = remoteStorage.retrieve(forKey: .pendingCustomAttributes) comme? [[String: Any]] else { return }

  // 1
  pendingAttributes. orChaque { setCustomAttributesWith(keysAndValues: $0) }

  // 4 
  remoteStorage.removeObject(forKey: . endingCustomAttributes)
}

func setCustomAttributesWith(keysAndValues: [String: Any]) {
  // 2 
  for (key, valeur) dans keysAndValues {
  // 3
    si let value = value comme? [String] {
      setCustomAttributeArrayWithKey(key, andValue: value)
    } else {
      setCustomAttributeWithKey(key, andValue: value)
    }
  }
 } }
```
{% endsubtab %}
{% subtab Objective-C %}
```objc
- (void)logPendingCustomAttributesIfNecessary {
  RemoteStorage *remoteStorage = [[RemoteStorage alloc] initWithStorageType:StorageTypeSuite];
  NSArray *pendingAttributes = [remoteStorage retrieveForKey:RemoteStorageKeyPendingCustomAttributes];

  // 1
  pour l'attribut (NSDictionary<NSString*, id> *en pendingAttributes) {
    [self setCustomAttributeWith:attribute];
  }

  // 4 
  [remoteStorage removeObjectForKey:RemoteStorageKeyPendingCustomAttributes];
}

- (void)setCustomAttributeWith:(NSDictionary<NSString *, id> *)keysAndValues {
  // 2
  pour (NSString *key in keysAndValues) {
  // 3 
    [self setCustomAttributeWith:key andValue:[keysAndValues objectForKey:key]];
  }
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab User Attributes %}

##### Enregistrement des attributs de l'utilisateur

Lors de l'enregistrement des attributs de l'utilisateur, il est recommandé de créer un objet personnalisé pour déchiffrer quel type d'attribut est en cours de mise à jour (`email`, `prénom`, `phone_number`, etc.). L'objet doit être compatible avec être stocké/récupéré à partir de `UserDefaults`. Voir le fichier d'aide `UserAttribute` pour un exemple de la façon d'accomplir cela.

1. Initialiser un objet `UserAttribute` encodé avec le type correspondant
2. Initialiser `userDefaults` pour récupérer et stocker les données de l'événement
3. S'il y a un tableau existant, ajoutez de nouvelles données au tableau existant et enregistrez
4. S'il n'y a pas de tableau existant, enregistrez le nouveau tableau dans `userDefaults`

{% subtabs global %}
{% subtab Swift %}
``` swift 
func saveUserAttribute() {
  // 1 
  garde let data = essayer? PropertyListEncoder().encode(UserAttribute.userAttributeType("USER-ATTRIBUTE-VALUE")) else { return }

  // 2       
  let remoteStorage = RemoteStorage(storageType: .suite)

  // 3    
  if var pendingAttributes = remoteStorage.retrieve(forKey: .pendingUserAttributes) comme? [Data] {
    pendingAttributes.append(contentsOf: [data])
    remoteStorage.store(pendingAttributes, forKey: . endingUserAttributes)
  } else {
  // 4 
    remoteStorage. tore([data], forKey : .pendingUserAttributes)
  }
 } }
```
{% endsubtab %}
{% subtab Objective-C %}
```objc
- (void)saveUserAttribute {
  // 1 
  UserAttribute *userAttribute = [[UserAttribute alloc] initWithUserField:@"USER-ATTRIBUTE-VALUE" attributeType:UserAttributeTypeEmail];

  NSError *error;
  NSData *data = [NSKeyedArchiver archivedDataWithRootObject:userAttribute requiringSecureCoding:YES error:&error];

  if (error ! nil) {
    // erreur de log
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

##### Envoi des attributs de l'utilisateur à Braze

Une fois le SDK initialisé est le meilleur moment pour enregistrer toutes les analyses enregistrées depuis une extension de contenu de notification. Cela peut être fait en bouclant les attributs en attente, en définissant l'attribut personnalisé approprié en Brésil, puis vider le stockage pour la prochaine fois que cette fonction est nécessaire.

1. Boucler à travers la table de données `pendingAttributes`
2. Initialiser un objet `UserAttribute` encodé à partir des données de l'attribut
3. Définir un champ utilisateur spécifique basé sur le type d'attribut utilisateur (email)
4. Supprimer tous les attributs utilisateur en attente du stockage

{% subtabs global %}
{% subtab Swift %}
``` swift 
func logPendingUserAttributesIfNecessary() {
  let remoteStorage = RemoteStorage(storageType: .suite)
  guard let pendingAttributes = remoteStorage.retrieve(forKey: .pendingUserAttributes) comme? [Data] else { return }

  // 1    
  pour attributeData in pendingAttributes {
  // 2 
    garde let userAttribute = essayer? PropertyListDecoder().decode(UserAttribute. elf, from: attributeData) else { continue }

  // 3    
    switch userAttribute {
    case . mail(laissez e-mail):
      utilisateur?. mail = email
    }
  }
  // 4   
  remoteStorage. emoveObject(forKey: .pendingUserAttributes)
}
```
{% endsubtab %}
{% subtab Objective-C %}
```objc
- (void)logPendingUserAttributesIfNecessary {
  RemoteStorage *remoteStorage = [[RemoteStorage alloc] initWithStorageType:StorageTypeSuite];
  NSArray *pendingAttributes = [remoteStorage retrieveForKey:RemoteStorageKeyPendingUserAttributes];

  // 1  
  pour (NSData *attributeData in pendingAttributes) {
    NSError *error;

  // 2 
    UserAttribute *userAttribute = [NSKeyedUnarchiver unarchivedObjectOfClass:[UserAttribute class] fromData:attributeData error:&error];

    si (erreur ! nil) {
      // erreur de log
    }

  // 3  
    if (userAttribute) {
      switch (userAttribute. ttributeType) {
        case UserAttributeTypeEmail:
          [self-user]. mail = attribut utilisateur. serField;
          break;
      }
    }
  }
  // 4 
  [remoteStorage remoteObjectForKey:RemoteStorageKeyPendingUserAttributes];
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Helper Files %}

##### Fichiers d'aide

{% details RemoteStorage Helper File %}
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
  private var storageType : RemoteStorageType = . tandard
  private lazy var defaults: UserDefaults = {
    switch storageType {
    case . tandard :
      return .standard
    case . uite :
      return UserDefaults(suiteName: "VOTRE-DOMAIN-IDENTIFIER")!
    }
  }()

  init(storageType: RemoteStorageType = .standard) {
    soi. torageType = storageType
  }

  func store(_ value: Any, forKey key: RemoteStorageKey) {
    par défaut. et(value, forKey : key.rawValue)
  }

  func retrieve(forKey : RemoteStorageKey) -> Any? {
    return defaults.object(forKey: key. awValue)
  }

  func removeObject(clé forKey : RemoteStorageKey) {
    defaults.removeObject(forKey: key. awValue)
  }

  func resetStorageKeys() {
    pour la clé dans RemoteStorageKey. llCases {
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
    self. torageType = stockageType;
  }
  retourne soi-même;
}

- (void)store:(id)value forKey:(RemoteStorageKey)key {
  [[self defaults] setValue:value forKey:[self-rawValueForKey:key]];
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
  if (! elfe efaults) {
    interrupteur (soi. torageType) {
      case StorageTypeStandard:
        return [NSUserDefaults standardUserDefaults];
        pause;
      case StorageTypeSuite :
        return [[NSUserDefaults alloc] initWithSuiteName:@"VOTRE DOMAIN-IDENTIFIER"];
    }
  } else {
    return self épouvantailles;
  }
}

- (NSString*)rawValueForKey:(RemoteStorageKey)remoteStorageKey {
    switch(remoteStorageKey) {
    case RemoteStorageKeyPendingCustomEvents:
      return @"pending_custom_events";
    cas RemoteStorageKeyPendingCustomAttributes:
      return @"pending_custom_attributes";
    cas RemoteStorageKeyPendingUserAttributes:
      return @"pending_user_attributes";
    par défaut:
      [Augmentation d'une exception NSException:NSGenericException format:@"FormatType inattendu. ];
  }
}
```
{% endsubtab %}
{% endsubtabs %}
{% enddetails %}
{% details UserAttribute Helper File %}
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

  func encode(encodeur : Encoder) lance {
    var values = encoder. ontainer(keyedBy: CodingKeys.self)

    changer de case {
    . mail(e-mail de laisse):
      valeurs d'essai. ncode(email, forKey: . mail)
    }
  }

  init(from decoder: Decoder) lance {
    let values = try decoder. ontainer(keyedBy: CodingKeys.self)

    let email = essayer values.decode(String. elf, forKey : .email)
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
    self. serField = userField;
    soi. ttributeType = attributeType;
  }
  return self;
}

- (void)encodeWithCoder:(NSCoder *)encoder {
  [encoder encodeObject:self. serField forKey:@"userField"];
  [encodeur encodeInteger:self. ttributeType forKey:@"attributeType"];
}

- (id)initWithCoder:(NSCoder *)decoder {
  if (self = [super init]) {
    self. serField = [decoder decodeObjectForKey:@"userField"];

    NSInteger attributeRawValue = [decoder decodeIntegerForKey:@"attributeType"];
    même. ttributeType = (UserAttributeType) attributeRawValue;
  }
  return self;
}

@end
```
{% endsubtab %}
{% endsubtabs %}
{% enddetails %}
{% details EventName Dictionary Helper File %}
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
  retour auto ;
}

@end
```
{% endsubtab %}
{% endsubtabs %}
{% enddetails %}
<br>
{% endtab %}
{% endtabs %}
[1]: {% image_buster /assets/img/push_implementation_guide/push1.png %} [3]: {% image_buster /assets/img/push_implementation_guide/push3. ng %} [5]: {% image_buster /assets/img/push_implementation_guide/push5.png %} [6]: {% image_buster /assets/img/push_implementation_guide/push6. ng %} [8]: {% image_buster /assets/img/push_implementation_guide/push8.png %} [9]: {% image_buster /assets/img/push_implementation_guide/push9.png %} [12]: {% image_buster /assets/img/push_implementation_guide/push12. ng %} [13]: {% image_buster /assets/img/push_implementation_guide/push13.png %} [14]: {% image_buster /assets/img/push_implementation_guide/push14. ng %} [15]: {% image_buster /assets/img/push_implementation_guide/push15.png %} [16]: {% image_buster /assets/img/push_implementation_guide/push16. ng %} [17]: {% image_buster /assets/img/push_implementation_guide/push17.png %} [18]: {% image_buster /assets/img/push_implementation_guide/push18. ng %} [19]: {% image_buster /assets/img/ios/push_story/add_app_groups.png %}

{% multi_lang_include developer_guide/prerequisites/swift.md %} Vous devrez également [configurer les notifications push]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift).

{% alert note %}
Ce guide d’implémentation est centré sur une implémentation Swift, mais des extraits de code Objective-C sont fournis aux personnes intéressées.
{% endalert %}

## Extensions d’application de contenu de notification

![Deux messages de notification push affichés côte à côte. Le message de gauche montre à quoi ressemble un envoi avec l'interface utilisateur par défaut. Le message de droite montre une notification push de carte de fidélisation pour du café, réalisée en implémentant une interface utilisateur de notification push personnalisée.]({% image_buster /assets/img/push_implementation_guide/push1.png %}){: style="max-width:65%;border:0;margin-top:10px"}

Les extensions d'applications de contenu de notification constituent une excellente option de personnalisation des notifications push. Les extensions d'apps de contenu de notification affichent une interface personnalisée pour les notifications de votre app lorsqu'une notification push est développée.

Les notifications push peuvent être étendues de trois manières différentes :
- Un appui long sur la bannière de notification push
- Faire glisser sur la bannière de notification push
- Faire glisser la bannière vers la gauche et sélectionner « Afficher »

Ces vues personnalisées offrent des moyens intelligents d'engager les clients en affichant des types de contenu distincts, notamment des notifications interactives, des notifications alimentées par des données utilisateur et même des messages push qui peuvent capturer des informations telles que des numéros de téléphone et des e-mails. L'une de nos fonctionnalités bien connues chez Braze, [Push Stories]({{site.baseurl}}/user_guide/message_building_by_channel/push/advanced_push_options/push_stories/), est un excellent exemple de ce à quoi peut ressembler une extension d'application de contenu par notification push !

### Conditions

![]({% image_buster /assets/img/push_implementation_guide/push15.png %}){: style="float:right;max-width:50%;margin-left:10px; border:0;margin-top:10px"}
- [Les notifications push]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift) intégrées avec succès dans votre app.
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

![Options de bouton de notification dans les paramètres de l’éditeur de messages push.]({% image_buster /assets/img/push_implementation_guide/push16.png %}){: style="max-width:75%;border:0;margin-top:10px"}
![]({% image_buster /assets/img/push_implementation_guide/push17.png %}){: style="max-width:75%;border:0;margin-top:10px"}

## Notifications push personnalisées

![Deux iPhone affichés côte à côte. Le premier iPhone affiche la vue non étendue du message push. Le deuxième iPhone affiche la version élargie du message push affichant une « progression » de l’état d’avancement d’un cours, le nom de la prochaine session et la date d’échéance de la prochaine session.]({% image_buster /assets/img/push_implementation_guide/push6.png %}){: style="float:right;max-width:40%;margin-left:15px;border:0"}

Les notifications push peuvent afficher des informations spécifiques à l’utilisateur dans une extension de contenu. Cela vous permet de créer du contenu push axé sur l'utilisateur, comme l'ajout de l'option de partage de votre progression sur différentes plateformes, l'affichage des réalisations déverrouillées ou l'affichage des listes de contrôle d'onboarding. Cet exemple montre une notification push affichée à un utilisateur après qu'il a terminé une tâche spécifique dans le cours d'apprentissage de Braze. En développant la notification, l'utilisateur peut voir sa progression dans son parcours d'apprentissage. Les informations fournies ici sont spécifiques à l'utilisateur et peuvent être déclenchées à la fin d'une session ou lors d'une action spécifique de l'utilisateur en utilisant un déclencheur de l'API. 

### Configuration du tableau de bord

Pour créer une notification push personnalisée, vous devez définir une vue personnalisée dans votre tableau de bord. 

1. Dans la page **Campagnes**, cliquez sur **Créer une campagne** pour lancer une nouvelle campagne de notification push.
2. Dans l'onglet **Composer**, basculez sur les **boutons de notification.** 
3. Saisissez une catégorie iOS personnalisée dans le champ **Catégorie de notification iOS.**  
4. Dans l'onglet **Paramètres**, créez des paires clé-valeur à l'aide de Liquid standard. Définissez les attributs utilisateur appropriés que vous souhaitez voir apparaître dans le message. Ces vues peuvent être personnalisées sur la base des attributs utilisateur spécifiques d’un profil utilisateur donné.
5. Dans la `.plist` de votre cible d'extension de contenu de notification, définissez l'attribut `UNNotificationExtensionCategory` sur votre catégorie iOS personnalisée. La valeur indiquée ici doit correspondre à celle définie dans le tableau de bord de Braze sous **Catégorie de notification iOS.** 

![Quatre ensembles de paires clé-valeur, où "next_session_name" et "next_session_complete_date" sont définis comme une propriété de déclencheur API à l'aide de Liquid, et "completed_session count" et "total_session_count" sont définis comme un attribut personnalisé de l'utilisateur à l'aide de Liquid.]({% image_buster /assets/img/push_implementation_guide/push5.png %}){: style="max-width:60%;"}

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
{% tab Objective-C %}
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

## Notification push de recueil d’informations

Les notifications push peuvent capturer les informations de l'utilisateur à l'intérieur d'une extension d'app de contenu, repoussant ainsi les limites de ce qu'il est possible de faire avec un push. Demander la contribution des utilisateurs par le biais de notifications push vous permet non seulement de demander des informations de base comme le nom ou l'e-mail, mais aussi d'inciter les utilisateurs à soumettre leurs commentaires ou à compléter un profil utilisateur inachevé. 

{% alert tip %}
Pour plus d'informations, voir [Consignation des données de notification push]({{site.baseurl}}/developer_guide/analytics/logging_channel_data/push_notifications/).
{% endalert %}

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

Comme le montre l'exemple, vous pouvez également inclure une image dans votre notification push. Pour ce faire, vous devez intégrer les [notifications riches]({{site.baseurl}}/developer_guide/push_notifications/rich/?sdktab=swift), définir le style de notification de votre campagne sur Notification riche et inclure une image push riche.

![Une notification push avec trois ensembles de paires clé-valeur. 1. "Braze_id" réglé comme un appel liquide pour récupérer l'ID de Braze. 2. "cert_title" défini comme "Braze Marketer Certification". 3. "Cert_description" défini comme "Entraîneur certifié pour le marché de la Braze...".]({% image_buster /assets/img/push_implementation_guide/push9.png %})

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
{% tab Objective-C %}
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

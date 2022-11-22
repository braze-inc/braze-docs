---
nav_title: Paires clé-valeur
article_title: Paires clé-valeur
page_order: 4
description: "Braze vous permet d’envoyer des charges utiles de données supplémentaires aux périphériques utilisateur via des paires clé-valeur. Cette fonctionnalité est disponible sur les canaux de notification push, in-app et Carte de contenu."
channel:
  - Notification push
  - messages in-app
  - cartes de contenu

---

# Paires clé-valeur

Braze vous permet d’envoyer des charges utiles de données supplémentaires aux périphériques utilisateur via des paires clé-valeur. Cette fonctionnalité est disponible sur les canaux de notification push, in-app et Carte de contenu. Les charges utiles de données supplémentaires peuvent vous aider à mettre à jour les mesures internes et le contenu des applications et de personnaliser les propriétés des notifications push, telles que la priorisation des alertes, la localisation et les sons.

## Notifications push

### iOS

Le service de notification push d’Apple (APN) prend en charge les préférences d’alerte et l’envoi de données personnalisées à l’aide de paires clé-valeur. Les APN utilisent la bibliothèque réservée ```aps``` d’Apple qui inclut des clés prédéterminées et des valeurs qui régissent les propriétés d’alerte.

##### Bibliothèque APS

| Clé  | Type de valeur  | Description de la valeur |
|-------------------|-----------------------------|----------------------------------|
| alerte             | objet chaîne de caractères ou dictionnaire | Pour les entrées de chaîne de caractères, affiche une alerte avec la chaîne de caractères comme message avec les boutons Fermer et Afficher ; pour les entrées non string, affiche une alerte ou une bannière en fonction des propriétés enfant de l’entrée |
| Badge             | chiffre                      | Régit le numéro affiché en tant que badge sur l’icône de l’application                                                                                                                              |
| son             | chaîne de caractères                      | Le nom du fichier sonore qui est utilisé comme alerte ; doit être dans le faisceau de l’application ou ```Library/Sounds``` le dossier                                                                                    |
| contenu disponible | chiffre                      | Entrer les valeurs d’un signal à l’application, la disponibilité de nouvelles informations lors du lancement ou de la reprise de session |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}


##### Bibliothèque des propriétés d’alerte

| Clé            | Type de valeur               | Description de la valeur                                                                                                                             |
|----------------|--------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| Un titre         | chaîne de caractères                   | Une courte chaîne de caractères qu’Apple Watch affiche brièvement dans le cadre d’une notification                                                                    |
| borps         | chaîne de caractères                   | Le contenu de la notification push                                                                                                                  |
| title-loc-key  | chaîne de caractères ou nulle           | Une clé qui définit la chaîne de caractères de titre pour la localisation actuelle du ```Localizable.strings``` fichier                                          |
| title-loc-args | tableau de chaînes de caractères ou de nul | Valeurs de chaîne de caractères pouvant s’afficher à la place des spécificateurs de format de localisation dans title-loc-key                                           |
| action-loc-key | tableau de chaînes de caractères ou de nul  | Si cette option est présente, la chaîne de caractères spécifiée définit la localisation des boutons Fermer et Afficher                                                         |
| loc-key        | chaîne de caractères ou nulle           | Une clé qui définit le message de notification pour la localisation actuelle à partir du ```Localizable.strings``` fichier                                  |
| loc-args       | Tableau de chaînes de caractères         | Les valeurs de chaîne de caractères pouvant s’afficher à la place des spécificateurs de format de localisation dans in-loc-key                                                       |
| launch-image   | Chaînes de caractères                  | Le nom d’un fichier image dans le faisceau d’applications que vous souhaitez utiliser comme image de lancement lorsque les utilisateurs cliquent sur le bouton d’action ou déplacent la diapo d’action |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

Le compositeur de messages de Braze gère automatiquement la création des clés suivantes : **alerte** et **ses propriétés**, **contenu disponible**, **son**, et **catégorie**. 

Ces valeurs peuvent être saisies dans l’onglet **Paramètres** lorsque vous créez une notification push. Sélectionner **Options d’alerte** et sélectionnez une clé de dictionnaire d’alerte pour que la clé soit automatiquement renseignée dans une nouvelle entrée de valeur clé.

![][16]
{% raw %}
Lorsque Braze envoie une notification push aux APN, la charge utile sera formaté en tant que JSON.

**Charge utile simple**

```
{
    "aps" : { "alert" : "Message received from Spencer" },
}
```

**Charge utile complexe**

```
{
    "aps" : {
        "alert" : {
            "body" : "Hi, welcome to our app!",
            "loc-key" : "France",
            "loc-args" : ["Bonjour", "bienvenue"],
            "action-loc-key" : "Button_Type_1",
            "launch-image" : "Paris"
      },
        "content-available" : 1
    },
}
```

{% endraw %}

##### Accéder aux paires clé-valeur personnalisées

En plus ```aps``` des valeurs de la charge utile de la bibliothèque, vous pouvez envoyer des paires clé-valeur personnalisées à l’appareil d’un utilisateur. Dans le rédacteur de message, sélectionnez l’onglet **Paramètres**, cliquez sur **Ajouter une nouvelle paire**, et spécifiez vos paires clé-valeur. Les valeurs de ces paires sont limitées aux types de primitives : dictionnaire (objet), baie, chaîne de caractère, numéro et booléen.

![][17]

Les scénarios d’utilisation pour les paires clé-valeur personnalisées comprennent, sans s’y limiter, les mesures internes et la définition du contexte de l’interface utilisateur. Braze vous permet d’envoyer des paires clé-valeur supplémentaires ainsi qu’une notification push à utiliser, comme vous le souhaitez via votre application au sein des [clés supplémentaires][1]. Si vous préférez utiliser une autre clé, assurez-vous que votre application peut gérer cette clé personnalisée.

{% alert warning %}
Vous devez éviter de gérer une clé ou un dictionnaire de niveau supérieur appelé ab dans votre application.
{% endalert %}

Apple conseille aux clients d’éviter les informations client ou les données sensibles en tant que données de charge utile personnalisées. En outre, Apple recommande que toute action associée à un message d’alerte ne supprime pas les données sur un périphérique.

{% alert warning %}
Si vous utilisez l’API du fournisseur HTTP/2, toute charge utile individuele que vous envoyez aux APN ne peut pas dépasser une taille de 4 096 octets. L’interface binaire héritée, qui sera bientôt dépréciée, prend en charge une taille de charge utile de 2 048 octets seulement.
{% endalert %}

### Android

Braze vous permet d’envoyer des charges utiles de données supplémentaires dans des notifications push à l’aide de paires clé-valeur

##### Charges utiles de données

Comme pour la notification push iOS, vous pouvez envoyer des paires clé-valeur personnalisées sur le périphérique d’un utilisateur. Dans le rédacteur de message, sélectionnez l’onglet **Paramètres**, cliquez sur **Ajouter une nouvelle paire**, et spécifiez vos paires clé-valeur.

Certains scénarios d’utilisation pour les paires clé-valeur personnalisées comprennent les mesures internes et le réglage du contexte de l’interface utilisateur, mais ils peuvent être utilisés pour tous les objectifs.

{% alert important %}
Le back-end de votre application doit être en mesure de traiter les paires clé-valeur personnalisées pour que les charges utiles de données fonctionnent correctement.
{% endalert %}

##### Options de messagerie FCM

Les notifications push d’Android peuvent être personnalisées avec des options de message FCM. Cela inclut [priorité de notification][8], [son][10], retard, durée de vie et collapsibilité. Ces valeurs peuvent être saisies dans l’onglet **Paramètres** lorsque vous créez une notification push. Consulter [Paramètres de notification push avancés][7] pour des instructions supplémentaires sur la manière de définir ces options dans le rédacteur de messages Braze.

![][18]

### Notifications push silencieuses

Une notification push silencieuse est une notification push qui ne contient aucun message d’alerte ou son, utilisée pour mettre à jour l’interface ou le contenu de votre application en arrière-plan. Ces notifications utilisent des paires clé-valeur pour déclencher ces actions d’application en arrière plan. Les notifications push silencieuses alimentent également la [désinstallation du suivi][4] de Braze.

Les marketeurs doivent tester que les notifications push silencieuses déclenchent le comportement attendu avant de les envoyer aux applications des utilisateurs. Une fois que vous avez composé votre notification push silencieuse sur [iOS][2] ou [Android][13], assurez-vous que vous n’avez qu’à cibler un utilisateur test en filtrant l’ [ID utilisateur externe][14] ou [l’adresse e-mail][15].

Lors du lancement de la campagne, vous devez vérifier que vous n’avez reçu aucune notification push visible sur votre appareil de test.

{% alert note %}
Le système d’exploitation iOS peut bloquer [les notifications]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/silent_push_notifications/#ios-silent-notifications-limitations) pour certaines fonctions (désinstallation, tracking, geofences et Push Stories). Notez que si vous rencontrez des difficultés avec ces fonctions, le blocage des notifications silencieuse d’iOS peut être la cause.
{% endalert %}

### Web

Les paires clé-valeur peuvent également être ajoutées aux notifications push Web. Dans le rédacteur de message, sélectionnez l’onglet **Paramètres**, cliquez sur **Ajouter une nouvelle paire**, et spécifiez vos paires clé-valeur.

![][20]

## Messages in-app

Pour ajouter une paire clé-valeur à un message In-App sélectionnez l'onglet **Paramètres** dans l'éditeur de message, cliquez sur **Ajouter une nouvelle paire** et spécifiez vos paires clé-valeur.

![][21]

## E-mails

Pour les clients Braze qui utilisent SendGrid, les paires clé-valeur sont envoyées comme [arguments uniques][11]. SendGrid vous permet de joindre un nombre illimité de paires clé-valeur jusqu’à 10 000 octets de données. Ces paires clé-valeur peuvent s’afficher dans des publications du [Webhook][12] de SendGrid. 

{% alert note %}
Notez que les e-mails renvoyés ne fournissent pas de paires clé-valeur à SendGrid.
{% endalert %}

![Onglet Envoi d’Info du rédacteur de courriers électronique de Braze.][22]

## Fil d’actualité

Les paires clé-valeur peuvent être ajoutées à une carte de fil d'actualité dans le rédacteur de messages Braze sous la liste déroulante des catégories.

![La section des paires clé-valeur lors de la composition d’une carte de fil d’actualités dans Braze.][23]

## Cartes de contenu

Pour ajouter une paire clé-valeur à une carte de contenu, allez à l’onglet **Paramètres** dans le rédacteur de messages Braze et cliquez sur **Ajouter une nouvelle paire**.

![Ajouter une paire clé-valeur à la carte de contenu][24]{: style="max-width:70%;"}


[1]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/customization/advanced_settings/#extracting-data-from-push-key-value-pairs
[2]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/silent_push_notifications/
[4]: {{site.baseurl}}/user_guide/data_and_analytics/tracking/uninstall_tracking/
[7]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/advanced_settings/
[8]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/advanced_settings/#notification-priority
[9]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/advanced_settings/#delivery-options
[10]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/advanced_settings/#sounds
[11]: https://sendgrid.com/docs/API_Reference/SMTP_API/unique_arguments.html
[12]: https://sendgrid.com/docs/for-developers/tracking-events/event/
[13]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/silent_push_notifications/
[14]: {{site.baseurl}}/developer_guide/rest_api/messaging/#external-user-id
[15]: {{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/
[16]: {% image_buster /assets/img_archive/keyvalue_automatickeys.png %}
[17]: {% image_buster /assets/img_archive/keyvalue_enterpairs.png %}
[18]: {% image_buster /assets/img_archive/keyvalue_androidkeys.png %}
[19]: {% image_buster /assets/img_archive/keyvalue_android.png %}
[20]: {% image_buster /assets/img_archive/keyvalue_web.png %}
[21]: {% image_buster /assets/img_archive/keyvalue_iam.png %}
[22]: {% image_buster /assets/img_archive/keyvalue_email.png %}
[23]: {% image_buster /assets/img_archive/keyvalue_newsfeed.png %}
[24]: {% image_buster /assets/img_archive/kvp_content_cards.png %}

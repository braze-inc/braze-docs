---
nav_title: Paires clé-valeur
article_title: Paires clé-valeur
page_order: 3
description: "Braze vous permet d'envoyer des charges payantes supplémentaires aux appareils utilisateurs via des paires clés-valeurs. Cette fonctionnalité est disponible sur les canaux de messagerie push, dans l'application et dans les fils d'actualité."
channel:
  - Pousser
  - messages intégrés à l'application
  - fil d'actualité
---

# Paires clé-valeur

Braze vous permet d'envoyer des charges payantes supplémentaires aux appareils utilisateurs via des paires clés-valeurs. Cette fonctionnalité est disponible sur les canaux de messagerie push, dans l'application et dans les fils d'actualité. Des blocs de données supplémentaires peuvent vous aider à mettre à jour les paramètres internes et le contenu de l'application, ainsi que personnaliser les propriétés de notification push, comme la priorisation des alertes, la localisation et les sons.

## Notifications push

### iOS

Le service de notification Push d'Apple (APN) prend en charge le réglage des préférences d'alerte et l'envoi de données personnalisées à l'aide de paires clé-valeurs. Les APN utilisent la bibliothèque aps `aps` réservée aux Apples, qui inclut des clés prédéterminées et des valeurs qui régissent les propriétés d'alerte.

##### Bibliothèque APS

| Clés               | Type de valeur                             | Description de la valeur                                                                                                                                                                                                            |
| ------------------ | ------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Alerte             | chaîne de caractères ou objet dictionnaire | Pour les entrées de chaîne, affiche une alerte avec la chaîne comme le message avec les boutons Fermer et Afficher; pour les entrées non-chaînes, affiche une alerte ou une bannière en fonction des propriétés enfants de l'entrée |
| insigne            | N°                                         | Règle le nombre de badges affichés sur l'icône de l'application                                                                                                                                                                     |
| son                | chaîne de caractères                       | Le nom du fichier son à jouer en tant qu'alerte; doit être dans le bundle de l'application ou dans le dossier `Librairie/Sons`                                                                                                      |
| contenu disponible | N°                                         | Valeurs d'entrée de 1 signal pour l'application la disponibilité de nouvelles informations lors du lancement ou de la reprise de la session                                                                                         |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}


##### Librairie de propriétés d'alerte

| Clés                    | Type de valeur             | Description de la valeur                                                                                                                                                                               |
| ----------------------- | -------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Titre:                  | chaîne de caractères       | Une courte chaîne que l'Apple Watch affiche brièvement dans le cadre d'une notification                                                                                                                |
| Corps                   | chaîne de caractères       | Contenu de la notification push                                                                                                                                                                        |
| title-clé-loc-de-verrou | chaîne ou null             | Une clé qui définit la chaîne de titre pour la localisation actuelle depuis le fichier `Localizable.strings`                                                                                           |
| title-loc-args          | tableau de chaînes ou NULL | Les valeurs de chaîne qui peuvent apparaître à la place des spécificateurs de format de localisation de titre dans la clé de localisation de titre                                                     |
| clé-loc-action-clé      | tableau de chaîne ou NULL  | Si elle est présente, la chaîne spécifiée définit la localisation pour les boutons Fermer et Voir                                                                                                      |
| clé de verrouillage     | chaîne ou null             | Une clé qui définit le message de notification pour la localisation actuelle du fichier `Localizable.strings`                                                                                          |
| loc-args                | tableau de chaînes         | Les valeurs de chaîne qui peuvent apparaître à la place des spécificateurs de format de localisation dans la clé de localisation                                                                       |
| image de lancement      | chaînes de caractères      | Le nom d'un fichier image dans le lot d'application que vous souhaitez utiliser comme image de lancement lorsque les utilisateurs appuient sur le bouton d'action ou déplacent la diapositive d'action |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

Le compositeur de message de Braze gère automatiquement la création des clés suivantes : **alerte** et **ses propriétés**, **contenu disponible**, **son**, et **catégorie**. Ces valeurs peuvent être entrées directement dans le tableau de bord comme indiqué ci-dessous.

!\[Clés automatiques iOS\]\[16\]
{% raw %}
Lorsque Braze envoie une notification push aux APN, la charge utile sera formatée en JSON.

**Charge simple**

```
{
    "aps" : { "alert" : "Message reçu de Spencer" },
}
```

**Charge complexe**

```
{
    "aps" : {
        "alert" : {
            "body" : "Bonjour, bienvenue dans notre application ! ,
            "loc-key" : "France",
            "loc-args" : ["Bonjour", "bienvenue"],
            "action-loc-key" : "Button_Type_1",
            "launch-image" : "Paris"
      },
        "contenu-disponible" : 1
    },
}
```

{% endraw %}

##### Paires clé-valeur personnalisées

En plus des valeurs de charge utile de la bibliothèque `aps` , vous pouvez envoyer des paires clé-valeur personnalisées à l'appareil d'un utilisateur. Dans le message composer, cliquez sur l'icône d'engrenage et indiquez vos paires clé-valeur ci-dessous. Les valeurs de ces paires sont limitées aux types primitifs : dictionnaire (objet), tableau, chaîne, nombre et booléen.

!\[key-valueInput\]\[17\]

Les cas d'utilisation pour les paires clé-valeur personnalisées incluent mais ne se limitent pas à la conservation et au réglage du contexte de l'interface utilisateur. Braze vous permet d'envoyer des paires clé-valeur supplémentaires avec une notification push pour être utilisé cependant vous aussi, s'il vous plaît via votre application dans la [touche extras][1]. Si vous préférez utiliser une autre clé, assurez-vous que votre application peut gérer cette clé personnalisée.

{% alert warning %}
Vous devriez éviter de manipuler une clé de niveau supérieur ou un dictionnaire appelé ab dans votre application.
{% endalert %}

Apple conseille aux clients d'éviter d'inclure des informations clients ou des données sensibles comme données de charge utile personnalisées. De plus, Apple recommande que toute action associée à un message d'alerte ne supprime pas les données d'un périphérique.

{% alert warning %}
Si vous utilisez l'API du fournisseur HTTP/2, toute charge utile que vous envoyez aux APN ne peut excéder une taille de 4096 octets. L'interface binaire héritée, qui sera bientôt dépréciée, ne prend en charge que la taille de la charge utile de 2048 octets.
{% endalert %}

### Android

Braze vous permet d'envoyer des blocs de données supplémentaires dans les notifications push en utilisant des paires clé-valeur.

##### Charge utile des données

Des paires de valeurs clés personnalisées peuvent être saisies en cliquant sur l'icône d'engrenage et en spécifiant vos paires clés-valeur ci-dessous.

!\[Key-Value Input\]\[19\]

Les cas d'utilisation pour les paires de valeurs clés personnalisées incluent mais ne se limitent pas à la conservation et au réglage du contexte de l'interface utilisateur ; elles peuvent être utilisées à n'importe quelle fin que vous choisissez.

{% alert important %}
Notez que le backend de votre application doit être en mesure de traiter des paires clé-valeur personnalisées pour que la charge utile de données fonctionne correctement.
{% endalert %}

##### Options de messagerie FCM

Les notifications push d'Android peuvent être davantage personnalisées avec les options de messages FCM. Celles-ci incluent [la priorité de notification][8], [le son][10], [le délai, la durée de vie et la possibilité de plier][9]. Ces valeurs peuvent être entrées directement dans le tableau de bord comme indiqué ci-dessous. Reportez-vous à la [Documentation de Braze][7] pour plus d'instructions sur la façon de définir ces options dans le compositeur de message de Braze.

!\[Clés automatiques Android\]\[18\]

### Notifications push silencieuses

Une notification push silencieuse est une notification push qui ne contient aucun message d'alerte ou de son, utilisée pour mettre à jour l'interface ou le contenu de votre application en arrière-plan. Ces notifications utilisent les paires clé-valeur pour déclencher ces actions en arrière-plan. Les notifications push silencieuses alimentent également le [suivi de désinstallation de Braze][4].

Les marketeurs devraient tester que les notifications push silencieuses provoquent un comportement attendu avant de les envoyer aux utilisateurs de leur application. Une fois que vous composez votre [notification push iOS][2] ou [Android][13] silencieuse, assurez-vous de ne cibler qu'un utilisateur de test qu'en filtrant sur [ID utilisateur externe][14] ou [adresse e-mail][15].

Lors du lancement de la campagne, vous devriez vérifier que vous n'avez pas reçu de notification push visible sur votre appareil de test.

{% alert note %}
Le système d'exploitation iOS peut [les notifications de portail]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/silent_push_notifications/#ios-silent-notifications-limitations) pour certaines fonctionnalités (Désinstallation du Tracking, Géofences et Histoires poussées). Veuillez noter que si vous rencontrez des difficultés avec ces fonctionnalités, la porte des notifications silencieuses d'iOS pourrait en être la cause.
{% endalert %}

### Web

Des paires de valeurs clés peuvent également être ajoutées aux notifications push web. Sélectionnez l'icône d'engrenage dans le compositeur de message Braze pour le faire.

!\[key-valueInput\]\[20\]

## Messages In-App

Pour ajouter une paire clé-valeur à un message dans l'application, sélectionnez l'icône d'engrenage dans le compositeur de message Braze.

!\[key-valueInput\]\[21\]

## E-mails

Pour les clients Braze qui utilisent SendGrid, les paires clé-valeur seront envoyées comme [arguments uniques][11]. SendGrid vous permet d'attacher un nombre illimité de paires clé-valeur pouvant atteindre 10 000 octets de données. Ces paires de valeurs clés peuvent être vues dans les messages du SendGrid [Webhook événement][12].

{% alert note %}
Notez que les courriels rebondis ne délivreront pas de paires clé-valeur à SendGrid.
{% endalert %}

!\[key-valueInput\]\[22\]

## Flux d'actualité

Des paires de valeurs clés peuvent être ajoutées à une carte de flux de nouvelles dans le message de Braze sous le menu déroulant des catégories.

!\[key-valueInput\]\[23\]

## Cartes de contenu

Pour ajouter une paire clé-valeur à une carte de contenu, allez dans l'onglet **Paramètres** du compositeur de message Braze et cliquez sur **Ajouter une nouvelle paire**.

!\[Ajouter la paire key-value à la fiche de contenu\]\[24\]{: style="max-width:70%;"}
[16]: {% image_buster /assets/img_archive/keyvalue_automatickeys.png %} [17]: {% image_buster /assets/img_archive/keyvalue_enterpairs.png %} [18]: {% image_buster /assets/img_archive/keyvalue_androidkeys. ng %} [19]: {% image_buster /assets/img_archive/keyvalue_android.png %} [20]: {% image_buster /assets/img_archive/keyvalue_web. ng %} [21]: {% image_buster /assets/img_archive/keyvalue_iam.png %} [22]: {% image_buster /assets/img_archive/keyvalue_email. ng %} [23]: {% image_buster /assets/img_archive/keyvalue_newsfeed.png %} [24]: {% image_buster /assets/img_archive/kvp_content_cards.png %}


[1]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/customization/kvp/
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

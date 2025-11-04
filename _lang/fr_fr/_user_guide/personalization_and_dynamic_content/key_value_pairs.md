---
nav_title: Paires clé-valeur
article_title: Paires clé-valeur
page_order: 4
description: "Cet article de référence traite des paires clé-valeur et de leur utilisation pour envoyer des données supplémentaires aux appareils des utilisateurs."
channel:
  - push
  - in-app messages
  - content cards

---

# Paires clé-valeur

> Cette page explique comment utiliser des paires clé-valeur pour envoyer des données supplémentaires aux appareils des utilisateurs. Cette fonctionnalité est disponible sur les canaux d'envoi de messages push, in-app, e-mail et carte de contenu.

Utilisez des paires clé-valeur pour ajouter des métadonnées structurées aux messages. Ces données supplémentaires peuvent enrichir les messages avec des informations contextuelles supplémentaires qui peuvent influencer le rendu ou le traitement d'un message.

Les paires clé-valeur étant des métadonnées, ces données ne sont pas nécessairement visibles par le destinataire, mais peuvent être utilisées par vos systèmes ou processus connectés pour personnaliser l'envoi des messages. 

Chaque paire est composée de

- **Clé :** L'identifiant (exemple : `utm_source`)
- **Valeur :** Les données associées (exemple : `newsletter`)

## Cas d'utilisation

Voici quelques exemples de cas d'utilisation pour l'ajout de métadonnées avec des paires clé-valeur :

1. **Paramètres de suivi :** Attacher des paramètres UTM à des fins d'analyse/analytique (si utilisé comme adjectif)
   - Clé : `utm_campaign`
   - Valeur : `spring_sale`
2. **Tags personnalisés :** Ajout de tags pour le routage ou la catégorisation interne
   - Clé : `priority`
   - Valeur : `high`
3. **Déclencheurs de comportement :** Métadonnées utilisées pour déclencher ou personnaliser des comportements in-app.
   - Clé : `deep_link`
   - Valeur : `app://promo-page`

## Notifications push

Les paires clé-valeur peuvent être ajoutées aux notifications push Android, iOS et web. Vous pourriez utiliser des paires clé-valeur pour mettre à jour les indicateurs internes et le contenu de l'app ou personnaliser les propriétés des notifications push, telles que la priorisation des alertes, la localisation et les sons.

Dans le compositeur de messages, sélectionnez l'onglet **Paramètres**, puis **Ajouter une nouvelle paire** et spécifiez vos paires clé-valeur.

### iOS

Le service Apple Push Notification (APN) permet de définir des préférences en matière d'alertes et d'envoyer des données personnalisées à l'aide de paires clé-valeur. APN utilise la bibliothèque ```aps``` réservée à Apple, qui comprend des clés et des valeurs prédéterminées régissant les propriétés des alertes.

##### Bibliothèque de l'APS

| Clé  | Type de valeur  | Valeur Description |
|-------------------|-----------------------------|----------------------------------|
| alerte             | chaîne de caractères ou objet dictionnaire | Pour les entrées de type chaîne, affiche une alerte avec la chaîne de caractères comme message et les boutons Fermer et Afficher ; pour les entrées de type autre que chaîne, affiche une alerte ou une bannière en fonction des propriétés enfant de l'entrée. |
| badge             | nombre                      | Régit le numéro qui s'affiche en tant que badge sur l'icône de l'app.                                                                                                                              |
| son             | chaîne de caractères                      | Le nom du fichier son à jouer en tant qu'alerte ; il doit se trouver dans le dossier bundle ou ```Library/Sounds``` de l'application.                                                                                    |
| contenu disponible | nombre                      | Une valeur de 1 signale à l'application la disponibilité de nouvelles informations lors du lancement ou de la reprise d'une session. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


##### Bibliothèque des propriétés d'alerte

| Clé            | Type de valeur               | Valeur Description                                                                                                                             |
|----------------|--------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| titre         | chaîne de caractères                   | Une chaîne de caractères courte que l'Apple Watch affiche brièvement dans le cadre d'une notification.                                                                    |
| corps         | chaîne de caractères                   | Le contenu de la notification push                                                                                                                  |
| title-loc-key  | chaîne de caractères ou null           | Une clé qui définit la chaîne de caractères du titre de la localisation actuelle à partir du fichier ```Localizable.strings```.                                          |
| title-loc-args | tableau de chaînes de caractères ou null | Valeurs de chaînes de caractères pouvant remplacer les spécificateurs du format de localisation du titre dans title-loc-key                                           |
| action-loc-key | tableau de chaînes de caractères ou null  | Si elle est présente, la chaîne de caractères spécifiée définit la localisation des boutons Fermer et Afficher.                                                         |
| loc-key        | chaîne de caractères ou null           | Une clé qui définit le message de notification pour la localisation actuelle à partir du fichier ```Localizable.strings```.                                  |
| loc-args       | tableau de chaînes de caractères         | Valeurs des chaînes de caractères qui peuvent remplacer les spécificateurs du format de localisation dans loc-key                                                       |
| image de lancement   | chaînes de caractères                  | Le nom d'un fichier image dans le bundle d'applications que vous souhaitez utiliser comme image de lancement lorsque les utilisateurs appuient sur le bouton d'action ou déplacent la glissière d'action. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Le compositeur de messages de Braze gère automatiquement la création des clés suivantes : **alerte** et ses **propriétés**, **contenu disponible**, **son** et **catégorie**. 

Ces valeurs peuvent être saisies dans l'onglet **Paramètres** lorsque vous créez un message push. Sélectionnez **Options d'alerte** et choisissez une clé du dictionnaire d'alerte pour que la clé soit automatiquement remplie dans une nouvelle entrée clé-valeur.

\![]({% image_buster /assets/img_archive/keyvalue_automatickeys.png %})
{% raw %}
Lorsque Braze envoie une notification push aux APN, la charge utile sera formatée sous forme de JSON.

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

##### Paires clé-valeur personnalisées

Outre les valeurs de la charge utile de la bibliothèque ```aps```, vous pouvez envoyer des paires clé-valeur personnalisées à l'appareil d'un utilisateur. Les valeurs de ces paires sont limitées aux types primitifs : dictionnaire (objet), tableau d'objets, chaîne de caractères, nombre et booléen.

\![]({% image_buster /assets/img_archive/keyvalue_enterpairs.png %})

Les cas d'utilisation des paires clé-valeur personnalisées comprennent, sans s'y limiter, la conservation des indicateurs internes et la définition du contexte de l'interface utilisateur. Braze vous permet d'envoyer des paires clé-valeur supplémentaires accompagnées d'une notification push à utiliser via votre application au sein de la [clé extras]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/customization/advanced_settings/#extracting-data-from-push-key-value-pairs). Si vous préférez utiliser une autre clé, confirmez que votre application peut gérer cette clé personnalisée.

{% alert warning %}
Vous devez éviter de manipuler une clé de premier niveau ou un dictionnaire appelé ab dans votre application.
{% endalert %}

Apple conseille à ses clients d'éviter d'inclure des informations sur les clients ou toute donnée sensible dans les données utiles personnalisées. En outre, Apple recommande que toute action associée à un message d'alerte ne supprime pas les données d'un appareil.

{% alert warning %}
Si vous utilisez l'API du fournisseur HTTP/2, toute charge utile individuelle que vous envoyez aux APN ne peut pas dépasser une taille de 4096 octets. L'ancienne interface binaire, qui sera bientôt dépréciée, ne prend en charge qu'une taille de charge utile de 2048 octets.
{% endalert %}

###### Campagnes déclenchées par l'API

Braze vous permet d'envoyer des paires clé-valeur de chaînes de caractères personnalisées, appelées `extras`. Pour accéder à vos extras dans les campagnes déclenchées par l'API et les campagnes planifiées déclenchées par l'API, dans le tableau de bord, définissez une clé comme "example_key", et une valeur comme {% raw %}`"$json:{"foo": 1, "bar": 1}"`{% endraw %}. La console de développement affichera alors le message suivant `"extras": { "test": { "foo": 1, "bar": 1 }`

### Android

Braze vous permet d'envoyer des données supplémentaires dans les notifications push à l'aide de paires clé-valeur.

##### Données

De manière similaire à iOS push, vous pouvez envoyer des paires clé-valeur personnalisées à l'appareil d'un utilisateur.

Les paires clé-valeur personnalisées sont notamment utilisées pour la conservation des indicateurs internes et la définition du contexte de l'interface utilisateur, mais elles peuvent être utilisées à n'importe quelle fin.

{% alert important %}
Le backend de votre app doit pouvoir traiter les paires clé-valeur personnalisées pour que la charge utile de données fonctionne correctement.
{% endalert %}

###### Campagnes déclenchées par l'API

Braze vous permet d'envoyer des paires clé-valeur de chaînes de caractères personnalisées, appelées `extras`. Pour accéder à vos extras dans les campagnes déclenchées par l'API et les campagnes planifiées déclenchées par l'API, dans le tableau de bord, définissez une clé comme "example_key", et une valeur comme {% raw %}`"$json:{"foo": 1, "bar": 1}"`{% endraw %}. La console de développement affichera alors `"extras": { "test": { "foo": 1, "bar": 1 }`.

##### Options d'envoi de messages du FCM

Les notifications push Android peuvent être encore plus personnalisées grâce aux options d'envoi de messages du FCM. Il s'agit notamment de la [priorité de notification]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/customization/advanced_settings/#notification-priority), du [son]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/customization/advanced_settings/#sounds), du délai, de la durée de vie et de la possibilité de s'effondrer. Ces valeurs peuvent être spécifiées dans l'onglet **Paramètres** lors de la création d'un message push. Reportez-vous à la section [Paramètres avancés de notification push]({{site.baseurl}}/developer_guide/push_notifications/customization/?sdktab=android#android_settings) pour plus d'instructions sur la manière de définir ces options dans le compositeur de messages de Braze.

\![]({% image_buster /assets/img_archive/keyvalue_androidkeys.png %})

### Notifications push silencieuses

Une notification push silencieuse est une notification push ne contenant ni message d'alerte ni son, utilisée pour mettre à jour l'interface ou le contenu de votre app en arrière-plan. Ces notifications utilisent des paires clé-valeur pour déclencher les actions de l'application en arrière-plan. Les notifications push silencieuses permettent également de [suivre les désinstallations]({{site.baseurl}}/user_guide/analytics/tracking/uninstall_tracking/).

Les marketeurs doivent tester que les notifications push silencieuses déclenchent le comportement attendu avant de les envoyer aux utilisateurs de leur appli. Après avoir composé votre notification push silencieuse [iOS]({{site.baseurl}}/developer_guide/push_notifications/silent/?sdktab=swift) ou [Android]({{site.baseurl}}/developer_guide/push_notifications/silent/?sdktab=android), assurez-vous de ne cibler qu'un utilisateur test en filtrant sur l'[ID externe]({{site.baseurl}}/developer_guide/rest_api/messaging/#external-user-id) ou l'[adresse e-mail]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/).

Lors du lancement de la campagne, vous devez vérifier que vous n'avez pas reçu de notification push visible sur votre appareil de test.

{% alert note %}
Le système d'exploitation iOS peut [porter des notifications]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/silent_push_notifications/#ios-silent-notifications-limitations) pour certaines fonctionnalités (suivi des désinstallations, géorepérages et Push Stories). Notez que si vous rencontrez des difficultés avec ces fonctionnalités, la porte des notifications silencieuses d'iOS pourrait en être la cause.
{% endalert %}

## Messages in-app

Pour ajouter une paire clé-valeur à un message in-app, sélectionnez l'onglet **Paramètres** dans le compositeur de messages, sélectionnez **Ajouter une nouvelle paire** et spécifiez vos paires clé-valeur.

\![]({% image_buster /assets/img_archive/keyvalue_iam.png %})

#### Campagnes déclenchées par l'API

Braze vous permet d'envoyer des paires clé-valeur de chaînes de caractères personnalisées, appelées `extras`. Pour accéder à vos extras dans les campagnes déclenchées par l'API et les campagnes planifiées déclenchées par l'API, dans le tableau de bord, définissez une clé comme "example_key", et une valeur comme {% raw %}`"$json:{"foo": 1, "bar": 1}"`{% endraw %}. La console de développement affichera alors `"extras": { "test": { "foo": 1, "bar": 1 }`.

## E-mails

SparkPost et SendGrid prennent tous deux en charge les paires clé-valeur dans les e-mails. Si vous utilisez Sendgrid, les paires clé-valeur seront envoyées en tant qu'[arguments uniques](https://docs.sendgrid.com/for-developers/sending-email/unique-arguments). SendGrid vous permet de joindre un nombre illimité de paires clé-valeur jusqu'à 10 000 octets de données. Ces paires clé-valeur sont visibles dans les messages du [Webhook d'événement](https://sendgrid.com/docs/for-developers/tracking-events/event/) SendGrid.

{% alert note %}
Les e-mails ayant fait l'objet d'un rebond ne délivreront pas de paire clé-valeur à SparkPost ou SendGrid.
{% endalert %}

!onglet Infos d'envoi du compositeur de messages e-mail dans Braze.]({% image_buster /assets/img_archive/keyvalue_email.png %})

## Cartes de contenu

Pour ajouter une paire clé-valeur à une carte de contenu, accédez à l'onglet **Paramètres** du compositeur de messages de Braze et sélectionnez **Ajouter une nouvelle paire.**

\![Ajouter une paire clé-valeur à la carte de contenu]({% image_buster /assets/img_archive/kvp_content_cards.png %}){: style="max-width:70%;"}



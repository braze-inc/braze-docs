---
nav_title: Sendbird
article_title: Sendbird
description: "Cet article de référence présente le partenariat entre Braze et Sendbird, une solution de messagerie in-app de premier plan qui permet aux utilisateurs de recevoir des notifications in-app sur la plateforme Sendbird."
alias: /partners/sendbird/
page_type: partner
search_tag: Partner

---

# Sendbird

> [Sendbird](https://sendbird.com/) Notifications offre aux marketeurs et aux gestionnaires de produits un nouveau canal puissant pour communiquer avec leurs clients in-app avec des messages persistants et interactifs à sens unique. Ces messages peuvent être utilisés pour toute communication et sont le plus souvent utilisés à des fins promotionnelles et transactionnelles.

_Cette intégration est maintenue par Sendbird._

## À propos de l'intégration

L'intégration de Braze et de Sendbird permet aux utilisateurs de Braze de :
* Utilisez les fonctionnalités de segmentation et de déclencheur de Braze pour lancer des notifications personnalisées in-app.
* Créez des notifications in-app personnalisées sur la plateforme Sendbird Notifications, qui sont ensuite diffusées dans l'environnement de l'application, améliorant ainsi l'engagement de l'utilisateur.

En exploitant les capacités conjointes de Braze et Sendbird Notifications, les entreprises peuvent renforcer l'engagement client et obtenir des taux de conversion plus élevés grâce à des stratégies de notification in-app efficaces.

## Conditions préalables

| Condition | Description |
| ----------- | ----------- |
| Compte Sendbird | Un compte Sendbird est nécessaire pour profiter de ce partenariat. |
| Sendbird UIKit | Vous devez avoir installé l'UIKit Sendbird dans votre application [iOS](https://sendbird.com/docs/notifications/v1/uikit/ios/install-uikit) ou [Android](https://sendbird.com/docs/notifications/v1/uikit/android/install-uikit). |
| Clé API REST de Braze | Une clé API Braze REST avec des autorisations `users.track`. <br><br> Elle peut être créée dans le tableau de bord de Braze depuis **Paramètres** > **Clés d'API**. |
| Endpoint REST de Braze | [L'URL de votre endpoint REST.]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints) Votre endpoint dépendra de l'URL de Braze pour votre instance. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Cas d’utilisation

![]({% image_buster /assets/img/sendbird/use-cases.png %})

L'intégration des notifications de Braze et Sendbird offre un éventail de cas d'utilisation pour stimuler l'engagement client et offrir une expérience utilisateur exceptionnelle :

- **Marketing** : Améliorez les campagnes ciblées avec des promotions et des recommandations personnalisées adaptées aux préférences des utilisateurs, telles que des réductions exclusives basées sur l'historique de navigation ou les achats passés.
- **Transactionnel** : Améliorez la communication avec vos clients grâce à des mises à jour en temps réel sur les commandes, les livraisons, la facturation et les paiements, y compris des notifications concernant le statut de la commande, les détails de l'expédition et les délais de livraison estimés.

## Intégration

### Étape 1 : Créer un modèle de notification

Les [modèles Sendbird](https://sendbird.com/docs/notifications/v1/templates) vous permettent d'envoyer des notifications in-app personnalisées en créant et en utilisant plusieurs modèles pour chaque canal. Les modèles peuvent être créés et personnalisés sur le tableau de bord de Sendbird sans avoir à écrire de code.

![]({% image_buster /assets/img/sendbird/sendbird-dashboard-template.png %})

### Étape 2 : Configurez l'intégration Braze dans le tableau de bord de Sendbird.

Depuis le **tableau de bord de Sendbird**, sélectionnez votre application, naviguez vers **Notifications > Intégrations**, et cliquez sur **Ajouter** sous la section **Braze**. Ici, vous aurez besoin de la clé API REST de Braze et de l'endpoint REST de Braze.

Une fois que vous avez renseigné tous les champs, cliquez sur **Enregistrer** pour terminer l'intégration et accéder aux endpoints d'intégration et au jeton API.

### Étape 3 : Installer le générateur de notifications Sendbird

Ensuite, vous devez installer [Sendbird Notification Builder](https://chrome.google.com/webstore/detail/apbhgfffamdcdogeijjcnjbmghahoaji). Cette extension Google Chrome vous permet d'envoyer des notifications personnalisées via Sendbird sur le tableau de bord de Braze.

![]({% image_buster /assets/img/sendbird/sendbird-notification-builder.png %})

#### Ajoutez les informations d'identification Sendbird à l'extension

Une fois l'extension installée, cliquez sur l'icône Sendbird dans la barre d'outils de votre navigateur et sélectionnez **Paramètres.** Ici, fournissez votre ID d'application et votre jeton API qui sont disponibles dans  **Sendbird Notification Builder**.

### Étape 4 : Mappez l'ID de l'utilisateur de Sendbird à l'ID de l'utilisateur de Braze

Un ID utilisateur Sendbird doit être ajouté au profil utilisateur Braze en tant qu'[attribut personnalisé]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/) pour que l'intégration puisse être utilisée. Vous pouvez télécharger et mettre à jour les profils utilisateurs via des fichiers CSV à partir de la page [Importation d'utilisateurs.]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import/#csv) Vous pouvez également utiliser l'ID de l'utilisateur de Braze comme ID de l'utilisateur de Sendbird.

### Étape 5 : Configurez votre modèle de webhook

Dans Braze, à partir de **Modèles et médias**, allez dans **Modèles de webhook** et choisissez le **modèle de webhook Sendbird.** Notez que ce modèle ne sera disponible que si vous avez installé l'extension Sendbird Notification Builder.

{% raw %}
1. Donnez un nom au modèle et ajoutez des équipes et des étiquettes si nécessaire.
2. Copiez un endpoint en temps réel ou par lot depuis le tableau de bord de Sendbird dans l'**URL du webhook.**
3. Dans le champ **Destinataire**, cliquez sur l'icône <i class="fas fa-plus"></i> et insérez l'attribut utilisateur mappé à l'ID utilisateur Sendbird.
    - `{{ '{{' }}custom_attribute.${sendbird_id}}}` si vous utilisez un attribut personnalisé `sendbird_id` comme ID d'utilisateur Sendbird.
    - `{{ '{{' }}${user_id}}}` si vous utilisez l'ID d'utilisateur Braze comme ID d'utilisateur Sendbird.
4. Dans l'onglet **Paramètres**, remplacez `SENDBIRD_API_TOKEN` par le jeton de l'API de notifications provenant du tableau de bord de Sendbird.
5. Enregistrez le modèle.
{% endraw %}

## Utilisation de cette intégration

### Campagnes

1. Dans le tableau de bord de Braze, sur la page **Campagnes**, cliquez sur **Créer une campagne** > **Webhook**.
2. Sélectionnez le modèle de webhook que vous avez créé ci-dessus. Il est fortement recommandé d'utiliser l'endpoint Batch pour les campagnes.
3. Personnalisez le modèle en modifiant ses variables dans l'onglet **Composer.** 

### Canevas

1. À partir d'un canvas nouveau ou existant, ajoutez un composant **Message.**  
2. Ouvrez le composant et sélectionnez **Webhook** dans les **canaux de communication.**
3. Sélectionnez le modèle de webhook que vous avez créé ci-dessus. Il est fortement recommandé d'utiliser l'endpoint en temps réel pour les canvas.
4. Personnalisez le modèle en modifiant ses variables dans l'onglet **Composer.** 

## Personnalisation

### Suivre la distribution et l’état d’ouverture

Pour intégrer l'événement de distribution des notifications et de statut d'ouverture à l'indicateur de conversion d'une campagne, ajoutez un événement personnalisé sur le tableau de bord de Braze.

1. Depuis le tableau de bord de Braze, accédez à **Paramètres > Gérer les paramètres > Événements personnalisés**, puis cliquez sur **\+ Ajouter un événement personnalisé.**
2. Après avoir créé un événement personnalisé, cliquez sur **Gérer les propriétés**, ajoutez une propriété nommée "statut" et choisissez "Chaîne de caractères" comme type de propriété.
3. Lorsque vous composez une notification dans les campagnes ou les canevas, saisissez le nom de l'événement personnalisé dans le champ **Nom de l'événement.** 

Cet événement personnalisé sera déclenché deux fois pour chaque notification, lorsqu'un message est envoyé et lorsqu'un utilisateur ouvre le message.
- Lorsqu'un message est envoyé, un événement personnalisé est déclenché avec le statut `SENT`.
- Lorsqu'un message est lu, un événement personnalisé est déclenché avec le statut `READ`.



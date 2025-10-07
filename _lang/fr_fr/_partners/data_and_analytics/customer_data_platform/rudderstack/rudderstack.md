---
nav_title: Rudderstack
article_title: Rudderstack
description: "Cet article présente le partenariat entre Braze et RudderStack, une infrastructure de données client open-source offrant une intégration fluide de Braze pour vos applications Android, iOS et web. Avec RuddStack, vous pouvez envoyer vos données d'événements personnalisés in-app directement à Braze pour une analyse contextuelle."
page_type: partner
search_tag: Partner

---

# RudderStack

> [RudderStack](https://rudderstack.com/) est une infrastructure de données clients open-source permettant de collecter et d'acheminer les données d'événements personnalisés vers votre entrepôt de données préféré et des dizaines d'autres fournisseurs d'analyse/analytique, tels que Braze. Il est prêt pour l'entreprise et offre un cadre de transformation robuste pour traiter vos données d'événements à la volée.

L'intégration entre Braze et Rudderstack offre une intégration SDK native pour vos applications Android, iOS et web, ainsi qu'une intégration de serveur à serveur à partir de vos services backend.

## Conditions préalables

| Condition | Description |
| --- | --- |
| Compte Rudderstack | Un [compte Rudderstack](https://app.rudderstack.com/) est nécessaire pour bénéficier de ce partenariat. |
| Source configurée | Une [source](https://www.rudderstack.com/docs/dashboard-guides/sources/) est essentiellement l'origine de toute donnée envoyée à Rudderstack, comme les sites web, les applications mobiles ou les serveurs dorsaux. Vous devez configurer la source avant de configurer Braze comme destination dans Rudderstack. |
| Clé API REST de Braze | Une clé API REST de Braze avec les autorisations `users.track`, `users.identify`, `users.delete` et `users.alias.new`.<br><br>Celle-ci peut être créée dans le tableau de bord de Braze à partir de **Paramètres** > **Clés API**. |
| Clé de l'application Braze | Pour obtenir votre clé d'app dans le tableau de bord de Braze, allez dans **Réglages** > **Paramètres de l'app** > **Identification** et trouvez le nom de votre app. Enregistrez la chaîne de caractères de l'identifiant associé.
| Centre de données | Votre centre de données s'aligne sur votre [instance de]({{site.baseurl}}/api/basics/#endpoints) tableau de bord de Braze.  |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Intégration

### Étape 1 : Ajouter une source

Pour commencer à envoyer des données à Braze, vous devez d'abord vous assurer qu'une source est configurée dans votre application Rudderstack. Visitez le site de [Rudderstack](https://www.rudderstack.com/docs/destinations/streaming-destinations/braze/#getting-started) pour savoir comment configurer votre source de données.

### Étape 2 : Configurer la destination

Maintenant que votre source de données est configurée, dans le tableau de bord de Rudderstack, sélectionnez **ADD DESTINATION** sous **Destinations.** Dans la liste des destinations disponibles, sélectionnez **Braze** et cliquez sur **Suivant.**

Dans la destination Braze, spécifiez la clé de l'application, la clé de l'API REST de Braze, le cluster de données et l'option du SDK natif (mode appareil uniquement). Lorsque l'option du SDK natif est activée, le SDK natif de Braze sera utilisé pour envoyer des événements. 

![]({% image_buster /assets/img/RudderStack/braze_settings.png %}){: style="max-width:70%;margin-bottom:15px;border:none;"}

### Étape 3 : Choisissez le type d'intégration

Vous pouvez choisir d'intégrer les bibliothèques web et natives côté client de Rudderstack avec Braze en utilisant l'une des approches suivantes :

- [Mode côte à côte / appareil](#device-mode)**:** Rudderstack enverra les données d'événement à Braze directement depuis votre client (navigateur ou application mobile).
- [Mode serveur à serveur / cloud](#cloud-mode)**:** Le SDK de Braze envoie les données d'événement directement à Rudderstack où elles sont transformées avant d’être acheminées vers Braze.
- [Mode hybride](#hybrid-mode)**:** Utilisez le mode hybride pour envoyer des événements iOS et Android générés automatiquement et générés par l'utilisateur vers Braze à l'aide d'une seule connexion.

{% alert note %}
Découvrez les [modes de connexion](https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/) de Rudderstack et les avantages de chacun d'entre eux.
{% endalert %}

#### Intégration côte à côte (mode appareil) {#device-mode}

Avec ce mode, vous pouvez envoyer vos événements à Braze en utilisant le SDK de Braze mis en place sur votre site web ou votre application mobile.

Configurez les mappages vers le SDK de Rudderstack pour votre plateforme sur le dépôt GitHub de Braze, comme décrit dans les [méthodes prises en charge](#supported-methods):

- [Android](https://github.com/rudderlabs/rudder-integration-braze-android)
- [iOS](https://github.com/rudderlabs/rudder-integration-braze-ios/tree/master)
- [Swift](https://github.com/rudderlabs/rudder-integration-braze-swift)
- [Web](https://github.com/rudderlabs/rudder-sdk-js/tree/production/src/integrations/Braze)
- [React Native](https://github.com/rudderlabs/rudder-sdk-react-native/tree/develop/libs/rudder-integration-braze-react-native)
- [Flutter](https://github.com/rudderlabs/rudder-sdk-flutter/tree/develop/packages/integrations/rudder_integration_braze_flutter)

Pour terminer l'intégration du mode appareil, reportez-vous aux instructions détaillées de Rudderstack concernant l'[ajout de Braze à votre projet](https://rudderstack.com/docs/destinations/marketing/braze/#adding-device-mode-integration).

#### Intégration de serveur à serveur (mode cloud) {#cloud-mode}

Dans ce mode, le SDK envoie les données d'événement directement au serveur Rudderstack. Rudderstack transforme ensuite ces données et les achemine vers la destination souhaitée. Cette transformation est effectuée dans le backend de Rudderstack à l'aide du module de transformation de RudderStack.

Pour permettre l'intégration, vous devrez mapper les méthodes de Rudderstack à Braze, comme décrit dans les [méthodes prises en charge.](#supported-methods)

{% alert note %}
Les SDK côté serveur de Rudderstack (Java, Python, Node.js, Go, Ruby) ne prennent en charge que le mode cloud. En effet, leurs SDK côté serveur fonctionnent dans le backend de Rudderstack et ne peuvent charger aucun SDK spécifique à Braze.
{% endalert %}

{% alert important %}
L'intégration de serveur à serveur ne prend pas en charge les fonctionnalités de Braze UI, telles que les notifications push ou l'envoi de messages in-app. Ces fonctionnalités sont toutefois prises en charge par l'intégration du mode appareil.
{% endalert %}

#### Mode hybride {#hybrid-mode}

Utilisez le mode hybride pour envoyer tous les événements à Braze depuis vos sources iOS et Android. 

Lorsque vous choisissez le mode hybride pour envoyer des événements à Braze, Rudderstack :
1. Initialise le SDK de Braze.
2. Envoie tous les événements générés par l'utilisateur (identifier, suivre, page, écran et groupe) à Braze uniquement via le mode cloud et bloque leur envoi via le mode appareil.
3. Envoie les événements générés automatiquement (messages in-app, notifications push qui nécessitent le SDK de Braze) via le mode appareil.

Pour [envoyer des événements via le mode hybride](https://www.rudderstack.com/docs/destinations/streaming-destinations/braze/#send-events-in-hybrid-mode), utilisez l'option de mode hybride lors de la connexion de votre source à la destination Braze. Ensuite, ajoutez l'intégration de Braze à votre projet.

## Étape 4 : Configurer des paramètres supplémentaires

Une fois la configuration initiale terminée, configurez les paramètres suivants pour recevoir correctement vos données dans Braze :

- **Activer les groupes d'abonnement dans les appels de groupe**: Activez ce paramètre pour envoyer le statut du groupe d'abonnement dans vos événements de groupe. Pour plus d'informations, consultez la section [Groupe](https://www.rudderstack.com/docs/destinations/streaming-destinations/braze/#group).
- **Utiliser l'opération d'attributs personnalisés**: Activez ce paramètre si vous souhaitez utiliser la fonctionnalité d'[attributs personnalisés imbriqués]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/array_of_objects/) de Braze pour créer des segments et personnaliser vos messages à l'aide d'un objet d'attribut personnalisé. Pour plus d'informations, consultez la section [Envoyer des caractéristiques d'utilisateur en tant qu'attributs personnalisés imbriqués](https://www.rudderstack.com/docs/destinations/streaming-destinations/braze/#send-user-traits-as-nested-custom-attributes).
- **Suivre les événements pour les utilisateurs anonymes**: Activez ce paramètre pour suivre l'activité de l'utilisateur anonyme et envoyer ces informations à Braze.

### Paramètres du mode appareil

Les paramètres suivants ne s'appliquent que si vous envoyez des événements à Braze via le [mode appareil](https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#device-mode):

- **Filtrage des événements côté client**: Ce paramètre vous permet de spécifier quels événements doivent être bloqués ou autorisés à transiter vers Braze. Pour plus d'informations sur ce paramètre, consultez la section [Filtrage des événements côté client](https://www.rudderstack.com/docs/sources/event-streams/sdks/event-filtering/).
- **Déduplication des caractéristiques** : Activez ce paramètre pour dédupliquer les traits de l'utilisateur dans l'appel [`identify`](https://www.rudderstack.com/docs/destinations/streaming-destinations/braze/#identify).
- **Afficher les journaux de Braze**: Ce paramètre ne s'applique que lorsque vous utilisez le [SDK JavaScript](https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/) comme source. Activez-la pour afficher les journaux de Braze à vos utilisateurs.
- **Catégories de cookies OneTrust**: Ce paramètre vous permet d'associer les groupes de consentement aux cookies [OneTrust](https://www.rudderstack.com/docs/sources/event-streams/sdks/onetrust/javascript/) à Braze.

## Méthodes prises en charge

Braze prend en charge les méthodes Rudderstack identify, track, screen, page, group et alias.

{% tabs %}
{% tab Identifier %}

La méthode Rudderstack [`identify`](https://rudderstack.com/docs/destinations/marketing/braze/#identify) associe les utilisateurs à leurs actions. RuddStack enregistre un ID unique et des données facultatives associées à l'utilisateur, telles que le nom, l'e-mail, l'adresse IP, etc.

**Gestion du delta pour les appels d'identification**<br>
Si vous envoyez des événements à Braze via le mode appareil, vous pouvez réduire vos coûts en dédupliquant vos appels à `identify`. Pour ce faire, activez le paramètre de déduplication des caractéristiques dans le tableau de bord. Rudderstack n'envoie alors à Braze que les attributs (traits) changés ou modifiés.

**Suppression d'un utilisateur**<br>
Vous pouvez supprimer un utilisateur dans Braze à l'aide de la [règle Suppression avec Supprimer](https://www.rudderstack.com/docs/api/data-regulation-api/#adding-a-suppression-with-delete-regulation) [ de l'API de réglementation des données](https://www.rudderstack.com/docs/api/data-regulation-api/) de Rudderstack.

{% endtab %}
{% tab Suivre %}

La [méthode`track` ](https://rudderstack.com/docs/destinations/marketing/braze/#track) de Rudderstack capture toutes les activités de l'utilisateur et les propriétés associées à ces activités.

**Commande terminée**<br>
En utilisant l'[API eCommerce de RudderStack](https://www.rudderstack.com/docs/event-spec/ecommerce-events-spec/) pour appeler la méthode de suivi d'un événement portant le nom `Order Completed`, RudderStack envoie les produits listés dans cet événement à Braze en tant que [`purchases`]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/exporting_revenue_data/#revenue-data).

{% endtab %}
{% tab Écran %}

La [méthode`screen` de](https://www.rudderstack.com/docs/destinations/streaming-destinations/braze/#screen) Rudderstack vous permet d'enregistrer les vues d'écran mobiles de vos utilisateurs avec toute information supplémentaire sur l'écran visualisé.

{% endtab %}
{% tab Page %}

La méthode [`page`](https://rudderstack.com/docs/destinations/marketing/braze/#page) de Rudderstack vous permet d'enregistrer les pages consultées de votre site web. Il saisit également toute autre information pertinente concernant cette page.

{% endtab %}
{% tab Groupe %}

La méthode [`group`](https://rudderstack.com/docs/destinations/marketing/braze/#group) de Rudderstack vous permet d'associer un utilisateur à un groupe.

**Statut du groupe d'abonnement**<br>
Pour mettre à jour le statut du groupe d'abonnement, activez le paramètre "Activer les groupes d'abonnement dans l'appel de groupe" dans le tableau de bord de Rudderstack et envoyez le statut du groupe d'abonnement dans l'appel de groupe.

{% endtab %}
{% tab Alias %}

La méthode [`alias`](https://www.rudderstack.com/docs/destinations/streaming-destinations/braze/#alias) de Rudderstack vous permet de fusionner différentes identités d'un utilisateur connu. Notez que Rudderstack prend en charge l'appel d'alias pour Braze uniquement en mode cloud.

{% endtab %}
{% endtabs %}

## Envoyer les caractéristiques de l'utilisateur sous forme d'attributs personnalisés imbriqués

Vous pouvez envoyer les traits d'utilisateur à Braze sous forme d'attributs personnalisés imbriqués et effectuer des opérations d'ajout, de mise à jour et de suppression sur ces traits. Pour ce faire, activez le paramètre "Utiliser le tableau de bord des opérations sur les attributs personnalisés" dans RudderStack lors de la configuration de la destination Braze. Cette fonctionnalité n'est disponible qu'en mode cloud.

Vous pouvez envoyer les caractéristiques de l'utilisateur sous forme d'attributs personnalisés imbriqués dans vos événements `identify` dans le format suivant :
```javascript
rudderanalytics.identify("1hKOmRA4GRlm", {
  "cars": {
    "add": [{
      "age": 27,
      "id": 1,
      "name": "Alex Keener"
    }],
    "update": [{
        "age": 30,
        "id": 2,
        "identifier": "id",
        "name": "Rowan"
      },
      {
        "age": 27,
        "id": 1,
        "identifier": "id",
        "name": "Mike"
      }
    ]
  },
  "country": "USA",
  "email": "alex@example.com",
  "firstName": "Alex",
  "gender": "M",
  "pets": [{
      "breed": "beagle",
      "id": 1,
      "name": "Scooby",
      "type": "dog"
    },
    {
      "breed": "calico",
      "id": 2,
      "name": "Garfield",
      "type": "cat"
    }
  ]
})
```

Pour envoyer les caractéristiques de l'utilisateur sous forme d'attributs personnalisés via les appels `track`, `page` ou `screen`, transmettez `traits` comme champ contextuel dans l'événement :
```javascript
rudderanalytics.track("Product Viewed", {
    revenue: 8.99,
    currency: "USD",
 },{
  "traits": {
    "cars": {
      "add": [{
        "age": 27,
        "id": 1,
        "name": "Alex Keener"
      }],
      "update": [{
          "age": 30,
          "id": 2,
          "identifier": "id",
          "name": "Mike"
        },
        {
          "age": 27,
          "id": 1,
          "identifier": "id",
          "name": "Rowan"
        }
      ]
    },
    "city": "Disney",
    "country": "USA",
    "email": "alexa@example.com",
    "firstName": "Alexa",
    "gender": "woman",
    "pets": [{
        "breed": "beagle",
        "id": 1,
        "name": "Scooby",
        "type": "dog"
      },
      {
        "breed": "calico",
        "id": 2,
        "name": "Garfield",
        "type": "cat"
      }
    ]
  }
});
```

{% alert note %}
Pour les opérations de mise à jour et de suppression, `identifier` est une clé obligatoire. Si les opérations d'ajout, de mise à jour ou de suppression ne sont pas présentes dans le tableau imbriqué, Rudderstack utilise par défaut l'opération de création pour créer les propriétés. Reportez-vous à la section [Tableau d'objets]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/array_of_objects/) pour plus d'informations sur l'envoi d'attributs personnalisés imbriqués.
{% endalert %}


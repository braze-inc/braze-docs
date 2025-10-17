---
nav_title: "Connexion à l'API de données client"
article_title: "Connexion à l'API de données clients de Movable Ink"
description: "Cet article de référence explique comment se connecter pour activer les données d'événements clients stockées dans Braze afin de générer du contenu personnalisé dans Movable Ink en utilisant l'API de données client."
page_type: partner
search_tag: Partner
---

# Connexion à l'API de données clients de Movable Ink

> Braze et l'intégration de l'API de données client de Movable Ink permettent aux marketeurs d'activer les données d'événements clients stockées dans Braze pour générer du contenu personnalisé au sein de Movable Ink.

Movable Ink est capable d'ingérer des événements comportementaux depuis Braze via leur API de données clients. Les événements seront stockés sur les profils des utilisateurs en fonction de l'ID utilisateur unique (UUID) qui est transmis à Movable Ink.

Pour plus d'informations sur les Stories, l'API de données client de Movable Ink et comment Movable Ink exploite les données comportementales, veuillez consulter les articles suivants du centre de support :

- [Contenu puissant avec des données comportementales](https://support.movableink.com/hc/en-us/sections/360001239453-Power-content-with-behavioral-data)
- [Introduction et guide de l'API de données clients](https://support.movableink.com/hc/en-us/articles/13815957200663-Customer-Data-API-introduction-and-guide)
- [FAQ : API de données clients](https://support.movableink.com/hc/en-us/articles/12423178752279-FAQ-Customer-Data-API)

## Conditions préalables

| Condition | Descriptif |
|---|---|
| Compte Movable Ink | Un compte Movable Ink est requis pour bénéficier de ce partenariat. |
| Identifiants API Movable Ink | L'équipe Solutions de Movable Ink vous générera des identifiants API. Les identifiants API se composent de :{::nomarkdown}<ul><li>Une URL d'endpoint (où les données seront envoyées)</li><li>Nom d'utilisateur et mot de passe (utilisés pour authentifier l'API)</li></ul>{:/} Si vous le souhaitez, Movable Ink peut fournir le nom d'utilisateur et le mot de passe sous forme de valeur encodée en base64 à utiliser comme valeur d'en-tête d'autorisation de base. |
| Charges utiles d'événements comportementaux | Vous devez partager vos charges utiles d'événements avec l’équipe d’expérience client de Movable Ink. Consultez la section [Partage des charges utiles d'événements](#event-payloads) avec Movable Ink pour plus de détails. |
| Actifs créatifs et logique commerciale | Vous devez partager des ressources créatives avec Movable Ink, notamment des fichiers Adobe Photoshop (PSD) indiquant à Movable Ink comment créer le bloc et une image de secours. Vous devrez également fournir la logique métier pour savoir comment et quand afficher le bloc de contenu activé par le partenaire. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Intégration

### Étape 1 : Créer une campagne de webhook dans Braze

#### Étape 1a: Créer une nouvelle campagne

1. Dans Braze, [créez une campagne de webhook]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/).
2. Donnez un nom et une description facultative à votre campagne.
3. Sélectionnez **Modèle vierge** comme votre modèle.

#### Étape 1b: Ajoutez vos identifiants d'API de données client

1. Dans le champ **URL du webhook**, entrez l'URL de l'endpoint Movable Ink.

![Onglet Compose du webhook composer dans Braze avec l'URL du point de terminaison Movable Ink et le Request Body définis comme des paires clé-valeur JSON.]({% image_buster /assets/img/movable_ink/cd_api_webhook_url.png %}){: style="max-width:75%" }

{:start="2"}
2\. Sélectionnez l'onglet **Paramètres**.
3\. Ajoutez les en-têtes de requête suivants en tant que paires clé-valeur :

| Clé | Valeur |
| --- | --- |
| Content-Type | application/json |
| Autorisation | Entrez l'authentification de base que vous avez reçue de Movable Ink. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![Onglet Paramètres du webhook composer dans Braze avec des paires clé-valeur pour Content-Type et Authorization.]({% image_buster /assets/img/movable_ink/cd_api_webhook_settings.png %}){: style="max-width:75%" }

#### Étape 1c: Configurez votre charge utile

1. Retournez dans l’onglet **Composer**.
2. Pour votre **corps de requête**, créez votre propre corps de requête avec des paires clé-valeur JSON ou entrez votre charge utile d'événement en tant que texte brut. Reportez-vous aux exemples de [charges utiles](#sample-payloads) pour des exemples d'événements de commerce électronique standard.

![Onglet Compose du webhook composer à Braze avec des paires clé-valeur JSON pour l'ID, l'horodatage, l'ID utilisateur et le type d'événement.]({% image_buster /assets/img/movable_ink/cd_api_webhook_kvp.png %}){: style="max-width:75%" }

#### Étape 1d : Testez votre webhook {#step-1d}

Vous devrez partager un échantillon de charge utile avec votre équipe Expérience Client de Movable Ink. Vous pouvez générer cette charge utile dans l'**onglet** Test en fonction de la charge utile que vous avez construite.

{% alert important %}
Movable Ink recommande d'attendre pour tester votre webhook dans Braze jusqu'à ce que votre équipe Expérience Client de Movable Ink ait confirmé qu'elle a terminé le mappage et est prête à recevoir un test. Si ce mappage n'est pas complet, vous recevrez probablement une erreur lors des tests.
{% endalert %}

Pour tester votre webhook, procédez comme suit :

1. Sélectionnez l'onglet **Test**.
2. Prévisualisez le message en tant qu'utilisateur pour voir un exemple de charge utile d'événement pour cet utilisateur. Vous pouvez choisir entre prévisualiser en tant qu'utilisateur aléatoire, utilisateur spécifique ou utilisateur personnalisé.
3. Si tout semble bon, cliquez sur **Envoyer le test** pour envoyer une requête de test.

![Message de réponse du webhook à Braze montrant une réponse 200 OK.]({% image_buster /assets/img/movable_ink/cd_api_webhook_response.png %}){: style="max-width:75%" }

### Étape 2 : Finalisez la configuration de votre campagne

#### Étape 2a: Planifiez votre campagne

Lorsque vous avez terminé de composer et de tester le webhook, [planifiez votre campagne]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types). 

Braze prend en charge les livraisons programmées, basées sur des actions et déclenchées par l'API. [livraison par événement]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/) est généralement la meilleure solution pour la plupart des cas d'utilisation d'événements comportementaux. Pour toute question sur ce qui a du sens pour votre cas d'utilisation, contactez vos responsables de satisfaction client Braze et Movable Ink.

Pour livraison par événement :

1. Spécifiez l'action de déclenchement. C'est l'événement qui déclenchera le webhook vers Movable Ink.
2. Assurez-vous que le **Délai de planification** est réglé sur **Immédiatement**. Les données d'événement doivent être envoyées à Movable Ink immédiatement après l'événement, sans délai.
3. Définissez la durée de la campagne en spécifiant une heure de début. Il est probable qu’il ne soit pas nécessaire de définir une heure de fin, mais il est possible d’en définir une si le cas d'utilisation le requête.

{% alert note %}
Pour vous assurer que les données sont diffusées en temps réel vers Movable Ink, ne sélectionnez pas **Envoyer la campagne aux utilisateurs dans leur fuseau horaire local**.
{% endalert %}

#### Étape 2b: Spécifiez votre audience

Ensuite, déterminez quels utilisateurs vous souhaitez cibler pour cette campagne. Pour plus de détails, consultez la section [Ciblage des utilisateurs]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/targeting_users/).

Veillez à ne pas utiliser le test A/B dans votre campagne en décochant la case **groupe de contrôle**. Si un groupe de contrôle est inclus, les données d’un pourcentage d'utilisateurs ne seront pas envoyées à Movable Ink. L’intégralité de votre audience devrait aller à la variante plutôt qu'au groupe de contrôle.

![Panel de test A/B dans une campagne Braze avec une distribution de 100% de la variante assignée à la variante 1, et aucun groupe de contrôle.]({% image_buster /assets/img/movable_ink/cd_api_webhook_ab.png %})

#### Étape 2c : Choisissez des événements de conversion (facultatif)

Si vous le souhaitez, vous pouvez attribuer des événements de conversion à cette campagne dans Braze.

Cependant, étant donné que le webhook est uniquement destiné à diffuser des données, l'attribution à ce niveau est probablement moins utile que de regarder l'attribution au niveau de la campagne après que les données comportementales de Braze soient utilisées pour personnaliser le contenu.

### Étape 3 : Lancer la campagne

Examinez votre configuration de webhook et lancez votre campagne.

## Considérations

### Aligner sur un identifiant utilisateur unique

Assurez-vous que la valeur de l'identifiant utilisateur unique (UUID) que vous utilisez comme votre `mi_u`, est disponible dans Braze et peut être incluse dans les charges utiles d'événements envoyées à Movable Ink.

Cela garantit que les événements comportementaux auxquels Movable Ink fait référence lors de la génération d'une image sont associés au même client pour lequel ils ont reçu les événements comportementaux. Si la valeur UUID n'est pas la même que celle de Braze `external_id`, l'UUID doit être capturé et transmis à Braze en tant qu'attribut ou dans les propriétés d'événement d'un événement Braze pour exploiter cet identifiant.

Braze suit le comportement des utilisateurs sur plusieurs plateformes (telles que le web et les applications mobiles), de sorte qu'un seul utilisateur peut avoir plusieurs identifiants anonymes distincts. Ces identifiants peuvent être fusionnés dans le seul profil utilisateur connu de Stories lorsqu'un `identify` événement est envoyé à Movable Ink, tant que l'événement `identify` inclut à la fois un identifiant anonyme et l'identifiant unique connu.

Une fois que Movable Ink reçoit un `user_id` pour un seul utilisateur, tous les événements futurs pour cet utilisateur doivent inclure ce même `user_id`.

### Partage des charges utiles d'événements avec Movable Ink {#event-payloads}

Avant de configurer le connecteur à l'API de données clients de Movable Ink, assurez-vous de partager vos charges utiles d'événements avec l’équipe d'expérience client de Movable Ink. Cela permet à Movable Ink de mapper vos événements à leur schéma d'événements et empêchera tout appel API rejeté ou échoué.

Vous pouvez générer une charge utile d'événement dans Braze en utilisant n'importe quelles propriétés d'événement. Générer une charge utile d'exemple pour un utilisateur aléatoire ou en recherchant un ID utilisateur spécifique. Reportez-vous à l'[étape 1d](#step-1d) ci-dessus pour plus de détails.

Partagez cet exemple de charge utile avec votre équipe Expérience Client Movable Ink. Assurez-vous qu'il n'y a pas d'informations personnelles sensibles identifiables dans l'exemple de charge utile (telles que l'adresse e-mail, le numéro de téléphone ou les dates de naissance complètes). 

Pour en savoir plus sur les propriétés des événements personnalisés et le format attendu des données contenues dans les propriétés, consultez [Propriétés des événements personnalisés]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#custom-event-properties).

### Utilisateurs connus contre utilisateurs anonymes

Dans Braze, les événements peuvent être enregistrés sous un profil d'utilisateur anonyme. Les identifiants liés au profil utilisateur lors de la journalisation des événements dépendent de la manière dont l'utilisateur a été créé (via le SDK Braze ou les API) et de son stade actuel dans le cycle de vie de l'utilisateur.

#### Transférer uniquement les événements Braze pour les utilisateurs connus

Dans votre campagne de webhook, utilisez le filtre `External User ID` pour cibler uniquement les utilisateurs qui ont un `external_id` avec le filtre `External User ID` `is not blank`.

#### Transfert des événements Braze pour les utilisateurs anonymes et connus

Si vous souhaitez transférer les événements Braze d'utilisateurs anonymes (utilisateurs avant qu'un `external_id` ne soit attribué à leur profil), vous devrez décider quel identifiant utiliser comme `anonymous_id` pour Movable Ink jusqu'à ce qu'un `external_id` soit disponible. Choisissez un `anonymous_id` qui restera constant sur votre profil utilisateur Braze. Vous pouvez utiliser la logique liquid dans le corps du webhook pour décider s'il faut passer un `anonymous_id` ou un `user_id`.

Pour plus d'informations, consultez les exemples de webhooks sous [exemples de charges utiles](#sample-payloads).

## Exemples de charges utiles

### Événement de vue de produit

{% tabs local %}
{% tab Exemple d'événement déclencheur Braze %}

{% raw %}

```json
{
  "events": [
    {
      "email": "test@braze.com",
      "name": "Product Viewed",
      "time": "2023-12-06T19:20:45+01:00",
      "properties": {
        "categories": [
          {
            "id": "Bathroom",
            "url": "https://example.com/cat/bathroom"
          }
        ],
        "meta": {
          "color": "green"
        },
        "title": "All-Purpose Cleaning Wipes",
        "price": 1.99,
        "id": "56544",
        "url": "https://www.example.com/variants_id/5f08cb918dcc595aa74b0fbc"
      }
    }
  ]
}
```

{% endraw %}

{% endtab %}
{% tab Charge utile de la requête Movable Ink attendue %}

{% raw %}

```
curl --location --request POST 'https://collector.movableink-dmz.com/behavioral/{{key}}' \
--header 'Authorization: Basic {{authorization}}' \
--header 'Content-Type: application/json' \
--data-raw '{
  "anonymous_id": "123-abc-678",
  "event": "product_viewed",
  "properties": {
    "categories": [
      {
        "id": "Bathroom",
        "url": "https://example.com/cat/bathroom"
      }
    ],
    "meta": {
      "color": "green"
    },
    "title": "All-Purpose Cleaning Wipes",
    "price": 1.99,
    "id": "56544",
    "url": "https://www.example.com/variants_id/5f08cb918dcc595aa74b0fbc"
  },
  "timestamp": 1257894000000,
  "timezone": "America/New_York",
  "type": "track",
  "user_id": "5c3aa83113dd490100d3d8d7"
}'

```

{% endraw %}
{% endtab %}
{% tab Exemple de webhook %}

Dans cet exemple, une adresse e-mail hachée est utilisée comme `anonymous_id` pour les utilisateurs qui n'ont pas de `external_id`.

{% raw %}

```liquid
// Converts the timestamp of "now" to seconds since 1970 and assigns it to a local variable "timestamp"
{% assign timestamp = "now" | date: "%s" %}

// Example of md5 hashing the email address to use as the anonymous_id
{% assign anon_id = {{${email_address}}} | md5 %}

// Condition logic to determine which identifier to use. If an external_id is available use that, otherwise use the anonymous_id
{% if {{${user_id}}} %}
{% capture user_identifier %}"user_id": "{{${user_id}}}"{% endcapture %}
{% else %}
{% capture user_identifier %}"anonymous_id": "{{anon_id}}"{% endcapture %}
{% endif %}

{
  {{user_identifier}}
  "event": "product_viewed",
  "properties": {
    "categories": [
      {
        "id": "{{event_properties.${categories}[0].id}}",
        "url": "{{event_properties.${categories}[0].url}}"
      }
    ],
    "meta": {
      "color": "{{event_properties.${meta}.color}}"
    },
    "title": "{{event_properties.${title}}}",
    "price": "{{event_properties.${price}}}",
    "id": "{{event_properties.${id}}}",
    "url": "{{event_properties.${url}}}"
  },
  "timestamp": "{{timestamp}}",
  "timezone": "{{${time_zone}}}",
  "type": "track",
}

```

{% endraw %}
{% endtab %}
{% endtabs %}

### Événement de vue de catégorie

{% tabs local %}
{% tab Exemple d'événement déclencheur Braze %}

{% raw %}

```json
{
  "events": [
    {
      "external_id": "123456789",
      "name": "Category Viewed",
      "time": "2023-12-06T19:20:45+01:00",
      "properties": {
        "id": "bathroom-1",
        "title": "Bathroom Stuff",
        "url": "https://www.example.com/categories/bathroom"
      }
    }
  ]
}
```

{% endraw %}

{% endtab %}
{% tab Charge utile de la requête Movable Ink attendue %}

{% raw %}

```
curl --location --request POST 'https://collector.movableink-dmz.com/behavioral/{{key}}' \
--header 'Authorization: Basic {{authorization}}' \
--header 'Content-Type: application/json' \
--data-raw '{
  "anonymous_id": "123-abc-678",
  "event": "category_viewed",
  "properties": {
    "id": "bathroom-1",
    "title": "Bathroom Stuff",
    "url": "https://www.example.com/categories/bathroom"
  },
  "timestamp": 1257894000000,
  "timezone": "America/New_York",
  "type": "track",
  "user_id": "5c3aa83113dd490100d3d8d7"
}'
```

{% endraw %}

{% endtab %}
{% tab Exemple de webhook %}

Cet exemple montre un webhook suivant les événements uniquement pour les utilisateurs connus (utilisateurs avec un `external_id`).

{% raw %}

```liquid
// Converts the timestamp of "now" to seconds since 1970 and assigns it to a local variable "timestamp"
{% assign timestamp = "now" | date: "%s" %}

{
  "event": "category_viewed",
  "properties": {
    "id": "{{event_properties.${id}}}",
    "title": "{{event_properties.${title}}}",
    "url": "{{event_properties.${url}}}"
  },
  "timestamp": "{{timestamp}}",
  "timezone": "{{${time_zone}}}",
  "type": "track",
  "user_id": "{{${user_id}}}"
}

```

{% endraw %}

{% endtab %}
{% endtabs %}

### Identifier l'événement

{% tabs local %}
{% tab Exemple d'événement déclencheur Braze %}

{% raw %}

```json
{
  "events": [
    {
      "external_id": "123456789",
      "name": "Account Created",
      "time": "2023-12-06T19:20:45+01:00"
    }
  ]
}
```

{% endraw %}
{% endtab %}
{% tab Charge utile de la requête Movable Ink attendue %}

{% raw %}

```
curl --location --request POST 'https://collector.movableink-dmz.com/behavioral/{{key}}' \
--header 'Authorization: Basic {{authorization}}' \
--header 'Content-Type: application/json' \
--data-raw '{
  "anonymous_id": "jg0iq5gd30dqpwn8zmx05p06mzjmjir4r8",
  "timestamp": 1257894000000,
  "timezone": "America/New_York",
  "type": "identify",
  "user_id": "mycustomerid123"
}'
```

{% endraw %}
{% endtab %}
{% tab Exemple de webhook %}

Dans cet exemple, une adresse e-mail hachée est utilisée comme `anonymous_id` pour les utilisateurs qui n'ont pas de `external_id`.

{% raw %}

```liquid
// Converts the timestamp of "now" to seconds since 1970 and assigns it to a local variable "timestamp"
{% assign timestamp = "now" | date: "%s" %}

// Example of md5 hashing the email address to use as the anonymous_id
{% assign anon_id = {{${email_address}}} | md5 %}

{
  "anonymous_id": "{{anon_id}}",
  "timestamp": "{{timestamp}}",
  "timezone": "{{${time_zone}}}",
  "type": "identify",
  "user_id": "{{${user_id}}}"
}

```

{% endraw %}

{% endtab %}
{% endtabs %}




---
nav_title: Zapier
article_title: Zapier
alias: /partners/zapier/
description: "Cet article de référence présente le partenariat entre Braze et Zapier, un outil Web d’automatisation qui vous permet de partager des données entre plusieurs applications Web et d’utiliser ces informations pour créer des actions automatisées."
page_type: partner
search_tag: Partenaire

---
# Intégration de Zapier

> [Zapier][1] est un outil Web d’automatisation qui vous permet de partager des données entre plusieurs applications Web et d’utiliser ces informations pour créer des actions automatisées. 

Le partenariat entre Braze et Zapier exploite l’API Braze et les [Webhooks][3] de Braze pour se connecter à des applications tierces, telles que Google Workplace, Slack, Salesforce, WordPress et plus encore afin d’automatiser diverses actions.

## Conditions préalables

| Conditions | Description |
|---|---|
| Compte Zapier | Un compte Zapier est requis pour profiter de ce partenariat. |
| Endpoint REST de Braze | URL de votre endpoint REST. Votre endpoint dépendra de l’[URL Braze pour votre instance][0]. |
{: .reset-td-br-1 .reset-td-br-2}

## Intégration

Dans l’exemple de Zapier ci-dessous, nous enverrons des informations de WordPress vers Braze à l’aide d’un Webhook POST. Ces informations peuvent ensuite être utilisées pour créer un Canvas Braze.

### Étape 1 : Créer un déclencheur Zapier

Selon la terminologie de Zapier, un « zap » est un flux de travail automatisé qui connecte vos applications et services. La première étape de n’importe quel zap consiste à désigner un déclencheur. Une fois votre zap activé, Zapier effectue automatiquement les actions appropriées chaque fois que votre déclencheur est détecté.

En utilisant notre exemple WordPress, dans la plateforme Zapier, nous allons configurer notre zap pour qu’il se déclenche lorsqu’un nouveau message est publié dans WordPress, en sélectionnant **Published (Publié)** et **Posts (Publications)** comme **Post Status (Statut de publication)** et **Post Type (Type de publication)**. 

![Sur la plateforme Zapier, dans un zap, choisissez l’un des déclencheurs suivants : « new comment (nouveau commentaire) », « any Webhook (n’importe quel Webhook) » ou « new post (nouvelle publication) ». Dans cet exemple, nous avons sélectionné « new post (nouvelle publication) ». ] [5]

![Sur la plateforme Zapier, dans un zap, configurez le déclencheur en sélectionnant le statut et le type de publication souhaités. Dans cet exemple, nous avons sélectionné « Published (Publié) » et « Posts (Publications) ».] [6]

### Étape 3 : Ajouter un Webhook d’action

Ensuite, définissez l’action zap. Une fois votre zap activé, l’action se produira automatiquement lorsque votre déclencheur est détecté.

Pour poursuivre notre exemple, nous souhaitons envoyer une requête POST en tant que JSON à un endpoint Braze. Pour cela, il faut sélectionner l’option **Webhooks** sous **Apps**.

![][7]

### Étape 4 : Configurer un Braze POST

Lors de la configuration de votre webhook, utilisez les paramètres suivants et fournissez votre endpoint REST Braze dans l'URL du webhook. Une fois terminé, sélectionnez **Publish (Publier)**.

- **Méthode** : POST
- **URL du webhook** : `https://rest.iad-01.braze.com/canvas/trigger/send`
- **Transmission des données** : False
- **Non aplati** : Non
- **En-tête de requête** :
  - **Type de contenu** : JSON
  - **Autorisation** : Bearer YOUR-API-KEY
- **Données** : 

```json
{
  "canvas_id": "your_canvas_identifier",
  "recipients": [
    {
      "external_user_id": "external_user_identifier",
      "canvas_entry_properties":{
        "string_property": "Your example string",
        "example_integer_property": 1
      }
    }
  ]
}
```

![][4]{: style="max-width:70%;"}

### Étape 5 : Créer une campagne Braze

Après avoir configuré votre zap, vous pouvez personnaliser vos campagnes ou Canvas Braze avec des données WordPress en utilisant le formatage de Liquid pour afficher les informations contenues dans vos messages.

[0]: {{site.baseurl}}/api/basics/#api-definitions
[1]: https://zapier.com/
[3]: {{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/#creating-a-webhook
[4]:{% image_buster /assets/img/zapier.png %}
[5]:{% image_buster /assets/img_archive/zapier1.png %}
[6]:{% image_buster /assets/img_archive/zapier2.png %}
[7]:{% image_buster /assets/img_archive/zapier3.png %}
[8]:{% image_buster /assets/img_archive/zapier4.png %}
[10]:{% image_buster /assets/img_archive/zapier5.png %}
[12]:{% image_buster /assets/img_archive/zapier6.png %}
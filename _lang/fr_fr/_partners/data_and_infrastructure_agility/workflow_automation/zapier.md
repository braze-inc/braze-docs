---
nav_title: Zapier
article_title: Zapier
alias: /partners/zapier/
description: "Cet article de référence décrit le partenariat entre Braze et Zapier, un outil Web d'automatisation qui vous permet de partager des données entre des applications Web et d'utiliser ces informations pour automatiser des actions."
page_type: partner
search_tag: Partner

---
# L'intégration de Zapier

> [Zapier][1] est un outil Web d'automatisation qui vous permet de partager des données entre des applications Web, puis d'utiliser ces informations pour automatiser les actions. 

Le partenariat entre Braze et Zapier s'appuie sur l'API Braze et les [webhooks][3] Braze pour se connecter à des applications tierces, telles que Google Workplace, Slack, Salesforce, WordPress, etc. afin d'automatiser diverses actions.

## Conditions préalables

| Exigences | Description |
|---|---|
| Compte Zapier | Un compte Zapier est nécessaire pour bénéficier de ce partenariat. |
| Endpoint REST de Braze | L'URL de votre endpoint REST. Votre endpoint dépendra de l'[URL de Braze pour votre instance][0]. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Intégration

Dans l'exemple Zapier suivant, nous allons envoyer des informations depuis WordPress à Braze à l'aide d'un webhook POST. Ces informations peuvent ensuite être utilisées pour créer un canvas Braze.

### Étape 1 : Création d'un déclencheur Zapier

Selon la terminologie de Zapier, un « zap » est un flux de travail automatisé qui connecte vos applications et vos services. La première partie de tout zap consiste à désigner un déclencheur. Une fois votre zap activé, Zapier effectuera automatiquement les actions correspondantes chaque fois que votre déclencheur est détecté.

En utilisant notre exemple WordPress, sur la plateforme Zapier, nous allons configurer notre zap pour qu'il se déclenche lorsqu'un nouveau message WordPress est ajouté et nous sélectionnerons **Publié** et **Articles** comme **État de publication** et **Type de publication**. 

![Sur la plateforme Zapier, dans un zap, sélectionnez le déclencheur comme « nouveau commentaire », « n'importe quel webhook » ou « nouvelle publication ». Dans cet exemple, « nouvelle publication » est sélectionnée. ][5]]

![Dans la plateforme Zapier, dans un zap, configurez le déclencheur en sélectionnant le statut et le type de publication souhaités. Dans cet exemple, « Publié » et « Publications » sont sélectionnés. ][6]]

### Étape 2 : Ajouter un webhook d'action

Définissez ensuite l'action de zap. Lorsque votre zap est activé et que votre déclencheur est détecté, l'action se produit automatiquement.

Toujours dans le cadre de notre exemple, nous voulons envoyer une requête POST en tant que fichier JSON à un endpoint Braze. Cela peut être fait en sélectionnant l'option **Webhooks** sous **Applications**.

![][7]

### Étape 3 : Configurer Braze POST

Lorsque vous configurez votre webhook, utilisez les paramètres suivants et indiquez votre endpoint Braze REST dans l'URL du webhook. Lorsque vous avez terminé, sélectionnez **Publier**.

- **Méthode** : POST
- **URL du webhook**: `https://rest.iad-01.braze.com/canvas/trigger/send`
- **Transmission des données :** Faux
- **Restructuration** : Non
- **En-tête de la requête** :
  - **Type de contenu : application/json**
  - **Autorisation**: Porteur de VOTRE CLÉ API
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

### Étape 4 : Créez une campagne Braze

Une fois que vous avez configuré votre zap avec succès, vous pouvez personnaliser vos campagnes Braze ou Canvases avec les données de WordPress en utilisant le formatage Liquid pour afficher les informations contenues dans vos messages.

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
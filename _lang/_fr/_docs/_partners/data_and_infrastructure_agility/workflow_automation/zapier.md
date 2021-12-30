---
nav_title: Zapier
article_title: Zapier
alias: /fr/partners/zapier
description: "Cet article décrit le partenariat entre Braze et Zapier, un outil web d'automatisation qui vous permet de partager des données entre les applications web, et d'utiliser ces informations pour automatiser les actions."
page_type: partenaire
search_tag: Partenaire
---

# Intégration de Zapier

> [Zapier][1] est un outil web d'automatisation qui vous permet de partager des données entre les applications web, puis d'utiliser ces informations pour automatiser les actions.

Le partenariat Braze et Zapier tire parti de l'API Braze et des [webhooks Braze][3] pour se connecter à des applications tierces - telles que Google Workplace, Slack, Salesforce, WordPress, etc. pour automatiser diverses actions.

## Pré-requis

| Exigences                       | Libellé                                                                                                    |
| ------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| Compte Zapier                   | Un compte Zapier est requis pour profiter de ce partenariat.                                               |
| Point de terminaison REST Braze | Votre URL de terminaison REST. Votre point de terminaison dépendra de l'URL [Braze pour votre instance][]. |
{: .reset-td-br-1 .reset-td-br-2}

## Intégration

Dans l'exemple Zapier ci-dessous, nous enverrons des informations de WordPress à Braze en utilisant un webhook POST. Cette information peut alors être utilisée pour créer une campagne Braze ou Canvas.

### Étape 1 : Créer un déclencheur Zapier

En utilisant la terminologie de Zapier, un "zap" est un flux de travail automatisé qui connecte vos applications et vos services. La première partie de tout zap est de désigner un déclencheur. Une fois que votre zap est activé, Zapier effectuera automatiquement les actions respectives chaque fois que votre déclencheur est détecté.

En utilisant notre exemple WordPress, dans la plateforme Zapier, Nous allons configurer notre zap pour déclencher quand un nouveau post WordPress est ajouté et sélectionnez **Publié** et **Posts** comme **Statut de Post** et **Type de Post**.

!\[Nouveau message Zapier\] \[5\]

!\[Zapier published options\] \[6\]

### Étape 3 : Ajouter un webhook d'action

Ensuite, définissez l'action zap. Lorsque votre zap est activé et que votre déclencheur est détecté, l'action se produit automatiquement.

En poursuivant notre exemple, nous voulons envoyer une requête POST en JSON à un point de terminaison Braze. Cela peut être fait en sélectionnant l'option **Webhooks** sous **Apps**.

!\[webhook Zapier\] \[7\]

### Étape 4 : Configurer Braze POST

Tout d'abord, choisissez **POST** comme type d'action du webhook. Ensuite, assurez-vous de remplir les champs suivants en utilisant votre point de terminaison Braze REST dans l'URL du webhook :

- **URL du Webhook**: `https://rest.iad-01.braze.com/campaigns/trigger/send`
- **Type de charge** : JSON
- **Données** : `trigger_properties__name`, `api_key`, et `campaign_id` Ces champs de données sont des paires de valeur clé qui seront utilisées pour la portion de données de la requête.

!\[Zapier POST\] \[10\]

### Étape 5 : Créer une campagne de Braze

!\[Campagne Zapier\] \[12\]

Une fois que vous avez configuré votre zap, vous pouvez personnaliser vos campagnes Braze ou Canvases avec des données Wordpress en utilisant le formatage Liquid pour afficher l'information dans vos messages.
[5]:{% image_buster /assets/img_archive/zapier1.png %} [6]:{% image_buster /assets/img_archive/zapier2.png %} [7]:{% image_buster /assets/img_archive/zapier3. ng %} [8]:{% image_buster /assets/img_archive/zapier4.png %} [10]:{% image_buster /assets/img_archive/zapier5.png %} [12]:{% image_buster /assets/img_archive/zapier6.png %}

[Braze pour votre instance]: {{site.baseurl}}/api/basics/#api-definitions
[1]: https://zapier.com/
[3]: {{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/#creating-a-webhook
---
nav_title: Zapier
article_title: Zapier
alias: /fr/partners/zapier
description: "Cet article décrit le partenariat entre Braze et Zapier, un outil web d'automatisation qui vous permet de partager des données entre les applications web, et d'utiliser ces informations pour automatiser les actions."
page_type: partenaire
search_tag: Partenaire
---

# Intégration de Zapier

[Zapier][1] est un outil web d'automatisation qui vous permet de partager des données entre les applications web, puis d'utiliser ces informations pour automatiser les actions. Vous pouvez utiliser les terminaux API de la plateforme Braze et les [webhooks][3] pour vous connecter à des applications tierces — comme Google Workplace, Slack, Salesforce, etc—et automatise une variété d'actions.

Dans l'exemple Zapier ci-dessous, nous enverrons des informations de Wordpress à Braze en utilisant un webhook POST. Nous utiliserons ensuite ces informations pour créer une campagne de Braze.

### Étape 1: Ajoutez WordRress comme déclencheur et sélectionnez un nouveau message après la connexion de votre compte:

En utilisant la terminologie de Zapier, un "zap" est un flux de travail automatisé qui relie vos applications et vos services ensemble. La première partie de tout zap est de désigner un déclencheur. Une fois que votre zap est activé, chaque fois que votre déclencheur est détecté, Zapier effectuera automatiquement ses actions respectives.

En utilisant notre exemple Wordpress, nous allons mettre en place notre déclencheur comme un post Wordpress publié.

!\[zapier1\] \[5\]

!\[zapier2\] \[6\]

### Étape 3: Ajouter une action "webhook" :

La deuxième partie de tout zap est l'action. Lorsque votre zap est activé et que votre déclencheur est détecté, l'action se produit automatiquement.

En utilisant le même exemple, notre action enverra une requête POST en JSON à un point de terminaison Braze.

!\[zapier3\] \[7\]

### Étape 4 : Choisissez POST comme type :

!\[zapier4\] \[8\]

### Étape 5 : Configurer Braze POST:

URL : `https://rest.iad-01.braze.com/campaigns/trigger/send`

Type de charge utile : JSON

Données : `trigger_properties__name`, `api_key`, `campaign_id` Ces champs de données sont des paires clé-valeur qui seront pour la partie données de la requête.

!\[zapier5\] \[10\]

> Ce qui précède est un exemple pour les clients sur l'instance `US-01`. Si vous n'êtes pas sur cette instance, veuillez vous référer à notre [documentation API][66] pour voir à quel point de terminaison vous devez faire des demandes.

## Étape 6: Créer une campagne de Braze :

!\[zapier6\] \[12\]

Une fois que vous avez configuré votre zap, vous pouvez maintenant utiliser les informations qui vous sont envoyées pour personnaliser votre campagne et envoyer vos messages. Vous pouvez également utiliser trigger_properties avec Liquid pour filtrer ce que ou si le message est envoyé.
[5]:{% image_buster /assets/img_archive/zapier1.png %} [6]:{% image_buster /assets/img_archive/zapier2.png %} [7]:{% image_buster /assets/img_archive/zapier3. ng %} [8]:{% image_buster /assets/img_archive/zapier4.png %} [10]:{% image_buster /assets/img_archive/zapier5.png %} [12]:{% image_buster /assets/img_archive/zapier6.png %}

[1]: https://zapier.com/
[3]: {{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/#creating-a-webhook
[66]: {{site.baseurl}}/developer_guide/rest_api/messaging/#sending-messages-via-api-triggered-delivery

---
nav_title: Jampp
article_title: Jampp
alias: /fr/partners/jampp/
description: "Cet article décrit le partenariat entre Braze et Jampp, une plateforme de marketing performant pour l'acquisition et le repositionnement de clients mobiles."
page_type: partenaire
search_tag: Partenaire
---

# Jampp

> Jampp est une plateforme de marketing performante pour l'acquisition et le reciblage de clients mobiles. Il combine des données comportementales avec des technologies prédictives et programmatiques pour générer des revenus pour les annonceurs en montrant leur caractère personnel, des publicités pertinentes qui incitent les consommateurs à acheter pour la première fois, ou plus souvent.

Les clients de Braze peuvent s’intégrer à Jampp en configurant le canal de webhook Braze pour diffuser des événements en Jampp. En conséquence, les clients peuvent ajouter des ensembles de données plus riches à leurs initiatives de redistribution avec Jampp au sein de l'écosystème de publicité mobile.

## Cas de redistribution

Quelques exemples de quand vous voulez rediriger les clients avec une publicité:
- Quand le courrier électronique d'un client ou le statut de l'abonnement push changent.
- Comment un client a interagi avec une campagne de messagerie Braze.
- Si le client a déclenché un géorepérage spécifique.

L'une des meilleures façons d'y parvenir est d'utiliser Braze ainsi qu'un partenaire de redistribution spécialisé dans le mobile, tel que Jampp. Vous voulez que le partenaire de rétractation reçoive les informations utilisateur automatisées de Braze à l'aide de webhooks. Vous pourrez tirer parti des capacités de ciblage et de déclenchement de Braze pour envoyer des événements à Jampp, qui pourrait ensuite être utilisé pour définir les définitions de campagnes de redistribution dans Jampp.

## Pré-requis pour l'intégration

Cette intégration prend en charge les applications iOS et Android.

| Exigences                                                        | Source  | Libellé                                                                                                                            |
| ---------------------------------------------------------------- | ------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| Android App ID                                                   | Brasero | Votre identifiant d'application unique pour Android (c.-à-d. « com.example »).                                                     |
| ID de l'application iOS                                          | Brasero | Votre identifiant d'application unique pour iOS (c.-à-d. « 012345678 »).                                                           |
| Activer IDFA Collection dans Braze SDK                           | Brasero | [La collection IDFA][4] est facultative dans le SDK Braze et désactivée par défaut.                                                |
| Collection de Google Advertising ID via un attribut personnalisé | Google  | La collection Google Advertising ID est facultative pour les clients et peut être collectée en tant qu'attribut [personnalisé][5]. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

{% alert important %}
Braze ne collecte pas automatiquement l'appareil IDFA/AAID, vous devez donc stocker ces valeurs vous-même. Veuillez noter que vous pouvez exiger le consentement de l'utilisateur pour collecter ces données.
{% endalert %}

# Intégration

### Étape 1 : Créer un modèle de webhook dans Braze

Vous pouvez créer ceci à partir de la section `Modèles & Médias` ou créer une nouvelle campagne de webhook en Brésil.

!\[Jampp_Webhook_Template\]\[6\]

### Étape 2 : Remplissez votre modèle

Pour ce webhook, toutes les données sont transmises à côté de l'URL HTTP en tant que paramètres de chaîne de requêtes. Les paramètres suivants qui doivent être définis :

- Vous devrez définir le nom de l'événement. Ceci est pour définir le nom de l'événement qui apparaîtra dans votre tableau de bord Jampp.
- Jampp exige que vous transmettiez l’identifiant unique de votre application pour Android (c.-à-d. « com.example») et iOS (c.-à-d. « 012345678»).
- Vous devrez également insérer [Liquid][1] pour l'attribut personnalisé approprié que vous suivez l'identifiant Google Advertising.

Voici un exemple de ce à quoi pourrait ressembler votre URL Webhook :

{% raw %}
```
{% assign event_name = 'your_jampp_event_name' %}
{% assign android_app_id = 'your_android_app_id' %}
{% assign iOS_app_id = 'your_iOS_app_id' %}

{% capture json %}{'name':'{{event_name}}', active':true,'joined':{{'maintenant' | date: '%s' }}}{% endcapture %}

http://tracking. ampp.com/event?kind={{event_name}}&rnd={{rnd}}&app={% if {{most_recently_used_device.${idfa}}} == vide %}{{android_app_id}}{% else %}{{iOS_app_id}}{% endif %}&apple_ifa={{most_recently_used_device.${idfa}}}&google_advertising_id={{custom_attribute.${aaid}}}&user_agent={user-agent}&prtnr=briser

{% si {{most_recently_used_device.${idfa}}} == vide et {{custom_attribute.${aaid}}} == vide %}
{% abort_message('No IDFA or AAID available') %}
{% endif %}
```

Éléments (à partir de l'exemple ci-dessus) à modifier avant d'envoyer la campagne:
1. `{% assign event_name = 'your_jampp_event_name' %}`
2. `{% assign android_app_id = 'your_android_app_id' %}`
3. `{% assign iOS_app_id = 'your_iOS_app_id' %}`
4. `&google_advertising_id={{custom_attribute.${aaid}}`
{% endraw %}

Veuillez noter que dans cet exemple l'identifiant Google Advertising est listé comme `aaid` mais vous devrez le remplacer par le nom d'attribut personnalisé que vos développeurs ont défini.

Après avoir défini les paramètres ci-dessus, insérez ce modèle de code Liquid dans le champ URL Webhook et modifiez si nécessaire. Vous n'avez pas à définir de Corps de Requête pour ce webhook. Voici le modèle en Brésil :

!\[Webhook Template Jampp\]\[2\]

#### En-têtes de requête et méthode

Le `Content-Type` doit être pré-rempli comme une paire clé-valeur dans le modèle de webhook.

!\[Méthode Jampp\]\[3\]

### Étape 3 : Aperçu de votre demande

Pour s'assurer que la requête s'affiche correctement pour différents utilisateurs, utilisez l'aperçu du message. Une bonne approche est de prévisualiser le Webhook pour les utilisateurs Android et iOS. Vous pouvez également envoyer des demandes de test à ces utilisateurs. Si la requête a réussi, l'API répond avec `HTTP 204`.

{% alert important %}
N'oubliez pas d'enregistrer votre modèle avant de quitter la page!
{% endalert %}
[2]: {% image_buster /assets/img/jampp_webhook.png %} [3]: {% image_buster /assets/img/jampp_method.png %} [6]: {% image_buster /assets/img/jampp_webhook_template.png %}

[1]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/using_liquid/#using-liquid
[4]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/optional_idfa_collection/#optional-idfa-collection
[5]: {{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#custom-attribute-data-types

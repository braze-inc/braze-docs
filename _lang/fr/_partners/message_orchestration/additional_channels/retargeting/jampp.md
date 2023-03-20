---
nav_title: Jampp
article_title: Jampp
alias: /partners/jampp/
description: "Cet article de référence présente le partenariat entre Braze et Jampp, une plateforme de marketing de performance utilisée pour acquérir et recibler les clients mobiles."
page_type: partner
search_tag: Partenaire

---

# Jampp

> [Jampp](https://www.jampp.com/) est une plateforme de marketing de performance utilisée pour acquérir et recibler les clients mobiles. Jampp combine des données comportementales avec une technologie prédictive et programmatique pour générer des revenus pour les annonceurs en montrant des publicités personnelles et pertinentes qui inspirent les consommateurs à acheter pour la première fois ou plusieurs fois.

L’intégration de Braze et Jampp permet aux utilisateurs de Braze de synchroniser les événements dans Jampp via des événements webhook de Braze. Par conséquent, les clients peuvent ajouter des ensembles de données plus riches à leurs initiatives de reciblage dans leurs écosystèmes de publicité mobile.

Voici quelques exemples de situations où vous voudriez recibler les clients avec une publicité :
- Lorsque l’état de l’abonnement à l’e-mail ou aux notifications push d’un client change.
- Lorsqu’un client interagit avec une campagne de communication Braze.
- Si le client a déclenché une geofence spécifique.

## Conditions préalables

Cette intégration prend en charge les applications iOS et Android.

| Condition | Description |
|---|---|
| Compte Jampp | Un [compte Jampp](https://www.jampp.com/) est requis pour profiter de ce partenariat. |
| ID d’application Android | Votre identifiant d’application Braze unique pour Android (c.-à-d. « com.exemple »). |
| ID d’application iOS | Votre identifiant d’application Braze unique pour iOS (c.-à-d. « 012345678 »). |
| Activer la collection IDFA dans SDK Braze | La collection IDFA est facultative dans le SDK Braze et désactivée par défaut. | 
| Collection d’ID publicitaires Google via un attribut personnalisé | La collection d’ID publicitaires Google est facultative pour les clients et peut être collectée en tant qu’[attribut personnalisé][5].
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

## Intégration

### Étape 1 : Créer votre modèle de webhook dans Braze

Pour créer un modèle de webhook Jampp à utiliser dans les campagnes ou les Canvas, accédez à la section **Templates & Media (Modèles et médias)** dans la plateforme Braze. Si vous souhaitez créer une campagne de webhook Jampp unique ou utiliser un modèle existant, sélectionnez **Webhook** dans Braze lors de la création d’une nouvelle campagne.

Dans votre nouveau modèle de webhook, renseignez les champs suivants :
- **Corps de la demande** : Texte brut
- **URL du webhook** : 
{% raw %}
```liquid
{% assign event_name = 'your_jampp_event_name' %}
{% assign android_app_id = 'your_android_app_id' %}
{% assign iOS_app_id = 'your_iOS_app_id' %}

{% capture json %}{'name':'{{event_name}}','active':true,'joined':{{'now' | date: '%s' }}}{% endcapture %}

http://tracking.jampp.com/event?kind={{event_name}}&rnd={{rnd}}&app={% if {{most_recently_used_device.${idfa}}} == blank %}{{android_app_id}}{% else %}{{iOS_app_id}}{% endif %}&apple_ifa={{most_recently_used_device.${idfa}}}&google_advertising_id={{custom_attribute.${aaid}}}&user_agent={user-agent}&prtnr=braze

{% if {{most_recently_used_device.${idfa}}} == blank and {{custom_attribute.${aaid}}} == blank %}
{% abort_message('No IDFA or AAID available') %}
{% endif %}
```
{% endraw %}

Dans l’URL du webhook, vous devez :
- Définir le nom de l’événement. Ce nom apparaîtra dans votre tableau de bord Jampp.
- Transmettre votre identifiant d’application unique pour Android (c.-à-d. « com.exemple ») et iOS (c.-à-d. « 012345678 »).
- Insérer la valeur [Liquid][1] pour l’attribut personnalisé approprié que vous suivez comme identifiant publicitaire Google. Notez que l’ID publicitaire Google est répertorié comme `aaid` dans cet exemple, mais vous devrez le remplacer par le nom d’attribut personnalisé défini par vos développeurs.

![URL du webhook et aperçu du message affichés dans le générateur de webhooks de Braze.][2]

{% alert important %}
Braze ne collecte pas automatiquement IDFA/AAID de l’appareil, vous devez donc stocker ces valeurs vous-même. Sachez que vous pouvez avoir besoin du consentement de l’utilisateur pour collecter ces données.
{% endalert %}

#### En-têtes et méthode de la requête

Le webhook Jampp nécessite une méthode HTTP et un en-tête de demande.

- **Méthode HTTP** : GET
- **En-têtes de requête** :
  - **Type de contenu** : application/json

![En-têtes de demande, méthode HTTP et aperçu du message affichés dans le générateur de webhooks de Braze.][3]

#### Corps de la demande

Vous ne devez pas définir un corps de demande pour ce webhook.

### Étape 2 : Prévisualiser votre demande

Prévisualisez le message pour vous assurer que la demande est correctement rendue pour différents utilisateurs. Nous recommandons de prévisualiser et d’envoyer des tests de demandes pour les utilisateurs Android et iOS. Si la demande aboutit, l’API renvoie `HTTP 204`.

{% alert important %}
N’oubliez pas d’enregistrer votre modèle avant de quitter la page ! <br>Des modèles de webhook mis à jour sont disponibles dans la liste **Saved Webhook Templates (Modèles de webhooks enregistrés)** lorsque vous créez une nouvelle [campagne de webhook]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/). 
{% endalert %}

[1]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/using_liquid/#using-liquid
[2]: {% image_buster /assets/img/jampp_webhook.png %}
[3]: {% image_buster /assets/img/jampp_method.png %}
[4]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/optional_idfa_collection/#optional-idfa-collection
[5]: {{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#custom-attribute-data-types

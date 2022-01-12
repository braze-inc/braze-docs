---
nav_title: Jampp
article_title: Jampp
alias: /fr/partners/jampp/
description: "Cet article décrit le partenariat entre Braze et Jampp, une plateforme de marketing performante utilisée pour l'acquisition et le repositionnement des clients mobiles."
page_type: partenaire
search_tag: Partenaire
---

# Jampp

> [Jampp](https://www.jampp.com/) est une plate-forme de marketing performante utilisée pour l'acquisition et le repositionnement de clients mobiles. Jampp combine les données comportementales avec la technologie prédictive et programmatique pour générer des revenus pour les annonceurs en montrant leur personnalité, des publicités pertinentes qui incitent les consommateurs à acheter pour la première fois ou plus souvent.

L'intégration de Braze et de Jampp permet aux utilisateurs de Braze de synchroniser les événements avec Jampp via les événements de Braze webhook. En conséquence, les clients peuvent ajouter des ensembles de données plus riches à leurs initiatives de redistribution dans leurs écosystèmes publicitaires mobiles.

Quelques exemples de quand vous voulez rediriger les clients avec une publicité:
- Quand le courrier électronique d'un client ou le statut de l'abonnement push changent.
- Comment un client a interagi avec une campagne de messagerie Braze.
- Si le client a déclenché un géorepérage spécifique.

## Pré-requis

Cette intégration prend en charge les applications iOS et Android.

| Exigences                                                        | Libellé                                                                                                                               |
| ---------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| Compte Jampp                                                     | Un \[compte Jampp\] \[https://www.jampp.com/\] est requis pour profiter de ce partenariat.                                            |
| Android app ID                                                   | Votre unique identifiant d'application Braze pour Android (c’est-à-dire "com.exemple").                                               |
| ID de l'application iOS                                          | Votre unique identifiant d'application Braze pour iOS (c'est-à-dire "012345678").                                                     |
| Activer la collection IDFA dans Braze SDK                        | La collection IDFA est optionnelle dans le Braze SDK et désactivée par défaut.                                                        |
| Collection d'ID de publicité Google via un attribut personnalisé | La collection Google d'ID publicitaire est facultative pour les clients et peut être collectée en tant qu'attribut [personnalisé][5]. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

## Intégration

### Étape 1 : Créer un modèle de webhook dans Braze

Créer un modèle de webhook Jampp à utiliser dans de futures campagnes ou Canvases, accédez à la section **Modèles & Médias** de la plateforme Braze. Si vous souhaitez créer une campagne Jampp unique ou utiliser un modèle existant, sélectionnez **Webhook** dans Braze lors de la création d'une nouvelle campagne.

Dans votre nouveau modèle Webhook, remplissez les champs suivants :
- **Corps de la requête**: Texte brut
- **URL du Webhook**:
{% raw %}
```liquid
{% assign event_name = 'your_jampp_event_name' %}
{% assign android_app_id = 'your_android_app_id' %}
{% assign iOS_app_id = 'your_iOS_app_id' %}

{% capture json %}{'name':'{{event_name}}', active':true,'joined':{{'maintenant' | date: '%s' }}}{% endcapture %}

http://tracking. ampp.com/event?kind={{event_name}}&rnd={{rnd}}&app={% if {{most_recently_used_device.${idfa}}} == vide %}{{android_app_id}}{% else %}{{iOS_app_id}}{% endif %}&apple_ifa={{most_recently_used_device.${idfa}}}&google_advertising_id={{custom_attribute.${aaid}}}&user_agent={user-agent}&prtnr=briser

{% si {{most_recently_used_device.${idfa}}} == vide et {{custom_attribute.${aaid}}} == vide %}
{% abort_message('No IDFA or AAID available') %}
{% endif %}
```
{% endraw %}

Dans l'URL du webhook ci-dessus, vous devez :
- Définit le nom de l'événement. Ce nom apparaîtra dans votre tableau de bord Jampp.
- Passez l'identifiant unique de votre application pour Android (c'est-à-dire "com.example") et iOS (c'est-à-dire "012345678").
- Insérez [Liquid][1] pour l'attribut personnalisé approprié que vous suivez en tant qu'identifiant publicitaire Google. Veuillez noter que l'ID de la publicité Google est listé comme `aaid` dans cet exemple, mais vous devrez le remplacer par le nom d'attribut personnalisé que vos développeurs ont défini.

!\[Webhook template Jampp\]\[2\]

{% alert important %}
Braze ne collecte pas automatiquement l'appareil IDFA/AAID, vous devez donc stocker ces valeurs vous-même. Veuillez noter que vous pouvez exiger le consentement de l'utilisateur pour collecter ces données.
{% endalert %}

#### En-têtes de requête et méthode

Le webhook Jampp nécessite une méthode HTTP et un en-tête de requête.

- **Méthode HTTP**: GET
- **En-têtes de la requête**:
  - **Content-Type**: application/json

!\[méthode Jampp\]\[3\]

#### Corps de la requête

Vous n'avez pas à définir le corps de la requête pour ce webhook.

### Étape 2 : Aperçu de votre demande

Aperçu du message pour s'assurer que la requête est correctement affichée pour les différents utilisateurs. Nous recommandons la prévisualisation et l'envoi de demandes de test pour les utilisateurs Android et iOS. Si la requête est réussie, l'API répondra avec `HTTP 204`.

{% alert important %}
N'oubliez pas d'enregistrer votre modèle avant de quitter la page! <br>Les modèles de webhook mis à jour peuvent être trouvés dans la liste **Modèles de Webhook enregistrés** lors de la création d'une nouvelle [campagne webhook]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/).
{% endalert %}
[2]: {% image_buster /assets/img/jampp_webhook.png %} [3]: {% image_buster /assets/img/jampp_method.png %}

[1]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/using_liquid/#using-liquid
[5]: {{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#custom-attribute-data-types
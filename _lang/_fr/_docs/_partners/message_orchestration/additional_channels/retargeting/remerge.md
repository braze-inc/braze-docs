---
nav_title: Rafraîchir
article_title: Rafraîchir
alias: /fr/partners/refusion/
description: "Cet article décrit le partenariat entre Braze et Remerge, une application conçue pour le repositionnement à grande échelle, vous doter d'outils permettant de segmenter efficacement les audiences d'applications et les utilisateurs de retarget."
page_type: partenaire
search_tag: Partenaire
---

# Rafraîchir

> [Remerge](https://www.remerge.io/) est conçu pour vous permettre de rediriger des applications à l'échelle, en vous armant d'outils pour segmenter efficacement les publics d'applications et les utilisateurs de retarget.

L'intégration de Braze et Remerge vous aide à développer la robustesse, campagnes de marketing de cycle de vie de plusieurs canaux en envoyant des données utilisateur à Remerge via des événements webhook pour aider les utilisateurs de retarget à travers leur plate-forme mobile à la demande.

## Pré-requis

| Exigences                                 | Libellé                                                                                 |
| ----------------------------------------- | --------------------------------------------------------------------------------------- |
| Compte Remerge                            | Un compte Remerge est nécessaire pour profiter de ce partenariat.                       |
| Clé Remerge webhook                       | Cette clé sera fournie par Remerge.                                                     |
| Android app ID                            | Votre unique identifiant d'application Braze pour Android (c'est-à-dire "com.exemple"). |
| ID de l'application iOS                   | Votre unique identifiant d'application Braze pour iOS (c'est-à-dire "012345678").       |
| Activer la collection IDFA dans Braze SDK | La collection IDFA est optionnelle dans le Braze SDK et désactivée par défaut.          |
{: .reset-td-br-1 .reset-td-br-2}

## Intégration

### Étape 1 : Créez votre modèle de webhook Braze

Pour créer un modèle de webhook Remerge pour de futures campagnes ou Canvases, accédez à la section **Modèles & Médias** de la plateforme Braze. Si vous souhaitez créer une campagne Remerge unique ou utiliser un modèle existant, sélectionnez **Webhook** dans Braze lors de la création d'une nouvelle campagne.

Dans votre nouveau modèle Webhook, remplissez les champs suivants :
- **Corps de la requête**: Texte brut
- **URL du Webhook**:
{% raw %}
```liquid
{% assign event_name = 'your_remerge_event_name' %} 
{% assign android_app_id = 'your_android_app_id' %} 
{% assign iOS_app_id = 'your_iOS_app_id' %}

{% capture json %}{'name':'event_name', active':true,'joined':{{'maintenant' | date: '%s' }}}{% endcapture %}

https://refusion. vents/event?partner=braze&app_id=\{% si most_recently_used_device.${idfa} == vide %}android_app_id{% else %}iOS_app_id{% endif %}&clé=1cs3p12k&ts='maintenant' | date: '%s' }}&{% if {{most_recently_used_device.${idfa} == blank%}aaid=custom_attribute.${aaid}{% else %}idfa=most_recently_used_device.${idfa{%endif%}&event=event_name&non_app_event=true&data=json | url_param_escape

{% if most_recently_used_device.${idfa} == vide et custom_attribute.${aaid} == vide %}
{% abort_message('No IDFA or AAID available') %}
{% endif %}
```
{% endraw %}

Dans l'URL du webhook ci-dessus, vous devez :
- Utilisez l'API `https://remerge.events/event` pour envoyer vos événements webhook.
- Définit le nom de l'événement. Ce nom apparaîtra dans votre tableau de bord [remerge.io][65].
- Passez l'identifiant d'application unique de votre application pour Android (c'est-à-dire "com.example") et iOS (c'est-à-dire "012345678") pour réfusionner.
- Définissez une clé ; Remerge la fournira.

!\[Refusion du modèle Webhook\]\[67\]

{% alert important %}
Braze ne collecte pas automatiquement l'appareil IDFA/AAID, vous devez donc stocker ces valeurs vous-même. Veuillez noter que vous pouvez exiger le consentement de l'utilisateur pour collecter ces données.
{% endalert %}

#### En-têtes de requête et méthode

Le webhook Remerge nécessite une méthode HTTP et un en-tête de requête.

- **Méthode HTTP**: GET
- **En-têtes de la requête**:
  - **Content-Type**: application/json

!\[Requête Méthode Remerge\]\[68\]

#### Corps de la requête

Vous n'avez pas à définir le corps de la requête pour ce webhook.

## Étape 2 : Aperçu de votre demande

Aperçu du message pour s'assurer que la requête est correctement affichée pour les différents utilisateurs. Nous recommandons la prévisualisation et l'envoi de demandes de test pour les utilisateurs Android et iOS. Si la requête est réussie, l'API répondra avec `HTTP 204`.

{% alert important %}
N'oubliez pas d'enregistrer votre modèle avant de quitter la page! <br>Les modèles de webhook mis à jour peuvent être trouvés dans la liste **Modèles de Webhook enregistrés** lors de la création d'une nouvelle [campagne webhook]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/).
{% endalert %}
[67]: {% image_buster /assets/img_archive/webhook_remerge_preview.png %} [68]: {% image_buster /assets/img_archive/httpmethod_remerge.png %}

[65]: https://www.remerge.io/

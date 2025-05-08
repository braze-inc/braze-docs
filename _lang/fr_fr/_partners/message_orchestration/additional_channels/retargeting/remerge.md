---
nav_title: Remerge
article_title: Remerge
alias: /partners/remerge/
description: "Cet article de référence présente le partenariat entre Braze et Remerge, une application de reciblage à grande échelle, qui vous fournit des outils pour segmenter efficacement les audiences des applications et recibler les utilisateurs."
page_type: partner
search_tag: Partner

---

# Remerge

> [Remerge](https://www.remerge.io/) est un outil de reciblage d'applications à grande échelle, qui vous fournit les outils nécessaires pour segmenter efficacement les audiences d'applications et recibler les utilisateurs.

_Cette intégration est maintenue par Remerge._

## À propos de l'intégration

L'intégration de Braze et Remerge vous permet de développer des campagnes marketing du cycle de vie cross-canal robustes en envoyant les données des utilisateurs à Remerge via des événements webhook afin de recibler les utilisateurs par le biais de leur plateforme mobile de gestion de la requête.

## Conditions préalables

| Condition | Description |
|---|---|
| Compte Remerge | Un compte Remerge est nécessaire pour profiter de ce partenariat. |
| Clé webhook Remerge | Cette clé sera fournie par Remerge. |
| ID de l'application Android | Votre identifiant unique d'application Braze pour Android (tel que "com.example"). |
| ID de l'application iOS | Votre identifiant unique d'application Braze pour iOS (tel que " 012345678 "). |
| Activez la collecte IDFA dans le SDK de Braze | La collecte IDFA est facultative dans le SDK de Braze et désactivée par défaut. | 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Intégration

### Étape 1 : Créez votre modèle de webhook Braze à Braze

Pour créer un modèle de webhook Remerge pour de futures campagnes ou Canvases, naviguez vers la rubrique **Modèles** > **Modèles de webhook** dans la plateforme Braze. 

Si vous souhaitez créer une campagne webhook Remerge ponctuelle ou utiliser un modèle existant, sélectionnez **Webhook** à Braze lors de la création d'une nouvelle campagne.

Dans votre nouveau modèle de webhook, remplissez les champs suivants :
- **Corps de la requête** : Texte brut
- **URL du webhook** :
{% raw %}
```liquid
{% assign event_name = 'your_remerge_event_name' %} 
{% assign android_app_id = 'your_android_app_id' %} 
{% assign iOS_app_id = 'your_iOS_app_id' %}

{% capture json %}{'name':'event_name','active':true,'joined':{{'now' | date: '%s' }}}{% endcapture %}

https://remerge.events/event?partner=braze&app_id=\{% if most_recently_used_device.${idfa} == blank %}android_app_id{% else %}iOS_app_id{% endif %}&key=1cs3p12k&ts='now' | date: '%s' }}&{% if {{most_recently_used_device.${idfa} == blank%}aaid=custom_attribute.${aaid}{% else %}idfa=most_recently_used_device.${idfa{%endif%}&event=event_name&non_app_event=true&data=json | url_param_escape

{% if most_recently_used_device.${idfa} == blank and custom_attribute.${aaid} == blank %}
{% abort_message('No IDFA or AAID available') %}
{% endif %}
```
{% endraw %}

Dans l'URL du webhook, vous devez :
- Utilisez l'API `https://remerge.events/event` pour envoyer vos événements webhook.
- Définissez le nom de l'événement. Ce nom apparaîtra dans votre [remerge.io][65] tableau de bord.
- Transmettez l'identifiant d'application unique de votre application pour Android (tel que "com.example") et iOS (tel que " 012345678 ") à Remerge.
- Définissez une clé ; Remerge vous la fournira.

![L'URL du webhook et l'envoi du message s'affichent dans le générateur de webhooks de Braze.][67]

{% alert important %}
Braze ne collecte pas automatiquement l'IDFA/AAID de l'appareil, vous devez donc enregistrer ces valeurs vous-même. Sachez que vous pouvez avoir besoin du consentement de l'utilisateur pour collecter ces données.
{% endalert %}

#### En-têtes de requête et méthode

Le webhook Remerge nécessite une méthode HTTP et un en-tête de requête.

- **Méthode HTTP**: GET
- **En-têtes de requête**:
  - **Content-Type**: application/json

![Les en-têtes de la requête, la méthode HTTP et l'envoi du message sont affichés dans le générateur de webhooks Braze.][68]

#### Corps de la requête

Vous ne devez pas définir de corps de requête pour ce webhook.

## Étape 2 : Prévisualiser votre requête

Prévisualisez le message pour vous assurer que le message envoyé sera approprié pour les différents utilisateurs. Nous vous recommandons de prévisualiser et d'envoyer des requêtes de test pour les utilisateurs Android et iOS. Si la requête aboutit, l'API répondra par `HTTP 204`.

{% alert important %}
N'oubliez pas d'enregistrer votre modèle avant de quitter la page ! <br>Les modèles de webhook mis à jour se trouvent dans la liste **Modèles de webhook enregistrés** lors de la création d'une nouvelle [campagne webhook.]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/)
{% endalert %}


[65]: https://www.remerge.io/
[66]: https://help.remerge.io/hc/en-us/articles/115003046534-Remerge-Event-Tracking-API
[67]: {% image_buster /assets/img_archive/webhook_remerge_preview.png %}
[68]: {% image_buster /assets/img_archive/httpmethod_remerge.png %}

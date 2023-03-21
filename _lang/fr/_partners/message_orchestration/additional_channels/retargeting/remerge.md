---
nav_title: Remerge
article_title: Remerge
alias: /partners/remerge/
description: "Cet article de référence décrit le partenariat entre Braze et Remerge, une application spécialement conçue pour le reciblage des applications à l’échelle et qui fournit les outils nécessaires pour segmenter efficacement l’audience des applications et recibler les utilisateurs."
page_type: partner
search_tag: Partenaire

---

# Remerge

> [Remerge](https://www.remerge.io/) est spécialement conçu pour le reciblage des applications à l’échelle et vous fournit les outils nécessaires pour segmenter l’audience des applications et recibler les utilisateurs facilement.

L’intégration de Braze et Remerge vous aide à développer des campagnes marketing robustes et cross-canal sur le cycle de vie en envoyant les données des utilisateurs à Remerge par le biais d’événements webhook pour aider à recibler les utilisateurs via leur plateforme mobile côté demande.

## Conditions préalables

| Condition | Description |
|---|---|
| Compte Remerge | Un compte Remerge est requis pour profiter de ce partenariat. |
| Clé de webhook Remerge | Cette clé sera fournie par Remerge. |
| ID d’application Android | Votre identifiant d’application Braze unique pour Android (c.-à-d. « com.exemple »). |
| ID d’application iOS | Votre identifiant d’application Braze unique pour iOS (c.-à-d. « 012345678 »). |
| Activer la collection IDFA dans SDK Braze | La collection IDFA est facultative dans le SDK Braze et désactivée par défaut. | 
{: .reset-td-br-1 .reset-td-br-2}

## Intégration

### Étape 1 : Créer votre modèle de webhook Braze

Pour créer un modèle de webhook Remerge à utiliser dans les campagnes ou les Canvas futurs, accédez à la section **Templates & Media (Modèles et médias)** dans la plateforme Braze. Si vous souhaitez créer une campagne de webhook Remerge unique ou utiliser un modèle existant, sélectionnez **Webhook** dans Braze lors de la création d’une nouvelle campagne.

Dans votre nouveau modèle de webhook, renseignez les champs suivants :
- **Corps de la demande** : Texte brut
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

Dans l’URL du webhook, vous devez :
- Utiliser l’API `https://remerge.events/event` pour envoyer vos événements webhook.
- Définir le nom de l’événement. Ce nom apparaîtra dans votre tableau de bord [remerge.io][65].
- Transmettre votre identifiant d’application unique pour Android (c.-à-d. « com.exemple ») et iOS (c.-à-d. « 012345678 ») à Remerge.
- Définir une clé ; cette clé sera fournie par Remerge.

![URL du webhook et aperçu du message affichés dans le générateur de webhooks de Braze.][67]

{% alert important %}
Braze ne collecte pas automatiquement IDFA/AAID de l’appareil, vous devez donc stocker ces valeurs vous-même. Sachez que vous pouvez avoir besoin du consentement de l’utilisateur pour collecter ces données.
{% endalert %}

#### En-têtes et méthode de la requête

Le webhook Remerge nécessite une méthode HTTP et un en-tête de demande.

- **Méthode HTTP** : GET
- **En-têtes de requête** :
  - **Type de contenu** : application/json

![En-têtes de demande, méthode HTTP et aperçu du message affichés dans le générateur de webhooks de Braze.][68]

#### Corps de la demande

Vous ne devez pas définir un corps de demande pour ce webhook.

## Étape 2 : Prévisualiser votre demande

Prévisualisez le message pour vous assurer que la demande est correctement rendue pour différents utilisateurs. Nous recommandons de prévisualiser et d’envoyer des tests de demandes pour les utilisateurs Android et iOS. Si la demande aboutit, l’API renvoie `HTTP 204`.

{% alert important %}
N’oubliez pas d’enregistrer votre modèle avant de quitter la page ! <br>Des modèles de webhook mis à jour sont disponibles dans la liste **Saved Webhook Templates (Modèles de webhooks enregistrés)** lorsque vous créez une nouvelle [campagne de webhook]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/). 
{% endalert %}

[65]: https://www.remerge.io/
[66]: https://help.remerge.io/hc/en-us/articles/115003046534-Remerge-Event-Tracking-API
[67]: {% image_buster /assets/img_archive/webhook_remerge_preview.png %}
[68]: {% image_buster /assets/img_archive/httpmethod_remerge.png %}

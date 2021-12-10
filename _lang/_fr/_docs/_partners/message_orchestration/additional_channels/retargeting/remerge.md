---
nav_title: Rafraîchir
article_title: Rafraîchir
alias: /fr/partners/refusion/
description: "Cet article décrit le partenariat entre Braze et Remerge, une application conçue pour le repositionnement à grande échelle, vous doter d'outils permettant de segmenter efficacement les audiences d'applications et les utilisateurs de retarget."
page_type: partenaire
search_tag: Partenaire
---

# Rafraîchir

> Remerge est conçu pour vous permettre de repositionner des applications à l'échelle, en vous fournissant des outils qui vous permettront de segmenter efficacement le public des applications et les utilisateurs de retarget.

Développer des campagnes marketing robustes et transversales avec les pouvoirs de Braze et Remerge combinés : construire des segments sur le tableau de bord Braze, puis envoyer via le webhook à Remerge pour retarget les utilisateurs via leur DSP mobile.

# Réseau de redistribution de Remerge

Pour utiliser Remerge, configurez le canal Braze webhook pour connecter Braze avec des actions de repositionnement. Il est important d'avoir un moyen automatique d'activer Braze et le système de redistribution (i.e. Remerge) pour avoir une visibilité de ce que l’autre système fait et s’adapter au message de l’autre. Le repositionnement des annonces est utile si vous avez des utilisateurs qui ont désactivé les notifications push ou des utilisateurs qui n'ont pas ouvert votre application récemment.

Par exemple, un utilisateur non enregistré pourrait recevoir une campagne de push disant « Merci d'avoir installé notre application, inscrivez-vous dès aujourd'hui ! » Une fois que l'utilisateur s'est inscrit après avoir reçu la campagne de push, il recevra un message de suivi adapté dans une annonce retardée telle que « Merci de vous être inscrit ! Voici 10% de réduction sur votre première commande. »

L'une des meilleures façons d'y parvenir est d'utiliser Braze ainsi qu'un partenaire de redistribution spécialisé dans le mobile, tel que Remerge. Vous voulez que le partenaire de rétractation reçoive les informations utilisateur automatisées de Braze à l'aide de webhooks. Vous pourrez tirer parti des capacités de ciblage et de déclenchement de Braze pour envoyer des événements à Remerge, qui pourrait ensuite être utilisé pour définir les définitions de campagnes de redistribution dans remerge.io.

## URL et corps de la requête

Pour ce webhook, toutes les données sont transmises à côté de l'URL HTTP en tant que paramètres de chaîne de requêtes. Il y a trois paramètres à définir:

- Vous devrez définir le nom de l'événement. Ceci est pour définir le nom de l'événement qui apparaîtra dans votre tableau de bord [remerge.io][65]
- Remerge vous demande de passer l'identifiant unique de l'application pour Android (c'est-à-dire "com.example") et iOS (c'est-à-dire "012345678")
- Enfin, vous devez définir une clé. Ceci sera fourni par Remerge

> Braze ne collecte pas automatiquement l'appareil IDFA/AAID, vous devez donc stocker ces valeurs vous-même. Veuillez noter que vous pouvez exiger le consentement de l'utilisateur pour collecter ces données.

Voici un exemple de ce à quoi pourrait ressembler votre URL Webhook :
{% raw %}
```
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
Après avoir défini les paramètres ci-dessus, insérez ce modèle de code Liquid dans le champ URL Webhook et modifiez si nécessaire. Vous n'avez pas à définir de Corps de Requête pour ce webhook. Voici le modèle en Brésil :

!\[Remerge\]\[67\]

> Remerge a utilisé pour offrir plusieurs terminaux selon l'endroit où vos données sont stockées, cependant, ils ont maintenant mis à jour leur documentation avec un seul point de terminaison :

```
https://refusion.events/event
```
Les anciens terminaux sont toujours valides et resteront valides, cependant, Remerge recommande aux clients de passer à ce nouveau point de terminaison pour des raisons de fiabilité.

Vous pouvez trouver plus d'informations sur le point de terminaison API de Remerge's [ici][66].

## En-têtes de requête et méthode

Ce webhook ne nécessite aucun *en-tête de requête*, mais assurez-vous de choisir GET dans le menu déroulant pour la *méthode HTTP*.

!\[Requête Méthode Remerge\]\[68\]

## Aperçu de votre demande

Pour s'assurer que la requête s'affiche correctement pour différents utilisateurs, utilisez l'aperçu du message. Une bonne approche est de prévisualiser le Webhook pour les utilisateurs Android et iOS. Vous pouvez également envoyer des demandes de test à ces utilisateurs. Si la requête a réussi, l'API répond avec `HTTP 204`.
[67]: {% image_buster /assets/img_archive/webhook_remerge_preview.png %} [68]: {% image_buster /assets/img_archive/httpmethod_remerge.png %}

[65]: https://www.remerge.io/
[66]: https://help.remerge.io/hc/en-us/articles/115003046534-Remerge-Event-Tracking-API

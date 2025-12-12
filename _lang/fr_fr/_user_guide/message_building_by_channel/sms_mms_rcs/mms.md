---
nav_title: "MMS"
article_title: À propos de MMS
page_order: 15
description: "Cet article de référence explique ce que sont les messages MMS et les cas d'utilisation générale du canal MMS."
page_type: reference
alias: /about_mms/
channel:
  - MMS
search_rank: 2  
---

# ![cours d'apprentissage de Braze]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/messaging-channels-sms){: style="float:right;width:120px;border:0;" class="noimgborder"} À propos des envois MMS

> Le MMS, également connu sous le nom de Multimedia Message Service, est utilisé pour envoyer des messages contenant des ressources multimédias (JPEG, GIF, PNG) aux téléphones mobiles.<br><br>Comme le SMS, le MMS est un canal d'envoi de messages très urgent qui vous permet de communiquer immédiatement avec vos clients d'une manière que vous ne pouvez pas utiliser avec d'autres canaux. Cependant, le MMS étend les capacités du SMS en vous donnant la possibilité d'ajouter des médias à des SMS qui ne seraient autrement que du texte.

## Cas d'utilisation potentiels

| Cas d'utilisation | Explication |
| --- | --- |
| Promotions | Atteignez les utilisateurs grâce à des campagnes SMS à forte visibilité, mais tirez également parti de l'aspect médiatique des MMS pour attirer les acheteurs avec ce que vous proposez. | 
| Campagnes de réengagement | Réengagez les clients qui ont choisi de recevoir des SMS lorsque tous les autres canaux ne parviennent pas à les faire revenir. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Faites connaissance avec MMS

### Disponibilité des MMS

La plupart des opérateurs américains et canadiens prennent en charge la réception et l'affichage de ressources multimédias sur les téléphones de leurs clients. Pour les opérateurs internationaux, Braze convertit automatiquement les messages MMS envoyés à partir d'un numéro de téléphone américain ou canadien pris en charge, et uniquement vers des destinations qui ne prennent pas en charge les MMS. Pour ces messages, Braze remplacera le média joint par une courte URL ajoutée au corps du message qui renvoie au fichier.

### Groupes d'abonnement

Un [groupe d'abonnement]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_subscription_group/#subscription-group-mms-enablement) est un ensemble de numéros de téléphone d'envoi (codes courts, codes longs et ID d'expéditeur alphanumériques) utilisés pour un type d'envoi de messages spécifique. Votre groupe d'abonnement nécessite un numéro de téléphone activé pour les MMS. Contactez votre gestionnaire de compte Braze pour activer cette fonctionnalité.

### Limites et débit des messages MMS

Les opérateurs imposent leurs propres limites de taille de fichier, qui déterminent en fin de compte le succès des envois de MMS. Ces limites peuvent varier en fonction de la zone géographique et de l'opérateur. Pour plus de sécurité, Braze recommande de ne pas dépasser 600 Ko pour votre ressource multimédia et d'inclure un corps de message. Nous vous recommandons également de procéder à des tests pour confirmer que vos médias peuvent être diffusés par les opérateurs de vos utilisateurs.

Le débit des MMS est d'un segment par seconde par l'intermédiaire d'un code long.

#### Limitation de la taille des fichiers des transporteurs

| Taille du fichier | Traitement des transporteurs |
| --- | --- |
| 300 KB | Tous les opérateurs devraient pouvoir traiter de manière fiable les envois MMS de cette taille. |
| 600 KB | Cette taille est considérée comme la taille maximale standard pour les MMS par la plupart des opérateurs. |
| 1 MB |  La plupart des opérateurs américains et canadiens peuvent traiter des envois MMS de cette taille, bien que cela puisse varier d'un opérateur à l'autre. Certains opérateurs peuvent autoriser des tailles de fichiers plus importantes. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

### MMS entrant

Lorsqu'un utilisateur envoie un message entrant contenant un élément multimédia, Braze expose l'URL de l'élément multimédia dans Currents ainsi que dans Liquid grâce à l'étiquette Liquid. {%raw%}`{{sms.${inbound_media_url}}}`{%endraw%}

### Types de fichiers acceptés

Braze accepte les fichiers JPEG, GIF, PNG et VCF et vous permet de joindre une seule ressource multimédia à votre message MMS.



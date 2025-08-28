---
nav_title: "À propos des MMS"
article_title: À propos des MMS
page_order: 0
description: "Cet article de référence présente les messages MMS et les cas d’utilisation générale du canal MMS."
page_type: reference
alias: /about_mms/
channel:
  - MMS
search_rank: 2  
---

# [![Cours d’apprentissage Braze]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/messaging-channels-sms){: style="float:right;width:120px;border:0;" class="noimgborder"}À propos des messages MMS

> Le MMS (Multimedia Message Service) est un service utilisé pour envoyer des messages contenant des ressources multimédias (JPG, GIF, PNG) à des téléphones portables.<br><br>Comme le SMS, le MMS est un canal de communication d’urgence qui vous permet de communiquer avec les clients de façon immédiate et sans pareille. Cependant, MMS étend les capacités des SMS en permettant aussi d’ajouter des médias à des SMS uniquement textuels.

## Cas d’usage potentiels

| Cas d’utilisation | Explication |
| --- | --- |
| Promotions | Atteignez les utilisateurs avec des campagnes par SMS à haute visibilité, mais profitez également de l’aspect média des MMS pour séduire les acheteurs avec vos offres. | 
| Campagnes de ré-engagement | Ré-engagez les clients qui se sont abonnés pour recevoir des SMS lorsque tous les autres canaux restent sans effets. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Découvrir les MMS

### Disponibilité des MMS

La plupart des opérateurs américains et canadiens prennent en charge la réception et l’affichage de ressources multimédias sur les téléphones de leurs clients. Pour les opérateurs internationaux, Braze convertit automatiquement les messages MMS envoyés depuis un numéro de téléphone américain ou canadien pris en charge, et uniquement vers des destinations ne prenant pas en charge les MMS. Pour ces messages en particulier, Braze remplacera les médias joints par une URL raccourcie, ajoutée au corps du message, qui renvoie au fichier.

### Groupes d’abonnement

Un [groupe d'abonnement]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_subscription_group/#subscription-group-mms-enablement) est un ensemble de numéros de téléphone d'envoi (codes courts, codes longs et ID d'expéditeur alphanumériques) utilisés pour un type d'envoi de messages spécifique. Votre groupe d’abonnement nécessite un numéro de téléphone avec MMS activés. Parlez avec votre gestionnaire de compte Braze de l’activation de cette fonction.

### Débit et limites des messages MMS

Les opérateurs imposent leurs propres limites de taille de fichier, qui déterminent en fin de compte le succès des envois de MMS. Ces limites peuvent varier en fonction de la zone géographique et de l'opérateur. Pour plus de sécurité, Braze recommande de ne pas dépasser 600 Ko pour votre ressource multimédia et d'inclure un corps de message. Nous vous recommandons également de procéder à des tests pour confirmer que vos médias peuvent être diffusés par les opérateurs de vos utilisateurs.

Le débit des MMS est d'un segment par seconde par l'intermédiaire d'un code long.

#### Limitation de la taille des fichiers des transporteurs

| Taille du fichier | Traitement des transporteurs |
| --- | --- |
| 300 KB | Tous les opérateurs devraient pouvoir traiter de manière fiable des envois MMS de cette taille. |
| 600 KB | Cette taille est considérée comme la taille maximale standard pour les MMS par la plupart des opérateurs. |
| 1 MB |  La plupart des opérateurs américains et canadiens peuvent traiter des envois MMS de cette taille, bien que cela puisse varier d'un opérateur à l'autre. Certains opérateurs peuvent autoriser des tailles de fichiers plus importantes. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

### MMS entrant

Lorsqu’un utilisateur envoie un message entrant contenant un média, Braze expose l’URL de cet élément dans Currents et Liquid via l’étiquette Liquid {%raw%}`{{sms.${inbound_media_url}}}`{%endraw%}.

### Types de fichiers acceptés

Braze accepte les fichiers JPEG, GIF, PNG et VCF et vous permet de joindre une seule ressource multimédia à votre message MMS.



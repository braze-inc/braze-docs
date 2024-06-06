---
nav_title: "À propos des MMS"
article_title: À propos des MMS
page_order: 0
description: "Cet article de référence présente les messages MMS et les cas d’utilisation générale du canal MMS."
page_type: reference
channel:
  - MMS
search_rank: 2  
---

# [![Cours d’apprentissage Braze]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/messaging-channels-sms){: style="float:right;width:120px;border:0;" class="noimgborder"}À propos des messages MMS

> Le MMS (Multimedia Message Service) est un service utilisé pour envoyer des messages contenant des ressources multimédias (JPG, GIF, PNG) à des téléphones portables.<br><br>Comme le SMS, le MMS est un canal de messagerie d’urgence qui vous permet de communiquer avec les clients de façon immédiate et sans pareille. Cependant, MMS étend les capacités des SMS en permettant aussi d’ajouter des médias à des SMS uniquement textuels.

## Cas d’usage potentiels

| Cas d’utilisation | Explication |
| --- | --- |
| Promotions | Atteignez les utilisateurs avec des campagnes par SMS à haute visibilité, mais profitez également de l’aspect média des MMS pour séduire les acheteurs avec vos offres. | 
| Campagnes de ré-engagement | Ré-engagez les clients qui se sont abonnés pour recevoir des SMS lorsque tous les autres canaux restent sans effets. |
{: .reset-td-br-1 .reset-td-br-2}

## Découvrir les MMS

### Disponibilité des MMS

La plupart des opérateurs américains et canadiens prennent en charge la réception et l’affichage de ressources multimédias sur les téléphones de leurs clients. Pour les opérateurs internationaux, Braze convertit automatiquement les messages MMS envoyés depuis un numéro de téléphone américain ou canadien pris en charge, et uniquement vers des destinations ne prenant pas en charge les MMS. Pour ces messages en particulier, Braze remplacera les médias joints par une URL raccourcie, ajoutée au corps du message, qui renvoie au fichier.

### Groupes d’abonnement

Un [groupe d’abonnement][1] est une collection de numéros de téléphone émetteurs (c.-à-d. codes courts, codes longs et/ou identifiants alphanumériques d’émetteurs) qui sont utilisés pour envoyer un type spécifique de message. Votre groupe d’abonnement nécessite un numéro de téléphone avec MMS activés. Un processus d’acquisition de liste blanche est nécessaire pour activer votre code court pour les capacités d’envoi MMS. Parlez avec votre gestionnaire de compte Braze de l’activation de cette fonction.

### Débit et limites des messages MMS

Pour les MMS, la limite de message est de 5 Mo (ceci inclut la ressource multimédia et la taille du corps de message). Pour plus de sécurité, Braze recommande de ne pas dépasser 4 Mo pour votre ressource multimédia quand elle est accompagnée d’un corps de message.

Le débit MMS est d’un segment par seconde via un code long.

### MMS entrant

Lorsqu’un utilisateur envoie un message entrant contenant un média, Braze expose l’URL de cet élément dans Currents et Liquid via la balise Liquid. {%raw%}`{{sms.${inbound_media_url}}}`{%endraw%}

### Types de fichiers acceptés

Braze accepte les fichiers JPG, GIF, PNG et VCF et vous permet de joindre une seule ressource multimédia à votre message MMS. Les prochaines itérations de MMS chez Braze permettront aux clients de joindre jusqu’à 10 ressources différentes et la prise en charge d’une plus large gamme de types de fichiers.


[picture]: {% image_buster /assets/img/sms/MMS.png %}
[1]: {{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_subscription_group/#subscription-group-mms-enablement

---
nav_title: "À propos des MMS"
article_title: À propos des MMS
page_order: 0
description: "Cet article de référence couvre ce que sont les messages MMS et les cas d'utilisation générale du canal MMS."
page_type: Référence
channel:
  - MMS
---

# À propos des MMS

!\[MMS\]\[picture\]{: style="float:right; max-width:30%; margin-left:15px; margin-bottom:15px; border:0"}

> Cet article de référence couvre ce que sont les messages MMS et les cas d'utilisation générale du canal MMS. En plus de cet article, vous pouvez également consulter notre cours LAB [SMS & MMS](https://lab.braze.com/messaging-channels-sms).

MMS, également connu sous le nom de Multimedia Message Service, est utilisé pour envoyer des messages contenant des ressources multimédia (JPG, GIF, PNG) aux téléphones mobiles.

J'aime les SMS, MMS est un canal de messagerie à haute urgence qui vous permet de communiquer immédiatement avec les clients d'une manière que vous ne pouvez pas avec un autre canal. Cependant, MMS étend les capacités des SMS en vous donnant la possibilité d'ajouter des médias à des SMS textuels autrement.

## Cas d'utilisation potentiels

| Cas d'utilisation         | Explication                                                                                                                                                               |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Promotions                | Atteignez les utilisateurs avec des campagnes SMS à haute visibilité mais aussi tirez parti de l'aspect média des MMS pour attirer les acheteurs avec ce que vous offrez. |
| Campagnes de réengagement | Reconnectez les clients qui ont choisi de recevoir des SMS quand tous les autres canaux ne les ramènent pas.                                                              |
{: .reset-td-br-1 .reset-td-br-2}

## Apprenez à connaître les MMS

### Disponibilité des MMS

La plupart des transporteurs américains et canadiens appuient la réception et l'affichage d'actifs multimédias sur les téléphones de leurs clients. Pour les transporteurs internationaux, Braze convertira automatiquement les messages MMS envoyés à partir d'un numéro de téléphone américain ou canadien pris en charge et uniquement pour les destinations qui ne prennent pas en charge les MMS. Pour ces messages, Braze remplacera les médias attachés par une URL courte ajoutée au corps du message qui renvoie au fichier.

### Groupes d'abonnement

Un [Groupe d'Abonnement][1] est une collection de numéros de téléphone (c.-à-d. les codes courts, les codes longs et/ou les identifiants alphanumériques de l'expéditeur) qui sont utilisés pour un type spécifique de messagerie. Votre groupe d'abonnement nécessite un numéro de téléphone qui est activé pour les MMS. Un processus de mise en liste blanche est nécessaire pour activer votre code court pour les capacités d'envoi de MMMS. Veuillez parler avec votre gestionnaire de compte Braze au sujet de l'activation de cette fonctionnalité.

### Limites de messages MMS et débit

Pour les MMS, la limite de messages est de 5 Mo (ce qui inclut le contenu multimédia et la taille du corps du message). Pour être plus sûre, Braze recommande de ne pas dépasser 4 Mo pour votre contenu multimédia tout en incluant un corps de message.

Le débit MMS est d'un segment par seconde via un code long.

### MMS entrants

Braze ne prend pas en charge les réponses MMS entrantes.

### Types de fichiers acceptés

Braze accepte les fichiers JPG, GIF, PNG, et VCF et vous permet d'attacher une seule ressource multimédia à votre message MMMS. Les futures itérations de MMS à Braze permettront aux clients d'attacher jusqu'à 10 actifs différents ainsi que de prendre en charge une gamme plus large de types de fichiers.
[picture]: {% image_buster /assets/img/sms/MMS.jpg %}

[1]: {{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_subscription_group/#subscription-group-mms-enablement
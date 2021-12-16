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

!\[MMS\]\[picture\]{: style="float:right; max-width:30%; margin-left:15px; margin-bottom:15px; border:0"} MMS, également connu sous le nom de service de message multimédia, est utilisé pour envoyer des messages contenant des ressources multimédia (jpg, gif, png) aux téléphones mobiles.

## Apprenez à connaître les MMS

- __Disponibilité des MMS :__ La plupart des transporteurs américains/canadiens supportent la réception et l'affichage des actifs multimédia sur les téléphones de leurs clients. Pour les transporteurs internationaux, Braze convertira automatiquement les messages MMS envoyés à partir d'un numéro de téléphone américain ou canadien pris en charge et uniquement pour les destinations qui ne prennent pas en charge les MMS. Pour ces messages, Braze remplacera les médias attachés par une URL courte ajoutée au corps du message qui renvoie au fichier.<br><br>
- __Groupe d'Abonnement :__ A [Groupe d'Abonnement][1] est une collection de numéros de téléphone envoyés (i. . les codes courts, les codes longs et/ou les identifiants alphanumériques de l'expéditeur) qui sont utilisés pour un type spécifique de messagerie. Votre groupe d'abonnement nécessite un numéro de téléphone qui est activé pour les MMS. Un processus de mise en liste blanche est nécessaire pour activer votre code court pour les capacités d'envoi de MMMS. Veuillez parler avec votre gestionnaire de compte Braze au sujet de l'activation de cette fonctionnalité.<br><br>
- __Limites de messages MMS :__ Pour MMS, la limite de message est de 5 Mo (cela inclut la ressource multimédia et la taille du corps du message). Pour être plus sûre, Braze recommande de ne pas dépasser 4 Mo pour votre contenu multimédia tout en incluant un corps de message.<br><br>
- __débit MMS :__ Le débit MMS est de 1 segment par seconde via un code long.<br><br>
- __MMS entrants :__ Braze ne prend pas en charge les réponses MMS entrantes en ce moment<br><br>
- __Types de fichiers acceptés :__ Actuellement, Braze accepte JPG, GIF, PNG, PNG, et les fichiers VCF et vous permet d'attacher un seul contenu multimédia à votre message MMS. Les futures itérations de MMS à Braze permettront aux clients d'attacher jusqu'à 10 actifs différents ainsi que de prendre en charge une gamme plus large de types de fichiers.
[picture]: {% image_buster /assets/img/sms/MMS.jpg %}

[1]: {{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_subscription_group/#subscription-group-mms-enablement
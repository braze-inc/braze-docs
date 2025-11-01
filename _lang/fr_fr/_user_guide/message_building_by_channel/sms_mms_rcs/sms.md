---
nav_title: "SMS"
article_title: À propos du SMS
page_order: 13
description: "Cet article de référence couvre les cas d'utilisation générale du canal SMS et les conditions requises pour mettre en place le SMS."
page_type: reference
alias: /about_sms/
channel:
  - SMS
search_rank: 2
---

# ![cours d'apprentissage de Braze]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/messaging-channels-sms){: style="float:right;width:120px;border:0;" class="noimgborder"} A propos de SMS

> Cet article présente des cas d'utilisation personnalisés, des exigences et des termes à connaître qui faciliteront votre intégration SMS et vous permettront de communiquer de manière efficace et stratégique avec vos clients. \![Message SMS avec le texte "Bienvenue à Braze ! Nous sommes ravis de vous compter parmi nous. Consultez notre documentation pour commencer. https://www.braze.com/docs/ Tapez HELP pour obtenir de l'aide et STOP pour arrêter."]({% image_buster /assets/img/sms/sms_about.png %}){: style="float:right;max-width:30%;margin-left:15px;margin-top:10px;border: 0;"}

<br>
Le SMS, également connu sous le nom de Short Message Service, est utilisé pour envoyer des messages textuels aux téléphones mobiles. Actuellement, plus de 23 milliards de messages texte sont envoyés chaque jour dans le monde, le SMS étant le moyen le plus direct d'atteindre les utilisateurs et les clients. Cette utilisation répandue et cette valeur prouvée ont fait du SMS un outil de marketing par sms efficace pour les entreprises de toutes tailles. 
<br><br>
## Cas d'utilisation potentiels

| Cas d'utilisation | Explication |
|---|---|
| Marketing général | Les messages SMS sont un moyen direct, souple et efficace de communiquer à vos clients les offres à venir, les ventes avantageuses et les produits actuels ou prévus. |
| Rappels | Les messages SMS peuvent être efficaces pour informer les utilisateurs qui ont pris rendez-vous pour un service. Par exemple, l'envoi d'un message SMS rappelant à un client la veille d'un rendez-vous chez le médecin permettra de minimiser les rendez-vous manqués, enregistrant ainsi un gain de temps et d'argent pour vous et vos clients. |
| Messages transactionnels | Les messages SMS sont un moyen efficace d'envoyer des notifications transactionnelles telles que des confirmations de commande et des informations sur l'envoi, en leur fournissant toutes les informations dont ils ont besoin en un seul endroit pratique. Notez qu'il existe des directives légales à respecter lors de l'envoi de messages transactionnels. Si vous n'êtes pas sûr de ces lignes directrices, adressez-vous à votre équipe juridique interne.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Exigences

Avant de commencer à envoyer des SMS, vous avez besoin de certaines choses. Pour en savoir plus, consultez le tableau suivant.

|Exigence | Description | Acquisition |
|---|---|---|
| Un numéro de téléphone dédié (soit un code court, soit un code long) | Un numéro de téléphone dédié fourni exclusivement à une seule marque ou à un seul hébergeur. | Braze se charge d'acquérir ces numéros pour vous. En savoir plus sur les [codes courts et longs]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/short_and_long_codes/).|
| Liste des utilisateurs avec numéros de téléphone | Avant de pouvoir commencer à envoyer des messages, vous devez ajouter des utilisateurs à votre compte. En outre, vous devez connaître la taille approximative de votre audience.  | Les utilisateurs sont initialement ajoutés à Braze via notre backend. Vous devez nous transmettre cette liste afin que nous la téléchargions pour vous. Les numéros de téléphone doivent être formatés sous la forme d'un numéro à 10 chiffres, ainsi que d'un code régional pour le pays. En savoir plus sur les [numéros de téléphone des utilisateurs]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/user_phone_numbers/). |
| [Mots clés et réponses pour les SMS]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/keywords/) | Tous les mots-clés de base doivent se voir attribuer des réponses avant que vous ne puissiez commencer à envoyer des messages. | Vous devez en dresser la liste et les envoyer à votre conseiller ou à votre gestionnaire d'onboarding au cours de votre processus d'onboarding. Visualisez les [modèles de mots-clés SMS.]({{site.baseurl}}/user_guide/message_building_by_channel/sms/phone_numbers/sending_phone_numbers/#short-code-application) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Termes à connaître

Pour obtenir une liste complète des termes, consultez la rubrique [Termes à connaître en matière de]({{site.baseurl}}/sms_terms_to_know/) SMS.


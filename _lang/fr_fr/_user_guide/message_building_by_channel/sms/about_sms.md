---
nav_title: "À propos des SMS"
article_title: À propos des SMS
page_order: 1
description: "Cet article de référence englobe les cas d’utilisation générale du canal SMS et les exigences nécessaires à son bon fonctionnement."
page_type: reference
channel:
  - SMS
search_rank: 2
---

# [![Cours d'apprentissage Braze]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/messaging-channels-sms){: style="float:right;width:120px;border:0;" class="noimgborder"}À propos des SMS

> Le présent article partage certains cas d’utilisation courants à titre de références, des exigences et des conditions à connaître pour favoriser l’intégration de SMS et vous permettre de communiquer de manière efficace et stratégique avec vos clients.![Message SMS avec le texte « Bienvenue dans Braze ! Nous sommes ravis de vous accueillir à bord. » Consultez notre documentation pour commencer. https://www.braze.com/docs/ Envoyez HELP pour obtenir de l'aide et STOP pour arrêter."][image]{: style="float:right;max-width:30%;margin-left:15px;margin-top:10px;border: 0;"}

<br>
Le SMS, pour Short Message Service, est utilisé pour envoyer des messages texte à des téléphones mobiles. Plus de 23 milliards de messages texte sont envoyés chaque jour dans le monde entier, les SMS étant la façon la plus directe d’atteindre les utilisateurs et les clients. L’utilisation répandue et la valeur prouvée des SMS en ont fait un outil de marketing efficace pour les entreprises de toutes tailles. 
<br><br>
## Cas d'utilisation potentiels

| Cas d’utilisation | Explication |
|---|---|
| Marketing général | Les SMS sont un moyen direct, flexible et efficace de communiquer les offres à venir, les ventes favorables et les produits actuels ou prévus à vos clients. |
| Rappels | Les SMS peuvent être efficaces pour prévenir les utilisateurs ayant pris rendez-vous pour un service. Par exemple, l’envoi d’un SMS de rappel la veille d’un rendez-vous médical limite le risque de le manquer et suppose un gain de temps et d’argent à vos clients et à vous-même. |
| Messages transactionnels | Les SMS sont un moyen efficace d’envoyer des notifications transactionnelles, telles que des confirmations de commande et des informations d’expédition, en fournissant toutes les informations nécessaires à un même endroit pratique. Veuillez noter que les directives juridiques doivent être respectées lors de l’envoi de messages transactionnels. En cas de doutes sur ces directives, contactez votre équipe juridique interne.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Conditions

Avant d’envoyer des SMS, vous avez besoin de certaines données. Consultez le tableau suivant pour en savoir plus.

|Condition | Description | Acquisition |
|---|---|---|
| Un numéro de téléphone dédié (code court ou code long) | Un numéro de téléphone dédié fourni exclusivement à une seule marque ou hôte. | Braze se charge d’obtenir ces numéros pour vous. En savoir plus sur les [codes courts et longs]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_setup/short_and_long_codes/).|
| Liste des utilisateurs avec numéros de téléphone | Pour pouvoir envoyer des messages, vous devez ajouter des utilisateurs à votre compte. Vous devez par ailleurs connaître la taille approximative de votre public.  | Les utilisateurs sont initialement ajoutés à Braze via notre backend. Vous devez nous transmettre cette liste pour que nous la téléchargions. Les numéros de téléphone doivent avoir un format de 10 chiffres et inclure un indicatif régional. En savoir plus sur les [numéros de téléphone des utilisateurs]({{site.baseurl}}/user_guide/message_building_by_channel/sms/phone_numbers/user_phone_numbers/). |
| [Mots-clés et réponses SMS]({{site.baseurl}}/user_guide/message_building_by_channel/sms/keywords/) | Pour pouvoir envoyer des messages, tous les mots-clés de base doivent avoir des réponses attribuées | Vous devez les répertorier et les envoyer à votre conseiller Braze ou au gestionnaire d’onboarding lors de votre processus d’onboarding. Voir [modèles de mots-clés SMS]({{site.baseurl}}/user_guide/message_building_by_channel/sms/phone_numbers/sending_phone_numbers/#short-code-application). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Termes à connaître

- **Code court :** Un code à 5 à 6 chiffres, plus court qu’un numéro de téléphone complet. Ce code est utilisé pour traiter et envoyer les SMS.<br><br>
- **Codes longs :** Code à 10 chiffres utilisé pour traiter les SMS. La plupart des numéros de téléphone moyens sont considérés comme des codes longs (e.g 123-456-7891). Ces codes sont utilisés pour traiter et envoyer les SMS.<br><br>
- **Groupe d'abonnement:** Une collection de numéros de téléphone d'envoi (tels que des codes courts, des codes longs et/ou des identifiants d'expéditeur alphanumériques) qui sont utilisés pour un type spécifique de messagerie. Par exemple, si une marque prévoit d’envoyer des messages SMS transactionnels et promotionnels, deux groupes d’abonnement avec des pools distincts de numéros de téléphone émetteurs devront être configurés dans votre tableau de bord de Braze.<br><br>
- **Limites de segment de message et de caractères :** Un segment de message désigne le nombre de segments dans lequel votre message SMS initial sera divisé. Chaque message a une limite de caractères qui, si elle est dépassée, entraîne la division du message en segments. Selon les normes d’encodage employées (UTF-2 ou GSM-7), les limites de caractères varient. Référez-vous à nos [limites de copie de message][2] pour plus d'informations sur la segmentation des messages et les limites de caractères des messages.<br><br>
- **Principaux indicateurs de campagne SMS :** <br>*Envoyé*, *Envoie au transporteur*, *Échec de livraison*, *Livraison confirmée*, *Rejets*, *Désinscription*, et *Aide*. <br>Pour plus d'informations sur ces indicateurs et d'autres indicateurs SMS, reportez-vous à [SMS reporting][1]. Notez que *Envoie au transporteur* est obsolète, mais continuera d'être pris en charge pour les utilisateurs qui l'ont déjà.

<br><br>

Pour obtenir une liste complète des termes, consultez nos [termes à connaître]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_setup/terms/) à propos des SMS.

[picture]: {% image_buster /assets/img/sms/sms_about.png %}
[1]: {{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_campaign_analytics/
[2]: {{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/segments/#things-to-keep-in-mind-as-you-create-your-copy

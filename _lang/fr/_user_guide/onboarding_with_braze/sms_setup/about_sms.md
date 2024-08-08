---
nav_title: "À propos des SMS"
article_title: À propos des SMS
page_order: 0
description: "Cet article de référence présente les cas d’utilisation généraux, les exigences et les termes à connaître sur le canal SMS."
page_type: reference
noindex: true
channel:
  - SMS
  
---

# [![Cours d’apprentissage Braze]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/messaging-channels-sms){: style="float:right;width:120px;border:0;" class="noimgborder"}À propos des SMS

> Le présent article partage certains cas d’utilisation courants à titre de références, des exigences et des conditions à connaître pour favoriser l’intégration de SMS et vous permettre de communiquer de manière efficace et stratégique avec vos clients.![Message SMS avec le texte « Bienvenue dans Braze ! Nous sommes ravis de vous accueillir à bord. » Consultez notre documentation pour commencer. https://www.braze.com/docs/ Envoyez AIDE par SMS pour obtenir de l’aide et ARRÊTER pour arrêter. »][image]{: style="float:right;max-width:30%;margin-left:15px;margin-top:10px;border: 0;"}

<br>
Le SMS, pour Short Message Service, est utilisé pour envoyer des messages texte à des téléphones mobiles. Plus de 23 milliards de messages texte sont envoyés chaque jour dans le monde entier, les SMS étant la façon la plus directe d’atteindre les utilisateurs et les clients. L’utilisation répandue et la valeur prouvée des SMS en ont fait un outil de marketing efficace pour les entreprises de toutes tailles. 
<br><br>

## Cas d’usage potentiels

| Cas d’utilisation | Explication |
|---|---|
| Marketing général | Les SMS sont un moyen direct, flexible et efficace de communiquer les offres à venir, les ventes favorables et les produits actuels ou prévus à vos clients. |
| Rappels | Les SMS peuvent être efficaces pour prévenir les utilisateurs ayant pris rendez-vous pour un service. Par exemple, l’envoi d’un SMS de rappel la veille d’un rendez-vous médical limite le risque de le manquer et suppose un gain de temps et d’argent à vos clients et à vous-même. |
| Messages transactionnels | Les SMS sont un moyen efficace d’envoyer des notifications transactionnelles, telles que des confirmations de commande et des informations d’expédition, en fournissant toutes les informations nécessaires à un même endroit pratique. Veuillez noter que les directives juridiques doivent être respectées lors de l’envoi de messages transactionnels. En cas de doutes sur ces directives, contactez votre équipe juridique interne..|
{: .reset-td-br-1 .reset-td-br-2}

## Conditions

Avant d’envoyer des SMS, vous avez besoin de certaines données. Consultez le tableau suivant pour en savoir plus.

|Condition | Description | Acquisition |
|---|---|---|
| Un numéro de téléphone dédié (code court ou code long) | Un numéro de téléphone dédié fourni exclusivement à une seule marque ou hôte. | Braze se charge d’obtenir ces numéros pour vous. Pour en savoir plus, consultez [Codes courts et longs]({{site.baseurl}}/user_guide/onboarding_with_braze/sms_setup/short_and_long_codes/)..|
| Liste des utilisateurs avec numéros de téléphone | Pour pouvoir envoyer des messages, vous devez ajouter des utilisateurs à votre compte. Vous devez par ailleurs connaître la taille approximative de votre public.  | Les utilisateurs sont initialement ajoutés à Braze via notre backend. Vous devez nous transmettre cette liste pour que nous la téléchargions. Les numéros de téléphone doivent avoir un format de 10 chiffres et inclure un indicatif régional. Pour en savoir plus, consultez [Migration des données utilisateur]({{site.baseurl}}//user_guide/onboarding_with_braze/sms_setup/user_data_migration/). |
| [Mots-clés et réponses SMS]({{site.baseurl}}/user_guide/message_building_by_channel/sms/keywords/) | Pour pouvoir envoyer des messages, tous les mots clés de base doivent avoir des réponses attribuées | Vous devez les répertorier et les envoyer à votre conseiller Braze ou au gestionnaire d’onboarding lors de votre processus d’onboarding. Par exemple, reportez-vous à [Application de code court]({{site.baseurl}}/user_guide/onboarding_with_braze/sms_setup/short_and_long_codes/#short-code-application). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

## Termes à connaître

- **Code court :** Un code à 5 à 6 chiffres, plus court qu’un numéro de téléphone complet. Ce code est utilisé pour traiter et envoyer les SMS.<br><br>
- **Codes longs :** Code à 10 chiffres utilisé pour traiter les SMS. La plupart des numéros de téléphone standard sont considérés des codes longs (par ex. 123-456-7891). Ces codes sont utilisés pour traiter et envoyer les SMS.<br><br>
- **Groupe d’abonnement :** Un groupe d’abonnement est une collection de numéros de téléphone expéditeurs (c.-à-d. codes courts, codes longs et/ou identifiants alphanumériques d’expéditeurs) qui sont utilisés pour envoyer un type spécifique de message. Par exemple, si une marque prévoit d’envoyer des messages SMS transactionnels et promotionnels, deux groupes d’abonnement avec des pools distincts de numéros de téléphone émetteurs devront être configurés dans votre tableau de bord de Braze.<br><br>
- ** Segments de message et limites de caractères :** Un segment de message désigne le nombre de segments dans lequel votre message SMS initial sera divisé. Chaque message a une limite de caractères qui, si elle est dépassée, entraîne la division du message en segments. Selon les normes d’encodage employées (UTF-2 ou GSM-7), les limites de caractères varient. Pour plus d’informations sur les segments de messages et les limites de caractères de message, reportez-vous à [Les bases d’envoi par SMS][2].<br><br>
- **Indicateurs standards de campagne par SMS :** <br>`Sent`, `Sends to Carrier`, `Delivery Failures`, `Confirmed Delivery`, `Rejections`, `Opt-Out` et `Help`. <br>Pour plus d’informations sur ces métriques, reportez-vous à [Rapports sur les SMS][1].

<br><br>

Pour obtenir une liste complète des termes, consultez notre SMS [Conditions à connaître]({{site.baseurl}}/user_guide/onboarding_with_braze/sms_setup/terms/) ou notre [Section SMS]({{site.baseurl}}/user_guide/message_building_by_channel/sms/) pour plus de sujets, comme la création d’une campagne SMS, l’analyse de campagnes SMS et le traitement des mots-clés SMS.

[picture]: {% image_buster /assets/img/sms/sms_about.png %}
[1]: {{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_campaign_analytics/
[2]: {{site.baseurl}}/user_guide/onboarding_with_braze/sms_setup/sms_sending/

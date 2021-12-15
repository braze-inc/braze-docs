---
nav_title: "À propos des SMS"
article_title: À propos des SMS
page_order: 0
description: "Cet article de référence couvre les cas d'utilisation générale du canal SMS et les exigences nécessaires à la mise en place et l'exécution des SMS."
page_type: Référence
channel:
  - SMS
---

# Que sont les messages SMS ?

!\[SMS about\]\[picture\]{: style="float:right;max-width:30%;margin-left:15px;border: 0;"}

Le SMS, également connu sous le nom de Short Message Service, est utilisé pour envoyer des messages texte aux téléphones mobiles. À l'heure actuelle, plus de 23 milliards de SMS sont envoyés chaque jour dans le monde entier, les SMS étant le moyen le plus direct d'atteindre les utilisateurs et les clients. Cette utilisation très répandue et cette valeur éprouvée ont fait des SMS un outil de marketing efficace pour les entreprises de toutes tailles.

Cet article partage certains cas d'utilisation courants à tirer, les exigences, et les conditions pour savoir qui aideront votre intégration par SMS et vous permettront de communiquer efficacement et stratégiquement avec vos clients.

## Cas d'utilisation potentiels

| Cas d'utilisation        | Explication                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Marketing général        | Les messages SMS sont un moyen direct, souple et efficace de communiquer à vos clients les offres à venir, les ventes favorables et les produits actuels ou attendus.                                                                                                                                                                                                                                                                                                          |
| Rappels                  | Les messages SMS peuvent être efficaces pour avertir les utilisateurs qui ont positionné un rendez-vous pour un service. Par exemple, envoyer un SMS rappelant à un client la veille du rendez-vous d'un médecin permettra de minimiser les rendez-vous manqués, économiser à vous et à vos clients du temps et de l'argent.                                                                                                                                                   |
| Messages transactionnels | Les SMS sont un moyen efficace d'envoyer des notifications transactionnelles telles que les confirmations de commande et les informations d'expédition, en leur fournissant toutes les informations dont ils ont besoin dans un seul endroit pratique. Notez qu'il existe des directives légales qui doivent être respectées lors de l'envoi de messages transactionnels. Si vous n'êtes pas sûr de ces lignes directrices, veuillez contacter votre équipe juridique interne. |
{: .reset-td-br-1 .reset-td-br-2}

## Exigences

Avant de commencer à envoyer des SMS, il y a des choses dont vous avez besoin. Consultez le tableau de base ci-dessous pour en savoir plus.

| Exigences                                                                                          | Libellé                                                                                                                                                                       | Acquisition                                                                                                                                                                                                                                                                                                                                                                                        |
| -------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Un numéro de téléphone dédié (code court ou code long)                                             | Un numéro de téléphone dédié fourni exclusivement à une seule marque ou hôte.                                                                                                 | Braze gère l'acquisition de ces numéros pour vous. Vous pouvez en savoir plus sur les [codes courts et longs ici]({{site.baseurl}}/user_guide/message_building_by_channel/sms/phone_numbers/sending_phone_numbers/).                                                                                                                                                                               |
| Liste des utilisateurs avec des numéros de téléphone                                               | Avant de pouvoir commencer à envoyer des messages, vous devez ajouter des utilisateurs à votre compte. De plus, vous devez connaître la taille approximative de votre public. | Les utilisateurs sont initialement ajoutés à Braze à travers notre backend. Vous devez nous transmettre cette liste pour que vous puissiez la télécharger. Les numéros de téléphone doivent être formatés sous la forme d'un numéro à 10 chiffres et d'un indicatif régional. [En savoir plus ici]({{site.baseurl}}/user_guide/message_building_by_channel/sms/phone_numbers/user_phone_numbers/). |
| [Mots clés et réponses SMS]({{site.baseurl}}/user_guide/message_building_by_channel/sms/keywords/) | Tous les mots-clés de base doivent avoir des réponses qui lui sont attribuées avant de pouvoir commencer la messagerie                                                        | Vous devriez les énumérer et les envoyer à votre représentant de Braze ou à votre gestionnaire d’intégration pendant votre processus d’intégration. [Voir les modèles de mots clés SMS ici]({{site.baseurl}}/user_guide/message_building_by_channel/sms/phone_numbers/sending_phone_numbers/#short-code-application).                                                                              |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

## Termes à connaître

- __Code court :__ Un code de 5 à 6 chiffres, c'est plus court qu'un numéro de téléphone complet. Ce code est utilisé pour adresser et envoyer des SMS.<br><br>
- __Codes longs :__ Un code à 10 chiffres utilisé pour traiter les messages SMS. La plupart des numéros de téléphone moyens sont considérés comme des codes longs (par exemple 123-456-7891). Ces codes sont utilisés pour adresser et envoyer des SMS.<br><br>
- __Groupe d'abonnement :__ Un groupe d'abonnement est une collection de numéros de téléphone envoyés (c.-à-d. les codes courts, les codes longs et/ou les identifiants alphanumériques de l'expéditeur) qui sont utilisés pour un type spécifique de messagerie. Par exemple, si une marque a l'intention d'envoyer des messages SMS transactionnels et promotionnels, deux groupes d'abonnement avec des groupes séparés d'envoi de numéros de téléphone devront être configurés dans votre tableau de bord Braze.<br><br>
- __Limites de segment de message et de caractères :__ Un segment de message indique le nombre de segments dans lesquels votre message SMS initial sera divisé. Chaque message a une limite de caractères qui, si elle est dépassée, provoquera la séparation du message en segments. Selon les normes d'encodage que vous utilisez (UTF-2 ou GSM-7), il y a des limites de caractères différentes. Veuillez consulter notre documentation de [Limites de copie de message][2] pour plus d'informations sur la segmentation des messages et les limites de caractères des messages.<br><br>
- __Métriques communes de la campagne SMS :__ <br>`Envoyé`, `Envoyé au Transporteur`, `Échec de livraison`, `Livraison confirmée`, `Rejets`, `Opt-Out`, et `Help`. <br>Pour obtenir des informations sur ces métriques, veuillez consulter la documentation [Analyse de campagne SMS][1].
[picture]: {% image_buster /assets/img/sms/sms_about.jpg %}

[1]: {{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_campaign_analytics/
[2]: {{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/segments/#things-to-keep-in-mind-as-you-create-your-copy

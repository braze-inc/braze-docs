---
nav_title: Consentement & Collecte d'adresse
article_title: Consentement & Collecte d'adresse
page_order: 2
page_type: Référence
description: "Cet article de référence couvre les meilleures pratiques pour la collecte de consentement et d'adresses e-mail utilisateur et définit les différents États abonnés possibles."
channel: Email
---

# Collecte de consentement et d'adresse

## Consentement

Avant d'envoyer vos e-mails initiaux, il est important d'obtenir la permission de vos clients d'abord. C'est une courtoisie commune et fait des merveilles pour vos tarifs ouverts !

### États des abonnés

Il y a trois états d'abonnement à l'e-mail pour un utilisateur : __choisi dans__, __abonné__, et __désabonné__. Pour changer l'état d'abonnement d'un utilisateur, en plus d'utiliser les méthodes décrites ci-dessus, vous pouvez utiliser nos [API REST]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status/).

| État de l'abonné | Libellé                                                                                                                                                                                        |
| ---------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Inscrit          | Ces clients ont cliqué sur le lien dans un e-mail de confirmation et ont choisi de recevoir activement vos messages.                                                                           |
| Inscrit          | Par défaut, vos clients sont abonnés à l'e-mail tant qu'ils ont une adresse e-mail valide stockée sur leur profil. Les clients restent abonnés jusqu'à ce qu'ils se désabonnent ou s'abonnent. |
| Désabonné        | Pour être marqué comme désabonné, un client s'est désabonné explicitement de vos e-mails ou a marqué un e-mail comme spam.                                                                     |
{: .reset-td-br-1 .reset-td-br-2}

## Méthodes de collecte d'adresses

| Méthode                        | Libellé                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| ------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Liste d'adresses achetées      | L'envoi d'e-mails à des listes achetées ou louées est en violation de votre contrat de Braze ! Si vous achetez des courriels, vous envoyez des messages non sollicités et vous risquez de vous retrouver face à des problèmes de délivrabilité.                                                                                                                                                                                                                                                                                                                                                                                      |
| Co-inscription                 | La co-inscription se réfère à une entente entre les entreprises pour collecter des informations d'utilisateur.<br><br>C'est une méthode risquée de collecte. Il permet aux utilisateurs de recevoir des courriels de tiers, parfois sans la connaissance ou la permission du client. Si vous empruntez cette voie, assurez-vous d'avoir des informations claires et la possibilité de vous désabonner au point de collecte.                                                                                                                                                                                              |
| Opt-In Pré-Sélectionné / Forcé | L'option pré-sélectionnée est un mode d'enregistrement par e-mail dans lequel la case d'inscription par e-mail est déjà cochée pour que les abonnés puissent recevoir votre e-mail. En laissant la case cochée, les abonnés choisissent et donnent leur consentement pour recevoir votre courriel.<br><br>Cette méthode a tendance à ennuyer les gens (elle est également illégale pour le courrier envoyé au Canada ou à l'intérieur du Canada). Il se peut que vous vous retrouviez avec une liste d'emails de taille décente, mais vous ne pouvez pas être sûr que ces utilisateurs veulent vos e-mails de marketing. |
| Single Opt-In                  | Le Single opt-in se produit lorsque les abonnés s'inscrivent via un formulaire d'abonnement et sont immédiatement ajoutés à votre liste de messagerie. <br><br>Avec cette méthode, les utilisateurs prennent une seule étape pour s'abonner, comme la saisie de leur adresse e-mail dans un champ de collection ou la sélection d'une boîte dans le cadre d'une transaction.                                                                                                                                                                                                                                             |
| Opt-In confirmé                | Un opt-in confirmé se produit quand un utilisateur coche une case demandant la communication par e-mail et qu'un message de confirmation est envoyé. <br><br>Cette méthode permet aux utilisateurs de choisir le type et la fréquence du contenu améliore l'engagement. Pour vous assurer que vous ne ciblez que les utilisateurs les plus engagés, vous pouvez également suivre la voie de la double confirmation de votre opt-in. Cette approche ajoute une étape supplémentaire dans laquelle l'utilisateur doit cliquer sur un bouton/lien dans l'e-mail de confirmation à placer dans la liste.                     |
{: .reset-td-br-1 .reset-td-br-2}
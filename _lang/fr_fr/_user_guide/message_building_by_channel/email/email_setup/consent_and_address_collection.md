---
nav_title: Consentement et collecte d’adresses
article_title: Consentement et collecte d’adresses
page_order: 6
page_type: reference
description: "Le présent article de référence couvre les bonnes pratiques pour recueillir le consentement et les adresses e-mail d’utilisateur et définit les différents états d’abonnement utilisateurs possibles."
channel: email

---

# Consentement et collecte d’adresses

> Avant d’envoyer vos e-mails initiaux, il est important d’obtenir d’abord l’autorisation de vos clients. C’est une courtoisie commune et fait des merveilles pour vos tarifs ouverts !

## États des abonnés

Il existe trois statuts d’abonnement aux e-mails pour un utilisateur : **abonné**, **inscrit** et **désabonné**. Pour modifier l'état de l'abonnement d'un utilisateur, consultez notre article sur la [modification des abonnements]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#changing-subscriptions) ou utilisez nos [API d'abonnement.]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status/)

| États des abonnés | Description |
|---|---|
| Abonné | Ces clients ont cliqué sur le lien dans un e-mail de confirmation et ont activement choisi de recevoir vos messages. |
| Abonné | Par défaut, les utilisateurs sont abonnés aux e-mails tant qu'ils ont une adresse e-mail valide enregistrée dans leur profil. Les utilisateurs restent abonnés jusqu'à ce qu'ils se désabonnent ou qu'ils choisissent de s'abonner. |
| Désabonné | Pour être marqué comme désabonné, un client est explicitement désinscrit de vos e-mails ou a signalé un e-mail comme spam. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Méthodes de collecte des adresses

En plus d’obtenir l’autorisation de vos utilisateurs avant de leur envoyer des messages, il existe plusieurs méthodes pour recueillir ces adresses e-mail qui peuvent avoir un impact sur votre livrabilité. 

### Liste d’adresses achetées

L’envoi d’e-mails à des listes achetées ou louées est en violation de votre contrat Braze ! Si vous achetez des e-mails, vous envoyez des messages totalement non sollicités et vous mettez à risque de problèmes de livrabilité.

### Co-inscription

La co-inscription désigne une convention entre des entreprises pour recueillir des informations sur l’utilisateur. Il s’agit d’une méthode de collecte à risque. Elle permet aux utilisateurs de recevoir des e-mails de tiers, parfois sans la connaissance ou l’autorisation du client. Si vous allez sur cette route, assurez-vous d’avoir des divulgations claires et la capacité de se désabonner au point de collecte.

### Abonnement pré-sélectionné ou forcé

L’abonnement présélectionné est une méthode d’inscription par e-mail dans laquelle la boîte de message électronique est déjà cochée pour que les abonnés reçoivent votre e-mail. En laissant la case cochée, les abonnés s’engagent et donnent leur consentement pour recevoir votre e-mail. Cette méthode a tendance à irriter (c’est également illégal pour les courriels envoyés vers ou au Canada). Vous pouvez obtenir une liste de courriels de taille convenable, mais vous ne pouvez vraiment pas vous assurer que ces utilisateurs veulent vos e-mails marketing.

### Abonnement unique

Un abonnement unique se produit lorsque les abonnés s’inscrivent via un formulaire d’abonnement et sont immédiatement ajoutés à votre liste de courriels. Avec cette méthode, les utilisateurs utilisent une seule étape pour s’abonner, comme saisir dans leur adresse e-mail dans un champ de collecte ou cocher une case dans le cadre d’une transaction.

### Abonnement confirmé

Un abonnement confirmé se produit lorsqu’un utilisateur coche une case demandant la communication par e-mail, et un message de confirmation est envoyé en retour. Cette méthode permet aux utilisateurs de choisir le type et la fréquence du contenu qui améliorent l’engagement. 

Pour cibler uniquement les utilisateurs les plus engagés, vous pouvez également passer à la méthode d’abonnement à double confirmation. Cette approche ajoute une étape supplémentaire dans laquelle l’utilisateur doit cliquer sur un bouton ou un lien dans l’e-mail de confirmation pour être placé dans la liste d’e-mails. 

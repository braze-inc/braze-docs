---
nav_title: "Consentement et collecte d'adresses"
article_title: "Consentement et collecte d'adresses"
page_order: 6
page_type: reference
description: "Cet article de référence présente les meilleures pratiques pour recueillir le consentement et les adresses e-mail des utilisateurs et définit les différents états possibles de l'utilisateur abonné."
channel: email

---

# Consentement et collecte d'adresses

> Avant d'envoyer vos premiers e-mails, il est important d'obtenir l'autorisation de vos clients. C'est un geste de courtoisie qui fait des merveilles pour vos taux d'ouverture !

## États de l'abonné

Il existe trois états d'abonnement à un e-mail pour un utilisateur : **"opted in**", " **subscribed**" et " **unsubscribed**". Pour modifier l'état de l'abonnement d'un utilisateur, consultez notre article sur la [modification des abonnements]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#changing-subscriptions) ou utilisez nos [API d'abonnement.]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status/)

| État de l'abonné | Description |
|---|---|
| Abonné | Ces clients ont cliqué sur le lien figurant dans un e-mail de confirmation et ont activement accepté de recevoir vos messages. |
| Abonné | Par défaut, les utilisateurs sont abonnés aux e-mails tant qu'ils ont une adresse e-mail valide enregistrée dans leur profil. Les utilisateurs restent abonnés jusqu'à ce qu'ils se désabonnent ou qu'ils choisissent de s'abonner. |
| Désabonné | Pour être marqué comme désabonné, un client doit soit s'être explicitement désabonné de vos e-mails, soit avoir marqué un e-mail comme spam. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Méthodes de collecte d'adresses

Outre l'obtention de l'autorisation de vos utilisateurs avant l'envoi de messages, il existe plusieurs méthodes de collecte de ces adresses e-mail qui peuvent avoir un impact sur votre livrabilité. 

### Listes d'adresses achetées

L'envoi d'e-mails à des listes achetées ou louées constitue une violation de votre contrat avec Braze ! Si vous achetez des e-mails, vous envoyez des messages totalement non sollicités et vous vous exposez à des problèmes de livrabilité.

### Co-enregistrement

L'enregistrement conjoint fait référence à un accord entre des entreprises pour collecter des informations sur les utilisateurs. Il s'agit d'une méthode de collecte risquée. Il permet aux utilisateurs de recevoir des e-mails de tiers, parfois à l'insu du client ou sans son autorisation. Si vous optez pour cette solution, veillez à ce que les informations soient claires et à ce qu'il soit possible de se désinscrire au point de collecte.

### Abonnement présélectionné ou forcé

L'opt-in présélectionné est une méthode d'inscription par e-mail dans laquelle la case d'inscription est déjà cochée pour que les abonnés reçoivent votre e-mail. En laissant la case cochée, les abonnés acceptent de recevoir votre e-mail. Cette méthode a tendance à ennuyer les gens (elle est également illégale pour les courriers envoyés au Canada). Vous pouvez vous retrouver avec une liste d'e-mails de taille convenable, mais vous ne pouvez pas être sûr que ces utilisateurs souhaitent recevoir vos e-mails de marketing.

### Abonnement unique

On parle d'abonnement unique lorsque les utilisateurs s'inscrivent via un formulaire d'abonnement et sont immédiatement ajoutés à votre liste d'e-mails. Avec cette méthode, les utilisateurs ne font qu'une seule démarche pour s'abonner, comme taper leur adresse e-mail dans un champ de collecte ou sélectionner une case dans le cadre d'une transaction.

### Abonnement confirmé

Un abonnement confirmé se produit lorsqu'un utilisateur coche une case demandant une communication par e-mail, et qu'un message de confirmation est envoyé en retour. Cette méthode permet aux utilisateurs de choisir le type et la fréquence du contenu améliore l'engagement. 

Pour confirmer que vous ne ciblez que les utilisateurs les plus engagés, vous pourriez également utiliser la méthode du double abonnement confirmé. Cette approche ajoute une étape supplémentaire au cours de laquelle l'utilisateur doit cliquer sur un bouton ou un lien dans l'e-mail de confirmation pour être inscrit dans la liste d'e-mails. 

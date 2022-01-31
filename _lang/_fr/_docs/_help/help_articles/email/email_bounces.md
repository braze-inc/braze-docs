---
nav_title: Envoyer les Bounces
article_title: Envoyer les Bounces
page_order: 0
page_type: Solution
description: "Cet article d'aide clarifie la différence entre les bounces durs et les bounces doux."
channel: Email
---

# Bounces par e-mail

Que faites-vous lorsque le message de votre campagne de courriel est rebondi à partir des adresses e-mail de vos utilisateurs? Commençons par définir et résoudre les deux types de bounces d'e-mail:
- Bounces durs
- Rebondissements doux

## Bounces durs

Lorsqu'un message de courrier électronique rebondit en dur, cela signifie que l'adresse e-mail est soit invalide soit n'existe pas. Lorsque cela se produit, Braze marque l'adresse e-mail comme non valide mais ne met pas à jour le [statut d'abonnement de l'utilisateur][1]. À ce stade, Braze ne fera aucune tentative pour envoyer des messages à des adresses e-mail marquées comme non valides.

## Rebondissements doux

Les Soft bounces se produisent lorsque l'adresse e-mail de votre destinataire est valide, le message e-mail atteint le serveur de messagerie du destinataire, mais le message a été rejeté pour un problème temporaire. Ces questions temporaires peuvent comprendre quand:
- La boîte de réception de votre destinataire est pleine
- Le message est trop volumineux pour la boîte de réception de votre destinataire
- Un serveur de messagerie a été désactivé

Tandis que les rebonds souples ne sont pas suivis dans vos analyses de campagne, vous pouvez surveiller les rebonds du soft dans le **Message Activity Log** dans la console **Developer** sur le tableau de bord de Braze. Ici, vous pouvez également voir la raison des rebondissements souples et comprendre les éventuels écarts entre les "envoi" et "envoiements" pour vos campagnes de messagerie.

Pour en savoir plus sur la gestion de vos abonnements aux e-mails et de votre campagne, consultez la section [Meilleures pratiques par e-mail][2]!

Vous avez encore besoin d'aide ? Ouvrez un ticket de support []({{site.baseurl}}/braze_support/).

_Dernière mise à jour le 26 janvier 2022_

[1]: {{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions
[2]: {{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices
---
nav_title: E-mails renvoyés
article_title: E-mails renvoyés
page_order: 0
page_type: solution
description: "Cet article d’aide clarifie la différence entre les hard bounces et les soft bounces."
channel: email
---

# E-mails renvoyés

Que faites-vous si un message de votre campagne e-mail est renvoyé par les adresses e-mail de vos utilisateurs ? Commençons par définir ces deux types de renvois d’e-mail : 
- Hard bounces
- Soft bounces  

## Hard bounces

Quand un e-mail fait un hard bounce, l’adresse e-mail n’est pas valide ou n’existe pas. Lorsque cela se produit, Braze marque l’adresse e-mail comme non valide mais ne met pas à jour le [statut d’abonnement][1] de l’utilisateur. À ce stade, Braze ne réessayera pas d’envoyer des messages aux adresses e-mail marquées comme non valides.

## Soft bounces

Les soft bounces se produisent lorsque l’adresse e-mail de votre destinataire est valide ou quand le message e-mail atteint le serveur de messagerie du destinataire, mais le message est rejeté à cause d’un problème temporaire. Ces problèmes temporaires peuvent inclure :
- La boîte de réception de votre destinataire est pleine
- Le message est trop volumineux pour la boîte de réception de votre destinataire  
- Un serveur de messagerie était en panne

Bien que les soft bounces ne soient pas suivies dans l’analyse de campagne, vous pouvez surveiller les primes souples dans le **Journal des activités du message** dans la **Developer Console** sur le tableau de bord de Braze. Ici, vous pouvez également voir la raison du soft bounce et comprendre les éventuelles divergences entre les « envois » et les « livraisons » dans vos campagnes e-mail.

Pour en savoir plus sur la gestion de vos abonnements et campagnes d’e-mails, consultez les [meilleures pratiques pour l’e-mail][2] !

Vous avez toujours besoin d’aide ? Ouvrez un [ticket de support]({{site.baseurl}}/braze_support/).

_Dernière mise à jour le 16 novembre 2022_

[1]: {{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions
[2]: {{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices
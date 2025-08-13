---
nav_title: FAQ
article_title: FAQ sur la poussée
page_order: 80
description: "Cet article aborde certaines des questions les plus fréquemment posées lors de l'implémentation des campagnes de push."
page_type: FAQ
channel:
  - Push
---

# Foire aux questions

> Cet article répond aux questions les plus fréquemment posées sur le canal push.

### Que se passe-t-il lorsque plusieurs utilisateurs se connectent à un même appareil ?

Lorsqu'un utilisateur se déconnecte d'un appareil ou d'un site web, il reste joignable par push jusqu'à ce qu'un autre utilisateur se connecte. À ce moment-là, le jeton push est réattribué au nouvel utilisateur. En effet, chaque appareil ne peut avoir qu'un seul abonnement push actif par appli ou site web.

Lorsqu'un jeton de poussée est réattribué, la modification est reflétée dans le **journal des modifications de la poussée** du profil utilisateur. Vous pouvez le trouver en allant dans l'onglet **Engagement** dans le profil utilisateur.

![Le "Push Changelog" dans la section "Contact Settings".]({% image_buster /assets/img/push_changelog_faq.png %}){: style="max-width:50%;"}

### Pourquoi un utilisateur bénéficiant d'un abonnement n'a-t-il pas de jeton de poussée ?

Cela peut se produire si le jeton push de l'utilisateur a été réattribué à quelqu'un d'autre qui utilisait le même appareil.

1. Accédez au **journal des modifications Push** dans l'onglet **Engagement** du profil de l'utilisateur concerné.
2. Recherchez un message indiquant que le jeton de poussée a été transféré à un autre utilisateur.
3. Copiez le jeton de poussée et collez-le dans la barre de recherche d'utilisateurs. 
4. Si le jeton push existe toujours, vous serez dirigé vers l'utilisateur qui s'est connecté le plus récemment sur l'appareil.

Si vous souhaitez que le jeton de poussée soit réattribué à l'utilisateur d'origine :

1. Demandez à l'utilisateur d'origine de se connecter au profil avec le jeton de poussée manquant.
2. Déclencher un nouvel envoi push. Le jeton sera alors transféré au compte si le mode push est toujours activé au niveau de l'appareil.


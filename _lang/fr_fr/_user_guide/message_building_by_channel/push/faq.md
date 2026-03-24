---
nav_title: FAQ
article_title: FAQ sur les notifications push
page_order: 25
description: "Cet article aborde certaines des questions les plus fréquemment posées lors de la mise en place de campagnes de notifications push."
page_type: FAQ
channel:
  - Push
---

# Foire aux questions

> Cet article répond aux questions les plus fréquemment posées sur le canal push.

### Que se passe-t-il lorsque plusieurs utilisateurs se connectent à un même appareil ?

Lorsqu'un utilisateur se déconnecte d'un appareil ou d'un site web, il reste joignable par notification push jusqu'à ce qu'un autre utilisateur se connecte. À ce moment-là, le jeton de notification push est réattribué au nouvel utilisateur. En effet, chaque appareil ne peut avoir qu'un seul abonnement push actif par application ou site web.

Lorsqu'un jeton de notification push est réattribué, la modification est reflétée dans le **journal des modifications push** du profil utilisateur. Vous pouvez le consulter en accédant à l'onglet **Engagement** du profil utilisateur.

![La section « Journal des modifications push » dans la section « Paramètres de contact ».]({% image_buster /assets/img/push_changelog_faq.png %}){: style="max-width:50%;"}

### Lorsque j'envoie un push de test, est-il envoyé à tous mes appareils ?

Oui. Le push de test est envoyé à chaque appareil compatible push associé au profil utilisateur sélectionné. Si vous avez plusieurs téléphones ou tablettes connectés avec le même utilisateur, chaque appareil disposant d'un jeton de notification push valide reçoit la notification.

Pour envoyer le push de test à un seul appareil, vous pouvez supprimer les jetons de notification push des autres appareils depuis le profil utilisateur avant de tester. Sinon, si vous envoyez via l'[endpoint `/messages/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/), définissez `send_to_most_recent_device_only` sur `true` dans l'objet `apple_push` ou `android_push` afin que seul l'appareil le plus récemment actif reçoive la notification push.

### Que signifie « Erreur lors de l'envoi de la notification push en raison d'un PAYLOAD non valide » ?

Ce message indique que les APN ont rejeté la demande push en raison d'un PAYLOAD non valide (par exemple, un PAYLOAD vide ou trop volumineux).

Pour plus de détails et connaître les étapes suivantes, consultez la section [Messages d'erreur courants liés aux notifications push]({{site.baseurl}}/user_guide/message_building_by_channel/push/push_error_codes/).

### Pourquoi un utilisateur ayant accepté les notifications n'a-t-il pas de jeton de notification push ?

Cela peut se produire si le jeton de notification push de l'utilisateur a été réattribué à quelqu'un d'autre qui utilisait le même appareil.

1. Accédez au **journal des modifications push** dans l'onglet **Engagement** du profil de l'utilisateur concerné.
2. Recherchez un message indiquant que le jeton de notification push a été transféré à un autre utilisateur.
3. Copiez le jeton de notification push et collez-le dans la barre de recherche d'utilisateurs. 
4. Si le jeton de notification push existe toujours, vous serez redirigé vers l'utilisateur qui s'est connecté le plus récemment sur l'appareil.

Si vous souhaitez que le jeton de notification push soit réattribué à l'utilisateur d'origine :

1. Demandez à l'utilisateur d'origine de se connecter au profil avec le jeton de notification push manquant.
2. Déclenchez un nouvel envoi push. Le jeton sera alors transféré vers le compte si les notifications push sont toujours activées au niveau de l'appareil.

### Quelle est la différence entre « Envoyer en production » et « Envoyer en développement » pour les certificats push iOS ?

Lors de l'ajout d'un certificat Apple Push dans Braze, les options **Envoyer en production** et **Envoyer en développement** déterminent quelle passerelle APN (Apple Push Notification service) Braze utilise pour envoyer les notifications push :

- **Envoyer en développement :** Sélectionnez cette option si l'application a été compilée en mode développement dans Xcode et signée avec un profil de provisionnement de développement. Les notifications push sont acheminées via la passerelle de développement (sandbox) d'Apple.
- **Envoyer en production :** Sélectionnez cette option si l'application est distribuée via TestFlight d'Apple, l'App Store ou la distribution d'entreprise. Les notifications push sont acheminées via la passerelle de production d'Apple.

Si la mauvaise option est sélectionnée, les notifications push échouent silencieusement car le type de jeton de notification push ne correspond pas à la passerelle. En règle générale, les applications distribuées via TestFlight ou l'App Store doivent utiliser **Envoyer en production**.
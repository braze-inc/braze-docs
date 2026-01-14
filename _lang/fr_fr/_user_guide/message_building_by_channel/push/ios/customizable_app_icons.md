---
nav_title: "Fonctionnalité d'icône d'application personnalisée (iOS)."
article_title: "Fonctionnalité de l'icône de l'application personnalisée"
page_order: 7
page_type: reference
description: "Cet article de référence couvre la mise à jour iOS 10.3 sur l'icône d'application personnalisable."
platform: iOS
channel:
  - push

---

# Fonctionnalité d'icône d'application personnalisée (iOS 10.3) 

> Avec iOS 10.3, Apple a introduit la possibilité de changer l'icône de l'écran d'accueil d'une application sans avoir à mettre à jour l'application à partir de l'App Store. Le développeur peut désormais permettre à l'utilisateur de modifier l'icône de l'écran d'accueil à l'intérieur de son application. Apple exige que toutes les images des icônes de l'application que le développeur souhaite mettre à la disposition de l'utilisateur soient incluses dans le binaire soumis à Apple pour examen lors de la publication de l'application sur l'Apple App Store.

Pour informer vos utilisateurs de cette fonctionnalité, il est possible d'envoyer un message in-app ou une notification push via Braze à l'utilisateur pour lui expliquer cette fonctionnalité ou lui demander s'il souhaite changer d'icône. Le développeur n'aurait qu'à créer un lien profond dans l'application où l'invite native d'iOS peut être affichée pour effectuer le changement d'icône. Ces conseils sont similaires à ceux que nous donnons aujourd'hui pour la mise en place d'une amorce de notification push pour les APN.

En outre, cet envoi de messages peut tirer pleinement parti de la segmentation pour rendre le message très contextuel pour l'utilisateur. Vous pouvez également utiliser le test A/B des messages pour voir quel envoi a le plus d'impact sur le résultat souhaité.

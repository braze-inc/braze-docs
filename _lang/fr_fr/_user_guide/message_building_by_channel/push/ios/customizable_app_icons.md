---
nav_title: "Fonctionnalité Icône d’application personnalisée (iOS)"
article_title: Fonctionnalité Icône d’application personnalisée
page_order: 7
page_type: reference
description: "Cet article de référence couvre la mise à jour à iOS 10.3 qui couvre l’Icône d’application personnalisée."
platform: iOS
channel:
  - push

---

# Fonctionnalité d’icône d’application personnalisée (iOS 10.3) 

> Avec iOS 10.3, Apple a introduit la possibilité de modifier l’icône de l’écran d’accueil d’une application sans avoir à mettre à jour l’application depuis l’App Store d’Apple. Le développeur peut maintenant permettre à l’utilisateur de modifier l’icône de l’écran d’accueil à l’intérieur de son application. Apple exige que toutes les images des icônes d’application que le développeur souhaite mettre à la disposition de l’utilisateur soient incluses dans le binaire soumis à Apple pour examen lors de la publication de l’application sur l’App Store d’Apple.

Pour informer vos utilisateurs de cette fonctionnalité, il est possible d’envoyer un message in-app ou une notification push via Braze à l’utilisateur expliquant cette fonctionnalité ou demandant à l’utilisateur s’il souhaite changer son icône. Le développeur doit juste créer un lien profond dans l’application où l’invite iOS native peut s’afficher pour modifier l’icône. Ceci est similaire aux mêmes conseils fournis autour de la mise en place d’une amorce de notification push pour les APN aujourd’hui.

De plus, cet envoi de messages peut tirer pleinement parti de la segmentation afin de rendre le message hautement contextuel pour un utilisateur. Vous pouvez également utiliser le test A/B des messages pour déterminer quel envoi de messages a le plus d'impact sur le résultat souhaité.

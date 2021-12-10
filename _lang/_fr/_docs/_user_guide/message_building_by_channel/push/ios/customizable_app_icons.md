---
nav_title: "Fonctionnalité de l'icône de l'application personnalisée (iOS)"
article_title: Fonctionnalité de l'icône de l'application personnalisée
page_order: 7
page_type: Référence
description: "Cet article de référence couvre la mise à jour iOS 10.3 sur l'icône Application personnalisable."
platform: iOS
channel:
  - Pousser
---

# Fonctionnalité de l'icône d'application personnalisable iOS 10.3

Avec iOS 10.3, Apple a introduit la possibilité de changer l'icône de l'écran d'accueil d'une application sans avoir à mettre à jour l'application depuis l'Apple App Store. Le développeur peut maintenant permettre à l'utilisateur de changer l'icône de l'écran d'accueil dans son application. Apple exige que toutes les images d'icônes de l'application que le développeur veut mettre à la disposition de l'utilisateur pour être inclus dans le binaire qui est soumis à Apple pour examen lors de la publication de l'application sur l'App Store d'Apple.

Pour avertir vos utilisateurs de cette fonctionnalité, il est possible d'envoyer un message In-App ou une notification push via Braze à l'utilisateur expliquant cette fonctionnalité ou demandant à l'utilisateur s'il souhaite modifier son icône. Le développeur aurait seulement besoin de créer un lien profond vers l'application où l'invite native iOS peut être montrée pour faire le changement d'icône. Ceci est similaire à la même orientation que celle que nous fournissons pour mettre en place un Primeur de Notification Push pour les APN aujourd'hui.

De plus, cette messagerie peut tirer pleinement parti de la capacité de segmentation de Braze pour rendre le message très contextuel à un utilisateur. Vous pouvez également tirer parti des tests A/B de Braze pour voir quelles messages ont le plus d'impact sur le résultat souhaité.

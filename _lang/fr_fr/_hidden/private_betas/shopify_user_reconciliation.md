---
nav_title: Rapprochement des utilisateurs de Shopify
article_title: Rapprochement des utilisateurs de Shopify
permalink: "/shopify_user_reconciliation/"
description: "Cet article de référence explique comment concilier l'identifiant de l'appareil de votre utilisateur et les informations personnelles lorsqu'ils atteignent le flux de paiement."
hidden: true
---

# Réconciliation des utilisateurs Shopify en dehors du flux de paiement 

> L’intégration Shopify rapproche l’ID de l’appareil de votre utilisateur et les informations personnelles lorsqu’il atteint le flux de paiement et y effectue n’importe quel événement de webhook Shopify.

{% alert note %}
Cette fonctionnalité est actuellement en version bêta. Si vous souhaitez participer à cet essai bêta, contactez votre gestionnaire du succès des clients ou votre gestionnaire de compte.
{% endalert %}

Pour soutenir la réconciliation des utilisateurs via votre flux d'inscription et de connexion Shopify, nous pouvons implémenter automatiquement une fonction JavaScript dans votre boutique Shopify en dehors du flux de paiement. Braze implémentera automatiquement une fonction partout où nous voyons un formulaire avec un `type="email"` sur la boutique Shopify, comme dans l'exemple ci-dessous.

![1]{:style="max-width:60%;"}

Une fois cette fonction appelée, l'utilisateur anonyme sur le web devient associé à l'adresse e-mail fournie. À l'avenir, tous les événements Shopify qui font référence à l'un des identifiants que nous utilisons (par exemple, l'ID client Shopify, l'adresse e-mail, le numéro de téléphone) seront attribués au même utilisateur Braze s'il y a une correspondance.

## Considérations

{% alert important %}
Braze ne reconnaît pas nécessairement tous les formulaires contenant `type="email"` sur le site Shopify d'un client. Cela signifie qu'il y a une possibilité que la fonction puisse manquer certains champs de saisie qui devraient être utilisés pour la réconciliation de l'utilisateur ou récupérer des champs incorrects qui définiraient la mauvaise adresse e-mail (par exemple, le formulaire de recommandation) sur le profil de l'utilisateur.
{% endalert %}

Nous vous encourageons à explorer tous les formulaires pris en charge sur le site Shopify et à évaluer comment cette solution bêta peut répondre efficacement à vos besoins. En choisissant d'utiliser cette fonctionnalité bêta, vous comprenez qu'il peut y avoir un comportement inattendu en apportant des modifications manuelles à vos formulaires Shopify.

[1]: {% image_buster /assets/img/shopify_type_email.png %}

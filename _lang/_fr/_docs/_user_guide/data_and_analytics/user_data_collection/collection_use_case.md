---
nav_title: Caisse d'utilisation de la collection
article_title: Caisse d'utilisation de la collection
page_order: 3
page_type: Référence
description: "Cet article de référence couvre un exemple de cas d'utilisation de la collecte de données utilisateur — comment une application de partage de courses peut décider quelles données utilisateur collecter."
---

# Cas d'utilisation de l'application Taxi ou partage de taxi

> Cet article de référence couvre un exemple de cas d'utilisation de la collecte de données utilisateur — comment une application de partage de courses peut décider quelles données utilisateur collecter.


Dans ce cas, envisageons une application Taxi/Ride-Sharing (comme Hailo, Uber, Lyft, etc.) pour décider quelles données utilisateur collecter. Les questions et le processus de brainstorming ci-dessous sont un excellent modèle pour les équipes de marketing et de développement à suivre. À la fin de cet exercice, les deux équipes devraient avoir une bonne compréhension de ce que les événements et attributs personnalisés ont un sens à collecter afin de contribuer à atteindre leur objectif.

## Question de cas #1 : Quel est le but ?

Leur objectif est simple dans la mesure où ils veulent que les utilisateurs dénigrent les trajets en taxi via leur application.

## Question de cas #2 : Quelles sont les étapes intermédiaires sur la voie menant à cet objectif à partir de l'installation de l'application ?

1. Ils ont besoin que les utilisateurs commencent le processus d'inscription et remplissent leurs informations personnelles.
2. Ils ont besoin d’utilisateurs pour terminer & vérifier le processus d’inscription en entrant un code dans l’application qu’ils reçoivent par SMS.
3. Ils doivent essayer de haïr un taxi.
4. Pour accabler un taxi, il doit être disponible lors de sa recherche.

Les actions ci-dessus pourraient alors être marquées comme les événements personnalisés suivants :

- Début de l'inscription
- Inscription terminée
- Taxi Hails Réussi
- Chaussures de Taxi échouées

Après avoir implémenté les événements, vous pouvez maintenant exécuter les campagnes suivantes :

1. Envoyer un message aux utilisateurs qui débutent l'inscription, mais qui n'ont pas terminé l'inscription dans un certain laps de temps.
2. Envoyez des messages de félicitations aux utilisateurs qui complètent l'inscription.
3. Envoyez des excuses et des crédits promotionnels aux utilisateurs qui ont échoué dans la grêle de taxi, qui n'ont pas été suivis par une grêle de taxi réussie dans un certain temps.
4. Envoyez des promotions aux utilisateurs avec beaucoup de Taxi Hails qui ont réussi à les remercier pour leur loyauté.
5. Nombreux, beaucoup plus.

## Question de cas #3 : Quelles autres informations souhaiterions-nous savoir sur nos utilisateurs qui informeront notre message ?

- Qu'ils disposent ou non de crédits promotionnels?
- La note moyenne qu'ils donnent à leurs chauffeurs?
- Codes promo uniques pour l'utilisateur ?

Les caractéristiques ci-dessus pourraient alors être marquées comme les attributs personnalisés suivants :

- Solde de crédit promotionnel (Type décimal)
- Notation moyenne des chauffeurs (type entier)
- Code promo unique (Type de chaîne de caractères)

Ajouter ces attributs vous permettrait d'envoyer des campagnes aux utilisateurs comme :

1. Rappelant aux utilisateurs qui n'ont pas utilisé l'application en 7 jours qui ont encore du crédit promotionnel sur leur compte qu'il est là et qu'ils devraient revenir sur l'application et l'utiliser !
2. Utilisez nos [modèles de messages et fonctionnalités de personnalisation][13] pour faire glisser l'attribut de code promo unique vers la messagerie destinée aux utilisateurs.


{% alert important %}
Braze va bannir ou bloquer les utilisateurs (« utilisateurs factices ») avec plus de 5 millions de sessions et ne plus ingérer leurs événements SDK car ils sont généralement le résultat d'une désintégration. Si vous trouvez que cela s'est produit pour un utilisateur légitime, veuillez contacter votre responsable de compte Braze.
{% endalert %}

[13]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/overview/#personalized-messaging

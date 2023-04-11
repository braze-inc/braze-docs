---
nav_title: Cas d’utilisation de collecte de données
article_title: Cas d’utilisation de collecte de données
page_order: 3
page_type: reference
description: "Cet article de référence couvre un exemple d’utilisation de collecte de données utilisateur, la manière dont une application de partage de trajets peut décider de ce que les données utilisateur peuvent collecter."

---

# Cas d’utilisation :application de taxi/partage de trajets

> Cet article de référence couvre un exemple d’utilisation de collecte de données utilisateur, la manière dont une application de partage de trajets peut décider de ce que les données utilisateur peuvent collecter.

Dans cet exemple, prenons une application de taxi/partage de trajets (comme Hailo, Uber, Lyft, etc.) qui décide quelles données utilisateur collecter. Le brainstorming et les questions suivantes sont un excellent modèle à suivre pour les équipes de marketing et de développement. À la fin de cet exercice, les deux équipes doivent avoir une solide compréhension des événements et attributs personnalisés qu’elles devraient collecter pour essayer d’atteindre leur objectif.

## Question n° 1 : Quel est l’objectif ?

Leur objectif est simple : ils veulent que les utilisateurs fassent des trajets en taxi via leur application.

## Question n° 2 : Quelles sont les étapes intermédiaires sur la voie de l’installation de l’application ?

1. Il faut que les utilisateurs commencent le processus d’inscription et donnent leurs informations personnelles.
2. Il faut que les utilisateurs confirment leur inscription en entrant un code reçu via SMS dans l’application.
3. Ils doivent essayer de commander un taxi.
4. Pour commander un taxi, il faut des taxis disponibles au moment de leur recherche.

Ces actions peuvent ensuite être des tags pour les événements personnalisés suivants :

- Inscription commencée
- Inscription terminée
- Appels de taxis réussis
- Appels de taxis échoués

Une fois que les événements ont été définis, vous pouvez maintenant exécuter les campagnes suivantes :

1. Envoyer des messages aux utilisateurs qui ont commencé l’enregistrement, mais n’ont pas terminé l’enregistrement dans un certain délai.
2. Envoyer des messages de félicitations aux utilisateurs qui se sont abonnés.
3. Envoyer des excuses et des remises aux utilisateurs qui n’ont pas réussi à avoir un taxi pour un trajet.
4. Envoyer des remises aux utilisateurs qui ont pris de nombreux taxis pour les remercier leur fidélité.
5. Et beaucoup, beaucoup d’autres.

## Question n° 3 : Quelles autres informations pourrions-nous connaître sur nos utilisateurs qui renseigneront nos envois de messages ?

- Ont-ils ou non un crédit promotionnel ?
- La note moyenne qu’ils donnent à leurs chauffeurs ?
- Codes promotionnels uniques pour l’utilisateur ?

Ces caractéristiques peuvent ensuite être des tags pour les attributs personnalisés suivants :

- Solde de crédit promotionnel (type décimal)
- Note moyenne du chauffeur (Type Entier)
- Code promotionnel unique (Type String)

L’ajout de ces attributs vous permettrait d’envoyer des campagnes aux utilisateurs pour :

1. Rappeler aux utilisateurs qui n’ont pas utilisé l’application depuis 7 jours que leur compte est éligible pour une remise et qu’ils devraient revenir sur l’appli pour en profiter !
2. Utilisez nos [fonctionnalités de personnalisation et de modélisation de messages][13] pour faire glisser l’attribut de Promotion Code unique dans la communication envoyée aux utilisateurs.


{% alert important %}
Braze interdit ou bloque les utilisateurs avec plus de 5 millions de sessions (« utilisateurs factices ») et cesse d’ingérer leurs événements SDK, car ces utilisateurs sont généralement le résultat d’une mauvaise intégration. Si vous constatez que cela s’est produit pour un utilisateur légitime, contactez votre gestionnaire de compte Braze.
{% endalert %}

[13]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/overview/#personalized-messaging

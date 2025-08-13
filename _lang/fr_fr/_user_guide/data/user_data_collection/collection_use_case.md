---
nav_title: Cas d’utilisation de collecte de données
article_title: Cas d’utilisation de collecte de données
page_order: 3
page_type: reference
description: "Cet article de référence couvre un cas d'utilisation de collecte de données utilisateur sur la façon dont une application de covoiturage pourrait décider des données utilisateur à collecter."

---

# Cas d’utilisation de collecte de données

> Cet article couvre un cas d'utilisation de collecte de données utilisateur sur la façon dont une application de covoiturage pourrait décider des données utilisateur à collecter.

Imaginons qu'une application de taxi ou de covoiturage, appelée StyleRyde, veuille décider des données utilisateur à collecter. Les questions et le processus de réflexion qui suivent constituent un excellent modèle à suivre pour leurs équipes de marketing et de développement. À la fin de cet exercice, les deux équipes devraient avoir une bonne compréhension des événements et attributs personnalisés qu'il est judicieux de collecter pour atteindre leur objectif.

## Question de cas 1 : Quel est l’objectif ?

L'objectif de StyleRyde est simple : il s'agit de permettre aux utilisateurs de héler des courses de taxi par le biais de son application.

## Question 2 : Quelles sont les étapes à suivre pour atteindre cet objectif après l'installation de l'application ?

1. StyleRyde demande aux utilisateurs de commencer le processus d'enregistrement et de remplir leurs informations personnelles.
2. StyleRyde a besoin que les utilisateurs complètent et vérifient le processus d'enregistrement en saisissant un code dans l'application qu'ils reçoivent par SMS.
3. StyleRyde demande aux utilisateurs de tenter de héler un taxi.
4. StyleRyde doit être disponible lorsque les utilisateurs hèlent un taxi.

Ces actions peuvent ensuite être des balises pour les événements personnalisés suivants :

- Inscription commencée
- Inscription terminée
- Appels de taxis réussis
- Appels de taxis échoués

Après avoir mis en œuvre les événements, StyleRyde peut mener des campagnes, notamment les suivantes :

1. Envoyez un message aux utilisateurs qui ont commencé l'inscription, mais qui n'ont pas terminé l'inscription dans un certain délai.
2. Envoyez des messages de félicitations aux utilisateurs qui ont terminé l'inscription.
3. Envoyez des excuses et un crédit promotionnel aux utilisateurs qui ont eu des tentatives de taxi infructueuses, qui n'ont pas été suivies par une tentative de taxi réussie dans un certain laps de temps.
4. Envoyer des remises aux utilisateurs qui ont pris de nombreux taxis pour les remercier leur fidélité.

## Question pratique 3 : Quelles autres informations sur les utilisateurs pourrions-nous collecter et utiliser pour enrichir nos messages ?

- Les utilisateurs disposent-ils d'un crédit promotionnel ?
- La note moyenne que les utilisateurs attribuent à leurs conducteurs ?
- Des codes promo uniques pour les utilisateurs ?

Ces caractéristiques peuvent ensuite être des balises  pour les attributs personnalisés suivants :

- Solde de crédit promotionnel (type décimal)
- Note moyenne du chauffeur (Type Entier)
- Code promotionnel unique (Type String)

Ces attributs vous permettent d'envoyer des campagnes à des utilisateurs tels que :

1. Rappeler aux utilisateurs qui n'ont pas utilisé l'application depuis sept jours et qui disposent d'un crédit promotionnel sur leur compte de revenir sur l'application et d'utiliser ce crédit.
2. En utilisant nos modèles de message et [les fonctionnalités de personnalisation]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/overview/#personalized-messaging) pour glisser l'attribut de code de promotion unique dans les messages destinés aux utilisateurs.

{% alert important %}
Braze bannira ou bloquera les utilisateurs ("utilisateurs fictifs") ayant plus de 5 000 000 de sessions et n'ingérera plus leurs événements SDK car ils sont généralement le résultat d'une mauvaise intégration. Si vous constatez que cela s’est produit pour un utilisateur légitime, contactez votre gestionnaire de compte Braze.
{% endalert %}


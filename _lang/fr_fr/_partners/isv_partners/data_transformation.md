---
nav_title: Transformation des données
hidden: true
---

# Transformation des données Braze

> Braze [Data Transformation]({{site.baseurl}}/data_transformation/) peut ingérer un webhook depuis une plateforme partenaire et permettre à un client de définir un mappage pour convertir la charge utile de ce webhook en données utilisateur souhaitées, telles que les attributs, les événements ou les achats sur les profils utilisateur de Braze.

## À quoi ressemblerait une intégration basée sur la transformation des données

Une intégration partenaire basée sur la fonctionnalité de transformation des données peut être un modèle de code de transformation partagé avec les clients via une documentation publique.

Pour les clients mutuels, cela ressemblerait à ceci :

1. Ils se connectent à votre plateforme et configurent des webhooks.
2. Ils collaborent avec l’équipe Braze pour accéder à Braze Data Transformation et créer une nouvelle transformation dans leur tableau de bord Braze.
3. L'URL générée par la transformation est copiée.
4. De retour dans Braze, ils envoient un webhook de test à l'URL de transformation copiée.
5. Dans Braze, ils copient et collent le modèle de code de transformation.
6. Ils activent la transformation.
7. Lorsque cette option est activée, ils peuvent vérifier via l'outil de recherche d'utilisateurs Braze que le profil utilisateur est mis à jour en fonction du webhook et modifier le code de transformation comme ils le souhaitent.

{% alert tip %}
Il est recommandé de créer une transformation par type de webhook envoyé à Braze lors de la création d'exemples de code de transformation.
{% endalert %}

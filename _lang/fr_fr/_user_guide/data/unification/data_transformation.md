---
nav_title: Transformation des données
article_title: Transformation des données
page_order: 0.3
layout: dev_guide
guide_top_header: "Transformation des données"
guide_top_text: "Braze Data Transformation vous permet de créer et de gérer des intégrations webhook pour automatiser le flux de données depuis des plateformes externes vers Braze. Ces données d'utilisateur nouvellement intégrées peuvent ensuite alimenter des cas d'utilisation marketing encore plus sophistiqués. Braze Data Transformation peut accélérer l'intégration de vos données, même si vous n'avez que très peu d'expérience en matière de codage, et peut aider à remplacer la dépendance de votre équipe à l'égard des appels d'API manuels, des outils d'intégration third-party, ou même des plateformes de données client."
page_type: landing
description: "Cette page d'atterrissage abrite des articles sur la transformation des données de Braze, notamment sur la façon de créer une transformation des données et sur les cas d'utilisation."
alias: /data_transformation/

guide_featured_title: "Articles de section"
guide_featured_list:
  - name: Créer une transformation
    link: /docs/user_guide/data/unification/data_transformation/creating_a_transformation/
    image: /assets/img/braze_icons/flip-forward.svg
  - name: "Cas d'utilisation"
    link: /docs/user_guide/data/unification/data_transformation/use_cases/
    image: /assets/img/braze_icons/users-01.svg
---

## Comment cela fonctionne-t-il ?

De nombreuses plateformes modernes disposent de "webhooks", ou notifications API en temps réel, pour envoyer des informations sur un nouvel événement ou de nouvelles données d'une plateforme à l'autre. La transformation des données fournit :

* Une adresse URL Braze pour recevoir ces webhooks.
* Capacités à transformer la charge utile du webhook avec du code JavaScript pour créer des requêtes valides vers divers endpoints de l'API Braze, notamment Braze `/users/track` ou `/catalogs`. Par exemple, pour la destination `/users/track`, vous pouvez choisir les informations à utiliser à partir du webhook et la manière dont vous souhaitez que les données soient conseillées sur les profils utilisateurs Braze en tant qu'attributs utilisateur, événements ou achats.
* La journalisation pour effectuer l'assurance qualité, le dépannage et le suivi des performances de vos transformations.

Le résultat final est une intégration webhook qui connecte une plateforme source de votre choix en transformant leurs webhooks en mises à jour Braze.

{% details More on webhooks %}
Les webhooks sont des notifications en temps réel envoyées via une requête HTTP POST à une destination spécifique. Les webhooks sont souvent utilisés pour envoyer des données d'un point à un autre, c'est-à-dire que le webhook peut transmettre des données sur une action qui s'est produite et sur les personnes impliquées dans cette action.

Par exemple, une plateforme d'enquête peut envoyer un webhook à une destination de votre choix chaque fois qu'une réponse à un formulaire en ligne est reçue. Ou encore, une plateforme de service client peut envoyer un webhook à une destination de son choix chaque fois qu'un ticket de service client est créé.
{% enddetails %}

## Niveaux de transformation des données

Le tableau suivant décrit les différences entre la version gratuite et la version pro de Data Transformation.

| Zone | Version gratuite | Pro de la transformation des données |
|----|----|----|
| Transformations actives | Jusqu'à 5 par entreprise | Jusqu'à 55 par entreprise |
| Par mois | 300 000 demandes par mois | 10 300 000 demandes par mois |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% alert important %}
Pour demander une mise à niveau vers Data Transformation Pro, contactez votre gestionnaire de compte Braze ou sélectionnez le bouton **Demander une mise à niveau** dans le tableau de bord de Braze.
{% endalert %}

### Limites de débit

La limite de débit pour les transformations de données de Braze est de 1 000 demandes entrantes par minute et par espace de travail. Si vous disposez de Data Transformation Pro et que vous avez besoin d'une limite de débit plus élevée, contactez votre gestionnaire de compte Braze.

## Questions fréquemment posées

### Qu'est-ce qui est synchronisé avec Braze Data Transformation ?

Toutes les données que la plateforme externe met à disposition dans un webhook peuvent être synchronisées avec Braze. Plus une plateforme externe envoie de données via des webhooks, plus il y a d'options pour choisir ce qui est synchronisé.

### Je suis un marketeur. Ai-je besoin de ressources de développement pour utiliser Braze Data Transformation ?

Nous aimerions que les développeurs utilisent également cette fonctionnalité, mais vous n'avez pas besoin d'en être un pour l'utiliser ! Les marketeurs peuvent également réussir à mettre en place des transformations sans ressources de développeurs.

### Puis-je quand même utiliser Braze Data Transformation si ma plateforme externe ne donne qu'une adresse e-mail ou un numéro de téléphone comme identifiant ?

Oui. Vous pouvez faire en sorte que vos transformations mettent à jour l'endpoint `/users/track` avec l'[adresse e-mail ou le numéro de téléphone comme identifiant]({{site.baseurl}}/api/endpoints/user_data/post_user_track/#example-request-for-updating-a-user-profile-by-email-address).

Pour ce faire, utilisez `email` ou `phone` comme propriété d'identification dans le code de transformation au lieu de `external_id` ou `braze_id`. L'exemple de [code de transformation]({{site.baseurl}}/user_guide/data_and_analytics/data_transformation/use_cases/#example-transformation-code) utilise cette fonctionnalité.

{% alert note %}
Les utilisateurs de l'accès anticipé à Braze Data Transformation qui ont commencé avant avril 2023 connaissent peut-être une fonction `get_user_by_email` qui les a aidés dans ce cas d'utilisation. Cette fonction a été supprimée.
{% endalert %}

### La transformation des données de Braze enregistre-t-elle des points de données ?

Oui, dans la plupart des cas. Braze Data Transformation crée finalement un appel `/users/track` qui écrit les attributs, les événements et les achats que vous souhaitez. Ces derniers enregistrent les points de données de la même manière que si l'appel à `/users/track` était effectué de manière indépendante. Vous avez le contrôle sur le nombre de points de données enregistrés en fonction de la façon dont vous écrivez votre transformation.

### Comment puis-je obtenir de l'aide pour configurer mon cas d'utilisation ou mon code de transformation ?

Contactez votre gestionnaire de compte Braze pour toute assistance supplémentaire.

---
nav_title: Analyse/analytique (si utilisé comme adjectif)
article_title: "Analyse/analytique des recommandations d'articles (si utilisées)"
description: "Découvrez les analyses/analytiques de recommandations d'articles et comment les afficher dans Braze."
page_order: 1.3
---

# Analyse/analytique des recommandations d'articles (si utilisées)

> Découvrez les analyses/analytiques de recommandations d'articles et comment les afficher dans Braze.

## Visualisation de l'analyse/analytique (si utilisée anjective)

Vous pouvez consulter les analyses/analytiques de votre recommandation pour savoir quels éléments ont été recommandés aux utilisateurs et quelle a été la précision du modèle de recommandation.

1. Allez dans **Analyse/analytique** > **Recommandation d'élément (si utilisé comme adjectif)**.
2. Sélectionnez votre recommandation dans la liste.

## Indicateurs disponibles

### L'audience

Il s'agit d'indicateurs liés à votre audience de recommandation, qui comprennent la précision, la couverture et le type de recommandation.

Les indicateurs d'audience de la recommandation montrent la précision (25,3 %), la couverture (54,3 %) et les types de recommandation répartis entre les articles personnalisés et les articles les plus populaires.]({% image_buster /assets/img/item_recs_analytics_1.png %})

Pour plus d'informations, reportez-vous au tableau suivant :

| Indicateurs              | Description |
| ------------------- | ---------- |
| **Précision**           | Le pourcentage de fois où le modèle a correctement deviné le prochain article acheté par un utilisateur. La précision dépend fortement de la taille et du mélange de votre catalogue et doit être utilisée comme un guide pour comprendre à quelle fréquence le modèle est correct.<br><br>Lors de tests antérieurs, nous avons constaté que les modèles fonctionnaient bien avec une précision allant de 6 à 20 %. Cette métrique est mise à jour lors du prochain recyclage du modèle.  |
| **Couverture**            | Quel est le pourcentage d'articles disponibles dans le catalogue qui sont recommandés à au moins un utilisateur. Vous pouvez vous attendre à une couverture d'articles plus élevée avec des recommandations d'articles personnalisées par rapport aux articles les plus populaires. |
| **Type de recommandation** | Le pourcentage d'utilisateurs qui recevront des recommandations personnalisées ou les plus récentes par rapport à la solution de repli des articles les plus populaires. La solution de repli est envoyée aux utilisateurs qui ne disposent pas de suffisamment de données pour générer une recommandation personnalisée ou la plus récente. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Articles

Ce tableau comprend des indicateurs sur les articles personnalisés, les plus récents et les plus populaires de votre catalogue.

\![Tableaux côte à côte répertoriant les éléments attribués aux utilisateurs, séparés par les recommandations personnalisées et les recommandations les plus populaires.]({% image_buster /assets/img/item_recs_analytics_2.png %})

Pour plus d'informations, reportez-vous au tableau suivant :

| Indicateurs              | Description |
| ------------------- | ---------- |
| **Articles personnalisés**<br><br>**Derniers articles** | Cette colonne répertorie chaque article du catalogue par ordre décroissant de recommandation aux utilisateurs. Cette colonne indique également le nombre d'utilisateurs auxquels le modèle a attribué chaque élément.<br><br>En fonction du [type de recommandation]({{site.baseurl}}/user_guide/brazeai/recommendations/), les éléments **personnalisés** ou les **plus récents** seront répertoriés. |
| **Articles les plus populaires** | Cette colonne présente chaque article du catalogue par ordre décroissant de popularité. La popularité fait ici référence aux éléments du catalogue avec lesquels les utilisateurs interagissent le plus souvent dans l'ensemble de l'espace de travail. Le plus populaire est utilisé comme solution de repli lorsque la personnalisation ou le plus récent ne peuvent être calculés pour un utilisateur individuel. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Aperçu

Il s'agit d'un aperçu de la configuration de la recommandation que vous avez choisie, qui comprend la date de la dernière mise à jour de la recommandation.

!Tableau d'aperçu des recommandations affichant le type, le catalogue, le type d'événement, le nom de l'événement personnalisé, le nom de la propriété et la date de la dernière mise à jour.]({% image_buster /assets/img/item_recs_analytics_3.png %}){: style="max-width:50%" }

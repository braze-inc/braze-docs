---
nav_title: "L'hymne du futur"
article_title: "L'hymne du futur"
description: "Découvrez comment intégrer Future Anthem à Braze."
alias: /partners/future_anthem/
page_type: partner
search_tag: Partner
---

# L'hymne du futur

> Amplifier AI, le produit tout-en-un de Future Anthem pour le secteur des jeux en argent réel, offre une personnalisation du contenu, des expériences en temps réel et des audiences dynamiques. Amplifier AI fonctionne de façon fluide/sans heurts/de la façon homogène, en permettant aux clients d'améliorer les profils des joueurs de Braze avec des attributs de joueurs spécifiques à l'industrie, tels que le jeu préféré, l'équipe préférée, le score d'engagement, la recommandation du prochain pari, le prochain pari attendu, etc.

{% alert important %}
Cette fonctionnalité est actuellement en accès anticipé. Veuillez contacter l'équipe de réussite client de Future Anthem pour commencer.
{% endalert %}

## Conditions préalables

| Condition              | Descriptif                                            |
|--------------------------|--------------------------------------------------------|
| Futur compte Anthem    | Un compte Future Anthem. |
| Clé d'API REST Braze       | Une clé de l'API REST de Braze avec l'extension [`users.track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track). Elle peut être créée dans le tableau de bord de Braze depuis **Paramètres** > **Clés d'API**. |
| Endpoint REST Braze      | L'[endpoint REST de]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints) Braze qui correspond à votre instance, par exemple `rest.iad-01.com`. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Cas d’utilisation

Grâce à cette intégration, vous pouvez :

- Identifiez les utilisateurs ayant un score d'engagement élevé et ciblez-les avec des offres personnalisées, telles que des promotions exclusives ou des récompenses VIP.
- Suggérer des jeux similaires à un utilisateur en fonction des jeux qu'il aime déjà.

## Intégration

L'équipe de la satisfaction client de Future Anthem vous aidera à mettre en place votre intégration. Contactez votre interlocuteur Customer Success qui vous aidera à identifier les attributs les plus pertinents à envoyer à Braze.

|Exemple d'attributs dans Future Anthem|Exemples d'attributs en Braze|
|-----------------------------------|---------------------------|
|![Les attributs du profil utilisateur.]({% image_buster /assets/img/future_anthem/future_anthem_example_attributes.png %})|![L'attribut de l'objet.]({% image_buster /assets/img/future_anthem/braze_example_attributes.png %})|

## Attributs personnalisés Braze

Voici les attributs personnalisés disponibles pour Braze. Pour plus d'informations, voir [Future Anthem : Mise en route](https://knowledge.futureanthem.com/getting-started).

{% tabs local %}
{% tab Recommandations de paris %}

| Sous-catégorie | Exemple (JSON) | Type de données |
| ------- | ----------- |----------- |
| Préférences de l'utilisateur | `{"Sport": "Ice Hockey", "League": "NHL", "Market": "Goals", "Team": "Rangers", "Player": "Kreider"}`| Objet |
| Recommandations de paris simples | `{"Sport": "Ice Hockey", "League": "NHL", "Market": "Goals", "Team": "Rangers", "Player": "Kreider"}`| Objet |
| Recommandations de paris accumulateurs | `{"Bet_1": "Halland Goal vs. Manchester United", "Bet_2": "Liverpool vs. Everton"}`| Objet |
| Recommandations de paris accumulateurs | `{"Bet_1": 1.5, "Bet_2": 2}` | Objet |
| Bet Builder Recommandations de paris | `{"Sport":"American Football", "Competition":"NFL", "Event":"Seahwaks@Giants", "Market":"MoneyLine", "Selection":"Seahawks"}`| Objet |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab Recommandations en matière de bonus %}

| Sous-catégorie | Exemple | Type de données |
| ------- | ----------- |----------- |
|NGR - Net Gaming revenue for the user's lifetime (Chiffre d'affaires net des jeux pour la durée de vie de l'utilisateur) | 2232| Nombre|
| NGR14 - Chiffre d'affaires net des jeux pour les 14 derniers jours d'activité | 42 | Nombre
| Score de rentabilité des joueurs| 130 | Nombre |
| Score d'engagement | 0.78 | Nombre |
| Score du risque d’attrition | 0.02 | Nombre |
| Date estimée du prochain pari | 2024-08-29 | Date |
| Bet and Get - Recommandation sur la valeur du bonus | 20 | Nombre |
| Autres recommandations sur la valeur de la prime à l'avenir | 0 | Nombre |
| Futur CLTV  | 3126 | Nombre |

{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab Recommandations de jeux %}

| Sous-catégorie | Exemple | Type de données |
| ------- | ----------- |----------- |
| Recommandé pour vous | Fluffy Favourites, Fishin' Frenzy, Big Bass Bonanza, Rainbow Gold, Wild West| Tableau |
| Jeux préférés | La frénésie de la pêche | Tableau |
| Nouveaux jeux recommandés | Sticky Bees, Beware the Deep Megaways, Gold Party, Les Pierrafeu| Tableau |
| Des joueurs comme vous jouent (filtrage collaboratif) |Gold Blitz, Big Bass Splash, Rick and Morty, Book of Dead, Gates of Olympus, Luck O' the Irish | Tableau |
| Parce que vous avez joué (Similitude de jeu)|Fluffy Favourites 2, Luck Rish Express, Gold Cash, Aztec Treasure Hunt, Stars Bonanza | Tableau |
| Prochaine étape (séquençage des jeux) | Fishin' Frenzy The Big Catch, Big Banker, 9 Masks Of Fire, Super Lion, Fishin' Bigger Pots Of Gold | Tableau |
| Jeux populaires | Temple de l'Iris, Fishin' Frenzy, Rishing Reward, Crazy Time, Fluffy Favourites | Tableau |
| Jeux en vogue | Pig Banker, Hyper Gold, Pyramid King, Gold Cash | Tableau |

{: .reset-td-br-1 .reset-td-br-2 role="presentation" }
{% endtab %}

{% tab Groupe de joueurs %}

| Sous-catégorie | Exemple | Type de données |
| ------- | ----------- |----------- |
| Montrer dans quel groupe se trouve le joueur | Jeu de grande valeur Diversité| Chaîne de caractères |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }
{% endtab %}

{% tab Durabilité du joueur - Risque potentiel du joueur %}

| Sous-catégorie | Exemple | Type de données |
| ------- | ----------- |----------- |
| Score de risque | 0.5| Nombre |
| Joueur à risque | Vrai | Valeur booléenne |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }
{% endtab %}
{% endtabs %}

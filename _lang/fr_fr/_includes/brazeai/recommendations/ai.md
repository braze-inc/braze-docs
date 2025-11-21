{% if include.section == "Plan-specific features" %}

## Fonctionnalités de l'intelligence artificielle propres au régime

Le tableau suivant décrit les différences entre la version gratuite et la version pro des types de recommandation Intelligence artificielle personnalisée, Populaire et Tendance :

| Secteur                   | Version gratuite                          | Version Pro            |
| :---------------------- | ------------------------------------- | :--------------------------------------- |
| Fréquence de mise à jour de l’utilisateur<sup>1</sup>   | Hebdomadaire                                | Tous les jours                                    |
| Fréquence de réentraînement du modèle  | Mensuelle                               | Hebdomadaire                                   |
| Modèles de recommandation maximale | 1 modèle par <sup>type2</sup> | 100 modèles par <sup>type2</sup> |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

<sup>1\. Il s'agit de la fréquence à laquelle les recommandations d'articles spécifiques à l'utilisateur sont mises à jour (tous les modèles à l'exception des articles les plus populaires, qui sont mis à jour lorsque le modèle se réapprend). Par exemple, si un utilisateur achète un produit sur la base des recommandations de produits avec l’IA, ses produits recommandés seront mis à jour selon cette fréquence</sup><br>
<sup>2\. Les types de recommandations disponibles sont les suivants : Intelligence artificielle personnalisée, Plus récent, Plus populaire et Tendance.</sup>

{% endif %}

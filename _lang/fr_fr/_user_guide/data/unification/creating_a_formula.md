---
nav_title: "Création d'une formule"
article_title: "Création d'une formule"
page_order: 1.2
page_type: reference
description: "Cet article de référence traite de la création et de la gestion des formules, qui vous aident à comprendre facilement les relations complexes qui existent dans vos données."
tool: Reports

---
# Création d'une formule

> Lors de l'affichage des analyses/analytiques dans Braze, vous pouvez combiner plusieurs points de données pour obtenir des informations précieuses sur vos données utilisateur. C'est ce que l'on appelle les formules. Utilisez des formules pour normaliser vos données de séries chronologiques en fonction de votre nombre total d'utilisateurs actifs mensuels (MAU) et d'utilisateurs actifs quotidiens (DAU). 

Les formules vous aident à comprendre les relations complexes qui existent dans vos données. Par exemple, vous pouvez comparer le nombre d'événements personnalisés réalisés par les utilisateurs actifs par jour qui correspondent à un segment particulier par rapport à la population générale (ou par rapport à un autre segment).

## Cas d'utilisation

Les formules, en particulier lorsqu'elles sont associées à des événements personnalisés, peuvent vous aider à comprendre les comportements des utilisateurs au sein de votre application. Les formules permettent également d'obtenir des informations plus approfondies sur les statistiques des segments d'achat, même si votre entreprise utilise des médias payants en conjonction avec Braze, tels que Google Ads ou la télévision. 

Les exemples suivants illustrent les types de comportements qui peuvent être détectés à l'aide de formules :

- **Applications de covoiturage :** Si vous disposez d'un événement personnalisé pour l'annulation d'un trajet par l'utilisateur, vous pouvez configurer une fonction pour les trajets annulés / DAU afin de déterminer si certains segments d'utilisateurs ont tendance à annuler plus de trajets que d'autres.
- **Applications de commerce électronique :** En configurant une fonction pour les achats d'un certain ID de produit / MAU, vous pouvez comparer la popularité d'un produit récemment promu entre les segments, même si toutes les promotions n'ont pas pu être suivies à l'aide de Braze.
- **Applications médias utilisant des publicités :** Si l'expérience des utilisateurs est interrompue par des publicités entre les clips vidéo ou audio, l'enregistrement des sorties de publicités intermédiaires en tant qu'événement personnalisé et le calcul du ratio sorties de publicités intermédiaires / DAU peuvent aider à trouver les meilleurs segments à cibler avec une campagne d'abonnements premium sans publicité.

## Création de formules

Les formules sont accessibles dans les panneaux de statistiques des pages [Accueil]({{site.baseurl}}/user_guide/analytics/dashboard/home_dashboard/), [Rapport sur les chiffres d'affaires]({{site.baseurl}}/user_guide/data/export_braze_data/exporting_revenue_data/) et [Rapport sur les événements personnalisés]({{site.baseurl}}/user_guide/data/custom_data/custom_events/) du tableau de bord. Pour afficher ce panneau, allez dans le graphique **Performance au fil du temps**, changez le menu déroulant **Statistiques pour** en **Formules d'indicateurs clés de performance**, puis sélectionnez au moins une formule d'indicateur clé de performance pour remplir le graphique.

Visualisez les statistiques des indicateurs clés de performance dans le tableau de bord de Braze.]({% image_buster /assets/img_archive/kpi_forms.png %})

Pour créer une nouvelle formule :

1. Accédez au tableau de bord approprié**(Accueil**, **Rapport sur les revenus** ou **Rapport sur les événements personnalisés**).
2. Sélectionnez **Gérer les formules des indicateurs clés de performance**.
3. Saisissez un nom pour votre formule.
4. Sélectionnez les numérateurs et les dénominateurs appropriés.
5. Sélectionnez **Enregistrer**.

## Numérateurs et dénominateurs disponibles

<style>
  div.small_table + table {
    max-width: 50%;
  }
  div.large_table + table {
    max-width: 75%;
  }
table th:nth-child(1),
table th:nth-child(2),
table th:nth-child(3),
table td:nth-child(1),
table td:nth-child(2),
table td:nth-child(3) {
    width:25%;
}
table td {
    word-break: break-word;
}
</style>

<div class="small_table"></div>

### Tableau de bord aperçu

| Numérateurs | Dénominateurs |
| --- | --- |
| UTILISATEUR ACTIF QUOTIDIEN | MAU |
| Sessions | UTILISATEUR ACTIF QUOTIDIEN |
| | Taille du segment |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Tableau de bord des recettes

| Numérateurs | Dénominateurs |
| --- | --- |
| Achats (tous) | UTILISATEUR ACTIF QUOTIDIEN |
| Sélectionner des achats (tels qu'une carte cadeau ou un produit ID) | MAU |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Tableau de bord personnalisé des événements

| Numérateurs | Dénominateurs |
| --- | --- |
| Nombre d'événements personnalisés | MAU |
|  | UTILISATEUR ACTIF QUOTIDIEN |
|  | Taille du segment (seuls les segments pour lesquels le [suivi analytique]({{site.baseurl}}/viewing_and_understanding_segment_data/) est activé peuvent être utilisés). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }


---
nav_title: Création d’une formule
article_title: Création d’une formule
page_order: 1.2
page_type: reference
description: "Cet article de référence couvre la création et la gestion des formules pour vous aider à comprendre facilement les relations complexes entre vos données."
tool: Reports

---
# Création d’une formule

> Les vues analytiques de Braze vous permettent désormais de combiner plusieurs points de données pour obtenir des informations précieuses sur vos données utilisateur. On les appelle des formules. Les formules vous permettent de normaliser vos données de séries temporelles selon votre nombre total d’utilisateurs actifs par mois (MAU) et d’utilisateurs actifs par jour (DAU). Elles vous aident également à comprendre facilement les relations complexes qui existent au sein de vos données. 

Par exemple, vous pouvez comparer combien d’événements personnalisés ont été effectués par des utilisateurs actifs quotidiens qualifiés pour un segment spécifique, par rapport à l’ensemble des clients (ou par rapport à un autre segment).

## Cas d’utilisation

Les formules, en particulier lorsqu’elles sont associées à des événements personnalisés, vous permettent de mieux comprendre les comportements des utilisateurs dans votre application. Les formules peuvent également donner des informations plus approfondies sur les tendances d’achat de vos segments, même si votre entreprise utilise des médias payants en même temps que Braze, comme Google Ads ou des publicités télévisées. 

Voici quelques exemples de types de comportements qui peuvent être détectés grâce aux formules :

- **Applications de covoiturage :** Si vous avez défini un événement personnalisé quand l’utilisateur annule un trajet, la configuration d’une fonction Trajets Annulés / Utilisateurs actifs par jour peut être utilisée pour déterminer si certains segments d’utilisateur ont plus tendance que d’autres à annuler leur taxi.
- **Applications d’E-commerce :** En configurant une fonction pour les achats d’un certain ID Produit/MAU, vous pouvez comparer la popularité entre les segments d’un produit qui a fait l’objet d’une promotion récente, même si toutes les promotions n’étaient pas suivies dans Braze.
- **Applications média utilisant des publicités :** Si l’expérience des utilisateurs est interrompue par des publicités entre des clips vidéo ou audio, enregistrer en tant qu’événement personnalisé les sorties pendant la publicité et calculer le ratio Sorties mi-publicité/Utilisateurs actifs par jour peut aider à identifier les meilleurs segments à cibler avec une campagne pour des abonnements premium sans publicité.

## Création de formules

Les formules sont accessibles sur les panneaux de statistiques des pages [Overview][9] (Aperçu), [Revenue][10] (Chiffre d’affaires) et [Custom Events][11] (Événements personnalisés) du tableau de bord. Pour afficher ce panneau, modifiez la liste déroulante **View Statistics For (Afficher les statistiques pour)** sur **KPI Formulas (Formules d’indicateurs clés de performance)**.

![Afficher les statistiques des formules d’indicateurs clés de performance sur le tableau de bord de Braze][16]

Pour créer une nouvelle formule :

1. Rendez-vous sur le tableau de bord approprié (Overview, Revenue, or Custom Events).
2. Cliquez sur **Manage KPI Formulas (Gérer les formules d’indicateurs clés de performance)**.
3. Saisissez un nom pour votre formule.
4. Sélectionnez les numérateurs et dénominateurs pertinents.
5. Cliquez sur **Save (Enregistrer)**.

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

### Tableau de bord Overview

| Numérateurs | Dénominateurs |
| --- | --- |
| Utilisateurs actifs quotidiens (DAU) | MAU |
| Sessions | Utilisateurs actifs quotidiens (DAU) |
| | Taille du segment |
{: .reset-td-br-1 .reset-td-br-2}

### Tableau de bord des revenus

| Numérateurs | Dénominateurs |
| --- | --- |
| Achats (tous) | Utilisateurs actifs quotidiens (DAU) |
| Sélectionnez Achats (comme une carte-cadeau ou un ID Produit) | MAU |
{: .reset-td-br-1 .reset-td-br-2}

### Tableau de bord des événements personnalisés

| Numérateurs | Dénominateurs |
| --- | --- |
| Nombre d’événements personnalisés | MAU |
|  | Utilisateurs actifs quotidiens (DAU) |
|  | Taille du segment (seuls les segments avec [suivi analytique][17] activé peuvent être utilisés) |
{: .reset-td-br-1 .reset-td-br-2}

[9]: {{site.baseurl}}/user_guide/data_and_analytics/reporting/understanding_your_app_usage_data/
[10]: {{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/exporting_revenue_data/
[11]: {{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/
[16]: {% image_buster /assets/img_archive/kpi_forms.png %}
[17]: {{site.baseurl}}/user_guide/data_and_analytics/reporting/viewing_and_understanding_segment_data/#viewing-and-understanding-segment-data

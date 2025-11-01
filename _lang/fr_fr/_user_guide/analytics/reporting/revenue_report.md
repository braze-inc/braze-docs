---
nav_title: "Chiffre d'affaires"
article_title: "Chiffre d'affaires"
page_type: reference
description: "Cette page décrit comment utiliser la page Rapport sur les recettes pour afficher des données sur les recettes sur des périodes spécifiques, les recettes d'un produit spécifique et les recettes totales de votre appli."
tool: Reports
---

# Chiffre d'affaires

> La page Rapport sur les recettes vous permet de consulter les données relatives aux recettes sur des périodes spécifiques, aux recettes d'un produit spécifique et aux recettes totales de votre application.

Pour afficher un rapport sur vos chiffres d'affaires à partir du tableau de bord, accédez à **Analyse** > **Rapport sur les revenus.** 

## Personnalisation de votre chiffre d'affaires

Vous pouvez personnaliser votre rapport d'affaires en sélectionnant une plage de dates, les applications sur lesquelles portera le rapport et des paramètres.

La page "Rapport sur les recettes" montre le graphique "Performance au fil du temps" avec "Recettes" comme paramètre.]({% image_buster /assets/img/revenue_report.png %})

### Filtrage par date et par application

Sélectionnez la plage de dates pour votre chiffre d'affaires et, si vous le souhaitez, une application spécifique ou une sélection d'applications.

### Filtrage par paramètres

Le graphique des **performances dans le temps** montre les données pour différents paramètres, qui peuvent être sélectionnés dans le menu déroulant **Statistiques pour.**  Vous pouvez éventuellement ventiler les données de certains paramètres dans le menu déroulant **Ventilation**.

Vous pouvez visualiser les données suivantes dans le **graphique des performances au fil du temps**:
- Formules d'indicateurs clés de performance
- Achats
    - (Facultatif) Achats par produit
- Chiffre d'affaires
    - (Facultatif) Chiffre d'affaires par segment
    - (Facultatif) Chiffre d'affaires par produit
- Chiffre d'affaires par heure
    - (Optionnel) Chiffre d'affaires par heure par segmentation
- Chiffre d'affaires par utilisateur

## Comprendre les chiffres d'affaires

<style>
    .no-split {
        word-break: keep-all;
    }
</style>

<table>
    <thead>
        <tr>
            <th>Indicateurs</th>
            <th>Définition</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#lifetime-revenue">Chiffre d'affaires à vie</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Lifetime Revenue' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#lifetime-value-per-user">Valeur vie client par utilisateur</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Lifetime Value Per User' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#average-daily-revenue">Chiffre d'affaires quotidien moyen</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Average Daily Revenue' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#daily-purchases">Achats quotidiens</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Daily Purchases' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#daily-revenue-per-user">Chiffre d'affaires quotidien par utilisateur</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Daily Revenue Per User' %}</td>
        </tr>
    </tbody>
</table>

## Visualisation de la répartition du produit

Consultez le tableau **Ventilation des produits** pour obtenir la liste des produits achetés au cours de la période sélectionnée, le nombre de produits achetés et le chiffre d'affaires généré par chacun d'entre eux.

Le tableau "Ventilation des produits" affiche les colonnes "Nom du produit", "Achats" et "Chiffre d'affaires".]({% image_buster /assets/img/revenue_report_product_breakdown.png %})



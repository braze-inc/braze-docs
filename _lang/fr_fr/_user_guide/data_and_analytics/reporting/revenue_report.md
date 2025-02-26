---
nav_title: "Rapport de chiffre d'affaires"
article_title: "Rapport de chiffre d'affaires"
page_type: reference
description: "Cet article de référence traite de la page Rapport de chiffre d'affaires."
tool: Reports
---

# Rapport de chiffre d'affaires

> La page Rapport de chiffre d'affaires vous permet de consulter les données relatives au chiffre d'affaires sur des périodes spécifiques, aux revenus d'un produit spécifique et aux revenus totaux de votre application.

Pour afficher un rapport sur vos chiffres d'affaires à partir du tableau de bord, accédez à **Analyse** > **Rapport sur les revenus.** 

{% alert note %}
Si vous utilisez l'[ancienne navigation]({{site.baseurl}}/navigation), cette page se trouve sous **Données.**
{% endalert %}

## Personnalisation de votre chiffre d'affaires

Vous pouvez personnaliser votre rapport du chiffre d'affaires en sélectionnant une plage de dates, les applications sur lesquelles portera le rapport, ainsi que des paramètres.

![Page « Rapport de chiffre d’affaires » montrant le graphique « Évolution des performances » avec « Chiffre d’affaires » comme paramètre.][1]

### Filtrage par date et par application

Sélectionnez la plage de dates pour votre rapport de chiffre d'affaires et, si vous le souhaitez, une application spécifique ou une sélection d'applications.

### Filtrage par paramètres

Le graphique des **performances dans le temps** montre les données pour différents paramètres, qui peuvent être sélectionnés dans le menu déroulant **Statistiques pour.**  Vous pouvez éventuellement ventiler les données de certains paramètres dans le menu déroulant **Ventilation.**

Vous pouvez visualiser les données suivantes dans le **graphique des performances au fil du temps**:
- Formules de KPI
- Achats
    - (Facultatif) Achats par produit
- Revenue
    - (Optionnel) Chiffre d'affaires par segment
    - (Facultatif) Chiffre d'affaires par produit
- Revenus horaires
    - (Optionnel) Chiffre d'affaires par heure par segmentation
- Chiffre d’affaires par utilisateur

## Calcul du chiffre d'affaires

<style>
    .no-split {
        word-break: keep-all;
    }
</style>

<table>
    <thead>
        <tr>
            <th>Indicateur</th>
            <th>Définition</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#lifetime-revenue">Revenus à vie</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Lifetime Revenue' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#lifetime-value-per-user">Valeur vie client par utilisateur</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Lifetime Value Per User' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#average-daily-revenue">Chiffre d'affaires quotidien moyen</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Average Daily Revenue' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#daily-purchases">Achats quotidiens</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Daily Purchases' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#daily-revenue-per-user">Revenus quotidiens par utilisateur</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Daily Revenue Per User' %}</td>
        </tr>
    </tbody>
</table>

## Visualisation de la répartition des produits

Consultez le tableau **Ventilation des produits** pour obtenir la liste des produits achetés au cours de la période sélectionnée, le nombre de produits achetés et le chiffre d'affaires généré par chacun d'entre eux.

![Tableau « Ventilation des produits » affichant les colonnes « Nom du produit », « Achetés » et « Chiffre d'affaires ».][2]


[1]: {% image_buster /assets/img/revenue_report.png %}
[2]: {% image_buster /assets/img/revenue_report_product_breakdown.png %}

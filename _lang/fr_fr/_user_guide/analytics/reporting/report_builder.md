---
nav_title: Générateur de rapports
article_title: Générateur de rapports
alias: /report_builder/
page_type: reference
description: "Cet article de référence décrit la fonctionnalité du générateur de rapports."
tool:
    - Reports
page_order: 6.2
---

# Générateur de rapports

> Cette page explique comment utiliser le générateur de rapports pour créer et afficher des rapports granulaires à l'aide des données de Braze, et comment ajouter des rapports aux tableaux de bord.

## Utilisation d'un modèle de rapport

1. Allez dans **Analyse/analytique** > **Générateur de rapports (Nouveau)**.
2. Sélectionnez la flèche **Autres options** en regard du bouton **Créer un nouveau rapport**, puis sélectionnez **Utiliser un modèle de rapport**.<br><br>\!["Créer un nouveau rapport" bouton déroulant avec options pour créer un rapport personnalisé ou utiliser un modèle.]({% image_buster /assets/img/report_builder_2/create_new_report.png %}){: style="max-width:40%;"}<br><br>
3. Sélectionnez l'un des modèles de rapport de la bibliothèque de modèles de Braze.
    - Utilisez les **éléments de la rangée** et le menu déroulant des **tags** pour trouver des rapports pertinents pour vos cas d'utilisation.<br><br>!fenêtre "Modèles de rapport de Braze" avec une liste de modèles de Braze à sélectionner.]({% image_buster /assets/img/report_builder_2/report_templates.png %}){: style="max-width:90%;"}<br><br>
4. Suivez les étapes 3 et suivantes de la section [Création d'un rapport](#creating-a-report) pour personnaliser davantage le rapport en fonction de votre cas d'utilisation.

## Création d'un rapport

1. Allez dans **Analyse/analytique** > **Générateur de rapports (Nouveau)**.
2. Sélectionnez **Créer un nouveau rapport**.
3. Dans le menu déroulant **Lignes**, sélectionnez les éléments sur lesquels vous souhaitez établir un rapport :
    - Campagnes
    - Toiles
    - Campagnes et toiles
    - Canaux
    - Tags

    Notez que votre sélection de **lignes** aura un impact sur [les indicateurs que vous pouvez visualiser](#metrics-availability). Par exemple, vous ne pouvez afficher les indicateurs multivariés que si vous établissez un rapport sur les **toiles** ou les **campagnes** avec une analyse détaillée de la **variante**. Vous ne pouvez pas afficher ces indicateurs lorsque vous établissez des rapports sur les campagnes et **les canevas**, même si ces campagnes et canevas comportent des tests multivariés. 

La section "Lignes et colonnes" contient des champs permettant de sélectionner les lignes et les regroupements de votre rapport.]({% image_buster /assets/img/report_builder_2/rows_and_columns.png %}){: style="width:90%;"}

{: start="4"}
4\. (Facultatif) Sélectionnez **Ajouter un éclatement** pour décomposer vos données en vues plus granulaires :
    \- Canaux
    \- Date
        \- Utilisez cette fonction pour diviser vos données en plages de temps plus petites. Par exemple, si vous souhaitez connaître les performances de vos campagnes par jour, sélectionnez la configuration suivante :
            - **Rangs**: Campagnes
            - **Groupement :** Date
            - **Intervalle :** Jours
    \- Variantes
    \- Campagnes et toiles

{% alert tip %}
Essayez différentes configurations d'options de recherche pour explorer les [nombreuses façons dont vous pouvez décomposer vos données](#metrics-availability).
{% endalert %}

{: start="5"}
5\. Dans la section **Colonnes**, sélectionnez **Personnaliser les indicateurs.**

\![La section "Personnaliser les indicateurs" avec des options permettant de sélectionner plusieurs indicateurs.]({% image_buster /assets/img/report_builder_2/customize_metrics.png %}){: style="width:90%;"}

{: start="6"}
6\. Parcourez les indicateurs par catégorie et cochez la case correspondante pour ajouter un indicateur à votre rapport.
    \- Réorganisez les indicateurs et les colonnes en faisant glisser l'icône en pointillé vers le haut ou vers le bas.
7\. Dans **Contenu du rapport**, configurez la plage de dates pour laquelle vous souhaitez inclure des données dans votre rapport.
8\. Ensuite, en fonction de vos sélections à l'étape 3, choisissez d'ajouter manuellement ou automatiquement des campagnes, des canevas ou les deux à votre rapport.
    - **Ajouter manuellement :** Choisissez chaque campagne ou Canvas à inclure dans le rapport en utilisant les filtres pour les dates de **dernier envoi** et les tags ou canaux, ou en recherchant le nom de la campagne ou du Canvas.<br><br>\![La section "Ajouter manuellement des campagnes et des toiles" avec une liste de campagnes à sélectionner.]({% image_buster /assets/img/report_builder_2/manually_add.png %}){: style="width:90%;"}<br><br>
    - **Ajouter automatiquement :** Définissez des règles pour les campagnes ou les canevas à inclure dans le rapport. Vous ne devez sélectionner qu'un seul champ sur cette page.
        \- Notez qu'au fur et à mesure que des campagnes ou des canevas supplémentaires remplissent les conditions que vous avez définies dans cet écran, ils seront automatiquement ajoutés aux exécutions futures de votre rapport.<br><br>La section "Ajouter automatiquement des campagnes et des toiles" contient des champs permettant de définir des règles pour les campagnes et les toiles qui doivent être ajoutées au rapport.]({% image_buster /assets/img/report_builder_2/automatically_add.png %}){: style="width:90%;"}<br><br>
9\. Exécutez le rapport en sélectionnant **Enregistrer & Exécuter**.

{% alert note %}
L'exécution du rapport peut prendre jusqu'à quelques minutes, en fonction de la plage de dates et du nombre de campagnes ou de Canevas que vous avez sélectionnés lors de l'étape de configuration.
{% endalert %}

## Disponibilité des indicateurs

Votre sélection de **rangées** affecte les indicateurs que vous pouvez sélectionner.

{% alert tip %}
Si vous souhaitez établir un rapport sur les variantes du canvas ou les étapes, sélectionnez **Canvas** pour les lignes et laissez le champ vide ou sélectionnez **Date** pour l'éclatement. Cela crée une liste déroulante **Vue Canvas** qui permet d'afficher les indicateurs pour le Canvas uniquement, ou de regrouper les indicateurs par variante, étape ou message. 

\![La liste déroulante "Canvas View" ouverte.]({% image_buster /assets/img/report_builder_2/canvas_view_dropdown.png %}){: style="width:40%;"}
{% endalert %}

| Indicateurs | Description |
| --- | --- |
| Indicateurs de conversion | Disponible pour les campagnes, les toiles, les campagnes et les toiles. |
| Entrées | Disponible pour les Campagnes, Toiles, Campagnes et Toiles, Tags. |
| Dernière date d'envoi | Disponible pour les campagnes, les toiles, les campagnes et les toiles. S'affiche uniquement pour les campagnes planifiées - ne s'affiche pas pour les campagnes basées sur des actions ou déclenchées par l'API. |
| Envoie | Disponible pour chaque canal concerné. |
| Envois de messages | Disponible pour les Campagnes, Toiles, Campagnes et Toiles, Tags. |
| Ligne d'objet | Disponible pour les campagnes e-mail avec **Variante** drilldown, les Canvases et les Canvases avec **Variante** drilldown. |
| Chiffre d'affaires total | Disponible pour les Campagnes, Toiles, Campagnes et Toiles, Tags. Indisponible avec la recherche de **canaux**. |
| Impressions uniques | Disponible pour les Campagnes, Toiles, Campagnes et Toiles, Tags. |
| Destinataires uniques | Disponible pour les Campagnes, Toiles, Campagnes et Toiles, Tags. Indisponible avec la recherche de **canaux**. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

## Visualisation d'un rapport

Après avoir exécuté votre rapport, vous pouvez visualiser vos résultats sous forme de tableau sur la page du rapport. 

\![Un tableau des données du rapport pour les indicateurs de chaque campagne.]({% image_buster /assets/img/report_builder_2/report_table.png %}){: style="width:90%;"}

### Création d'un graphique de rapport

Au bas de la page, vous pouvez créer un graphique de vos données en sélectionnant un **type de graphique** et en configurant les indicateurs du graphique. Par défaut, vous verrez le premier indicateur.

Un graphique des données du rapport avec des options permettant de configurer l'axe des x, l'axe des y, le type de graphique, etc.]({% image_buster /assets/img/report_builder_2/visualize_table.png %}){: style="max-width:90%;"}

{% alert note %}
Pour créer un graphique linéaire, sélectionnez **Date** comme option de recherche lors de la configuration de l'état. Cela permet d'afficher les tendances dans le temps.
{% endalert %}

#### Télécharger un graphique de rapport

Pour télécharger une image du graphique du rapport, sélectionnez l'icône en pointillé, puis choisissez une option de téléchargement.

Un menu avec des options de téléchargement pour différents formats de fichiers.]({% image_buster /assets/img/report_builder_2/download_options.png %}){: style="max-width:70%;"}

## Partager un rapport

Vous pouvez partager un lien vers le tableau de bord du rapport en sélectionnant **Partager** et l'une de ces options :
- **Partager un lien :** Copiez et partagez le lien.

\!["Partager un lien" avec un lien vers le rapport.]({% image_buster /assets/img/report_builder_2/share_this_report.png %}){: style="max-width:70%;"}

- **Envoyez ou planifiez un e-mail :** Envoyez un e-mail immédiatement ou à une heure donnée contenant un lien de téléchargement qui expire au bout d'une heure. Vous pouvez sélectionner les destinataires parmi les utilisateurs du tableau de bord répertoriés dans le menu déroulant **Destinataires de l'e-mail** ou saisir toute autre adresse e-mail.

!Fenêtre "Planifier un e-mail" avec des champs permettant de choisir le format du rapport, le destinataire et la date d'envoi.]({% image_buster /assets/img/report_builder_2/schedule_an_email.png %}){: style="max-width:70%;"}

- **Téléchargez le fichier CSV :** Téléchargez un fichier CSV du rapport.

## Ajouter un rapport à un tableau de bord

1. Sélectionnez l'icône en pointillé en haut du tableau du rapport.
2. Sélectionnez **Ajouter au tableau de bord**.
3. Sélectionnez si vous souhaitez créer un nouveau tableau de bord ou l'ajouter à un tableau de bord existant.<br><br>\![Fenêtre avec des options permettant de sélectionner si vous souhaitez ajouter le rapport à un tableau de bord nouveau ou existant.]({% image_buster /assets/img/report_builder_2/add_to_dashboard.png %}){: style="width:90%;"}<br><br>
4. Suivez les étapes de [Dashboard Builder]({{site.baseurl}}/user_guide/analytics/reporting/dashboard_builder/) pour en savoir plus sur la création d'un tableau de bord.


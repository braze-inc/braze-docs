---
nav_title: Données du segment
article_title: Afficher et comprendre les données de segment
page_order: 2
page_type: reference
description: "Cette page explique la section des segments de votre tableau de bord de Braze, et comprend un résumé des statistiques fournies."
tool: 
  - Segments
  - Reports
  
---
# Données de segment

> Cette page explique la section des segments de votre tableau de bord de Braze, et comprend un résumé des statistiques fournies.

## Accès aux données relatives à vos segments

La page **Segments** de votre tableau de bord Braze contient un résumé de tous vos segments et vous permet d'examiner les données détaillées de chacun d'entre eux. Sur cette page, recherchez et sélectionnez le nom d'un segment pour modifier et consulter ses données. Pour savoir comment créer un segment, consultez [Créer un segment][3].

![Page Segments][1]

Après avoir sélectionné le nom d'un segment, vous pouvez afficher les statistiques et les filtres du segment, et modifier le segment en ajoutant ou en supprimant des filtres. Assurez-vous d’enregistrer vos modifications !

![Données de segment][2]

Lorsque vous activez [le suivi analytique pour un segment][9], Braze vous permet d'afficher les sessions, les événements personnalisés et le chiffre d'affaires au fil du temps pour ce segment.

### Statistiques de segment

Vous pouvez consulter les statistiques de segmentation suivantes, qui se mettent à jour en temps réel lorsque vous ajoutez ou supprimez des filtres :

<style>
    .no-split {
        word-break: keep-all;
    }
</style>

<table>
    <thead>
        <tr>
            <th>Statistique</th>
            <th>Définition</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td class="no-split">Total des utilisateurs</td>
            <td class="no-split">Combien d’utilisateurs votre application a-t-elle au total ?</td>
        </tr>
        <tr>
            <td class="no-split">Utilisateurs sélectionnés</td>
            <td class="no-split">Combien d’utilisateurs sont dans votre segment et le pourcentage de votre base d’utilisateurs totale qu’il représente.</td>
        </tr>
        <tr>
            <td class="no-split">Valeur à vie (utilisateurs payants)</td>
            <td class="no-split">La valeur à vie par utilisateur (Valeur à vie) dans ce segment et la valeur à vie par utilisateur payant dans ce segment. La Valeur à vie est calculée en divisant votre revenu à vie par les utilisateurs à vie.</td>
        </tr>
        <tr>
            <td class="no-split">E-mails (avec abonnement)</td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Emailable' %} En raison de la <a href="/docs/help/best_practices/spam_regulations/#spam-regulationsspam regulations">réglementation sur les spams</a>, il est conseillé de demander à vos utilisateurs d'accepter explicitement en mettant en œuvre une politique de double abonnement dans laquelle les utilisateurs doivent cliquer sur un lien dans un e-mail de confirmation initial. Pour encourager davantage d'utilisateurs à s'abonner, vous pouvez cibler un message destiné à <a href="/docs/user_guide/message_building_by_channel/email/managing_user_subscriptions/#segmenting-by-user-subscriptions">ceux qui n'ont pas choisi de s'abonner ou de se désabonner</a>.</td>
        </tr>
        <tr>
            <td class="no-split">Poussée activée (abonnement)</td>
            <td class="no-split">Notification push activée désigne le nombre d’utilisateurs avec au moins un jeton de notification push. Certains utilisateurs peuvent avoir plusieurs jetons push (par exemple, s'ils possèdent un iPhone et un iPad), de sorte que le nombre de notifications push que vous envoyez à ce segment peut être supérieur au nombre d'utilisateurs "push enabled". " Opted In " fait référence au nombre d'utilisateurs qui ont explicitement opté pour les notifications push. Les utilisateurs doivent toujours s’abonner explicitement pour recevoir des notifications push.</td>
        </tr>
    </tbody>
</table>

### Statistiques des segments

Vous pouvez voir les performances d'un segment par rapport à un autre en fonction d'un ensemble d'indicateurs clés de performance présélectionnés en vous rendant sur la page [Statistiques des segments de]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_insights/) votre tableau de bord.

### Utilisation des messages
La section **Utilisation des messages** indique les segments, les campagnes et les canevas actuellement activés qui ciblent votre segment.

![Dans Utilisation des messages, vous pouvez voir les campagnes qui utilisent votre segment.][4]

### Adhésion historique
La section **Historique de l'adhésion** montre comment la taille de votre segmentation a évolué dans le temps. Utilisez la liste déroulante pour filtrer l’appartenance au segment par plage de dates. 

Le nombre historique de membres du segment est une estimation, de la même manière que la taille du segment est une estimation avant que vous ne cliquiez sur **Calculer les statistiques exactes.** Braze estime le nombre de membres en interrogeant les utilisateurs dans un compartiment aléatoire. Cela signifie qu'un jour, le nombre de membres peut être basé sur des utilisateurs dont le numéro de compartiment aléatoire est compris entre 111 et 120, et un autre jour, sur des utilisateurs dont le numéro de compartiment aléatoire est compris entre 8 452 et 8 455. Par conséquent, le graphique peut présenter de légères fluctuations à chaque date en raison des différents nombres d'utilisateurs atterrissant dans les compartiments aléatoires.

![Utilisez la liste déroulante Historique des inscriptions pour filtrer l’appartenance au segment par plage de dates.][10]

### Aperçu de l’utilisateur

Pour afficher des informations détaillées et spécifiques à l'utilisateur sur vos segments, cliquez sur **Données utilisateur** et sélectionnez **Aperçu de l'utilisateur**.

![Informations spécifiques à l’utilisateur][7]

Sur cette page, vous pouvez afficher un certain nombre d’attributs spécifiques à l’utilisateur, tels que le sexe, l’âge, le nombre de sessions, et s’il accepte de recevoir des notifications push et des e-mails.

![Aperçu de l’utilisateur][8]

## Visualisation des données de performance par segment

Utilisez les [modèles de rapport de Query Builder]({{site.baseurl}}/user_guide/analytics/reporting/data_by_segments/) pour décomposer les indicateurs de performance des campagnes, Canvas, variantes et étapes par segments.

## Création d'un rapport de répartition des segments avec le générateur de rapports

Pour créer un rapport à partir d'un modèle du [générateur de requêtes]({{site.baseurl}}/user_guide/analytics/query_builder/), accédez au **générateur de requêtes** et procédez comme suit :

1. Sélectionnez **Créer une requête SQL** > **Modèle de requête.**
2. Filtrez les modèles pour ceux avec des indicateurs incluant des « répartitions de segments ».
3. Sélectionnez le modèle que vous souhaitez utiliser.
4. Remplissez les variables de votre modèle SQL dans l'onglet [Variables.](#variables) 
5. (Facultatif) Modifiez directement le code SQL dans le modèle.
6. Sélectionnez **Exécuter la requête**. Vos résultats s'affichent dans un tableau.

## Variables {#variables}

Avant de générer votre rapport, allez dans l'onglet **Variables** pour fournir des informations au générateur de rapports, y compris les variables requises qui varieront en fonction du rapport. 

![][11]

Les variables sont les suivantes

- **Campagne ou canvas :** Vous pouvez inclure une ou plusieurs campagnes ou canevas (il n'y a pas de maximum pour le nombre de campagnes ou de canevas que vous pouvez spécifier). Si vous n'indiquez aucune campagne ou Canvase, le rapport inclura toutes les campagnes ou Canvases de la période que vous avez choisie.
- **Variante :** Si vous utilisez un modèle qui propose une décomposition au niveau des variantes, après avoir sélectionné une campagne ou un Canvas, vous pouvez sélectionner des variantes au sein de cette campagne ou de ce Canvas. Si vous sélectionnez plusieurs variantes, vos résultats seront regroupés par variante.
- **Étape :** Si vous sélectionnez une variante du canvas, vous pouvez sélectionner une étape du canvas. Vous ne pouvez pas sélectionner une étape sans avoir au préalable sélectionné une variante du canvas. 
- **Intervalle de temps :** Identifiez la période dont vous souhaitez extraire les données. Si aucun intervalle de temps n'est spécifié, l'intervalle de temps sera par défaut les 30 derniers jours.
- **Nom du produit :** Si vous exécutez un rapport sur les données d'achat, vous pouvez identifier un produit spécifique pour lequel vous souhaitez obtenir des données.
- **Fenêtre de conversion :** Toujours requis pour les rapports contenant des données sur les chiffres d'affaires et les achats. Nombre de jours après la réception de l'e-mail ou le clic auquel Braze doit attribuer les achats ou les chiffres d'affaires.
- **Segments :** Identifiez les segments en fonction desquels ventiler les données. S'il n'est pas spécifié, le rapport sera exécuté pour tous les segments pour lesquels le suivi analytique est activé.
- **Tags :** Spécifiez des tags dans les **Variables** pour exécuter votre rapport pour toutes les campagnes ou les Canevas avec certains tags. Vous pouvez inclure plusieurs étiquettes. Si vous ajoutez à la fois des étiquettes et des campagnes ou canevas spécifiques à un rapport, celui-ci inclura les données de vos étiquettes et des campagnes ou canevas spécifiés. 

## Disponibilité des données

Les données sont disponibles pour les périodes où ces deux conditions sont remplies :

1. Le [suivi de l'analyse/analytique par segment]({{site.baseurl}}/user_guide/analytics/tracking/segment_analytics_tracking/) est activé pour les segments dont vous souhaitez consulter les données.
2. La fonctionnalité de données de performance par segment est activée.

Vous ne pouvez pas accéder aux données des périodes antérieures à l'activation de cette fonctionnalité pour votre entreprise. Par exemple, si le suivi analytique est activé pour le segment A le 1er octobre et que cette fonctionnalité est activée pour votre entreprise le 2 octobre, vous ne pourrez alors consulter les données du segment A que pour les campagnes et les Canevas qui ont enregistré des indicateurs après le 2 octobre. 

Si votre entreprise a activé cette fonctionnalité le 2 octobre et a activé le suivi analytique pour le segment B le 3 octobre, vous ne pourrez voir les données du segment B que pour les campagnes et les canevas qui ont enregistré des indicateurs après le 3 octobre.


[1]: {% image_buster /assets/img_archive/segments.png %}
[2]: {% image_buster /assets/img_archive/A_Tracking.png %}
[3]: {{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/#creating-a-segment
[4]: {% image_buster /assets/img_archive/historical_membership1.png %}
[5]: {{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#segmenting-by-user-subscriptions
[6]: {{site.baseurl}}/help/best_practices/spam_regulations/#spam-regulations
[7]: {% image_buster /assets/img_archive/preview_users.png %}
[8]: {% image_buster /assets/img_archive/user_preview.png %}
[9]: {{site.baseurl}}/user_guide/data_and_analytics/tracking/segment_analytics_tracking/
[10]: {% image_buster /assets/img_archive/historical_membership2.png %}
[11]:{% image_buster /assets/img_archive/variables_panel.png %}
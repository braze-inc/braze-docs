---
nav_title: Générateur de tableaux de bord
article_title: Générateur de tableaux de bord
alias: "/dashboard_builder/"
description: "Cet article de référence explique comment utiliser Dashboard Builder pour créer des tableaux de bord et des visualisations à partir de rapports créés dans Query Builder."
page_type: reference
tool:
    - Reports
page_order: 6.1
---

# Générateur de tableaux de bord

> Utilisez Dashboard Builder pour créer des tableaux de bord et des visualisations à partir des rapports créés dans Report Builder ou Query Builder.

Dashboard Builder vous permet de créer et de visualiser des tableaux de bord analytiques personnalisés à partir de zéro et à partir des tableaux de bord fournis par Braze. Vous pouvez utiliser soit un générateur de rapports (Report Builder), soit une source de données SQL (Query Builder) pour alimenter votre tableau de bord, ou bien commencer à partir de l'un des nombreux tableaux de bord fournis par Braze.

## Création d'un tableau de bord personnalisé

1. Allez dans **Analyse/analytique** > **Générateur de tableau de bord (si vous utilisez un tableau adjectif**).
2. Sélectionnez **Créer un tableau de bord**.
3. Sélectionnez la source de données qui alimentera vos rapports :
- **Les rapports** qui ont été créés dans le générateur de rapports
- Les **requêtes personnalisées** qui ont été créées dans Query Builder<br><br>![Fenêtre permettant de sélectionner la source de données pour votre tableau de bord.]({% image_buster /assets/img/select_data_source.png %})<br><br>

Maintenant, suivez les étapes respectives pour votre source de données :

{% tabs %}
{% tab Reports %}

{: start="4"}
4\. Sélectionnez **\+ Ajouter une tuile**, puis choisissez l'un des rapports que vous avez créés dans le [générateur de rapports (Nouveau)]({{site.baseurl}}/user_guide/analytics/reporting/report_builder/).

{% alert important %}
Une fois qu'un rapport du générateur de rapports est ajouté à une vignette du générateur de tableaux de bord, la vignette n'est plus connectée au rapport d'origine. Si vous modifiez le rapport d'origine dans le générateur de rapports, il est nécessaire de supprimer la vignette existante du tableau de bord et d'en créer une nouvelle en utilisant le rapport mis à jour comme source de données.
{% endalert %}

{: start="5"}
5\. Sélectionnez l'icône du crayon pour modifier l'affichage du titre et du type de graphique dans la tuile.
    \- Vous pouvez basculer entre différents types de graphiques sous la visualisation par défaut. Les options actuelles comprennent les diagrammes à barres (horizontaux ou verticaux) et les diagrammes linéaires (disponibles uniquement si vous avez sélectionné **Date** comme option de recherche dans la configuration du générateur de rapports).<br><br>![Basculation pour sélectionner différents types de graphiques.]({% image_buster /assets/img/report_builder_types.png %})<br><br>
    \- Utilisez le menu déroulant des indicateurs pour sélectionner les indicateurs à inclure dans votre visualisation. Par défaut, la première colonne du rapport sera la mesure affichée par défaut.
6\. Sélectionnez **Enregistrer** après avoir modifié la visualisation à votre convenance.
7\. Ajoutez un nom, une description et une étiquette pour faciliter la recherche ultérieure de votre tableau de bord.
{% endtab %}
{% tab Custom Queries %}
{: start="4"}
4\. Sélectionnez **\+ Ajouter une tuile**, puis choisissez une requête que vous avez exécutée dans Query Builder.
5\. Pour modifier l'affichage des résultats de la requête dans la tuile, sélectionnez l'icône en forme de crayon pour changer le titre et le type de graphique.
    \- Vous pouvez basculer entre différents types de graphiques sous la visualisation par défaut. Les options actuelles comprennent les tableaux, les diagrammes à barres (horizontaux ou verticaux) et les diagrammes linéaires.<br><br>![Basculation pour sélectionner différents types de graphiques.]({% image_buster /assets/img/query_builder_types.png %})<br><br>
        \- Si vous sélectionnez l'une des options de graphique, veuillez utiliser le menu déroulant **de l'axe X** pour sélectionner une seule colonne parmi les résultats de votre requête à utiliser comme axe X.
        \- Utilisez le menu déroulant de **l'axe des Y** pour sélectionner les indicateurs à inclure dans votre visualisation. Par défaut, toutes les colonnes des résultats de votre requête s'affichent, désélectionnez donc les colonnes qui ne vous intéressent pas.<br><br>![Basculation pour sélectionner différents types de graphiques.]({% image_buster /assets/img/query_builder_axis.png %})<br><br>
        \- (Facultatif) Vous pouvez utiliser la liste déroulante **Groupement** pour regrouper les résultats de votre requête. Par exemple, si vous avez l'ID de la campagne comme résultat d'une colonne et que vous souhaitez additionner toutes les lignes ayant cette valeur, utilisez le menu déroulant **Regroupement**.  
        \- (Facultatif) Pour modifier les données affichées, sélectionnez la requête associée au visuel et effectuez vos modifications dans [Query Builder]({{site.baseurl}}/user_guide/analytics/query_builder/).
6\. Sélectionnez **Enregistrer** après avoir modifié la visualisation à votre convenance.
7\. Ajoutez un nom, une description et une étiquette pour faciliter la recherche ultérieure de votre tableau de bord.
{% endtab %}
{% endtabs %}

{: start="8"}
8\. Répétez les étapes 4 à 7 pour votre méthode respective jusqu'à ce que vous ayez créé le tableau de bord souhaité.
9\. Sélectionnez **View Dashboard** > sélectionnez **Run Dashboard**. 

Votre tableau de bord peut prendre jusqu'à quelques minutes pour finir de générer des rapports.

{% alert note %}
Vous pouvez ajouter jusqu'à 10 tuiles à un tableau de bord.
{% endalert %}

## Gestion des tuiles du tableau de bord

### Supprimer des tuiles

Supprimez une tuile du tableau de bord en sélectionnant **Supprimer la tuile** en bas de la tuile. **Cette action ne peut pas être annulée.**

### Dalles en double

Faites une copie de votre tuile en sélectionnant **Dupliquer la tuile** en bas de la tuile.

### Adjust tile size and position (Ajuster la taille et la position des carreaux)

Veuillez ajuster la taille de la vignette en faisant glisser son coin inférieur droit, et ajustez sa position sur le tableau de bord en faisant glisser la poignée située dans son coin supérieur droit.

## Exécution d'un tableau de bord

1. Allez dans **Analyse/analytique** > **Générateur de tableau de bord (si vous utilisez un tableau adjectif**). La page d'accueil répertorie tous les tableaux de bord existants dans votre espace de travail, les tableaux de bord créés par Braze apparaissant en haut de la liste. Ils sont signalés par la mention « (Braze) » dans le titre.
2. Sélectionnez le tableau de bord qui vous intéresse.
3. Veuillez sélectionner **« Exécuter le tableau de bord** » pour charger le tableau de bord correspondant à l'aide de ce tableau de bord.

### Tableaux de bord disponibles

Braze propose des tableaux de bord prédéfinis pour les cas d'utilisation fréquents, tels que l'analyse du chiffre d'affaires à l'aide de l'attribution au dernier contact. Veuillez noter que la fonctionnalité permettant de modifier un tableau de bord n'est pas encore disponible. Veuillez contacter votre gestionnaire de la satisfaction client si vous souhaitez consulter un tableau de bord spécifique à l'avenir.

#### Revenus - Attribution au dernier contact

Le tableau de bord **«** **Chiffre d'affaires - Attribution au dernier point de contact** » fournit un aperçu du chiffre d'affaires généré par les campagnes, les canevas et les canaux. Toutes les données relatives aux revenus sont attribuées au message du dernier contact pendant la fenêtre d'attribution.

Les interactions comprennent _les clics sur les e-mails_ (clics sur les liens), _les clics sur les cartes de contenu_, _les clics sur les messages in-app_ (à l'exception des boutons de fermeture), _les ouvertures de notifications push_, _les clics sur les liens courts dans les SMS_, _les lectures WhatsApp_ et _les envois de webhooks_.

| Indicateurs | Définition |
| --- | --- |
| Revenus totaux au dernier contact | Somme de toutes les campagnes et de tous les chiffres d'affaires Canvas avec un événement de dernière touche dans la plage de dates et la fenêtre d'attribution sélectionnées. |
| Total des conversions d'achat | Somme de tous les événements de revenus de campagnes et de canvas avec un événement qualifiant de dernier contact. |
| Nombre moyen de jours de conversion | Le temps moyen entre tous les événements d'achat de la campagne et de la toile avec un événement de dernière touche qualifiant. |
| Revenu par destinataire | Somme des chiffres d'affaires des événements qualifiés divisée par le nombre d'utilisateurs uniques ayant reçu un message dans la plage de dates. |
| Acheteurs uniques | Nombre d'utilisateurs uniques pour lesquels un événement de revenus a été validé. |
| Chiffre d'affaires par pays | Somme de tous les événements de revenus de campagnes et de canvas avec un événement de dernier contact, regroupés par pays. |
| Revenus par campagne | Somme de toutes les affaires de campagne et de chiffre d'affaires Canvas avec un événement de dernière touche qualifiant, regroupées par campagne. |
| Revenus par variante de campagne | Somme de toutes les campagnes et de tous les chiffres d'affaires Canvas avec un événement de dernière touche qualifiant, regroupés par variante de campagne. |
| Revenus par canvas | Somme de tous les chiffres d'affaires de la campagne et du Canvas avec un événement de dernière touche qualifiant, regroupés par Canvas. |
| Revenus par variante du canvas | Somme de toutes les campagnes et de tous les événements de revenus Canvas avec un événement de dernière touche qualifiant, regroupés par variante Canvas. |
| Achats par produit | Décompte de tous les achats regroupés par produit. |
| Chiffre d'affaires par canal | Somme de toutes les affaires de chiffre d'affaires de la campagne et du Canvas avec un événement de dernière touche qualifiant, regroupées par canal. | 
| Série chronologique des chiffres d'affaires | Somme de tous les chiffres d'affaires de la campagne et du Canvas avec un événement de dernière touche qualifiant, regroupés par jour en UTC. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Appareils et opérateurs

| Indicateurs | Définition |
| --- | --- |
| Opérateurs d'appareils | Nombre d'utilisateurs dans la plage de dates sélectionnée qui ont ouvert une notification push, regroupés par transporteur d'appareil. |
| Modèle de l’appareil | Nombre d'utilisateurs dans la plage de dates sélectionnée qui ont ouvert une notification push, regroupés par modèle d'appareil. |
| Système d’exploitation de l’appareil | Nombre d'utilisateurs dans la plage de dates sélectionnée qui ont ouvert une notification push, regroupés par système d'exploitation de l'appareil. |
| Taille de l'écran de l'appareil | Nombre d'utilisateurs dans la plage de dates sélectionnée qui ont ouvert une notification push, regroupés par résolution d'écran (taille) de l'appareil. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Statistiques des segments - E-mail

| Indicateurs  | Définition  |
|---|---|
| Indicateurs hebdomadaires relatifs aux e-mails (taux) | Taux d'engagement par e-mail (taux de réception/distribution, de rebond, d'ouverture, de clics et de désabonnement) regroupés par segment et affichés sous forme de séries chronologiques hebdomadaires.|
| Indicateurs hebdomadaires relatifs aux e-mails (nombre) | Nombre d'interactions par e-mail (envoyés, livrés, rebonds, ouvertures, clics, désabonnements) regroupées par segment et affichées sous forme de séries chronologiques hebdomadaires.|
| Indicateurs hebdomadaires d'achat (taux) | Taux de conversion des achats (chiffre d'affaires par destinataire) à partir des ouvertures et des clics sur les e-mails, regroupés par segment et affichés sous forme de série chronologique hebdomadaire.|
| Indicateurs hebdomadaires d'achat (nombre) | Nombre d'achats et chiffres d'affaires totaux générés par les ouvertures et les clics sur les e-mails, regroupés par segment et affichés sous forme de série chronologique hebdomadaire.|
| Engagement par e-mail par segment | Tableau récapitulatif présentant les indicateurs globaux d'engagement par e-mail (envois, livraisons, rebonds, ouvertures, clics, désabonnements et leurs taux) regroupés par segment.|
| Achats&  Chiffre d'affaires par segment | Tableau récapitulatif présentant les indicateurs d'achat totaux (achats, chiffre d'affaires et chiffre d'affaires par destinataire) à partir des ouvertures et des clics sur les e-mails, agrégés par segment.|
| Les 10 meilleures campagnes en termes d'indicateurs d'engagement | Liste classée des campagnes présentant les indicateurs d'engagement par e-mail les plus élevés (indicateur configurable pour le classement).|
| Les 10 campagnes les moins performantes en termes d'indicateurs d'engagement | Liste classée des campagnes présentant les indicateurs d'engagement par e-mail les plus faibles (indicateur configurable pour le classement).|
| Les 10 meilleures toiles pour les indicateurs d'engagement | Liste classée des toiles présentant les indicateurs d'engagement par e-mail les plus élevés (indicateur configurable pour le classement).|
| Les 10 canevas les moins performants en termes d'indicateurs d'engagement | Liste classée des toiles présentant les indicateurs d'engagement par e-mail les plus faibles (indicateur configurable pour le classement).|
| Les 10 meilleures campagnes pour les indicateurs d'achat | Liste classée des campagnes présentant les indicateurs de conversion d'achat les plus élevés à partir de l'engagement par e-mail (indicateur configurable pour le classement).|
| Les 10 campagnes les moins performantes en termes d'indicateurs d'achat | Liste classée des campagnes présentant les indicateurs de conversion d'achat les plus faibles à partir de l'engagement par e-mail (indicateur configurable pour le classement).|
| Les 10 meilleures toiles à acquérir - Indicateurs | Liste classée des toiles présentant les meilleurs indicateurs de conversion d'achat à partir de l'engagement par e-mail (indicateur configurable pour le classement).|
| Les 10 toiles les moins vendues en termes d'indicateurs | Liste classée des toiles présentant les indicateurs de conversion d'achat les plus faibles à partir de l'engagement par e-mail (indicateur configurable pour le classement).|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Analyse des sessions

| Indicateurs | Définition  |
|---|---|
| Nombre de sessions par jour (série chronologique) | Nombre de sessions uniques regroupées par jour dans la plage de dates sélectionnée, affichées sous forme de série chronologique.|
| Nombre moyen de sessions par utilisateur | Nombre moyen de sessions par utilisateur calculé en divisant le nombre total de sessions par le nombre d'utilisateurs uniques au cours de la période sélectionnée.|
| Les campagnes se transforment en sessions | Nombre de sessions uniques qui se sont produites en même temps que les conversions de campagne, regroupées par ID de campagne et classées par nombre de sessions.|
| Les toiles se transforment en séances | Nombre de sessions uniques qui ont eu lieu en même temps que les conversions Canvas, regroupées par ID de canvas et classées par nombre de sessions.|
| Nombre total de sessions par utilisateur | Liste des 1 000 utilisateurs ayant enregistré le plus grand nombre de sessions au cours de la période sélectionnée.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Faites-nous part de vos commentaires

Sélectionnez le bouton **Envoyer un commentaire** ou contactez votre gestionnaire de satisfaction client pour nous faire part de votre commentaire.


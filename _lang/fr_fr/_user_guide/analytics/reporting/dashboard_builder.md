---
nav_title: Générateur de tableau de bord
article_title: Générateur de tableau de bord
alias: "/dashboard_builder/"
description: "Cet article de référence explique comment utiliser Dashboard Builder pour créer des tableaux de bord et des visualisations à partir de rapports créés dans Query Builder."
page_type: reference
tool:
    - Reports
page_order: 6.1
---

# Générateur de tableau de bord

> Utilisez Dashboard Builder pour créer des tableaux de bord et des visualisations à partir des rapports créés dans Report Builder ou Query Builder.

Dashboard Builder vous permet de composer et de visualiser des tableaux de bord analytiques personnalisés (à partir de zéro ou de tableaux de bord fournis par Braze). Vous pouvez utiliser une source de données sans code (Report Builder) ou une source de données SQL (Query Builder) pour alimenter votre tableau de bord, ou partir d'un des nombreux tableaux de bord fournis par Braze.

## Création d'un tableau de bord personnalisé

1. Allez dans **Analyse/analytique** > **Générateur de tableau de bord (si vous utilisez un tableau adjectif**).
2. Sélectionnez **Créer un tableau de bord**.
3. Sélectionnez la source de données qui alimentera vos rapports :
- **Les rapports** qui ont été créés dans le générateur de rapports
- Les **requêtes personnalisées** qui ont été créées dans Query Builder<br><br>\![Fenêtre de sélection de la source de données pour votre tableau de bord.]({% image_buster /assets/img/select_data_source.png %})<br><br>

Maintenant, suivez les étapes respectives pour votre source de données :

{% tabs %}
{% tab Reports %}

{: start="4"}
4\. Sélectionnez **\+ Ajouter une tuile**, puis choisissez l'un des rapports que vous avez créés dans le [générateur de rapports (Nouveau)]({{site.baseurl}}/user_guide/analytics/reporting/report_builder/).
5\. Sélectionnez l'icône du crayon pour modifier l'affichage du titre et du type de graphique dans la tuile.
    \- Vous pouvez basculer entre différents types de graphiques sous la visualisation par défaut. Les options actuelles comprennent les diagrammes à barres (horizontaux ou verticaux) et les diagrammes linéaires (disponibles uniquement si vous avez sélectionné **Date** comme option de recherche dans la configuration du générateur de rapports).<br><br>\![Bascule pour différents types de graphiques.]({% image_buster /assets/img/report_builder_types.png %})<br><br>
    \- Utilisez le menu déroulant des indicateurs pour sélectionner les indicateurs à inclure dans votre visualisation. Par défaut, la première colonne du rapport sera la mesure affichée par défaut.
6\. Sélectionnez **Enregistrer** après avoir modifié la visualisation à votre convenance.
7\. Ajoutez un nom, une description et une étiquette pour faciliter la recherche ultérieure de votre tableau de bord.
{% endtab %}
{% tab Custom Queries %}
{: start="4"}
4\. Sélectionnez **\+ Ajouter une tuile**, puis choisissez une requête que vous avez exécutée dans Query Builder.
5\. Pour modifier l'affichage des résultats de la requête dans la tuile, sélectionnez l'icône en forme de crayon pour changer le titre et le type de graphique.
    \- Vous pouvez basculer entre différents types de graphiques sous la visualisation par défaut. Les options actuelles comprennent les tableaux, les diagrammes à barres (horizontaux ou verticaux) et les diagrammes linéaires.<br><br>\![Bascule pour différents types de graphiques.]({% image_buster /assets/img/query_builder_types.png %})<br><br>
        \- Si vous choisissez l'une des options de graphique, utilisez le menu déroulant de l **'axe des X** pour sélectionner une seule colonne des résultats de votre requête à utiliser comme axe des x.
        \- Utilisez le menu déroulant de **l'axe des Y** pour sélectionner les indicateurs à inclure dans votre visualisation. Par défaut, toutes les colonnes des résultats de votre requête s'affichent, désélectionnez donc les colonnes qui ne vous intéressent pas.<br><br>\![Bascule pour différents types de graphiques.]({% image_buster /assets/img/query_builder_axis.png %})<br><br>
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

Ajustez la taille de la tuile en faisant glisser le coin inférieur droit de la tuile, et ajustez la position de la tuile sur le tableau de bord en faisant glisser la poignée située dans le coin supérieur droit de la tuile.

## Exécution d'un tableau de bord

1. Allez dans **Analyse/analytique** > **Générateur de tableau de bord (si vous utilisez un tableau adjectif**). La page d'accueil répertorie tous les tableaux de bord existants dans votre espace de travail, les tableaux de bord créés par Braze figurant en haut de la page. Ils sont signalés par la mention "(Braze)" dans le titre.
2. Sélectionnez le tableau de bord qui vous intéresse.
3. Sélectionnez **Exécuter le tableau** de bord pour charger le tableau de bord correspondant à l'aide de ce tableau de bord.

### Tableaux de bord disponibles

Braze propose des tableaux de bord préconstruits pour les cas d'utilisation fréquents, tels que l'analyse des chiffres d'affaires à l'aide de l'attribution de la dernière touche. Notez que la possibilité de modifier un tableau de bord n'est pas encore disponible. Contactez votre gestionnaire de satisfaction client si vous souhaitez voir apparaître certains tableaux de bord à l'avenir.

#### Chiffre d'affaires - Attribution de la dernière touche

Le tableau de bord **Revenu - Attribution de la dernière touche** permet d'examiner le chiffre d'affaires à travers les campagnes, les Canvas et les canaux. Toutes les données relatives aux affaires sont attribuées au dernier message touché pendant la fenêtre d'attribution.

Les touches comprennent le _clic sur l'e-mail_ (clic sur le lien), le clic _sur la carte de contenu_, le _clic sur le message in-app_ (à l'exception des boutons de fermeture), les _ouvertures push_, le _clic sur le lien court SMS_, la _lecture WhatsApp_ et l'_envoi webhook_.

| Indicateurs | Définition |
| --- | --- |
| Chiffre d'affaires total de la dernière touche | Somme de toutes les campagnes et de tous les chiffres d'affaires Canvas avec un événement de dernière touche dans la plage de dates et la fenêtre d'attribution sélectionnées. |
| Total des conversions d'achat | Un compte de toutes les affaires de campagne et de chiffre d'affaires Canvas avec un événement de dernière touche qualifiant. |
| Nombre moyen de jours de conversion | Le temps moyen entre tous les événements d'achat de la campagne et de la toile avec un événement de dernière touche qualifiant. |
| Chiffre d'affaires par destinataire | Somme des chiffres d'affaires des événements qualifiés divisée par le nombre d'utilisateurs uniques ayant reçu un message dans la plage de dates. |
| Acheteurs uniques | Nombre d'utilisateurs uniques pour lesquels un chiffre d'affaires a été enregistré. |
| Chiffre d'affaires par pays | Somme de toutes les affaires de campagne et de chiffre d'affaires Canvas avec un événement de dernière touche, regroupées par pays. |
| Chiffre d'affaires par campagne | Somme de toutes les affaires de campagne et de chiffre d'affaires Canvas avec un événement de dernière touche qualifiant, regroupées par campagne. |
| Chiffre d'affaires par variante de campagne | Somme de toutes les campagnes et de tous les chiffres d'affaires Canvas avec un événement de dernière touche qualifiant, regroupés par variante de campagne. |
| Chiffre d'affaires par canvas | Somme de tous les chiffres d'affaires de la campagne et du Canvas avec un événement de dernière touche qualifiant, regroupés par Canvas. |
| Chiffre d'affaires par variante du canvas | Somme de toutes les campagnes et de tous les événements de revenus Canvas avec un événement de dernière touche qualifiant, regroupés par variante Canvas. |
| Achats par produit | Un décompte de tous les achats regroupés par produit. |
| Chiffre d'affaires par canal | Somme de toutes les affaires de chiffre d'affaires de la campagne et du Canvas avec un événement de dernière touche qualifiant, regroupées par canal. | 
| Série chronologique des chiffres d'affaires | Somme de tous les chiffres d'affaires de la campagne et du Canvas avec un événement de dernière touche qualifiant, regroupés par jour en UTC. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Appareils et supports

| Indicateurs | Définition |
| --- | --- |
| Porteurs d'appareils | Nombre d'utilisateurs dans la plage de dates sélectionnée qui ont ouvert une notification push, regroupés par transporteur d'appareil. |
| Modèle d'appareil | Nombre d'utilisateurs dans la plage de dates sélectionnée qui ont ouvert une notification push, regroupés par modèle d'appareil. |
| Système d'exploitation de l'appareil | Nombre d'utilisateurs dans la plage de dates sélectionnée qui ont ouvert une notification push, regroupés par système d'exploitation de l'appareil. |
| Taille de l'écran de l'appareil | Nombre d'utilisateurs dans la plage de dates sélectionnée qui ont ouvert une notification push, regroupés par résolution d'écran (taille) de l'appareil. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Statistiques des segments - e-mail

| Indicateurs  | Définition  |
|---|---|
| Indicateurs hebdomadaires des e-mails (taux) | Taux d'engagement des e-mails (taux de réception/distribution, de rebond, d'ouverture, de clics, de désabonnement) regroupés par segment et affichés sous forme de séries chronologiques hebdomadaires.|
| Indicateurs des e-mails hebdomadaires (nombre) | Comptes d'engagement par e-mail (envoyés, délivrés, rebonds, ouvertures, clics, désabonnements) regroupés par segment et affichés sous forme de séries chronologiques hebdomadaires.|
| Indicateurs d'achats hebdomadaires (taux) | Taux de conversion des achats (chiffre d'affaires par destinataire) à partir des ouvertures et des clics sur les e-mails, regroupés par segment et affichés sous la forme d'une série chronologique hebdomadaire.|
| Indicateurs d'achats hebdomadaires (nombre) | Nombre d'achats et total des chiffres d'affaires provenant des ouvertures et des clics sur les e-mails, regroupés par segment et affichés sous forme de séries chronologiques hebdomadaires.|
| Engagement par e-mail par segmentation | Tableau récapitulatif des indicateurs d'engagement des e-mails (envoyés, livrés, rebonds, ouvertures, clics, désabonnements et leurs taux) agrégés par segment.|
| Achats & Chiffre d'affaires par segment | Tableau récapitulatif des indicateurs d'achat totaux (achats, chiffre d'affaires et chiffre d'affaires par destinataire) provenant des ouvertures et des clics d'e-mails, agrégés par segmentation.|
| Les 10 meilleures campagnes pour les indicateurs d'engagement | Liste classée des campagnes ayant les indicateurs d'engagement par e-mail les plus élevés (métrique configurable pour le classement).|
| Les 10 campagnes les moins performantes en termes d'indicateurs d'engagement | Liste classée des campagnes dont les indicateurs d'engagement par e-mail sont les plus bas (métrique configurable pour le classement).|
| Les 10 meilleures toiles pour les indicateurs d'engagement | Liste classée des Canevas ayant les indicateurs d'engagement par e-mail les plus élevés (métrique configurable pour le classement).|
| Les 10 canevas les moins performants en termes d'indicateurs d'engagement | Liste classée des Canevas ayant les indicateurs d'engagement par e-mail les plus bas (métrique configurable pour le classement).|
| Les 10 meilleures campagnes pour les indicateurs d'achat | Liste classée des campagnes ayant les indicateurs de conversion d'achat les plus élevés grâce à l'engagement par e-mail (métrique configurable pour le classement).|
| Les 10 campagnes les moins performantes en termes d'indicateurs d'achat | Liste classée des campagnes ayant les indicateurs de conversion d'achat les plus bas à partir de l'engagement par e-mail (métrique configurable pour le classement).|
| Les 10 meilleurs canevas pour les indicateurs d'achat | Liste classée des toiles ayant les indicateurs de conversion d'achat les plus élevés grâce à l'engagement par e-mail (métrique configurable pour le classement).|
| Les 10 canevas les moins performants en termes d'indicateurs d'achat | Liste classée des Canvases ayant les indicateurs de conversion d'achat les plus bas à partir de l'engagement par e-mail (métrique configurable pour le classement).|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Analyse/analytique de la session (si utilisée comme adjective)

| Indicateurs | Définition  |
|---|---|
| \# Nombre de sessions par jour (série chronologique) | Nombre de sessions uniques regroupées par jour dans la plage de dates sélectionnée, affiché sous forme de série chronologique.|
| Nombre moyen de sessions par utilisateur | Nombre moyen de sessions par utilisateur calculé comme le nombre total de sessions divisé par le nombre d'utilisateurs uniques dans la plage de dates sélectionnée.|
| Les campagnes se transforment en sessions | Nombre de sessions uniques survenues en même temps que les conversions de la campagne, regroupées par ID de campagne et classées par nombre de sessions.|
| Les toiles se transforment en sessions | Nombre de sessions uniques qui se sont produites en même temps que les conversions Canvas, regroupées par ID Canvas et classées par nombre de sessions.|
| Nombre total de sessions par utilisateur | Liste des 1 000 premiers utilisateurs en fonction du nombre total de sessions dans la plage de dates sélectionnée.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Faites-nous part de vos commentaires

Sélectionnez le bouton **Envoyer un commentaire** ou contactez votre gestionnaire de satisfaction client pour nous faire part de votre commentaire.


---
nav_title: Générateur de tableaux de bord
article_title: Générateur de tableaux de bord
permalink: "/dashboard_builder/"
description: "Cet article de référence explique comment utiliser Dashboard Builder pour créer des tableaux de bord et des visualisations à partir de rapports créés dans Query Builder."
page_type: reference
hidden: true
---

# Générateur de tableaux de bord

> Utilisez Dashboard Builder pour créer des tableaux de bord et des visualisations à partir des rapports créés dans Query Builder. Vous pouvez commencer par utiliser les modèles de requêtes SQL préconstruits dans Query Builder ou écrire vos propres requêtes SQL personnalisées pour obtenir encore plus d'informations.

Braze propose des modèles prédéfinis de tableau de bord pour les cas d'utilisation fréquents, tels que l'analyse des revenus à l'aide de l'attribution au dernier contact. Notez que la possibilité de modifier un tableau de bord modèle n'est pas encore disponible.

{% alert note %}
Le générateur de tableau de bord est actuellement en accès anticipé. Si vous souhaitez participer à cet accès anticipé, contactez votre gestionnaire de la satisfaction client.
{% endalert %}

## Exécution d'un modèle de tableau de bord

1. Allez dans **Analyse/analytique** > **Générateur de tableau de bord (si vous utilisez un tableau adjectif**). La page d'accueil répertorie tous les tableaux de bord existants dans votre espace de travail, les modèles créés par Braze figurant en haut de la page. Ils sont signalés par la mention « (Braze) » dans le titre.
2. Sélectionnez le tableau de bord qui vous intéresse.
3. Sélectionnez **Exécuter le tableau de bord** pour générer un tableau de bord à l'aide de ce modèle.

### Modèles de tableaux de bord disponibles

#### Revenus - Attribution au dernier contact

Le modèle **Revenus - Attribution au dernier contact** permet d'examiner les revenus pour l’ensemble des campagnes, des canvas et des canaux. Toutes les données relatives aux revenus sont attribuées au message du dernier contact pendant la fenêtre d'attribution.

Ces contacts incluent : `Email Click`, `Content Card Click`, `In-App Message Click`, `SMS Delivery`, `WhatsApp Read` et `Webhook Send`.

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

## Création d'un tableau de bord personnalisé

1. Sélectionnez **Créer un tableau de bord**, ou un tableau de bord existant et **Modifier**. Sélectionnez ensuite **\+ Ajouter une tuile.**
2. Sélectionnez **Sélectionner une requête existante** et choisissez une requête que vous avez exécutée dans le générateur de requêtes (Query Builder).
3. Pour modifier l'affichage des résultats de la requête dans la tuile, sélectionnez l'icône en forme de crayon pour changer le titre et le type de graphique.<br><br>![Vue de l'éditeur de tuiles avec des options permettant de modifier le titre et le type de graphique.][2]{: style="max-width:60%;"}<br><br>
    - Si vous sélectionnez un type de graphique ( **colonne**, **barre** ou **ligne**) :
        - Sélectionnez un champ de la requête à utiliser pour l'axe des X.
        - Désélectionnez les colonnes qui ne vous intéressent pas.<br><br>![Liste déroulante avec les types de graphiques.][1]{: style="max-width:40%;"}

{: start="4"}        
4\. Veillez à enregistrer vos modifications. Si vous souhaitez supprimer la vignette, sélectionnez l'icône de la corbeille. Les tuiles supprimées ne peuvent pas être annulées et doivent être recréées.
5\. Ajustez la taille de la tuile en faisant glisser le coin inférieur droit et la position de la tuile sur le bord en faisant glisser la poignée située dans le coin supérieur droit.<br><br>![Vignette tirée par la poignée.][3]<br><br>
6\. Ajoutez des tuiles supplémentaires jusqu'à ce que votre tableau de bord soit complet.
7\. Sélectionnez **Afficher le tableau de bord**, puis sélectionnez **Exécuter le tableau de bord**. La génération de rapports depuis votre tableau de bord peut prendre plusieurs minutes.

## Faites-nous part de vos commentaires

N'hésitez pas à nous faire part de vos commentaires en contactant votre gestionnaire de la satisfaction client ou en répondant à l'e-mail d'habilitation que vous avez reçu.

[1]: {% image_buster /assets/img/chart_type.png %}
[2]: {% image_buster /assets/img/sample_tile.png %}
[3]: {% image_buster /assets/img/drag_tile.png %}

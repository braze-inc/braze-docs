---
nav_title: Indicateurs par segmentation
article_title: Indicateurs par segmentation
page_order: 2.5
page_type: reference
description: "Cette page décrit comment vous pouvez utiliser les modèles de rapport de Query Builder pour décomposer les indicateurs de performance des campagnes, Canvas, variantes et étapes par segments."
tool: 
  - Segments
  - Reports
  
---

# Indicateurs par segments

> Utilisez les modèles de rapport de [Query Builder]({{site.baseurl}}/user_guide/analytics/query_builder/) pour décomposer les indicateurs de performance des campagnes, Canvas, variantes et étapes par segments.

Le [suivi analytique]({{site.baseurl}}/user_guide/data_and_analytics/tracking/segment_analytics_tracking#segment-analytics-tracking) doit être activé pour les segments pour lesquels vous souhaitez accéder aux indicateurs.

Pour exécuter ces rapports, procédez comme suit :
1. Dans le **générateur de requêtes**, choisissez de créer un nouveau rapport SQL avec un modèle. 
2. Sélectionnez **Segment breakdowns** for the metric, ce qui permet de filtrer les modèles pour ceux dont les indicateurs incluent des ventilations de segment, à savoir
- Indicateurs de performance de l'e-mail par segmentation
- Indicateurs d'engagement par e-mail pour les variantes ou les étapes, par segmentation.
- Achats et revenus par segment
- Achats et revenus par segment, pour les différentes variantes ou étapes
- Performance des notifications push par segment

![La page de répartition des segments contient un éditeur SQL, un panneau latéral avec des onglets pour les variables, les tables de données disponibles, l'historique des requêtes et le générateur de requêtes basé sur l’IA, ainsi qu'une section de résultats.]({% image_buster /assets/img_archive/segment_breakdown.png %})

## Modèles de rapport

{% tabs %}
{% tab Indicateurs d'engagement par e-mail par segment %}

### Visualisation des indicateurs pour les campagnes ou les canevas {#campaign-canvas-email}

Pour afficher les indicateurs de performance des e-mails ventilés par segment au niveau de la campagne ou du Canvas, utilisez l'onglet [Variables](#variables) pour spécifier les campagnes ou Canvas et une période de temps pour l'extraction des données. Si aucune campagne ni aucun canvas n'est spécifié, le rapport inclura les e-mails de toutes les campagnes et de tous les canvas de la période spécifiée. Vous pouvez également opter pour l'affichage de toutes les campagnes et de toutes les toiles avec certains tags.

Les indicateurs d'e-mail suivants sont disponibles dans ce rapport :
- Envois
- Réceptions
- Plaintes
- Ouverture unique
- Ouvertures automatiques uniques
- Ouvertures non automatiques uniques
- Clics uniques
- Se désabonne
- Rebonds
- Soft bounces
- Différés

#### Résultats

Vos résultats afficheront les indicateurs d'engagement par e-mail par segment pour les campagnes ou les Canevas que vous avez sélectionnés. Si vous n'avez pas sélectionné de campagnes ou de canevas spécifiques, votre rapport affichera les indicateurs d'e-mail pour chaque segment sur l'ensemble des campagnes et canevas d'e-mail dans la période de votre rapport. 

- **Rangs :** Segments
- **Colonnes :** Indicateurs d'engagement par e-mail

### Visualisation des indicateurs pour les variantes ou les étapes

Pour afficher les performances des e-mails ventilées par segment au niveau de la variante de la campagne, de la variante du canevas ou de l'étape du canevas, choisissez d'abord un rapport au niveau de la variante ou de l'étape (il s'agit des rapports dont le titre contient "pour les variantes ou les étapes"), puis utilisez l'onglet **Variables** pour spécifier les éléments suivants :

- Campagne ou Canvas spécifique (obligatoire si vous utilisez un rapport de variante ou d'étape du canvas) 
- Variantes (obligatoire si vous utilisez un rapport de variante ou de niveau d'étape)
- Étape du canvas (facultatif)

Les indicateurs sont les mêmes que ceux proposés pour le modèle de [niveau campagne ou Canvas.](#campaign-canvas-email)  Si vous choisissez plusieurs variantes, vos résultats seront regroupés par variante.

#### Résultats

Vos résultats montreront les indicateurs d'engagement par e-mail par segment pour vos variantes ou étapes sélectionnées. 

- **Rangs :** Segments
- **Colonnes :** Indicateurs d'engagement par e-mail

{% endtab %}

{% tab Achats et chiffres d'affaires par segment %}
### Visualisation des indicateurs pour les campagnes ou les canevas

Pour afficher les indicateurs d'achats et d'affaires ventilés par segment pour une campagne ou un Canvas spécifique, utilisez l'onglet [Variables](#variables) pour spécifier les éléments suivants :

- Fenêtre de conversion (le nombre de jours après la réception de l'e-mail ou le clic auquel Braze doit attribuer les achats ou les revenus)
- Produit spécifique (facultatif) 

En outre, utilisez l'onglet **Variables** pour indiquer si le rapport doit être exécuté pour une ou plusieurs campagnes ou toiles, ou pour une ou plusieurs étiquettes. Si vous n'avez pas choisi de campagne, de canvas ou de tags, le rapport s'exécutera pour tous les e-mails des campagnes ou des canvas pendant la période choisie.

Actuellement, ce rapport récupère uniquement les indicateurs du canal e-mail. Les données relatives aux chiffres d'affaires ou aux achats effectués par d'autres canaux que l'e-mail ne seront pas prises en compte dans le rapport. 

Les indicateurs suivants sont disponibles pour les e-mails :

- Achats uniques à la réception
- Revenus à la réception
- Achats uniques lors du clic
- Revenus lors du clic
- Destinataires uniques
- Clics uniques sur l'e-mail

Tous les indicateurs de taux utilisent comme dénominateur les destinataires uniques des e-mails.

#### Définitions

- « À la réception » fait référence aux événements d'achat ou aux revenus qui ont eu lieu dans votre fenêtre de conversion spécifiée, après que les utilisateurs ont reçu les campagnes ou les canvas indiqués. 
- « Lors du clic » fait référence aux événements d'achat ou aux revenus qui ont eu lieu après les événements d'achat, dans votre fenêtre de conversion spécifiée, après que les utilisateurs ont cliqué sur les campagnes ou les canvas indiqués.

Par exemple, disons qu'un segment contient 10 utilisateurs et que cinq d'entre eux ont effectué un achat après avoir reçu votre e-mail. Si l'un de ces cinq personnes a effectué un achat après avoir cliqué sur votre e-mail, votre "taux d'achats uniques à la réception" serait de 50 % et votre "taux d'achats uniques au clic" de 10 %.

![Le rapport présente les indicateurs relatifs aux e-mails, notamment les achats uniques à la réception, le chiffre d'affaires à la réception, les achats uniques au clic, le chiffre d'affaires au clic, les destinataires uniques et les clics uniques sur l'e-mail.]({% image_buster /assets/img_archive/segment_breakdown_results.png %})

#### Résultats

Vos résultats montreront les indicateurs d'achat par segment pour vos campagnes ou Canevas sélectionnés. Si vous n'avez pas sélectionné de campagnes ou de canevas spécifiques, votre rapport affichera les indicateurs d'achat pour chaque segment sur l'ensemble des campagnes d'e-mailing ou des canevas dans la période de temps de votre rapport. 

- **Rangs :** Segments
- **Colonnes :** Indicateurs d'achat


### Visualisation des indicateurs pour les variantes ou les étapes

Pour afficher les indicateurs d'achat et de chiffre d'affaires ventilés par segment pour une variante de campagne, une variante du canvas ou une étape du canvas spécifique, utilisez l'onglet [Variables](#variables) pour spécifier les éléments suivants :

- Campagne spécifique ou Canvas
- Variantes 
- Étape du canvas (facultatif) 
- Intervalle de temps
- Produit spécifique (facultatif) 

#### Résultats

Vos résultats afficheront les indicateurs d'achat par segment pour les variantes ou les étapes que vous avez sélectionnées.

- **Rangs :** Segments
- **Colonnes :** Indicateurs d'achat

{% endtab %}
{% tab Envoi de messages par le haut ou par le bas pour l'engagement dans l'e-mail %}

### Visualisation des indicateurs pour les personnes les plus performantes ou les moins performantes.

Ce rapport dans l'onglet [Variables](#variables) affiche les campagnes, les canvas ou les étapes de canvas qui ont été les plus ou les moins performants pour un indicateur d'engagement spécifié sur l’e-mail. 

Les cas d'utilisation sont les suivants : 
- 10 campagnes avec les taux d'ouverture d'e-mails uniques les plus élevés
- 25 toiles avec le plus grand nombre de désabonnements par e-mail
- 50 étapes du canvas avec le plus grand nombre de clics uniques

Les indicateurs d'e-mail suivants sont disponibles dans ce rapport :
- Envois
- Réceptions
- Plaintes
- Ouverture unique
- Ouvertures automatiques uniques
- Ouvertures non automatiques uniques
- Clics uniques
- Se désabonne
- Rebonds
- Soft bounces
- Plaintes

Pour afficher ce rapport, vous devez spécifier les variables suivantes dans l'onglet **Variables :** 
- **Indicateurs :** Sélectionnez l'un des indicateurs permettant de classer vos résultats.
- **Nombre de rapports :** Sélectionnez les premiers ou les derniers résultats et le nombre de résultats, par exemple les 10 premiers ou les 15 derniers.
- **Type de message :** Précisez si vos résultats sont des campagnes, des canvas ou des étapes de canvas.

#### Résultats

Vos résultats afficheront les campagnes, les toiles ou les étapes du canvas les plus importantes (ou les moins importantes) que vous avez sélectionnées. Par exemple, si vous avez sélectionné les 10 meilleures campagnes pour le taux de clics, vos résultats afficheront les 10 meilleures campagnes classées du taux de clics le plus élevé au plus bas. Vos colonnes afficheront tous les indicateurs d'engagement par e-mail pour chaque ligne (campagnes, Canvas ou étapes de message).

{% endtab %}
{% tab Envoi de messages par le haut ou par le bas pour les achats %}

### Visualisation des indicateurs pour les personnes les plus performantes ou les moins performantes.

Ce rapport dans l'onglet [Variables](#variables) affiche les campagnes, les canvas ou les étapes de Canvas les plus ou les moins performants pour un indicateur d'achat ou de revenu spécifié.

Les cas d'utilisation sont les suivants :
- 20 campagnes avec les taux d'achat les plus élevés pour un produit spécifique
- 25 toiles ayant généré le plus de chiffre d'affaires
- 10 étapes de canvas avec le taux d'achat de produits le plus bas

Les indicateurs d'e-mail suivants sont disponibles dans ce rapport :
- Achats uniques à la réception
- Revenus à la réception
- Achats uniques lors du clic
- Revenus lors du clic
- Destinataires uniques
- Clics uniques sur l'e-mail

Pour afficher ce rapport, vous devez spécifier les variables suivantes dans l'onglet **Variables :** 
- **Indicateurs :** Sélectionnez l'un des indicateurs permettant de classer vos résultats.
- **Nombre de rapports :** Sélectionnez les premiers ou les derniers résultats et le nombre de résultats, par exemple les 10 premiers ou les 15 derniers.
- **Type de message :** Précisez si vos résultats sont des campagnes, des canvas ou des étapes de canvas.
- **Fenêtre de conversion :** Le nombre de jours après la réception de l'e-mail ou le clic auquel Braze attribuera les achats ou les chiffres d'affaires. 

#### Définitions

- « À la réception » fait référence aux événements d'achat ou aux revenus qui ont eu lieu dans votre fenêtre de conversion spécifiée, après que les utilisateurs ont reçu les campagnes ou les canvas indiqués. 
- « Lors du clic » fait référence aux événements d'achat ou aux revenus qui ont eu lieu après les événements d'achat, dans votre fenêtre de conversion spécifiée, après que les utilisateurs ont cliqué sur les campagnes ou les canvas indiqués.

Par exemple, disons qu'un segment contient 10 utilisateurs et que cinq d'entre eux ont effectué un achat après avoir reçu votre e-mail. Si l'un de ces cinq personnes a effectué un achat après avoir cliqué sur votre e-mail, votre taux d'"achats uniques à la réception" serait de 50 % et votre taux d'"achats uniques au clic" de 10 %.

#### Résultats

Vos résultats afficheront les campagnes, les toiles ou les étapes du canvas les plus importantes (ou les moins importantes) que vous avez sélectionnées. Par exemple, si vous avez sélectionné les 10 meilleures campagnes pour le "chiffre d'affaires au clic", vos résultats afficheront les 10 meilleures campagnes classées du plus élevé au plus faible "chiffre d'affaires au clic". Vos colonnes afficheront tous les indicateurs d'achat pour chaque ligne (campagnes, Canvas ou étapes d'envoi de messages).

{% endtab %}
{% tab Performances des notifications push par segment %}

### Affichage des indicateurs de poussée pour les segments

Ce rapport, dans l'onglet [Variables](#variables), affiche les indicateurs de poussée ventilés par segmentation. 

Dans l'onglet **Variables**, indiquez les campagnes ou les canevas pour lesquels vous souhaitez afficher les indicateurs, ainsi qu'une période de temps pour l'extraction des données. Si vous ne sélectionnez pas de campagne ou de Canvase, le rapport affichera les poussées de toutes les campagnes et Canvases dans la période que vous avez spécifiée. Vous pouvez également afficher toutes les campagnes et toutes les toiles avec certains tags.

Les indicateurs de poussée suivants sont disponibles dans ce rapport :

- Envois
- Rebonds
- Réceptions
- Ouvertures directes

#### Résultats

Votre rapport affichera les résultats suivants :

- **Rangs :** Segments
- **Colonnes :** Métriques de notification push
{% endtab %}
{% endtabs %}
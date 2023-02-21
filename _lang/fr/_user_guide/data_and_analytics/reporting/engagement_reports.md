---
nav_title: Engagement Reports
article_title: Engagement Reports
page_order: 3
local_redirect:
  report-glossary: '/docs/user_guide/data_and_analytics/report_metrics/'
page_type: tutorial
description: "Cet article de présentation vous guide dans la création, la personnalisation et la planification des rapports sur l’engagement pour les campagnes et les Canvas."
tool:
  - Campagnes
  - Canvas
  - Rapports
---
# Engagement reports

Les rapports d’engagement sont l’outil de reporting personnalisé de Braze, où vous pouvez tirer des statistiques d’engagement sur les messages de vos campagnes et Canvas.

- Le rapport est exporté en tant que lien intégré dans un e-mail déclenché.
- Quel que soit le nombre de campagnes ou de Canvas sélectionnés, deux fichiers `.csv` seulement seront générés - un pour toutes les données de la campagne, et un pour toutes les données du Canvas.
- Certaines données sont agrégées au niveau « campagne » ou « Canvas » et non pas au niveau « variante » ou « étape » spécifique .

{% alert tip %}
Les rapports ne sont pas enregistrés dans le tableau de bord. Relancer le rapport peut fournir des statistiques actualisées.
{% endalert %}

## Créer un nouveau rapport

1. Dans votre compte de tableau de bord, naviguez jusqu’à **Engagement Reports (Rapports de mission)**, sous **Data (Données)**.
2. Cliquez sur **+ Create New Report (+ Créer un nouveau rapport)**.
3. Ajoutez les [messages des campagnes et du Canvas](#manually-select-campaigns-or-canvases) (individuellement ou [par balise](#automatically-select-campaigns-or-canvases)) que vous souhaitez compiler dans votre rapport.
4. [Ajouter des statistiques](#add-statistics-to-your-report) à votre rapport.
5. Sélectionnez la compression et le délimiteur pour votre rapport.
6. Entrez les adresses e-mail des utilisateurs de Braze qui recevront ce rapport.
7. Sélectionnez la [période](#time-frame) pour les données qui seront affichées dans votre rapport .
8. Sélectionnez les [intervalles (quotidien, hebdomadaire, etc.)](#data-display) pour la ventilation de vos données.
9. Indiquez si le rapport doit être [envoyé immédiatement](#send-immediately) ou à une [date future spécifiée](#send-at-designated-time).
10. Exécutez le rapport, puis ouvrez-le dans votre e-mail quand il arrive !

{% alert note %}
Votre compte utilisateur Braze doit avoir l’autorisation « d’exporter les données utilisateur » pour utiliser les Engagement Reports.
{% endalert %}

---

## Ajouter des messages à votre rapport

L’onglet Ajouter des messages vous permet de sélectionner vos messages de deux façons :

![engagement_reports_message_selection][2]

### Sélection manuelle des campagnes ou des Canvas

Cette option vous permet de choisir les campagnes ou les Canvas que vous souhaitez dans ce rapport.

### Sélection automatique des campagnes ou des Canvas

Cette option vous permet d’inclure automatiquement tous les messages en fonction d’une balise spécifique. Vous pouvez cibler les messages qui ont une ou toutes les balises répertoriées.  Cette option est utile si vous configurez des rapports récurrents et utilisez notre système de tags.


## Ajouter des statistiques à votre rapport

L’onglet Statistiques affiche automatiquement les statistiques des types de campagnes ou de Canvas que vous avez sélectionnés.  Par exemple, si vous avez sélectionné Messages e-mail, vous ne verrez que les statistiques des E-mails.  Si vous avez choisi une combinaison d’ E-mail et de notification push, vous verrez les statistiques pour ces deux canaux.

![engagement_report_add_stats][3]

| channel| statistiques disponibles|
| ------| --------------|
| E-mail | Envois, ouvertures, ouvertures uniques, clics, clics uniques, Click to Open (c.-à-d. taux de réactivité), désabonnement, bounces, livrés, signalements de Spam |
| Notification push  | Envois, Ouvertures, Ouvertures Influencées, Bounces, Body Clicks |
| Notification push Web | Envois, Ouvertures, Bounces, Body Clicks |
| Message in-app | Impressions, clics, clics du Premier Bouton, clics du Second Bouton |
| Webhook  |  Envoi, erreurs |
| SMS | Envois, Envois à l’opérateur, livraisons confirmées, échecs de livraison, rejets |
{: .reset-td-br-1 .reset-td-br-2}

## Configuration de la couverture et de la distribution des données de rapport

L’onglet **Set Up Report (Configurer le rapport0** vous permet de saisir le nom de votre rapport, de sélectionner la compression et le délimiteur du rapport et d’indiquer à qui vous souhaitez envoyer ce rapport.  

![engagement_reports_data_coverage][4]

### Plage temporelle

Par défaut, la plage de données affichée va du premier message sélectionné jusqu’à la date actuelle.  Vous pouvez personnaliser cette option en sélectionnant la liste déroulante de date et en utilisant la sélection de plage personnalisée OU en sélectionnant le bouton radio suivant et en définissant votre plage de dates avec les options de menu déroulant disponibles.

### Affichage des données

Par défaut, les données dans les rapports d’engagement sont affichées sur une base quotidienne (1 jour). Si vous souhaitez afficher ces données pour différents intervalles, vous pouvez choisir un nombre explicite de jours ou de semaines pour regrouper les données du rapport. Ainsi, au lieu de voir les métriques quotidiennes, vous pouvez analyser votre engagement par semaine, mois, trimestre, etc. Si une agrégation centrée sur le temps ne suffira pas, vous pouvez également choisir d’exporter des données au niveau de la campagne ou du Canvas .

## Programmer votre rapport

Vous avez deux options lors de la planification de votre rapport :

![engagement_reports_schedule_report][5]{: style="max-width:65%;" }

### Envoyer immédiatement

Une fois le rapport enregistré, Braze enverra ce rapport immédiatement

### Envoyer à un moment spécifié

Cette option vous permet de choisir la fréquence à laquelle vous souhaitez recevoir ce rapport.  Vous pouvez choisir d’envoyer ce rapport tous les X jours, semaines ou mois.  De plus, vous pouvez indiquer quand arrêter d’envoyer le rapport.

## Ouvrir le rapport  

Vous recevrez un e-mail contenant des liens vers vos rapports. Lorsque vous cliquez sur les liens fournis, vous téléchargez automatiquement un fichier ZIP contenant vos fichiers CSV-un par campagnes.

Le rapport, lorsqu’il est ouvert, contient toutes les statistiques sélectionnées dans la section [Ajouter des statistiques](#add-statistics-to-your-reports) lors de la configuration.



[2]: {% image_buster /assets/img_archive/engagement_report_add_messages.png %}
[3]: {% image_buster /assets/img_archive/engagement_report_add_stats.png %}
[4]: {% image_buster /assets/img_archive/engagement_report_datacoverage.png %}
[5]: {% image_buster /assets/img_archive/engagement_report_reportschedule.png %}

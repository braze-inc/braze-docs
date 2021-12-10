---
nav_title: Rapports d'engagement
article_title: Rapports d'engagement
page_order: 3
local_redirect:
  report-glossary: '/fr/docs/user_guide/data_and_analytics/report_metrics/'
page_type: tutoriel
description: "Cet article pratique vous guide à travers la création, la personnalisation et la planification des rapports d'engagement pour les campagnes et les canvases."
tool:
  - Campagnes
  - Toile
  - Rapports
---

# Rapports d'engagement

Les rapports d'engagement sont l'outil de rapport personnalisé de Brase, où vous pouvez tirer des statistiques d'engagement pour des messages spécifiques de campagnes et de canvases.

- Le rapport est exporté sous la forme d'un lien intégré dans un e-mail déclenché.
- Indépendamment du nombre de campagnes ou de Canvas sélectionnés, seul un maximum de deux `. sv` fichiers seront générés - un pour toutes les données de la campagne, et un pour toutes les données de Canvas .
- Certaines données sont agrégées au niveau « campagne » ou « Canv » par rapport au niveau individuel « variante » ou « étape ».

{% alert tip %}
Les rapports ne sont pas sauvegardés dans le tableau de bord, et la réexécution du rapport peut entraîner la mise à jour des statistiques.
{% endalert %}

## Créer un nouveau rapport

![GIF de la création d'un rapport d'engagement]({% image_buster /assets/img/engagement_reports.gif %}){: style="float:right;max-width:50%;border:0px;"}

1. Dans votre compte de tableau de bord, accédez à **Rapports d'engagement**, sous **Données**.
2. Cliquez sur **+ Créer un nouveau rapport**.
3. Ajoutez les [campagnes et les messages Canvas](#manually-select-campaigns-or-canvases) (individuellement ou [par tag](#automatically-select-campaigns-or-canvases)) que vous souhaitez compiler dans votre rapport.
4. [Ajouter des statistiques](#add-statistics-to-your-report) à votre rapport.
5. Sélectionnez la compression et le délimiteur pour votre rapport.
6. Entrez les adresses e-mail des utilisateurs de Braze qui devraient recevoir ce rapport.
7. Sélectionnez la [période](#time-frame) à partir de laquelle vous souhaitez que votre rapport exécute des données.
8. Sélectionnez les intervalles [(quotidiens, hebdomadaires, etc.)](#data-display) à partir desquels vous aimeriez voir la ventilation de vos données.
9. Planifiez votre rapport à [envoyer immédiatement](#send-immediately) ou à un [futur, heure spécifiée](#send-at-designated-time).
10. Exécutez le rapport, puis ouvrez-le dans votre e-mail quand il arriver!

{% alert note %}
Votre compte utilisateur Braze doit avoir accès à « Exporter les données utilisateur » pour utiliser les rapports d'engagement.
{% endalert %}

---

## Ajouter des messages à votre rapport

L'onglet Ajouter des messages vous permet de sélectionner vos messages de deux manières:

!\[engagement_reports_message_selection\]\[2\]

### Sélectionner manuellement des campagnes ou des toiles

Cette option vous donne la liberté de choisir les campagnes ou Canvases que vous souhaitez dans ce rapport.

### Sélectionner automatiquement les campagnes ou les toiles

Cette option vous donne la possibilité d'inclure automatiquement tous les messages en fonction d'un tag spécifique. Vous pouvez cibler les messages qui ont un ou tous les tags listés.  Cette option est utile si vous configurez des rapports récurrents et utilisez notre système de marquage.


## Ajouter des statistiques à votre rapport

L'onglet Stats vous montrera automatiquement les statistiques pour les types de campagnes ou de toiles que vous avez sélectionnées.  Par exemple, si vous avez sélectionné les messages par e-mail, vous ne verrez que les statistiques par courriel.  Si vous avez choisi une combinaison de Courriel et Push, vous verrez les statistiques pour ces deux chaînes.

!\[engagement_report_add_stats\]\[3\]

| canal          | stats disponibles                                                                                   |
| -------------- | --------------------------------------------------------------------------------------------------- |
| Courriel       | Envoyer, Ouvrir, Ouvertures uniques, Clics, Clics Uniques, Désabonner, Bounces, Livré, Spam signalé |
| Pousser        | Envoyer, Ouvrir, Ouvertures Influencées, Rebondissements, Clics Corps                               |
| Push Web       | Envoyer, Ouvrir, Bounces, Clics Corps                                                               |
| Message In-App | Impressions, clics, clics sur le premier bouton, clics sur le deuxième bouton                       |
| Webhook        | Envoyer, Erreurs                                                                                    |
| SMS            | Envoyer, envoyer au transporteur, les livraisons confirmées, les échecs de livraison, les rejets    |
{: .reset-td-br-1 .reset-td-br-2}

## Configurez la couverture et la distribution des données du rapport

L'onglet **Rapport de configuration** vous permet de saisir le nom de votre rapport. sélectionnez la compression et le délimiteur du rapport et incluez à qui vous souhaitez envoyer ce rapport.

!\[engagement_reports_data_coverage\]\[4\]

### Intervalle de temps

Par défaut, la plage de données affichée va du message le plus ancien sélectionné jusqu'à la date actuelle.  Vous pouvez personnaliser cela en sélectionnant le menu déroulant de la date et en utilisant la sélection de la plage personnalisée OU en sélectionnant le bouton radio suivant et en définissant votre plage de dates avec les options déroulantes disponibles.

### Affichage des données

Par défaut, les données affichées dans les rapports d'engagement sont quotidiennes (1 jour). Si vous souhaitez voir ces données à différents intervalles, vous pouvez choisir un nombre explicite de jours ou de semaines pour regrouper les données du rapport. Donc, au lieu de voir des métriques quotidiennes, vous pouvez regarder votre engagement par semaine, mois, trimestre, etc. Si une agrégation chronologique ne suffit pas, vous pouvez également choisir d'exporter des données au niveau de la campagne ou de Canvas .

## Planifier votre rapport

Il y a deux options lors de la planification de votre rapport :

!\[engagement_reports_schedule_report\]\[5\]{: style="max-width:65%;" }

### Envoyer immédiatement

Une fois le rapport enregistré, Braze enverra ce rapport immédiatement

### Envoyer à une heure désignée

Cette option vous donne la flexibilité de choisir la fréquence à laquelle vous souhaitez recevoir ce rapport.  Vous pouvez choisir d'envoyer ce rapport tous les X jours, semaines ou mois.  De plus, vous pouvez définir quand arrêter l'envoi du rapport.

## Ouvrir le rapport

Vous recevrez un e-mail avec des liens vers vos rapports. Lorsque vous cliquez sur les liens fournis, vous téléchargerez automatiquement un fichier ZIP contenant vos fichiers CSV - un pour toutes les Campagnes.

Le rapport, une fois ouvert, contiendra toutes les statistiques sélectionnées dans la section [Ajouter des statistiques](#add-statistics-to-your-reports) du processus d'installation.
[2]: {% image_buster /assets/img_archive/engagement_report_add_messages.png %} [3]: {% image_buster /assets/img_archive/engagement_report_add_stats. ng %} [4]: {% image_buster /assets/img_archive/engagement_report_datacoverage.png %} [5]: {% image_buster /assets/img_archive/engagement_report_reportschedule.png %}

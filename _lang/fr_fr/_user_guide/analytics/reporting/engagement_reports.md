---
nav_title: Rapports d’engagement
article_title: Rapports d’engagement
page_order: 3
local_redirect:
  report-glossary: '/docs/user_guide/data_and_analytics/report_metrics/'
page_type: tutorial
description: "Cet article de présentation vous guide dans la création, la personnalisation et la planification des rapports sur l’engagement pour les campagnes et les Canvas."
tool:
  - Campaigns
  - Canvas
  - Reports
---

# Rapports d’engagement

> Les rapports d'engagement vous permettent d'obtenir des statistiques d'engagement pour des messages spécifiques de campagnes et de canevas à recevoir sous forme d'e-mail au moment de votre choix.

{% alert note %}
Vous devez disposer de l'autorisation "Exportation de données utilisateur" pour exécuter les rapports d'engagement.
{% endalert %}

Avec les rapports d'engagement, vous pouvez sélectionner manuellement les campagnes et les Canvases à inclure dans votre rapport d'e-mail, ou spécifier des règles pour sélectionner automatiquement les campagnes et les Canvases pertinentes.

Quel que soit le nombre de campagnes ou de Canvas que vous sélectionnez, deux fichiers CSV sont générés, l'un pour toutes les données de la campagne et l'autre pour toutes les données du Canvas. Vous pouvez accéder à ces fichiers CSV à partir du lien figurant dans l'e-mail de votre rapport. Les rapports d'engagement ne sont pas enregistrés dans le tableau de bord de Braze.

Certaines données sont agrégées au niveau de la campagne ou du canvas et non au niveau de la variante de campagne individuelle ou de l'étape de canvas. Si vous [supprimez une étape du canvas après le lancement]({{site.baseurl}}/user_guide/engagement_tools/canvas/managing_canvases/change_your_canvas_after_launch/#canvas-details), cela supprimera également les données des rapports d'engagement.

{% alert tip %}
Vous pouvez exécuter à nouveau le rapport pour obtenir des statistiques actualisées.
{% endalert %}

## Créer un nouveau rapport

### Étape 1 : Créer un rapport

Dans votre compte tableau de bord, accédez à **Analyse/analytique** > **Rapports d'**engagement (si vous utilisez un tableau de bord). Sélectionnez **\+ Créer un nouveau rapport**.

### Étape 2 : Ajouter des messages

Ajoutez les campagnes et les messages Canvas que vous souhaitez compiler dans votre rapport. Vous pouvez sélectionner vos messages de deux manières :

- Sélection manuelle des campagnes et des toiles
- Sélectionner automatiquement les campagnes et les canevas en fonction de règles spécifiques

![engagement_reports_message_selection]({% image_buster /assets/img_archive/engagement_report_add_messages.png %})

#### Sélection manuelle des campagnes ou des Canvas

Cette option vous permet de choisir les campagnes ou les Canvas que vous souhaitez dans ce rapport.

#### Sélection automatique des campagnes ou des Canvas

Cette option vous permet d'inclure automatiquement tous les messages contenant une [étiquette]({{site.baseurl}}/user_guide/administrative/app_settings/tags/) spécifique. Vous pouvez cibler les messages qui ont une ou toutes les balises répertoriées. Cette option est utile si vous mettez en place des rapports récurrents et que vous taguez régulièrement vos messages d'engagement.

### Étape 3 : Ajouter des statistiques {#add-statistics-to-your-reports}

L'étape **Ajouter des statistiques** vous montre les statistiques pour les types de campagnes ou de canevas que vous avez sélectionnés. Par exemple, si vous avez sélectionné les messages e-mail, vous ne pouvez consulter que les statistiques pertinentes relatives aux e-mails. Si vous avez choisi une combinaison d'e-mail et de push, vous pouvez consulter les statistiques pour ces deux canaux.

![engagement_report_add_stats]({% image_buster /assets/img_archive/engagement_report_add_stats.png %})

| Canal | Statistiques disponibles |
| ------| --------------|
| E-mail | Envois, ouvertures, ouvertures uniques, clics, clics uniques, Click to Open (c.-à-d. taux de réactivité), désabonnement, bounces, livrés, signalements de Spam |
| Notification push  | Envois, Ouvertures, Ouvertures Influencées, Bounces, Body Clicks |
| Notification push Web | Envois, Ouvertures, Bounces, Body Clicks |
| Message in-app | Impressions, clics, clics du Premier Bouton, clics du Second Bouton |
| Webhook  |  Envoi, erreurs |
| SMS | Envois, Envois à l’opérateur, livraisons confirmées, échecs de livraison, rejets |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert note %}
L'*envoi au transporteur* est obsolète, mais continuera d'être pris en charge par les utilisateurs qui en disposent déjà.
{% endalert %}

### Étape 4 : Configuration complète du rapport

Donnez un nom à votre rapport, choisissez sa mise en forme et sélectionnez vos destinataires. Par défaut, les rapports d'engagement sont envoyés sous la forme d'un fichier ZIP dont les données sont délimitées par des virgules (où chaque donnée est séparée par une virgule).

Vous pouvez choisir parmi les options de compression et de délimitation suivantes :

- **Compression :** ZIP, non compressé ou gzip
- **Séparateur :** Virgule (`,`), Deux-points (`:`), Point-virgule (`;`), ou Pipes (`|`).

{% alert note %}
Les statistiques sont uniquement collectées pour la période spécifiée par le rapport. Pour recevoir des statistiques précises sur les taux d'ouverture et de clics, sélectionnez une plage de dates qui inclut le moment où les événements d'envoi ont été effectués pour vos campagnes et vos Canevas.
{% endalert %}

#### Sélectionner la fenêtre temporelle

Par défaut, la plage de données affichée est basée sur le fuseau horaire de votre entreprise et va du premier message sélectionné jusqu'à la date actuelle. Vous pouvez personnaliser cette option en sélectionnant la liste déroulante de date et en utilisant la sélection de plages personnalisées OU en sélectionnant le bouton radio suivant et en définissant votre plage de dates avec les options de menu déroulant disponibles.

#### Sélectionner l'affichage des données

Par défaut, les données affichées dans les rapports d'engagement sont quotidiennes (un jour). Pour visualiser ces données sur différents intervalles, choisissez un nombre explicite de jours ou de semaines pour agréger les données pour le rapport. Ainsi, au lieu de voir des indicateurs quotidiens, vous pouvez visualiser votre engagement par semaine, mois, trimestre ou autre. Si une agrégation centrée sur le temps ne suffit pas, vous pouvez également choisir d’exporter des données au niveau de la campagne ou du Canvas.

![engagement_reports_data_coverage]({% image_buster /assets/img_archive/engagement_report_datacoverage.png %})

#### Programmer votre rapport

Vous avez deux options lors de la planification de votre rapport :

- **Envoyer immédiatement :** Une fois le rapport lancé, Braze l'enverra immédiatement.
- **Envoyer à un moment spécifié :** Cette option vous permet de choisir la fréquence de réception de ce rapport. Vous pouvez choisir d'envoyer ce rapport tous les X jours, semaines ou mois. Vous pouvez également définir le moment où l'envoi du rapport doit cesser.

![engagement_reports_schedule_report]({% image_buster /assets/img_archive/engagement_report_reportschedule.png %}){: style="max-width:65%;" }

### Étape 5 : Vérifier et lancer le test

La dernière étape de la configuration de votre rapport présente un aperçu des options configurées. Examinez votre rapport et, lorsque vous êtes satisfait, sélectionnez **Lancer le rapport.**

### Étape 6 : Consultez votre e-mail  

Vous recevrez un e-mail contenant des liens vers vos rapports à l'heure ou à la planification de votre choix. **Ces liens expirent une heure après l'envoi du rapport.** Lorsque vous sélectionnez les liens fournis, vous téléchargez automatiquement un fichier ZIP contenant vos fichiers CSV - un pour chaque campagne.

Le rapport contient toutes les statistiques sélectionnées dans la section [Ajouter des statistiques de](#add-statistics-to-your-reports) la procédure de configuration.



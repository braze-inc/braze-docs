---
nav_title: "Rapports d'engagement"
article_title: "Rapports d'engagement"
page_order: 3
local_redirect:
  report-glossary: '/docs/user_guide/data_and_analytics/report_metrics/'
page_type: tutorial
description: "Cet article pratique vous guide dans la création, la personnalisation et la planification des rapports d'engagement pour les campagnes et les Canevas."
tool:
  - Campaigns
  - Canvas
  - Reports
---

# Rapports d'engagement

> Les rapports d'engagement vous permettent d'obtenir des statistiques d'engagement pour des messages spécifiques de campagnes et de canevas à recevoir sous forme d'e-mail au moment de votre choix.

{% alert note %}
Vous devez disposer de l'autorisation "Exportation de données utilisateur" pour exécuter les rapports d'engagement.
{% endalert %}

Avec les rapports d'engagement, vous pouvez sélectionner manuellement les campagnes et les Canvases à inclure dans votre rapport d'e-mail, ou spécifier des règles pour sélectionner automatiquement les campagnes et les Canvases pertinentes.

Quel que soit le nombre de campagnes ou de Canvas que vous sélectionnez, deux fichiers CSV sont générés, l'un pour toutes les données de la campagne et l'autre pour toutes les données du Canvas. Vous pouvez accéder à ces fichiers CSV à partir du lien figurant dans l'e-mail de votre rapport. Les rapports d'engagement ne sont pas enregistrés dans le tableau de bord de Braze.

Certaines données sont agrégées au niveau de la campagne ou du Canvas par rapport à la variante individuelle de la campagne ou à l'étape du Canvas. Si vous [supprimez une étape du canvas après le lancement]({{site.baseurl}}/user_guide/engagement_tools/canvas/managing_canvases/change_your_canvas_after_launch/#canvas-details), cela supprimera également les données des rapports d'engagement.

{% alert tip %}
Vous pouvez exécuter à nouveau le rapport pour obtenir des statistiques actualisées.
{% endalert %}

## Créer un nouveau rapport

### Étape 1 : Créer un rapport

Dans votre compte tableau de bord, accédez à **Analyse/analytique** > **Rapports d'**engagement (si vous utilisez un tableau de bord). Sélectionnez **\+ Créer un nouveau rapport**.

### Étape 2 : Ajouter des messages

Ajoutez les campagnes et les messages Canvas que vous souhaitez compiler dans votre rapport. Vous pouvez sélectionner vos messages de deux manières :

- Sélection manuelle des campagnes et des toiles
- Sélectionner automatiquement les campagnes et les canevas en fonction de règles spécifiques

![engagement_reports_message_selection]({% image_buster /assets/img_archive/engagement_report_add_messages.png %})

#### Sélectionner manuellement des campagnes ou des toiles

Cette option vous donne la liberté de choisir les campagnes ou les canevas que vous souhaitez voir figurer dans ce rapport.

#### Sélectionner automatiquement des campagnes ou des toiles

Cette option vous permet d'inclure automatiquement tous les messages contenant une [étiquette]({{site.baseurl}}/user_guide/administrative/app_settings/tags/) spécifique. Vous pouvez cibler les messages qui comportent l'un ou l'autre ou l'ensemble des tags répertoriés. Cette option est utile si vous mettez en place des rapports récurrents et que vous taguez régulièrement vos messages d'engagement.

### Étape 3 : Ajouter des statistiques {#add-statistics-to-your-reports}

L'étape **Ajouter des statistiques** vous montre les statistiques pour les types de campagnes ou de canevas que vous avez sélectionnés. Par exemple, si vous avez sélectionné les messages e-mail, vous ne pouvez consulter que les statistiques pertinentes relatives aux e-mails. Si vous avez choisi une combinaison d'e-mail et de push, vous pouvez consulter les statistiques pour ces deux canaux.

![engagement_report_add_stats]({% image_buster /assets/img_archive/engagement_report_add_stats.png %})

| Chaîne | Statistiques disponibles |
| ------| --------------|
| e-mail | Envois, ouvertures, ouvertures uniques, clics, clics uniques, clics d'ouverture, désabonnements, rebonds, livrés, spams signalés |
| Pousser  | Envois, ouvertures, ouvertures influencées, rebonds, clics directs |
| Web Push | Envois, ouvertures, rebonds, clics du corps |
| Message in-app | Impressions, clics, clics du premier bouton, clics du deuxième bouton |
| webhook  |  Envois, erreurs |
| SMS | Envois, Envois au transporteur, Réceptions/distributions confirmées, Échecs de livraison, Rejets |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert note %}
L'*envoi au transporteur* est obsolète, mais continuera d'être pris en charge par les utilisateurs qui en disposent déjà.
{% endalert %}

### Étape 4 : Configuration complète du rapport

Donnez un nom à votre rapport, choisissez sa mise en forme et sélectionnez vos destinataires. Par défaut, les rapports d'engagement sont envoyés sous la forme d'un fichier ZIP dont les données sont délimitées par des virgules (où chaque donnée est séparée par une virgule).

Vous pouvez choisir parmi les options de compression et de délimitation suivantes :

- **Compression :** ZIP, non compressé ou gzip
- **Délimiteur :** Virgule (`,`), Deux-points (`:`), Point-virgule (`;`), ou Pipes (`|`).

{% alert note %}
Les statistiques ne sont collectées que pour la période spécifiée par le rapport. Pour recevoir des statistiques précises sur les taux d'ouverture et de clics, sélectionnez une plage de dates qui inclut le moment où les événements d'envoi ont été effectués pour vos campagnes et vos Canevas.
{% endalert %}

#### Sélectionnez une période

Par défaut, la plage de données affichée est basée sur le fuseau horaire de votre entreprise et va du premier message sélectionné jusqu'à la date actuelle. Vous pouvez la personnaliser en sélectionnant la liste déroulante des dates et en utilisant la sélection de plage personnalisée OU en sélectionnant le bouton radio suivant et en définissant votre plage de dates à l'aide des options de la liste déroulante.

#### Sélectionner l'affichage des données

Par défaut, les données affichées dans les rapports d'engagement sont quotidiennes (un jour). Pour visualiser ces données sur différents intervalles, choisissez un nombre explicite de jours ou de semaines pour agréger les données pour le rapport. Ainsi, au lieu de voir des indicateurs quotidiens, vous pouvez visualiser votre engagement par semaine, mois, trimestre ou autre. Si une agrégation centrée sur le temps ne suffit pas, vous pouvez également choisir d'exporter les données au niveau de la campagne ou du Canvas.

![engagement_reports_data_coverage]({% image_buster /assets/img_archive/engagement_report_datacoverage.png %})

#### Planifiez votre rapport

Vous avez deux possibilités pour planifier votre rapport :

- **Envoyer immédiatement :** Une fois le rapport lancé, Braze l'enverra immédiatement.
- **Envoyer à une heure donnée :** Cette option vous permet de choisir la fréquence de réception de ce rapport. Vous pouvez choisir d'envoyer ce rapport tous les jours, semaines ou mois. Vous pouvez également définir le moment où l'envoi du rapport doit cesser.

![engagement_reports_schedule_report]({% image_buster /assets/img_archive/engagement_report_reportschedule.png %}){: style="max-width:65%;" }

### Étape 5 : Examen et lancement

La dernière étape de la configuration de votre rapport présente un aperçu des options configurées. Examinez votre rapport et, lorsque vous êtes satisfait, sélectionnez **Lancer le rapport.**

### Étape 6 : Consultez votre e-mail  

Vous recevrez un e-mail contenant des liens vers vos rapports à l'heure ou à la planification de votre choix. **Ces liens expirent une heure après l'envoi du rapport.** Lorsque vous sélectionnez les liens fournis, vous téléchargez automatiquement un fichier ZIP contenant vos fichiers CSV - un pour chaque campagne.

Le rapport contient toutes les statistiques sélectionnées dans la section [Ajouter des statistiques de](#add-statistics-to-your-reports) la procédure de configuration.



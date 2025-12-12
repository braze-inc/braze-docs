---
nav_title: Statuts
article_title: Statuts de la campagne et du canvas
page_order: 1
description: "Découvrez les statuts des campagnes et des Canvas et comment les utiliser dans le tableau de bord."
tool:
    - Campaigns
    - Canvas
---

# Statuts de la campagne et du canvas

> Découvrez les statuts des campagnes et des Canvas et comment vous pouvez les utiliser dans le tableau de bord.

## Filtrage par statut

Pour filtrer vos campagnes ou Canevas par statut, sélectionnez **Tous les statuts**, puis choisissez un statut.

Le menu déroulant "Tous les statuts" dans le tableau de bord de Braze.]({% image_buster /assets/img/messaging_fundamentals/filter-by-status.png %}){: style="max-width:70%;"}

## Changement d'état

Pour modifier le statut d'une campagne ou d'un canvas, sélectionnez le menu <i class="fas fa-ellipsis-vertical"></i>, puis choisissez un statut.

Une liste des toiles dans le tableau de bord de Braze, avec le menu ouvert pour l'une des toiles.]({% image_buster /assets/img/messaging_fundamentals/change-status.png %})

## Statuts disponibles

Il s'agit des statuts disponibles pour les campagnes et les toiles :

| Statut | Description |
| --- | --- |
| Actif | Les campagnes actives et les canevas sont en cours d'envoi. Par défaut, vous verrez les campagnes actives et les Canevas sur les pages respectives. |
| Projet | Les brouillons des campagnes et des toiles sont enregistrés mais ne sont pas lancés. Pour continuer à modifier et commencer à envoyer, vous pouvez sélectionner le brouillon en allant dans **Messagerie** dans le tableau de bord de Braze et en sélectionnant **Canvas** ou **Campagnes**. |
| Archivé | Les campagnes et les canevas archivés sont des messages qui ne sont plus envoyés. Ces campagnes et toiles sont également supprimées des graphiques statistiques de la page d'accueil. [**Accueil**]({{site.baseurl}}/user_guide/analytics/dashboard/home_dashboard) et [**chiffre d'affaires**]({{site.baseurl}}/user_guide/analytics/reporting/revenue_report) des pages Accueil et Revenus.|
| Arrêtée | Les campagnes et les toiles arrêtées sont en pause, mais vous pouvez toujours les modifier. Pour reprendre, sélectionnez le menu <i class="fas fa-ellipsis-vertical"></i>, puis **Reprise**. Pour plus d'informations, reportez-vous à la section [Comportement des toiles à l'arrêt.](#stopped-canvas-behavior) |
| Au repos | Lorsqu'une campagne ou un Canvas n'envoie plus de messages, Braze lui attribue un statut d'inactivité pour faciliter le tri et la gestion de votre liste de campagnes et de Canvas. Vous pouvez visualiser les campagnes ou les toiles qui seront automatiquement arrêtées et la date d'arrêt associée. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Arrêt du comportement de Canvas {#stopped-canvas-behavior}

Lorsqu'une toile est arrêtée, il se produit ce qui suit :

- **Envois planifiés :** Vos messages planifiés ne seront pas envoyés, quelle que soit la place de l'utilisateur dans le canvas. Cela inclut également les utilisateurs qui ont été mis en file d'attente en raison de la limite de débit.
- **Envoi d'e-mails :** Les envois d'e-mails peuvent ne pas cesser immédiatement, car votre fournisseur de services d'e-mailing (ESP) peut continuer à traiter vos demandes existantes.
- **Retard par paliers :** Les utilisateurs se trouvant dans une [étape du]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/delay_step/) canvas y resteront normalement, mais quitteront le canvas à la fin de la période définie.

Pour reprendre le canvas, sélectionnez le menu <i class="fas fa-ellipsis-vertical"></i>, puis **Reprendre**. Lorsqu'il est réactivé, tous les messages précédemment interrompus sont envoyés conformément à la planification, tant que l'heure prévue n'est pas dépassée.

## Meilleures pratiques

### Contrôlez vos messages par statut

Vous pouvez surveiller vos messages par état pour examiner les détails des performances. Par exemple, si vous avez une série de campagnes actives, vous pouvez évaluer les performances de chaque campagne avec leurs indicateurs d'engagement et faire les ajustements nécessaires. Si, au contraire, vous avez quelques toiles arrêtées, vous pouvez vous demander s'il convient de les reprendre pour l'envoi de messages ou de les archiver complètement.

{% alert tip %}
Vous cherchez d'autres moyens de rester organisé ? Ajoutez des [Teams]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/teams) et des [tags]({{site.baseurl}}/user_guide/administrative/app_settings/tags) pour fournir plus de contexte en un coup d'œil.
{% endalert %}

### Contrôlez vos messages actifs

En réalisant des audits de vos campagnes et canevas actifs, vous pouvez évaluer leur pertinence et leur performance, et supprimer ou mettre à jour les campagnes et canevas obsolètes afin de conserver la fraîcheur de votre envoi de messages.

---
nav_title: Kameleoon
article_title: Kameleoon
description: "Apprenez à intégrer Kameleoon à Braze"
alias: /partners/kameleoon/
page_type: partner
search_tag: Partner
---

# Kameleoon

>[Kameleoon](https://www.kameleoon.com) est une solution d'optimisation avec des fonctionnalités d'expérimentation, de personnalisation par l'intelligence artificielle et de gestion des fonctionnalités dans une seule plateforme unifiée.

## Conditions préalables

Avant de commencer, vous aurez besoin des éléments suivants :

| Exigence | Description |  
| --- | --- |  
| Compte Kameleoon | Un compte Kameleoon est nécessaire pour bénéficier de ce partenariat.|  
| Compte Braze| Un compte Braze actif avec l'intégration du [Braze Web SDK]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=web) sur votre page web. Vous devez également activer la segmentation des propriétés d'événement. Pour en faire la demande, reportez-vous à la rubrique [Considérations.](#considerations)|  
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Cas d’utilisation

Kameleoon envoie des événements personnalisés à Braze pour identifier les utilisateurs participant à des campagnes d'expérimentation et de personnalisation, ce qui permet un ciblage plus précis et un envoi de messages personnalisés.

## Intégration de Kameleoon

Cette intégration fonctionne comme un tracker JavaScript via le site engine.js de Kameleoon. Il peut être activé rapidement à partir de la plateforme Kameleoon.

### Étape 1 : Accédez à la page Intégrations de Kameleoon

Dans votre application Kameleoon, sélectionnez **Admin** puis **Intégrations** dans la barre latérale.

![Le panneau d'administration de la plateforme Kameleoon.]({% image_buster /assets/img/kameleoon/img_1.png %}){: style="max-width:70%;"}

### Étape 2 : Installer l'outil Braze

Par défaut, l'outil Braze n'est pas installé. Recherchez l'icône Braze, puis sélectionnez **Installer l'outil**. ![Un carré gris avec une flèche pointant vers le bas.]({% image_buster /assets/img/kameleoon/img_2.png %})

Sélectionnez les projets pour lesquels vous souhaitez activer l'outil Braze, afin que les données de Kameleoon soient correctement rapportées à Braze.

![L'icône de l'outil Braze dans Kameloon.]({% image_buster /assets/img/kameleoon/img_3.png %})

Après avoir configuré l'outil, sélectionnez **Valider**, ce qui fermera le panneau de configuration. Vous verrez alors un basculeur **ON** à côté de l'icône de l'outil Braze, y compris le nombre de projets sur lesquels l'outil est configuré.

![L'outil Braze est basculé sur "On" dans Kameleoon.]({% image_buster /assets/img/kameleoon/img_4.png %})

{% alert important %}  
Cette fonctionnalité est en version bêta. Rejoignez le [programme bêta de Kameleoon](https://help.kameleoon.com/account-and-team-management/join-beta-program/) pour commencer à utiliser cette intégration.  
{% endalert %}  
    
### Étape 3 : Associer Braze aux campagnes de Kameleoon

#### Dans l'éditeur graphique/de code

Pour finaliser votre expérience, sélectionnez l'étape **Intégrations** pour configurer Braze comme outil de suivi, puis sélectionnez **Braze**.

![Le tableau de bord des intégrations dans Kameleoon montrant toutes les intégrations disponibles, y compris l'intégration active Braze.]({% image_buster /assets/img/kameleoon/img_5.png %})

Braze sera mentionné dans le résumé avant la mise en ligne/en production/instantanée. Kameleoon transmettra automatiquement les données à Braze, et vous pourrez les utiliser pour l'analyse et la segmentation directement dans Braze.

##### Création de personnalisation

Sur la page de **création de la personnalisation**, vous pouvez sélectionner Braze parmi les outils de reporting pour personnaliser vos rapports.

![La section Outils de reporting montre des intégrations telles que Heap, Mixpanel, Clarity, avec Braze sélectionné.]({% image_buster /assets/img/kameleoon/img_6.png %})

##### Création d'un drapeau de fonctionnalité

Configurez l'intégration dans l'environnement de la fonctionnalité dans la section **Intégrations**. Activez-la pour les environnements dans lesquels vous souhaitez qu'elle soit active.

![La page du drapeau de fonctionnalité dans Kameleoon avec les intégrations disponibles. Il existe deux commutateurs pour chaque partenaire, "Règles de réception/distribution" et "Expériences de fonctionnalité".]({% image_buster /assets/img/kameleoon/img_7.png %})

##### Page des résultats

Une fois que Braze est défini comme outil de reporting pour une expérience, vous pouvez le sélectionner (ou le désélectionner) sur la page des résultats de Kameleoon dans le menu de **configuration de l'expérience.** 

{% alert note %}  
Cette intégration nécessite une [mise en œuvre hybride](https://developers.braze-presentation.preview.kameleoon.net/core-concepts/hybrid-experimentation?language=en#sending-exposure-events-to-third-party-analytics) et n'est compatible qu'avec les SDK web.
{% endalert %}

![Le panneau latéral de la page de résultats dans Kameleoon.]({% image_buster /assets/img/kameleoon/img_8.png %}){: style="max-width:50%;" }

Les outils de rapport associés à l'expérience s'affichent. Sélectionnez **Modifier** pour modifier cette sélection.

### Étape 4 : Analysez et exploitez vos données Kameleoon dans Braze

Une fois l'intégration mise en place, Kameleoon enverra à Braze des événements personnalisés appelés `kameleoon_exposure` avec des propriétés telles que le **nom de l'expérience**, l'**ID de l'expérience**, le **nom de la variation**, l'**ID de la variation**.

![Le journal des événements utilisateurs personnalisés dans Braze, montrant un exemple de charge utile de l'événement qui a été reçu par Braze depuis Kameleoon.]({% image_buster /assets/img/kameleoon/img_9.png %})

Vous pouvez ensuite consulter ces données dans les événements personnalisés, créer des rapports d'événements personnalisés pour identifier l'exposition aux campagnes Kameleoon et activer la segmentation en fonction des propriétés d'événement. Vous pouvez utiliser des événements personnalisés lors de la création de campagnes et de Canevas ultérieurs ou liés par le biais de [parcours d'action]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/action_paths/#action-groups), de [déclencheurs basés sur des actions]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery) ou de la création de [segmentations]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/)

En outre, ces événements seront accessibles par le biais des [objets d'événement personnalisés de Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events/), ce qui permettra d'établir des rapports et des analyses complets.

## Considérations

### Segmentation des propriétés des événements de la demande

Avant de pouvoir utiliser la segmentation des propriétés d'événement, vous devez l'activer dans Braze. Utilisez le modèle suivant pour contacter votre CSM de Braze ou l'équipe d'assistance pour obtenir l'accès.

   <table>
   <thead>
      <tr>
         <th>Champ</th>
         <th>Détails</th>
      </tr>
   </thead>
   <tbody>
      <tr>
         <td><strong>Objet</strong></td>
         <td>Demande d'activation de la segmentation des propriétés d'événement pour l'intégration de Kameleoon</td>
      </tr>
      <tr>
         <td><strong>Corps</strong></td>
         <td>
         Bonjour Teams,<br><br>
         Nous aimerions activer la segmentation des propriétés d'événement pour les événements envoyés depuis notre intégration Kameleoon&lt;>Braze. Voici les détails :<br><br>
         - <strong>Nom de l'événement :</strong> Kameleoon<br>
         - <strong>Propriétés d'événement :</strong> <code>kameleoon_campaign_name</code>, <code>kameleoon_variation_name</code><br><br>
         Veuillez confirmer une fois que les propriétés ont été activées dans notre compte.<br><br>
         Merci.
         </td>
      </tr>
   </tbody>
   </table>
   {: .reset-td-br-1 .reset-td-br-2 role="presentation"}

### Points de données Braze

L'événement personnalisé envoyé par Kameleoon à Braze - y compris toutes les propriétés d'événement activées pour la segmentation - enregistrera des points de données dans votre instance Braze.
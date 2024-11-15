---
nav_title: "Création d'une carte bannière"
article_title: "Création d'une carte bannière"
permalink: "/create_banner_card/"
description: "Cet article de référence explique comment créer et envoyer des cartes bannières à l'aide des campagnes Braze."
page_type: reference
---

# Création d'une carte bannière

> Cet article explique comment créer une carte-bannière dans Braze lorsque vous créez des campagnes.

Similaires aux [cartes de contenu]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/about/), les cartes bannières sont intégrées directement dans votre application ou votre site web afin que vous puissiez engager les utilisateurs avec une expérience sur type bannière. Ils constituent une solution rapide et fluide pour créer des messages personnalisés pour vos utilisateurs tout en étendant la portée d'autres canaux (tels que l'e-mail ou les notifications push). 

Les cartes bannières sont idéales pour :

- Mise en avant des fonctionnalités
- Informer les utilisateurs des événements à venir
- Partager des mises à jour sur les programmes de fidélisation

Parce que les cartes bannières se personnalisent à chaque fois qu'un utilisateur démarre une nouvelle session et qu'elles peuvent être configurées pour ne jamais expirer, elles constituent un outil utile à ajouter à votre stratégie d'engagement.

{% alert important %}
Les cartes bannières sont actuellement en accès anticipé. Contactez votre gestionnaire de compte Braze si vous souhaitez participer à cet accès anticipé.
{% endalert %}

## Prérequis : Déterminer le placement

Avant de créer une carte bannière, vous devez désigner les zones de votre application où vous souhaitez afficher la carte bannière. C'est ce que l'on appelle le placement. Après avoir créé un placement, vous pouvez le sélectionner lors de la création de votre campagne de cartes bannières. Si vous avez déjà un placement, passez à l'[étape 1](#step-1-create-your-campaign).

Pour créer un placement :

1. Allez dans **Réglages** > **Placement des cartes bannières**.
2. Donnez un nom à l'emplacement de votre carte bannière.
3. (Facultatif) Ajoutez une description pour expliquer où cette carte bannière est destinée à être placée.
4. Saisissez un ID de placement unique. Travaillez avec votre équipe de développeurs pour définir cet ID, car ils devront l'utiliser lors de l'intégration. Évitez de modifier votre ID de placement après le lancement, car cela peut rompre l'intégration avec votre app ou votre site web.
5. Sélectionnez **Enregistrer**.

Chaque placement peut être utilisé dans un maximum de 10 campagnes. 

{% alert important %}
Les ID de placement sont uniques par espace de travail.
{% endalert %}

## Étape 1 : Créer votre campagne

Après avoir déterminé l'emplacement de votre Banner Card, il est temps de créer votre campagne.

1. Allez dans **Messagerie** > **Campagnes** et sélectionnez **Créer une campagne**.
2. Sélectionnez **Banner Card**.
3. Donnez un nom clair et significatif à votre campagne.
4. Ajoutez des Teams et des tags si nécessaire. Les balises facilitent la recherche et l’identification des campagnes, et la création de rapports. Par exemple, lorsque vous utilisez le générateur de rapports, vous pouvez filtrer par les étiquettes pertinentes.
5. Sélectionnez un [placement à](#prerequisite-determine-placement) associer à votre campagne. C'est l'endroit où la carte bannière apparaîtra dans votre application ou votre site.
6. Ajoutez et nommez autant de variantes que vous le souhaitez pour votre campagne. Vous pouvez choisir différents types de messages et de mises en page pour chaque variante ajoutée. Pour plus d'informations sur les variantes, reportez-vous au [test multivarié et au test A/B]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/).

## Étape 2 : Composer une carte-bannière

Pour modifier les détails du contenu de votre message :

1. Sélectionnez **Modifier message**. Le compositeur ouvrira.
2. Choisissez un style de ligne qui correspond à votre message. Glissez-déposez une ligne dans la zone du canvas.
3. Glissez-déposez des blocs dans la rangée pour créer votre message.
4. Définissez le [style de](#styles) votre message.

### Styles

Sélectionnez **Style** pour ajuster les paramètres à appliquer à tous les blocs du message.

![Panneau de style du compositeur Banner Card.]({% image_buster /assets/img/banner_cards/banner_card_styles.png %})

Ici, vous pouvez fournir un style personnalisé tel que les propriétés de l'arrière-plan, les paramètres de la bordure et les valeurs par défaut de vos cartes bannières. Les styles appliqués ici peuvent être remplacés pour un bloc ou une ligne spécifique. Pour remplacer les styles, sélectionnez le bloc ou la ligne en question afin d'afficher ses propriétés et d'apporter des modifications.

### Comportement lors du clic

Lorsque votre client clique sur un lien dans la carte-bannière, vous pouvez soit le faire naviguer plus profondément dans votre application, soit le rediriger vers une autre page web.

Vous pouvez également choisir d'enregistrer un attribut personnalisé ou un événement personnalisé. Cela permettra de mettre à jour le profil de votre client avec des données personnalisées lorsqu'il cliquera sur la carte bannière.

## Étape 3 : Créez le reste de votre campagne

Concevez ensuite le reste de votre campagne. Reportez-vous aux sections suivantes pour plus de détails sur la meilleure façon d'utiliser nos outils pour créer des cartes bannières.

### Choisissez une durée de campagne

Sélectionnez la date et l'heure de début de la campagne de la carte bannière. 

Par défaut, les cartes bannières durent indéfiniment. Si vous le souhaitez, sélectionnez **Heure de fin** pour spécifier une date et une heure de fin.

### Choisir les utilisateurs à cibler

Ensuite, ciblez les utilisateurs en choisissant des segments ou des filtres pour réduire votre audience. Vous obtiendrez automatiquement un aperçu de ce à quoi ressemble la population de ce segment approximatif à l'heure actuelle. Gardez à l’esprit que l’appartenance à un segment exact est toujours calculée juste avant l’envoi du message.

### Sélectionner des événements de conversion

Braze vous permet de suivre la fréquence à laquelle les utilisateurs effectuent des actions spécifiques, et les événements de conversion, après avoir reçu une campagne. Vous pouvez autoriser une fenêtre de 30 jours maximum pendant laquelle une conversion sera comptabilisée si l’utilisateur effectue l’action spécifiée.

## Étape 4 : Test et déploiement

Après avoir créé votre campagne, testez-la et examinez-la pour vous assurer qu'elle fonctionne comme prévu. Vous êtes alors prêt à lancer votre campagne de cartes bannières !

## Choses à savoir

### Expiration des cartes bannières

Par défaut, les Banner Cards n'ont pas de date d'expiration, mais vous pouvez ajouter une date de fin facultative.

### Gestion des placements

Les placements sont uniques par espace de travail et chaque placement peut être utilisé dans un maximum de 10 campagnes.

Les ID de placement doivent être uniques pour un espace de travail et ne doivent pas être modifiés après le lancement. Travaillez avec votre équipe de développeurs pour définir cet ID, car ils devront l'utiliser lors de l'intégration. 

### Analyse

Le tableau suivant définit les indicateurs clés de Banner Card.

<style>
    .no-split {
        word-break: keep-all;
    }
</style>

<table>
    <thead>
        <tr>
            <th>Indicateur</th>
            <th>Définition</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td class="no-split"><a href='https://braze.com/docs/user_guide/data_and_analytics/report_metrics#total-impressions'>Impressions totales</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Total Impressions' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href='https://www.braze.com/docs/user_guide/data_and_analytics/report_metrics#unique-impressions'>Impressions uniques</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Unique Impressions' %} Each user is only counted once.</td>
        </tr>
        <tr>
            <td class="no-split"><a href='https://www.braze.com/docs/user_guide/data_and_analytics/report_metrics#total-clicks'>Nombre total de clics</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Total Clicks' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href='https://www.braze.com/docs/user_guide/data_and_analytics/report_metrics#unique-clicks'>Clics uniques</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Unique Clicks' %} Each user is only counted once.</td>
        </tr>
        <tr>
            <td class="no-split"><a href='https://www.braze.com/docs/user_guide/data_and_analytics/report_metrics#primary-conversions-a-or-primary-conversion-event'>Conversions primaires</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Primary Conversions (A) or Primary Conversion Event' %}<ul><li>{% multi_lang_include metrics.md metric='Conversions (B, C, D)' %}</li><li>{% multi_lang_include metrics.md metric='Conversion Rate' %}</li></ul></td>
        </tr>
    </tbody>
</table>

Pour une liste complète des indicateurs, des définitions et des calculs, consultez notre [glossaire des indicateurs du rapport.]({{site.baseurl}}/user_guide/data_and_analytics/report_metrics/)
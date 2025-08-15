---
nav_title: Reporting
article_title: Rapports LINE
page_order: 4
description: "Cet article de référence décrit les indicateurs LINE utilisés chez Braze, ainsi que la façon de les visualiser dans vos campagnes LINE."
page_type: reference
channel:
 - LINE
alias: /line/reporting/
---

# Rapports LINE

> Après avoir lancé votre campagne ou Canvas, vous pouvez consulter les indicateurs clés sur la page des détails de la campagne ou des analyses de Canvas. Cet article explique où vous pouvez trouver ces indicateurs et ce qu'ils représentent.

{% alert tip %}
Vous cherchez des définitions pour les termes et les indicateurs de votre rapport ? Reportez-vous au [glossaire des indicateurs de rapport]({{site.baseurl}}/user_guide/data/report_metrics/).
{% endalert %}

## Analyse de campagne

Dans l'onglet **Analyse/analytique de la campagne**, vous pouvez consulter vos rapports dans une série d'adjectifs. Vous pouvez en voir plus ou moins que ceux énumérés dans les sections ci-dessous, mais chacun a sa raison d'être.

{% alert note %}
Les statistiques d'ouverture et de clics pour LINE ne sont calculées que si plus de 20 utilisateurs effectuent l'événement un jour donné.
{% endalert %}

### Détails de la campagne

Le panneau **Détails de la campagne** donne un aperçu de haut niveau des performances de vos messages LINE.

Examinez ce panneau pour voir les indicateurs globaux tels que le nombre de messages envoyés au nombre de destinataires, le taux de conversion primaire et le chiffre d'affaires total généré par ce message. Vous pouvez également consulter les paramètres de livraison, d'audience et de conversion à partir de cette page.

#### Groupes de contrôles

Pour mesurer l'impact d'un message LINE individuel, vous pouvez ajouter un [groupe de contrôle]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/) à un test A/B. Le panneau supérieur **Détails de la campagne** n'inclut pas les indicateurs de la variante Groupe de contrôle.

### Performance de la ligne

Le tableau de bord **LINE Performance** indique le niveau de performance de votre message en fonction de différents critères. Les indicateurs de ce volet varient en fonction de votre canal de communication choisi, et selon que vous exécutez ou non un test multivarié. Vous pouvez cliquer sur l'icône <i class="fa fa-eye preview-icon"></i> **Preview** pour visualiser votre message pour chaque variante ou canal de communication.

![Le panneau "LINE Performance" montre les indicateurs pour deux variantes.]({% image_buster /assets/img/line/line_performance.png %})

Si vous souhaitez simplifier votre vue, sélectionnez **\+ Ajouter/Supprimer des colonnes** et effacez les indicateurs souhaités. Par défaut, tous les indicateurs sont affichés.

#### Indicateurs LINE

Voici quelques indicateurs clés de LINE que vous pouvez voir dans vos analyses/analytiques. Pour connaître les définitions de tous les indicateurs LINE utilisés dans Braze, consultez le [glossaire des indicateurs de rapport]({{site.baseurl}}/user_guide/data/report_metrics/).

| Terme | Définition |
| --- | --- |
| Envois | Nombre total d'envois communiqués avec succès entre Braze et LINE. Cela ne signifie pas que le message a été reçu par l'utilisateur. |
| Ouvertures uniques | Nombre total d'envois de messages LINE qui ont été ouverts par les utilisateurs après qu'un seuil minimum de 20 messages par jour a été atteint. |
| Nombre total d’ouvertures | Nombre total de fois où les messages LINE envoyés ont été ouverts par les utilisateurs après qu'un seuil minimum de 20 messages par jour a été atteint. |
| Clics uniques | Le nombre total d'envois de messages LINE qui ont été cliqués par les utilisateurs, après qu'un seuil minimum de 20 messages par jour a été atteint. |
| Nombre total de clics | Nombre total de fois où les messages LINE envoyés ont été cliqués par les utilisateurs après qu'un seuil minimum de 20 messages par jour a été atteint. |
{: .reset-td-br-1 .reset-td-br-2 }

### Performances historiques

Le panneau **Performances historiques** vous permet de visualiser les indicateurs du panneau **Performances des messages** sous la forme d'un graphique dans le temps. Utilisez les filtres en haut du volet pour modifier les statistiques et les canaux affichés dans le graphique. La plage temporelle de ce graphique reflète toujours la plage de temps spécifiée en haut de la page.

Pour obtenir une ventilation jour par jour, sélectionnez le menu hamburger <i class="fas fa-bars"></i> et sélectionnez **Télécharger CSV** pour recevoir une exportation CSV du rapport.

### Détails de l'événement de conversion
 
Le panneau **Détails de l'événement de conversion** vous indique les performances de vos événements de conversion pour votre campagne. Pour plus d'informations, reportez-vous à la section [Événements de conversion]({{site.baseurl}}/user_guide/engagement_tools/testing/conversion_correlation).

### Corrélation de conversion

Le panneau **Corrélation de conversion** vous donne des informations sur les attributs et les comportements des utilisateurs qui favorisent ou entravent les résultats que vous avez définis pour les campagnes. Pour plus d'informations, consultez la section [Corrélation de conversion]({{site.baseurl}}/user_guide/engagement_tools/testing/conversion_correlation).



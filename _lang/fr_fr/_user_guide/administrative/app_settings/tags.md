---
nav_title: Tags
article_title: Tags
page_order: 12
page_type: reference
description: "Cet article de référence traite des tags dans le tableau de bord de Braze, que vous pouvez utiliser pour organiser et trier davantage votre engagement."

---
# Tags

> Braze assure le suivi des informations relatives à l'auteur, à l'éditeur, à la date et au statut des segments, des campagnes et des canevas, et vous donne la possibilité de créer des tags pour mieux organiser et trier votre engagement.

## Tags de campagne, de canvas et de segmentation

Vous pouvez ajouter des tags lorsque vous créez ou modifiez une campagne, un Canvas ou un segment. Cliquez sur <span style="font-size: 14px;margin-bottom: .5rem;height: 16px;width: 16px;" class="fas fa-tag" ></span>**Tags** sous le nom de l'engagement et sélectionnez une étiquette existante, ou commencez à taper pour ajouter une nouvelle étiquette.

!Ajout de tags lors de la création de la campagne.]({% image_buster /assets/img_archive/tags_add_tag.png %}){: style="max-width:60%;" }

{% alert important %}
Vous pouvez ajouter jusqu'à 175 tags à une campagne, un Canvas ou un segment.
{% endalert %}

### Étiquettes en vrac

Vous pouvez également ajouter des étiquettes à plusieurs campagnes, canevas ou segments en sélectionnant plusieurs engagements et en sélectionnant <span style="font-size: 14px;margin-bottom: .5rem;height: 16px;width: 16px;" class="fas fa-tag" ></span>**Tag As.**

!Ajout de tags à plusieurs campagnes en même temps.]({% image_buster /assets/img_archive/tags_apply_multiple.gif %})

{% alert important %}
Lorsque vous utilisez le marquage en bloc pour appliquer une nouvelle étiquette à plusieurs campagnes qui ont déjà des étiquettes différentes, chaque campagne sélectionnée recevra la nouvelle étiquette, et toutes les étiquettes présentes sur une campagne seront appliquées à toutes les autres campagnes sélectionnées, même si ces étiquettes ne leur étaient pas associées à l'origine.
{% endalert %}

### Affichage des tags

Les tags définis sur une campagne, un Canvas ou un segment sont visibles sur la page de détails près du nom de l'engagement. Ils apparaissent également dans les analyses/analytiques de la campagne (s'ils sont utilisés comme adjectifs).

\![Tags affichés sur la page d'analyse/analytique de la campagne (si utilisés comme adjectifs).]({% image_buster /assets/img_archive/tag_details_page.png %}){: style="max-width:60%;" }

### Filtrage par étiquette

Les étiquettes sont visibles dans la liste des campagnes, des toiles ou des segments, ainsi que des tags supplémentaires pour les étiquettes d'état telles que **Archivé** et **Brouillon**. Pour filtrer par étiquette, sélectionnez le nom de l'étiquette dans la liste des étiquettes.

!Tags sur la liste des campagnes.]({% image_buster /assets/img_archive/tags_grid.png %})

## Tags de données personnalisés

Des étiquettes peuvent également être ajoutées aux données personnalisées lors de la gestion des [attributs]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#managing-custom-attributes) et des [événements personnalisés]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#managing-custom-events). 

{% alert important %}
Cette fonctionnalité est actuellement en accès anticipé. Contactez votre gestionnaire satisfaction client si vous souhaitez participer à cet accès anticipé.
{% endalert %}

## Gestion des étiquettes

Vous pouvez utiliser les mêmes étiquettes pour toutes les campagnes, toutes les campagnes et tous les segments. Pour renommer, supprimer ou ajouter des tags de manière efficace dans votre tableau de bord, accédez à **Paramètres** > **Gestion des tags**.

! [onglet Étiquettes de la page Gérer les paramètres.]({% image_buster /assets/img_archive/tags_view.png %})

Pour mieux organiser vos tags, imbriquez-les sous un tag parent. Par exemple, vous pouvez regrouper tous les tags relatifs aux fêtes sous une étiquette parentale `Holidays`, ou tous les tags relatifs à une étape de votre entonnoir marketing sous une étiquette parentale `Funnel`. 

Pour ce faire, créez un nouveau tag, sélectionnez **Nest Tag Under**, et choisissez le tag existant sous lequel vous souhaitez imbriquer votre nouveau tag. Vous pouvez également imbriquer des étiquettes existantes à partir de la page **Gestion des étiquettes.**  Sur cette page, passez la souris sur une ligne contenant votre étiquette et cliquez sur **<i class="fas fa-pencil-alt"></i>Modifier**. Ensuite, suivez les mêmes étapes que précédemment.

\![Créer une étiquette imbriquée.]({% image_buster /assets/img_archive/tag_nested.png %}){: style="max-width:70%;" }

## Meilleures pratiques {#tags-best-practices}

Les étiquettes peuvent être un outil d'organisation utile pour garder une trace des tactiques d'engagement. Vous pouvez relier les segments et les campagnes aux objectifs de l'entreprise, aux étapes de l'entonnoir, etc.

Voici un exemple d'étiquettes qu'une application de commerce électronique pourrait trouver utiles :

<style>
table td {
    word-break: break-word;
}
</style>


<table>
<thead>
  <tr>
    <th>Entonnoir</th>
    <th>Objectifs de l'entreprise</th>
    <th>Régionale</th>
    <th>Campagnes</th>
    <th>Vacances</th>
    <th>Transactions</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>Embarquement<br>Réengagement<br>Fidèle<br>PowerUser<br>Désabonner<br>Perdu</td>
    <td>HighSpender<br>Utilisateur actif<br>Nouveaux utilisateurs<br>FacebookAttribution<br>Première action</td>
    <td>États-Unis<br>Nord-Est<br>Midwest<br>Sud<br>Ouest<br>LATAM<br>AP<br>Europe occidentale<br>Moyen-Orient</td>
    <td>Vente<br>Coupons<br>Evénements</td>
    <td>MLK<br>SuperBowl<br>PiDay<br>Fête de la St-Patrick<br>La folie du mois de mars<br>Pâques<br>Pâque<br>Fête des mères<br>Journée du souvenir<br>Fête des pères<br>Quatrième juillet<br>Fête du travail<br>Journée des vétérans<br>ColumbusDay<br>Jour du Président<br>Halloween<br>RoshHashanah<br>Thanksgiving<br>Noël<br>Hanoukka<br>Nouvelles années</td>
    <td>Transactionnel<br>Notification<br>Action connectée</td>
  </tr>
</tbody>
</table>

## Cas d'utilisation

Vous voulez savoir comment utiliser les tags pour gérer le cycle de vie de vos messages ? Voici quelques cas d'utilisation courants.

{% tabs %}
{% tab Throttling %}

### L'étranglement

Limitez la fréquence à laquelle vos clients reçoivent des campagnes d'un certain type. Par exemple, vous pouvez définir les filtres suivants pour limiter la fréquence des campagnes promotionnelles :

`Last received campaign` avec l'étiquette `Promo` il y a plus de 5 jours
<br>`OR`<br>
`Has not received campaign` avec étiquette `Promo`

{% endtab %}
{% tab Reporting %}

### Rapports

Implantez un rapport d'engagement pour garder un œil sur le volume de toutes les campagnes avec une certaine étiquette. Par exemple, si vous souhaitez surveiller toutes vos campagnes push, vous pouvez ajouter une étiquette telle que `Push Reporting` à ces campagnes, puis implémenter un [rapport d'engagement]({{site.baseurl}}/user_guide/data_and_analytics/reporting/engagement_reports/#automatically-select-campaigns-or-canvases) qui vous enverra chaque jour un rapport sur ces campagnes étiquetées.

{% endtab %}
{% endtabs %}
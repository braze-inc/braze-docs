---
nav_title: Balises
article_title: Balises
page_order: 12
page_type: reference
description: "Cet article de référence couvre les balises du tableau de bord de Braze, que vous pouvez utiliser pour organiser et trier de manière plus précise votre projet."

---
# Balises

> Braze suit l’auteur, l’éditeur, la date et l’état des informations sur les segments, campagnes et Canvas, et vous donne la possibilité de créer des balises pour organiser et trier de manière plus précise votre projet.

## Balises campagne, Canvas et segment

Vous pouvez ajouter des balises lors de la création ou de la modification d’une campagne, d’un Canvas ou d’un segment. Cliquez sur <span style="font-size: 14px;margin-bottom: .5rem;height: 16px;width: 16px;" class="fas fa-tag" ></span>**Tags** sous le nom de l'engagement et sélectionnez une étiquette existante, ou commencez à taper pour ajouter une nouvelle étiquette.

![Ajout de balises pendant la création de campagnes][2]

Vous pouvez également ajouter des tags à plusieurs campagnes, canevas ou segments en sélectionnant plusieurs engagements et en cliquant sur <span style="font-size: 14px;margin-bottom: .5rem;height: 16px;width: 16px;" class="fas fa-tag" ></span>**Tag As.**

![Ajout de balises à plusieurs campagnes en même temps][5]

Les balises définies sur une campagne, un Canvas ou un segment sont visibles sur la page de détail à côté du nom de l’engagement.

![Balises affichées sur la page Campaign Details (Détails de la campagne)][3]

Ils sont également visibles dans la liste des campagnes, des toiles ou des segments, avec des tags supplémentaires pour les étiquettes d'état telles que **Archivé** et **Brouillon.**

![Tags sur la liste des campagnes][4]{: style ="max-width:70%;" }

Pour filtrer par une balise, sélectionnez le nom de la balise dans la liste des balises ou recherchez la balise dans le volet de recherche à l’aide du sélecteur `tag:`. Par exemple, pour rechercher la balise `Onboarding`, saisissez « tag:Onboarding ».

![Recherche de toutes les campagnes marquées comme e-mail de bienvenue][6]

{% alert important %}
Vous pouvez ajouter jusqu'à 175 tags à une campagne, un Canvas ou un segment.
{% endalert %}

## Tags de données personnalisés

Des étiquettes peuvent également être ajoutées aux données personnalisées lors de la gestion des [attributs personnalisés]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#managing-custom-attributes) et des [événements personnalisés]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#managing-custom-events). 

{% alert important %}
Cette fonctionnalité est actuellement disponible en accès anticipé. Si vous souhaitez participer à cet accès anticipé, contactez votre gestionnaire de la satisfaction client.
{% endalert %}

## Bonnes pratiques {#tags-best-practices}

Les balises peuvent être un outil organisationnel utile pour suivre les tactiques d’engagement. Vous pouvez lier des segments et des campagnes à des objectifs commerciaux, à des étapes d’entonnoir et autres.

Voici un exemple d'étiquettes qu'une application de commerce électronique pourrait trouver utiles :

<style>
table td {
    word-break: break-word;
}
</style>


<table>
<thead>
  <tr>
    <th>Entonnoir</th>
    <th>Objectifs commerciaux</th>
    <th>Régional</th>
    <th>Campagnes</th>
    <th>Jours fériés</th>
    <th>Transactions</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>On-boarding<br>Ré-engagement<br>Loyal<br>PowerUser<br>Attrition<br>Lost</td>
    <td>HighSpender<br>ActiveUser<br>NewUsers<br>FacebookAttribution<br>FirstAction</td>
    <td>UnitedStates<br>Northeast<br>Midwest<br>South<br>West<br>LATAM<br>AP<br>WesternEurope<br>MiddleEast</td>
    <td>Sales<br>Coupons<br>Événements</td>
    <td>MLK<br>SuperBowl<br>PiDay<br>StPatricksDay<br>MarchMadness<br>Easter<br>Passover<br>MothersDay<br>MemorialDay<br>FathersDay<br>FourthJuly<br>LaborDay<br>VeteransDay<br>ColumbusDay<br>PresidentsDay<br>Halloween<br>RoshHashanah<br>Thanksgiving<br>Christmas<br>Hanukkah<br>NewYears</td>
    <td>Transactionnel<br>Notification<br>ConnectedActionTaken</td>
  </tr>
</tbody>
</table>

Vous pouvez utiliser les mêmes balises sur les campagnes, les Canvas et les segments. Pour renommer, supprimer ou ajouter des tags de manière efficace dans votre tableau de bord, accédez à **Paramètres** > **Gestion des tags**.

{% alert note %}
Si vous utilisez l'[ancienne version de navigation]({{site.baseurl}}/navigation), cette page se trouve dans **Paramètres** > **Gérer les paramètres** > **Étiquettes**.
{% endalert %}

![Onglet Balises de la page Gérer les paramètres][8]

Pour une meilleure organisation des balises, elles peuvent être insérées sous une balise parent. Toutes les balises de vacances peuvent par exemple être insérées sous une `Holidays`balise parent, ou toutes les balises liées à une étape de l’entonnoir marketing sous une balise parent`Funnel`. 

Pour ce faire, créez un nouveau tag, sélectionnez **Nest Tag Under**, et choisissez le tag existant sous lequel vous souhaitez imbriquer votre nouveau tag. Vous pouvez également imbriquer des étiquettes existantes à partir de la page **Gestion des étiquettes**. Sur cette page, passez la souris sur une ligne contenant votre étiquette et cliquez sur **<i class="fas fa-pencil-alt"></i>Modifier**. Ensuite, suivez les mêmes étapes que précédemment.

![Créer une étiquette imbriquée][1]{: style ="max-width:70%;" }

## Cas d’utilisation

Vous cherchez de l’inspiration sur la façon d’exploiter les balises pour gérer le cycle de vie de votre messagerie ? Voici quelques exemples d’utilisation courante :

### Étranglement

Limitez la fréquence à laquelle vos clients reçoivent des campagnes d’un certain type. Par exemple, vous pouvez définir les filtres suivants pour limiter la fréquence des campagnes promotionnelles :

`Last received campaign` avec balise `Promo` il y a plus de 5 jours
<br>`OR`<br>
`Has not received campaign` avec balise `Promo`

### Reporting

Configurez un Engagement Report pour garder un œil sur le volume de toutes les campagnes avec une certaine balise. Par exemple, si vous souhaitez surveiller toutes vos campagnes push, vous pouvez ajouter une étiquette telle que `Push Reporting` à ces campagnes, puis implémenter un [rapport d'engagement]({{site.baseurl}}/user_guide/data_and_analytics/reporting/engagement_reports/#automatically-select-campaigns-or-canvases) qui vous enverra chaque jour un rapport sur ces campagnes étiquetées.



[1]: {% image_buster /assets/img_archive/tag_nested.png %}
[2]: {% image_buster /assets/img_archive/tags_add_tag.png %}
[3]: {% image_buster /assets/img_archive/tag_details_page.png %}
[4]: {% image_buster /assets/img_archive/tags_grid.png %}
[5]: {% image_buster /assets/img_archive/tags_apply_multiple.png %}
[6]: {% image_buster /assets/img_archive/tags_filtering.png %}
[7]: {% image_buster /assets/img_archive/Tags-Potential_Tags.png %}
[8]: {% image_buster /assets/img_archive/tags_view.png %}

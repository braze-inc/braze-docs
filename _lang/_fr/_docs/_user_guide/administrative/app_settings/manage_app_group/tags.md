---
nav_title: Tags
article_title: Tags
page_order: 2
page_type: Référence
description: "Cet article de référence couvre les tags dans le tableau de bord de Braze, que vous pouvez utiliser pour organiser et trier votre engagement."
---

# Tags

Braze suit l'auteur, l'éditeur, la date et l'état des informations sur les segments, les campagnes et les Canvases, et vous donne la possibilité de créer des tags pour organiser et trier votre engagement.

## Balises de campagne, Canvas et segment

Vous pouvez ajouter des tags lors de la création ou de l'édition d'une campagne, de Canvas ou d'un segment. Cliquez sur <span style="font-size: 14px;margin-bottom: .5rem;height: 16px;width: 16px;" class="fas fa-tag" ></span>**Tags** en dessous du nom de l'engagement et sélectionnez un tag existant, ou commencez à taper pour ajouter un nouveau tag.

!\[Création de la campagne\]\[2\]

Vous pouvez également ajouter des balises à plusieurs campagnes, Canvases ou segments en sélectionnant plusieurs engagements et en cliquant sur <span style="font-size: 14px;margin-bottom: .5rem;height: 16px;width: 16px;" class="fas fa-tag" ></span>**Tag as**.

!\[Tagging multiple\]\[5\]

Les balises définies sur une campagne, Canvas ou segment sont visibles sur la page de détail sous le nom de la participation.

!\[Détails de la campagne\]\[3\]

Ils sont également visibles dans la liste des campagnes, des vases, ou des segments comme des bulles au-dessus du nom de l'engagement, ainsi que les étiquettes de statut telles que **Archivées** et **Brouillon**.

!\[Campaigns\]\[4\]{: style ="max-width:70%;" }

Pour filtrer par tag, sélectionnez le nom de la balise dans la barre d'outils de gauche ou recherchez la balise dans le volet de recherche en utilisant la balise `:` sélecteur. Par exemple, pour rechercher la balise `Onboarding` , entrez "tag:Onboarding".

!\[Tag Search for Campaigns and Segments\]\[6\]

## Meilleures pratiques {#tags-best-practices}

Les balises peuvent être un outil organisationnel utile pour garder une trace des tactiques d'engagement. Vous pouvez relier les segments et les campagnes aux objectifs de l’entreprise, aux étapes de l’entonnoir et autres.

Ci-dessous est un exemple de tags qu'une application eCommerce peut trouver utile:

!\[Potential Tags\]\[7\]

Vous pouvez utiliser les mêmes balises à travers les campagnes, les canevas et les segments. Pour renommer, supprimer ou ajouter efficacement des tags dans votre tableau de bord, allez à la page **Gérer les paramètres** et sélectionnez l'onglet **Tags**.

!\[affichage des balises\]\[8\]

Pour organiser davantage vos tags, imbriquez vos tags sous un tag parent. Par exemple, vous pouvez garder toutes les balises de vacances imbriquées sous un tag parent `Holidays` , ou tous les tags liés à une étape de votre entonnoir de marketing sous un tag `Entonnoir` parent.

Pour ce faire, créez un nouveau tag, sélectionnez **Nest Tag Under**et choisissez le tag existant pour imbriquer votre nouveau tag. Vous pouvez également imbriquer les tags existants à partir de **Gérer les paramètres** > **Tags**. Sur cette page, survolez une ligne avec votre tag et cliquez sur **<i class="fas fa-pencil-alt"></i>Modifier**. Ensuite, suivez les mêmes étapes qu'avant.

!\[Create a nested tag\]\[1\]{: style ="max-width:70%;" }

## Cas d'utilisation

Vous cherchez de l'inspiration sur la façon de tirer parti des tags pour gérer votre cycle de vie de la messagerie ? Voici quelques cas d'utilisation courants:

### Grottling

Limitez la fréquence à laquelle vos clients reçoivent des campagnes d'un certain type. Par exemple, vous pouvez définir les filtres suivants pour limiter la fréquence des campagnes promotionnelles :

`La dernière campagne reçue` avec le tag `Promo` il y a plus de 5 jours <br>`OU`<br> `N'a pas reçu la campagne` avec le tag `Promo`

### Rapports

Mettre en place un rapport d'engagement pour garder un œil sur le volume de toutes les campagnes avec un certain tag. Par exemple, si vous voulez surveiller toutes vos campagnes de push, vous pourriez ajouter un tag comme `Rapport Push` à ces campagnes, puis mettez en place un [Rapport d'Engagement]({{site.baseurl}}/user_guide/data_and_analytics/your_reports/engagement_reports/#automatically-select-campaigns-or-canvases) pour vous envoyer un rapport de ces campagnes taggées chaque jour.
[1]: {% image_buster /assets/img_archive/tag_nested.png %} [2]: {% image_buster /assets/img_archive/tags_add_tag. ng %} [3]: {% image_buster /assets/img_archive/tag_details_page.png %} [4]: {% image_buster /assets/img_archive/tags_grid. ng %} [5]: {% image_buster /assets/img_archive/tags_apply_multiple.png %} [6]: {% image_buster /assets/img_archive/tags_filtering. ng %} [7]: {% image_buster /assets/img_archive/Tags-Potential_Tags.png %} [8]: {% image_buster /assets/img_archive/tags_view.png %}

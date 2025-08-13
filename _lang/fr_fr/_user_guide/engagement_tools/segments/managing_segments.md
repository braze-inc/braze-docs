---
nav_title: Gestion des segments
article_title: Gestion des segments
page_order: 1
page_type: tutorial
tool: Segments
description: "Cet article couvre les actions que vous pouvez entreprendre pour gérer vos segments, telles que filtrer une liste de segments, créer des segments et modifier des segments."

---

# Gestion des segments

> La section Segments vous permet d'afficher une liste complète de vos segments existants, de créer de nouveaux segments et de modifier des segments existants. Vous pouvez affiner la liste des segmentations en sélectionnant divers filtres et colonnes afin de n'afficher que les informations les plus pertinentes pour vous.

![La section Segments affiche une liste des segments actifs.]({% image_buster /assets/img/segment/segments_page.png %})

## Personnaliser votre vue

Personnalisez votre vue de la liste des segments en utilisant des filtres et en modifiant les colonnes que vous souhaitez voir apparaître. Lorsque vous quittez la section **Segments** et que vous y revenez, la liste revient à l'affichage par défaut, ce qui efface tous les filtres que vous avez sélectionnés précédemment.

### Filtre d'état

Vous pouvez réduire la liste pour n'afficher que les segments actifs ou archivés. Tout segment non archivé est considéré comme actif.

### Filtres

Triez les segments de la liste en définissant les filtres suivants :
- **Dernière modification par :** L'utilisateur qui a modifié les segments pour la dernière fois
- **Dernière modification :** Période au cours de laquelle les segments ont été modifiés pour la dernière fois
- **Taille estimée :** Nombre approximatif d'utilisateurs dans les segments
- **Tags :** Tags associés aux segments
- **Teams :** Teams associés aux segments
- **Segments de suivi avancés uniquement :** Affichez uniquement les segments pour lesquels le [suivi des analyses]({{site.baseurl}}/user_guide/data_and_analytics/tracking/segment_analytics_tracking#segment-analytics-tracking) est activé.

### Colonnes

Il s'agit des colonnes d'informations que vous pouvez sélectionner pour les afficher dans la liste des segments :
- **Filtres :** Nombre de filtres dans la segmentation
- **Dernière modification :** Date à laquelle le segment a été modifié pour la dernière fois
- **Dernière modification par :** L'utilisateur qui a modifié le segment pour la dernière fois
- **Tags :** Tags associés au segmentation
- **Teams :** Teams associés au segmentation
- **Taille estimée :** Estimation du nombre d'utilisateurs dans le segment
- **Canvas :** Nombre de toiles qui utilisent le segment
- **Campagnes :** Nombre de campagnes utilisant le segment

### Afficher uniquement les étoilés

En sélectionnant **Afficher uniquement les** segments marqués d'un astérisque, vous réduisez votre affichage aux segments que vous avez marqués d'un astérisque.

## Gérer des segments spécifiques

![Le menu de modification d'un segment présente les options "Modifier", "Dupliquer", "Archiver" et "Ajouter à la liste".]({% image_buster /assets/img/segment/segments_page_edit_menu.png %}){: style="float:right;max-width:25%;"}

Pour gérer un segment spécifique, survolez-le et sélectionnez l'icône de menu au bout de la ligne pour faire apparaître les options suivantes :
- **Modifier :** Modifiez les filtres de votre segmentation.
- **Dupliquer :** Faites une copie de votre segmentation.
- **Archiver :** Archivez le segment. Notez que cela archivera également toutes les campagnes ou Canvases qui utilisent ce segment.
- **Ajouter aux segments étoilés :** Étoilez le segment, ce qui vous permet d'y accéder rapidement en cochant la case Afficher uniquement les étoiles dans la section des segments.
 
Vous pouvez également effectuer des actions en masse, notamment l'archivage et le tagging en masse, en cochant les cases situées à côté de plusieurs noms de segments.

![Plusieurs segments sélectionnés avec "CRM" dans le champ déroulant "Tag As".]({% image_buster /assets/img/segment/segments_bulk_action.png %}){: style="max-width:45%;"}

### modifications depuis la dernière consultation

Le nombre de mises à jour des segments par d'autres membres de votre équipe est suivi par l'indicateur *Changements depuis le dernier affichage* sur la page d'aperçu du segment. Sélectionnez **Changements depuis la dernière consultation** pour afficher un journal des modifications apportées au nom, à la description et à l'audience cible du segment. Pour chaque mise à jour, vous pouvez voir qui a effectué la mise à jour et quand. Vous pouvez utiliser ce journal des modifications pour auditer les modifications apportées à votre segmentation.

## Recherche de segments
Recherchez des noms de segmentation en saisissant des termes dans le champ de recherche. 

Tous les termes et chaînes de caractères saisis dans ce champ feront l'objet d'une recherche. Par exemple, la recherche de « segment d'essai 1 » renverra les segments dont le nom contient « essai », « segment » ou « 1 ». Pour rechercher une chaîne de caractères exacte, ajoutez des guillemets avant et après votre terme de recherche. En recherchant ["segment d'essai 1"], vous obtiendrez tous les segments dont le nom contient l'expression exacte "segment d'essai 1".

![Les résultats de la recherche d'utilisateurs sont les suivants : "Tous les utilisateurs (Test)", "Tous les utilisateurs", "Tous les utilisateurs 15".]({% image_buster /assets/img/segment/segments_search.png %})


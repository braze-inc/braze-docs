---
nav_title: Gérer les segments
article_title: Gérer les segments
page_order: 1
page_type: tutorial
tool: Segments
description: "Cet article présente les actions disponibles pour gérer vos segments : filtrer une liste de segments, créer des segments et modifier des segments."

---

# Gérer les segments

> La section Segments vous permet de consulter la liste complète de vos segments existants, d'en créer de nouveaux et de modifier ceux qui existent déjà. Vous pouvez affiner cette liste en sélectionnant divers filtres et colonnes afin de n'afficher que les informations les plus pertinentes pour vous.

![La section Segments affiche une liste des segments actifs.]({% image_buster /assets/img/segment/segments_page.png %})

## Personnaliser votre vue

Adaptez votre vue de la liste des segments en utilisant des filtres et en choisissant les colonnes à afficher. Lorsque vous quittez la section **Segments** puis y revenez, la liste revient à l'affichage par défaut et tous les filtres précédemment sélectionnés sont effacés.

### Filtre d'état

Vous pouvez restreindre la liste pour n'afficher que les segments actifs ou archivés. Tout segment non archivé est considéré comme actif.

### Filtres

Triez les segments de la liste en ajustant les filtres suivants :
- **Dernière modification par :** L'utilisateur qui a modifié les segments en dernier
- **Dernière modification :** Période au cours de laquelle les segments ont été modifiés pour la dernière fois
- **Taille estimée :** Fourchette approximative du nombre d'utilisateurs dans les segments
- **Étiquettes :** Étiquettes associées aux segments
- **Équipes :** Équipes associées aux segments
- **Segments avec suivi avancé uniquement :** Affichez uniquement les segments pour lesquels le [suivi analytique]({{site.baseurl}}/user_guide/data_and_analytics/tracking/segment_analytics_tracking#segment-analytics-tracking) est activé.

### Colonnes

Voici les colonnes d'informations que vous pouvez choisir d'afficher dans la liste des segments :
- **Filtres :** Nombre de filtres dans le segment
- **Dernière modification :** Date de la dernière modification du segment
- **Dernière modification par :** L'utilisateur qui a modifié le segment en dernier
- **Étiquettes :** Étiquettes associées au segment
- **Équipes :** Équipes associées au segment
- **Taille estimée :** Estimation du nombre d'utilisateurs dans le segment
- **Canvas :** Nombre de Canvas qui utilisent le segment
- **Campagnes :** Nombre de campagnes qui utilisent le segment

### Afficher uniquement les favoris

En sélectionnant **Afficher uniquement les étoilés**, vous limitez l'affichage aux segments que vous avez marqués d'une étoile.

## Consulter l'utilisation d'un segment dans l'envoi de messages {#messaging-use}

Accédez à la section **Utilisation des messages** d'un segment pour obtenir un aperçu des endroits où ce segment est utilisé, par exemple dans d'autres segments, des campagnes ou des Canvas.

{% alert note %}
Pour éviter les boucles de segments se référençant mutuellement, les segments qui utilisent le filtre **Appartenance à un segment** ne peuvent pas être référencés par d'autres segments. Pour en savoir plus, consultez la section [Filtres de segmentation]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/).
{% endalert %}

## Gérer des segments spécifiques

![Menu de modification d'un segment avec les options Modifier, Dupliquer, Archiver et Ajouter aux favoris.]({% image_buster /assets/img/segment/segments_page_edit_menu.png %}){: style="float:right;max-width:25%;"}

Pour gérer un segment spécifique, survolez-le et sélectionnez l'icône de menu en fin de ligne pour afficher les options suivantes :
- **Modifier :** Modifiez les filtres de votre segment.
- **Dupliquer :** Créez une copie de votre segment.
- **Archiver :** Archivez le segment. Notez que cela archivera également toutes les campagnes ou tous les Canvas qui utilisent ce segment.
- **Ajouter aux favoris :** Marquez le segment d'une étoile pour y accéder rapidement en cochant la case Afficher uniquement les étoilés dans la section des segments.
 
Vous pouvez également effectuer des actions groupées (archivage et étiquetage en masse, notamment) en cochant les cases situées à côté de plusieurs noms de segments.

![Plusieurs segments sélectionnés avec « CRM » sélectionné dans le champ déroulant « Étiqueter en tant que ».]({% image_buster /assets/img/segment/segments_bulk_action.png %}){: style="max-width:45%;"}

### Modifications depuis la dernière consultation

Le nombre de mises à jour apportées aux segments par d'autres membres de votre équipe est suivi grâce à l'indicateur *Modifications depuis la dernière consultation* sur la page d'aperçu du segment. Sélectionnez **Modifications depuis la dernière consultation** pour afficher un journal des modifications portant sur le nom, la description et l'audience cible du segment. Pour chaque mise à jour, vous pouvez voir qui a effectué la modification et quand. Ce journal des modifications vous permet d'auditer les changements apportés à votre segment.

## Rechercher des segments

Recherchez des segments par leur nom en saisissant des termes dans le champ de recherche. 

Tous les termes et chaînes de caractères saisis dans ce champ font l'objet d'une recherche. Par exemple, la recherche de « segment d'essai 1 » renverra les segments dont le nom contient « essai », « segment » ou « 1 ». Pour rechercher une chaîne de caractères exacte, encadrez votre terme de recherche avec des guillemets. En recherchant ["segment d'essai 1"], vous obtiendrez tous les segments dont le nom contient l'expression exacte « segment d'essai 1 ».

![Lorsque vous saisissez « all users » dans le champ de recherche, les résultats incluent « All Users (Test) », « All Users » et « All Users 15 ».]({% image_buster /assets/img/segment/segments_search.png %})

### Segments dans les Canvas

Pour rechercher toutes les références à un segment, y compris celles présentes dans d'autres segments, campagnes ou Canvas, accédez à la section [Utilisation des messages](#messaging-use) du segment. Le filtre **Segment cible** sur la page **Canvas** ne recherche que les segments d'audience Canvas.

![Filtre Segment cible sur la page Canvas.]({% image_buster /assets/img/segment/target_segment.png %}){: style="max-width:45%;"}
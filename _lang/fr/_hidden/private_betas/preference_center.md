---
nav_title: Centre de préférences d’e-mail par glisser-déposer
article_title: Centre de préférences d’e-mail par glisser-déposer
permalink: "/dnd_preference_center/"
description: "Cette page de référence explique comment créer un centre de préférences d'e-mail avec l'éditeur Drag & Drop."
---

# Créer un centre de préférences d’e-mail avec l’éditeur Drag & Drop

Avec l’éditeur Drag & Drop, vous pouvez désormais créer et personnaliser un centre de préférences pour aider à gérer les utilisateurs qui reçoivent certains types de communication. 

{% alert note %}
Le centre de préférences d’e-mail par glisser-déposer est actuellement en accès anticipé. Contactez votre gestionnaire de compte Braze si vous souhaitez participer à l’accès anticipé.
{% endalert %}

## Étape 1 : Créer un centre de préférences d’e-mail

Créez un centre de préférences en accédant à la page **Subscription Group > Email Preference Center (Groupe) d'abonnement > Centre de préférences d'e-mail** dans le tableau de bord. Ici, une liste de centres de préférences personnalisés s’affiche. Cliquez sur **Create New (Créer nouveau)** pour créer un nouveau centre de préférences, ou cliquez sur le nom d’un centre existant pour apporter des modifications.

![][1]

## Étape 2 : Nommez le centre de préférences d’e-mail

Les noms des centres de préférences ne peuvent contenir que des caractères alphanumériques, des tirets ou des traits de soulignement. Le nom que vous fournissez déterminera la syntaxe de la balise Liquid générée. 

Cette balise Liquid peut être incluse dans toutes les campagnes par e-mail sortantes ou les étapes Canvas et dirigera les utilisateurs vers le centre de préférences.

![][2]

## Étape 3 : Ajouter des groupes d'abonnement au centre de préférences

Cliquez sur **Launch Editor (Lancer l’éditeur)** pour commencer à concevoir votre centre de préférences dans l’éditeur Drag & Drop.

### Définir les groupes d'abonnement disponibles
Pour déterminer quels groupes d'abonnements doivent être affichés dans le centre de préférences, cliquez sur le bouton **+ Add subscription groups (+ Ajouter des groupes d'abonnement)** pour lancer un module modal dans lequel les groupes d'abonnement souhaités peuvent être sélectionnés. Après la sélection, cliquez sur le bouton **Add Subscription Groups (Ajouter des groupes d'abonnement)** pour les ajouter au centre de préférences.

Vous pouvez également configurer les groupes d'abonnement sélectionnés en cliquant sur le bloc intelligent et en ajustant les propriétés du bloc.
- Ajuster l'ordre d'affichage des groupes d'abonnement
- Ajouter ou supprimer des groupes d'abonnement supplémentaires
- Inclure des descriptions
- Ajouter ou supprimer une case à cocher « S’abonner à tous »
- Ajouter ou supprimer une case à cocher « Se désabonner de tous »

![][3]{: style="max-width:38%;"} ![][4]{: style="max-width:45%;"}

## Étape 4 : Personnaliser le centre de préférences à l’aide de l’éditeur Drag & Drop

### Définir des styles communs
Vous pouvez définir certains styles pour qu’ils soient appliqués à tous les blocs pertinents dans votre centre de préférences à partir de l’onglet **Common Styles (Styles communs)**. Les styles définis dans cette section sont utilisés partout dans votre message sauf aux endroits où vous les remplacez pour un bloc spécifique. Pour une expérience de conception plus facile, nous vous recommandons de configurer des styles au niveau de la page avant de personnaliser les styles au niveau des blocs.

![][5]{: style="max-width:45%;"}

{% alert tip %}
Pour revenir aux styles communs, cliquez sur le bouton « X » sur les propriétés de chaque bloc. Sélectionnez ensuite le conteneur du message, le bouton « X » du message ou l’arrière-plan de l’éditeur.
{% endalert %}

## Glisser-déposer des composants du centre de préférences

L’éditeur Drag & Drop utilise deux composants principaux pour faciliter et accélérer la composition du centre de préférence : lignes et blocs. Tous les blocs doivent être placés dans une ligne.

{% tabs %}
{% tab Rows %}

Les lignes sont des unités structurelles qui définissent la composition horizontale d’une section du message en utilisant des cellules.

![]({% image_buster /assets/img/preference_center/preference_center6.png %}){: style="max-width:45%;"}

Lorsque vous sélectionnez une ligne, vous pouvez ajouter ou supprimer autant de colonnes que nécessaire de la section de personnalisation des colonnes pour disposer plusieurs éléments de contenu côte à côte.

Vous pouvez également faire glisser pour ajuster la taille des colonnes existantes.

![]({% image_buster /assets/img/preference_center/preference_center7.png %}){: style="max-width:45%;"}

En tant que bonne pratique, formatez vos propriétés de ligne et de colonne avant de formater l’un des blocs à l’intérieur des lignes. Vous pouvez ajuster l’espacement et l’alignement à de nombreux endroits. Il est plus facile de le modifier au fur et à mesure en commençant à la base.

{% endtab %}
{% tab Blocks %}

Les blocs représentent divers types de contenu que vous pouvez utiliser dans votre message. Il suffit d’en faire glisser un à l’intérieur d’un segment de ligne existant et il s’ajustera automatiquement à la largeur de la cellule.

![]({% image_buster /assets/img/preference_center/preference_center8.png %}){: style="max-width:45%;"}

Chaque bloc possède ses propres paramètres, comme un contrôle granulaire sur la marge intérieure. Le panneau latéral droit passe automatiquement à un panneau de style pour l’élément de contenu sélectionné. Pour plus d’informations, voir [Propriétés du bloc éditeur]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/editor_blocks/).

{% endtab %}
{% endtabs %}

## Étape 5 : Personnaliser votre page de confirmation

N’oubliez pas de personnaliser la page de confirmation ! Vous pouvez modifier cette page en cliquant sur **Confirmation Page (Page de confirmation)** en haut de la **fenêtre de l’éditeur Drag & Drop**. Cette page s’affichera pour les utilisateurs après la mise à jour de leurs préférences à l’aide du centre de préférences. Les mêmes capacités de style ci-dessus s’appliquent également à cette page.

![][9]{: style="max-width:65%;"}

## Étape 6 : Prévisualisez et lancez votre centre de préférences

Vous pouvez prévisualiser votre centre de préférences en cliquant sur l’onglet **Preview (Aperçu)** dans l’éditeur. Cependant, la fonctionnalité de test est désactivée. Après avoir modifié votre centre de préférences, vous pouvez fermer l’éditeur Drag & Drop en cliquant sur le bouton **Done (Terminé)**.

Vous verrez un aperçu du centre de préférences et de la page de confirmation. Cliquez sur **Save as Draft (Enregistrer en tant qu’ébauche)** pour revenir plus tard à ce centre de préférences ou, si vous êtes satisfait, cliquez sur **Launch Preference Center (Lancer le centre de préférences)**.

Lors du lancement du centre de préférences, vous serez invité à confirmer son nom, car il ne peut pas être modifié après le lancement. Une fois confirmé, le centre de préférences sera lancé et prêt à l’emploi.

## Utiliser le centre de préférences

Pour placer un lien vers le centre de préférences dans vos e-mails, copiez la balise Liquid du centre de préférences souhaité en cliquant sur l’icône **Copy Liquid (Copier le Liquid)**.

![][10]{: style="max-width:75%;"}

Ajoutez la balise Liquid à l’emplacement souhaité dans votre e-mail, comme pour les [URL de désabonnement]({{site.baseurl}}/user_guide/message_building_by_channel/email/preference_center/preference_center/#custom-footer).

## Erreurs

Si une erreur se produit lorsqu’un utilisateur clique sur **Save (Enregistrer)** dans un centre de préférences, le message d’erreur par défaut suivant s’affiche, qui ne peut pas être personnalisé ou stylisé dans l’éditeur. Cependant, la localisation des messages d’erreur est toujours prise en charge sur ces pages. 

![Une erreur indiquant : « Une erreur s'est produite lors de l'enregistrement de vos préférences. Veuillez réessayer. »][11]{: style="max-width:55%;"}

[1]: {% image_buster /assets/img/preference_center/preference_center1.png %} 
[2]: {% image_buster /assets/img/preference_center/preference_center2.png %} 
[3]: {% image_buster /assets/img/preference_center/preference_center3.png %} 
[4]: {% image_buster /assets/img/preference_center/preference_center4.png %} 
[5]: {% image_buster /assets/img/preference_center/preference_center5.png %} 
[6]: {% image_buster /assets/img/preference_center/preference_center6.png %} 
[7]: {% image_buster /assets/img/preference_center/preference_center7.png %} 
[8]: {% image_buster /assets/img/preference_center/preference_center8.png %} 
[9]: {% image_buster /assets/img/preference_center/preference_center9.png %} 
[10]: {% image_buster /assets/img/preference_center/preference_center10.png %} 
[11]: {% image_buster /assets/img/preference_center/preference_center11.png %} 

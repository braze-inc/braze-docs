---
nav_title: Centre de préférences de messagerie par glisser-déposer
article_title: Centre de préférences de messagerie par glisser-déposer
alias: "/dnd_preference_center/"
description: "Cette page de référence explique comment créer un centre de préférences d'e-mail avec l'éditeur par glisser-déposer."
page_order: 2
---

# Créer un centre de préférences de messagerie avec glisser-déposer

> En utilisant l'éditeur de glisser-déposer, vous pouvez créer et personnaliser un centre de préférences pour aider à gérer quels utilisateurs reçoivent certains types de communication. Vous pouvez avoir jusqu'à 50 centres de préférences par espace de travail.

{% multi_lang_include drag_and_drop_access.md variable_name='dnd editors' %}

## Étape 1 : Créer un centre de préférences d’e-mail

Créez un centre de préférences en accédant à **Audience** > **Abonnements** > **Centre de préférences de messagerie**.

Ici, une liste de centres de préférences personnalisés s’affiche. Sélectionnez **Créer Nouveau** pour créer un nouveau centre de préférences, ou sélectionnez le nom d'un centre existant pour apporter des modifications.

![Une liste de centres de préférences personnalisés avec le nom, la description, le type, le statut, la date de dernière modification et la date de création par l'utilisateur.]({% image_buster /assets/img/preference_center/preference_center1.png %})

## Étape 2 : Nommez le centre de préférences d’e-mail

Les noms des centres de préférences ne peuvent contenir que des caractères alphanumériques, des tirets ou des traits de soulignement. Le nom que vous fournissez déterminera la syntaxe de la balise Liquid générée. 

Cette balise Liquid peut être incluse dans toutes les campagnes par e-mail sortantes ou les étapes Canvas et dirigera les utilisateurs vers le centre de préférences.

![Un exemple de Liquid pour un centre de préférences.]({% image_buster /assets/img/preference_center/preference_center2.png %})

## Étape 3 : Ajouter des groupes d'abonnement au centre de préférences

Sélectionnez **Lancer l'éditeur** pour commencer à concevoir votre centre de préférences dans l'éditeur par glisser-déposer.

### Définir les groupes d'abonnement disponibles

Pour déterminer quels groupes d'abonnement doivent être affichés dans le centre de préférences, sélectionnez le bouton **\+ Ajouter des groupes d'abonnement** pour lancer une fenêtre modale où les groupes d'abonnement souhaités peuvent être sélectionnés. Après avoir sélectionné, sélectionnez le bouton **Ajouter des groupes d'abonnement** pour les ajouter au centre de préférences.

Vous pouvez configurer davantage les groupes d'abonnement sélectionnés en sélectionnant le bloc intelligent et en ajustant les propriétés du bloc.
- Ajuster l'ordre des groupes d'abonnement
- Ajouter ou supprimer des groupes d'abonnement supplémentaires
- Inclure des descriptions
- Ajouter ou supprimer une case à cocher **Abonner à tout** qui abonnera l'utilisateur à tous les groupes d'abonnement affichés dans ce bloc
- Ajouter ou supprimer une case à cocher **Se désabonner de tout** qui désabonnera l'utilisateur de tous les groupes d'abonnement affichés dans ce bloc

![Exemple d'un centre de préférences offrant la possibilité de s'abonner à tous les messages, au marketing, à la lettre d'information et aux e-mails hebdomadaires, ou de se désabonner de tous.]({% image_buster /assets/img/preference_center/preference_center3.png %}){: style="max-width:38%;"} ![]({% image_buster /assets/img/preference_center/preference_center4.png %}){: style="max-width:45%;"}

Le bouton **Désabonner de tout** en bas du modèle est non amovible et [dèsabonnera globalement]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#subscription-states) l'utilisateur de la réception de tout message électronique.

## Étape 4 : Personnalisez le centre de préférences à l'aide de l'éditeur par glisser-déposer

### Définir des styles communs

Vous pouvez définir certains styles à appliquer à tous les blocs pertinents dans votre centre de préférences à partir de l'onglet **Styles communs**. Les styles définis dans cette section sont utilisés partout dans votre message sauf aux endroits où vous les remplacez pour un bloc spécifique. Pour une expérience de conception plus facile, nous vous recommandons de configurer des styles au niveau de la page avant de personnaliser les styles au niveau des blocs.

![Exemple de paramètres de style communs pour le texte, les boutons et les liens.]({% image_buster /assets/img/preference_center/preference_center5.png %}){: style="max-width:45%;"}

{% alert tip %}
Pour revenir aux styles communs, cliquez sur le bouton « X » sur les propriétés de chaque bloc. Sélectionnez ensuite le conteneur du message, le bouton « X » du message ou l’arrière-plan de l’éditeur.
{% endalert %}

## Composants du centre de préférences par glisser-déposer

L'éditeur de glisser-déposer utilise deux composants clés pour rendre la composition du centre de préférences rapide et facile : les lignes et les blocs. Tous les blocs doivent être placés dans une ligne.

{% tabs %}
{% tab Lignes %}

Les lignes sont des unités structurelles qui définissent la composition horizontale d’une section du message en utilisant des cellules.

![Option permettant de sélectionner le type de ligne dans votre message.]({% image_buster /assets/img/preference_center/preference_center6.png %}){: style="max-width:45%;"}

Lorsque vous sélectionnez une ligne, vous pouvez ajouter ou supprimer autant de colonnes que nécessaire de la section de personnalisation des colonnes pour disposer plusieurs éléments de contenu côte à côte. Vous pouvez également faire glisser pour ajuster la taille des colonnes existantes.

![Options permettant de personnaliser les propriétés de votre colonne, notamment la couleur d'arrière-plan, le style de bordure, le rayon de la bordure et l'espacement.]({% image_buster /assets/img/preference_center/preference_center7.png %}){: style="max-width:45%;"}

En tant que bonne pratique, formatez vos propriétés de ligne et de colonne avant de formater l’un des blocs à l’intérieur des lignes. Vous pouvez ajuster l’espacement et l’alignement à de nombreux endroits. Il est plus facile de le modifier au fur et à mesure en commençant à la base.

{% endtab %}
{% tab Blocs %}

Les blocs représentent divers types de contenu que vous pouvez utiliser dans votre message. Faites glisser l'un à l'intérieur d'un segment de ligne existant, qui s'ajustera automatiquement à la largeur de la cellule.

![Option permettant de sélectionner des blocs, y compris le titre, le paragraphe, le bouton, l'image et l'espacement.]({% image_buster /assets/img/preference_center/preference_center8.png %}){: style="max-width:45%;"}

Chaque bloc possède ses propres paramètres, comme un contrôle granulaire sur la marge intérieure. Le panneau latéral droit passe automatiquement à un panneau de style pour l’élément de contenu sélectionné. Pour plus d'informations, voir [Propriétés du bloc éditeur]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/editor_blocks/).

Si vous utilisez le bloc de code personnalisé dans votre centre de préférences, les cadres en ligne peuvent ne pas se générer dans le code personnalisé lorsqu'il est livré à vos utilisateurs.

{% endtab %}
{% endtabs %}

## Étape 5 : Personnaliser votre page de confirmation

N’oubliez pas de personnaliser la page de confirmation ! Vous pouvez modifier cette page en sélectionnant **Page de confirmation** en haut de la fenêtre de l'éditeur par glisser-déposer. Cette page s’affichera pour les utilisateurs après la mise à jour de leurs préférences à l’aide du centre de préférences. Les mêmes capacités de style ci-dessus s’appliquent également à cette page.

![Exemple de page de confirmation pour communiquer que les préférences de l'utilisateur ont été mises à jour.]({% image_buster /assets/img/preference_center/preference_center9.png %}){: style="max-width:65%;"}

## Étape 6 : Prévisualisez et lancez votre centre de préférences

Vous pouvez prévisualiser votre centre de préférences en sélectionnant l'onglet **Prévisualiser** dans l'éditeur. Cependant, la fonctionnalité de test est désactivée. Après avoir modifié votre centre de préférences, vous pouvez fermer l'éditeur en sélectionnant le bouton **Terminé**.

Vous verrez un aperçu du centre de préférences et de la page de confirmation. Sélectionnez **Enregistrer comme brouillon** pour revenir plus tard à ce centre de préférences, ou si vous êtes satisfait, sélectionnez **Lancer le centre de préférences**.

Lors du lancement du centre de préférences, vous serez invité à confirmer son nom, car il ne peut pas être modifié après le lancement. Après avoir confirmé le nom, le centre de préférences est lancé et prêt à être utilisé.

## Utiliser le centre de préférences

{% multi_lang_include preference_center_warning.md %}

Pour placer un lien vers le centre de préférences dans vos e-mails, copiez la balise Liquid du centre de préférences souhaité en sélectionnant l'icône **Copier Liquid**.

![L'option Copier le liquide dans la ligne d'un centre de préférences.]({% image_buster /assets/img/preference_center/preference_center10.png %}){: style="max-width:75%;"}

Ajoutez l’étiquette Liquid à l'endroit souhaité dans votre e-mail, comme pour les [URL de désabonnement]({{site.baseurl}}/user_guide/message_building_by_channel/email/custom_email_footer/#adding-a-custom-unsubscribe-link).

## Gestion des erreurs

Si une erreur se produit lorsqu'un utilisateur sélectionne **Enregistrer** sur un centre de préférences, il recevra le message d'erreur par défaut suivant, qui ne peut pas être personnalisé ou stylé dans l'éditeur. Cependant, la localisation des messages d’erreur est toujours prise en charge sur ces pages. 

![Une erreur indiquant : « Une erreur s'est produite lors de l'enregistrement de vos préférences. Veuillez réessayer"]({% image_buster /assets/img/preference_center/preference_center11.png %}){: style="max-width:55%;"}


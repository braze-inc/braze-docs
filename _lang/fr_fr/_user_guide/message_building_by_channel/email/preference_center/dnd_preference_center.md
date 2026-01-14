---
nav_title: Centre de préférences pour les e-mails par glisser-déposer
article_title: "Centre de préférences d'e-mail à glisser-déposer"
alias: "/dnd_preference_center/"
description: "Cette page de référence explique comment créer un centre de préférences pour les e-mails à l'aide de l'éditeur par glisser-déposer."
page_order: 2
---

# Créez un centre de préférences pour les e-mails par glisser-déposer

> À l'aide de l'éditeur par glisser-déposer, vous pouvez créer et personnaliser un centre de préférences pour aider à gérer les utilisateurs qui reçoivent certains types de communication. Vous pouvez avoir jusqu'à 100 centres de préférences par espace de travail.

{% multi_lang_include drag_and_drop/drag_and_drop_access.md variable_name='dnd editors' %}

## Étape 1 : Créer un centre de préférences pour les e-mails

Créez un centre de préférences en accédant à **Audience** > **Centres de préférences e-mail.**

Une liste de centres de préférences personnalisés s'affiche alors. Sélectionnez **Créer nouveau** pour créer un nouveau centre de préférences ou sélectionnez le nom d'un centre existant pour le modifier.

Une liste de centres de préférences personnalisés avec le nom, la description, le type, le statut, la date de dernière modification et la date de création par l'utilisateur.]({% image_buster /assets/img/preference_center/preference_center1.png %})

## Étape 2 : Nommez le centre de préférences e-mail

Les noms des centres de préférences ne peuvent contenir que des caractères alphanumériques, des tirets ou des traits de soulignement. Le nom que vous fournissez déterminera la syntaxe de l'étiquette Liquid générée. 

Cette étiquette Liquid peut être incluse dans toute campagne d'e-mail sortant ou étape du canvas et dirigera les utilisateurs vers le centre de préférences.

\![Un exemple de Liquid pour un centre de préférences.]({% image_buster /assets/img/preference_center/preference_center2.png %})

## Étape 3 : Ajouter des groupes d'abonnement au centre de préférences

Sélectionnez **Lancer l'éditeur** pour commencer à concevoir votre centre de préférences dans l'éditeur par glisser-déposer.

### Définir les groupes d'abonnement disponibles

Pour déterminer quels groupes d'abonnement doivent être affichés dans le centre de préférences, sélectionnez le bouton **\+ Ajouter des groupes d'abonnement** pour lancer une fenêtre modale/boîte de dialogue dans laquelle les groupes d'abonnement souhaités peuvent être sélectionnés. Après la sélection, cliquez sur le bouton **Ajouter des groupes d'abonnement** pour les ajouter au centre de préférences.

Vous pouvez configurer davantage les groupes d'abonnement sélectionnés en sélectionnant le bloc intelligent et en ajustant les propriétés du bloc.
- Adjust the order of subscription groups (Ajustez l'ordre des groupes d'abonnement)
- Ajouter ou supprimer des groupes d'abonnement supplémentaires
- Inclure des descriptions
- Ajoutez ou supprimez la case à cocher **S'abonner à tous** qui sonnera l'utilisateur à tous les groupes d'abonnement affichés dans ce bloc.
- Ajoutez ou supprimez la case à cocher **Se désabonner de tous** qui désabonnera l'utilisateur de tous les groupes d'abonnement affichés dans ce bloc.

Un exemple de centre de préférences avec les options pour s'abonner à tous les messages, marketing, newsletter, et e-mails hebdomadaires, ou pour se désabonner de tous.]({% image_buster /assets/img/preference_center/preference_center3.png %}){: style="max-width:38%;"}\![]({% image_buster /assets/img/preference_center/preference_center4.png %}){: style="max-width:45%;"}

Le bouton " **Se désabonner de tout"** au bas du modèle est inamovible et [désabonnera globalement l]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#subscription-states) 'utilisateur de tout envoi d'e-mail.

## Étape 4 : Personnalisez le centre de préférences à l'aide de l'éditeur par glisser-déposer

### Définir des styles communs

Vous pouvez définir certains styles à appliquer à tous les blocs concernés dans votre centre de préférences à partir de l'onglet **Styles communs**. Les styles définis dans cette section sont utilisés partout dans votre message, sauf lorsque vous les remplacez pour un bloc spécifique. Pour faciliter la conception, nous vous recommandons de définir les styles au niveau de la page avant de personnaliser les styles au niveau du bloc.

Exemple de paramètres de style communs pour le texte, les boutons et les liens.]({% image_buster /assets/img/preference_center/preference_center5.png %}){: style="max-width:45%;"}

{% alert tip %}
Pour revenir aux styles communs, sélectionnez le bouton "X" sur les propriétés des blocs individuels. Sélectionnez ensuite le contenant du message, le bouton "X" du message ou l'arrière-plan de l'éditeur.
{% endalert %}

## Glisser-déposer les composants du centre de préférences

L'éditeur par glisser-déposer utilise deux éléments clés pour rendre la composition des centres de préférences rapide et facile : les lignes et les blocs. Tous les blocs doivent être placés en rangée.

{% tabs %}
{% tab Rows %}

Les lignes sont des unités structurelles qui définissent la composition horizontale d'une section du message en utilisant des cellules.

!Option permettant de sélectionner le type de ligne de votre message.]({% image_buster /assets/img/preference_center/preference_center6.png %}){: style="max-width:45%;"}

Lorsqu'une ligne est sélectionnée, vous pouvez ajouter ou supprimer le nombre de colonnes dont vous avez besoin dans la section Personnalisation des colonnes pour placer différents éléments de contenu côte à côte. Vous pouvez également faire glisser pour ajuster la taille des colonnes existantes.

\![Options permettant de personnaliser les propriétés de votre colonne, notamment la couleur d'arrière-plan, le style de bordure, le rayon de la bordure et l'espacement.]({% image_buster /assets/img/preference_center/preference_center7.png %}){: style="max-width:45%;"}

La meilleure pratique consiste à formater les propriétés des lignes et des colonnes avant de formater les blocs à l'intérieur des lignes. Vous pouvez ajuster l'espacement et l'alignement à de nombreux endroits. En partant de la base, il est donc plus facile de modifier le texte au fur et à mesure.

{% endtab %}
{% tab Blocks %}

Les blocs conseillent différents types de contenu que vous pouvez utiliser dans votre message. Faites-en glisser un à l'intérieur d'un segment de ligne existant, qui s'adaptera automatiquement à la largeur de la cellule.

!Option permettant de sélectionner des blocs, notamment le titre, le paragraphe, le bouton, l'image et l'intercalaire.]({% image_buster /assets/img/preference_center/preference_center8.png %}){: style="max-width:45%;"}

Chaque bloc dispose de ses propres paramètres, tels que le contrôle granulaire du remplissage. Le panneau de droite se transforme automatiquement en panneau de style pour l'élément de contenu sélectionné. Pour plus d'informations, voir [Propriétés du bloc éditeur]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/editor_blocks/).

Si vous utilisez le bloc Code personnalisé dans votre centre de préférences, il se peut que les cadres en ligne ne soient pas générés dans le code personnalisé lorsqu'ils sont transmis à vos utilisateurs.

{% endtab %}
{% endtabs %}

## Étape 5 : Personnalisez votre page de confirmation

N'oubliez pas de personnaliser la page de confirmation ! Vous pouvez modifier cette page en sélectionnant **Page de confirmation** en haut de la fenêtre de l'éditeur par glisser-déposer. Cette page sera affichée aux utilisateurs après la mise à jour de leurs préférences à l'aide du centre de préférences. Les mêmes possibilités de stylisation que celles décrites ci-dessus s'appliquent également à cette page.

Exemple de page de confirmation indiquant que les préférences de l'utilisateur ont été mises à jour.]({% image_buster /assets/img/preference_center/preference_center9.png %}){: style="max-width:65%;"}

## Étape 6 : Prévisualisez et lancez votre centre de préférences

Vous pouvez prévisualiser votre centre de préférences en sélectionnant l'onglet **Aperçu** dans l'éditeur. Cependant, la fonctionnalité de test est désactivée. Après avoir modifié votre centre de préférences, vous pouvez fermer l'éditeur en sélectionnant le bouton **Terminé**.

Vous verrez un aperçu du centre de préférences et de la page de confirmation. Sélectionnez **Enregistrer comme brouillon** pour revenir ultérieurement à ce centre de préférences ou, si vous êtes satisfait, sélectionnez **Lancer le centre de préférences.**

Lors du lancement du centre de préférences, vous serez invité à confirmer le nom, car il ne peut pas être modifié après le lancement. Après avoir confirmé le nom, le centre de préférences est lancé et prêt à être utilisé.

## Utiliser le centre de préférences

{% multi_lang_include alerts/important_alerts.md alert='Preference Center warning' %}

Pour placer un lien vers le centre de préférences dans vos e-mails, copiez l'étiquette Liquid du centre de préférences souhaité en sélectionnant l'icône **Copier Liquid.** 

!L'option Copier le liquide dans la ligne d'un centre de préférences.]({% image_buster /assets/img/preference_center/preference_center10.png %}){: style="max-width:75%;"}

Ajoutez l'étiquette Liquid à l'endroit souhaité dans votre e-mail, de la même manière que les [URL de désabonnement]({{site.baseurl}}/user_guide/message_building_by_channel/email/custom_email_footer/#adding-a-custom-unsubscribe-link) sont insérées.

## Traitement des erreurs

Si une erreur survient lorsqu'un utilisateur sélectionne **Enregistrer** dans un centre de préférences, le message d'erreur par défaut suivant lui sera présenté. Ce message ne peut pas être personnalisé ou stylisé dans l'éditeur. Cependant, la localisation des messages d'erreur est toujours prise en charge sur ces pages. 

\![Une erreur signalant "Il y a eu un problème pour enregistrer vos préférences. Veuillez réessayer."]({% image_buster /assets/img/preference_center/preference_center11.png %}){: style="max-width:55%;"}


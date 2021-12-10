---
nav_title: Équipes
article_title: Équipes
page_order: 4
page_type: Référence
description: "Cet article de référence couvre différents aspects des équipes dans votre tableau de bord Braze, comme la création et l'archivage d'équipes ou l'attribution de rôles."
---

# Équipes

Les administrateurs de Braze peuvent diviser les sous-ensembles des utilisateurs de leur tableau de bord en équipes avec des rôles et des permissions d'utilisateurs variables. Les équipes peuvent être configurées à travers la localisation de la base client, la langue, et des attributs personnalisés tels que les membres et les non-membres ont un accès différent aux fonctionnalités de messagerie et aux données du client. Une fois créés, des filtres et des tags d'équipe peuvent être assignés à travers divers outils d'engagement fournissant l'accès aux équipes et le filtrage des utilisateurs finaux en fonction des définitions d'équipes assignées.

{% include video.html id="UYjKrFcL9sQ" align="right" %}

## Création d'une équipe

Allez à la page __Gérer les paramètres__ et cliquez sur __Gérer les équipes__. À partir de là, vous verrez une option pour __+Ajouter une équipe__ qui remplit ensuite une fenêtre modale. Ici non seulement vous donnerez un nom à l'équipe, mais vous aurez également la possibilité d'utiliser un attribut personnalisé, , ou la langue pour mieux définir l'accès qui sera accordé.

Cette équipe peut plus tard être utilisée pour filtrer les utilisateurs finaux pour les objets d'engagement tels que les campagnes, les canvases, les cartes, les segments et plus, en accordant aux membres de cette équipe. Voir [Tags et Filtres](#tags-and-filters) ci-dessous pour en savoir plus.

!\[Ajout d'une équipe\]\[68\]

## Assigner des rôles d'équipe

Les administrateurs de Braze peuvent assigner des rôles d'équipe à leurs utilisateurs du tableau de bord, qui sont limités à seulement des données en lecture/écriture disponibles pour leurs équipes particulières. Les rôles prédéfinis de l'équipe incluent la langue et l'emplacement (par pays et régions).

Pour assigner un rôle d'équipe, accédez à __Gérer les utilisateurs__ et sélectionnez un utilisateur que vous souhaitez ajouter à votre équipe. En utilisant l'icône crayon, modifiez leur rôle utilisateur à __Limité__ et ajoutez-les au groupe d'application approprié. Le groupe d'applications assigné remplira une ligne de cases à cocher en bas de la page. Ensuite, une liste déroulante d'équipe apparaîtra, sélectionnez l'équipe que vous souhaitez appliquer et attribuez des permissions spécifiques en utilisant la ligne de permission d'équipe qui apparaît.

!\[Teams\]\[2\]

Pour voir les descriptions de ce que chaque utilisateur inclut et comment les utiliser, consultez notre section [Permissions utilisateur]({{site.baseurl}}/user_guide/administrative/manage_your_braze_users/user_permissions/#editing-user-permissions).

## Affecter les tags et les filtres des équipes {#tags-and-filters}

Les objets du tableau de bord peuvent être assignés aux équipes. Les canvases, les campagnes, les cartes, les segments, les modèles de courrier électronique et les ressources de la bibliothèque de médias peuvent tous être étiquetés avec un filtre et un tag d'équipe.

!\[Teams\]\[3\]{: style="max-width:70%;"}

Basé sur les définitions appliquées à l'équipe créée, lorsqu'un filtre d'équipe est attribué, vous limitez automatiquement les profils d'utilisateurs qu'un objet tableau de bord peut inclure en fonction de la définition de votre équipe. Par exemple, TeamA est défini comme les utilisateurs finaux des États-Unis. Lorsqu'un filtre d'équipe TeamA est affecté à CampaignA, CampaignA n'inclut que les utilisateurs finaux des États-Unis, et seule TeamA (autre que les administrateurs du tableau de bord) pourra accéder à CampaignA.

Basé sur les autorisations assignées, les membres des équipes ne seront autorisés qu'à accéder aux outils d'engagement du tableau de bord qui ont le filtre d'équipe défini. Les membres sont également en mesure de filtrer les Canvases, campagnes, cartes et segments par équipe pour identifier les objets du tableau de bord qui leur sont pertinents.

Notez que les équipes ne sont pas disponibles sur tous les contrats de Braze. Si vous souhaitez accéder à cette fonctionnalité, contactez votre responsable de compte et votre gestionnaire de succès client ou contactez-nous à [hello@braze. om](mailto:success@braze.com) pour une consultation.

## Archiver une équipe existante

Vous pouvez archiver les équipes à partir de la page **Gérer les équipes** , sous **Gérer les paramètres**. Sélectionnez une ou plusieurs équipes à archiver.

Si l'équipe n'est associée à aucun objet au sein de Braze, l'équipe sera immédiatement archivée. Si l'équipe est associée à un objet, une option vous sera présentée pour « supprimer l'équipe après le processus d'archive » ou « remplacer l'équipe par une autre équipe »

!\[Archiving a team\]\[86\]{: style="max-width:70%;"}

Les administrateurs peuvent désarchiver une équipe en sélectionnant l'équipe archivée, puis en cliquant sur **Désarchivé**.
[2]: {% image_buster /assets/img/teams.png %} [3]: {% image_buster /assets/img/teams1. ng %} [68]: {% image_buster /assets/img_archive/adding_a_team.png %} [86]: {% image_buster /assets/img_archive/archive_a_team.png %}

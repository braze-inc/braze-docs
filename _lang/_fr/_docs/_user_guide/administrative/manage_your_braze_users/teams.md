---
nav_title: Équipes
article_title: Équipes
page_order: 4
page_type: Référence
description: "Cet article de référence couvre différents aspects des équipes dans votre tableau de bord Braze, comme la création et l'archivage d'équipes ou l'attribution de rôles."
---

# Équipes

Les administrateurs de Braze peuvent regrouper leurs utilisateurs du tableau de bord en équipes avec différents rôles et permissions d'utilisateur. Les équipes peuvent être configurées à travers la localisation de la base client, la langue, et les attributs personnalisés pour que les membres et les non-membres aient un accès différent aux fonctionnalités de messagerie et aux données du client. Des filtres et des balises d'équipe peuvent être assignés à travers différents outils d'engagement.

{% include video.html id="UYjKrFcL9sQ" align="right" %}

## Création d'équipes

Allez à la page **Gérer les paramètres** , sélectionnez **Gérer les équipes**et cliquez sur <i class="fas fa-plus"></i> **Ajouter une équipe**. Entrez le **nom d'équipe**. Utilisez l'équipe **Définir (facultatif)** pour sélectionner un attribut, un emplacement ou une langue personnalisés pour définir davantage les permissions.

Les équipes peuvent être utilisées pour filtrer les utilisateurs finaux pour les objets d'engagement tels que les campagnes, les Canvases, les Cartes de Contenu, les segments, etc. Voir [Tags et Filtres](#tags-and-filters) ci-dessous pour en savoir plus.

{% alert note %}
Notez que les équipes ne sont pas disponibles sur tous les contrats de Braze. Si vous souhaitez accéder à cette fonctionnalité, contactez votre gestionnaire de compte Braze ou [contactez-nous](mailto:success@braze.com) pour une consultation.
{% endalert %}

!\[Ajout d'équipe\]\[68\]

## Attribution de rôles

Les administrateurs de Braze peuvent assigner des rôles d'équipe à leurs utilisateurs du tableau de bord qui sont limités à seulement lire ou écrire des données disponibles pour leurs équipes particulières. Les rôles prédéfinis de l'équipe incluent la langue et l'emplacement.

Pour assigner un rôle d'équipe, accédez à **Gérer les utilisateurs** et sélectionnez un utilisateur que vous souhaitez ajouter à votre équipe. En utilisant l'icône crayon, modifiez leur rôle utilisateur à **Limité** et ajoutez-les au groupe d'application approprié. Le groupe d'applications assigné remplira une ligne de cases à cocher en bas de la page. Ensuite, une liste déroulante de l'équipe apparaît, sélectionnez l'équipe que vous souhaitez appliquer et attribuez des permissions spécifiques en utilisant la ligne de permission d'équipe qui apparaît.

!\[Teams\]\[2\]

Pour voir les descriptions de ce que chaque utilisateur inclut et comment les utiliser, consultez notre section [Permissions utilisateur]({{site.baseurl}}/user_guide/administrative/manage_your_braze_users/user_permissions/#editing-user-permissions).

## Attribution de tags et de filtres {#tags-and-filters}

Les objets du tableau de bord peuvent être assignés aux équipes. Les canvases, les campagnes, les cartes, les segments, les modèles de courrier électronique et les ressources de la bibliothèque de médias peuvent tous être étiquetés avec un filtre et un tag d'équipe.

!\[Team Tags\]\[3\]{: style="max-width:70%;"}

Basé sur les définitions appliquées à l'équipe créée, lorsqu'un filtre d'équipe est attribué, vous limitez automatiquement les profils d'utilisateurs qu'un objet tableau de bord peut inclure en fonction de la définition de votre équipe. Par exemple, TeamA est défini comme les utilisateurs finaux des États-Unis. Lorsqu'un filtre d'équipe TeamA est affecté à CampaignA, CampaignA n'inclut que les utilisateurs finaux des États-Unis, et seule TeamA (autre que les administrateurs du tableau de bord) pourra accéder à CampaignA.

Basé sur les autorisations assignées, les membres des équipes ne seront autorisés qu'à accéder aux outils d'engagement du tableau de bord qui ont le filtre d'équipe défini. Les membres sont également en mesure de filtrer les Canvases, campagnes, cartes et segments par équipe pour identifier les objets du tableau de bord qui leur sont pertinents.

## Archivage d'une équipe existante

Vous pouvez archiver les équipes à partir de la page **Gérer les équipes** , sous **Gérer les paramètres**. Sélectionnez une ou plusieurs équipes à archiver.

Si l'équipe n'est associée à aucun objet au sein de Braze, l'équipe sera immédiatement archivée.

Si l'équipe est associée à un objet, une option vous sera présentée pour supprimer l'équipe après le processus d'archivage ou pour remplacer l'équipe.

!\[Archiving Team\]\[86\]{: style="max-width:70%;"}

Les administrateurs de Braze peuvent désarchiver une équipe en sélectionnant l'équipe archivée et en cliquant sur **désarchivé**.
[2]: {% image_buster /assets/img/teams.png %} [3]: {% image_buster /assets/img/teams1. ng %} [68]: {% image_buster /assets/img_archive/adding_a_team.png %} [86]: {% image_buster /assets/img_archive/archive_a_team.png %}

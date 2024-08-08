---
nav_title: Teams
article_title: Teams
page_order: 4
page_type: reference
description: "Cet article de référence couvre comment utiliser les équipes Braze dans le tableau de bord. Ici, vous pouvez apprendre comment créer des équipes, attribuer des rôles, des balises et des filtres."

---

# [![Cours d’apprentissage Braze]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/dive-into-braze-teams/869939){: style="float:right;width:120px;border:0;" class="noimgborder"}Teams

> Les administrateurs de Braze peuvent regrouper leurs utilisateurs de tableau de bord en équipes avec des rôles et autorisations différents. Les équipes peuvent être configurées en fonction de la localisation de la base de clients, de la langue et d’attributs personnalisés afin que les membres et les non-membres aient un accès différent aux fonctionnalités d’envoi de messages et aux données client. Des filtres et des balises d’équipes peuvent être attribués à différents outils d’engagement. 

{% multi_lang_include video.html id="UYjKrFcL9sQ" align="right" %}

## Créer des équipes

Allez à la page **Manage Settings (Gérer les paramètres)**, sélectionnez **Manage Teams (Gérer les équipes)** et cliquez sur <i class="fas fa-plus"></i> **Add Team (Ajouter une équipe)**. Saisissez le **Team Name (Nom de l’équipe)**. Utilisez l’option **Define Team (Optional) [Définir l’équipe (facultatif)]** pour sélectionner un attribut personnalisé, un emplacement ou une langue pour définir davantage les autorisations. 

Les Teams (Équipes) peuvent être utilisées pour filtrer des utilisateurs finaux pour des objets d’engagement tels que des campagnes, des Canvas, des cartes de contenu, des segments, etc. Voir la section de cet article sur [Assigning tags and filters (Attribution des balises et des filtres)](#tags-and-filters) pour en savoir plus. 

{% alert note %}
L’option Teams (Équipes) n’est pas disponible sur tous les contrats Braze. Si vous souhaitez accéder à cette fonctionnalité, contactez votre gestionnaire de compte Braze ou [contactez-nous](mailto:success@braze.com) pour une consultation.
{% endalert %}

![Ajouter une nouvelle Team][68]

## Affectation des rôles

Les administrateurs de Braze peuvent attribuer des rôles de Team à leurs utilisateurs de tableau de bord qui sont limités uniquement à la lecture ou à l’écriture des données disponibles à leurs Teams (Équipes) particulières. Les rôles de Team prédéfinis comprennent la langue et l’emplacement. 

Pour attribuer un rôle de Team, naviguez vers **Manage Users (Gérer les utilisateurs)** et sélectionnez un utilisateur que vous souhaitez ajouter à votre Team (Équipe). Cliquez sur <i class="fa fa-edit"></i> **Edit (Modifier)**, définissez leur rôle d’utilisateur à **Limité** et ajoutez-les au groupe d’apps approprié. Sélectionnez ensuite l’**équipe** à laquelle vous désirez ajouter cet utilisateur et affectez des autorisations spéciales depuis la colonne de permissions **Équipe**. Prenez en considération le fait que certaines autorisations ne sont attribuées que par groupe d’app et qu’elles s’afficheront comme « -- » dans la colonne de permissions **Équipe**.

![Affectation des rôles de Team][2]

Pour voir les descriptions de ce que chaque utilisateur peut obtenir et comment les utiliser, consultez notre [section Autorisations utilisateur]({{site.baseurl}}/user_guide/administrative/manage_your_braze_users/user_permissions/#editing-user-permissions).

## Attribution de balises et de filtres {#tags-and-filters}

Les objets du tableau de bord peuvent être attribués aux Teams (Équipes). Les Canvas, campagnes, cartes, segments, modèles de courrier électronique et actifs de bibliothèque multimédia peuvent tous être étiquetés avec un filtre et une balise de Team. 
 
![Ajout d’une balise de Team à une campagne][3]{: style="max-width:70%;"}

Sur la base des définitions appliquées à l’équipe créée, lorsqu’un filtre de Team (Équipe) est affecté, vous limitez automatiquement les profils d’utilisateur qu’un objet de tableau de bord peut inclure en fonction de la définition de votre Team (Équipe). Par exemple, Team A (Équipe A) est définie comme des utilisateurs finaux des États-Unis. Lorsqu’un filtre de Team A (Équipe A) est affecté à la campagne A, la campagne A inclura uniquement les utilisateurs finaux des États-Unis, et seule la Team A (autres que les administrateurs du tableau de bord) pourra accéder à la campagne A. 

En fonction des autorisations attribuées, les membres des équipes ne seront autorisés à accéder aux outils d’engagement du tableau de bord que pour lequel le filtre de Team (Équipe) est défini. Les membres peuvent également filtrer des Canvas, des campagnes, des cartes et des segments par Team pour identifier les objets du tableau de bord qui les concernent.

## Archivage d’une Team existante

Vous pouvez archiver les équipes dans la page **Manage Teams (Gérer les équipes)**, sous **Manage Settings (Gérer les paramètres)**. Sélectionnez une ou plusieurs Teams à archiver.

Si la Team n’est pas associée à un objet au sein de Braze, la Team sera archivée immédiatement.

Si la Team est associée à un objet, vous aurez le choix entre supprimer la Team après le processus d’archivage et remplacer la Team.

![Archivage d’une Team associée à un objet dans Braze][86]{: style="max-width:70%;"}

Les administrateurs de Braze peuvent désarchiver une Team en sélectionnant la Team archivée et en cliquant sur **Non archivé**.

[2]: {% image_buster /assets/img/teams.png %}
[3]: {% image_buster /assets/img/teams1.png %}
[68]: {% image_buster /assets/img_archive/adding_a_team.png %}
[86]: {% image_buster /assets/img_archive/archive_a_team.png %}

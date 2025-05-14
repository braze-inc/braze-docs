---
nav_title: Gestion des modèles
article_title: Gestion des modèles
page_order: 3

page_type: reference
description: "Cet article de référence décrit comment dupliquer et archiver des modèles dans la section Modèles et médias du tableau de bord de Braze."
tool:
  - Templates
  - Media

---

# Gestion des modèles

> L'archivage ou la duplication des modèles peut permettre de mieux les organiser et les gérer. Cet article de référence explique comment archiver et dupliquer des modèles dans la section **Modèles** du tableau de bord de Braze.

## Duplication de modèles

### Modèle individuel

![][8]{: style="float:right;max-width:15%;margin-left:15px;"}

Pour dupliquer un modèle individuel, sélectionnez l'icône <i class="fas fa-cog"></i> du modèle individuel et sélectionnez **Dupliquer** dans le menu déroulant.
<br><br>

{% alert note %}
Pour les modèles de [blocs de contenu]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/content_blocks/), un brouillon est créé. Pour tous les autres modèles, une nouvelle copie est automatiquement créée.
{% endalert %}

### Modèles multiples

{% raw %}

Vous pouvez dupliquer plusieurs modèles à la fois en cochant la case à côté du nom de chaque modèle que vous souhaitez dupliquer. Sélectionnez d'abord les modèles, puis le bouton **Dupliquer** qui apparaît.

Les modèles dupliqués peuvent être trouvés en triant la colonne **Dernière modification.**  Par défaut, les nouveaux modèles seront nommés `Copy of ORIGINAL_TEMPLATE_NAME`.

{% endraw %}

![GIF montrant un utilisateur qui sélectionne deux modèles et clique sur « Duplicate (Dupliquer) », créant ainsi un total de quatre modèles, triés par la dernière date de modification des modèles.][9]

## Modèles d'archivage

![Menu déroulant des paramètres étendus qui affiche trois options : Modifier, Archiver et Dupliquer, où l'option Archiver est mise en évidence.][10]{: style="float:right;max-width:20%;margin-left:15px;"}

Pour archiver un modèle individuel, sélectionnez l'icône des paramètres dans l'écran de la grille des modèles et sélectionnez **Archiver**. Lorsqu'un modèle est archivé, notez les différents scénarios suivants :

- Les campagnes actives continuent d'utiliser le modèle archivé sans interruption.
- Les brouillons de campagne conservent le contenu du modèle archivé et peuvent être modifiés et lancés.
- Pour modifier un modèle archivé, vous devez d'abord le sortir des archives. De même, pour utiliser un modèle archivé pour une campagne, vous devez d'abord sortir le modèle des archives.

Pour archiver plusieurs modèles, cochez la case à côté de chaque modèle que vous souhaitez archiver. Après avoir sélectionné plusieurs modèles, sélectionnez **Archiver la sélection**. Vous pouvez retrouver vos modèles archivés en sélectionnant **Archivé** sous **Afficher** dans la grille des modèles.

![La section Saved Drop & Drop Email Templates (Modèles d’e-mail envoyés et enregistrés) qui montre deux modèles sélectionnés : « Try Premium Template (Essayer le modèle Premium » et « Welcome Template (Modèle de bienvenue) ». Le bouton « Archive Selected (Archiver la sélection) » est mis en surbrillance par l’utilisateur.][11]

{% alert important %}
L'archivage n'est pas disponible actuellement pour les [modèles de liens]({{site.baseurl}}/user_guide/message_building_by_channel/email/link_templates/#link-templates).
{% endalert %}

[10]: {% image_buster /assets/img/template_archive_cog.png %}
[11]: {% image_buster /assets/img/archive_multiple_template.png %}
[8]: {% image_buster /assets/img/template_duplicate_cog.png %}
[9]: {% image_buster /assets/img/duplicate_multiple_template.gif %}
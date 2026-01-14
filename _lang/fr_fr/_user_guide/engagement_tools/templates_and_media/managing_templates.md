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

\![Menu déroulant avec option de duplication.]({% image_buster /assets/img/template_duplicate_cog.png %}){: style="float:right;max-width:15%;margin-left:15px;"}

Pour dupliquer un modèle individuel, sélectionnez l'icône <i class="fas fa-cog"></i> du modèle individuel et sélectionnez **Dupliquer** dans le menu déroulant.
<br><br>

{% alert note %}
Pour les modèles de [blocs de contenu]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/content_blocks/), un brouillon est créé. Pour tous les autres modèles, une nouvelle copie est automatiquement créée.
{% endalert %}

### Modèles multiples

{% raw %}

Vous pouvez dupliquer plusieurs modèles en cochant la case située à côté du nom du modèle. Sélectionnez d'abord les modèles, puis sélectionnez **Dupliquer**.

Les modèles dupliqués peuvent être trouvés en triant la colonne **Dernière modification.**  Par défaut, les nouveaux modèles seront nommés `Copy of ORIGINAL_TEMPLATE_NAME`.

{% endraw %}

Trois modèles triés en fonction de l'heure à laquelle ils ont été modifiés pour la dernière fois, avec un modèle copié en tête de liste.]({% image_buster /assets/img/duplicate_multiple_template.gif %})

## Modèles d'archivage

Le menu déroulant des paramètres est élargi et présente trois options : "Archiver", "Dupliquer" et "Copier dans l'espace de travail", l'option "Archiver" étant mise en évidence.]({% image_buster /assets/img/template_archive_cog.png %}){: style="float:right;max-width:20%;margin-left:15px;"}

Pour archiver un modèle individuel, sélectionnez l'icône des paramètres dans l'écran de la grille des modèles et sélectionnez **Archiver**. Lorsqu'un modèle est archivé, notez les différents scénarios suivants :

- Les campagnes actives continuent d'utiliser le modèle archivé sans interruption.
- Les projets de campagne conservent le contenu du modèle archivé et peuvent être modifiés et lancés.
- Pour modifier un modèle archivé, vous devez d'abord le désarchiver. De même, pour utiliser un modèle archivé pour une campagne, vous devez d'abord désarchiver le modèle.

Pour archiver plusieurs modèles, cochez la case en regard de chaque modèle que vous souhaitez archiver. Après avoir sélectionné plusieurs modèles, sélectionnez **Archiver**. Vous pouvez retrouver vos modèles archivés en sélectionnant **Archivé** sous **Afficher** dans la grille des modèles.

!Saved Drop & Drop Email Templates section qui montre deux modèles sélectionnés et une barre d'outils avec l'option d'archivage.]({% image_buster /assets/img/archive_multiple_template.png %}){: style="max-width:60%;"}

{% alert important %}
L'archivage n'est pas disponible actuellement pour les [modèles de liens]({{site.baseurl}}/user_guide/message_building_by_channel/email/link_templates/#link-templates).
{% endalert %}


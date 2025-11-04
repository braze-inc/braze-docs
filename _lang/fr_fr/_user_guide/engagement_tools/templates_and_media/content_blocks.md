---
nav_title: Bibliothèque des blocs de contenu
article_title: Bibliothèque des blocs de contenu
page_order: 1
page_type: reference
description: "Cet article de référence explique comment utiliser la bibliothèque de blocs de contenu pour gérer votre contenu cross-canal réutilisable dans un emplacement/localisation unique."
tool: 
  - Templates
  - Media

---

# Bibliothèque des blocs de contenu

> La bibliothèque de blocs de contenu vous permet de gérer votre contenu cross-canal réutilisable dans un emplacement/localisation unique.

Avec les blocs de contenu, vous pouvez :

- Créez un aspect cohérent pour vos campagnes d'e-mail en les utilisant comme en-têtes et pieds de page.
- Distribuez les mêmes codes d'offre par le biais de différents canaux.
- Créez des ressources prédéfinies qui peuvent être utilisées pour créer des messages avec des informations et des ressources cohérentes.
- Copier des corps de messages entiers dans d'autres messages.

## Créer un bloc de contenu

Deux types d'éditeurs sont utilisés pour créer un bloc de contenu : l'éditeur classique et l'éditeur par glisser-déposer. Ces deux types d'éditeurs correspondent au type de bloc de contenu : HTML et glisser-déposer. Vous pouvez également créer et gérer vos blocs de contenu [à l'aide de l'API]({{site.baseurl}}/api/endpoints/templates/).

{% tabs %}
{% tab Drag-and-drop %}

{% multi_lang_include create_content_block.md location="dnd" %}

{% endtab %}
{% tab HTML %}

{% multi_lang_include create_content_block.md location="html" %}

{% endtab %}
{% endtabs %}

### Spécifications du bloc de contenu

| Attribut du bloc de contenu | Spécifications |
|---|---|
| Nom | Champ obligatoire de 100 caractères maximum. Il ne peut pas être renommé après que le bloc de contenu a été enregistré. En outre, vous ne pouvez pas donner à un nouveau bloc de contenu le même nom qu'à un bloc de contenu précédent, même si ce dernier a été archivé. |
| Description | (facultatif) Maximum de 250 caractères. Décrivez le bloc de contenu afin que les autres utilisateurs de Braze sachent à quoi il sert et où il est utilisé. |
| Taille du contenu | Maximum de 50 KB. |
| Placement | Les blocs de contenu ne peuvent pas être utilisés dans le pied de page d'un e-mail. |
| Création | Editeur HTML ou éditeur par glisser-déposer. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert tip %}
Lors de la création de blocs de contenu, il peut être utile de visualiser HTML et Liquid en ajoutant des sauts de ligne. Si ces sauts de ligne sont laissés lors de l'envoi, vous risquez d'avoir des espaces superflus qui peuvent affecter le rendu du bloc. Pour éviter cela, utilisez l'étiquette **Capture** sur votre bloc ainsi que le filtre **| strip.** 
{% raw %}
```
{% capture your_variable %}
{{content_blocks.${your_content_block}}}
{% endcapture %}{{your_variable | strip}}
```
{% endraw %}
{% endalert %}

## Utilisation des blocs de contenu

Après avoir créé votre bloc de contenu, vous pouvez l'insérer dans vos messages en suivant les étapes suivantes : 

1. Copiez l'**étiquette Liquid du bloc de contenu** à partir de la section **Détails du bloc de contenu**.
2. Insérez l'étiquette Liquid du bloc de contenu dans le message. Vous pouvez également commencer à taper l'étiquette Liquid et laisser l'étiquette se remplir automatiquement.

### Ce qu'il faut savoir

- L'utilisation de blocs de contenu HTML dans des e-mails par glisser-déposer **ou de** blocs de contenu par glisser-déposer dans des e-mails HTML peut entraîner des problèmes de rendu inattendus. En effet, l'éditeur par glisser-déposer génère du HTML et du CSS qui rendent le contenu dynamique alors que l'éditeur HTML est plus statique.
- Les propriétés d'événement d'un canevas ne sont prises en charge que dans un canevas. Si vous faites référence à un bloc de contenu avec des propriétés d'entrée Canvas dans une campagne, il ne se remplira pas.

### Mise à jour et copie des blocs de contenu

Si vous choisissez de mettre à jour un bloc de contenu, il sera mis à jour dans tous les messages dans lesquels le bloc de contenu est utilisé s'il est inséré via Liquid. Si le bloc de contenu est importé à l'aide de la liste déroulante des **blocs de contenu** sous les **rangées** dans l'éditeur par glisser-déposer, il ne sera pas mis à jour dans tous les messages.

Si vous souhaitez mettre à jour un bloc de contenu pour un seul message ou en faire une copie pour l'utiliser dans d'autres messages, vous pouvez soit copier le code HTML du message d'origine dans le nouveau message, soit modifier le bloc de contenu d'origine (il doit déjà avoir été utilisé dans un message) et l'enregistrer. Un message vous invite à l'enregistrer en tant que nouveau bloc de contenu.

Après avoir modifié un bloc de contenu, vous pouvez enregistrer et lancer le bloc de contenu mis à jour en sélectionnant **Lancer le bloc de contenu**. Vous pouvez également sélectionner **Plus** > **Dupliquer** pour créer un double de votre bloc de contenu.

\![Un bloc de contenu qui dit "Bienvenue à notre bulletin d'information".]({% image_buster /assets/img/copy-content-block.png %})

Vous pouvez également [dupliquer]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/managing_templates/) un bloc de contenu. Cette opération crée une copie provisoire du bloc de contenu.

### Prévisualisation des blocs de contenu

Après avoir ajouté un bloc de contenu dans une campagne ou un canvas actif, vous pouvez prévisualiser ce bloc de contenu à partir de la bibliothèque des blocs de contenu en survolant le bloc de contenu et en sélectionnant l'icône de **prévisualisation** <i class="fa fa-eye preview-icon"></i>. 

Cet aperçu comprend des informations sur le bloc de contenu, telles que l'auteur, les tags, la date de création, la date de dernière modification, la description, le type d'éditeur, le nombre d'inclusions avec des détails, ainsi qu'un aperçu réel du bloc de contenu.

\![Aperçu d'un bloc de contenu "Workout_Promo" pour le cyclisme et la danse qui comporte six inclusions.]({% image_buster /assets/img/preview_tab_content_block.png %}){: style="max-width:60%;"} 

### Blocs de contenu imbriqués

Les blocs de contenu peuvent être imbriqués, mais une seule fois. Vous pouvez imbriquer le bloc de contenu A dans le bloc de contenu B, mais vous ne pourrez pas imbriquer le bloc de contenu B dans le bloc de contenu C.

{% alert warning %}
Rien ne vous empêchera d'imbriquer un troisième niveau de bloc de contenu, mais vous ne verrez pas le contenu se développer dans les imbrications au-delà du deuxième. Le contenu et l'extrait de code Liquid sont supprimés du message.
{% endalert %}

En outre, les blocs de contenu ne peuvent pas être utilisés dans un pied de page d'e-mail, alors que les pieds de page d'e-mail peuvent être utilisés dans les blocs de contenu.

### Archivage des blocs de contenu

Le menu déroulant des paramètres s'enrichit de trois options : Archiver, dupliquer et copier dans l'espace de travail.]({% image_buster /assets/img/template_archive_cog.png %}){: style="max-width:20%;float:right;margin-left:15px;" }

Une fois que vous avez fini d'utiliser un bloc de contenu, vous pouvez l'archiver à partir de la page [Modèles et médias & ]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/managing_templates/). Les blocs de contenu archivés sont en lecture seule, il faut donc désarchiver le bloc de contenu avant de le modifier. Les blocs de contenu ne peuvent pas être archivés s'ils sont utilisés dans des messages.

#### Meilleures pratiques

- Lorsque votre bloc n'est utilisé que dans quelques e-mails, nous vous recommandons d'archiver le bloc périmé et de mettre à jour vos messages en ligne/en production/instantané avec un bloc plus récent qui n'a pas été archivé.
- Si votre bloc ne contient qu'une coquille ou ne nécessite qu'une modification mineure, nous ne vous recommandons pas de l'archiver. Au lieu de cela, mettez à jour le bloc et envoyez !
- Lorsque votre bloc est utilisé dans plus de messages que vous ne pouvez raisonnablement gérer avec la première suggestion de cette liste, nous vous recommandons de supprimer tout le contenu du bloc et de l'archiver. Cela permettra de s'assurer qu'aucune information obsolète n'est incluse dans les nouveaux e-mails envoyés.
- Si vous archivez accidentellement un bloc de contenu, vous pouvez le désarchiver.

!Panneau des blocs de contenu enregistrés où le menu déroulant des paramètres pour "Test_32" est élargi pour afficher trois options : Désarchiver, dupliquer et copier dans l'espace de travail]({% image_buster /assets/img/unarchive-content-block.png %})


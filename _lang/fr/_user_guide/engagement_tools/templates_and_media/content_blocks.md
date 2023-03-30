---
nav_title: Blocs de contenu
article_title: Blocs de contenu
page_order: 1
page_type: reference
description: "Cet article de référence explique comment utiliser la bibliothèque de blocs de contenu pour gérer votre contenu réutilisable sur plusieurs canaux à un seul et même endroit."
tool: 
  - Templates
  - Médias

---

# Blocs de contenu

> La bibliothèque de blocs de contenu vous permet de gérer votre contenu réutilisable sur plusieurs canaux dans un seul emplacement centralisé. Pour accéder à cette fonction, accédez à l’onglet **Content Blocks Library (Bibliothèque de blocs de contenu)** dans la section [Templates & Media (Modèles et médias)][6] de votre compte Braze.

Avec les blocs de contenu, vous pouvez :

- Créer un look & feel cohérent pour vos campagnes d’e-mail en utilisant des blocs de contenu pour les en-têtes et pieds de page.
- Distribuer les mêmes codes promotionnels sur différents canaux.
- Créer des ressources prédéfinies qui peuvent être utilisées pour créer des messages avec des informations et des ressources cohérentes.
- Copier-coller des corps de message entiers dans d’autres messages.

## Créer un bloc de contenu

Créer un bloc de contenu est simple : accédez à la section **Templates & Media (Modèles et médias)**, puis cliquez sur l’onglet **Content Blocks Library (Bibliothèque de blocs de contenu)**. Cliquez sur **Créer un bloc de contenu**. Pour finir, il ne vous reste qu’à créer votre bloc de contenu !

![][1]

Les blocs de contenu sont répartis en deux types : `HTML` ou `text`. Braze sélectionne le type pour vous en fonction du contenu que vous avez inséré dans le bloc. Si Braze détecte une balise `HTML` dans le bloc de contenu, le type de bloc passera automatiquement à `HTML`. Sinon, il sera considéré comme du `text`.  

Vous pouvez également créer et gérer vos blocs de contenu [via une API][5].

{% alert tip %}
Au moment de créer des blocs de contenu, il peut parfois être utile d’ajouter des sauts de ligne pour visualiser HTML et Liquid. Si ces sauts de ligne sont laissés au moment de l’envoi, vous risquez de vous retrouver avec des espaces étrangers qui peuvent affecter la façon dont le bloc va s’afficher. Pour éviter cela, utilisez la balise **Capturer** sur votre bloc avec le filtre de bande **&#124;**. 
{% raw %}
```
{% capture your_variable %}
{{content_blocks.${your_content_block}}}
{% endcapture %}{{your_variable | strip}}
```
{% endraw %}
{% endalert %}

## Utilisation des blocs de contenu

1. Créez votre bloc de contenu.
2. Copiez la balise Liquid du bloc de contenu sur la page de votre bloc de contenu.
3. Insérez la balise Liquid du bloc de contenu dans le message. Vous pouvez également commencer à saisir le Liquid pour que la balise s’insère automatiquement.

## Mise à jour et copie des blocs de contenu

Si vous choisissez de mettre à jour un bloc de contenu, il sera mis à jour dans tous les messages qui utilisent ce bloc de contenu.

Si vous souhaitez mettre à jour un bloc de contenu pour un seul message ou faire une copie pour l’utiliser dans d’autres messages, vous pouvez copier le fichier HTML du message original vers votre nouveau ou modifier le bloc de contenu d’origine (il doit déjà avoir été utilisé dans un message) et l’enregistrer. Une invite s’affichera ensuite pour vous permettre de l’enregistrer en tant que nouveau bloc de contenu.

![Enregistrez la boîte de dialogue Bloc de contenu qui indique « Enregistrer et mettre à jour » pour mettre à jour ce bloc de contenu. Cela appliquera des modifications aux messages qui utilisent actuellement ce bloc de contenu. Sélectionnez « Enregistrer comme copie » pour enregistrer vos modifications en tant que copie de ce bloc de contenu. Les mises à jour ne s’appliqueront pas aux messages qui utilisent actuellement ce bloc de contenu avec trois boutons : Cancel (Annuler), Save as Copy (Enregistrer comme copie) et Save and Update (Enregistrer et mettre à jour).][2]{: height="70%" width="70%"}

Vous pouvez également [dupliquer]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/duplicate/) un bloc de contenu à l’aide de notre fonction Modèles et médias. En dupliquant un bloc de contenu, une copie « ébauche » sera créée.

## Blocs de contenu imbriqués

Les blocs de contenu peuvent être imbriqués, mais ils ne peuvent l’être qu’une seule fois ! Vous pouvez imbriquer le bloc de contenu A dans le bloc de contenu B, mais vous ne pourrez pas imbriquer le bloc de contenu B dans le bloc de contenu C.

{% alert warning %}
Rien ne vous empêche d’imbriquer un troisième niveau de bloc de contenu, mais vous ne verrez pas le contenu s’étendre dans des imbrications au-delà de la seconde. Le contenu et l’extrait de code Liquid sont supprimés du message.
{% endalert %}

De plus, les blocs de contenu ne peuvent pas être utilisés dans le pied de page d’un e-mail, bien que les pieds de page puissent être utilisés dans les blocs de contenu.

## Archivage des blocs de contenu

![Menu déroulant des paramètres étendus qui affiche trois options : Edit (Modifier), Archive (Archiver) et Duplicate (Dupliquer), lorsque l’option Archive (Archiver) est mise en surbrillance.][3]{: style="max-width:20%;float:right;margin-left:15px;" }

Lorsque vous avez terminé d’utiliser un bloc de contenu, vous pouvez l’archiver en accédant à la page [Modèles et médias]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/archive/).

Les messages qui utilisent le bloc de contenu que vous avez archivé fonctionneront comme s’il était toujours là. Cependant, nous recommandons de suivre plusieurs meilleures pratiques pour vous assurer qu’aucune information obsolète ne sera incluse par accident dans vos e-mails.

1. Lorsque votre bloc n’est utilisé que dans quelques e-mails, nous vous recommandons d’archiver le bloc obsolète et de mettre à jour vos messages en direct avec un bloc plus récent qui n’a pas été archivé.
2. Si votre bloc ne contient qu’une seule faute de frappe ou n’a besoin que d’un changement mineur, nous ne recommandons pas d’archiver le bloc. Il vous suffit de le mettre à jour et de l’envoyer !
3. Lorsque votre bloc est utilisé dans un plus grand nombre de messages que vous ne pouvez raisonnablement gérer en suivant la première suggestion de cette liste, nous vous recommandons de supprimer **tout** le contenu du bloc, puis de l’archiver. Cela vous permettra de garantir qu’aucune information obsolète ne se retrouve pas erreur dans les nouveaux e-mails que vous envoyez.

{% alert tip %}
Vous pouvez enregistrer un bloc de contenu même si celui-ci ne contient aucun contenu.
{% endalert %}

Si vous avez fait une erreur en archivant un bloc de contenu, vous avez toujours la possibilité de le décompresser.  

![Panneau Blocs de contenu enregistrés dans lequel le menu déroulant des paramètres pour « Content_Block_1 » est agrandi pour afficher deux options : Décompresser et dupliquer.][4]

## Spécifications des blocs de contenu

| Attribut de bloc de contenu | Spécifications |
|---|---|
| Nom | Ce champ obligatoire est limité à 100 caractères. Il ne peut pas être renommé après avoir enregistré un bloc de contenu. De plus, vous ne pouvez pas nommer un nouveau bloc de contenu en utilisant le même nom que le précédent bloc de contenu, même si le précédent a été archivé. |
| Description | Ce champ facultatif est limité à 250 caractères. Ajoutez une description au bloc de contenu afin que les autres personnes qui le consultent dans le produit Braze sachent à quoi il sert et où il est utilisé. |
| Taille du contenu | Limité à 50 Ko (Kilo-octet). |
| Placement | Les blocs de contenu ne peuvent pas être utilisés dans le pied de page des e-mails. |
| Création | HTML ou texte. |
{: .reset-td-br-1 .reset-td-br-2}

[1]: {% image_buster /assets/img/create-content-blocks.gif %}
[2]: {% image_buster /assets/img/copy-content-block.png %}
[3]: {% image_buster /assets/img/template_archive_cog.png %}
[4]: {% image_buster /assets/img/unarchive-content-block.png %}
[5]: {{site.baseurl}}/api/endpoints/templates/
[6]: {{site.baseurl}}/user_guide/engagement_tools/templates_and_media/

---
nav_title: Blocs de contenu
article_title: Blocs de contenu
page_order: 1
page_type: Référence
description: "Cet article de référence explique comment utiliser la bibliothèque de blocs de contenu pour gérer votre contenu réutilisable et inter-canal dans un seul emplacement centralisé."
tool:
  - Modèles
  - Médias
---

# Blocs de contenu

> La bibliothèque de blocs de contenu vous permet de gérer votre contenu réutilisable et multi-canal dans un seul et même emplacement. Pour accéder à cette fonctionnalité, allez dans l'onglet __Content Blocks Library__ dans la section [Modèles & Média][6] de votre compte Braze.

Avec les blocs de contenu, vous pouvez:

- Créez une apparence et une apparence cohérentes à vos campagnes de courriels en utilisant des blocs de contenu comme entêtes et pied de page.
- Distribuez les mêmes codes de l'offre par le biais de canaux différents.
- Créer des actifs prédéfinis qui peuvent être utilisés pour construire des messages avec des informations et des actifs cohérents.
- Copier le corps entier du message vers d'autres messages.

## Créer un bloc de contenu

Créer un bloc de contenu est facile — allez dans __Modèles & Médias__, puis sélectionnez l'onglet __Bibliothèque de blocs de contenu__. Cliquez sur __Créer un bloc de contenu.__

Ensuite, créez votre bloc de contenu !

!\[Créer un nouveau bloc de contenu\]\[1\]

Les blocs de contenu ont deux types : `HTML` ou `texte`. Braze sélectionnera le type pour vous en fonction du contenu que vous avez inséré dans le bloc. Si Braze détecte le balisage `HTML` dans le bloc de contenu, le type de bloc passera automatiquement à `HTML`. Sinon, il sera considéré comme `texte`.

Vous pouvez également [créer et gérer vos blocs de contenu via l'API][5].

{% alert tip %}
Lors de la création de blocs de contenu, il aide parfois à visualiser HTML et Liquid en ajoutant des sauts de ligne. Si ces sauts de ligne sont laissés pendant l'envoi, vous risquez d'avoir des espaces extérieurs qui peuvent affecter la façon dont le bloc sera affiché. Pour éviter cela, utilisez la balise __Capture__ sur votre bloc avec le filtre __&#124; bande__.
{% raw %}
```
{% capture your_variable %}
{{content_blocks.${your_content_block}}}
{% endcapture %}{{your_variable | strip}}
```
{% endraw %}
{% endalert %}

## Utiliser les blocs de contenu

1. Créez votre bloc de contenu.
2. Copiez la balise Liquid de bloc de contenu de votre page de bloc de contenu.
3. Insérez la balise Liquid du bloc de contenu dans le message. Vous pouvez également commencer à taper le Liquid et faire remplir automatiquement le tag.

## Mise à jour et copie des blocs de contenu

Si vous choisissez de mettre à jour un bloc de contenu, il sera mis à jour dans tous les messages que le bloc de contenu est utilisé.

Si vous voulez mettre à jour un bloc de contenu pour un seul message ou faire une copie à utiliser dans d'autres messages, vous pouvez copier le HTML du message original vers votre nouveau message ou modifiez le bloc de contenu original (il doit déjà avoir été utilisé dans un message) et enregistrez-le. Vous obtiendrez alors une invite qui vous permettra de l'enregistrer en tant que nouveau bloc de contenu.

!\[Save Content Block dialog\]\[2\]{: height="70%" width="70%"}

Vous pouvez également [dupliquer un bloc de contenu]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/duplicate/) avec nos Modèles & Fonctionnalité Média. Lorsque vous faites cela, une copie "brouillon" est créée.

## Blocs de contenu imbriqués

Les blocs de contenu peuvent être imbriqués, mais une seule fois ! Vous pouvez imbriquer _Bloc de contenu A_ dans _Bloc de contenu B_, mais vous ne pourrez pas imbriquer le _Bloc de contenu B_ dans le _Bloc de contenu C_.

{% alert warning %}
Rien ne vous empêchera d’imbriquer un troisième niveau de bloc de contenu, mais vous ne verrez pas le contenu s’étendre dans les nids au-delà du second. Le contenu et le snippet Liquid sont supprimés du message.
{% endalert %}

De plus, les blocs de contenu ne peuvent pas être utilisés dans un pied de page de courriel, même si les pieds de page peuvent être utilisés dans les blocs de contenu.

## Archivage des blocs de contenu

!\[Développer l'icône des paramètres et sélectionner Archive\]\[3\]{: style="max-width:20%;float:right;margin-left:15px;" }

Une fois que vous avez fini d'utiliser un bloc de contenu, vous pouvez l'archiver à partir de la page [Modèles & Média]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/archive/).

Les messages utilisant le bloc archivé se feront toujours comme s'il était là. Cependant, nous vous recommandons plusieurs pratiques exemplaires afin de vous assurer que les informations périmées ne sont pas incluses accidentellement dans vos courriels.

1. Lorsque votre bloc n'est utilisé que dans quelques e-mails, Nous vous recommandons d'archiver le bloc obsolète et de mettre à jour vos messages en direct avec un nouveau bloc qui n'a pas été archivé.
2. Lorsque votre bloc a seulement une faute de frappe ou a besoin d'un changement mineur, nous ne recommandons pas d'archiver le bloc. Il vous suffit de mettre à jour et d'envoyer !
3. Lorsque votre bloc est utilisé dans plus de messages que vous ne pouvez raisonnablement gérer avec la première suggestion de cette liste, nous vous recommandons de supprimer __tout le contenu__ du bloc, puis de l'archiver. Ainsi, aucune information obsolète ne sera transmise dans les courriels qui viennent d'être envoyés.

{% alert tip %}
  Vous pouvez enregistrer un bloc de contenu sans le contenu.
{% endalert %}

Si vous avez fait une erreur dans l'archivage d'un bloc de contenu, vous pouvez le désarchiver.

!\[Développer l'icône des paramètres et sélectionner Déarchiver\]\[4\]

## Caractéristiques du bloc de contenu

| Attribut de bloc de contenu | Caractéristiques                                                                                                                                                                                                                                                            |
| --------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Nom                         | Champ obligatoire limité à 100 caractères. Il ne peut pas être renommé après que le bloc de contenu ait été enregistré. De plus, vous ne pouvez pas nommer un nouveau bloc de contenu avec le même nom qu'un bloc de contenu précédent, même si le précédent a été archivé. |
| Libellé                     | Champ facultatif limité à 250 caractères. Décrivez le bloc de contenu pour que les autres personnes qui le consulteront dans le produit Braze sachent à quoi il sert et où il est utilisé.                                                                                  |
| Taille du contenu           | Limité à 50 Ko (Kilobyte).                                                                                                                                                                                                                                                  |
| Placement                   | Les blocs de contenu ne peuvent pas être utilisés dans un pied de page de courriel.                                                                                                                                                                                         |
| Création                    | HTML ou Texte.                                                                                                                                                                                                                                                              |
{: .reset-td-br-1 .reset-td-br-2}
[1]: {% image_buster /assets/img/create-content-blocks.gif %} [2]: {% image_buster /assets/img/copy-content-block. ng %} [3]: {% image_buster /assets/img/template_archive_cog.png %} [4]: {% image_buster /assets/img/unarchive-content-block.png %}

[5]: {{site.baseurl}}/api/endpoints/templates/
[6]: {{site.baseurl}}/user_guide/engagement_tools/templates_and_media/

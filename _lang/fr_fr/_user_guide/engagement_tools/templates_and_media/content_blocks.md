---
nav_title: Bibliothèque de blocs de contenu
article_title: Bibliothèque de blocs de contenu
page_order: 1
page_type: reference
description: "Cet article de référence explique comment utiliser la bibliothèque de blocs de contenu pour gérer votre contenu réutilisable sur plusieurs canaux à un seul et même endroit."
tool: 
  - Templates
  - Media

---

# Bibliothèque de blocs de contenu

> La bibliothèque de blocs de contenu vous permet de gérer votre contenu réutilisable sur plusieurs canaux dans un seul emplacement centralisé.

Avec les blocs de contenu, vous pouvez :

- Créez une apparence et une sensation cohérentes pour vos campagnes par e-mail en les utilisant comme en-têtes et pieds de page.
- Distribuer les mêmes codes promotionnels sur différents canaux.
- Créer des ressources prédéfinies qui peuvent être utilisées pour créer des messages avec des informations et des ressources cohérentes.
- Copier-coller des corps de message entiers dans d’autres messages.

## Créer un bloc de contenu

Il existe deux types d'éditeurs utilisés pour créer un bloc de contenu : classique et glisser-déposer. Ces deux types d'éditeurs correspondent au type de bloc de contenu : HTML et glisser-déposer. Vous pouvez également créer et gérer vos blocs de contenu [via l'API][5]].

{% tabs %}
{% tab Glisser-déposer %}

{% multi_lang_include create_content_block.md location="dnd" %}

{% endtab %}
{% tab HTML %}

{% multi_lang_include create_content_block.md location="html" %}

{% endtab %}
{% endtabs %}

### Spécifications des blocs de contenu

| Attribut de bloc de contenu | Spécifications |
|---|---|
| Nom | Champ obligatoire avec un maximum de 100 caractères. Il ne peut pas être renommé une fois le bloc de contenu enregistré. De plus, vous ne pouvez pas nommer un nouveau bloc de contenu en utilisant le même nom que le précédent bloc de contenu, même si le précédent a été archivé. |
| Description | (facultatif) Maximum de 250 caractères. Décrivez le bloc de contenu afin que les autres utilisateurs de Braze sachent à quoi il sert et où il est utilisé. |
| Taille du contenu | Maximum 50 Ko (kilo-octets). |
| Placement | Les blocs de contenu ne peuvent pas être utilisés dans le pied de page des e-mails. |
| Création | Éditeur HTML ou éditeur par glisser-déposer. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert tip %}
Au moment de créer des blocs de contenu, il peut parfois être utile d’ajouter des sauts de ligne pour visualiser HTML et Liquid. Si ces sauts de ligne sont laissés au moment de l’envoi, vous risquez de vous retrouver avec des espaces étrangers qui peuvent affecter la façon dont le bloc va s’afficher. Pour éviter cela, utilisez la balise **Capture** sur votre bloc avec le filtre **| strip**.
{% raw %}
```
{% capture your_variable %}
{{content_blocks.${your_content_block}}}
{% endcapture %}{{your_variable | strip}}
```
{% endraw %}
{% endalert %}

## Utilisation des blocs de contenu

Après avoir créé votre bloc de contenu, vous pouvez l'insérer dans vos messages en procédant comme suit : 

1. Copiez l’**étiquette Liquid du bloc de contenu** de la section **Détails du bloc de contenu**.
2. Insérez l’étiquette Liquid du bloc de contenu dans le message. Vous pouvez également commencer à saisir le Liquid pour que la balise s’insère automatiquement.

{% alert note %}
Les propriétés d'entrée et les propriétés d'événement de Canvas sont uniquement prises en charge dans un canvas, pas dans le bloc de contenu.
{% endalert %}

### Mise à jour et copie des blocs de contenu

Si vous choisissez de mettre à jour un bloc de contenu, il sera mis à jour dans tous les messages où le bloc de contenu est utilisé s'il est inséré via Liquid. Si le bloc de contenu est importé en utilisant la liste déroulante **Blocs de contenu** sous **Lignes** dans l'éditeur glisser-déposer, il ne sera pas mis à jour dans tous les messages.

Si vous souhaitez mettre à jour un bloc de contenu pour un seul message ou en faire une copie à utiliser dans d'autres messages, vous pouvez soit copier le HTML du message original dans votre nouveau message, soit modifier le bloc de contenu original (il doit avoir été utilisé dans un message déjà) et l'enregistrer. Une invite s’affichera ensuite pour vous permettre de l’enregistrer en tant que nouveau bloc de contenu.

Après avoir apporté des modifications à un bloc de contenu, vous pouvez enregistrer et lancer le bloc de contenu mis à jour en cliquant sur **Lancer le bloc de contenu**. Ou, vous pouvez sélectionner **Plus** > **Dupliquer** pour créer un duplicata de votre bloc de contenu.

![][2]

Vous pouvez également [dupliquer]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/duplicate/) un bloc de contenu. Cela crée une copie brouillon du bloc de contenu.

### Aperçu des blocs de contenu

Après avoir ajouté un bloc de contenu dans une campagne active ou un Canvas, vous pouvez prévisualiser ce bloc de contenu depuis la bibliothèque de blocs de contenu en survolant le bloc de contenu et en sélectionnant l'icône <i class="fa fa-eye preview-icon"></i> **Prévisualiser**. 

Cet aperçu inclut des informations sur le bloc de contenu, telles que son créateur, les étiquettes, la date de création, la date de dernière modification, la description, le type d'éditeur, le nombre d'inclusions avec des détails et un aperçu réel du bloc de contenu.

![][7]{: style="max-width:60%;"} 

### Blocs de contenu imbriqués

Les blocs de contenu peuvent être imbriqués, mais une seule fois. Vous pouvez imbriquer le bloc de contenu A dans le bloc de contenu B, mais vous ne pourrez pas imbriquer le bloc de contenu B dans le bloc de contenu C.

{% alert warning %}
Rien ne vous empêche d’imbriquer un troisième niveau de bloc de contenu, mais vous ne verrez pas le contenu s’étendre dans des imbrications au-delà de la seconde. Le contenu et l’extrait de code Liquid sont supprimés du message.
{% endalert %}

De plus, les blocs de contenu ne peuvent pas être utilisés dans le pied de page d’un e-mail, bien que les pieds de page puissent être utilisés dans les blocs de contenu.

### Archivage des blocs de contenu

![Menu déroulant des paramètres étendus qui affiche trois options : Archiver, Dupliquer et Copier dans l'espace de travail.][3]{: style="max-width:20%;float:right;margin-left:15px;" }

Une fois que vous avez terminé d'utiliser un bloc de contenu, vous pouvez l'archiver depuis la page [Modèles et médias]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/archive/). Les blocs de contenu archivés sont en lecture seule. Par conséquent, sortez le bloc de contenu des archives avant de le modifier. Les blocs de contenu ne peuvent pas être archivés s'ils sont utilisés dans des messages.

#### Bonnes pratiques

- Lorsque votre bloc n’est utilisé que dans quelques e-mails, nous vous recommandons d’archiver le bloc obsolète et de mettre à jour vos messages en cours avec un bloc plus récent qui n’a pas été archivé.
- Si votre bloc ne contient qu’une seule faute de frappe ou n’a besoin que d’un changement mineur, nous ne recommandons pas d’archiver le bloc. Il vous suffit de le mettre à jour et de l’envoyer !
- Lorsque votre bloc est utilisé dans plus de messages que vous ne pouvez raisonnablement gérer avec la première suggestion de cette liste, nous vous recommandons de supprimer tout le contenu du bloc, puis de l'archiver. Cela garantira qu'aucune information obsolète n'est incluse dans les nouveaux e-mails envoyés.
- Si vous archivez accidentellement un bloc de contenu, vous pouvez le sortir des archives.

![Panneau Blocs de contenu enregistrés dans lequel le menu déroulant des paramètres pour « Test_32 » est développé et affiche trois options : Désarchiver, Dupliquer et Copier dans l'espace de travail][4]

[2]: {% image_buster /assets/img/copy-content-block.png %}
[3]: {% image_buster /assets/img/template_archive_cog.png %}
[4]: {% image_buster /assets/img/unarchive-content-block.png %}
[5]: {{site.baseurl}}/api/endpoints/templates/
[6]: {{site.baseurl}}/user_guide/engagement_tools/templates_and_media/
[7]: {% image_buster /assets/img/preview_tab_content_block.png %}

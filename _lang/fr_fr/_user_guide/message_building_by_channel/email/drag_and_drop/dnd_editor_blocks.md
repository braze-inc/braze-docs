---
nav_title: Blocs éditeur
article_title: "Blocs de l'éditeur par glisser-déposer"
alias: "/dnd/editor_blocks/"
channel: email
page_order: 1
description: "Cet article de référence couvre les différents blocs éditeur qui sont fournis dans l'éditeur par glisser-déposer pour l'e-mail."
tool: Media

---

# Blocs éditeur

> Cet article de référence répertorie les types de blocs éditeurs et leurs propriétés personnalisables. Ces blocs sont disponibles dans l'éditeur par glisser-déposer sous la section **Contenu.** 

Pour utiliser un bloc éditeur, glissez un bloc éditeur à l'intérieur d'une colonne dans l'éditeur par glisser-déposer. Il s’ajuste automatiquement à la largeur de la colonne. Chaque bloc éditeur possède ses propres paramètres, tels que le contrôle granulaire sur la marge intérieure.

Pour plus d'informations sur l'utilisation et la personnalisation de ces blocs éditeurs dans votre e-mail, consultez la section [Plus de détails créatifs.]({{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/overview/#creative-details) 

{% alert tip %}
Vous pouvez également [ajouter des attributs personnalisés]({{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/overview/#creative-details/) à n'importe quelle URL dans les blocs éditeurs `Image`, `Button`, ou `Text`.
{% endalert %}

## Types

Le tableau suivant décrit comment les utilisateurs peuvent exploiter chaque type de bloc éditeur.

| nom | Description |
|---|---|
|`Title`| Ajoute du texte aux balises H1, H2 et H3 de l’e-mail. | 
|`Paragraph`| Saisit le texte dans son message. Une barre d’outils permet d’utiliser les polices et la fonction d’édition de texte. | 
|`List`| Ajoute une liste à puces. |
|`Button`| Ajoute un bouton standard. Les propriétés de ce bloc permettent de modifier et de configurer facilement les liens. | 
|`Divider`| Insère une ligne continue, en pointillés ou en tirets pour faciliter l’espacement.|
|`Spacer`| Ajoute de l’espace ou une marge intérieure entre les autres blocs. |
|`Image`| Insère une image de la bibliothèque multimédia. | 
|`Video`| Crée un lien vers le contenu vidéo. |
|`Social`| Insère l’icône de la plateforme des réseaux sociaux. Des images personnalisées peuvent être chargées pour des icônes spécifiques aux marques. |
|`Icons`| Insère une icône. Des images personnalisées peuvent être téléchargées. Une icône de marque substitutive surdimensionnée sera utilisée jusqu’à ce qu’une image soit chargée. |
|`HTML`| Insère l’élément HTML brut. Recommandé pour les liquides, tels que le contenu connecté ou les déclarations conditionnelles. | 
|`Menu`| Crée un menu flexible pour le message que vous créez. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" } 

## Propriétés

Les détails des propriétés de chaque bloc éditeur sont fournis dans les tableaux suivants.

### Titre

| propriétés | Description |
|---|---|
|`Title`| Sélectionne le style de titre. Seuls les titres H1, H2 ou H3 sont disponibles. | 
|`Font family`| Il s’agit du style de police pour votre titre. |
|`Font weight`| Il s’agit de la force globale de la police. |
|`Font size`| Détermine la taille de votre texte. |
|`Text color`| Modifie la couleur du titre. |
|`Link color`| Modifie la couleur du lien. |
|`Align`| Déplace le titre à gauche, au centre ou à droite. |
|`Line height`| Modifie l’espace entre les lignes de texte. |
|`Line spacing`| Modifie l’espace entre chaque caractère. |
|`Text direction`| Valeur par défaut de gauche à droite, mais peut être modifiée de droite à gauche. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Paragraphe

Reportez-vous au tableau suivant pour plus de détails sur les propriétés du bloc éditeur de `Paragraph`.

| propriétés | Description |
|---|---|
|`Font family`| Il s’agit du style de la police de caractères pour votre paragraphe de texte. |
|`Font weight`| Il s’agit de la force globale de la police. |
|`Font size`| Détermine la taille de votre texte. |
|`Text color`| Modifie la couleur du titre. |
|`Link color`| Modifie la couleur du lien. |
|`Align`| Déplace le titre à gauche, au centre ou à droite. |
|`Paragraph spacing`| Modifie l’espace entre les paragraphes. |
|`Line height`| Modifie l’espace entre les lignes de texte. |
|`Letter spacing`| Modifie l’espace entre chaque caractère. |
|`Text direction`| Valeur par défaut de gauche à droite, mais peut être modifiée de droite à gauche. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Liste

Reportez-vous au tableau suivant pour plus de détails sur les propriétés du bloc éditeur de `List`.

| propriétés | Description |
|---|---|
|`List type`| Il s’agit du type de liste. Elle peut être à puces ou numérotée. |
|`List style type`| Détermine le style de votre liste. |
|`Start list from`| Détermine le numéro de départ de votre liste. |
|`Font family`| Il s’agit du style de la police de caractères pour votre paragraphe de texte. |
|`Font weight`| Il s’agit de la force globale de la police. |
|`Font size`| Détermine la taille de votre texte. |
|`Text color`| Modifie la couleur du titre. |
|`Link color`| Modifie la couleur du lien. |
|`Align`| Déplace le titre à gauche, au centre ou à droite. |
|`List items spacing`| Modifie l’espace entre les éléments de liste. |
|`List items indent`| Modifie l’indentation des éléments de liste. |
|`Line height`| Modifie l’espace entre les lignes de texte. |
|`Letter spacing`| Modifie l’espace entre chaque caractère. |
|`Text direction`| Valeur par défaut de gauche à droite, mais peut être modifiée de droite à gauche. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Bouton

Reportez-vous au tableau suivant pour plus de détails sur le bloc éditeur de `Button`.

| propriétés | Description |
|---|---|
|`Link Type`| Détermine l’action lorsque vous cliquez sur le bouton et définit le protocole de lien approprié. |
|`URL`| Dynamique basée sur la sélection `Link Type`.|
|`Button options`| Définit diverses options pour les boutons, telles que la police, la largeur, la couleur, etc.|
|`Button Hover`| Le style du bouton lorsqu'un utilisateur le survole à l'aide d'une souris ou d'un trackpad. Il s'agit de la couleur d'arrière-plan du bouton, de la couleur de la police et des styles de bordure.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Ligne de séparation

Reportez-vous au tableau suivant pour plus de détails sur le bloc éditeur de `Divider`.

| propriétés | Description |
|---|---|
|`Transparent`| Si activé, les options de « ligne » et de « largeur » sont supprimées. |
|`Line`| Les différents formats de lignes, qu’elles soient en pointillés, continues ou discontinues.  De plus, vous pouvez modifier l’épaisseur et la couleur de la ligne de séparation. |
|`Width `| Ajuste l’étendue de la ligne de séparation par incréments de 5.  |
|`Align`| Déplace la ligne à gauche, au centre ou à droite. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Espaceur

Reportez-vous au tableau suivant pour plus de détails sur le bloc éditeur de `Spacer`.

| propriétés | Description |
|---|---|
|`Height`| Ajuste la hauteur du bloc d’espacement. La valeur par défaut est 60px.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Image

Reportez-vous au tableau suivant pour plus de détails sur le bloc éditeur de `Image`. Pour les images dynamiques (images avec Liquid), vous devez définir une image de repli pour utiliser les paramètres de largeur automatique.

| propriétés | Description |
|---|---|
|`Auto Width`| Modifie la largeur de l'image en pixels. |
|`Align`| Oriente l'image vers la gauche, le centre ou la droite du bloc. |
|`Image with Liquid`| Utilisez la logique Liquid pour définir dynamiquement différentes images au sein d'un même bloc de contenu. |
|`URL`| Définissez une image en utilisant l'adresse de l'endroit où elle est hébergée. |
|`Alternate text`| Une courte description de l'image qui donne aux utilisateurs les mêmes informations que celles présentées dans l'image. Ceci est essentiel pour l'accessibilité des lecteurs d'écran ou lorsque l'image ne se charge pas. |
|`Image with Rounded Corners`| Rendre l'image avec des coins arrondis. Par défaut, les images sont rendues avec des coins carrés. |
|`Action`| Déclenche une action lorsque l'utilisateur clique sur l'image.|
|`Block Options`| Définit l'espacement autour du bloc d'image. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert tip %}
Pour `Auto Width`, le redimensionnement automatique d’images choisit la meilleure taille pour l’image selon une combinaison de largeur d’image et d’espace disponible dans la mise en page :
- Les images plus larges que l’espace disponible seront définies à 100 % de largeur et conserveront cette taille sur les appareils mobiles, utilisant ainsi toute la largeur de l’écran de l’appareil.
- Les images plus petites que l’espace disponible utiliseront la taille normale de l’image pour éviter les effets de distorsion ou les images floues.
{% endalert %}

### Vidéo

Reportez-vous au tableau suivant pour plus de détails sur le bloc éditeur de `Video`.

| propriétés | Description |
|---|---|
|`URL`| L’URL de la vidéo. |
|`Title`| Généré automatiquement à partir des métadonnées de la vidéo ou peut être personnalisé.  Notez que seuls YouTube et Vimeo sont pris en charge. |
|`Play Icon Style`| Inclut différentes options pour le bouton de lecture situé en haut d’une image vidéo. |
|`Play Icon Color`| Option permettant de sélectionner **Clair** ou **Foncé** pour le bouton de lecture. |
|`Play Icon Size`| Choisissez la taille du pixel pour le bouton de lecture. Les valeurs préfixées vont de 50 px à 80 px (incrémentées de 5 px). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert tip %}
Les vidéos hébergées par Vimeo ne fonctionneront que si elles sont définies comme publiques. Tous les autres paramètres de sécurité disponibles dans Vimeo (par exemple, « Masquer sur Vimeo.com ») généreront un format de lien différent qui n'est pas pris en charge par ce bloc de contenu. Ces types de liens sont modifiés par le créateur, ce qui empêche Braze de générer une miniature.
{% endalert %}

### Réseaux sociaux

Reportez-vous au tableau suivant pour plus de détails sur le bloc éditeur de `Social`.

| propriétés | Description |
|---|---|
|`Select icon collection`| Définit le style de votre collection d'icônes. |
|`Configure icon collection`| Défini l’URL pour chaque icône sociale. Inclut le basculeur " **Plus d'options"** pour modifier le titre et le texte alternatif. |
|`Align`| Déplace l'icône sociale vers la gauche, le centre ou la droite.
|`Icon spacing`| Détermine l'espacement entre chaque icône sociale. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Icônes

Reportez-vous au tableau suivant pour plus de détails sur le bloc éditeur de `Icons`.

| propriétés | Description |
|---|---|
|`Font family`| Il s’agit du style de la police de caractères pour votre paragraphe de texte. |
|`Font weight`| Il s’agit de la force globale de la police. |
|`Font size`| Détermine la taille de votre texte. |
|`Text color`| Modifie la couleur du titre. |
|`Link color`| Modifie la couleur du lien. |
|`Align`| Déplace l'icône vers la gauche, le centre ou la droite. |
|`Letter spacing`| Modifie l’espace entre chaque caractère. |
|`Icon size`| Détermine la taille de votre icône. |
|`Icon spacing`| Modifie l'espace de l'icône. |
|`Icon padding`| Modifie le remplissage de l'icône. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### HTML

Reportez-vous au tableau suivant pour plus de détails sur le bloc éditeur de `HTML`.

| propriétés | Description |
|---|---|
|`html editor`| Saisir l’élément HTML brut. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Menu

Reportez-vous au tableau suivant pour plus de détails sur le bloc éditeur de `Menu`.

| propriétés | Description |
|---|---|
|`Configure menu items`| Ajouter un élément de menu. |
|`Font Family`| Style à utiliser pour votre menu. |
|`Font Size`| La taille de votre menu. |
|`Text Color`| Modifie la couleur du menu. |
|`Link Color`| Modifie la couleur du texte du menu. |
|`Align`| Déplace le menu à gauche, au centre ou à droite. |
|`Letter spacing`| Modifie l’espace entre chaque caractère. |
|`Layout`| Détermine que la mise en page soit horizontale ou verticale. |
|`Separator`| Ajouter un ou des caractères entre les options de menu. |
|`Mobile menu`| Comprend des options pour modifier la taille de l’icône, la couleur et le type d’icône lorsqu’elle est affiché sur un appareil mobile. |
|`Item padding`| Modifie le padding en utilisant soit le bouton **+** ou **-**, soit en entrant un nombre spécifique. |
|`All sides`| Définit une valeur de marge intérieure uniforme si `Item padding` est désactivé. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Ajouter une personnalisation Liquid

Reportez-vous au tableau suivant pour plus de détails sur `Add Personalization`.

| nom | Description |
|---|---|
| `Add Personalization` | Permet de rechercher des extraits de code Liquid standard tels que des attributs par défaut (standard), des attributs personnalisés, des blocs de contenu, etc. | 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

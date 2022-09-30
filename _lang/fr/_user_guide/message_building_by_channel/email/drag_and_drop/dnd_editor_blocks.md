---
nav_title: Blocs éditeur
article_title: Blocs de l’éditeur Drag & Drop
alias: "/dnd/editor_blocks/"
channel: E-mail
page_order: 1
description: "Le présent article de référence couvre les différents blocs éditeur qui sont fournis dans l’éditeur d’e-mail Drag & Drop."
tool: Media

---

# Blocs éditeur

Les blocs éditeur sont les différents blocs disponibles dans l’éditeur Drag & Drop dans la section **Content (Contenu)**. Cette section comprend une série de mosaïques qui représentent les différents types de contenu que vous pouvez utiliser dans votre message.

Pour les utiliser, faites glisser un bloc éditeur dans une colonne. Il s’ajuste automatiquement à la largeur de la colonne. Chaque bloc éditeur possède ses propres paramètres, tels que le contrôle granulaire sur la marge intérieure. Le panneau latéral droit passe automatiquement à un panneau de propriétés pour l’élément de contenu sélectionné.

## Types

Le tableau suivant décrit comment les utilisateurs peuvent exploiter chaque type de bloc éditeur.

| nom | description |
|---|---|
| `Title`  | Ajoute du texte aux balises H1, H2 et H3 de l’e-mail. | 
| `Text`  |  Saisit le texte dans son message. Une barre d’outils permet d’utiliser les polices et la fonction d’édition de texte. | 
| `Image` | Insère une image de la bibliothèque multimédia. | 
| `Button` |  Ajoute un bouton standard. Les propriétés de ce bloc permettent de modifier et de configurer facilement les liens.  | 
| `Divider` |  Insère une ligne continue, en pointillés ou en tirets pour faciliter l’espacement.|
| `HTML` |  Insère l’élément HTML brut. Idéal pour les fonctions Liquid avancées tels que le contenu connecté ou les instructions conditionnelles. | 
| `Menu` |  Crée un menu flexible pour le message que vous créez. |
| `Spacer` |  Ajoute de l’espace ou une marge intérieure entre les autres blocs. |
| `Social Icon` | Insère l’icône de la plateforme des réseaux sociaux. |
{: .reset-td-br-1 .reset-td-br-2} 

## Propriétés

Les détails des propriétés de chaque bloc éditeur sont fournis dans les tableaux suivants.

### Titre

| propriétés | description |
|---|---|
| `Title`  | Sélectionne le style de titre. Seuls les titres H1, H2 ou H3 sont disponibles. | 
|`Font Family`| Il s’agit du style de police pour votre titre. |
|`Font Size`| Détermine la taille de votre texte. |
|`Text Color`| Modifie la couleur du titre. |
|`Link Color`| Modifie la couleur du lien. |
|`Align`| Déplace le titre à gauche, au centre ou à droite. |
|`Line Height`| Modifie l’espace entre les lignes de texte. |
|`Line spacing`| Modifie l’espace entre chaque caractère. |
|`Text direction`| Valeur par défaut de gauche à droite, mais peut être modifiée de droite à gauche. |
{: .reset-td-br-1 .reset-td-br-2}

### Texte

Reportez-vous au tableau suivant pour plus de détails sur les propriétés du bloc éditeur de `Text`.

| propriétés | description |
|---|---|
|`Text Color`| Modifie la couleur du titre. |
|`Link Color`| Modifie la couleur du lien. |
|`Line Height`| Modifie l’espace entre les lignes de texte|
|`Line spacing`| Modifie l’espace entre chaque caractère|
{: .reset-td-br-1 .reset-td-br-2}

### Image

Reportez-vous au tableau suivant pour plus de détails sur le bloc éditeur de `Image`.

| propriétés | description |
|---|---|
|`Auto Width`| Modifie les pixels de l’image. |
|`Align`| Déplace l’image à gauche, au centre ou à droite. |
|`URL`| L’adresse d’hébergement de votre image. |
|`Alternate text`| La copie écrite qui apparaît à la place d’une image lorsque l’image ne se charge pas. |
{: .reset-td-br-1 .reset-td-br-2}

{% alert tip %}
Pour `Auto Width`, le redimensionnement automatique d’images choisit la meilleure taille pour l’image selon une combinaison de largeur d’image et d’espace disponible dans la mise en page :
- Les images plus larges que l’espace disponible seront définies à 100 % de largeur et conserveront cette taille sur les appareils mobiles, utilisant ainsi toute la largeur de l’écran de l’appareil.
- Les images plus petites que l’espace disponible utiliseront la taille normale de l’image pour éviter les effets de distorsion ou les images floues.
{% endalert %}

### Bouton

Reportez-vous au tableau suivant pour plus de détails sur le bloc éditeur de `Button`.

| propriétés | description |
|---|---|
|`Link Type`| Détermine l’action lorsque vous cliquez sur le bouton et définit le protocole de lien approprié. |
|`URL`| Dynamique basée sur la sélection `Link Type`.|
{: .reset-td-br-1 .reset-td-br-2}

### Ligne de séparation

Reportez-vous au tableau suivant pour plus de détails sur le bloc éditeur de `Divider`.

| propriétés | description |
|---|---|
|`Transparent`| Si activé, les options de « ligne » et de « largeur » sont supprimées. |
|`Line `| Les différents formats de lignes, qu’elles soient en pointillés, continues ou discontinues.  De plus, vous pouvez modifier l’épaisseur et la couleur de la ligne de séparation|
|`Width `| Ajuste l’étendue de la ligne de séparation par incréments de 5  |
|`Align`| Déplace la ligne à gauche, au centre ou à droite |
{: .reset-td-br-1 .reset-td-br-2}

### HTML

Reportez-vous au tableau suivant pour plus de détails sur le bloc éditeur de `HTML`.

| propriétés | description |
|---|---|
|`html editor`| Saisir l’élément HTML brut |
{: .reset-td-br-1 .reset-td-br-2}

### Menu

Reportez-vous au tableau suivant pour plus de détails sur le bloc éditeur de `Menu`.

| propriétés | description |
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
|`Item padding`| Modifie la marge intérieure à l’aide du bouton **+** ou **-** ou en saisissant une valeur spécifique. |
|`All sides`| Définit une valeur de marge intérieure uniforme si `Item padding` est désactivé. |
{: .reset-td-br-1 .reset-td-br-2}

### Espacement

Reportez-vous au tableau suivant pour plus de détails sur le bloc éditeur de `Spacer`.

| propriétés | description |
|---|---|
|`height`| Ajuste la hauteur du bloc d’espacement. La valeur par défaut est 60px.|
{: .reset-td-br-1 .reset-td-br-2}

### Ajouter une personnalisation Liquid

Reportez-vous au tableau suivant pour plus de détails sur `Add Personalization`.

| nom | description |
|---|---|
| `Add Personalization` | Permet de rechercher des extraits de code Liquid standard tels que des attributs par défaut, des attributs personnalisés, des blocs de contenu, etc. | 
{: .reset-td-br-1 .reset-td-br-2}

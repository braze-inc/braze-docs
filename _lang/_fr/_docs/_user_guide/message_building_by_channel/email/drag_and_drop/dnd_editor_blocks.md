---
nav_title: Blocs de l'éditeur
article_title: Glisser & déposer les blocs de l'éditeur
alias: "/dnd/editor_blocks/"
channel: Email
page_order: 2
description: "Cet article de référence couvre les différents blocs d'éditeur qui sont fournis dans l'éditeur de courriel Glisser & Déposer."
tool: Médias
---

# Glisser & déposer les blocs de l'éditeur

Les blocs de l'éditeur sont les différents blocs disponibles dans l'éditeur Glisser & Déposer sous la section 'Contenu'.  Cette section comprend une série de tuiles qui représentent les différents types de contenu que vous pouvez utiliser dans votre message. D'autres seront disponibles à l'avenir.

Pour les utiliser, faites glisser un à l'intérieur d'une colonne. Il s'ajuste automatiquement à la largeur de la colonne.  Chaque bloc de contenu a ses propres paramètres, tels que le contrôle granulaire du remplissage. Le panneau de droite passe automatiquement à un panneau de propriétés pour l'élément de contenu sélectionné.

## Types de bloc

| Nom                | Libellé                                                                                                                |
| ------------------ | ---------------------------------------------------------------------------------------------------------------------- |
| `Titre de la page` | Permet aux utilisateurs d'ajouter du texte avec les balises H1, H2 et H3 pour les courriels.                           |
| `Texte du texte`   | Permet aux utilisateurs de saisir du texte dans leur message.  Une barre d'outils aide à éditer la police et le texte. |
| `Image`            | Permet d'insérer une image de la médiathèque.                                                                          |
| `Bouton`           | Ajouter un bouton standard.  Les propriétés de ce bloc permettent l'édition et le réglage des liens facilement.        |
| `Diviseur`         | Insérez une ligne solide, pointillée ou pointillée pour faciliter l'espacement.                                        |
| `HTML`             | Insert raw HTML.  Idéal pour les liquides avancés tels que le contenu connecté ou les instructions conditionnelles.    |
| `Menu`             | Créez un menu flexible pour le message que vous concevez.                                                              |
| `Espaceur`         | Ajouter de l'espace, ou "remplissage", entre les autres blocs.                                                         |
{: .reset-td-br-1 .reset-td-br-2}

## Propriétés du type de bloc

Les détails pour chaque type de bloc sont fournis ci-dessous.

### Titre de la page

| Propriétés            | Libellé                                                                              |
| --------------------- | ------------------------------------------------------------------------------------ |
| `Titre de la page`    | Sélectionnez le style de l'en-tête.  H1, H2 ou H3 sont disponibles uniquement.       |
| `Famille de police`   | Le style à utiliser pour votre titre                                                 |
| `Font Size`           | La taille de votre texte                                                             |
| `Couleur du texte`    | Modifie la couleur du titre                                                          |
| `Couleur du lien`     | Modifie la couleur du lien                                                           |
| `Align`               | Déplace le titre soit à gauche, au centre ou à droite                                |
| `Hauteur de la ligne` | Modifier la distance entre les lignes de texte                                       |
| `Interligne`          | Modifier la distance entre chaque caractère                                          |
| `Direction du texte`  | Par défaut de gauche à droite, mais peut être modifié pour écrire de droite à gauche |
{: .reset-td-br-1 .reset-td-br-2}

### Texte du texte

| Propriétés            | Libellé                                        |
| --------------------- | ---------------------------------------------- |
| `Couleur du texte`    | Modifie la couleur du titre                    |
| `Couleur du lien`     | Modifie la couleur du lien                     |
| `Hauteur de la ligne` | Modifier la distance entre les lignes de texte |
| `Interligne`          | Modifier la distance entre chaque caractère    |
{: .reset-td-br-1 .reset-td-br-2}

### Image

| Propriétés         | Libellé                                                                              |
| ------------------ | ------------------------------------------------------------------------------------ |
| `Auto Width`       | Modifie le px de l'image                                                             |
| `Align`            | Déplace l'image vers la gauche, le centre ou la droite                               |
| `URL`              | L'adresse hébergée pour votre image                                                  |
| `Texte alternatif` | La copie écrite qui apparaît à la place d'une image lorsque l'image ne se charge pas |
{: .reset-td-br-1 .reset-td-br-2}

{% alert tip %}
_Note à propos de la largeur automatique_ Le redimensionnement automatique de l'image choisit la meilleure taille pour l'image en se basant sur une combinaison de largeur d'image et d'espace disponible dans la mise en page :
- Grandes images, plus larges que l'espace disponible, sera défini à 100% de largeur et conservera ce ratio sur mobile, en utilisant la largeur d'affichage de l'appareil entière.
- Les petites images, plus petites que l'espace disponible, utilisent la taille naturelle de l'image pour éviter des effets de distorsion ou des images floues.
{% endalert %}

### Bouton

| Propriétés  | Libellé                                                                             |
| ----------- | ----------------------------------------------------------------------------------- |
| `Link Type` | L'action désirée en cliquant sur le bouton.  Définit le protocole de lien approprié |
| `URL`       | Dynamique basé sur le type de lien choisi.                                          |
{: .reset-td-br-1 .reset-td-br-2}

### Diviseur

| Propriétés     | Libellé                                                                                                                                                           |
| -------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `Transparence` | Si activé, les options 'ligne' et 'largeur' sont supprimées.                                                                                                      |
| `Lignes`       | Les différents formats de ligne, qu'ils soient pointillés, pointés ou solides.  De plus, vous pouvez modifier l'épaisseur et la couleur de la ligne de séparation |
| `Width`        | Ajuste le spread du diviseur par incréments de 5                                                                                                                  |
| `Align`        | Déplace la ligne à gauche, centre ou à droite                                                                                                                     |
{: .reset-td-br-1 .reset-td-br-2}

### HTML

| Propriétés     | Libellé                  |
| -------------- | ------------------------ |
| `Éditeur html` | Saisir le code HTML brut |
{: .reset-td-br-1 .reset-td-br-2}

### Menu

| Propriétés                        | Libellé                                                                                                                |
| --------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| `Configurer les éléments du menu` | Ajouter un lien de menu                                                                                                |
| `Famille de police`               | Le style à utiliser pour votre menu                                                                                    |
| `Font Size`                       | La taille de votre menu                                                                                                |
| `Couleur du texte`                | Modifie la couleur du menu                                                                                             |
| `Couleur du lien`                 | Modifie la couleur du texte du menu                                                                                    |
| `Align`                           | Déplace le menu vers la gauche, le centre ou la droite                                                                 |
| `Espacement des lettres`          | Modifier la distance entre chaque caractère                                                                            |
| `Mise en page`                    | horizontal ou vertical                                                                                                 |
| `Séparateur`                      | Ajouter des caractères(s) entre les options du menu                                                                    |
| `Menu mobile`                     | Options pour modifier la taille de l'icône, la couleur et le type d'icône lorsqu'il est affiché sur un appareil mobile |
| `Item padding`                    | Si activé, vous pouvez modifier le remplissage en utilisant le bouton + ou - ou en entrant un numéro spécifique        |
| `Tous les côtés`                  | Si le 'remplissage d'élément' est désactivé, définissez un numéro de remplissage cohérent                              |
{: .reset-td-br-1 .reset-td-br-2}

### Espaceur

| Propriétés | Libellé                                                                |
| ---------- | ---------------------------------------------------------------------- |
| `Hauteur`  | Ajuste la hauteur du bloc intercalaire. La valeur par défaut est 60px. |
{: .reset-td-br-1 .reset-td-br-2}

### Ajouter une personnalisation Liquid

| Nom                            | Libellé                                                                                                                                                                            |
| ------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `Ajouter une personnalisation` | Situé dans le menu de gauche.  Permet de rechercher des extraits de liquides standard tels que les attributs par défaut, les attributs personnalisés, les blocs de contenu, etc... |
{: .reset-td-br-1 .reset-td-br-2}

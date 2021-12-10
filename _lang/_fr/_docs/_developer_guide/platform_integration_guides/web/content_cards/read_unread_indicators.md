---
nav_title: Lecture & Indicateurs non lus
article_title: Carte de contenu lue & Indicateurs non lus pour le Web
page_order: 2
platform: Web
channel: cartes de contenu
page_type: Référence
description: "Cet article de référence couvre les indicateurs lus et non lus dans les Cartes de Contenu."
---

# Indicateurs lus et non lus

Braze fournit des indicateurs sur les Cartes de Contenu comme illustré ci-dessous:

| Indicateur | Exemple                     |
| ---------- | --------------------------- |
| Lu         | !\[ReadContentCard\]\[2\]   |
| Non lus    | !\[UnreadContentCard\]\[3\] |
{: .reset-td-br-1 .reset-td-br-2}

## Changement des couleurs

Pour changer la couleur de l'indicateur non lu d'une carte, ajoutez un CSS personnalisé à votre page Web. Par exemple, le changement en vert avec le CSS suivant :

```css
.ab-unread-indicator { background-color: vert !important; }
```

## Désactivation des indicateurs

Afin de désactiver cette fonctionnalité, ajoutez le style suivant à votre `css`:

```css
.ab-unread-indicator { display: none; }
```
[2]:{% image_buster /assets/img_archive/readcontentcard.png %} [3]:{% image_buster /assets/img_archive/unreadcontentcard.png %}

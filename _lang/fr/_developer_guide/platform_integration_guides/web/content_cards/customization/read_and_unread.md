---
nav_title: Indicateurs de messages non lus et lus
article_title: Indicateurs de messages non lus et lus de carte de contenu pour le Web
page_order: 2
platform: Web
channel: cartes de contenu
page_type: reference
description: "Cet article de référence indique comment utiliser et personnaliser les indicateurs de messages non lus et lus de carte de contenu dans votre application Web."

---

# Indicateurs de messages non lus et lus

> Braze fournit des indicateurs sur les cartes de contenu comme indiqué dans les captures d’écran suivantes. Cet article de référence indique comment utiliser et personnaliser les indicateurs de messages non lus et lus de carte de contenu dans votre application Web.

|Indicateur|Exemple |
|---|---|
| Lue | ![Une carte de contenu Web sans ligne bleue sous la carte indique qu’elle a été lue.][2] |
| Non lue | ![Une carte de contenu Web avec une ligne bleue sous la carte indique qu’elle n’a pas été lue.][3] |
{: .reset-td-br-1 .reset-td-br-2}

## Changer les couleurs

Pour modifier la couleur de l’indicateur de messages non lus d’une carte, ajoutez un CSS personnalisé à votre page Web. Par exemple, en changeant la couleur à vert avec le CSS suivant :

```css
.ab-unread-indicator { background-color: green !important; }
```

## Désactiver les indicateurs

Pour désactiver cette fonctionnalité, ajoutez le style suivant à votre `css` :

```css
.ab-unread-indicator { display: none; }
```

[2]:{% image_buster /assets/img_archive/readcontentcard.png %}
[3]:{% image_buster /assets/img_archive/unreadcontentcard.png %}

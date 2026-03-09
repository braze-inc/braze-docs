---
nav_title: Code personnalisé et passerelle JavaScript
article_title: Code personnalisé et pont JavaScript pour les bannières
page_order: 2
page_type: reference
description: "Découvrez comment utiliser le code HTML personnalisé dans les bannières et le pont JavaScript pour enregistrer les clics et utiliser des déclencheurs Braze."
channel:
  - banners
---

# Code personnalisé et pont JavaScript pour les bannières

> Lorsque vous utilisez le bloc éditeur **de code personnalisé** dans le compositeur de bannières, il est nécessaire d'appeler`brazeBridge.logClick()`  depuis votre code HTML personnalisé pour enregistrer les clics. Les bannières utilisent le même pont JavaScript que les messages in-app, donc les mêmes méthodes et modèles s'appliquent.

Si vous utilisez du code HTML personnalisé dans votre conception de bannière, le SDK Braze ne peut pas associer automatiquement des écouteurs de clic aux éléments de votre code personnalisé. Il est `brazeBridge.logClick()`nécessaire d'appeler explicitement tout élément cliquable (liens, boutons et autres éléments similaires) que vous souhaitez suivre dans les analyses de campagne.

Par exemple, pour enregistrer un clic lorsqu'un utilisateur appuie sur un bouton dans votre code HTML personnalisé :

```html
<button onclick="brazeBridge.logClick()">
  Click me
</button>
```

Pour obtenir la référence complète du pont JavaScript, y compris toutes les méthodes disponibles et les options de suivi des clics, veuillez consulter la section ci-dessous.

## Pont JavaScript {#javascript-bridge}

{% include javascript_bridge/reference.md %}

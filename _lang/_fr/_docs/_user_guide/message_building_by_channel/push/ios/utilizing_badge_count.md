---
nav_title: Utiliser le nombre de badges
article_title: Utiliser le nombre de badges
page_order: 8
page_type: Référence
description: "Cet article couvre l'utilisation du nombre de badges iOS pour réengager les utilisateurs qui n'ont pas remarqué de push, ou qui ont désactivé les notifications push en premier plan."
platform: iOS
channel:
  - Pousser
  - messages intégrés à l'application
  - fil d'actualité
---

# Utilisation du nombre de badges

Le nombre de badges iOS affiche le nombre de notifications non lues dans votre application, en prenant la forme d'un cercle rouge dans le coin supérieur droit de l'icône de l'application. Ces dernières années, le badging est devenu un moyen efficace de réengager les utilisateurs de l'application.

Le nombre de badges peut être utilisé pour réengager vos utilisateurs qui n'ont pas remarqué de push, ou qui ont désactivé les notifications push en premier plan. De même, il peut être utilisé pour informer vos utilisateurs des messages non consultés tels que les changements de flux d'actualités ou les mises à jour dans l'application.

## Nombre de badges avec Braze

Vous pouvez spécifier le nombre de badges désirés lorsque vous composez une notification push via le tableau de bord de Brase. Cela peut être réglé sur un attribut utilisateur avec la messagerie personnalisée de Brase, permettant une logique infiniment personnalisable. Si vous souhaitez envoyer un push silencieux qui met à jour le nombre de badges sans déranger l'utilisateur, ajouter le drapeau "Content-Available" à votre push et laisser son contenu vide.

### Suppression du nombre de badges

Définissez le nombre de badges à 0 ou "" pour supprimer le nombre de badges de l'icône de l'application. Braze effacera également automatiquement le badge quand une notification push est reçue lorsque l'application est au premier plan.

## Meilleures pratiques

Afin d'optimiser la puissance de réengagement du badging, il est crucial de configurer les paramètres de votre badge de manière à simplifier au maximum l'expérience de l'utilisateur.

### Garder le nombre de badges bas
La recherche montre qu'une fois que le nombre de badges augmente les doubles chiffres passés, les utilisateurs perdent généralement de l'intérêt pour les mises à jour et cessent souvent d'utiliser l'application tout à fait ensemble.

> Il peut y avoir des exceptions à cette règle en fonction de la nature de votre application (par exemple, des applications de messagerie électronique et de messagerie de groupe).

### Limiter les choses qu'un nombre de badges peut représenter
Lorsque vous insignez, vous voulez rendre les notifications aussi claires et directes que possible. En limitant le nombre de choses qu'un badge peut représenter, vous pouvez fournir à vos utilisateurs un sentiment de familiarité avec les fonctionnalités et les mises à jour de votre application.

### Flux d'actualité et badge dans l'application
L'une des fonctionnalités les plus puissantes du badging est qu'il vous permet de vous engager avec vos utilisateurs sans l'urgence d'une notification push par le biais des mises à jour des News Feed et de l'application. Pour vous assurer que vos utilisateurs restent intéressés par les notifications de badge in-app, vous devez essayer de concentrer ces mises à jour de badge sur des messages personnalisés ou urgents.

---
nav_title: Utilisation du nombre de badges
article_title: Utilisation du nombre de badges
page_order: 8

page_type: reference
description: "Cet article traite de l’utilisation du nombre de badges iOS pour réengager les utilisateurs qui n’ont pas remarqué une notification push ou qui ont désactivé les notifications push de premier plan."
platform: iOS
channel: 
- push
- in-app messages

---

# Utilisation du nombre de badges

> Le compteur de badges iOS affiche le nombre de notifications non lues dans votre application, sous la forme d’un cercle rouge dans le coin supérieur droit de l’icône de l’application. Ces dernières années, l’utilisation de badges est un moyen efficace de réengager les utilisateurs d’applications.

Le nombre de badges peut être utilisé pour réengager vos utilisateurs qui n’ont pas remarqué la notification push ou qui ont désactivé les notifications push de premier plan. De même, il peut être utilisé pour informer vos utilisateurs des messages non consultés, tels que les mises à jour dans l’application.

## Nombre de badges avec Braze

Vous pouvez spécifier le nombre de badges souhaité lorsque vous composez une notification push via le tableau de bord de Braze. Ceci peut être défini comme un attribut de l'utilisateur avec un envoi de messages personnalisés, ce qui permet une logique personnalisable à l'infini. Si vous souhaitez envoyer une notification push silencieuse qui met à jour le nombre de badges sans perturber l’utilisateur, ajoutez l’indicateur « Content-Available » (Contenu disponible) à votre notification push et laissez le contenu de son message vide.

{% alert note %}
Vous vous demandez comment décompter les badges sur Android ? Android traite automatiquement l’affectation de badges par l’application des notifications push, il n’existe donc aucun paramètre de personnalisation pour les badges dans Braze.
{% endalert %}

### Retrait du nombre de badges

Définissez le nombre de badges sur 0 ou sur "" pour supprimer le nombre de badges de l’icône de l’application. Braze efface automatiquement le nombre de badges lorsqu’une notification push est reçue pendant que l’application est au premier plan.

## Bonnes pratiques

Afin d’optimiser la puissance de réengagement de l’utilisation de badges, il est essentiel que vous configuriez vos paramètres de badge de manière à simplifier l’expérience de l’utilisateur.

### Maintenir le nombre de badges bas
Les recherches montrent qu'une fois que le nombre de badges dépasse les deux chiffres, les utilisateurs se désintéressent généralement des mises à jour et cessent souvent complètement d'utiliser l'application.

> Il peut y avoir des exceptions à cette règle en fonction de la nature de votre application (par exemple, les e-mails et les applications d'envoi de messages en groupe).

### Limiter les éléments associés au nombre de badges
Lorsque vous utilisez les badges, vous voulez rendre les notifications aussi claires et directes que possible. En limitant le nombre de choses qu’une notification de badge peut représenter, vous pouvez fournir à vos utilisateurs un sentiment de familiarité avec les fonctionnalités et les mises à jour de votre application.


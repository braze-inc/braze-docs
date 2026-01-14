---
nav_title: Utilisation du nombre de badges
article_title: Utilisation du nombre de badges
page_order: 8

page_type: reference
description: "Cet article traite de l'utilisation du nombre de badges iOS pour réengager les utilisateurs qui n'ont pas remarqué un push, ou qui ont désactivé les notifications push au premier plan."
platform: iOS
channel: 
- push
- in-app messages

---

# Utilisation du nombre de badges

> Le compteur de badges iOS affiche le nombre de notifications non lues au sein de votre application, prenant la forme d'un cercle rouge dans le coin supérieur droit de l'icône de l'application. Ces dernières années, le badge s'est imposé comme un moyen efficace pour réengager les utilisateurs d'applis.

Le décompte des badges peut être utilisé pour réengager vos utilisateurs qui n'ont pas remarqué un push, ou qui ont désactivé les notifications push au premier plan. De même, il peut être utilisé pour notifier à vos utilisateurs des messages non visualisés tels que des mises à jour in-app.

## Comptage des badges avec Braze

Vous pouvez spécifier le nombre de badges souhaité lorsque vous composez une notification push via le tableau de bord de Braze. Il peut être défini comme un attribut de l'utilisateur avec un envoi de messages personnalisés, ce qui permet une logique personnalisable à l'infini. Si vous souhaitez envoyer un push silencieux qui met à jour le nombre de badges sans déranger l'utilisateur, ajoutez le drapeau "Content-Available" à votre push et laissez le contenu de son message vide.

{% alert note %}
Vous vous demandez comment définir le nombre de badges pour Android ? Android gère automatiquement le badgeage des applications pour le push, il n'y a donc pas de paramètres de personnalisation pour le badgeage dans Braze.
{% endalert %}

### Suppression du nombre de badges

Réglez le nombre de badges sur 0 ou sur "" pour supprimer le nombre de badges de l'icône de l'application. Braze effacera également automatiquement le badge lorsqu'une notification push est reçue alors que l'application est au premier plan.

## Meilleures pratiques

Afin d'optimiser le pouvoir de réengagement des badges, il est essentiel que vous configuriez les paramètres de vos badges de manière à simplifier au maximum l'expérience de l'utilisateur.

### Limitez le nombre de badges
Les recherches montrent qu'une fois que le nombre de badges dépasse les deux chiffres, les utilisateurs se désintéressent généralement des mises à jour et cessent souvent complètement d'utiliser l'application.

> Il peut y avoir des exceptions à cette règle en fonction de la nature de votre application (par exemple, les e-mails et les applications d'envoi de messages en groupe).

### Limiter les choses qu'un nombre de badges peut représenter
Lorsque vous badgez, vous voulez que les notifications soient aussi claires et directes que possible. En limitant le nombre de choses qu'une notification de badge peut représenter, vous pouvez donner à vos utilisateurs un sentiment de familiarité avec les fonctionnalités et les mises à jour de votre appli.


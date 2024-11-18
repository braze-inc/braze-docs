---
nav_title: Chevauchement de la barre de défilement
article_title: Chevauchement de la barre de défilement
page_order: 0

page_type: solution
description: "Cet article aide les utilisateurs sur Mac à résoudre les problèmes de barre de défilement sur les documents de Braze."
---

# Chevauchement de la barre de défilement

Vous êtes sur Mac et vos barres de défilement chevauchent le contenu de la documentation Braze comme dans l’exemple suivant ?

![Exemple de chevauchement de la barre de défilement][1]

Vérifiez si votre barre de défilement chevauche le bloc de code suivant :

```
<your-bucket-prefix>/dataexport.<cluster-identifier>.S3.integration.<integration-id>/event_type=<event-type>/date=<date>/<schema-id>/<zone>/dataexport.<cluster-identifier>.S3.integration.<integration-id>+<partition>+<offset>.avro
```

Si votre barre de défilement chevauche le bloc de code, nous vous suggérons de modifier le paramètre **Afficher les barres de défilement :** sur **Toujours** dans vos **paramètres généraux**. Cela permettra d’étendre les éléments des documents (comme les blocs de code) pour toujours afficher la barre de défilement et empêcher l’illisibilité.

![Paramètres généraux MacOS][2]

Voici à quoi votre barre de défilement mise à jour devrait ressembler maintenant :

![Exemple de barre de défilement fixe sans chevauchement][3]

_Dernière mise à jour le 27 mars 2019_

{% comment %}
Insérez ceci là où il existe une seule ligne de code long pouvant causer des problèmes :
_Vous ne voyez pas le code à cause de la barre de défilement ? Vous trouverez [ici la]({{site.baseurl}}/help/help_articles/docs/scroll_bar_overlap/) marche à suivre pour y remédier._
{% endcomment %}

[1]: {% image_buster /assets/img/scroll-overlap.png %}
[2]: {% image_buster /assets/img/general-on-mac.png %}
[3]: {% image_buster /assets/img/scroll-bar-on.png %}

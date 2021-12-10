---
nav_title: Chevauchement de la barre de défilement
article_title: Chevauchement de la barre de défilement
page_order: 0
page_type: Solution
description: "Cet article aide les utilisateurs de Mac à comprendre comment résoudre les barres de défilement qui chevauchent le contenu dans la documentation de Braze."
---

# Chevauchement de la barre de défilement

Utilisez-vous un Mac et découvrez que vos barres de défilement se chevauchent dans Braze Docs comme l'exemple ci-dessous ?

!\[Chevauchement de la barre de défilement\]\[1\]

Vérifiez si votre barre de défilement chevauche le bloc de code ci-dessous:

```
<your-bucket-prefix>/dataexport.<cluster-identifier>.S3.intégration.<integration-id>/event_type=<event-type>/date=<date>/<schema-id>/<zone>/dataexport.<cluster-identifier>.S3.integration.<integration-id>+<partition>+<offset>.avro
```

Si votre barre de défilement chevauche le bloc de code, nous vous suggérons de modifier la barre de défilement `:` à "Toujours" dans vos paramètres généraux. Cela va étendre les fonctionnalités de Docs (comme les blocs de code) pour toujours afficher la barre de défilement et éviter l'illégitimité.

!\[Paramètres généraux\]\[2\]

Voici à quoi devrait ressembler votre barre de défilement actualisée maintenant :

!\[Scroll Fixed\]\[3\]

_Dernière mise à jour le 27 mars 2019_

{% comment %}
Insérez ceci là où il y a une seule ligne de code long qui pourrait causer des problèmes : _Impossible de voir le code à cause de la barre de défilement ? Voir comment résoudre cela [ici]({{site.baseurl}}/help/help_articles/docs/scroll_bar_overlap/)._
{% endcomment %}
[1]: {% image_buster /assets/img/scroll-overlap.png %} [2]: {% image_buster /assets/img/general-on-mac.png %} [3]: {% image_buster /assets/img/scroll-bar-on.png %}

---
nav_title: "Objet Alias de l'utilisateur"
article_title: Objet API User Alias Object
page_order: 11
page_type: Référence
description: "Cet article explique les différents composants de l'objet User Alias."
---

# Spécification de l'objet alias de l'utilisateur

Un alias sert d'identifiant d'utilisateur unique alternatif. Utiliser des alias pour identifier les utilisateurs avec des dimensions différentes de votre identifiant utilisateur principal :
- Définissez un identifiant cohérent pour les analytiques qui suivront un utilisateur donné avant et après qu'ils se soient connectés à une application mobile ou à un site web.
- Ajoutez les identifiants utilisés par un fournisseur tiers à vos utilisateurs de Braze pour réconcilier plus facilement vos données en externe.

L'objet Alias Utilisateur se compose de deux parties : un `alias_name` pour l'identifiant lui-même, et un `alias_label` indiquant le type d'alias. Les utilisateurs peuvent avoir plusieurs alias avec _différentes_ étiquettes, mais un seul `alias` par `alias_label`.

Cet objet est fréquemment utilisé dans tous nos terminaux, et souvent dans d'autres objets.

## Corps de l'objet
```json
{
  "user_alias" : {
    "alias_name" : (requis, chaîne),
    "alias_label" : (requis, chaîne)
  }
 } }
```

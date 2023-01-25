---
nav_title: "Objet alias utilisateur"
article_title: Objet alias utilisateur API
page_order: 11
page_type: reference
description: "Cet article explique les différents composants de l’objet alias utilisateur."

---

# Spécification de l’objet alias utilisateur

Un alias sert d’identifiant utilisateur unique alternatif. Utilisez des alias pour identifier les utilisateurs de dimensions autres que votre ID utilisateur principal :
- Définissez un identifiant cohérent pour l’analyse qui suivra un utilisateur donné avant et après qu’il s’est connecté à une application mobile ou un site Internet.
- Ajoutez les identifiants utilisés par un fournisseur tiers à vos utilisateurs Braze afin de faciliter le rapprochement de vos données en externe.

L’objet alias utilisateur se compose de deux parties : un `alias_name` pour l’identifiant lui-même et `alias_label` indiquant le type d’alias. Les utilisateurs peuvent avoir plusieurs alias avec différentes étiquettes, mais seulement un `alias_name` par `alias_label`.

Cet objet est fréquemment utilisé dans tous nos endpoints, et souvent dans d’autres objets.

## Corps de l’objet
```json
{
  "user_alias" : {
    "alias_name" : (required, string),
    "alias_label" : (required, string)
  }
}
```

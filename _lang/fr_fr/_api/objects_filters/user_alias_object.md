---
nav_title: "Objet Alias utilisateur"
article_title: Objet Alias utilisateur API
page_order: 11
page_type: reference
description: "Cet article de référence explique les différents composants de l’objet Alias utilisateur."

---

# Objet Alias utilisateur

> Un alias sert d’identifiant utilisateur unique alternatif. En utilisant un objet alias utilisateur, vous pouvez définir un identifiant cohérent pour les analyses qui suivra un utilisateur donné avant et après qu'il se soit connecté à une application mobile ou à un site web. Vous pouvez également utiliser cet objet pour ajouter les identifiants utilisés par un fournisseur tiers à vos utilisateurs Braze afin de concilier plus facilement vos données en externe.

L’objet Alias utilisateur se compose de deux parties : un `alias_name` pour l’identifiant lui-même et un `alias_label` indiquant le type d’alias. Les utilisateurs peuvent avoir plusieurs alias avec différentes étiquettes, mais seulement un `alias_name` par `alias_label`.

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

### Exemple

```json
{
  "user_alias": {
    "alias_name": "john_doe_123",
    "alias_label": "email_id"
  },
  "external_id": "user_456"
}
```
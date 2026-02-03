---
nav_title: "Objeto de alias de usuário"
article_title: Objeto de alias de usuário da API
page_order: 11
page_type: reference
description: "Este artigo de referência explica os diferentes componentes do objeto de alias de usuário."

---

# Objeto de alias de usuário

> Um alias serve como um identificador de usuário exclusivo alternativo. Usando um objeto de alias de usuário, é possível definir um identificador consistente para análise de dados que seguirá um determinado usuário antes e depois do registro em um app móvel ou site. Também é possível usar esse objeto para adicionar os identificadores usados por um fornecedor terceirizado aos seus usuários do Braze para reconciliar mais facilmente seus dados externamente.

O objeto de alias de usuário consiste em duas partes: um `alias_name` para o próprio identificador e um `alias_label` indicando o tipo de alias. Os usuários podem ter vários aliases com rótulos diferentes, mas apenas um `alias_name` por `alias_label`.

Esse objeto é usado com frequência em todos os nossos endpoints e, muitas vezes, em outros objetos.

## Corpo do objeto

```json
{
  "user_alias" : {
    "alias_name" : (required, string),
    "alias_label" : (required, string)
  }
}
```

### Exemplo

```json
{
  "user_alias": {
    "alias_name": "john_doe_123",
    "alias_label": "email_id"
  },
  "external_id": "user_456"
}
```
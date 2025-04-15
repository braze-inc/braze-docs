---
nav_title: Definição de IDs de usuário
article_title: Configuração de IDs de usuário para o Roku
platform: Roku
page_order: 0
page_type: reference
description: "Este artigo de referência aborda métodos para identificar e definir IDs de usuário para o Roku, bem como práticas recomendadas e considerações importantes."
 
---

# Definição de IDs de usuário

> Este artigo de referência aborda métodos para identificar e definir IDs de usuário para o Roku, bem como práticas recomendadas e considerações importantes.

{% multi_lang_include archive/setting_user_ids/setting_user_ids.md %}

A seguinte chamada deve ser feita assim que o usuário for identificado (geralmente após o registro) para definir o ID do usuário:

```brightscript
m.Braze.setUserId(YOUR_USER_ID_STRING)
```

## Convenção de nomenclatura de ID de usuário sugerida

{% multi_lang_include archive/setting_user_ids/naming_convention.md %}

## Práticas recomendadas e notas para integração de ID do usuário

{% multi_lang_include archive/setting_user_ids/best_practices.md %}


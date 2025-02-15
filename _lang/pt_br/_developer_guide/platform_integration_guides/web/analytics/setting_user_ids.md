---
nav_title: Definição de IDs de usuário
article_title: Definição de IDs de usuário para a Web
platform: Web
page_order: 1
page_type: reference
description: "Este artigo descreve como definir IDs de usuário para cada um dos seus usuários, incluindo práticas recomendadas e pontos importantes a serem considerados antes de fazer qualquer alteração."
 
---

# Definição de IDs de usuário

> Este artigo descreve como definir IDs de usuário para cada um dos seus usuários, incluindo práticas recomendadas e pontos importantes a serem considerados antes de fazer qualquer alteração.

{% multi_lang_include archive/setting_user_ids/setting_user_ids.md %}

A seguinte chamada deve ser feita assim que o usuário for identificado (geralmente após o registro) para definir o ID do usuário:

```javascript
braze.changeUser(YOUR_USER_ID_STRING);
```

{% alert warning %}
**Não ligue para `changeUser()` quando um usuário fizer o registro de saída.** A configuração de `changeUser()` como um valor padrão estático associará TODAS as atividades do usuário a esse "usuário" padrão até que o usuário registre novamente.
{% endalert %}

Não é recomendável alterar o ID do usuário quando um usuário faz o registro, pois isso impossibilita o direcionamento de campanhas de reengajamento para o usuário conectado anteriormente. Se você antecipar vários usuários no mesmo dispositivo, mas quiser direcionar apenas um deles quando o aplicativo estiver em um estado de logout, recomendamos acompanhar separadamente o ID de usuário que deseja direcionar enquanto estiver desconectado e voltar para esse ID de usuário como parte do processo de logout do app.

Para saber mais, consulte a [`changeUser()` Javadocs](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#changeuser "documentação").

## Sugestão de convenção de nomenclatura de ID de usuário

{% multi_lang_include archive/setting_user_ids/naming_convention.md %}

## Práticas recomendadas e notas para integração de ID do usuário

{% multi_lang_include archive/setting_user_ids/best_practices.md %}

## Aliasing de usuários

{% multi_lang_include archive/setting_user_ids/aliasing.md plataforma="Web" %}


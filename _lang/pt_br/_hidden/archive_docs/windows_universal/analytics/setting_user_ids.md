---
nav_title: Definir IDs de usuário
article_title: Definir IDs de usuário para Windows Universal
platform: Windows Universal
page_order: 1
description: "Este artigo de referência aborda como configurar IDs de usuário na plataforma Windows Universal."
hidden: true
---

# Definir IDs de usuário
{% multi_lang_include archive/windows_deprecation.md %}

{% multi_lang_include archive/setting_user_ids/setting_user_ids.md %}

A seguinte chamada deve ser feita assim que o usuário for identificado (geralmente após o registro) para definir o ID do usuário:

```csharp
Appboy.SharedInstance.ChangeUser(YOUR_USER_ID_STRING);
```

{% alert warning %}
**Não chame `changeUser()` quando um usuário fizer logout. `changeUser()` só deve ser usado quando o usuário fizer o registro no aplicativo.** A configuração de `changeUser()` como um valor padrão estático associará TODAS as atividades do usuário a esse "usuário" padrão até que o usuário acesse novamente.
{% endalert %}

Além disso, recomendamos não alterar o ID do usuário quando um usuário se desconecta, pois isso impede o direcionamento de campanhas de reengajamento para o usuário conectado anteriormente. Se você prevê múltiplos usuários no mesmo dispositivo, mas deseja direcionar apenas um deles quando seu aplicativo estiver desconectado, recomendamos manter separadamente o rastreamento do ID do usuário que você deseja direcionar enquanto estiver desconectado e retornar a esse ID de usuário como parte do processo de logout do seu aplicativo.

## Sugestão de convenção de nomenclatura de ID de usuário

{% multi_lang_include archive/setting_user_ids/naming_convention.md %}

## Práticas recomendadas e notas para integração de ID do usuário

{% multi_lang_include archive/setting_user_ids/best_practices.md %}


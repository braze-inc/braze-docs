---
nav_title: Definindo IDs de Usuário
article_title: Configurando IDs de Usuário para Unity
platform: 
  - Unity
  - iOS
  - Android
page_order: 0
description: "Este artigo de referência explica como definir IDs de usuário na plataforma Unity, incluindo convenções de nomenclatura sugeridas e melhores práticas."
 
---

# Configurando IDs de usuário

> Este artigo de referência explica como definir IDs de usuário na plataforma Unity, incluindo convenções de nomenclatura sugeridas e melhores práticas.

{% multi_lang_include archive/setting_user_ids/setting_user_ids.md %}

Você deve fazer a seguinte chamada assim que o usuário for identificado (geralmente após o login) para definir o ID do usuário:

```csharp
AppboyBinding.ChangeUser("YOUR_USER_ID_STRING");
```

{% alert warning %}
**Não chame `ChangeUser()` quando um usuário fizer logout. `ChangeUser()` só deve ser usado quando o usuário fizer o registro no aplicativo.** A configuração de `ChangeUser()` como um valor padrão estático associará TODAS as atividades do usuário a esse "usuário" padrão até que o usuário acesse novamente.
{% endalert %}

Além disso, recomendamos não alterar o ID do usuário quando um usuário faz logout, pois isso impede que você possa direcionar o usuário anteriormente logado com campanhas de re-engajamento. Se você antecipar vários usuários no mesmo dispositivo, mas quiser direcionar apenas um deles quando seu app estiver em um estado desconectado, recomendamos acompanhar separadamente o ID do usuário que você deseja direcionar enquanto estiver desconectado e voltar para esse ID de usuário como parte do processo de sair do seu app.

## Sugestão de convenção de nomenclatura de ID de usuário

{% multi_lang_include archive/setting_user_ids/naming_convention.md %}

## Práticas recomendadas e notas para integração de ID do usuário

{% multi_lang_include archive/setting_user_ids/best_practices.md %}

[1]: {{site.baseurl}}/developer_guide/rest_api/user_data/#user-data
[2]: {{site.baseurl}}/api/endpoints/messaging/

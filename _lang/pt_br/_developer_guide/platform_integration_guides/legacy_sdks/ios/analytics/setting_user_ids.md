---
nav_title: Definição de IDs de usuário
article_title: Configuração de IDs de usuário para iOS
platform: iOS
page_order: 1
description: "Este artigo de referência mostra como definir IDs de usuário em seu app iOS, convenções de nomenclatura de IDs de usuário sugeridas e algumas práticas recomendadas."
 
noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Definição de IDs de usuário para iOS

{% multi_lang_include archive/setting_user_ids/setting_user_ids.md %}

## Convenção de nomenclatura de ID de usuário sugerida

{% multi_lang_include archive/setting_user_ids/naming_convention.md %}

## Atribuindo uma ID de usuário

A seguinte chamada deve ser feita assim que o usuário for identificado (geralmente após o registro) para definir o ID do usuário:

{% tabs %}
{% tab OBJECTIVE C %}

```objc
[[Appboy sharedInstance] changeUser:@"YOUR_USER_ID_STRING"];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.changeUser("YOUR_USER_ID")
```

{% endtab %}
{% endtabs %}

{% alert warning %}
**Não chame `changeUser()` quando um usuário fizer logout. `changeUser()` só deve ser chamado quando o usuário fizer o registro no app.** A definição de [`changeUser()`](https://appboy.github.io/appboy-ios-sdk/docs/interface_appboy.html#ac8b369b40e15860b0ec18c0f4b46ac69%20%22changeuser%22) para um valor padrão estático associará TODAS as atividades do usuário a esse "usuário" padrão até que o usuário se registre novamente.
{% endalert %}

Certifique-se de chamar esse método na thread principal do aplicativo. Chamar o método de forma assíncrona pode levar a um comportamento indefinido.

Além disso, recomendamos não alterar o ID do usuário quando um usuário se desconecta, pois isso impede o direcionamento de campanhas de reengajamento para o usuário conectado anteriormente. Se você antecipar vários usuários no mesmo dispositivo, mas quiser direcionar apenas um deles quando o aplicativo estiver em um estado de logout, recomendamos acompanhar separadamente o ID de usuário que deseja direcionar enquanto estiver desconectado e voltar para esse ID de usuário como parte do processo de logout do app.

## Notas e práticas recomendadas de integração de ID de usuário

{% multi_lang_include archive/setting_user_ids/best_practices.md %}

## Aliasing de usuários

{% multi_lang_include archive/setting_user_ids/aliasing.md platform="iOS" %}


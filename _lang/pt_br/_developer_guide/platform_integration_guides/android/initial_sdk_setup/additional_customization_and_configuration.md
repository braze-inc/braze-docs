---
nav_title: Outras personalizações de SDK
article_title: Outras personalizações de SDK para Android e FireOS
page_order: 3
platform: 
  - Android
  - FireOS
description: "Este artigo de referência cobre opções adicionais de personalização e configuração, como registro detalhado, supressão de registro e como implementar várias chaves de API."

---

# Outras personalizações de SDK para Android e FireOS

> Este artigo de referência cobre opções adicionais de personalização e configuração, como registro detalhado, supressão de registro e como implementar várias chaves de API.

## Usando R8/ProGuard com Braze

A configuração de [redução de código](https://developer.android.com/studio/build/shrink-code) é incluída automaticamente com sua integração Braze.

Os aplicativos do cliente que ofuscam o código da Braze devem armazenar arquivos de mapeamento de versão para que a Braze interprete os rastreamentos de pilha. Se você quiser manter todo o código da Braze, adicione o seguinte ao seu arquivo ProGuard:

```
-keep class bo.app.** { *; }
-keep class com.braze.** { *; }
```

## Registro

Por padrão, o nível de registro do Braze Android SDK é definido como `INFO`. Você pode [suprimir esses registros](#suppressing-logs) ou [definir um nível de registro diferente](#enabling-logs), como `VERBOSE`, `DEBUG` ou `WARN`.

### Ativação de registros {#enabling-logs}

Para ajudar a solucionar problemas no seu app, ou reduzir o tempo de resposta com o suporte da Braze, você vai querer ativar registros detalhados para o SDK. Quando você enviar registros detalhados para o suporte da Braze, certifique-se de que eles comecem assim que você lançar seu aplicativo e terminem muito depois que seu problema ocorrer.

Lembre-se de que registro detalhados são destinados apenas para o seu ambiente de desenvolvimento, então é interessante desativá-los antes de lançar seu app.

{% alert important %}
Ativar registros detalhados antes de qualquer outra chamada em `Application.onCreate()` para garantir que seus registros sejam o mais completos possível.
{% endalert %}

{% tabs %}
{% tab Aplicativo %}
Para ativar logs diretamente no seu app, adicione o seguinte ao método `onCreate()` do seu aplicativo antes de qualquer outro método.

{% subtabs %}
{% subtab JAVA %}
```java
BrazeLogger.setLogLevel(Log.MIN_LOG_LEVEL);
```
{% endsubtab %}

{% subtab KOTLIN %}
```kotlin
BrazeLogger.logLevel = Log.MIN_LOG_LEVEL
```
{% endsubtab %}
{% endsubtabs %}

Substitua `MIN_LOG_LEVEL` pelo **Constante** do nível de registro que você gostaria de definir como seu nível de registro mínimo. Quaisquer registro em um nível `>=` para o seu conjunto `MIN_LOG_LEVEL` serão encaminhados para o método padrão do Android [`Log`](https://developer.android.com/reference/android/util/Log). Qualquer registro `<` que você definir como `MIN_LOG_LEVEL` será descartado.

| Constante    | Valor          | Descrição                                                               |
|-------------|----------------|---------------------------------------------------------------------------|
| `VERBOSE`   | 2              | Registra as mensagens mais detalhadas para depuração e desenvolvimento.            |
| `DEBUG`     | 3              | Registra mensagens descritivas para depuração e desenvolvimento.                  |
| `INFO`      | 4              | Registra mensagens informativas para destaques gerais.                       |
| `WARN`      | 5              | Registra mensagens de aviso para identificar situações potencialmente prejudiciais.     |
| `ERROR`     | 6              | Registra mensagens de erro para indicar falha no aplicativo ou problemas sérios. |
| `ASSERT`    | 7              | Registra mensagens de asserção quando as condições são falsas durante o desenvolvimento.     |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Por exemplo, o código a seguir encaminhará os níveis de registro `2`, `3`, `4`, `5`, `6` e `7` para o método `Log`.

{% subtabs %}
{% subtab JAVA %}
```java
BrazeLogger.setLogLevel(Log.VERBOSE);
```
{% endsubtab %}

{% subtab KOTLIN %}
```kotlin
BrazeLogger.logLevel = Log.VERBOSE
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab braze.xml %}
Para ativar registros no `braze.xml`, adicione o seguinte ao seu arquivo:

```xml
<integer name="com_braze_logger_initial_log_level">MIN_LOG_LEVEL</integer>
```

Substitua `MIN_LOG_LEVEL` pelo **Valor** do nível de registro que você gostaria de definir como seu nível de registro mínimo. Quaisquer registro em um nível `>=` para o seu conjunto `MIN_LOG_LEVEL` serão encaminhados para o método padrão do Android [`Log`](https://developer.android.com/reference/android/util/Log). Qualquer registro `<` que você definir como `MIN_LOG_LEVEL` será descartado.

| Constante    | Valor          | Descrição                                                               |
|-------------|----------------|---------------------------------------------------------------------------|
| `VERBOSE`   | 2              | Registra as mensagens mais detalhadas para depuração e desenvolvimento.            |
| `DEBUG`     | 3              | Registra mensagens descritivas para depuração e desenvolvimento.                  |
| `INFO`      | 4              | Registra mensagens informativas para destaques gerais.                       |
| `WARN`      | 5              | Registra mensagens de aviso para identificar situações potencialmente prejudiciais.     |
| `ERROR`     | 6              | Registra mensagens de erro para indicar falha no aplicativo ou problemas sérios. |
| `ASSERT`    | 7              | Registra mensagens de asserção quando as condições são falsas durante o desenvolvimento.     |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Por exemplo, o código a seguir encaminhará os níveis de registro `2`, `3`, `4`, `5`, `6` e `7` para o método `Log`.

```xml
<integer name="com_braze_logger_initial_log_level">2</integer>
```
{% endtab %}
{% endtabs %}

### Verificação de registros detalhados

Para verificar se seus registros estão definidos para `VERBOSE`, verifique se `V/Braze` ocorre em algum lugar nos seus registros. Se isso acontecer, os registros detalhados foram ativados com sucesso. Por exemplo:

```
2077-11-19 16:22:49.591 ? V/Braze v9.0.01 .bo.app.d3: Request started
```

### Supressão de registros

O nível de registro padrão para o Braze Android SDK é `INFO`. Para suprimir todos os registros para o Braze Android SDK, chame `BrazeLogger.SUPPRESS` no método `onCreate()` do seu app _antes_ de qualquer outro método.

{% tabs local %}
{% tab JAVA %}
```java
BrazeLogger.setLogLevel(BrazeLogger.SUPPRESS);
```
{% endtab %}

{% tab KOTLIN %}
```kotlin
BrazeLogger.setLogLevel(BrazeLogger.SUPPRESS)
```
{% endtab %}
{% endtabs %}

## Múltiplas chaves de API

O caso de uso mais comum para várias chaves de API é separar chaves de API para variantes de build de depuração e release.

Para alternar facilmente entre várias chaves de API em suas compilações, recomendamos criar um arquivo `braze.xml` separado para cada [variante de compilação](https://developer.android.com/studio/build/build-variants.html) relevante. Uma variante de compilação é uma combinação de tipo de compilação e sabor do produto. Observe que, por padrão, [um novo projeto Android é configurado com os tipos de compilação `debug` e `release`](http://tools.android.com/tech-docs/new-build-system/user-guide#TOC-Build-Types) e nenhum tipo de produto.

Para cada variante de compilação relevante, crie um novo `braze.xml` para ela em `src/<build variant name>/res/values/`:

```xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
<string name="com_braze_api_key">REPLACE_WITH_YOUR_BUILD_VARIANT_API_KEY</string>
</resources>
```

Quando a variante de compilação for compilada, ela usará o nova chave de API.

Consulte a documentação da [configuração de tempo de execução]({{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/runtime_configuration/) para definir uma chave de API no código.

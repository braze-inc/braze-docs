---
page_order: 1.4
nav_title: Registro Detalhado
article_title: Registro detalhado
description: "Aprenda como ativar o registro detalhado para o SDK da Braze, coletar logs para solução de problemas e compartilhá-los com o suporte da Braze."
---

# Registro detalhado

> O registro detalhado fornece informações detalhadas e de baixo nível do SDK da Braze, permitindo que você veja como o SDK é inicializado, se comunica com os servidores e processa canais de mensagens como push, mensagens no app e Cartões de Conteúdo.

Quando algo não está funcionando como esperado—como uma notificação por push não chegando, uma mensagem no app não sendo exibida ou dados de usuários não sincronizando—os logs detalhados ajudam você a identificar a causa raiz. Em vez de adivinhar, você pode ver exatamente o que o SDK está fazendo em cada etapa.

{% alert tip %}
Se você quiser depurar sem ativar o registro detalhado manualmente, pode usar o [Depurador de SDK]({{site.baseurl}}/developer_guide/sdk_integration/debugging) para criar sessões de depuração diretamente no dashboard da Braze.
{% endalert %}

## Quando usar o registro detalhado

Ative o registro detalhado quando precisar:

- **Verificar a inicialização do SDK**: Confirme se o SDK inicia corretamente com a chave de API e o endpoint corretos.
- **Resolver problemas de entrega de mensagens**: Verifique se os tokens de push estão registrados, se as mensagens no app são acionadas ou se os Cartões de Conteúdo estão sincronizados.
- **Depurar links profundos**: Verifique se o SDK recebe e abre links profundos de push, mensagens no app ou Cartões de Conteúdo.
- **Validar rastreamento de sessões**: Confirme se as sessões começam e terminam como esperado.
- **Diagnosticar problemas de conectividade**: Inspecione as requisições e respostas de rede entre o SDK e os servidores da Braze.

## Ativando o registro detalhado

{% alert important %}
Os logs detalhados são destinados apenas para ambientes de desenvolvimento e teste. Desative o registro detalhado antes de liberar seu app para produção para evitar que informações sensíveis sejam expostas.
{% endalert %}

{% tabs %}
{% tab Android %}

Ative o registro detalhado antes de qualquer outra chamada de SDK no seu `Application.onCreate()` método para capturar a saída mais completa.

**Em código:**

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

**Em `braze.xml`:**

```xml
<integer name="com_braze_logger_initial_log_level">2</integer>
```

Para verificar se o registro detalhado está ativado, procure por `V/Braze` na saída do Logcat. Por exemplo:

```
2077-11-19 16:22:49.591 ? V/Braze v9.0.01 .bo.app.d3: Request started
```

Para detalhes completos, veja [registro do SDK Android]({{site.baseurl}}/developer_guide/sdk_integration#android_enabling-logs).

{% endtab %}
{% tab Swift %}

Defina o nível de registro como `.debug` no seu objeto `Braze.Configuration` durante a inicialização.

{% subtabs %}
{% subtab SWIFT %}
```swift
let configuration = Braze.Configuration(
  apiKey: "<BRAZE_API_KEY>",
  endpoint: "<BRAZE_ENDPOINT>"
)
configuration.logger.level = .debug
let braze = Braze(configuration: configuration)
```
{% endsubtab %}
{% subtab OBJECTIVE-C %}
```objc
BRZConfiguration *configuration = [[BRZConfiguration alloc] initWithApiKey:@"<BRAZE_API_KEY>"
                                                                  endpoint:@"<BRAZE_ENDPOINT>"];
[configuration.logger setLevel:BRZLoggerLevelDebug];
Braze *braze = [[Braze alloc] initWithConfiguration:configuration];
```
{% endsubtab %}
{% endsubtabs %}

O nível `.debug` é o mais detalhado e é recomendado para solução de problemas. Para detalhes completos, veja [registro do SDK Swift]({{site.baseurl}}/developer_guide/sdk_integration#swift_log-levels).

{% endtab %}
{% tab Web %}

Adicione `?brazeLogging=true` como um parâmetro de URL, ou ative o registro durante a inicialização do SDK:

```javascript
braze.initialize('YOUR-API-KEY', {
    baseUrl: 'YOUR-SDK-ENDPOINT',
    enableLogging: true
});
```

Você também pode alternar o registro após a inicialização:

```javascript
braze.toggleLogging();
```

Os registros aparecem na aba **Console** das ferramentas de desenvolvedor do seu navegador. Para detalhes completos, veja [registro do SDK Web]({{site.baseurl}}/developer_guide/sdk_integration#web_logging).

{% endtab %}
{% tab Unity %}

1. Abra Configurações da Braze navegando até **Braze** > **Configuração da Braze**.
2. Selecione o dropdown **Mostrar Configurações do Braze Android**.
3. No campo **Nível de Registro do SDK**, insira `0`.

{% endtab %}
{% tab React Native %}

Defina o nível de registro durante a configuração do SDK:

```javascript
const configuration = new Braze.BrazeConfiguration('YOUR-API-KEY', 'YOUR-SDK-ENDPOINT');
configuration.logLevel = Braze.LogLevel.Verbose;
```

{% endtab %}
{% endtabs %}

## Coletando registros

Depois de ativar o registro detalhado, reproduza o problema que você está solucionando, e então colete os registros do console ou da ferramenta de depuração da sua plataforma.

{% tabs %}
{% tab Android %}

Use **Logcat** no Android Studio para capturar registros:

1. Conecte seu dispositivo ou inicie um emulador.
2. No Android Studio, abra **Logcat** no painel inferior.
3. Filtre por `V/Braze` ou `D/Braze` para isolar a saída do Braze SDK.
4. Reproduza o problema.
5. Copie os registros relevantes e salve-os em um arquivo de texto.

{% endtab %}
{% tab iOS %}

Use o app **Console** no macOS para capturar registros:

1. Instale o app no seu dispositivo com o registro detalhado ativado.
2. Conecte seu dispositivo ao seu Mac.
3. Abra o app **Console** e selecione seu dispositivo na barra lateral **Devices**.
4. Filtre os registros por `Braze` ou `BrazeKit` na barra de pesquisa.
5. Reproduza o problema.
6. Copie os registros relevantes e salve-os em um arquivo de texto.

{% endtab %}
{% tab Web %}

Use as ferramentas de desenvolvedor do seu navegador:

1. Abra as ferramentas de desenvolvedor do seu navegador (geralmente **F12** ou **Cmd+Option+I**).
2. Acesse a guia **Console**.
3. Reproduza o problema.
4. Copie a saída do console e salve-a em um arquivo de texto.

{% endtab %}
{% endtabs %}

{% alert tip %}
Ao coletar registros para o suporte da Braze, comece a registrar antes de iniciar seu app e continue até bem depois que o problema ocorrer. Isso ajuda a capturar toda a sequência de eventos.
{% endalert %}

## Lendo registros detalhados

Registros detalhados seguem uma estrutura consistente que ajuda você a rastrear o que o SDK está fazendo. Para aprender a interpretar a saída de registros para canais específicos, incluindo quais entradas-chave procurar e padrões comuns de solução de problemas, veja [Reading verbose logs]({{site.baseurl}}/developer_guide/sdk_integration/reading_verbose_logs).

## Compartilhando registros com o suporte da Braze

Quando você contatar o suporte da Braze com um problema de SDK, inclua o seguinte:

1. **Arquivo de log detalhado**: Uma captura completa do log desde o lançamento do app até a ocorrência do problema.
2. **Passos para reproduzir**: Uma descrição clara das ações que disparam o problema.
3. **Comportamento esperado vs. real**: O que você esperava que acontecesse e o que aconteceu de fato.
4. **Versão do SDK**: A versão do SDK do Braze que você está usando.
5. **Plataforma e versão do SO**: Por exemplo, iOS 18.0, Android 14 ou Chrome 120.
---
nav_title: Solução de problemas de deep linking
article_title: Solução de problemas de deep linking
description: "Problemas comuns de deep linking no iOS e como diagnosticá-los, incluindo links de esquema personalizado, links universais, links de e-mail e provedores de terceiros como o Branch."
page_order: 1.2
channel:
  - push notifications
  - in-app messages
  - content cards
  - email
---

# Solução de problemas de deep linking

> Esta página cobre problemas comuns de deep linking no iOS e como diagnosticá-los. Para ajuda na escolha do tipo de link certo, veja [guia de deep linking para iOS]({{site.baseurl}}/developer_guide/push_notifications/ios_deep_linking_guide). Para detalhes de implementação, veja [Deep linking]({{site.baseurl}}/developer_guide/push_notifications/deep_linking/?sdktab=swift).

## O deep link de esquema personalizado não abre a visualização correta

Se um deep link de esquema personalizado (por exemplo, `myapp://products/123`) abrir seu app, mas não navegar para a tela pretendida:

1. **Verifique se o esquema está registrado.** No Xcode, verifique se seu esquema está listado em `CFBundleURLTypes` em `Info.plist`.
2. **Verifique seu manipulador.** Defina um ponto de interrupção em `application(_:open:options:)` para confirmar se está sendo chamado e inspecione o parâmetro `url`.
3. **Teste o link de forma independente.** Execute o seguinte comando no Terminal para testar o deep link fora do Braze:
   ```bash
   xcrun simctl openurl booted "myapp://products/123"
   ```
   Se o link não funcionar aqui, o problema está no manuseio de URL do seu app—não no Braze.
4. **Verifique o formato da URL.** Verifique se a URL na sua campanha corresponde ao que seu manipulador espera. Erros comuns incluem componentes de caminho ausentes ou caixa de texto incorreta.

## O link universal abre no Safari em vez do app

Se um link universal (por exemplo, `https://myapp.com/products/123`) abrir no Safari em vez do seu app:

### Verifique a permissão de Domínios Associados

No Xcode, acesse seu alvo de app > **Assinatura & Capacidades** e verifique se `applinks:yourdomain.com` está listado sob **Domínios Associados**.

### Valide o arquivo AASA

Seu arquivo de Associação de Site de App da Apple (AASA) deve estar hospedado em um destes locais:

- `https://yourdomain.com/.well-known/apple-app-site-association`
- `https://yourdomain.com/apple-app-site-association`

Verifique o seguinte:

- O arquivo é servido via HTTPS com um certificado válido.
- O `Content-Type` é `application/json`.
- O tamanho do arquivo é inferior a 128 KB.
- O `appID` corresponde ao seu ID de Equipe e ID de Pacote (por exemplo, `ABCDE12345.com.example.myapp`).
- O array `paths` ou `components` inclui os padrões de URL que você espera.

Você pode validar seu AASA usando [ferramenta de validação de busca da Apple](https://search.developer.apple.com/appsearch-validation-tool/) ou executando:

```bash
swcutil dl -d yourdomain.com
```

### Verifique o `AppDelegate`

Verifique se `application(_:continue:restorationHandler:)` está implementado em seu `AppDelegate` e lida com o `NSUserActivity` corretamente:

```swift
func application(_ application: UIApplication,
                 continue userActivity: NSUserActivity,
                 restorationHandler: @escaping ([UIUserActivityRestoring]?) -> Void) -> Bool {
  guard userActivity.activityType == NSUserActivityTypeBrowsingWeb,
        let url = userActivity.webpageURL else {
    return false
  }
  // Handle the URL
  return true
}
```

### Verifique a configuração do SDK do Braze

Se você estiver usando links universais de notificações push entregues pelo Braze, mensagens no app ou Cartões de Conteúdo, confirme se `forwardUniversalLinks` está habilitado:

```swift
let configuration = Braze.Configuration(apiKey: "<BRAZE_API_KEY>", endpoint: "<BRAZE_ENDPOINT>")
configuration.forwardUniversalLinks = true
```

{% alert note %}
O encaminhamento de links universais requer acesso aos direitos do aplicativo. Ao executar em um simulador, essas permissões não estão disponíveis diretamente. Para testar em um simulador, adicione o arquivo `.entitlements` à fase de construção **Copiar Recursos do Pacote**.
{% endalert %}

### Verifique o problema de pressionar longo

Se você pressionar longo um link universal e selecionar **Abrir**, o iOS pode "quebrar" a associação do link universal para aquele domínio. Este é um comportamento conhecido do iOS. Para redefini-lo, pressione longo o link novamente e selecione **Abrir em [Nome do App]**.

## O deep link do e-mail não abre o app

Os links de e-mail passam pelo sistema de rastreamento de cliques do seu ESP, que envolve links em um domínio de rastreamento (por exemplo, `https://click.yourdomain.com/...`). Para que os links universais funcionem a partir do e-mail, você deve configurar o arquivo AASA no seu domínio de rastreamento de cliques — não apenas no seu domínio principal.

### Verifique o AASA do domínio de rastreamento de cliques

1. Identifique seu domínio de rastreamento de cliques nas configurações do seu ESP (SendGrid, SparkPost ou Amazon SES).
2. Hospede o arquivo AASA em `https://your-click-tracking-domain/.well-known/apple-app-site-association`.
3. Certifique-se de que o arquivo AASA no domínio de rastreamento de cliques inclua o mesmo `appID` e padrões de caminho válidos.

Para instruções de configuração específicas do ESP, veja [Links universais e Links de App]({{site.baseurl}}/user_guide/message_building_by_channel/email/universal_links/).

### Verifique a cadeia de redirecionamento

Alguns ESPs realizam um redirecionamento da URL de rastreamento de cliques para sua URL final. Links universais só funcionam se o iOS reconhecer o domínio *inicial* (o domínio de rastreamento de cliques) como associado ao seu app. Se o redirecionamento contornar a verificação do AASA, o link será aberto no Safari.

Para testar:

1. Envie um e-mail de teste para você mesmo.
2. Pressione longamente o link e inspecione a URL — esta é a URL de rastreamento de cliques.
3. Verifique se este domínio possui um arquivo AASA válido.

## O deep link funciona a partir de push, mas não a partir de mensagens no app (ou vice-versa)

### Verifique o BrazeDelegate

Se você implementar `BrazeDelegate.braze(_:shouldOpenURL:)`, verifique se ele lida com links de forma consistente entre os canais. O parâmetro `context` inclui o canal de origem. Procure lógica condicional que pode filtrar acidentalmente links de canais específicos.

### Ativar o registro detalhado

[Ative o registro detalhado]({{site.baseurl}}/developer_guide/verbose_logging) e reproduza o problema. Procure a entrada de `Opening` no registro:

```
Opening '<URL>':
- channel: <SOURCE_CHANNEL>
- useWebView: <true/false>
- isUniversalLink: <true/false>
```

Compare a saída do registro para o canal funcionando vs. o canal não funcionando. Diferenças em `useWebView` ou `isUniversalLink` indicam como o SDK está interpretando o link de forma diferente.

### Verifique se há delegados de exibição personalizados

Se você usar um delegado de exibição de mensagem no app ou manipulador de clique de Cartão de Conteúdo personalizado, verifique se ele passa corretamente os eventos de link para o SDK Braze para tratamento.

## "Abrir URL da Web Dentro do App" mostra uma página em branco ou quebrada

Se selecionar **Abrir URL da Web Dentro do App** resultar em uma WebView em branco ou quebrada:

1. **Verifique se a URL usa HTTPS.** A WebView do SDK requer URLs compatíveis com ATS. Links HTTP falham silenciosamente.
2. **Verifique os cabeçalhos de Política de Segurança de Conteúdo.** Se a página da web de destino definir `X-Frame-Options: DENY` ou um `Content-Security-Policy` restritivo, isso bloqueia a renderização em uma WebView.
3. **Verifique se há redirecionamentos para esquemas personalizados.** Se a página da web redirecionar para um esquema personalizado (por exemplo, `myapp://`), a WebView não consegue lidar com isso.
4. **Teste a URL no Safari.** Se a página não carregar no Safari no dispositivo, ela também não carregará na WebView.

## Solução de problemas do Branch com Braze {#branch}

Se você usar [Branch]({{site.baseurl}}/partners/message_orchestration/deeplinking/branch_for_deeplinking/) como seu provedor de links:

### Verifique as rotas do BrazeDelegate para o Branch

Seu `BrazeDelegate` deve interceptar links do Branch e passá-los para o SDK do Branch. Verifique o seguinte:

```swift
func braze(_ braze: Braze, shouldOpenURL context: Braze.URLContext) -> Bool {
  if let host = context.url.host, host.contains("app.link") {
    // Route to Branch SDK
    Branch.getInstance.handleDeepLink(context.url)
    return false
  }
  // Let Braze handle other links
  return true
}
```

Se `shouldOpenURL` retornar `true` para links do Branch, o Braze os manipula diretamente em vez de encaminhá-los para o Branch.

### Verifique o domínio do link do Branch

Verifique se o domínio do Branch em seu `BrazeDelegate` corresponde ao seu domínio real do link do Branch. O Branch usa vários formatos de domínio:

- `yourapp.app.link` (padrão)
- `yourapp-alternate.app.link` (alternativo)
- Domínios personalizados (se configurados no painel do Branch)

### Ative o registro de ambos os SDKs

Para diagnosticar onde o link quebra na cadeia:

1. Ative [Braze registro detalhado]({{site.baseurl}}/developer_guide/verbose_logging) — procure entradas `Opening '<URL>':` para verificar se o SDK recebeu o link.
2. Ative [modo de teste do Branch](https://help.branch.io/developers-hub/docs/ios-basic-integration#test-deep-linking) — verifique o painel do Branch para eventos de clique em links.
1. Ative [Braze registro detalhado]({{site.baseurl}}/developer_guide/verbose_logging). Procure entradas `Opening '<URL>':` para verificar se o SDK recebeu o link.
2. Ative [modo de teste do Branch](https://help.branch.io/developers-hub/docs/ios-basic-integration#test-deep-linking). Verifique o painel do Branch para eventos de clique em links.
3. Se o Braze registrar o link, mas o Branch não ver um clique, a lógica de roteamento `BrazeDelegate` é provavelmente o problema.

### Verifique a configuração do painel do Branch

No painel do Branch, verifique:

- O **Bundle ID** e o **Team ID** do seu app correspondem ao seu projeto Xcode.
- Seus **Associated Domains** incluem o domínio do link do Branch.
- Seu arquivo AASA do Branch é válido (o Branch hospeda isso automaticamente em `app.link` domínios).

### Teste os links do Branch de forma independente

Teste o link do Branch fora do Braze para isolar o problema:

1. Abra o link do Branch no Safari no seu dispositivo. Se não abrir o app, o problema está na sua configuração do Branch ou AASA — não no Braze.
2. Cole o link do Branch no app Notas e toque nele. Links universais funcionam de forma mais confiável a partir do Notas do que da barra de endereços do Safari.

## Dicas gerais de depuração

### Use registro detalhado

[Ativar registro detalhado]({{site.baseurl}}/developer_guide/verbose_logging) para ver exatamente como o SDK processa os links. Entradas-chave a serem observadas:

| Entrada de registro | O que isso significa |
|---|---|
| `Opening '<URL>': - channel: notification` | SDK está processando um link de uma notificação por push |
| `Opening '<URL>': - channel: inAppMessage` | SDK está processando um link de uma mensagem no app |
| `Opening '<URL>': - channel: contentCard` | SDK está processando um link de um cartão de conteúdo |
| `useWebView: true` | SDK abre a URL na WebView do app |
| `isUniversalLink: true` | SDK identificou a URL como um link universal |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Para mais detalhes sobre como ler esses registros, veja [Lendo registros detalhados]({{site.baseurl}}/developer_guide/verbose_logging).

### Teste links em isolamento

Antes de testar pelo Braze, verifique se seu deep link ou link universal funciona por conta própria:

- **Esquema personalizado**: Execute `xcrun simctl openurl booted "myapp://path"` no Terminal.
- **Link universal**: Cole a URL no aplicativo Notas em um dispositivo físico e toque nela. Não teste a partir da barra de endereços do Safari, pois o iOS trata URLs digitadas de forma diferente de links tocados.
- **Link Branch**: Abra o link Branch a partir do aplicativo Notas em um dispositivo.

### Teste em um dispositivo físico

Links universais têm suporte limitado no simulador iOS. Sempre teste em um dispositivo físico para resultados precisos. Se você precisar testar em um simulador, adicione o arquivo `.entitlements` à fase de construção **Copiar Recursos do Pacote**.
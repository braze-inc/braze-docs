---
page_order: 1.1
nav_title: Guia de deep linking para iOS
article_title: Guia de deep linking para iOS
description: "Saiba que tipo de deep link usar para seu aplicativo iOS, quando você precisa de um arquivo AASA e quais métodos de delegado de app implementar."
channel:
  - push notifications
  - in-app messages
  - content cards
  - email
---

# Guia de deep linking para iOS

> Este guia ajuda você a escolher a estratégia de deep linking certa para seu app iOS, dependendo do canal de envio de mensagens que você está usando e se você usa um provedor de links terceirizado, como o Branch.

Para obter detalhes sobre a implementação, consulte [deep linking]({{site.baseurl}}/developer_guide/push_notifications/deep_linking/?sdktab=swift). Para solucionar problemas, consulte [Solução de problemas de deep linking]({{site.baseurl}}/developer_guide/push_notifications/deep_linking_troubleshooting).

## Escolhendo um tipo de link

Existem três maneiras de lidar com links de mensagens Braze em seu app iOS. Cada um funciona de maneira diferente e é adequado para diferentes canais e casos de uso.

| Tipo de ligação | Exemplo | Ideal para | Abre sem o app instalado? |
|---|---|---|---|
| **Esquema personalizado** | `myapp://products/123` | Notificações push, mensagens no app, cartões de conteúdo | Não — o link não funciona |
| **Link universal** | `https://myapp.com/products/123` | E-mail, SMS, canais com rastreamento de cliques | Sim — volta para a web |
| **Abrir URL no app** | Qualquer`https://`URL | Exibindo conteúdo da web em um WebView modal | N/A — exibe no WebView |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

### Deep links com esquema personalizado

Deep links personalizados (por exemplo, `myapp://products/123`) abrem seu app diretamente em uma tela específica. São a opção mais simples para canais em que os links não são modificados por terceiros.

**Use deep links com esquema personalizado quando:**
- Envio de notificações por push, mensagens no app ou cartões de conteúdo
- Você não precisa do link para funcionar se o app não estiver instalado.
- Você não precisa de rastreamento de cliques (envoltório de link ESP de e-mail)

**Não utilize deep links com esquema personalizado quando:**
- Envio de e-mails — os ESPs envolvem links para rastreamento de cliques, o que quebra esquemas personalizados
- Você precisa do link para voltar a uma página da web se o app não estiver instalado.

### Links universais

Links universais (por exemplo, `https://myapp.com/products/123`) são URLs HTTPS padrão que o iOS pode encaminhar para o seu app em vez de abrir em um navegador. Eles exigem configuração no lado do servidor (um arquivo AASA) e configuração no lado do app (direito de domínios associados).

**Use links universais quando:**
- Envio de e-mails. Seu ESP envolve links para rastreamento de cliques, portanto, os links devem ser HTTPS.
- Envio de SMS ou outros canais onde os links são encurtados ou encapsulados.
- Você precisa do link para voltar a uma página da web quando o app não estiver instalado.
- Você está usando um provedor de links de terceiros, como Branch ou Appsflyer.

**Não utilize links universais quando:**
- Você só precisa de deep links de push, mensagens no app ou cartões de conteúdo. Os esquemas personalizados são mais simples.

### “Abrir URL da Web dentro do app”

Esta opção abre uma página da Web dentro de um WebView modal no seu app. É totalmente gerenciado pelo SDK Braze usando`Braze.WebViewController`— você não precisa escrever nenhum código de gerenciamento de URL.

**Use “Abrir URL da Web dentro do app” quando:**
- Você deseja exibir uma página da web (como uma promoção ou artigo) sem sair do seu app.
- A URL é uma página web HTTPS padrão, não um deep link para uma tela específica do app.

**Não utilize “Abrir URL da Web dentro do app” quando:**
- Você precisa navegar para uma visualização específica em seu app. Em vez disso, use um esquema personalizado ou um link universal.
- A página da Web requer autenticação ou possui cabeçalhos de Política de Segurança de Conteúdo que bloqueiam a incorporação.

## O que você precisa para cada tipo de link

### Deep links com esquema personalizado

| Requisito | Informações |
|---|---|
| Arquivo AASA | Não é necessário |
| `Info.plist` | Registre seu plano em`CFBundleURLTypes`  e adicione-o a `LSApplicationQueriesSchemes` |
| Método delegado do app | Implementar`application(_:open:options:)`para analisar a URL e navegar |
| Configuração do SDK Braze | Nenhum — o SDK abre URLs de esquema personalizado por padrão |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Links universais

| Requisito | Informações |
|---|---|
| Arquivo AASA | Obrigatório — host em `https://yourdomain.com/.well-known/apple-app-site-association` |
| Domínios associados | Adicione`applinks:yourdomain.com`no Xcode em **Recursos de &assinatura** |
| Método delegado do app | Implementar`application(_:continue:restorationHandler:)`para lidar com `NSUserActivity` |
| Configuração do SDK Braze | Definir `configuration.forwardUniversalLinks = true` |
| BrazeDelegate (opcional) | Implementar`braze(_:shouldOpenURL:)`para roteamento personalizado (por exemplo, Branch) |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert important %}
Se você enviar e-mails através do Braze, seu ESP (SendGrid, SparkPost ou Amazon SES) envolverá os links em um domínio de rastreamento de cliques. Você também deve hospedar o arquivo AASA em seu domínio de rastreamento de cliques, não apenas em seu domínio principal. Para uma configuração completa, consulte [Links universais e Links de apps]({{site.baseurl}}/user_guide/message_building_by_channel/email/universal_links/).
{% endalert %}

### “Abrir URL da Web dentro do app”

| Requisito | Informações |
|---|---|
| Arquivo AASA | Não é necessário |
| Método delegado do app | Não é necessário — o SDK lida com isso automaticamente |
| Configuração do SDK Braze | Nenhum — selecione **Abrir URL da Web dentro do app** no criador da campanha |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Quando você precisa de um arquivo AASA {#when-aasa}

Um arquivo Apple App Site Association (AASA) só é necessário quando você usa **links universais**. Ele informa ao iOS quais URLs seu app pode processar.

Você precisa de um arquivo AASA quando:

- Você envia deep links em campanhas de e-mail (porque os ESPs envolvem os links em URLs de rastreamento de cliques HTTPS).
- Você envia deep links em campanhas por SMS (porque os links podem ser encurtados para URLs HTTPS).
- Você usa o Branch, o Appsflyer ou outro provedor de links (porque eles usam seus próprios domínios HTTPS).
- Você usa links universais de push, mensagens no app ou cartões de conteúdo (menos comum, mas possível com `forwardUniversalLinks = true`).

Você não precisa de um arquivo AASA quando:

- Você só usa deep links com esquema personalizado (por exemplo, `myapp://`) de push, mensagens no app ou cartões de conteúdo.
- Utilize a opção **Abrir URL da Web dentro do app**.

Para obter instruções de configuração da AASA, consulte [Links universais e Links de apps]({{site.baseurl}}/user_guide/message_building_by_channel/email/universal_links/#setting-up-universal-links-and-app-links).

## Quando você precisa de código de app para lidar com links {#when-app-code}

O método delegado que você implementa depende do tipo de link que está usando:

| Método delegado | Alças | Quando implementar |
|---|---|---|
| `application(_:open:options:)` | Deep links de esquema personalizado (`myapp://`) | Você usa deep links com esquema personalizado de qualquer canal |
| `application(_:continue:restorationHandler:)` | Links universais (`https://`) | Você usa links universais de e-mail, SMS ou com `forwardUniversalLinks = true` |
| `BrazeDelegate.braze(_:shouldOpenURL:)` | Todos os URLs abertos pelo SDK | Você precisa de uma lógica de roteamento personalizada (por exemplo, ramificação, tratamento condicional, análise de dados). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% alert tip %}
Se você usar um provedor de links de terceiros, como o Branch, implemente`BrazeDelegate.braze(_:shouldOpenURL:)`  para interceptar URLs e encaminhá-los para o SDK do provedor. Consulte [Branch para deep linking]({{site.baseurl}}/partners/message_orchestration/deeplinking/branch_for_deeplinking/) para um exemplo completo.
{% endalert %}

## Usando o Branch com o Braze {#branch}

Se você usar [o Branch]({{site.baseurl}}/partners/message_orchestration/deeplinking/branch_for_deeplinking/) como seu provedor de links, sua configuração exigirá algumas etapas adicionais além da configuração padrão de link universal:

1. **SDK da filial**: Integre o SDK do Branch seguindo [a documentação do Branch](https://help.branch.io/developers-hub/docs/native-sdks-overview).
2. **Domínios associados**: Adicione seu domínio Branch (por exemplo, `applinks:yourapp.app.link`) no Xcode em **Recursos de &assinatura**.
3. **BrazeDelegate**: Implemente`braze(_:shouldOpenURL:)`para encaminhar os links do Branch para o SDK do Branch, em vez de permitir que o Braze os processe diretamente.
4. **Encaminhe links universais**: Defina`configuration.forwardUniversalLinks = true`na sua configuração do SDK Braze.

Para obter detalhes sobre a implementação e orientações sobre depuração, consulte [Branch para deep linking]({{site.baseurl}}/partners/message_orchestration/deeplinking/branch_for_deeplinking/).
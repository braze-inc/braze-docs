---
nav_title: Extensões do navegador
article_title: Integração de extensões de navegador para a Web
platform: Web
page_order: 20
page_type: reference
description: "Este artigo descreve como usar o Braze Web SDK em suas extensões de navegador (Google Chrome, Firefox)."

---

# Extensão do navegador

> Este artigo descreve como usar o Braze Web SDK em suas extensões de navegador (Google Chrome, Firefox).

Integre o Braze Web SDK em sua extensão de navegador para coletar análises de dados e exibir mensagens personalizadas para os usuários. Isso inclui **as extensões do Google Chrome** e **os complementos do Firefox**.

## O que é suportado

Em geral, como as extensões são HTML e JavaScript, você pode usar a Braze para o seguinte:

* **Análise de dados**: Capture eventos personalizados, atributos e até mesmo identifique usuários recorrentes com a sua extensão. Use essas características de perfil para potencializar o envio de mensagens entre canais.
* **Mensagens no app**: Dispare mensagens no app quando os usuários realizarem uma ação em sua extensão, usando nosso envio de mensagens HTML nativo ou personalizado.
* **Cartões de conteúdo**: Adicione um feed de cartões nativos à sua extensão para integração ou conteúdo promocional.
* **Web push**: Envie notificações oportunas mesmo quando sua página da Web não estiver aberta no momento.

## O que não é suportado

* Os trabalhadores de serviço não são suportados pelo Braze Web SDK, no entanto, isso está no planejamento para consideração futura.

## Tipos de extensão

O Braze pode ser incluído nas seguintes áreas de sua extensão:

| Área | Informações | O que é suportado |
|--------|-------|------|
| Página pop-up | A página [Popup](https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/user_interface/Popups) é uma caixa de diálogo que pode ser mostrada aos usuários quando eles clicam no ícone da sua extensão na barra de ferramentas do navegador.| Análise de dados, mensagens no app e cartões de conteúdo |
| Scripts em segundo plano | [Scripts em segundo plano](https://developer.chrome.com/extensions/background_pages) (somente Manifesto v2) permitem que sua extensão inspecione e interaja com a navegação do usuário ou modifique páginas da Web (por exemplo, como os bloqueadores de anúncios detectam e alteram o conteúdo das páginas). | Análise de dados, mensagens no app e cartões de conteúdo.<br><br>Os scripts em segundo plano não são visíveis para os usuários, portanto, para o envio de mensagens, seria necessário comunicar-se com as guias do navegador ou com a página pop-up ao exibir mensagens. |
| Páginas de opções | A [página Options](https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/user_interface/Options_pages) permite que os usuários alternem as configurações na extensão. É uma página HTML autônoma que abre uma nova guia. | Análise de dados, mensagens no app e cartões de conteúdo |
{: .reset-td-br-1 .reset-td-br-2, .reset-td-br-3 role="presentation" }

## Permissões

O `manifest.json` não requer permissões adicionais como um arquivo de localização empacotado com sua extensão ao integrar o SDK da Braze (`braze.min.js`). 

No entanto, se você usar [Google Tag Manager]({{ site.baseurl }}/developer_guide/platform_integration_guides/web/google_tag_manager/), ou referenciar o SDK do Braze a partir de uma URL externa, ou tiver definido uma Política de Segurança de Conteúdo rigorosa para sua extensão, você precisará ajustar a configuração [`content_security_policy`](https://developer.chrome.com/extensions/contentSecurityPolicy) em seu `manifest.json` para permitir fontes de script remotas.

## Primeiros passos

{% alert tip %}
Antes de começar, leia o [guia de configuração inicial do Web SDK]({{site.baseurl}}/developer_guide/platform_integration_guides/web/initial_sdk_setup/) para saber mais sobre a integração de JavaScript em geral.  <br><br>Pode ser interessante marcar a [referência do JavaScript SDK](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html) para obter detalhes completos sobre todos os diferentes métodos e opções de configuração do SDK.
{% endalert %}

Para integrar o Web SDK da Braze, primeiro você precisará baixar uma cópia da biblioteca JavaScript mais recente. Isso pode ser feito usando o NPM ou baixando-o diretamente do [CDN da Braze](https://js.appboycdn.com/web-sdk/latest/braze.min.js).

Alternativamente, se você preferir usar [Google Tag Manager]({{ site.baseurl }}/developer_guide/platform_integration_guides/web/google_tag_manager/) ou usar uma cópia do SDK Braze hospedada externamente, tenha em mente que carregar recursos externos exigirá que você ajuste sua configuração [`content_security_policy`](https://developer.chrome.com/extensions/contentSecurityPolicy) em seu `manifest.json`.

Depois de baixar, copie o arquivo `braze.min.js` em algum lugar do diretório de sua extensão.

### Popups de extensão {#popup}

Para adicionar a Braze a uma extensão pop-up, faça referência ao arquivo JavaScript local em seu site `popup.html`, como faria em um site normal. Se você estiver usando o Google Tag Manager, pode adicionar Braze usando nossos [modelos do Google Tag Manager]({{ site.baseurl }}/developer_guide/platform_integration_guides/web/google_tag_manager/).

```html
<html>
    <title>popup.html</title>
    <!-- Add the Braze library -->
    <script src="/relative/path/to/braze.min.js"></script>
    <script>
    // Initialize Braze here
    </script>
</html>
```

### Script em segundo plano (somente Manifesto v2) {#background-script}

Para usar a Braze no script em segundo plano de sua extensão, adicione a biblioteca Braze ao `manifest.json` no vetor `background.scripts`. Isso tornará a variável global `braze` disponível em seu contexto de script em segundo plano.


```json
{
    "manifest_version": 2,
    "background": {
        "scripts": [
            "relative/path/to/braze.min.js",
            "background.js"
        ],
    }
}
```

### Página de opções {#options-page}

Se você usar uma página de opções (por meio das propriedades do manifesto `options` ou `options_ui` ), poderá incluir o Braze da mesma forma que faria nas [instruções do`popup.html` ](#popup).

## Inicialização

Depois que o SDK for incluído, você poderá inicializar a biblioteca como de costume. 

Como não há suporte para cookies em extensões de navegador, você pode desativar os cookies, configurando no inicialização como `noCookies: true`.

```javascript
braze.initialize("YOUR-API-KEY-HERE", {
    baseUrl: "YOUR-API-ENDPOINT",
    enableLogging: true,
    noCookies: true
});
```

Para saber mais sobre nossas opções de inicialização suportadas, visite a [referência do Web SDK](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initialize).

## Push

As caixas de diálogo pop-up de extensão não permitem push prompts (elas não têm a barra de URL na navegação). Então, para registrar e solicitar permissão de push dentro do diálogo Popup de uma extensão, você terá que usar uma solução alternativa de domínio, conforme descrito em [Domínio de push alternativo]({{ site.baseurl }}/developer_guide/platform_integration_guides/web/push_notifications/alternate_push_domain).


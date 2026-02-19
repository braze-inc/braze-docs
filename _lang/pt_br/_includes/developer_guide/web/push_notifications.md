{% multi_lang_include archive/web-v4-rename.md %}

{% multi_lang_include developer_guide/prerequisites/web.md %}

## Protocolos push

As notificações por push da Web são implementadas usando o [padrão push do W3C](http://www.w3.org/TR/push-api/), que é suportado pela maioria dos principais navegadores. Para saber mais sobre padrões específicos de protocolo push e suporte a navegadores, consulte os recursos da [Apple](https://developer.apple.com/notifications/safari-push-notifications/) [, Mozilla](https://developer.mozilla.org/en-us/docs/web/api/push_api#browser_compatibility) e [Microsoft](https://developer.microsoft.com/en-us/microsoft-edge/status/pushapi/).

## Configuração de notificações por push

### Etapa 1: Configure seu service worker

No arquivo `service-worker.js` de seu projeto, adicione o seguinte trecho e defina a opção de [`manageServiceWorkerExternally`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initialize) para `true` ao inicializar o Web SDK.

<script src="{{site.baseurl}}/assets/js/embed.js?target=https://github.com/braze-inc/braze-web-sdk/blob/master/sample-builds/cdn/service-worker.js&style=github&showBorder=on&showLineNumbers=on&showFileMeta=on&showCopy=on"></script>

{% alert important %}
Seu servidor da Web deve retornar um `Content-Type: application/javascript` ao servir seu arquivo de service worker. Além disso, se o arquivo do service worker não tiver o nome `service-worker.js`, você precisará usar a [opção de inicialização](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initializationoptions) `serviceWorkerLocation`.
{% endalert %}

### Etapa 2: Registre o navegador

Para solicitar imediatamente permissões por push de um usuário para que seu navegador possa receber notificações por push, ligue para `braze.requestPushPermission()`. Para testar primeiro se o push é compatível com o navegador, ligue para `braze.isPushSupported()`.

Também é possível [enviar um prompt de soft push]({{site.baseurl}}/developer_guide/push_notifications/soft_push_prompts/?sdktab=web) para o usuário antes de solicitar permissão de push para mostrar sua própria interface de usuário relacionada a push.

{% alert important %}
No MacOS, tanto **o Google Chrome** quanto **o Google Chrome Helper (Alertas)** devem ser ativados pelo usuário final em **Configurações do sistema > Notificações** antes que as notificações por push possam ser exibidas - mesmo que as permissões sejam concedidas.
{% endalert %}

### Etapa 3: Desativar `skipWaiting` (opcional)

O arquivo de serviço do Braze chamará automaticamente o endereço `skipWaiting` após a instalação. Se quiser desativar essa funcionalidade, adicione o seguinte código ao seu arquivo de service worker, depois de importar o Braze:

<script src="{{site.baseurl}}/assets/js/embed.js?target=https%3A%2F%2Fgithub.com%2Fbraze-inc%2Fbraze-web-sdk%2Fblob%2Fmaster%2Fsnippets%2Fservice-worker-skip-waiting.js&style=github&showBorder=on&showLineNumbers=on&showFileMeta=on&showCopy=on"></script>

## Cancelamento da inscrição de um usuário

Para cancelar a inscrição de um usuário, ligue para `braze.unregisterPush()`.

{% alert important %}
As versões recentes do Safari e do Firefox exigem que você chame esse método a partir de um manipulador de eventos de curta duração (como um manipulador de clique de botão ou um prompt soft push). Isso está de acordo com as [práticas recomendadas de experiência do usuário do Chrome](https://docs.google.com/document/d/1WNPIS_2F0eyDm5SS2E6LZ_75tk6XtBSnR1xNjWJ_DPE) para registro push.
{% endalert %}

## Domínios alternativos

Para integrar o web push, seu domínio deve ser [seguro](https://w3c.github.io/webappsec-secure-contexts/), o que geralmente significa `https`, `localhost` e outras exceções, conforme definido no [padrão push do W3C](https://www.w3.org/TR/service-workers/#security-considerations). Você também precisará ser capaz de registrar um Service Worker na raiz do seu domínio ou, pelo menos, controlar os cabeçalhos HTTP desse arquivo. Este artigo aborda como integrar os web pushes da Braze em um domínio alternativo.

### Casos de uso

Se não for possível atender a todos os critérios descritos no [padrão push do W3C](https://www.w3.org/TR/service-workers/#security-considerations), você poderá usar esse método para adicionar uma caixa de diálogo de prompt push ao seu site. Isso pode ser útil se você quiser permitir que os usuários façam o pedido de aceitação em um site `http` ou em um pop-up de extensão do navegador que esteja impedindo a exibição do seu pedido de push.

### Considerações

Lembre-se de que, como muitas soluções alternativas na Web, os navegadores evoluem continuamente, e esse método pode não ser viável no futuro. Antes de continuar, certifique-se de que:

- Você possui um domínio seguro separado (`https://`) e permissões para registrar um Service Worker nesse domínio.
- Os usuários são registrados no seu site, o que garante que os tokens por push correspondam ao perfil correto.

{% alert important %}
Você não pode usar esse método para implementar notificações por push para a Shopify. A Shopify removerá automaticamente os cabeçalhos necessários para entregar o push dessa forma.
{% endalert %}

### Configuração de um domínio push alternativo

Para deixar claro o exemplo a seguir, usaremos `http://insecure.com` e `https://secure.com` como nossos dois domínios, com o objetivo de fazer com que os visitantes se registrem para push em `http://insecure.com`. Esse exemplo também poderia ser aplicado a um esquema `chrome-extension://` para a página pop-up de uma extensão de navegador.

#### Etapa 1: Iniciar o fluxo de solicitação

Em `insecure.com`, abra uma nova janela para o seu domínio seguro usando um parâmetro de URL para passar o ID externo Braze do usuário atualmente registrado.

**http://insecure.com**
```html
<button id="opt-in">Opt-In For Push</button>
<script>
// the same ID you would use with `braze.changeUser`:
const user_id = getUserIdSomehow();
// pass the user ID into the secure domain URL:
const secure_url = `https://secure.com/push-registration.html?external_id=${user_id}`;

// when the user takes some action, open the secure URL in a new window
document.getElementById("opt-in").onclick = function(){
    if (!window.open(secure_url, 'Opt-In to Push', 'height=500,width=600,left=150,top=150')) {
        window.alert('The popup was blocked by your browser');
    } else {
        // user is shown a popup window
        // and you can now prompt for push in this window
    }
}
</script>
```

#### Etapa 2: Registro para push

No momento, o site `secure.com` abrirá uma janela pop-up na qual você poderá inicializar o Braze Web SDK para o mesmo ID de usuário e solicitar a permissão do usuário para o web push.

**https://secure.com/push-registration.html**

<script src="{{site.baseurl}}/assets/js/embed.js?target=https%3A%2F%2Fgithub.com%2Fbraze-inc%2Fbraze-web-sdk%2Fblob%2Fmaster%2Fsnippets%2Falternate-push-domain-registration.html&style=github&showBorder=on&showLineNumbers=on&showFileMeta=on&showCopy=on"></script>

#### Etapa 3: Comunicação entre domínios (opcional)

Agora que os usuários podem fazer a aceitação a partir desse fluxo de trabalho originado em `insecure.com`, convém modificar seu site com base no fato de o usuário já ter feito a aceitação ou não. Não faz sentido pedir ao usuário que se registre no push se ele já estiver registrado.

Você pode usar iFrames e a API [`postMessage`](https://developer.mozilla.org/en-US/docs/Web/API/Window/postMessage) para se comunicar entre seus dois domínios. 

**insecure.com**

Em nosso domínio `insecure.com`, solicitaremos ao domínio seguro (onde o push está _realmente_ registrado) informações sobre o registro push do usuário atual:

```html
<!-- Create an iframe to the secure domain and run getPushStatus onload-->
<iframe id="push-status" src="https://secure.com/push-status.html" onload="getPushStatus()" style="display:none;"></iframe>

<script>
function getPushStatus(event){
    // send a message to the iframe asking for push status
    event.target.contentWindow.postMessage({type: 'get_push_status'}, 'https://secure.com');
    // listen for a response from the iframe's domain
    window.addEventListener("message", (event) => {
        if (event.origin === "http://insecure.com" && event.data.type === 'set_push_status') {
            // update the page based on the push permission we're told
            window.alert(`Is user registered for push? ${event.data.isPushPermissionGranted}`);
        }
    }   
}
</script>
```

**secure.com/push-status.html**

<script src="{{site.baseurl}}/assets/js/embed.js?target=https%3A%2F%2Fgithub.com%2Fbraze-inc%2Fbraze-web-sdk%2Fblob%2Fmaster%2Fsnippets%2Falternate-push-domain-status.html&style=github&showBorder=on&showLineNumbers=on&showFileMeta=on&showCopy=on"></script>

## Perguntas frequentes (FAQ)

### Trabalhadores de serviços

#### E se eu não conseguir registrar um service worker no diretório raiz?

Por padrão, um service worker só pode ser usado no mesmo diretório em que está registrado. Por exemplo, se o seu arquivo de service worker existir em `/assets/service-worker.js`, só será possível registrá-lo em `example.com/assets/*` ou em um subdiretório da pasta `assets`, mas não na sua página inicial (`example.com/`). Por isso, é recomendável hospedar e registrar o service worker no diretório raiz (como `https://example.com/service-worker.js`).

Se não for possível registrar um service worker no domínio raiz, uma alternativa é usar o cabeçalho HTTP [`Service-Worker-Allowed`](https://w3c.github.io/ServiceWorker/#service-worker-script-response) ao servir o arquivo do service worker. Ao configurar seu servidor para retornar `Service-Worker-Allowed: /` na resposta para o service worker, isso instruirá o navegador a ampliar o escopo e permitir que ele seja usado em um diretório diferente.

#### Posso criar um service worker usando um Tag Manager?

Não, os service workers devem ser hospedados no servidor de seu site e não podem ser carregados por meio do Tag Manager.

### Segurança do site

#### O HTTPS é necessário?

Sim. Os padrões da web exigem que o domínio que está solicitando a permissão de notificação por push seja seguro.

#### Quando um site é considerado "seguro"?

Um site é considerado seguro se corresponder a um dos seguintes padrões de origem segura. As notificações por push do Braze Web são criadas com base nesse padrão aberto, de modo que os ataques man-in-the-middle são evitados.

- `(https, , *)`
- `(wss, *, *)`
- `(, localhost, )`
- `(, .localhost, *)`
- `(, 127/8, )`
- `(, ::1/128, *)`
- `(file, *, —)`
- `(chrome-extension, *, —)`

#### E se um site seguro não estiver disponível?

Embora a prática recomendada do setor seja tornar todo o site seguro, os clientes que não podem proteger o domínio do site podem contornar o requisito usando um modal seguro. Saiba mais em nosso guia para usar o [Alternar o domínio de push]({{ site.baseurl }}/developer_guide/platform_integration_guides/web/push_notifications/alternate_push_domain) ou veja uma [demonstração funcional](http://appboyj.com/modal-test.html).

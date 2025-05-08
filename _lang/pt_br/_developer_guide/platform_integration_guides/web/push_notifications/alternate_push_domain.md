---
nav_title: Domínio alternativo de web push
article_title: Domínio alternativo de web push
platform: Web
page_order: 20
page_type: reference
description: "Este artigo aborda como integrar os web pushes da Braze em um domínio alternativo."
channel: push

---

# Domínio alternativo de web push

> Para integrar o web push, seu domínio deve ser [seguro](https://w3c.github.io/webappsec-secure-contexts/), o que geralmente significa `https`, `localhost` e outras exceções, conforme definido no [padrão push do W3C](https://www.w3.org/TR/service-workers/#security-considerations). Você também precisará ser capaz de registrar um Service Worker na raiz do seu domínio ou, pelo menos, controlar os cabeçalhos HTTP desse arquivo. Este artigo aborda como integrar os web pushes da Braze em um domínio alternativo.

_Se não for possível atender a todos esses critérios_, use este guia para configurar uma solução alternativa que permita adicionar uma caixa de diálogo de push prompt ao seu site. Por exemplo, este artigo seria útil se você quiser que o usuário faça o pedido de aceitação em um site `http` (inseguro) ou em um pop-up de extensão do navegador que impeça a exibição do pedido de push.

## Advertências
Lembre-se de que, como muitas soluções alternativas na Web, os navegadores evoluem continuamente e, no futuro, isso pode não funcionar como pretendido.

- Isso exige que:
  - Você possui um domínio seguro separado (`https://`) e tem acesso para registrar um Service Worker nesse domínio.
  - Os usuários devem estar registrados no seu site para garantir que os tokens por push estejam vinculados aos mesmos perfis.

{% alert note %}
O push para Shopify não pode ser implementado dessa forma. A Shopify tome providências para remover cabeçalhos desnecessários para entregar o push.
{% endalert %}

## Integração

Para deixar claro o exemplo a seguir, usaremos `http://insecure.com` e `https://secure.com` como nossos dois domínios, com o objetivo de fazer com que os visitantes se registrem para push em `http://insecure.com`. Esse exemplo também poderia ser aplicado a um esquema `chrome-extension://` para a página pop-up de uma extensão de navegador.

### Etapa 1: Iniciar o fluxo de solicitação

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

### Etapa 2: Registro para push

No momento, o site `secure.com` abrirá uma janela pop-up na qual você poderá inicializar o Braze Web SDK para o mesmo ID de usuário e solicitar a permissão do usuário para o web push.

**https://secure.com/push-registration.html**

<script src="{{site.baseurl}}/assets/js/embed.js?target=https%3A%2F%2Fgithub.com%2Fbraze-inc%2Fbraze-web-sdk%2Fblob%2Fmaster%2Fsnippets%2Falternate-push-domain-registration.html&style=github&showBorder=on&showLineNumbers=on&showFileMeta=on&showCopy=on"></script>

### Etapa 3: Comunicação entre domínios (opcional)

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


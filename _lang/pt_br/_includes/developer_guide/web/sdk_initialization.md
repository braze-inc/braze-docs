## Usando o Google Tag Manager {#initialization-tag}

### Etapa 1: Configuração do push (opcional)

Opcionalmente, se você quiser enviar push por meio do Google Tag Manager, primeiro siga as diretrizes [de integração de push]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=web) para:
1. Configure o service worker do seu site, colocando-o no diretório raiz do site
2. Configure o registro do navegador. Depois que o service worker for configurado, você deverá definir o método `braze.requestPushPermission()` nativamente no app ou por meio de uma tag HTML personalizada (via dashboard do GTM). Você também precisará se certificar de que a tag seja acionada depois que o SDK for inicializado.

### Etapa 2: Selecione a tag de inicialização

Procure a Braze na galeria de modelos da comunidade e selecione a **tag Braze Initialization**.

![Uma caixa de diálogo que mostra as definições de configuração da tag Braze Initialization. As configurações incluídas são "tag type", "API key", "API endpoint", "SDK version", "external user ID" e "Safari web push ID".]({% image_buster /assets/img/web-gtm/gtm-initialization-tag.png %})

### Etapa 3: Configurar definições

Insira sua chave de identificador do app Braze API e o endpoint de SDK, que podem ser encontrados na página **Manage Settings (Gerenciar configurações)** de seu dashboard. Digite a versão mais recente do SDK para Web em `major.minor`. Por exemplo, se a versão mais recente for `4.1.2`, digite `4.1`. Você pode ver uma lista das versões do SDK em nosso [changelog](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md).

### Etapa 4: Escolha as opções de inicialização

Escolha entre o conjunto opcional de opções de inicialização adicionais descritas no [Initial setup]({{ site.baseurl }}/developer_guide/platform_integration_guides/web/initial_sdk_setup/#step-2-initialize-braze) guide.

### Etapa 5: Verificação e controle de qualidade

Depois de implementar essa tag, há duas maneiras de verificar uma integração adequada:

1. Usando a [ferramenta de debug](https://support.google.com/tagmanager/answer/6107056?hl=en) do Google Tag Manager, você verá que a tag Braze Initialization foi disparada em suas páginas ou eventos configurados.
2. Você deverá ver solicitações de rede feitas à Braze e a biblioteca global `window.braze` deverá estar definida em sua página da Web.

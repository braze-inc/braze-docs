### Pré-requisitos

Antes de usar este método de integração, você precisará [criar uma conta e um contêiner para o Google Tag Manager](https://support.google.com/tagmanager/answer/14842164).

### Etapa 1: Abra a galeria de modelos de tag

No [Google Tag Manager](https://tagmanager.google.com/), escolha seu espaço de trabalho e, em seguida, selecione **Modelos**. No painel **Modelo de Tag**, selecione **Pesquisar Galeria**.

![A página de modelos para um espaço de trabalho de exemplo no Google Tag Manager.]({% image_buster /assets/img/web-gtm/search_tag_template_gallery.png %}){: style="max-width:95%;"}

### Etapa 2: Adicione o modelo de tag de inicialização

Na galeria de modelos, procure por `braze-inc`, em seguida, selecione **Tag de Inicialização Braze**.

![A galeria de modelos mostrando os vários modelos 'braze-inc'.]({% image_buster /assets/img/web-gtm/template_gallery_results.png %}){: style="max-width:80%;"}

Selecione **Adicionar ao espaço de trabalho** > **Adicionar**.

![A página 'Tag de Inicialização Braze' no Google Tag Manager.]({% image_buster /assets/img/web-gtm/add_to_workspace.png %}){: style="max-width:70%;"}

### Etapa 3: Configure a tag

Na seção **Modelos**, selecione seu modelo recém-adicionado.

![A página "Modelos" no Google Tag Manager mostrando o modelo de Tag de Inicialização Braze.]({% image_buster /assets/img/web-gtm/select_tag_template.png %}){: style="max-width:95%;"}

Selecione o ícone de lápis para abrir o menu suspenso **Configuração da Tag**.

![O bloco de Configuração da Tag com o ícone de 'lápis' mostrado.]({% image_buster /assets/img/web-gtm/gtm-initialization-tag.png %})

Insira as informações mínimas necessárias:

| Campo         | Descrição |
| ------------- | ----------- |
| **Chave de API**   | Sua [Chave de API Braze]({{site.baseurl}}/api/basics/#about-rest-api-keys), encontrada no painel do Braze em **Configurações** > **Configurações do App**. |
| **Endpoint de API** | Sua URL de endpoint REST. Seu endpoint dependerá do [URL da Braze para [sua instância]({{site.baseurl}}/api/basics/#endpoints). |
| **Versão do SDK**  | A versão mais recente `MAJOR.MINOR` do SDK Web Braze listada no [changelog]({{site.baseurl}}/developer_guide/changelogs/?sdktab=web). Por exemplo, se a versão mais recente for `4.1.2`, digite `4.1`. Para mais informações, veja [Sobre a gestão de versões do SDK]({{site.baseurl}}/developer_guide/sdk_integration/version_management/). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

Para configurações adicionais de inicialização, selecione **Opções de Inicialização Braze** e escolha quaisquer opções que você precisar.

![A lista de Opções de Inicialização do Braze está em 'Configuração de Tag'.]({% image_buster /assets/img/web-gtm/braze_initialization_options.png %}){: style="max-width:65%;"}

### Etapa 4: Escolha as opções de inicialização

A Tag de Inicialização do Braze expõe as seguintes opções. A maioria delas mapeia diretamente para o [SDK Web `InitializationOptions`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initializationoptions), e algumas correspondem a métodos do SDK Web que a tag chamará durante a inicialização. Selecione as opções que correspondem às suas necessidades de integração:

| Opção GTM | Configuração ou método do SDK Web | Descrição |
| --- | --- | --- |
| **Permitir Mensagens In-App em HTML** | `allowUserSuppliedJavascript` | Ativa mensagens in-app em HTML, Banners e ações de clique em JavaScript fornecidas pelo usuário. Necessário para [mensagens in-app em HTML]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/customize/html_in-app_messages/) e [Banners]({{site.baseurl}}/developer_guide/banners/placements/?sdktab=web) que usam HTML personalizado. Ative isso apenas quando confiar no conteúdo HTML e JavaScript, pois permite a execução de JavaScript fornecido pelo usuário. |
| **Número da Versão do App** | `appVersion`, `appVersionNumber` | Versão do app para segmentação (por exemplo, `1.2.3.4`). |
| **Abrir Nova Sessão Automaticamente** | `braze.openSession()` | Abre uma nova sessão após o SDK ser inicializado, chamando este método para você. |
| **Mostrar Novas Mensagens In-App Automaticamente** | `braze.automaticallyShowInAppMessages()` | Exibe automaticamente novas mensagens in-app quando elas chegam do servidor, chamando este método após a inicialização. |
| **Desativar Manutenção Automática do Token Push** | `disablePushTokenMaintenance` | Impede que o SDK sincronize tokens push com o backend do Braze em novas sessões. |
| **Desativar Registro Automático do Service Worker** | `manageServiceWorkerExternally` | Use se você registrar e controlar o service worker você mesmo. |
| **Desativar Cookies** | `noCookies` | Usa localStorage em vez de cookies para dados de usuário/sessão. Previne o reconhecimento entre subdomínios. |
| **Desativar Font Awesome** | `doNotLoadFontAwesome` | Impede que o SDK carregue o Font Awesome do CDN. Use se seu site tiver seu próprio Font Awesome. |
| **Ativar Autenticação do SDK** | `enableSdkAuthentication` | Ativa [Autenticação do SDK]({{site.baseurl}}/developer_guide/sdk_integration/authentication/). |
| **Ativar Registro do SDK Web** | `enableLogging` | Ativa o registro no console para depuração. Remova antes da produção. |
| **Intervalo Mínimo Entre Mensagens Disparadas** | `minimumIntervalBetweenTriggerActionsInSeconds` | Segundos mínimos entre ações de disparo (padrão: 30). |
| **Abrir Cartões em Nova Guia** | `openCardsInNewTab` | Abre links de Cartão de Conteúdo em uma nova guia ao usar a interface padrão do Feed. |
| **Localização do Service Worker** | `serviceWorkerLocation` | Caminho personalizado para o arquivo do service worker (padrão: `/service-worker.js`). |
| **Tempo de Expiração da Sessão (segundos)** | `sessionTimeoutInSeconds` | Tempo limite da sessão em segundos (padrão: 1800). |

{% alert note %}
Para ativar [Mensagens HTML personalizadas no aplicativo]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/customize/html_in-app_messages/) ao usar a Tag de Inicialização do Braze no Google Tag Manager, selecione **Permitir Mensagens HTML no Aplicativo** em **Opções de Inicialização do Braze**. Esta caixa de seleção mapeia para a opção de inicialização `allowUserSuppliedJavascript` em `braze.initialize()` e a define como `true`. A Tag de Inicialização do Braze no Google Tag Manager usa este rótulo em vez do nome da opção.
{% endalert %}

Para opções não expostas no modelo GTM (como `contentSecurityNonce`, `localization` ou `devicePropertyAllowlist`), use [inicialização em tempo de execução]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=web) em vez disso.

### Etapa 5: Defina para Disparar em *todas as páginas*

A tag de inicialização deve ser executada em todas as páginas do seu site. Isso permite que você use métodos do SDK do Braze e registre análises de web push.

### Etapa 6: Verifique sua integração

Você pode verificar sua integração usando qualquer uma das seguintes opções:

- **Opção 1:** Usando a [ferramenta de debug](https://support.google.com/tagmanager/answer/6107056?hl=en) do Google Tag Manager, você pode verificar se a Tag de Inicialização do Braze está disparando corretamente nas suas páginas ou eventos configurados.
- **Opção 2:** Verifique se há solicitações de rede feitas para o Braze a partir da sua página da web. Além disso, a biblioteca global `window.braze` deve agora estar definida.

---
nav_title: Segmento
article_title: Segmento
page_order: 1
alias: /partners/segment/
description: "Este artigo de referência descreve a parceria entre o Braze e a Segment, uma plataforma de dados do cliente que coleta e encaminha informações entre fontes em sua pilha de marketing."
page_type: partner
search_tag: Partner

---

# Segmento

{% multi_lang_include video.html id="RfOHfZ34hYM" align="right" %}

> A [Segment](https://segment.com) é uma plataforma de dados do cliente que ajuda você a coletar, limpar e ativar os dados de seus clientes. 

A integração do Braze e do Segment permite rastrear seus usuários e encaminhar dados para vários provedores de análise de dados de usuários. O Segment permite que você:

- Sincronize [o Segment Engage]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/segment/segment_engage/) com o Braze para uso na campanha do Braze e na segmentação do Canva.
- [Importar dados entre as duas plataformas](#integration-options). Oferecemos uma integração lado a lado de SDK para seus aplicativos Android, iOS e da Web e uma integração de servidor para servidor para sincronizar seus dados com as APIs REST do Braze.
- [Conecte os dados à Segment pelo Currents]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/segment/segment_for_currents/). 

## Pré-requisitos

| Requisito | Descrição |
| ----------- | ----------- |
| Conta do segmento | É necessário ter uma [conta da Segment](https://app.segment.com/login) para aproveitar essa parceria. |
| [Bibliotecas](https://segment.com/docs/sources/) de código-fonte instaladas e de código-fonte do Segment | A origem de todos os dados enviados à Segment, como apps móveis, sites ou servidores back-end.<br><br>Instale as bibliotecas em seu app, site ou servidor antes de configurar um fluxo em `Source > Destination`. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integração

Para integrar o Braze e o Segment, você deve definir [o Braze como um destino](#connection-settings) de acordo com o [tipo de integração escolhido](#integration-options) (modo de conexão). Se você for um cliente novo no Braze, poderá retransmitir dados históricos para o Braze usando [replays de segmentos](#segment-replays). Em seguida, você deve configurar [mapeamentos](#methods) e [testar sua integração](#step-4-test-your-integration) para garantir um fluxo de dados suave entre o Braze e o Segment.

### Etapa 1: crie um destino da Braze {#connection-settings}

Depois de configurar suas fontes com êxito, você precisará configurar a Braze como um [destino](https://segment.com/docs/destinations/) para cada fonte (iOS, Android, Web etc.). Você terá muitas opções para personalizar o fluxo de dados entre o Braze e o Segment usando as configurações de conexão.

### Etapa 2: escolha a estrutura do destino e o tipo de conexão {#integration-options}

No Segment, navegue até **Destinos** > **Braze** > **Configurar** **o** **Braze** > **Selecione sua fonte** > **Configuração**.

![A página de configuração da fonte. Essa página inclui configurações para definir a estrutura de destino como "ações" ou "clássica" e definir o modo de conexão como "modo de nuvem" ou "modo de dispositivo".]({% image_buster /assets/img/segment/setup.png %})

Você pode integrar o código-fonte da Web da Segment (Analytics.js) e as bibliotecas nativas do lado do cliente com a Braze usando uma integração lado a lado (modo dispositivo) ou uma integração servidor a servidor (modo nuvem).

Sua escolha do modo de conexão será determinada pelo tipo de fonte para o qual o destino está configurado.

| Integração | Informações |
| ----------- | ------- |
| [Lado a lado<br>(modo dispositivo)](#side-by-side-sdk-integration) |Usa o SDK da Segment para traduzir eventos em chamadas nativas do Braze, permitindo acesso a recursos mais profundos e uso mais abrangente do Braze do que a integração de servidor para servidor.<br><br>Observe que a Segment não é compatível com todos os métodos da Braze (por exemplo, cartões de conteúdo). Para usar um método da Braze que não esteja mapeado por um mapeamento correspondente, será necessário invocar o método adicionando o código nativo da Braze à sua base de código. |
| [De servidor para servidor<br>(modo nuvem)](#server-to-server-integration) | Encaminha dados do Segment para os endpoints da API do Braze REST.<br><br>Não oferece suporte aos recursos da interface do usuário do Braze, como envio de mensagens no app, cartões de conteúdo ou notificações por push. Também existem dados capturados automaticamente, como campos em nível de dispositivo, que não estão disponíveis por meio desse método.<br><br>Considere uma integração lado a lado se quiser usar esses recursos.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert note %}
Visite [o Segment](https://segment.com/docs/destinations/#connection-modes) para saber mais sobre as duas opções de integração (modos de conexão), incluindo os benefícios de cada uma.
{% endalert %}

#### Integração lado a lado de SDK

Também chamada de modo dispositivo, essa integração mapeia o SDK e os [métodos](#methods) da Segment para o SDK da Braze, permitindo o acesso a todos os recursos do nosso SDK, como push, envio de mensagens no app e outros métodos nativos da Braze. 

{% alert note %}
Ao usar o modo de dispositivo da Segment, você não precisa integrar o Braze SDK diretamente. Ao adicionar a Braze como um destino do modo dispositivo para a Segment, o Segment SDK inicializará o Braze SDK e chamará os métodos mapeados relevantes da Braze.
{% endalert %}

Ao usar uma conexão no modo dispositivo, semelhante à integração nativa do Braze SDK, o Braze SDK atribuirá um `device_id` e um identificador de backend, `braze_id`, a cada usuário. Isso permite que o Braze capture a atividade anônima do dispositivo fazendo a correspondência com esses identificadores em vez de `userId`. 

{% tabs local %}
{% tab Android %}

{% alert important %}
O código-fonte para a integração do modo de dispositivo Android é mantido pela Braze e é atualizado regularmente para refletir as novas versões do Braze SDK.

<br>
O Braze SDK a ser usado depende do Segment SDK que você usa:

| | Segment SDK | Braze SDK |
| - | ----------- | --------- |
| Preferencialmente | [Análise de dados Kotlin](https://github.com/segmentio/analytics-kotlin) | [Braze Segment Kotlin](https://github.com/braze-inc/braze-segment-kotlin) |
| Legacy | [Análise de dados - Android](https://github.com/segmentio/analytics-android) | [Braze Segment Android](https://github.com/braze-inc/braze-segment-android)
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }


{% endalert %}

Para configurar o Braze como um destino de modo de dispositivo para sua origem Android, escolha **Actions (Ações** ) como a **estrutura Destination**(Destino) e selecione **Save (Salvar)**. 

Para concluir a integração lado a lado, consulte as instruções detalhadas da Segment para adicionar a dependência de destino do Braze ao seu app para [Android](https://segment.com/docs/connections/sources/catalog/libraries/mobile/kotlin-android/destination-plugins/braze-kotlin-android/).

O código-fonte para a integração do [modo de dispositivo Android](https://github.com/braze-inc/braze-segment-kotlin) é mantido pelo Braze e é atualizado regularmente para refletir as novas versões do Braze SDK.

{% endtab %}
{% tab iOS %}

{% alert important %}
O código-fonte para a integração do modo de dispositivo iOS é mantido pelo Braze e é atualizado regularmente para refletir as novas versões do Braze SDK.

<br>
O Braze SDK a ser usado depende do Segment SDK que você usa:

| | Segment SDK | Braze SDK |
| - | ----------- | --------- |
| Preferencial | [Analytics-Swift](https://github.com/segmentio/analytics-swift) | [Braze Segment Swift](https://github.com/braze-inc/braze-segment-swift) |
| Legacy | [Análise de dados iOS](https://github.com/segmentio/analytics-ios) | [Braze Segment iOS](https://github.com/Appboy/appboy-segment-ios) |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }
{% endalert %}

Para configurar o Braze como um destino no modo dispositivo para sua origem iOS, escolha **Ações** como a **estrutura de destino** e selecione **Salvar**. 

Para concluir a integração lado a lado, consulte as instruções detalhadas do Segment para adicionar o pod Braze Segment ao seu app [para iOS](https://segment.com/docs/connections/sources/catalog/libraries/mobile/apple/destination-plugins/braze-swift/).

O código-fonte da integração [do modo de dispositivo iOS](https://github.com/braze-inc/braze-segment-swift) é mantido pela Braze e é atualizado regularmente para refletir as novas versões do Braze SDK.

{% endtab %}
{% tab Web ou JavaScript %}

A estrutura do Braze Web Mode (Actions) da Segment é recomendada para configurar o Braze como um destino de modo de dispositivo para sua fonte da Web. 

Em Segment, selecione **Actions (Ações** ) como sua estrutura de destino e **Device Mode (Modo dispositivo** ) como seu modo de conexão.

![]({% image_buster /assets/img/segment/website.png %})

{% endtab %}
{% tab React Native %}
O código-fonte do [plug-in React Native Braze](https://github.com/segmentio/analytics-react-native/tree/master/packages/plugins/plugin-braze) é mantido pela Segment e é atualizado regularmente para refletir as novas versões do Braze SDK.

Ao conectar uma fonte React Native Segment à Braze, configure uma origem e um destino por sistema operacional. Por exemplo, um destino para iOS e de um destino para Android. 

Na base de código do seu aplicativo, inicialize condicionalmente o Segment SDK por tipo de dispositivo, usando a respectiva chave de gravação de origem associada a cada app.

Quando um token por push é registrado de um dispositivo e enviado à Braze, ele é associado ao identificador do app usado na inicialização do SDK. A inicialização condicional do tipo de dispositivo ajuda a confirmar que todos os tokens por push enviados ao Braze estão associados ao aplicativo relevante.

{% alert important %}
Se o aplicativo React Native inicializar o Braze com o mesmo identificador de aplicativo do Braze para todos os dispositivos, todos os usuários do React Native serão considerados usuários de Android ou iOS no Braze, e todos os tokens por push serão associados a esse sistema operacional.
{% endalert %}

Para configurar o Braze como um destino de modo de dispositivo para cada origem, selecione **Ações** como a **estrutura de destino** e, em seguida, selecione **Salvar**.

{% endtab %}
{% endtabs %}

#### Integração de servidor para servidor

Também chamada de modo de nuvem, essa integração encaminha dados do Segment para as APIs REST do Braze. Use a estrutura [do Braze Cloud Mode (Actions)](https://segment.com/docs/connections/destinations/catalog/braze-cloud-mode-actions/) do Segment para configurar um destino em modo de nuvem para qualquer uma de suas origens. 

Ao contrário da integração lado a lado, a integração servidor a servidor não oferece suporte aos recursos da interface do usuário do Braze, como envio de mensagens no app, cartões de conteúdo ou registro automático de token por push. Também existem dados [capturados automaticamente]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/#user-data-collection) (como usuários anônimos e campos no nível do dispositivo) que não estão disponíveis no modo de nuvem.

Se quiser usar esses dados e recursos, considere adotar a integração lado a lado (modo de dispositivo) do SDK.

O código-fonte do [destino Braze Cloud Mode (Actions)](https://github.com/segmentio/action-destinations/tree/main/packages/destination-actions/src/destinations/braze) é mantido pela Segment.

### Etapa 3: Configurações

Defina as configurações para seu destino. Nem todas as configurações se aplicarão a todos os tipos de destinos.

{% tabs local %}
{% tab Modo de dispositivo móvel %}

| Configuração | Descrição |
| ------- | ----------- |
| Identificador do app | O identificador de aplicativo usado para fazer referência ao aplicativo específico. Isso pode ser encontrado no dashboard do Braze em **Manage Settings (Gerenciar configurações)** | 
| Ponto de extremidade personalizado da API<br>(Endpoint de SDK) | Seu endpoint de SDK da Braze que corresponde à sua instância (como `sdk.iad-01.braze.com`) | 
| Região do ponto final | Sua instância da Braze (como US 01, US 02, EU 01 etc.) | 
| Ativar o registro automático de mensagens no app | Desative essa opção se quiser registrar manualmente as mensagens no app. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab Modo de dispositivo da Web %}

| Configuração | Descrição |
| ------- | ----------- |
| Identificador do app | O identificador de aplicativo usado para fazer referência ao aplicativo específico. Isso pode ser encontrado no dashboard do Braze em **Manage Settings (Gerenciar configurações)** | 
| Ponto de extremidade personalizado da API<br>(Endpoint de SDK) | Seu endpoint de SDK da Braze que corresponde à sua instância (como `sdk.iad-01.braze.com`) | 
| ID de web push do Safari | Caso ofereça suporte ao push do Safari, especifique essa opção com o ID de web push que você forneceu à Apple ao criar o certificado de push do Safari (começa com `web`, como `web.com.example.domain`). |
| Versão do Braze Web SDK | A versão do SDK para Web da Braze que você gostaria de usar |
| Envie automaticamente mensagens no app | Por padrão, todas as mensagens no app para as quais um usuário é elegível são automaticamente entregues ao usuário. Desative essa opção se quiser exibir manualmente as mensagens no app. |
| Não carregue a fonte awesome | O Braze usa Font Awesome para os ícones de mensagens no app. Por padrão, a Braze carregará automaticamente o FontAwesome a partir do CDN do FontAwesome. Para desativar esse comportamento (por exemplo, porque seu site usa uma versão personalizada do FontAwesome), defina essa opção como `TRUE`. Observe que, se fizer isso, você será responsável por garantir que a FontAwesome seja carregada em seu site; caso contrário, as mensagens no app poderão não ser renderizadas corretamente. |
| Ativar mensagens no app em HTML | Quando ativada, essa opção permite que os usuários do dashboard da Braze usem mensagens HTML no app. | 
| Abra as mensagens no app em uma nova guia | Por padrão, os links de cliques em mensagens no app são carregados na guia atual ou em uma nova guia, conforme especificado no dashboard, mensagem por mensagem. Defina essa opção como `TRUE` para forçar todos os links de cliques em mensagens no app a abrirem em uma nova guia ou janela. |
| Índice z de mensagens no app | Forneça um valor para essa opção para substituir os índices z padrão do Braze. | 
| Exigir o cancelamento explícito de mensagens no app | Por padrão, quando uma mensagem no app estiver sendo exibida, pressionar o botão de escape ou clicar no fundo acinzentado da página descartará a mensagem. Defina essa opção como true para evitar esse comportamento e exigir um clique explícito no botão para descartar as mensagens. |
| Intervalo mínimo entre ações-gatilho em segundos | O padrão é 30.<br>Por padrão, uma ação-gatilho só será disparada se pelo menos 30 segundos tiverem se passado desde a última ação-gatilho. Forneça um valor para essa opção de configuração para substituir o padrão por um valor próprio. Não recomendamos que esse valor seja menor que 10 para evitar que o usuário receba notificações de spam.|
| Local do trabalho de serviço | Por padrão, ao registrar usuários para notificações por push na Web, o Braze procurará o arquivo de service worker necessário no diretório raiz do seu servidor da Web em `/service-worker.js`. Se quiser hospedar o trabalho de serviço em um caminho diferente nesse servidor, forneça um valor para essa opção que seja o caminho absoluto para o arquivo. (por exemplo, `/mycustompath/my-worker.js`). Observe que a definição de um valor aqui limita o escopo das notificações por push em seu site. A título de ilustração, no exemplo acima, como o arquivo do service worker está localizado no diretório `/mycustompath/`, `requestPushPermission` só pode ser chamado a partir de páginas da Web que comecem com `http://yoursite.com/mycustompath/`. |
| Desativar a manutenção do token por push | Por padrão, os usuários que já concederam permissão de web push sincronizarão seu token por push com o backend do Braze automaticamente em novas sessões para garantir a entregabilidade. Para desativar esse comportamento, defina a opção como `FALSE`. |
| Gerenciar o trabalhado de serviços externamente | Se você tiver seu próprio trabalho de serviço para registrar e controlar o ciclo de vida, defina essa opção como `TRUE`, e o Braze SDK não registrará nem cancelará o registro de um trabalho de serviço. Se essa opção for definida como `TRUE`, para que o push funcione corretamente, você mesmo deverá registrar o service worker antes de chamar `requestPushPermission` e garantir que ele contenha o código do service worker do Braze, seja com `self.importScripts('https://js.appboycdn.com/web-sdk-develop/4.1/service-worker.js');` ou incluindo o conteúdo desse arquivo diretamente. Quando essa opção é `TRUE`, a opção `serviceWorkerLocation` é irrelevante e é ignorada. |
| Nonce de segurança de conteúdo | Se você fornecer um valor para essa opção, o Braze SDK adicionará o nonce a todos os elementos `<script>` e `<style>` criados pelo SDK. Isso permite que o Braze SDK trabalhe com a política de segurança de conteúdo do seu site. Além de definir esse nonce, talvez seja necessário permitir o carregamento do FontAwesome, o que pode ser feito adicionando `use.fontawesome.com` à sua lista de permissões da política de segurança de conteúdo ou usando a opção `doNotLoadFontAwesome` e carregando-o manualmente. |
| Permitir atividade de rastreador | Por padrão, o SDK para Web da Braze ignora a atividade de spiders ou rastreadores da Web conhecidos, como o Google, com base na string do agente do usuário. Isso economiza pontos de dados, torna a análise de dados mais precisa e pode melhorar a classificação da página. No entanto, se quiser que o Braze registre a atividade desses rastreadores, defina essa opção como `TRUE`. |
| Ativar o registro | Defina como `TRUE` para ativar o registro por padrão. Note que isso fará com que a Braze registre no console JavaScript, que é visível para todos os usuários. Antes de liberar sua página para produção, você deve removê-la ou fornecer outro agente de registro com `setLogger`. |
| Permitir JavaScript fornecido pelo usuário | Por padrão, o SDK para Web da Braze não permite ações de clique em JavaScript fornecidas pelo usuário, pois permite que os usuários do dashboard da Braze executem JavaScript no seu site. Para indicar que você confia nos usuários do dashboard do Braze para escrever ações de clique em JavaScript não maliciosas, defina essa propriedade como `TRUE`. Se `enableHtmlInAppMessages` for `TRUE`, essa opção também será definida como `TRUE`. |
| Versão do app| Se você fornecer um valor para essa opção, os eventos de usuário enviados ao Braze serão associados à versão fornecida, que pode ser usada para segmentação de usuários. |
| Tempo limite da sessão em segundos | O padrão é 30.<br>Por padrão, as sessões são encerradas após 30 minutos de inatividade. Forneça um valor para essa opção de configuração para substituir o padrão por um valor próprio. | 
| Lista de permissões de propriedades do dispositivo | Por padrão, o Braze SDK detecta e coleta automaticamente todas as propriedades do dispositivo em `DeviceProperties`. Para substituir esse comportamento, forneça uma matriz de `DeviceProperties`. Observe que, sem algumas propriedades, nem todos os recursos funcionam corretamente. Por exemplo, a entrega no horário local não funcionará sem o fuso horário. |
| Localização | Por padrão, todas as mensagens visíveis ao usuário geradas pelo SDK são exibidas no idioma do navegador do usuário. Forneça um valor para essa opção para substituir esse comportamento e forçar um idioma específico. O valor dessa opção deve ser um código de idioma ISO 639-1. |
| Sem cookies | Por padrão, o SDK do Braze armazena pequenas quantidades de dados (IDs de usuário, IDs de sessão) em cookies. Isso é feito para permitir que o Braze reconheça usuários e sessões em diferentes subdomínios do seu site. Se isso for um problema para você, passe `TRUE` para essa opção para desativar o armazenamento de cookies e confiar inteiramente no localStorage do HTML 5 para identificar usuários e sessões. |
| Rastreamento de todas as páginas | **Somente modo de dispositivo Web de destino clássico (manutenção)**<br><br>A Segment recomenda a migração para o destino da estrutura do Web Actions, onde essa configuração pode ser [ativada por meio de mapeamentos](https://segment.com/docs/connections/destinations/catalog/braze-web-device-mode-actions/#braze-web-settings-mapping).<br><br>Isso enviará todas as [chamadas de página](https://segment.com/docs/spec/page/) para o Braze como um evento "Loaded/Viewed a Page" (Carregado/Visualizado uma página). |
| Rastrear apenas páginas nomeadas | **Somente modo de dispositivo Web de destino clássico (manutenção)**<br><br>A Segment recomenda a migração para o destino da estrutura do Web Actions, onde essa configuração pode ser [ativada por meio de mapeamentos](https://segment.com/docs/connections/destinations/catalog/braze-web-device-mode-actions/#braze-web-settings-mapping).<br><br>Isso enviará apenas chamadas de página para o Braze com um nome associado a elas. |
| Registre a compra quando a receita estiver presente | **Somente modo de dispositivo Web de destino clássico (manutenção)**<br><br>A Segment recomenda a migração para o destino da estrutura do Web Actions, onde essa configuração pode ser [ativada por meio de mapeamentos](https://segment.com/docs/connections/destinations/catalog/braze-web-device-mode-actions/#braze-web-settings-mapping).<br><br>Quando essa opção estiver ativada, todas as chamadas de rastreamento com a propriedade de receita dispararão um evento de compra. | 
| Rastrear apenas usuários conhecidos | **Somente modo de dispositivo Web de destino clássico (manutenção)**<br><br>A Segment recomenda a migração para o destino Web Actions Framework, onde essa configuração pode ser ativada por meio de mapeamentos.<br><br>Se ativada, essa nova configuração posterga a chamada de `window.appboy.initialize` até que haja um `userId` válido. | 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab Modo de nuvem %}

| Configuração | Descrição |
| ------- | ----------- |
| Identificador do app | O identificador de aplicativo usado para fazer referência ao aplicativo específico. Isso pode ser encontrado no dashboard do Braze em **Manage Settings (Gerenciar configurações)** | 
| Chave da API REST | Isso pode ser encontrado em seu dashboard do Braze em **Settings** > **API Keys** (Configurações > Chaves de API). | 
| Ponto de extremidade personalizado da API REST | O endpoint REST da Braze que corresponde à sua instância (como rest.iad-01.braze.com). | 
| Atualizar somente usuários existentes | **Somente modo de nuvem de destino clássico (manutenção)**<br><br>A Segment recomenda a migração para o destino do Cloud Actions Framework, onde essa configuração pode ser [ativada por meio de mapeamentos](https://segment.com/docs/connections/destinations/catalog/braze-web-device-mode-actions/#braze-web-settings-mapping).<br><br>Determina se os usuários existentes serão atualizados apenas. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% endtabs %}

### Etapa 4: métodos de mapas {#methods}

O Braze oferece suporte aos métodos [Page](https://segment.com/docs/connections/sources/catalog/libraries/website/javascript/#page), [Identify](https://segment.com/docs/spec/identify/) e [Track](https://segment.com/docs/spec/track/) Segment. Os tipos de identificadores usados nesses métodos dependerão do fato de os dados estarem sendo enviados por meio de uma integração servidor a servidor (modo nuvem) ou lado a lado (modo dispositivo). Nos destinos Braze Web Mode Actions e Cloud Mode Actions, você também pode optar por configurar um mapeamento para uma [chamada de alias da Segment](https://segment.com/docs/connections/spec/alias/). 

{% alert note %}
Embora os aliases de usuário sejam suportados como um identificador no destino do Braze Cloud Mode (Actions), deve-se notar que a chamada de alias do Segment não está diretamente relacionada aos aliases de usuário do Braze.
{% endalert %}

| Tipo de identificador | Destinos aceitos |
| --------------- | --------------------- |
| `userId` (`external_id`) | Tudo |
| Usuário anônimo | Destinos do modo dispositivo |
| Alias de usuário | Destinos no modo nuvem |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

O destino Modo de nuvem (Ações) oferece uma [ação Criar alias](https://segment.com/docs/connections/destinations/catalog/actions-braze-cloud/#create-alias) que pode ser usada para criar um usuário somente de alias ou adicionar um alias a um perfil `external_id` existente. A [ação Identificar usuário](https://segment.com/docs/connections/destinations/catalog/actions-braze-cloud/#identify-user) pode ser usada juntamente com a ação Criar alias para mesclar um usuário somente de alias com um `external_id` depois que um estiver disponível para o usuário. 

Também é possível criar uma solução alternativa e usar o `braze_id` para enviar dados de usuários anônimos no modo de nuvem. Para isso, é necessário incluir manualmente o endereço `braze_id` do usuário em todas as suas chamadas à API do Segment. Você pode saber mais sobre como configurar essa solução alternativa na [documentação do Segment](https://segment.com/docs/connections/destinations/catalog/braze/#capture-the-braze_id-of-anonymous-users).

Os dados de destinos enviados à Braze podem ser agrupados em ações do modo de nuvem. Os tamanhos dos lotes são limitados a 75 eventos, e esses lotes se acumulam em um período de 30 segundos antes de serem descarregados. O agrupamento de solicitações é feito por ação. Por exemplo, as chamadas de identificação (atribuições) serão agrupadas em uma solicitação e as chamadas de rastreamento (eventos personalizados) serão agrupadas em uma segunda solicitação. A Braze recomenda ativar esse recurso, pois ele reduz o número de solicitações enviadas da Segment para a Braze. Por sua vez, isso reduzirá o risco de o destino atingir os limites de frequência do Braze e tentar novamente as solicitações. 

Você pode ativar a criação de lotes para uma ação em Braze Destination > **Mappings** (Destino da Braze > Mapeamentos). A partir daí, clique no ícone de três pontos à direita do mapeamento e selecione **Editar mapeamento**. Role até a parte inferior da seção **Select mappings (Selecionar mapeamentos** ) e verifique se a opção **Batch Data to Braze** está definida como **Yes (Sim**).


{% tabs local %}
{% tab Identificar %}
#### Identificar

A chamada [Identify](https://segment.com/docs/spec/identify/) permite vincular um usuário às suas ações e registrar atribuições sobre ele. 

Certas características especiais do Segmento são mapeadas para campos de perfil de atribuição padrão no Braze:

| Características de segmentos especiais | Atribuições padrão do Braze |
| ------------- | ----------- |
| `userId` | `external_id` |
| `firstName` | `first_name` |
| `lastName` | `last_name` |
| `email` | `email` |
| `birthday` | `dob` |
| `address.country` | `country` |
| `address.city` | `home_city` |
| `gender` | `gender` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Outros campos de perfil reservados do Braze, como `email_subscribe` e `push_subscribe`, podem ser enviados usando a convenção de nomenclatura do Braze para esses campos e passando-os como características em uma chamada de identificação.

##### Adição de um usuário a um grupo de inscrições

Também é possível inscrever ou cancelar a inscrição de um usuário em um determinado grupo de inscrições usando os seguintes campos no parâmetro traits.

Use o campo reservado do perfil da Braze chamado `braze_subscription_groups`, que pode ser associado a um vetor de objetos. Cada objeto do vetor deve ter duas chaves reservadas:

1. `subscription_group_state`: Indica se o usuário está `"subscribed"` ou `"unsubscribed"` em um grupo de inscrições específico.
2. `subscription_group_id`: Representa o ID exclusivo do grupo de inscrições. Você pode encontrar esse ID no dashboard do Braze, em **Gerenciamento do grupo de inscrições**.

{% subtabs %}
{% subtab Swift %}
```swift
analytics.identify(
  userId: "{your-user}",
  traits: [
    "braze_subscription_groups": [
      [
        "subscription_group_id": "{your-group-id}",
        "subscription_group_state": "subscribed"
      ],
      [
        "subscription_group_id", "{your-group-id}",
        "subscription_group_state": "unsubscribed"
      ]
    ]
  ]
)
```
{% endsubtab %}
{% subtab Kotlin %}
```kotlin
analytics.identify(
  "{your-user}",
  buildJsonObject {
    put("braze_subscription_groups", buildJsonArray {
        add(
          buildJsonObject {
            put("subscription_group_id", "{your-group-id}")
            put("subscription_group_state", "subscribed")
          }
        )
        add(
          buildJsonObject {
            put("subscription_group_id", "{your-group-id}")
            put("subscription_group_state", "unsubscribed")
          }
        )
      }
    )
  }
)
```
{% endsubtab %}
{% subtab TypeScript %}
```typescript
analytics.identify(
  "{your-user}",
  {
    braze_subscription_groups: [
      {
        subscription_group_id: "{your-group-id}",
        subscription_group_state: "subscribed"
      },
      {
        subscription_group_id: "{your-group-id}",
        subscription_group_state: "unsubscribed"
      }
    ]
  }
)
```
{% endsubtab %}
{% endsubtabs %}

##### Atributos personalizados

Todas as outras características serão registradas como [atributos personalizados]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/).

| Método de segmento | Método Braze | Exemplo |
|---|---|---|
| Identificar com o ID do usuário | Definir ID externa | Segmento:  `analytics.identify("dawei");`<br>Braze: `Braze.changeUser("dawei")` |
| Identificar-se com traços reservados | Definir atribuições do usuário | Segmento: `analytics.identify({email: "dawei@braze.com"});`<br> Braze: `Braze.getUser().setEmail("dawei@braze.com");`
| Identifique-se com características personalizadas | Definir atributos personalizados | Segmento: `analytics.identify({fav_cartoon: "Naruto"});`<br>Braze: `Braze.getUser().setCustomAttribute("fav_cartoon": "Naruto")`;
| Identifique-se com a ID e as características do usuário | Segmento: Definir ID e atribuição externa | Combine os métodos anteriores. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Nos destinos [Ações do Modo Web](https://segment.com/docs/connections/destinations/catalog/braze-web-device-mode-actions/#update-user-profile) e [Ações do Modo Nuvem](https://segment.com/docs/connections/destinations/catalog/braze-cloud-mode-actions/#update-user-profile), os mapeamentos acima podem ser definidos usando a Ação Atualizar Perfil de Usuário.

{% alert important %}
Ao passar os dados de usuários, verifique se só passa valores para atributos que foram alterados desde a última atualização. Isso garante que você não consuma desnecessariamente pontos da sua cota de dados. Para fontes do lado do cliente, use a ferramenta [middleware](https://github.com/segmentio/segment-braze-mobile-middleware) de código aberto da Segment para otimizar sua integração e limitar o uso de pontos de dados, eliminando chamadas `identify()` da Segment. 

{% endalert %}
{% endtab %}

{% tab Rastrear %}
#### Rastreamento

Quando rastrear um evento, registraremos esse evento como um [evento personalizado]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#custom-events) usando o nome fornecido. 

Os metadados enviados dentro do objeto de propriedades da chamada de rastreamento serão registrados no Braze como as propriedades de evento personalizado para o evento associado. Todos os [tipos de dados de propriedades de eventos personalizados]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#custom-event-properties) são compatíveis.

Nos destinos [Ações do modo Web](https://segment.com/docs/connections/destinations/catalog/braze-web-device-mode-actions/#track-event) e [Ações do modo Nuvem](https://segment.com/docs/connections/destinations/catalog/braze-cloud-mode-actions/#track-event), os mapeamentos acima podem ser definidos usando a Ação de rastreamento de eventos.

| Método de segmento | Método Braze | Exemplo |
|---|---|---|
| [Rastreamento](https://segment.com/docs/spec/track/) | Registrado como um [evento personalizado]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#custom-events). | Segmento: `analytics.track("played_game");` <br>Braze: `Braze.logCustomEvent("played_game");`|
| [Rastreamento com propriedades](https://segment.com/docs/spec/track/) | Registrado como [propriedade de evento]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#custom-event-properties). | Segmento: `analytics.track("played_game", {name: "BotW", weapon: "boomerang"});` <br>Braze: `Braze.logCustomEvent("played_game", { "name": "BotW", "weapon": "boomerang"});` |
| [Rastreamento com o produto](https://segment.com/docs/spec/track/) | Registrado como um [evento de compra]({{site.baseurl}}/developer_guide/analytics/logging_purchases/?tab=web). | Segmento: `analytics.track("Order Completed", {products: [product_id: "ab12", price: 19]});` <br>Braze: `Braze.logPurchase("ab12", 19);` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

##### Pedido concluído {#order-completed}

Quando você rastrear um evento com o nome `Order Completed` usando o formato descrito na [API de comércio eletrônico](https://segment.com/docs/spec/ecommerce/v2/) da Segment, registraremos os produtos que você listou como [compras]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/exporting_revenue_data/#revenue-data).

Nos destinos [Web Mode Actions](https://segment.com/docs/connections/destinations/catalog/braze-web-device-mode-actions/#track-purchase) e [Cloud Mode Actions](https://segment.com/docs/connections/destinations/catalog/braze-cloud-mode-actions/#track-purchase), o mapeamento padrão pode ser personalizado pela ação de rastreamento de compra.

{% endtab %}

{% tab Página %}
#### Página {#page}

A chamada [Page](https://segment.com/docs/spec/page/) permite registrar sempre que um usuário vê uma página do seu site, juntamente com quaisquer propriedades opcionais sobre a página.

Esse tipo de evento pode ser usado como um disparo nos destinos Web Mode Actions e Cloud Actions para registrar um evento personalizado no Braze.
{% endtab %}

{% endtabs %}

### Etapa 5: Teste sua integração

Ao usar a integração lado a lado (modo de dispositivo), suas métricas de [visão geral]({{site.baseurl}}/user_guide/data_and_analytics/analytics/understanding_your_app_usage_data/) (sessões vitalícias, MAU, usuário ativo diário, aderência, sessões diárias e sessões diárias por MAU) podem ser usadas para assegurar que a Braze receba dados da Segment.

Você pode visualizar seus dados nas páginas de [eventos personalizados]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/export_custom_event_data/#custom-event-data) ou [de receita]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/exporting_revenue_data/#revenue-data), ou [criando um segmento]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/#creating-a-segment). A página **Eventos personalizados** do dashboard permite que você visualize as contagens de eventos personalizados ao longo do tempo. Observe que você não poderá usar [fórmulas]({{site.baseurl}}/user_guide/data_and_analytics/creating_a_formula/#creating-a-formula) que incluam estatísticas de MAU e DAU ao usar uma integração de servidor para servidor (modo de nuvem).

Se estiver enviando dados de compra para o Braze (veja o pedido concluído na guia **Rastreamento** da [etapa 3](#methods)), a página de [receita]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/exporting_revenue_data/#revenue-data) permite visualizar dados sobre receita ou compras em períodos específicos ou a receita total do seu app.

[A criação de um segmento]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/#creating-a-segment) permite filtrar os usuários com base nos dados de eventos e atributos personalizados.

{% alert important %}
Se você usar uma integração de servidor para servidor (modo de nuvem), os filtros relacionados aos dados de sessão coletados automaticamente (como "primeiro aplicativo usado" e "último aplicativo usado") não funcionarão. Use uma integração lado a lado (modo de dispositivo) se quiser usá-los na sua integração da Segment e da Braze.
{% endalert %}

## Exclusão e supressão de usuários 

Se precisar excluir ou suprimir usuários, note que [o recurso de exclusão de usuários do Segment](https://segment.com/docs/privacy/user-deletion-and-suppression/#which-destinations-can-i-send-deletion-requests-to) **é** mapeado para o [endpoint `/users/delete`]({{site.baseurl}}/api/endpoints/user_data/post_user_delete/) da Braze. Observe que a verificação dessas exclusões pode levar até 30 dias.

É necessário selecionar um identificador de usuário comum entre a Braze e a Segment (como em `external_id`). Depois de iniciar uma solicitação de exclusão com o Segment, você pode visualizar o status na guia solicitações de exclusão no dashboard do Segment.

## Repetições de segmentos

A Segment presta um serviço aos clientes para "reproduzir" todos os dados históricos em um novo parceiro de tecnologia. Os novos clientes da Braze que desejarem importar todos os dados históricos relevantes poderão fazê-lo por meio da Segment. Fale com seu representante da Segment se isso for algo de seu interesse.

O Segment se conectará ao nosso [endpoint`/users/track` ]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) para importar dados de usuários para o Braze em seu nome.

{% alert important %}
Todos os identificadores compatíveis com o destino das ações do modo de nuvem são compatíveis como parte das repetições de segmentos.
{% endalert %}

## Práticas recomendadas

{% details Analise os casos de uso para evitar excedentes de dados. %}

O Segment **não** limita o número de elementos de dados que os clientes enviam para ele. O segmento permite que você envie todos ou decida quais eventos serão enviados ao Braze. Em vez de enviar todos os seus eventos usando o Segment, sugerimos que você analise os casos de uso com suas equipes de marketing e editorial para determinar quais eventos serão enviados ao Braze para evitar excedentes de dados.

{% enddetails %}

{% details Entenda a diferença entre o ponto de extremidade da API personalizada e o ponto de extremidade da API REST personalizada nas configurações de destino do modo de dispositivo móvel. %}

| Terminologia do Braze | Segmento equivalente |
| ----------------- | ------------------ |
| Endpoint do SDK do Braze | Ponto de extremidade personalizado da API |
| Ponto de extremidade REST do Braze | Ponto de extremidade personalizado da API REST |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Seu endpoint da Braze API (chamado de "Custom API Endpoint" na Segment) é o endpoint de SDK que a Braze configura para seu SDK (por exemplo, `sdk.iad-03.braze.com`). Seu endpoint da API REST da Braze (chamado de "Custom REST API Endpoint" na Segment) é o endpoint da REST API (por exemplo, `https://rest.iad-03.braze.com`)
{% enddetails %}

{% details Verifique se o ponto de extremidade da API personalizada foi inserido corretamente nas configurações de destinos do modo dispositivo móvel. %}

| Terminologia do Braze | Segmento equivalente |
| ----------------- | ------------------ |
| Endpoint do SDK do Braze | Ponto de extremidade personalizado da API |
| Ponto de extremidade REST do Braze | Ponto de extremidade personalizado da API REST |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

É necessário seguir o formato adequado para não correr o risco de informar o endpoint do Braze SDK incorretamente. Seu endpoint do Braze SDK não deve incluir `https://` (por exemplo, `sdk.iad-03.braze.com`), senão a integração da Braze será interrompida. Isso é necessário porque o Segment prefixa automaticamente seu endpoint com `https://`, o que resulta em uma tentativa de inicialização da Braze com o endereço inválido `https://https://sdk.iad-03.braze.com`.

{% enddetails %}

{% details Nuances do mapeamento de dados. %}

Cenários em que os dados não serão transmitidos conforme o esperado:

1. Atributos personalizados aninhados
  - Embora [os atributos personalizados aninhados]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/nested_custom_attribute_support/) possam tecnicamente ser enviados ao Braze por meio do Segment, **toda a carga útil** será enviada a cada vez. Isso incorrerá em [pontos de dados]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/nested_custom_attribute_support/#data-points) por chave passada no objeto aninhado toda vez que a carga útil for enviada.<br><br> Para gastar apenas um subconjunto de pontos de dados quando a carga útil é enviada, você pode usar o recurso de [funções de destino](https://segment.com/docs/connections/functions/destination-functions/) personalizadas pertencente ao Segment. Esse recurso da plataforma Segment permite que você personalize a forma como os dados são enviados para destinos downstream.

  {% alert note %}
  As funções de destinos personalizados são controladas na Segment, e o Braze tem insight limitado sobre as funções que foram configuradas externamente.
  {% endalert %}

{: start="2"}
2\. Passagem de dados anônimos de servidor para servidor.
  - Os clientes podem usar as bibliotecas de servidor para servidor da Segment para canalizar dados anônimos para outros sistemas. Consulte a seção de métodos de mapa para saber mais sobre como enviar usuários sem um `external_id` para o Braze por meio de uma integração de servidor para servidor (modo de nuvem).

{% enddetails %}

{% details Personalização da inicialização do Braze. %}

Há várias maneiras diferentes de personalizar o Braze: push, mensagens no app, cartões de conteúdo e inicialização. Com uma integração lado a lado, você ainda pode personalizar o push, as mensagens no app e os cartões de conteúdo, como faria com uma integração direta do Braze.

No entanto, personalizar quando o Braze SDK é integrado ou especificar as configurações de inicialização é uma tarefa complicada que nem sempre é possível. Isso ocorre porque a Segment inicializa o Braze SDK para você quando a inicialização do Segment ocorre.

{% enddetails %}

{% details Sending deltas to Braze. %}

Ao passar os dados de usuários, verifique se só passa valores para atributos que foram alterados desde a última atualização. Isso garante que você não consuma desnecessariamente pontos da sua cota de dados. Para fontes do lado do cliente, use a ferramenta [middleware](https://github.com/segmentio/segment-braze-mobile-middleware) de código aberto da Segment para otimizar sua integração e limitar o uso de pontos de dados, eliminando chamadas `identify()` da Segment. 

{% enddetails %}



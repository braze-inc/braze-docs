---
nav_title: Visão geral do SDK
article_title: Visão geral do SDK para desenvolvedores
description: "Este artigo de referência sobre integração apresenta uma visão geral técnica para os desenvolvedores do SDK da Braze. Ele discute as análises de dados padrão rastreadas pelo SDK, como bloquear a coleta automática de dados e a versão em tempo real do SDK do app."
page_order: 0
---

# [![Curso do Braze Learning]({% image_buster /assets/img/bl_icon3.png %}](https://learning.braze.com/path/developer/sdk-integration-basics) ){: style="float:right;width:120px;border:0;" class="noimgborder"}Visão geral do SDK para desenvolvedores

> Antes de começar a integrar os SDKs da Braze, você pode se perguntar o que exatamente está desenvolvendo e integrando. Talvez você esteja curioso para saber como pode personalizar o SDK para atender ainda mais às suas necessidades. O objetivo deste artigo é tirar as suas dúvidas sobre o SDK. 

Você é um profissional de marketing e está procurando um resumo básico do SDK? Em vez disso, dê uma olhada em nossa [visão geral para profissionais de marketing]({{site.baseurl}}/user_guide/getting_started/web_sdk/).

Em resumo, o SDK da Braze:
* Coleta e sincroniza dados de usuários em um perfil de usuário consolidado
* Coleta automaticamente dados da sessão, informações do dispositivo e tokens por push
* Captura dados de engajamento de marketing e dados personalizados específicos de sua empresa
* Potencializa as notificações por push, as mensagens no app e os canais de envio de mensagens do cartão de conteúdo

## Performance do app

O Braze não deve ter nenhum impacto negativo sobre a performance do seu app.

Os SDKs da Braze têm um impacto muito pequeno no tamanho do app. Alteramos automaticamente a taxa de envio dos dados do usuário dependendo da qualidade da rede, além de permitir o controle manual da rede. Agrupamos automaticamente as solicitações de API do SDK para garantir que os dados sejam registrados rapidamente, mantendo a máxima eficiência da rede. Por fim, a quantidade de dados enviados do cliente para a Braze em cada chamada de API é extremamente pequena.

## Compatibilidade do SDK

O SDK da Braze foi projetado para ser discreto e não interferir em outros SDKs presentes em seu app. Se estiver enfrentando algum problema que acredite ser devido à incompatibilidade com outro SDK, entre em contato com o suporte da Braze.

## Análise de dados padrão e tratamento de sessões

Certos dados de usuários são coletados automaticamente pelo nosso SDK—por exemplo, Primeiro Uso do App, Último Uso do App, Contagem Total de Sessões, Sistema Operacional do Dispositivo, etc. Se você seguir nossos guias de integração para implementar nossos SDKs, poderá aproveitar esta [coleta de dados padrão]({{site.baseurl}}/user_guide/data/user_data_collection/sdk_data_collection/). Verificar esta lista pode ajudá-lo a evitar armazenar as mesmas informações sobre os usuários mais de uma vez. Com exceção do início e do fim da sessão, todos os outros dados rastreados automaticamente não contam para a sua cota de pontos de dados.

{% alert note %}
Todos os nossos recursos são configuráveis, mas é uma boa ideia implementar completamente o modelo padrão de coleta de dados.

<br>Se necessário para o seu caso de uso, você pode [limitar a coleta de determinados dados](#blocking-data-collection) após a conclusão da integração.
{% endalert %}

## Upload e download de dados

O SDK da Braze armazena dados em cache (sessões, eventos personalizados etc.) e faz upload deles periodicamente. Somente após os dados terem sido enviados, os valores serão atualizados no dashboard. O intervalo de upload leva em consideração o estado do dispositivo e é determinado pela qualidade da conexão de rede:

|Qualidade da conexão de rede |    Intervalo de descarga de dados|
|---|---|
|Excelente    |10 segundos|
|Boa    |30 segundos|
|Ruim    |60 segundos|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Se não houver conexão de rede, os dados serão armazenados em cache localmente no dispositivo até que a conexão de rede seja restabelecida. Quando a conexão for restabelecida, os dados serão enviados para a Braze.

O Braze envia dados para o SDK no início de uma sessão com base nos segmentos em que o usuário se enquadra no momento da sessão. As novas mensagens no app não serão atualizadas durante a sessão. No entanto, os dados de usuários durante a sessão serão processados continuamente à medida que forem enviados pelo cliente. Por exemplo, um usuário desistente (usou o aplicativo pela última vez há mais de 7 dias) ainda receberá conteúdo direcionado a usuários desistentes em sua primeira sessão de volta ao app.

## Bloqueio da coleta de dados

É possível (embora não recomendado) bloquear a coleta automática de determinados dados da sua integração SDK ou permitir processos que façam isso. 

O bloqueio da coleta de dados não é recomendado porque a remoção de dados analíticos reduz a capacidade de personalização e direcionamento da sua plataforma. Por exemplo:

- Se você optar por não integrar completamente a funcionalidade de localização em um dos SDKs, não poderá personalizar suas mensagens com base em idioma ou localização. 
- Se optar por não fazer a integração por fuso horário, talvez não consiga enviar mensagens dentro do fuso horário de um usuário. 
- Se você optar por não integrar informações visuais de um dispositivo específico, o conteúdo da mensagem poderá não ser otimizado para esse dispositivo.

É altamente recomendável integrar completamente os SDKs para aproveitar ao máximo os recursos de nosso produto.

{% tabs %}
{% tab SDK da Web %}

Você pode simplesmente não integrar determinadas partes do SDK ou usar [`disableSDK`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#disablesdk) para um usuário. Esse método sincronizará os dados registrados antes de `disableSDK()` ter sido chamado e fará com que todas as chamadas subsequentes ao Braze Web SDK para essa página e para futuros carregamentos de página sejam ignoradas. Para retomar a coleta de dados, use o método [`enableSDK()`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#enablesdk). Para saber mais, consulte o artigo [Desativação do rastreamento Web]({{site.baseurl}}/developer_guide/analytics/managing_data_collection/?sdktab=web).

{% endtab %}
{% tab SDK para Android %}

Você pode usar [`setDeviceObjectAllowlist`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.configuration/-braze-config/-builder/set-device-object-allowlist.html?query=fun%20setDeviceObjectAllowlist(deviceObjectAllowlist:%20EnumSet%3CDeviceKey%3E):%20BrazeConfig.Builder) para configurar o SDK para enviar apenas um subconjunto de chaves ou valores de objetos do dispositivo de acordo com uma lista de permissões definida. Essa capacitação deve ser ativada via [`setDeviceObjectAllowlistEnabled`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.configuration/-braze-config/-builder/set-device-object-allowlist-enabled.html?query=fun%20setDeviceObjectAllowlistEnabled(enabled:%20Boolean):%20BrazeConfig.Builder).

{% alert important %}
Uma lista de permissão vazia fará com que **nenhum** dado do dispositivo seja enviado ao Braze.
{% endalert %}

{% endtab %}
{% tab Swift SDK %}

Você pode atribuir um conjunto de campos elegíveis a [`configuration.devicePropertyAllowList`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/devicepropertyallowlist) em seu site `Braze.Configuration` para especificar uma lista de permissões para os campos do dispositivo que são coletados pelo SDK. A lista completa de campos está definida em [`Braze.Configuration.DeviceProperty`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/deviceproperty). Para desativar a coleta de todos os campos do dispositivo, defina o valor dessa propriedade como um conjunto vazio (`[]`).

{% alert important %}
Por padrão, todos os campos são coletados pelo Braze Swift SDK. A remoção de algumas propriedades do dispositivo pode desativar os recursos do SDK.
{% endalert %}

Para saber mais, consulte [Armazenamento]({{site.baseurl}}/developer_guide/storage/?tab=swift) na documentação do Swift SDK.

{% endtab %}
{% endtabs %}

## Qual é a versão do SDK que estou usando?

Use o dashboard para ver a versão do SDK de um determinado app em **Configurações > Configurações do app**. A **versão do SDK ativa** exibe a versão mais recente do SDK da Braze usada pelo seu app ativo mais recente para pelo menos 5% dos seus usuários.

![Um app chamado Swifty em um espaço de trabalho. A versão do Live SDK é 6.6.0.]({% image_buster /assets/img/live-sdk-version.png %}){: style="max-width:80%"} 

{% alert tip %}
Se você tiver um app iOS, confirme se está usando o [Swift SDK]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=swift) em vez do antigo [Objective-C iOS SDK]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/overview/) se a **Versão do Live SDK** for igual ou superior a 5.0.0, que foi a primeira versão lançada do Swift SDK.
{% endalert %}


---
nav_title: Coleta de dados do SDK
article_title: Coleta de Dados do SDK
page_order: 1
page_type: reference
description: "Este artigo de referência aborda os dados que são coletados pelo SDK através de uma integração personalizada, integração coletada automaticamente e integração mínima."

---

# Coleta de dados do SDK

> Quando você integra o SDK da Braze com seu aplicativo ou site, a Braze coleta automaticamente certos tipos de dados. Alguns desses dados são essenciais para nossos processos e alguns desses dados podem ser ativados ou desativados com base em suas necessidades. Você também pode configurar a Braze para coletar tipos adicionais de dados para potencializar ainda mais sua segmentação e mensagens.

A Braze é projetada para permitir uma coleta de dados flexível, para que você possa integrar o SDK da Braze das seguintes maneiras:

- **[Integração mínima](#minimum-integration):** A Braze coleta automaticamente dados que são necessários para se comunicar com os serviços da Braze.
- **[Dados opcionais coletados por padrão](#optional-data-collected-by-default):** A Braze captura automaticamente alguns dados que são amplamente úteis para a maioria dos seus casos de uso. Você pode optar por desativar a coleta automática desses dados se não forem essenciais para a comunicação com os serviços da Braze.
- **[Dados opcionais não coletados por padrão](#data-not-collected-by-default):** A Braze captura alguns dados que são úteis para certos casos de uso e não ativa automaticamente a coleta por razões de conformidade ampla. Você pode optar por coletar esses dados onde for adequado para seus casos de uso.
- **[Integração personalizada](#personalized-integration):** A Braze oferece a flexibilidade de coletar dados além dos dados opcionais padrão.

## Integração mínima

A seguir, lista os dados estritamente necessários gerados e recebidos pela Braze quando você inicializa o SDK. Esses dados não são configuráveis e são essenciais nas funções principais da plataforma. Exceto pelo início e fim da sessão, todos os outros dados rastreados automaticamente não contam para o uso de pontos de dados.

| Atributo | Descrição | Por que é coletado |
| --------- | ----------- | ------------------ |
| Nome da versão do aplicativo /<br> Código da versão do aplicativo | A versão mais recente do aplicativo | Este atributo é usado para enviar mensagens relacionadas à compatibilidade da versão do aplicativo para os dispositivos corretos. Pode ser usado para notificar os usuários sobre interrupções de serviço ou bugs. |
| País | País identificado pela geolocalização do endereço IP. Se a geolocalização do endereço IP não estiver disponível, isso é identificado pela [localização do dispositivo](#optional-data-collected-by-default). O valor pode ser alternativamente o que os SDKs definem diretamente com `setCountry`, mas note que passar um valor de atributo por SDK ou API registrará pontos de dados.| Este atributo é usado para direcionar mensagens com base na localização. |
| ID do dispositivo | Identificador do dispositivo, uma string gerada aleatoriamente | Este atributo é usado para diferenciar os dispositivos dos usuários e enviar mensagens para o dispositivo correto. |
| SO e versão do SO | Dispositivo ou navegador atualmente relatado e versão do dispositivo ou navegador | Este atributo é usado para enviar mensagens apenas para dispositivos compatíveis. Ele também pode ser usado dentro da segmentação para direcionar usuários a atualizar versões do aplicativo. |
| Início da sessão e fim da sessão | Quando o usuário começa a usar seu aplicativo ou site integrado | O SDK do Braze relata dados de sessão usados pelo painel do Braze para calcular o engajamento do usuário e outras análises essenciais para entender seus usuários. Exatamente quando o início da sessão e o fim da sessão são chamados pelo seu aplicativo ou site é configurável por um desenvolvedor ([Android]({{site.baseurl}}/developer_guide/analytics/tracking_sessions/?tab=android), [iOS]({{site.baseurl}}/developer_guide/analytics/tracking_sessions/?tab=swift), [Web]({{site.baseurl}}/developer_guide/analytics/tracking_sessions/?tab=web)). |
| Dados de interação de mensagens do SDK | Aberturas diretas de push, interações de mensagens no aplicativo, interações de Cartões de Conteúdo | Este atributo é usado para fins de controle de qualidade, como verificar se uma mensagem foi recebida e se o envio não está duplicado. |
| Versão do SDK | Versão atual do SDK | Este atributo é usado para enviar mensagens apenas para dispositivos compatíveis e evitar interrupções no serviço. |
| ID da sessão e timestamp da sessão | Identificador da sessão, uma string gerada aleatoriamente e timestamp da sessão | Usado para determinar se o usuário está iniciando uma nova sessão ou uma sessão existente e para determinar a re-eligibilidade de mensagens destinadas a este usuário.<br><br>Certos canais de mensagens, como mensagens no aplicativo e Cartões de Conteúdo, são sincronizados com o dispositivo no início da sessão. Nosso backend usará então dados relacionados a quando contatou pela última vez os servidores do Braze (que o dispositivo armazena e envia de volta) para saber se o usuário é elegível para novas mensagens.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

### Métricas calculadas

O Braze gera métricas calculadas com base em dados do SDK, dados de interação de mensagens relacionadas a mensagens não-SDK e informações derivadas. Para clareza, esses dados calculados não são rastreados pelo SDK, mas gerados pelos serviços do Braze, e um perfil de usuário exibirá tanto dados rastreados quanto dados gerados. 

Métricas calculadas incluem os seguintes atributos.

| Atributo                                      | Descrição                                                          |
|-----------------------------------------------|----------------------------------------------------------------------|
| Aplicativo usado pela primeira vez                                 | Tempo                                                                 |
| Último aplicativo usado                                  | Tempo                                                                 |
| Contagem total de sessões                            | Número                                                               |
| Cartão clicado                                   | Número                                                               |
| Última mensagem recebida                     | Tempo                                                                 |
| Última campanha de email recebida                   | Tempo                                                                 |
| Última campanha de push recebida                    | Tempo                                                                 |
| Número de itens de feedback                       | Número                                                               |
| Número de sessões nos últimos Y dias          | Número e hora                                                      |
| Mensagem recebida da campanha                  | Booleano. Este filtro visa usuários com base em se eles receberam uma campanha anterior.                               |
| Mensagem recebida da campanha com tag        | Booleano. Este filtro visa usuários com base em se eles receberam uma campanha que atualmente tem uma tag.                  |
| Campanha de retargeting                              | Booleano. Este filtro visa usuários com base em se eles abriram ou clicaram em um email específico, push ou mensagem no aplicativo no passado. |
| Desinstalado                                    | Booleano e tempo |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

{% alert important %}
Se você estiver interessado apenas na integração mínima, e integrar com mParticle, Segment, Tealium ou GTM, observe o seguinte:
- **Plataformas móveis**: Você deve atualizar manualmente o código para essas configurações. mParticle e Segment não oferecem uma maneira de fazer isso através de sua plataforma. 
- **Web**: A integração com Braze deve ser feita de forma nativa para permitir a configuração de integração mínima. Os gerenciadores de tags não oferecem uma maneira de fazer isso através de sua plataforma.
{% endalert %} 

## Dados opcionais coletados por padrão

Além dos dados de integração mínima, os seguintes atributos são capturados automaticamente pelo Braze quando você inicializa a integração do SDK. Você pode [optar por não participar]({{site.baseurl}}/developer_guide/platform_integration_guides/sdk_primer/#blocking-data-collection) da coleta desses atributos para permitir uma integração mínima.

| Atributo               | Plataforma          | Descrição                                                                        | Por que é coletado                                                                                                                                                      |
|-------------------------|-------------------|------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Nome do navegador            | Web               | Nome do navegador                                                                | Este atributo é usado para enviar mensagens apenas para navegadores compatíveis. Ele também pode ser usado para segmentação baseada em navegador.                                     |
| Localidade do dispositivo           | Android, iOS      | O local padrão do dispositivo                                                   | Este atributo é usado para traduzir mensagens para o idioma preferido do usuário.                                                                                            |
| Local mais recente do dispositivo           | Android, iOS      | O local padrão mais recente do dispositivo                                                   | Este atributo vem das configurações do dispositivo do usuário e é usado para traduzir mensagens para o idioma preferido do usuário. É independente do atributo `Most Recent Location`.                                                                                            |
| Modelo do dispositivo            | Android, iOS      | O hardware específico do dispositivo                                                | Este atributo é usado para enviar mensagens apenas para dispositivos compatíveis. Também pode ser usado dentro da segmentação.                                                 |
| Marca do dispositivo            | Android           | A marca do dispositivo (por exemplo, Samsung)                                         | Este atributo é usado para enviar mensagens apenas para dispositivos compatíveis.                                                                                          |
| Operadora de telefonia do dispositivo | Android, iOS      | A operadora móvel                                                                 | Este atributo é opcionalmente usado para direcionamento de mensagens.<br><br>**Nota:** Este campo foi descontinuado a partir do iOS 16 e será definido como `--` em uma versão futura do iOS. |
| Idioma                | Android, iOS, Web | Idioma do dispositivo ou do navegador, retirado do local do dispositivo                                                            | Este atributo é usado para traduzir mensagens para o idioma preferido do usuário. É baseado na localidade do dispositivo.                                                                                            |
| Configurações de notificação   | Android, iOS, Web | Se este aplicativo tem notificações push habilitadas.                                   | Este atributo é usado para habilitar notificações push.                                                                                                                    |
| Resolução              | Android, iOS, Web | Resolução do dispositivo ou do navegador                                                          | Opcionalmente usado para direcionamento de mensagens baseado no dispositivo. O formato deste valor é "`<width>`x`<height>`".                                                                 |
| Fuso horário               | Android, iOS, Web | Fuso horário do dispositivo ou do navegador                                                           | Este atributo é usado para enviar mensagens no momento apropriado, de acordo com o fuso horário local de cada usuário.                                                   |
| Agente do usuário              | Web               | [Agente do usuário](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/User-Agent) | Este atributo é usado para enviar mensagens apenas para dispositivos compatíveis. Também pode ser usado dentro da segmentação.                                                 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

Para saber mais sobre como rastrear propriedades em nível de dispositivo (como operadora de celular do dispositivo, fuso horário, resolução e outros), consulte a documentação específica da plataforma: [Android]({{site.baseurl}}/developer_guide/storage/?tab=android), [iOS]({{site.baseurl}}/developer_guide/storage/?tab=swift), [Web]({{site.baseurl}}/developer_guide/storage/#cookies).

## Dados não coletados por padrão

Por padrão, os seguintes atributos não são coletados. Cada atributo precisa ser integrado manualmente.

| Atributo                  | Plataforma     | Descrição                                                                                                                                                                                                                                                                                                               | Por que não é coletado                                                                                                                                                                                                                                                                 |
|----------------------------|--------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Rastreamento de anúncios do dispositivo ativado | Android, iOS | No iOS:<br>[`set(adTrackingEnabled:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/set(adtrackingenabled:))<br><br>No Android:<br>[`Braze.setGoogleAdvertisingId()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/set-google-advertising-id.html) | Esta propriedade requer permissões adicionais em nível de aplicativo, que devem ser concedidas pelo integrador.                                                                                                                                                                                      |
| IDFA do dispositivo                | iOS          | Identificador do dispositivo para anunciantes                                                                                                                                                                                                                                                                                         | Isso requer o framework de Transparência de Rastreamento de Anúncios, que acionará uma revisão adicional de privacidade da App Store. Para mais detalhes, veja [`set(identifierForAdvertiser:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/set(identifierforadvertiser:)) |
| ID de Publicidade do Google      | Android      | Identificador para publicidade dentro dos aplicativos do Google Play                                                                                                                                                                                                                                                                        | Isso requer que o aplicativo recupere o GAID e o passe para o Braze. Para mais detalhes, consulte [ID de Publicidade do Google Opcional]({{site.baseurl}}/developer_guide/platform_integration_guides/android/sdk_integration#google-advertising-id).                                         |
| Localização mais recente | Android, iOS | Esta é a última localização GPS conhecida do dispositivo do usuário. Isso é atualizado no início da sessão e é armazenado no perfil do usuário. | Isso requer que o usuário conceda permissão de localização ao seu aplicativo. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

{% alert note %}
O SDK do Braze não armazena endereços IP localmente.
{% endalert %}

## Integração personalizada

Para aproveitar ao máximo o Braze, nossos integradores de SDK costumam implementar os SDKs do Braze e registrar [atributos personalizados]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#setting-custom-attributes), [eventos personalizados]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#logging-custom-events) e [eventos de compra]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/purchase_events/#logging-purchase-events) que são pertinentes ao seu negócio, além dos dados coletados automaticamente.

Uma integração personalizada permite uma comunicação customizada que é relevante para a experiência dos seus usuários.

{% alert important %}
O Braze banirá ou bloqueará usuários com mais de 5.000.000 sessões ("usuários fictícios") e não ingerirá mais seus eventos de SDK. Para mais informações, consulte [Bloqueio de spam]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_archival/#spam-blocking).
{% endalert %}



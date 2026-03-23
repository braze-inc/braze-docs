---
nav_title: Coleta de dados do SDK
article_title: Coleta de dados do SDK
page_order: 1
page_type: reference
description: "Este artigo de referência aborda os dados que são coletados pelo SDK por meio de uma integração personalizada, integração coletada automaticamente e integração mínima."

---

# Coleta de dados do SDK

> Quando você integra o SDK da Braze com seu app ou site, a Braze coleta automaticamente certos tipos de dados. Alguns desses dados são essenciais para nossos processos e outros podem ser ativados ou desativados de acordo com suas necessidades. Você também pode configurar a Braze para coletar tipos adicionais de dados para aprimorar ainda mais sua segmentação e envio de mensagens.

A Braze foi projetada para permitir a coleta flexível de dados, portanto, você pode integrar o SDK da Braze das seguintes maneiras:

- **[Integração mínima](#minimum-integration):** A Braze coleta automaticamente os dados necessários para a comunicação com os serviços da Braze.
- **[Dados opcionais coletados por padrão](#optional-data-collected-by-default):** A Braze captura automaticamente alguns dados que são amplamente úteis para a maioria dos seus casos de uso. Você pode optar por desativar a coleta automática desses dados se eles não forem essenciais para a comunicação com os serviços da Braze.
- **[Dados opcionais não coletados por padrão](#data-not-collected-by-default):** A Braze captura alguns dados que são úteis para determinados casos de uso e não ativa automaticamente a coleta por motivos de ampla conformidade. Você pode optar por coletar esses dados onde for mais adequado aos seus casos de uso.
- **[Integração personalizada](#personalized-integration):** A Braze oferece a flexibilidade de coletar dados além dos dados opcionais padrão.

## Integração mínima

A seguir, listamos os dados estritamente necessários gerados e recebidos pela Braze quando você inicializa o SDK. Esses dados não são configuráveis e são essenciais para as principais funções da plataforma. Exceto pelo início e fim da sessão, todos os outros dados rastreados automaticamente não contam para o uso de pontos de dados.

| Atributo | Descrição | Por que é coletado |
| --------- | ----------- | ------------------ |
| App-Version-Name /<br> App-Version-Code | A versão mais recente do app | Esse atributo é usado para enviar mensagens relacionadas à compatibilidade da versão do app para os dispositivos corretos. Ele pode ser usado para notificar os usuários sobre interrupções ou bugs no serviço. |
| País | País identificado pela geolocalização do endereço IP. Se a geolocalização do endereço IP não estiver disponível, isso é identificado pelo [local do dispositivo](#optional-data-collected-by-default). O valor pode ser alternativamente o que os SDKs definem diretamente com `setCountry`, mas note que passar um valor de atributo por SDK ou API registrará pontos de dados. **Depois que o país for definido manualmente (pelo método do SDK, API REST ou upload de CSV), o SDK não atualizará mais esse valor automaticamente.**| Esse atributo é usado para direcionar mensagens com base na localização. |
| ID do dispositivo | Identificador do dispositivo, uma string gerada aleatoriamente | Esse atributo é usado para diferenciar os dispositivos dos usuários e enviar mensagens para o dispositivo correto. |
| Sistema operacional e versão do sistema operacional | Dispositivo ou navegador relatado atualmente e versão do dispositivo ou navegador | Esse atributo é usado para enviar mensagens apenas para dispositivos compatíveis. Também pode ser usado dentro da segmentação para direcionar os usuários a fazer upgrade das versões do app. |
| Início da sessão e fim da sessão | Quando o usuário começa a usar seu app ou site integrado | O SDK da Braze relata dados de sessão usados pelo dashboard da Braze para calcular o engajamento do usuário e outras análises de dados essenciais para entender seus usuários. O momento exato em que o início e o fim da sessão são chamados pelo seu app ou site é configurável por um desenvolvedor ([Android]({{site.baseurl}}/developer_guide/analytics/tracking_sessions/?tab=android), [iOS]({{site.baseurl}}/developer_guide/analytics/tracking_sessions/?tab=swift), [Web]({{site.baseurl}}/developer_guide/analytics/tracking_sessions/?tab=web)). |
| Dados de interação de mensagem do SDK | Aberturas diretas de push, interações de mensagem no app, interações de cartão de conteúdo | Esse atributo é usado para fins de controle de qualidade, como verificar se uma mensagem foi recebida e se o envio não está duplicado. |
| Versão do SDK | Versão atual do SDK | Esse atributo é usado para enviar mensagens apenas para dispositivos compatíveis e evitar a interrupção do serviço. |
| ID da sessão e timestamp da sessão | Identificador da sessão, uma string gerada aleatoriamente e timestamp da sessão | Usado para determinar se o usuário está iniciando uma nova sessão ou uma sessão existente e para determinar a reelegibilidade das mensagens destinadas a este usuário.<br><br>Certos canais de envio de mensagens, como mensagens no app e Cartões de conteúdo, são sincronizados com o dispositivo ao iniciar a sessão. Nosso backend usará então dados relacionados a quando ele contatou os servidores da Braze pela última vez (que o dispositivo armazena e envia de volta) para saber se o usuário é elegível para novas mensagens.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

### Métricas calculadas

A Braze gera métricas calculadas com base em dados do SDK, dados de interação de mensagens relacionados a mensagens que não são do SDK e informações derivadas. Para maior clareza, esses dados calculados não são rastreados pelo SDK, mas gerados pelos serviços da Braze, e um perfil de usuário exibirá tanto os dados rastreados quanto os dados gerados. 

As métricas calculadas incluem os seguintes atributos.

| Atributo                                      | Descrição                                                          |
|-----------------------------------------------|----------------------------------------------------------------------|
| Usou o app pela primeira vez                                 | Horário                                                                 |
| Usou o app pela última vez                                  | Horário                                                                 |
| Contagem total de sessões                            | Número                                                               |
| Clicou no cartão                                   | Número                                                               |
| Última mensagem recebida                     | Horário                                                                 |
| Última campanha de e-mail recebida                   | Horário                                                                 |
| Última campanha de push recebida                    | Horário                                                                 |
| Número de itens de feedback                       | Número                                                               |
| Número de sessões nos últimos Y dias          | Número e tempo                                                      |
| Mensagem recebida da campanha                  | Booleano. Esse filtro direciona os usuários com base no fato de terem recebido uma campanha anterior.                               |
| Mensagem recebida da campanha com tag        | Booleano. Esse filtro direciona os usuários com base no fato de terem recebido uma campanha que atualmente tem uma tag.                  |
| Redirecionar campanha                              | Booleano. Esse filtro direciona os usuários com base no fato de terem aberto ou clicado em um e-mail, push ou mensagem no app específico no passado. |
| Desinstalou                                    | Booleano e tempo |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

{% alert important %}
Se estiver interessado apenas na integração mínima e fizer a integração com mParticle, Segment, Tealium ou GTM, observe o seguinte:
- **Plataformas móveis**: Você deve atualizar manualmente o código para essas configurações. O mParticle e o Segment não oferecem uma maneira de fazer isso por meio de suas plataformas. 
- **Web**: A integração com a Braze deve ser feita nativamente para permitir a configuração mínima de integração. Os gerenciadores de tags não oferecem uma maneira de fazer isso por meio de sua plataforma. 
{% endalert %} 

## Dados opcionais coletados por padrão

Além dos dados mínimos de integração, os seguintes atributos são capturados automaticamente pela Braze quando você inicializa a integração do SDK. É possível [desativar]({{site.baseurl}}/developer_guide/platform_integration_guides/sdk_primer/#blocking-data-collection) a coleta desses atributos para permitir uma integração mínima.

| Atributo               | Plataforma          | Descrição                                                                        | Por que é coletado                                                                                                                                                      |
|-------------------------|-------------------|------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Nome do navegador            | Web               | Nome do navegador                                                                | Esse atributo é usado para enviar mensagens apenas para navegadores compatíveis. Também pode ser usado para segmentação baseada em navegador.                                     |
| Local do dispositivo           | Android, iOS      | O local padrão do dispositivo                                                   | Esse atributo é usado para traduzir mensagens para o idioma preferido do usuário.                                                                                            |
| Local mais recente do dispositivo           | Android, iOS      | O local padrão mais recente do dispositivo                                                   | Esse atributo vem das configurações do dispositivo do usuário e é usado para traduzir mensagens para o idioma preferido do usuário. É independente do atributo `Most Recent Location`.                                                                                            |
| Modelo do dispositivo            | Android, iOS      | O hardware específico do dispositivo                                                | Esse atributo é usado para enviar mensagens apenas para dispositivos compatíveis. Também pode ser usado dentro da segmentação.                                                 |
| Marca do dispositivo            | Android           | A marca do dispositivo (por exemplo, Samsung)                                         | Esse atributo é usado para enviar mensagens apenas para dispositivos compatíveis.                                                                                          |
| Operadora sem fio do dispositivo | Android, iOS      | A operadora móvel                                                                 | Esse atributo é opcionalmente usado para direcionamento de mensagens.<br><br>**Nota:** Este campo foi descontinuado a partir do iOS 16 e será definido como `--` em uma versão futura do iOS. |
| Idioma                | Android, iOS, Web | Idioma do dispositivo ou do navegador, obtido do local do dispositivo.                                                           | Esse atributo é usado para traduzir mensagens para o idioma preferido do usuário. É baseado no local do dispositivo.                                                                                            |
| Configurações de notificação   | Android, iOS, Web | Se este app tem notificações por push ativadas.                                   | Esse atributo é usado para ativar notificações por push.                                                                                                                    |
| Resolução              | Android, iOS, Web | Resolução do dispositivo ou do navegador                                                          | Opcionalmente usado para direcionamento de mensagens baseado em dispositivo. O formato deste valor é "`<width>`x`<height>`".                                                                 |
| Fuso horário               | Android, iOS, Web | Fuso horário do dispositivo ou do navegador                                                           | Esse atributo é usado para enviar mensagens no horário apropriado, de acordo com o horário local de cada usuário.                                                   |
| Agente do usuário              | Web               | [Agente do usuário](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/User-Agent) | Esse atributo é usado para enviar mensagens apenas para dispositivos compatíveis. Também pode ser usado dentro da segmentação.                                                 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

Para saber mais sobre o rastreamento de propriedades em nível de dispositivo (como operadora sem fio do dispositivo, fuso horário, resolução e outros), consulte a documentação específica da plataforma: [Android]({{site.baseurl}}/developer_guide/storage/?tab=android), [iOS]({{site.baseurl}}/developer_guide/storage/?tab=swift), [Web]({{site.baseurl}}/developer_guide/storage/#cookies).

## Dados não coletados por padrão

Por padrão, os seguintes atributos não são coletados. Cada atributo precisa ser integrado manualmente.

| Atributo                  | Plataforma     | Descrição                                                                                                                                                                                                                                                                                                               | Por que não é coletado                                                                                                                                                                                                                                                                 |
|----------------------------|--------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Rastreamento de anúncios no dispositivo ativado | Android, iOS | No iOS:<br>[`set(adTrackingEnabled:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/set(adtrackingenabled:))<br><br>No Android:<br>[`Braze.setGoogleAdvertisingId()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/set-google-advertising-id.html) | Essa propriedade requer permissões adicionais em nível de app, que devem ser concedidas pelo integrador.                                                                                                                                                                                      |
| IDFA do dispositivo                | iOS          | Identificador de dispositivo para anunciantes                                                                                                                                                                                                                                                                                         | Isso requer o framework de Transparência de Rastreamento de Anúncios, que disparará uma revisão adicional de privacidade da App Store. Para mais detalhes, veja [`set(identifierForAdvertiser:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/set(identifierforadvertiser:)) |
| ID de publicidade do Google      | Android      | Identificador para publicidade em apps do Google Play                                                                                                                                                                                                                                                                        | Isso requer que o app recupere o GAID e o passe para a Braze. Para mais detalhes, consulte [ID de publicidade opcional do Google]({{site.baseurl}}/developer_guide/platform_integration_guides/android/sdk_integration#google-advertising-id).                                         |
| Local mais recente | Android, iOS | Esta é a última localização GPS conhecida do dispositivo do usuário. Isso é atualizado no início da sessão e é armazenado no perfil do usuário. | Isso requer que o usuário conceda permissão de localização ao seu app. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

{% alert note %}
O SDK da Braze não armazena endereços IP localmente.
{% endalert %}

## Integração personalizada

Para aproveitar ao máximo a Braze, nossos integradores de SDK geralmente implementam os SDKs da Braze e registram [atributos personalizados]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#setting-custom-attributes), [eventos personalizados]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#logging-custom-events) e [eventos de compra]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/purchase_events/#logging-purchase-events) que são pertinentes aos seus negócios, além dos dados coletados automaticamente.

Uma integração personalizada permite uma comunicação personalizada que é relevante para a experiência dos seus usuários.

{% alert important %}
A Braze banirá ou bloqueará os usuários com mais de 5.000.000 de sessões ("usuários fictícios") e não mais ingerirá seus eventos de SDK. Para saber mais, consulte [Bloqueio de spam]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_archival/#spam-blocking).
{% endalert %}
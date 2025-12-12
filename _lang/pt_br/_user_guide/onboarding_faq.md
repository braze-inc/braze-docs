---
article_title: PERGUNTAS FREQUENTES
hidden: true
permalink: /onboarding_faq/
excerpt_separator: ""
page_type: glossary
layout: onboarding_faq
description: "Esta página contém uma coleção de perguntas frequentes, descritas por categoria."

---

{% multi_lang_include video.html id="keAZAlBR9zc" source="youtube" %}


<!--- Users --->

{% api %}

### Como lido com dados anônimos de usuários?

{% apitags %}
Usuários
{% endapitags %}

Inicialmente, quando um perfil de usuário é reconhecido por meio do SDK, o Braze cria um perfil de usuário anônimo com um `braze_id` associado: um identificador de usuário exclusivo que é definido pelo Braze.

Para controlar ainda mais os usuários anônimos, é possível implementar [aliases de usuário]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle#user-aliases) que permitem marcar usuários anônimos com um identificador. Esses usuários podem então ser exportados usando seus aliases ou referenciados pela API.

Se um perfil de usuário anônimo com um alias for reconhecido posteriormente com um `external_id`, ele será tratado como um perfil de usuário identificado normal, mas manterá o alias existente e ainda poderá ser referenciado por esse alias.

Para usuários de alias que você deseja mesclar com usuários identificados, é possível mesclar quaisquer campos que sejam pertinentes ao perfil real que você deseja manter. Você teria que exportar esses dados antes de excluí-los do perfil de alias usando nosso [ponto de extremidade Exportar perfil de usuário por identificador]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/). Em seguida, você pode usar nosso [ponto de extremidade Rastrear usuários]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) para publicar esses eventos no perfil que você manteve. Isso preservará todos os dados que você deseja manter, como atributos que foram registrados anteriormente em um perfil, mas não no outro.

Para obter um detalhamento completo dos diferentes métodos de coleta de dados de usuários novos e existentes no Braze, consulte [as práticas recomendadas de coleta de dados]({{site.baseurl}}/user_guide/data/user_data_collection/best_practices/).

{% endapi %}
{% api %}

### Como posso importar usuários que já coletei e identifiquei fora do Braze?

{% apitags %}
Usuários
{% endapitags %}

Para importar usuários identificados anteriormente, você pode carregar um CSV no Braze ou enviar dados por meio da API.

#### CSV

Você pode carregar e atualizar perfis de usuários por meio de arquivos CSV em **Audience** > **Import Users**. Ao importar os dados de seus clientes, você precisará especificar o identificador exclusivo de cada cliente, também conhecido como `external_id`.

Antes de iniciar a importação do CSV, é importante que a equipe de engenharia entenda como os usuários serão identificados no Braze. Normalmente, esse seria um ID de banco de dados usado internamente. Isso deve estar alinhado com a forma como os usuários serão identificados pelo Braze SDK no celular e na Web, de modo que cada cliente tenha um único perfil de usuário no Braze em todos os seus dispositivos. Saiba mais sobre o [ciclo de vida do perfil de usuário]({{site.baseurl}}/user_guide/data/user_data_collection/user_profile_lifecycle/) Braze.

Quando você fornecer um `external_id` em sua importação, o Braze atualizará qualquer usuário existente com o mesmo `external_id` ou criará um usuário recém-identificado com esse conjunto `external_id`, caso não seja encontrado um.

Para obter mais informações e fazer download de modelos de importação de CSV, consulte [importação de usuários]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import/#csv).

#### API

Para carregar usuários via API, você pode usar nosso [endpoint Track users]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) para importá-los para o Braze.

Se você não tiver certeza de que o usuário já existe no Braze, poderá implementar nosso [endpoint Exportar perfil de usuário por identificador]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/) para verificar. Se você identificar que o usuário já existe no Braze, poderá usar nosso endpoint `/users/track` para publicar os novos dados que deseja adicionar ao perfil do usuário que já existe no Braze.

{% alert note %}
Tenha em mente as seguintes nuances ao usar o endpoint `/users/track`:

- Ao criar usuários somente de alias por meio desse endpoint, você deve definir explicitamente o sinalizador `_update_existing_only` como false.
- A atualização do status da assinatura com esse ponto de extremidade atualizará o usuário especificado pela ID externa (como User1) e atualizará o status da assinatura de todos os usuários com o mesmo e-mail desse usuário (User1).
{% endalert %}

{% endapi %}
{% api %}

### Qual é a diferença entre os status das assinaturas push?

{% apitags %}
Usuários
{% endapitags %}

Há três opções de estado de assinatura push: assinada, opt-in e cancelada.

Por padrão, para que o usuário receba suas mensagens por push, o estado da assinatura de push dele deve ser inscrito ou aceito, e ele deve estar habilitado para push. Você pode substituir essa configuração, se necessário, ao redigir uma mensagem.

|Estado de adesão|Descrição|
|---|---|
|Assinatura| Estado padrão da assinatura push quando um perfil de usuário é criado no Braze. |
|Opção de adesão| Um usuário expressou explicitamente sua preferência por receber notificações por push. O Braze moverá automaticamente o estado de aceitação de um usuário para `Opted-In` se ele aceitar um prompt push no nível do sistema operacional.<br><br>Isso não se aplica a usuários do Android 12 ou inferior.|
|Cancelamento da inscrição| Um usuário cancelou explicitamente a assinatura do push por meio do seu aplicativo ou de outros métodos fornecidos pela sua marca. Por padrão, as campanhas push do Braze têm como alvo apenas os usuários que são `Subscribed` ou `Opted-in` para push.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endapi %}
{% api %}

### E se eu tiver identificado usuários duplicados?

{% apitags %}
Usuários
{% endapitags %}

Se tiver identificado usuários duplicados, será necessário limpar esses perfis de usuário. Você pode fazer isso por meio das etapas a seguir:

1. Exporte os perfis de usuário usando nosso ponto de extremidade `/users/export/ids`.
2. Identifique o perfil correto do usuário (em última análise, sua equipe precisará decidir sobre as informações corretas) e também:
    - Mescle todos os campos que sejam pertinentes ao perfil real que você deseja manter usando o ponto de extremidade `/user/track`.
    - Exclua o perfil duplicado e não útil sem mesclar nenhum dado usando o ponto de extremidade users/delete. Depois de excluir um perfil de usuário, **não há como recuperar as informações**.

{% alert important %}
Recomendamos que você importe primeiro os novos perfis de usuário com o endereço `external_id` correto e os atributos e eventos personalizados correspondentes. Depois que os perfis de usuário são excluídos, eles não podem ser recuperados, portanto, a exclusão deve ser a última etapa.
{% endalert %}

Alguns aspectos adicionais a serem observados:

- Todos os dados de engajamento (como campanhas ou Canvases recebidos) em perfis de usuários duplicados serão perdidos. A única maneira de manter o contexto histórico de engajamento é adicionando-o como um atributo personalizado (como um atributo personalizado de matriz de todas as campanhas ou Canvases recebidos).
- Ao migrar perfis de usuário, também cabe à sua equipe decidir qual perfil de usuário das duplicatas será mantido. A Braze não pode decidir ou fornecer a você uma lista de perfis a serem excluídos.  
- Por fim, será importante que a sua equipe avalie o processo de inscrição a partir da experiência dos usuários e certifique-se de chamar o método `changeUser()` somente quando um usuário for identificado.

{% endapi %}
{% api %}

<!-- Segments -->

### Como faço para criar um segmento quando importo um grupo de usuários por meio de CSV?

{% apitags %}
Segmentos
{% endapitags %}

Para importar o arquivo CSV, navegue até a página **User Import (Importação de usuário** ) na seção Users (Usuários). A tabela **Recent Imports (Importações recentes** ) lista até vinte de suas importações mais recentes, seus nomes de arquivo, número de linhas no arquivo, número de linhas importadas com sucesso, total de linhas em cada arquivo e o status de cada importação.

O painel **Importar CSV** contém instruções de importação e um botão para iniciar a importação. Clique em **Select CSV File (Selecionar arquivo CSV** ) e selecione o arquivo de seu interesse. Em seguida, antes de clicar em **Start Import (Iniciar importação)**, você tem a opção de informar ao Braze o que fazer com essa lista em "What do you want us to do with the users in this CSV" (O que você quer que façamos com os usuários neste CSV).

Selecione **Importar usuários neste CSV e também possibilite redirecionar esse lote específico de usuários como um grupo** e, em seguida, selecione **Gerar automaticamente um segmento a partir dos usuários que são importados desse CSV**. Depois que você clicar em **Start Import**, o Braze fará o upload do arquivo, verificará os cabeçalhos das colunas e os tipos de dados de cada coluna e criará um segmento.

Para fazer download de um modelo CSV, consulte a [importação de usuários]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import/#csv).

{% endapi %}
{% api %}

### Que tipos de filtros posso usar ao criar um segmento?

{% apitags %}
Segmentos
{% endapitags %}

O Braze SDK oferece um poderoso arsenal de filtros para segmentar e direcionar seus usuários com base em recursos e atributos específicos. Você pode usar o glossário [Segmentation Filters (Filtros de segmentação]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters) ) para pesquisar ou restringir esses filtros por Categoria de filtro (Dados personalizados, Atividade do usuário, Retargeting, Atividade de marketing, Atributos do usuário, Atribuição de instalação, Atividade social, Testes, Outros).

{% endapi %}
{% api %}

### Como configuro a segmentação por local para que eu possa segmentar os usuários pelo local mais recente e usá-lo em minhas campanhas e estratégias baseadas em local?

{% apitags %}
Segmentos
{% endapitags %}

Navegue até a página **Segments (Segmentos** ), em Engagement (Envolvimento), para visualizar todos os seus segmentos de usuários atuais. Nessa página, você pode criar e nomear novos segmentos. Para começar, clique em **Create Segment (Criar segmento** ) e dê um nome ao seu segmento.

Depois de criar seu segmento, adicione um filtro `Most Recent Location` para segmentar os usuários pelo último local em que eles usaram seu aplicativo. É possível destacar os usuários em uma região circular padrão ou criar uma região poligonal personalizada.

- Para regiões circulares, você pode mover a origem e ajustar o raio de localização para sua segmentação.
- Para regiões poligonais, você pode designar mais especificamente quais áreas deseja incluir no seu segmento.

{% alert tip %}
Interessado em aproveitar as vantagens da segmentação por local com a ajuda de um parceiro Braze? Confira nossos [parceiros de localização contextual]({{site.baseurl}}/partners/message_personalization/) Braze disponíveis.
{% endalert %}

{% endapi %}
{% api %}

### Como posso direcionar listas precisas de usuários com base em seu evento personalizado e comportamento de compra nos últimos 365 dias?

{% apitags %}
Segmentos
{% endapitags %}

Você pode usar [as Extensões de Segmento]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/)! As Extensões de Segmento permitem segmentar uma lista mais precisa de usuários do que seria possível com um segmento regular.

Você pode criar até 10 Extensões de Segmento por espaço de trabalho. Depois que essas listas de extensão são geradas, elas podem ser incluídas ou excluídas como um filtro em seus segmentos. Ao criar uma extensão de segmento, você também pode especificar que a lista seja gerada novamente a cada 24 horas.

1. Em Engagements (Compromissos), expanda **Segments (Segmentos** ) e clique em **Segment Extension (Extensão de segmento**).
2. Na tabela Segment Extensions (Extensões de segmento), clique em **\+ Create New Extension (Criar nova extensão**).
3. Nomeie sua extensão de segmento descrevendo o tipo de usuários que pretende filtrar. Isso garantirá que essa extensão possa ser descoberta com facilidade e precisão ao aplicá-la como um filtro em seu segmento.
4. Selecione entre uma compra ou critérios de eventos personalizados para segmentação.
5. Escolha qual item comprado ou evento personalizado específico você deseja segmentar para sua lista de usuários. 
6. Escolha quantas vezes (mais do que, menos do que ou igual a) o usuário precisaria ter concluído o evento e quantos dias para olhar para trás, até 365 dias.

Para aumentar a precisão da segmentação, você pode selecionar **Add Property Filters (Adicionar filtros de propriedade** ) e segmentar com base nas propriedades específicas de sua compra ou evento personalizado. O Braze oferece suporte à segmentação de propriedades de eventos com base em objetos string, numéricos, booleanos e de tempo.

Também oferecemos suporte à segmentação com base em [propriedades de eventos aninhados]({{site.baseurl}}/user_guide/data/custom_data/custom_events/nested_objects/).

As Extensões de Segmento dependem do armazenamento de longo prazo das propriedades de eventos e não têm o limite de 30 dias de armazenamento de propriedades de eventos personalizados. Isso significa que você pode analisar as propriedades de eventos rastreadas no último ano, e o rastreamento não espera até que a extensão tenha sido configurada primeiro.

{% alert note %}
O uso de propriedades de eventos nas Extensões de Segmento não afeta o uso do ponto de dados.
{% endalert %}

{% endapi %}
{% api %}

#### Manter as Extensões de Segmento atualizadas

{% apitags %}
Segmentos
{% endapitags %}

Você pode especificar se deseja que essa extensão represente um único instantâneo no tempo ou se deseja que essa extensão seja regenerada diariamente. Sua extensão sempre começará a ser processada após o salvamento inicial. Se quiser que a extensão seja regenerada diariamente, selecione **Regenerate Extension Daily** e a regeneração começará a ser processada por volta da meia-noite de cada dia no fuso horário de sua empresa.

Quando terminar, clique em **Salvar**. Sua extensão começará a ser processada. O tempo necessário para gerar sua extensão depende de quantos usuários você tem, quantos eventos personalizados ou eventos de compra você está capturando e quantos dias você está olhando para trás no histórico.

Por fim, depois de criar uma extensão, você pode usá-la como um filtro ao criar um segmento ou definir um público-alvo para uma campanha ou Canvas. Comece escolhendo `Braze Segment Extension` na lista de filtros na seção **User Attributes (Atributos do usuário** ). Na lista de filtros Extensão do Segmento Braze, escolha a extensão que você deseja incluir ou excluir nesse segmento. Para visualizar os critérios da extensão, clique em **View Extension Details (Exibir detalhes da extensão**). Agora você pode prosseguir normalmente com a criação do seu segmento.

{% endapi %}
{% api %}

<!-- Campaigns -->

### Como você cria uma campanha multicanal?

{% apitags %}
Campanhas
{% endapitags %}

Para criar uma campanha multicanal, vá para a página **Campanhas**, selecione **Criar campanha** e, em seguida, selecione **Campanha multicanal**. Quando estiver em uma campanha multicanal, selecione **Add Messaging Channel (Adicionar canal de mensagens** ) na guia de composição para adicionar os canais desejados. Clique nos ícones de canal que aparecem para alternar entre diferentes compositores de mensagens à medida que você cria a cópia da campanha para os diferentes canais.

{% endapi %}
{% api %}

### Quais são algumas maneiras de começar a testar e otimizar campanhas?

{% apitags %}
Campanhas
{% endapitags %}

A criação de campanhas multivariadas e a execução de Canvases com diversas variantes são uma ótima maneira de começar! Por exemplo, você pode executar uma [campanha multivariada]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/) para testar uma mensagem com diferentes cópias ou linhas de assunto. Telas com várias variantes são úteis para testar fluxos de trabalho inteiros.

{% endapi %}
{% api %}

### Por que há uma diferença entre o número de destinatários únicos e o número de envios de uma determinada campanha ou Canvas?

{% apitags %}
Campanhas
{% endapitags %}

Uma possível explicação para essa diferença pode ser o fato de a campanha ou o Canvas ter ativado a reelegibilidade. Com isso ativado, os usuários que se qualificarem para as configurações de segmento e entrega poderão receber a mensagem mais de uma vez. Se a reelegibilidade não estiver ativada, a explicação provável para a diferença entre os envios e os destinatários exclusivos pode ser devido ao fato de os usuários terem vários dispositivos em plataformas associadas aos seus perfis.

Por exemplo, se você tiver um Canvas que tenha notificações push para iOS e Web, um determinado usuário com dispositivos móveis e desktop poderá receber mais de uma mensagem.

{% endapi %}
{% api %}

### O que a entrega por fuso horário local oferece?

{% apitags %}
Campanhas
{% endapitags %}

A entrega por fuso horário local permite a entrega de campanhas de mensagens a um segmento com base no fuso horário individual de um usuário. Sem a entrega por fuso horário local, as campanhas serão agendadas com base nas configurações de fuso horário de sua empresa no Braze.

Por exemplo, uma empresa sediada em Londres que envia uma campanha às 12h alcançará usuários na costa oeste dos Estados Unidos às 4h. Se o seu aplicativo estiver disponível apenas em determinados países, isso pode não ser um risco para você; caso contrário, é altamente recomendável evitar o envio de notificações push de manhã cedo para sua base de usuários!

{% endapi %}
{% api %}

### Como o Braze reconhece o fuso horário de um usuário?

{% apitags %}
Campanhas
{% endapitags %}

O Braze determinará automaticamente o fuso horário de um usuário a partir de seu dispositivo. Ele foi projetado para suportar a precisão do fuso horário e a cobertura total dos seus usuários. Os usuários criados por meio da API do usuário ou de outra forma sem um fuso horário terão o fuso horário da sua empresa como fuso horário padrão até que sejam reconhecidos no seu aplicativo pelo SDK.

Você pode verificar o fuso horário da sua empresa nas [configurações da empresa]({{site.baseurl}}/user_guide/administrative/app_settings/company_settings/).

{% endapi %}
{% api %}

### Como programo uma campanha de fuso horário local?

{% apitags %}
Campanhas
{% endapitags %}

Ao programar uma campanha, você precisa optar por enviá-la em um horário designado e, em seguida, selecionar **Enviar campanha para usuários em seu fuso horário local**.

A Braze recomenda enfaticamente que todas as campanhas de fuso horário local sejam agendadas com 24 horas de antecedência. Como uma campanha desse tipo precisa ser enviada ao longo de um dia inteiro, programá-la com 24 horas de antecedência permite que sua mensagem alcance todo o segmento. No entanto, você pode agendar essas campanhas com menos de 24 horas de antecedência, se necessário. Lembre-se de que o Braze não enviará mensagens a nenhum usuário que tenha perdido o horário de envio por mais de 1 hora.

Por exemplo, se forem 13 horas e você programar uma campanha de fuso horário local para as 15 horas, a campanha será enviada imediatamente a todos os usuários cujo horário local seja de 15 a 16 horas, mas não aos usuários cujo horário local seja 17 horas. Além disso, o horário de envio escolhido para sua campanha precisa ainda não ter ocorrido no fuso horário de sua empresa.

A edição de uma campanha de fuso horário local programada com menos de 24 horas de antecedência não alterará a programação da mensagem. Se você decidir editar uma campanha de fuso horário local para enviar em um horário posterior (por exemplo, 19h em vez de 18h), os usuários que estavam no segmento segmentado quando o horário de envio original foi escolhido ainda receberão a mensagem no horário original (18h). Se você editar um fuso horário local para enviar em um horário anterior (por exemplo, 16h em vez de 17h), a campanha ainda será enviada a todos os membros do segmento no horário original (17h).

{% alert note %}
Para as etapas do Canvas, os usuários não precisam estar na etapa por 24 horas para receber a próxima etapa para entrega no fuso horário local.
{% endalert %}

Se você permitiu que os usuários se tornassem reelegíveis para a campanha, eles a receberão novamente no horário original (17 horas). Para todas as ocorrências subsequentes de sua campanha, no entanto, suas mensagens serão enviadas somente no horário atualizado.

{% endapi %}
{% api %}

### Quando as alterações nas campanhas de fuso horário local entram em vigor?

{% apitags %}
Campanhas
{% endapitags %}

Os segmentos-alvo para campanhas de fuso horário local devem incluir pelo menos uma janela de 48 horas para qualquer filtro baseado em tempo, a fim de garantir a entrega a todo o segmento. Por exemplo, considere um segmento direcionado a usuários no segundo dia com os seguintes filtros:

- Aplicativo usado pela primeira vez há mais de 1 dia
- Primeiro uso do aplicativo há menos de 2 dias

A entrega por fuso horário local pode perder usuários nesse segmento com base no tempo de entrega e no fuso horário local dos usuários. Isso ocorre porque um usuário pode deixar o segmento no momento em que seu fuso horário aciona a entrega.

{% endapi %}
{% api %}

### Que alterações posso fazer nas campanhas programadas antes do lançamento?

{% apitags %}
Campanhas
{% endapitags %}

Quando a campanha é programada, é necessário editar qualquer coisa que não seja a composição da mensagem antes de colocar as mensagens na fila para envio. Como em todas as campanhas, você não pode editar eventos de conversão depois que a campanha é lançada.

{% endapi %}
{% api %}

### Qual é a "zona de segurança" antes que as mensagens em uma campanha programada sejam enfileiradas?

{% apitags %}
Campanhas
{% endapitags %}

- As campanhas programadas uma única vez podem ser editadas até o horário de envio programado.
- As campanhas programadas recorrentes podem ser editadas até o horário de envio programado.
- As campanhas de horário de envio local podem ser editadas até 24 horas antes do horário de envio programado.
- As campanhas com horário de envio ideal podem ser editadas até 24 horas antes do dia em que a campanha está programada para ser enviada.

{% endapi %}
{% api %}

### E se eu fizer uma edição dentro da "zona de segurança"?

{% apitags %}
Campanhas
{% endapitags %}

Alterar o tempo de envio em campanhas dentro desse período pode levar a um comportamento indesejado, por exemplo:

- O Braze não enviará mensagens a nenhum usuário que tenha perdido o horário de envio por mais de uma hora.
- As mensagens que já estavam na fila ainda podem ser enviadas no horário originalmente enfileirado, em vez do horário ajustado.

{% endapi %}
{% api %}

### O que devo fazer se a "zona de segurança" já tiver passado?

{% apitags %}
Campanhas
{% endapitags %}

Para garantir que as campanhas funcionem conforme desejado, recomendamos interromper a campanha atual (isso interromperá todas as mensagens na fila). Em seguida, você pode duplicar a campanha, fazer as alterações necessárias e lançar a nova campanha. Talvez seja necessário excluir dessa campanha os usuários que já tenham recebido a primeira campanha.

Certifique-se de reajustar os horários do cronograma da campanha para permitir o envio por fuso horário.

{% endapi %}
{% api %}

### Quando o Braze avalia os usuários para entrega no fuso horário local?

{% apitags %}
Campanhas
{% endapitags %}

Para a entrega no fuso horário local, o Braze avalia a elegibilidade de entrada dos usuários durante essas duas instâncias:

- No horário de Samoa (UTC+13) do dia programado
- No horário local do dia programado

Para que um usuário seja elegível para participar, ele deve ser elegível para ambas as verificações. Por exemplo, se um Canvas estiver programado para ser lançado em 7 de agosto de 2021 às 14h do fuso horário local, a segmentação de um usuário localizado em Nova York exigiria as seguintes verificações de elegibilidade:

- Nova York em 6 de agosto de 2021 às 21 horas
- Nova York em 7 de agosto de 2021 às 14h

O usuário precisa estar no segmento por 24 horas antes do lançamento. Se o usuário não for elegível na primeira verificação, o Braze não tentará a segunda verificação.

{% endapi %}
{% api %}

### Por que o número de usuários que entram em uma campanha não corresponde ao número esperado?

{% apitags %}
Campanhas
{% endapitags %}

O número de usuários que entram em uma campanha pode ser diferente do número esperado devido à forma como os públicos e os acionadores são avaliados. No Braze, um público é avaliado antes do acionador (a menos que seja usado um [acionador de alteração de atributo]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/attribute_triggers#change-custom-attribute-value)). Isso fará com que os usuários saiam da campanha se não fizerem parte do público-alvo selecionado inicialmente, antes que qualquer ação de acionamento seja avaliada.

{% endapi %}
{% api %}

<!-- Canvases -->

### O que acontece se o público e o tempo de envio forem idênticos para um Canvas que tem uma variante, mas várias ramificações?

{% apitags %}
Telas
{% endapitags %}

Colocamos um trabalho na fila para cada etapa - eles são executados mais ou menos ao mesmo tempo, e um deles "vence". Na prática, isso pode ser classificado de maneira um pouco uniforme, mas é provável que haja pelo menos uma leve tendência para a etapa que foi criada primeiro.

Além disso, não podemos garantir exatamente como será essa distribuição. Se quiser garantir uma divisão uniforme, adicione um filtro [de número de balde aleatório]({{site.baseurl}}/user_guide/engagement_tools/testing/random_bucket_numbers/).

{% endapi %}
{% api %}

### O que acontece quando você interrompe um Canvas?

{% apitags %}
Telas
{% endapitags %}

Quando você interrompe um Canvas, aplica-se o seguinte:

- Os usuários serão impedidos de entrar no Canvas.
- Nenhuma outra mensagem será enviada, independentemente de onde o usuário esteja no fluxo.
    - **Exceção:** O Email Canvases não será interrompido imediatamente. Depois que as solicitações de envio vão para o SendGrid, não há nada que possamos fazer para impedir que elas sejam entregues ao usuário.

{% alert note %}
A interrupção de um Canvas não encerrará os usuários que estiverem aguardando em uma etapa. Se você reativar o Canvas e os usuários ainda estiverem esperando, eles concluirão a etapa e passarão para o próximo componente. No entanto, se o tempo em que o usuário deveria ter avançado para o próximo componente tiver passado, ele sairá do Canvas.
{% endalert %}

{% endapi %}
{% api %}

### Quando um evento de exceção é acionado?

{% apitags %}
Telas
{% endapitags %}

Os eventos de exceção só são acionados enquanto o usuário está esperando para receber o componente do Canvas ao qual está associado. Se um usuário executar uma ação antecipadamente, o evento de exceção não será acionado.

Se quiser excluir os usuários que realizaram um determinado evento com antecedência, use [filtros]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/).

{% endapi %}
{% api %}

### Como a edição de um Canvas afeta os usuários que já estão no Canvas?

{% apitags %}
Telas
{% endapitags %}

Se você editar algumas das etapas de um Canvas de várias etapas, os usuários que já estavam no público, mas não receberam as etapas, receberão a versão atualizada da mensagem. Observe que isso só ocorrerá se eles ainda não tiverem sido avaliados para a etapa.

Para obter mais informações sobre o que você pode ou não pode editar após o lançamento, consulte [Alterar seu Canvas após o lançamento]({{site.baseurl}}/post-launch_edits/).

{% endapi %}
{% api %}

### Como as conversões de usuários são rastreadas em um Canvas?

{% apitags %}
Telas
{% endapitags %}

Um usuário só pode converter uma vez por entrada no Canvas.

As conversões são atribuídas à mensagem mais recente recebida pelo usuário para essa entrada. O bloco de resumo no início de um Canvas reflete todas as conversões realizadas pelos usuários dentro desse caminho, independentemente de terem ou não recebido uma mensagem. Cada etapa subsequente mostrará apenas as conversões que ocorreram enquanto essa foi a etapa mais recente que o usuário recebeu.

{% details Use cases %}

#### Caso de uso 1

Há um caminho do Canvas com 10 notificações por push e o evento de conversão é "início da sessão" ("Abre o aplicativo"):

- O usuário A abre o aplicativo depois de entrar, mas antes de receber a primeira mensagem.
- O usuário B abre o aplicativo após cada notificação push.

**Resultado:**
O resumo mostrará duas conversões, enquanto as etapas individuais mostrarão uma conversão de um na primeira etapa e zero em todas as etapas subsequentes.

{% alert note %}
Se o Quiet Hours estiver ativo quando o evento de conversão ocorrer, as mesmas regras se aplicam.
{% endalert %}

#### Caso de uso 2

Há um Canvas de uma etapa com o Quiet Hours:

1. O usuário entra no Canvas.
2. A primeira etapa não tem atraso, mas está dentro do Quiet Hours, portanto a mensagem é suprimida.
3. O usuário realiza o evento de conversão.

**Resultado:**
O usuário será contado como convertido na variante geral do Canvas, mas não na etapa, pois não recebeu a etapa.

{% enddetails %}

{% endapi %}
{% api %}

### Ao analisar o número de usuários únicos, o Canvas Analytics ou o segmentador é mais preciso?

{% apitags %}
Telas
{% endapitags %}

O segmentador é uma estatística mais precisa para dados de usuários exclusivos em comparação com as estatísticas do Canvas ou da campanha. Isso ocorre porque as estatísticas do Canvas e da campanha são números que o Braze incrementa quando algo acontece, o que significa que há variáveis que podem fazer com que esse número seja diferente do número do segmentador. Por exemplo, os usuários podem converter mais de uma vez para um Canvas ou campanha.  

{% endapi %}
{% api %}

### Por que o número de usuários que entram em um Canvas não corresponde ao número esperado?

{% apitags %}
Telas
{% endapitags %}

O número de usuários que entram em um Canvas pode ser diferente do número esperado devido à forma como os públicos e os acionadores são avaliados. No Braze, um público é avaliado antes do acionador (a menos que seja usado um acionador de [alteração de atributo]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/attribute_triggers/#change-custom-attribute-value) ). Isso fará com que os usuários saiam do Canvas se não fizerem parte do público selecionado antes que qualquer ação de acionamento seja avaliada.

{% endapi %}
{% api %}

<!-- Analytics -->

### Que métricas o Braze mede?

{% apitags %}
Análises
{% endapitags %}

Dependendo do canal, o Braze mede uma variedade de métricas para permitir que você determine o sucesso de uma campanha e informe as futuras. Você pode encontrar uma lista abrangente em nosso [glossário de métricas de relatórios]({{site.baseurl}}/user_guide/data/report_metrics/).

{% endapi %}
{% api %}

### Como a receita é calculada no Braze?

{% apitags %}
Análises
{% endapitags %}

Na página **Receita**, você pode visualizar dados sobre a receita ou as compras em períodos específicos, para um produto específico ou a receita ou as compras totais do seu aplicativo. Esses números de receita são gerados a partir das compras feitas pelos destinatários da campanha em um determinado período de conversão.

Dito isso, é importante observar que o Braze é uma ferramenta de marketing e não uma ferramenta de gerenciamento de receita. Nosso [objeto de compra]({{site.baseurl}}/api/objects_filters/purchase_object/) não oferece suporte a reembolsos e cancelamentos, portanto, você pode ver discrepâncias ao comparar dados com outras ferramentas.

{% endapi %}
{% api %}

### Quais recursos de relatório o Currents permite?

{% apitags %}
Análises
{% endapitags %}

Nossa ferramenta Currents transmite continuamente os dados de engajamento de mensagens e de comportamento do cliente para um de nossos vários parceiros de dados, permitindo que você use os dados exclusivos e valiosos que o Braze cria para impulsionar seus esforços de business intelligence e análise em outros parceiros de primeira linha.

Esses dados vão além das métricas de engajamento de mensagens e também podem incluir números mais complexos, como atributos personalizados e desempenho de eventos. Para obter mais detalhes, consulte nosso [glossário de eventos atuais]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/customer_behavior_events/).

{% endapi %}
{% api %}

### Como posso agendar um relatório de compromisso recorrente?

{% apitags %}
Análises
{% endapitags %}

Para agendar um relatório de compromisso recorrente, faça o seguinte:

1. Em sua conta do painel, navegue até **Relatórios de envolvimento**, em **Dados**.
2. Clique em **\+ Criar novo relatório**.
3. Adicione as [campanhas e as mensagens do Canvas]({{site.baseurl}}/user_guide/data_and_analytics/reporting/engagement_reports/#manually-select-campaigns-or-canvases) (individualmente ou [por tag]({{site.baseurl}}/user_guide/data_and_analytics/reporting/engagement_reports/#automatically-select-campaigns-or-canvases)) que você gostaria de compilar em seu relatório.
4. [Adicione estatísticas]({{site.baseurl}}/user_guide/data_and_analytics/reporting/engagement_reports/#add-statistics-to-your-report) ao seu relatório.
5. Selecione a compressão e o eliminador para seu relatório.
6. Digite os endereços de e-mail dos usuários do Braze que devem receber esse relatório.
7. Selecione o [período de tempo]({{site.baseurl}}/user_guide/data_and_analytics/reporting/engagement_reports/#time-frame) a partir do qual você gostaria que o relatório executasse os dados.
8. Selecione os [intervalos (diários, semanais, etc.)]({{site.baseurl}}/user_guide/data_and_analytics/reporting/engagement_reports/#data-display) em que deseja ver o detalhamento de seus dados.
9. Programe seu relatório para ser [enviado imediatamente]({{site.baseurl}}/user_guide/data_and_analytics/reporting/engagement_reports/#send-immediately) ou em um [momento futuro especificado]({{site.baseurl}}/user_guide/data_and_analytics/reporting/engagement_reports/#send-at-designated-time).
10. Execute o relatório e abra-o em seu e-mail quando ele chegar!

{% endapi %}
{% api %}

### Qual é a diferença entre os Relatórios de envolvimento e o Criador de relatórios?

{% apitags %}
Análises
{% endapitags %}

Os relatórios de engajamento fornecem CSVs de estatísticas de engajamento para mensagens específicas de campanhas e Canvases por meio de um e-mail acionado. Determinados dados são agregados no nível da campanha ou do Canvas em comparação com o nível da variante ou etapa individual. Os relatórios não são salvos no painel, e a reexecução do relatório pode resultar em estatísticas atualizadas.

O Report Builder permite comparar os resultados de várias campanhas ou Canvases em uma única exibição, para que você possa determinar facilmente quais estratégias de engajamento tiveram maior impacto em suas principais métricas. Tanto para campanhas quanto para Canvases, você pode exportar seus dados e salvar seu relatório para visualização futura.

Para obter mais informações sobre os usos de relatórios e análises no Braze, consulte a [visão geral dos relatórios]({{site.baseurl}}/user_guide/analytics/reporting/reports_overview/).

{% endapi %}

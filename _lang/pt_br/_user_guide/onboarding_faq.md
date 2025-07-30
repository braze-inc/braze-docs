---
article_title: Perguntas frequentes
hidden: true
permalink: /onboarding_faq/
excerpt_separator: ""
page_type: glossary
layout: onboarding_faq
description: "Esta página contém uma coleção de perguntas frequentes, organizadas por categoria."

---

{% multi_lang_include video.html id="keAZAlBR9zc" source="youtube" %}


<!--- Users --->

{% api %}

### Como eu lido com dados de usuários anônimos?

{% apitags %}
Usuários
{% endapitags %}

Inicialmente, quando um perfil de usuário é reconhecido via SDK, a Braze cria um perfil de usuário anônimo com um `braze_id` associado: um identificador de usuário único que é definido pela Braze.

Para acompanhar melhor os usuários anônimos, você pode implementar [aliases de usuário]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle#user-aliases) que permitem tag usuários anônimos com um identificador. Esses usuários podem então ser exportados usando seus aliases, ou referenciados pela API.

Se um perfil de usuário anônimo com um pseudônimo for posteriormente reconhecido com um `external_id`, ele será tratado como um perfil de usuário identificado normal, mas manterá seu pseudônimo existente e ainda poderá ser referenciado por esse pseudônimo.

Para usuários de alias que você deseja mesclar com usuários identificados, você pode mesclar quaisquer campos que sejam pertinentes ao perfil real que você deseja manter. Você teria que exportar esses dados antes de excluí-los do perfil de alias usando nosso [endpoint Exportar perfil de usuário por identificador]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/). Você pode então usar nosso [endpoint de Rastreamento de usuários]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) para postar esses eventos no perfil que você manteve. Isso preservará quaisquer dados que você queira manter, como atributos que foram previamente registrados em um perfil, mas não no outro.

Para uma análise completa dos diferentes métodos de coleta de novos e existentes dados de usuários no Braze, confira [as melhores práticas de coleta de dados]({{site.baseurl}}/user_guide/data/user_data_collection/best_practices/).

{% endapi %}
{% api %}

### Como posso importar usuários que já coletei e identifiquei fora do Braze?

{% apitags %}
Usuários
{% endapitags %}

Para importar usuários previamente identificados, você pode fazer upload de um CSV para a Braze ou enviar dados através da API.

#### CSV

Você pode fazer upload e atualizar perfis de usuários via arquivos CSV de **público** > **Importar Usuários**. Ao importar seus dados de cliente, você precisará especificar o identificador único de cada cliente, também conhecido como `external_id`.

Antes de iniciar sua importação de CSV, é importante entender com sua equipe de engenharia como os usuários serão identificados no Braze. Normalmente, isso seria um ID de banco de dados usado internamente. Isso deve estar alinhado com a forma como os usuários serão identificados pelo SDK da Braze em dispositivos móveis e web, para que cada cliente tenha um único perfil de usuário na Braze em todos os seus dispositivos. Saiba mais sobre o [ciclo de vida do perfil de usuário da Braze]({{site.baseurl}}/user_guide/data/user_data_collection/user_profile_lifecycle/).

Quando você fornece um `external_id` na sua importação, a Braze atualizará qualquer usuário existente com o mesmo `external_id` ou criará um novo usuário identificado com esse conjunto de `external_id` se não for encontrado nenhum.

Para saber mais e para baixar os modelos de importação de CSV, consulte [importação de usuário]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import/#csv).

#### API

Para fazer upload de usuários via API, você pode usar nosso [endpoint Track users]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) para importá-los para a Braze.

Se você não tiver certeza se o usuário já existe no Braze, você pode implementar nosso [endpoint de Exportação de perfil de usuário por identificador]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/) para verificar. Se você identificar que o usuário já existe no Braze, você pode usar nosso `/users/track` endpoint para postar os novos dados que você gostaria de adicionar ao perfil do usuário que já existe no Braze.

{% alert note %}
Mantenha as seguintes nuances em mente ao usar o endpoint `/users/track`:

- Ao criar usuários apenas com alias por meio desse endpoint, você deve definir explicitamente a `_update_existing_only` flag como falsa.
- Atualizar o status da inscrição com este endpoint atualizará tanto o usuário especificado pelo seu ID externo (como Usuário1) quanto o status da inscrição de qualquer usuário com o mesmo e-mail que esse usuário (Usuário1).
{% endalert %}

{% endapi %}
{% api %}

### Qual é a diferença entre os status de inscrição push?

{% apitags %}
Usuários
{% endapitags %}

Existem três opções de estado de inscrição push: inscrito, aceitação e não inscrito.

Por padrão, para que seu usuário receba suas mensagens por push, seu estado de inscrição de push deve ser inscrito ou optado, e eles devem estar habilitados para push. Você pode substituir essa configuração, se necessário, ao criar uma mensagem.

|Estado de aceitação|Descrição|
|---|---|
|Inscreveu-se| Estado de inscrição de push padrão quando um perfil de usuário é criado no Braze. |
|Aceitou| Um usuário expressou explicitamente uma preferência por receber notificações por push. A Braze moverá automaticamente o estado de aceitação do usuário para `Opted-In` se um usuário aceitar um prompt de push no nível do sistema operacional.<br><br>Isso não se aplica a usuários no Android 12 ou inferior.|
|Cancelou inscrição| Um usuário cancelou explicitamente a inscrição de push através do seu aplicativo ou outros métodos fornecidos pela sua marca. Por padrão, as campanhas de push da Braze têm como alvo apenas os usuários que são `Subscribed` ou `Opted-in` para push.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endapi %}
{% api %}

### E se eu identifiquei usuários duplicados?

{% apitags %}
Usuários
{% endapitags %}

Se você identificou usuários duplicados, será necessário limpar esses perfis de usuário. Você pode fazer isso através das seguintes etapas:

1. Exporte os perfis de usuário usando nosso endpoint `/users/export/ids`.
2. Identificar o perfil correto do usuário (em última análise, sua equipe precisará decidir sobre as informações corretas) e/ou:
    - Mescle quaisquer campos que sejam pertinentes ao perfil real que você deseja manter usando o endpoint `/user/track`.
    - Exclua o perfil duplicado e não útil sem mesclar nenhum dado usando o endpoint users/delete. Depois de excluir um perfil de usuário, **não há como recuperar as informações**.

{% alert important %}
Recomendamos que você primeiro importe os novos perfis de usuário com o `external_id` correto e os atributos e eventos personalizados correspondentes. Depois que os perfis de usuário são excluídos, eles não podem ser recuperados, então a exclusão deve ser a última etapa.
{% endalert %}

É importante observar:

- Qualquer dado de engajamento (como campanhas ou canvas recebidos) em perfis de usuário duplicados será perdido. A única maneira de reter o contexto histórico de engajamento é adicioná-lo como um atributo personalizado (como um atributo personalizado de array de todas as campanhas ou canvas recebidas).
- Ao migrar perfis de usuário, também cabe à sua equipe decidir qual perfil de usuário dos duplicados será mantido. Braze não pode decidir ou fornecer uma lista de perfis para excluir.  
- Em última análise, será importante para sua equipe avaliar o processo de inscrição a partir da experiência dos seus usuários e garantir que você esteja chamando o método `changeUser()` apenas quando um usuário se tornar identificado.

{% endapi %}
{% api %}

<!-- Segments -->

### Como crio um segmento quando importo um grupo de usuários através de CSV?

{% apitags %}
Segmentos
{% endapitags %}

Para importar seu arquivo CSV, navegue até a página de **importação de usuário** na seção Usuários. A tabela **Recent Imports** lista até vinte das suas importações mais recentes, seus nomes de arquivo, número de linhas no arquivo, número de linhas importadas com sucesso, total de linhas em cada arquivo e o status de cada importação.

O painel **Importar CSV** contém instruções de importação e um botão para iniciar sua importação. Clique em **Selecionar arquivo CSV** e selecione seu arquivo de interesse. Em seguida, antes de clicar em **Iniciar Importação**, você tem a opção de informar à Braze o que fazer com esta lista em "O que você quer que façamos com os usuários neste CSV".

Selecione **Importar Usuários neste CSV e também possibilitar redirecionar este lote específico de usuários como um grupo**, e então selecione **Gerar automaticamente um segmento dos usuários que são importados deste CSV**. Depois que você clicar em **Start Import**, a Braze fará upload do seu arquivo, verificará os cabeçalhos das colunas e os tipos de dados de cada coluna, e criará um segmento.

Para baixar um modelo de CSV, consulte a [importação de usuário]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import/#csv).

{% endapi %}
{% api %}

### Quais tipos de filtros posso usar ao criar um segmento?

{% apitags %}
Segmentos
{% endapitags %}

O SDK da Braze fornece um arsenal poderoso de filtros para segmentar e direcionar seus usuários com base em recursos e atributos específicos. Você pode usar o glossário de [Filtros de Segmentação]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters) para pesquisar ou restringir esses filtros por Categoria de Filtro (Dados Personalizados, Atividade do Usuário, redirecionamento, Atividade de Marketing, Atributos do Usuário, atribuição da instalação, Atividade Social, Testes, Outros).

{% endapi %}
{% api %}

### Como configuro o direcionamento de local para que eu possa segmentar os usuários pelo local mais recente e usá-lo em minhas campanhas e estratégias baseadas em local?

{% apitags %}
Segmentos
{% endapitags %}

Navegue para a página **Segmentos**, em engajamento, para ver todos os seus segmentos de usuários atuais. Nesta página, você pode criar e nomear novos segmentos. Para começar, clique em **Criar Segmento** e dê um nome ao seu segmento.

Depois de criar seu segmento, adicione um `Most Recent Location` filtro para segmentar os usuários pelo último lugar em que usaram seu app. Você pode destacar usuários em uma região circular padrão ou criar uma região poligonal personalizada.

- Para regiões circulares, você pode mover a origem e ajustar o raio de localização para sua segmentação.
- Para regiões poligonais, você pode designar mais especificamente quais áreas deseja incluir em seu segmento.

{% alert tip %}
Interessado em aproveitar o direcionamento de local com a ajuda de um parceiro Braze? Confira nossos [parceiros de localização contextual]({{site.baseurl}}/partners/message_personalization/).
{% endalert %}

{% endapi %}
{% api %}

### Como posso segmentar listas precisas de usuários com base em seu evento personalizado e comportamento de compra nos últimos 365 dias?

{% apitags %}
Segmentos
{% endapitags %}

Você pode usar [extensões de segmento]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/)! extensões de segmento ativar você para segmentar uma lista mais precisa de usuários do que você poderia com um segmento regular.

Você pode criar até 10 extensões de segmento por espaço de trabalho. Depois que essas listas de extensões são geradas, elas podem ser incluídas ou excluídas como um filtro em seus segmentos. Ao criar uma extensão de segmento, você também pode especificar que a lista seja regenerada uma vez a cada 24 horas.

1. Em Engajamentos, expanda **Segmentos** e clique em **extensão de segmento**.
2. Na tabela de extensões de segmento, clique em **\+ Criar nova extensão**.
3. Nomeie sua extensão de segmento descrevendo o tipo de usuários que você pretende filtrar. Isso garantirá que esta extensão possa ser facilmente e precisamente descoberta ao aplicá-la como um filtro em seu segmento.
4. Selecione entre um critério de compra ou evento personalizado para direcionamento.
5. Escolha qual item comprado ou evento personalizado específico você gostaria de direcionar para sua lista de usuários. 
6. Escolha quantas vezes (mais que, menos que ou igual a) o usuário precisaria ter completado o evento, e quantos dias retroceder, até 365 dias.

Para aumentar a precisão do direcionamento, você pode selecionar **Adicionar Filtros de Propriedade** e segmentar com base nas propriedades específicas da sua compra ou evento personalizado. A Braze é compatível com segmentação de propriedades de eventos com base em string, numéricos, booleanos e objetos de tempo.

Também suportamos a segmentação com base em [propriedades de eventos aninhados]({{site.baseurl}}/user_guide/data/custom_data/custom_events/nested_objects/).

Extensões de segmento dependem do armazenamento de longo prazo das propriedades do evento e não têm o limite de armazenamento de propriedades de evento personalizado de 30 dias. Isso significa que você pode olhar para trás nas propriedades do evento rastreadas no último ano, e o rastreamento não espera até que a extensão tenha sido configurada primeiro.

{% alert note %}
O uso de propriedades de eventos dentro de extensões de segmento não impacta o uso de pontos de dados.
{% endalert %}

{% endapi %}
{% api %}

#### Manter as extensões de segmento atualizadas

{% apitags %}
Segmentos
{% endapitags %}

Você pode especificar se deseja que esta extensão represente um momento específico ou que seja gerada novamente a cada dia. Sua extensão sempre começará a ser processada logo após ser salva. Se você gostaria que a extensão fosse regenerada diariamente, selecione **Regenerar Extensão Diariamente** e a regeneração começará a ser processada por volta da meia-noite de cada dia no fuso horário da sua empresa.

Quando terminar, clique em **Salvar**. Sua extensão começará a processar. O tempo necessário para gerar sua extensão depende de quantos usuários você tem, quantos eventos personalizados ou eventos de compra você está capturando e quantos dias você está olhando para trás na história.

Finalmente, depois de criar uma extensão, você pode usá-la como um filtro ao criar um segmento ou definir um público para uma campanha ou canva. Comece escolhendo `Braze Segment Extension` da lista de filtros na seção **Atributos do Usuário**. Na lista de filtros de extensão de segmento do Braze, escolha a extensão que deseja incluir ou excluir neste segmento. Para ver os critérios de extensão, clique em **Ver Detalhes da Extensão**. Agora você pode continuar como de costume criando seu segmento.

{% endapi %}
{% api %}

<!-- Campaigns -->

### Como você cria uma campanha multicanal?

{% apitags %}
Campanhas
{% endapitags %}

Para criar uma campanha multicanal, acessar a página **Campanhas**, selecionar **Criar Campanha**, e então selecionar **Campanha Multicanal**. Quando estiver dentro de uma campanha multicanal, selecione **Adicionar canal de envio de mensagens** na guia de composição para adicionar os canais desejados. Clique nos ícones do canal que aparecem para alternar entre diferentes compositores de envio de mensagens enquanto você cria a cópia da sua campanha para os diferentes canais.

{% endapi %}
{% api %}

### Quais são algumas maneiras de começar a testar e otimizar campanhas?

{% apitags %}
Campanhas
{% endapitags %}

Criar campanhas multivariantes e executar canvas com várias variantes é uma ótima maneira de começar! Por exemplo, você pode executar uma [campanha multivariante]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/) para testar uma mensagem que possui diferentes cópias ou linhas de assunto. Canvas com várias variantes são úteis para testar fluxos de trabalho inteiros.

{% endapi %}
{% api %}

### Por que há uma diferença entre o número de destinatários únicos e o número de envios para uma determinada campanha ou canva?

{% apitags %}
Campanhas
{% endapitags %}

Uma possível explicação para essa diferença pode ser devido à campanha ou canva ter a re-eligibilidade ativada. Ao ativar isso, os usuários que se qualificarem para o segmento e as configurações de entrega poderão receber a mensagem mais de uma vez. Se a re-eligibilidade não estiver ativada, a provável explicação para a diferença entre envios e destinatários únicos pode ser devido a usuários com vários dispositivos em diferentes plataformas associados aos seus perfis.

Por exemplo, se você tiver uma canva que tenha notificações push para iOS e web, um determinado usuário com dispositivos móveis e de desktop pode receber mais de uma mensagem.

{% endapi %}
{% api %}

### O que a entrega no fuso local oferece?

{% apitags %}
Campanhas
{% endapitags %}

A entrega no fuso local permite que você entregue campanhas de envio de mensagens para um segmento com base no fuso horário individual de um usuário. Sem entrega de fuso local, as campanhas serão agendadas com base nas configurações de fuso horário da sua empresa no Braze.

Por exemplo, uma empresa com sede em Londres que envia uma campanha às 12h atingirá usuários na costa oeste da América às 4h. Se o seu app estiver disponível apenas em alguns países, isso pode não ser um risco para você, caso contrário, recomendamos fortemente evitar enviar notificações por push de manhã cedo para sua base de usuários!

{% endapi %}
{% api %}

### Como o Braze reconhece o fuso horário de um usuário?

{% apitags %}
Campanhas
{% endapitags %}

Braze determinará automaticamente o fuso horário de um usuário a partir de seu dispositivo. Isso é projetado para suportar a precisão do fuso horário e a cobertura total de seus usuários. Os usuários criados através da API de Usuário ou de outra forma sem um fuso horário terão o fuso horário da sua empresa como seu fuso horário padrão até serem reconhecidos em seu app pelo SDK.

Você pode verificar o fuso horário da sua empresa nas [configurações da empresa]({{site.baseurl}}/user_guide/administrative/app_settings/company_settings/).

{% endapi %}
{% api %}

### Como faço para agendar uma campanha no fuso local?

{% apitags %}
Campanhas
{% endapitags %}

Ao agendar uma campanha, você precisa escolher enviá-la em um horário designado e, em seguida, selecionar **Enviar campanha para usuários no seu fuso local**.

A Braze recomenda fortemente que todas as campanhas no fuso local sejam agendadas com 24 horas de antecedência. Como tal campanha precisa ser enviada ao longo de um dia inteiro, agendá-la com 24 horas de antecedência permite que sua mensagem alcance todo o seu segmento. No entanto, você pode agendar essas campanhas com menos de 24 horas de antecedência, se necessário. Lembre-se de que a Braze não enviará mensagens para nenhum usuário que tenha perdido o horário de envio por mais de 1 hora.

Por exemplo, se for 13h e você agendar uma campanha de fuso local para as 15h, a campanha será enviada imediatamente para todos os usuários cujo fuso local seja das 15h às 16h, mas não para os usuários cujo fuso local seja 17h. Além disso, o horário de envio que você escolher para sua campanha ainda não deve ter ocorrido no fuso horário da sua empresa.

Editar uma campanha de fuso local que está programada para menos de 24 horas de antecedência não alterará o cronograma da mensagem. Se você decidir editar uma campanha de fuso local para enviar em um horário posterior (por exemplo, 19h em vez de 18h), os usuários que estavam no segmento alvo quando o horário de envio original foi escolhido ainda receberão a mensagem no horário original (18h). Se você editar um fuso local para enviar em um horário anterior (por exemplo, 16h em vez de 17h), a campanha ainda será enviada a todos os membros do segmento no horário original (17h).

{% alert note %}
Para as etapas do canva, os usuários não precisam estar na etapa por 24 horas para receber a próxima etapa para entrega no fuso local.
{% endalert %}

Se você permitiu que os usuários se tornassem re-elegíveis para a campanha, eles a receberão novamente no horário original (17h). Para todas as ocorrências subsequentes de sua campanha, no entanto, suas mensagens serão enviadas apenas no horário atualizado.

{% endapi %}
{% api %}

### Quando as alterações nas campanhas de fuso local entram em vigor?

{% apitags %}
Campanhas
{% endapitags %}

Os segmentos-alvo para campanhas de fuso local devem incluir pelo menos uma janela de 48 horas para quaisquer filtros baseados em tempo para garantir a entrega a todo o segmento. Por exemplo, considere um segmento direcionando usuários no seu segundo dia com os seguintes filtros:

- Usou o app pela primeira vez há mais de 1 dia
- Primeiro uso do app há menos de 2 dias

A entrega no fuso local pode não alcançar os usuários deste segmento com base no horário de entrega e no fuso local dos usuários. Isso ocorre porque um usuário pode deixar o segmento no momento em que seu fuso horário aciona a entrega.

{% endapi %}
{% api %}

### Quais mudanças posso fazer nas campanhas agendadas antes do lançamento?

{% apitags %}
Campanhas
{% endapitags %}

Quando a campanha está agendada, edições em qualquer coisa além da composição da mensagem precisam ser feitas antes de colocarmos as mensagens na fila para envio. Como em todas as campanhas, você não pode editar eventos de conversão após o lançamento da campanha.

{% endapi %}
{% api %}

### Qual é a "zona segura" antes que as mensagens em uma campanha agendada sejam enfileiradas?

{% apitags %}
Campanhas
{% endapitags %}

- Campanhas agendadas únicas podem ser editadas até o horário de envio agendado.
- Campanhas recorrentes agendadas podem ser editadas até o horário de envio agendado.
- Campanhas de envio local podem ser editadas até 24 horas antes do horário de envio agendado.
- Campanhas de envio em horário ideal podem ser editadas até 24 horas antes do dia em que a campanha está programada para ser enviada.

{% endapi %}
{% api %}

### E se eu fizer uma edição dentro da "zona segura"?

{% apitags %}
Campanhas
{% endapitags %}

Alterar o horário de envio das campanhas dentro desse período pode levar a um comportamento indesejado, por exemplo:

- A Braze não enviará mensagens para nenhum usuário que tenha perdido o horário de envio por mais de uma hora.
- Mensagens que já estavam na fila podem ainda ser enviadas no horário originalmente agendado, em vez do horário ajustado.

{% endapi %}
{% api %}

### O que devo fazer se a "zona segura" já passou?

{% apitags %}
Campanhas
{% endapitags %}

Para garantir que as campanhas operem conforme desejado, recomendamos parar a campanha atual (isso interromperá quaisquer mensagens na fila). Você pode então duplicar a campanha, fazer as alterações necessárias e lançar a nova campanha. Você pode precisar excluir usuários desta campanha que já receberam a primeira campanha.

Reajuste os horários da campanha para permitir o envio no fuso horário.

{% endapi %}
{% api %}

### Quando o Braze avalia os usuários para a entrega no fuso local?

{% apitags %}
Campanhas
{% endapitags %}

Para entrega no fuso local, Braze avalia os usuários para sua elegibilidade de entrada durante estas duas instâncias:

- No horário de Samoa (UTC+13) do dia agendado
- No fuso local do dia agendado

Para que um usuário seja elegível para entrada, ele deve ser elegível para ambas as verificações. Por exemplo, se um canva estiver programado para ser lançado em 7 de agosto de 2021 às 14h no fuso local, então direcionar um usuário localizado em Nova York exigiria as seguintes verificações de elegibilidade:

- Nova Iorque em 6 de agosto de 2021 às 21h
- Nova Iorque em 7 de agosto de 2021 às 14h

O usuário precisa estar no segmento por 24 horas antes do lançamento. Se o usuário não for elegível na primeira verificação, então a Braze não tentará a segunda verificação.

{% endapi %}
{% api %}

### Por que o número de usuários que entram em uma campanha não corresponde ao número esperado?

{% apitags %}
Campanhas
{% endapitags %}

O número de usuários que entram em uma campanha pode diferir do seu número esperado por causa de como as audiências e os gatilhos são avaliados. Na Braze, um público é avaliado antes do gatilho (a menos que use uma [mudança no gatilho do atributo]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/attribute_triggers#change-custom-attribute-value)). Isso fará com que os usuários abandonem a campanha se eles não fizerem parte do seu público selecionado antes que quaisquer ações de disparo sejam avaliadas.

{% endapi %}
{% api %}

<!-- Canvases -->

### O que acontece se o público e o horário de envio forem idênticos para um canva que tem uma variante, mas várias ramificações?

{% apitags %}
Canvas
{% endapitags %}

Nós enfileiramos um trabalho para cada etapa—eles são executados aproximadamente ao mesmo tempo, e um deles "vence". Na prática, isso pode ser classificado de forma um pouco uniforme, mas é provável que tenha pelo menos uma leve tendência para a etapa que foi criada primeiro.

Além disso, não podemos garantir exatamente como será essa distribuição. Se você quiser garantir uma divisão uniforme, adicione um filtro de [número de bucket aleatório]({{site.baseurl}}/user_guide/engagement_tools/testing/random_bucket_numbers/).

{% endapi %}
{% api %}

### O que acontece quando você para uma canva?

{% apitags %}
Canvas
{% endapitags %}

Quando você interrompe um canva, o seguinte se aplica:

- Os usuários serão impedidos de entrar na canva.
- Nenhuma outra mensagem será enviada, independentemente de onde um usuário esteja no fluxo.
    - **Exceção:** Os canvas por e-mail não pararão imediatamente. Depois que as solicitações de envio acessam o SendGrid, não há nada que possamos fazer para impedir que elas sejam entregues ao usuário.

{% alert note %}
Parar uma canva não fará com que os usuários que estão esperando em uma etapa saiam. Se você reativar o canva e os usuários ainda estiverem esperando, eles completarão a etapa e passarão para o próximo componente. No entanto, se o tempo que o usuário deveria ter progredido para o próximo componente tiver passado, ele sairá do canva.
{% endalert %}

{% endapi %}
{% api %}

### Quando um evento de exceção dispara?

{% apitags %}
Canvas
{% endapitags %}

Os eventos de exceção só disparam enquanto o usuário está esperando para receber o componente canva com o qual está associado. Se um usuário realizar uma ação com antecedência, o evento de exceção não disparará.

Se você quiser excetuar usuários que realizaram um determinado evento com antecedência, use [filtros]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/) em vez disso.

{% endapi %}
{% api %}

### Como a edição de uma canva afeta os usuários que já estão na canva?

{% apitags %}
Canvas
{% endapitags %}

Se você editar algumas das etapas de um canva de várias etapas, os usuários que já estavam no público, mas não receberam as etapas, receberão a versão atualizada da mensagem. Observe que isso só acontecerá se eles ainda não tiverem sido avaliados para a etapa.

Para saber mais sobre o que você pode ou não pode editar após o lançamento, confira [Alterando seu Canva após o lançamento]({{site.baseurl}}/post-launch_edits/).

{% endapi %}
{% api %}

### Como são rastreadas as conversões de usuários em uma canva?

{% apitags %}
Canvas
{% endapitags %}

Um usuário só pode converter uma vez por entrada de canva.

As conversões são atribuídas à mensagem mais recente recebida pelo usuário para essa entrada. O bloco de resumo no início de uma canva reflete todas as conversões realizadas pelos usuários dentro daquela jornada, independentemente de terem recebido uma mensagem ou não. Cada etapa subsequente mostrará apenas as conversões que ocorreram enquanto essa era a etapa mais recente que o usuário recebeu.

{% details Casos de uso %}

#### Caso de uso 1

Há uma jornada de canva com 10 notificações por push e o evento de conversão é "início de sessão" ("Abre o app"): 

- O usuário A abre o app após entrar, mas antes de receber a primeira mensagem.
- O usuário B abre o app após cada notificação por push.

**Resultado:**
O resumo mostrará duas conversões, enquanto as etapas individuais mostrarão uma conversão de uma na primeira etapa e zero para todas as etapas subsequentes.

{% alert note %}
Se o horário de silêncio estiver ativo quando o evento de conversão acontecer, as mesmas regras se aplicam.
{% endalert %}

#### Caso de uso 2

Há um canva de uma etapa com horário de silêncio:

1. Usuário entra na canva.
2. Primeira etapa não tem postergação, mas está dentro do horário de silêncio, então a mensagem é suprimida.
3. Usuário realiza o evento de conversão.

**Resultado:**
O usuário será contado como convertido na variante geral da canva, mas não na etapa, pois não recebeu a etapa.

{% enddetails %}

{% endapi %}
{% api %}

### Ao observar o número de usuários únicos, a análise de dados do canva ou o segmentador é mais precisa?

{% apitags %}
Canvas
{% endapitags %}

O segmentador é uma estatística mais precisa para dados de usuários únicos em comparação com canva ou estatísticas de campanha. Isso ocorre porque as estatísticas de canva e campanha são números que a Braze incrementa quando algo acontece—o que significa que há variáveis que podem resultar nesse número ser diferente do segmentador. Por exemplo, os usuários podem converter mais de uma vez para uma canva ou campanha.  

{% endapi %}
{% api %}

### Por que o número de usuários entrando em uma canva não corresponde ao número esperado?

{% apitags %}
Canvas
{% endapitags %}

O número de usuários que entram em uma canva pode diferir do número esperado devido à forma como os públicos e gatilhos são avaliados. Na Braze, um público é avaliado antes do disparador (a menos que esteja usando um disparador de [alteração de atribuição]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/attribute_triggers/#change-custom-attribute-value)). Isso fará com que os usuários saiam da canva se não fizerem parte do seu público selecionado antes que qualquer ação de disparar seja avaliada.

{% endapi %}
{% api %}

<!-- Analytics -->

### Quais métricas a Braze mede?

{% apitags %}
Análise de dados
{% endapitags %}

Dependendo do canal, a Braze mede uma variedade de métricas para ativar você a determinar o sucesso de uma campanha e informar as futuras. Você pode encontrar uma lista abrangente em nosso [glossário de métricas de relatório]({{site.baseurl}}/user_guide/data/report_metrics/).

{% endapi %}
{% api %}

### Como a receita é calculada no Braze?

{% apitags %}
Análise de dados
{% endapitags %}

Na página **Receita**, você pode visualizar dados sobre receita ou compras em períodos específicos, para um produto específico, ou a receita ou compras totais do seu app. Estes números de receita são gerados a partir das compras feitas pelos destinatários da campanha dentro de um certo período de conversão.

Dito isso, é importante notar que a Braze é uma ferramenta de marketing e não uma ferramenta de gestão de receita. Nosso [objeto de compra]({{site.baseurl}}/api/objects_filters/purchase_object/) não suporta reembolsos e cancelamentos, então você pode ver discrepâncias ao comparar dados com outras ferramentas.

{% endapi %}
{% api %}

### Quais capacidades de relatórios o Currents permite?

{% apitags %}
Análise de dados
{% endapitags %}

Nossa ferramenta Currents transmite continuamente tanto o envio de mensagens quanto os dados de engajamento e comportamento do cliente para um de nossos muitos parceiros de dados, capacitando você a usar os dados únicos e valiosos que a Braze cria para impulsionar seus esforços de business intelligence e análise de dados em outros parceiros de melhor qualidade.

Esses dados vão além das métricas de engajamento de envio de mensagens e também podem incluir números mais complexos, como atributo personalizado e performance de eventos. Para mais informações, acesse nosso [glossário de eventos do Currents]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/customer_behavior_events/).

{% endapi %}
{% api %}

### Como posso agendar um relatório de engajamento recorrente?

{% apitags %}
Análise de dados
{% endapitags %}

Para agendar um relatório de engajamento recorrente, faça o seguinte:

1. No seu dashboard, navegue até **Relatórios de Engajamento**, em **Dados**.
2. Clique em **\+ Criar Novo Relatório**.
3. Adicione as [campanhas e mensagens de canva]({{site.baseurl}}/user_guide/data_and_analytics/reporting/engagement_reports/#manually-select-campaigns-or-canvases) (individualmente ou [por tag]({{site.baseurl}}/user_guide/data_and_analytics/reporting/engagement_reports/#automatically-select-campaigns-or-canvases)) que você gostaria de compilar em seu relatório.
4. [Adicione estatísticas]({{site.baseurl}}/user_guide/data_and_analytics/reporting/engagement_reports/#add-statistics-to-your-report) ao seu relatório.
5. Selecione a compressão e o delimitador para o seu relatório.
6. Insira os endereços de e-mail dos usuários da Braze que devem receber este relatório.
7. Selecione o [período de tempo]({{site.baseurl}}/user_guide/data_and_analytics/reporting/engagement_reports/#time-frame) a partir do qual você gostaria que seu relatório executasse os dados.
8. Selecione os [intervalos (diários, semanais, etc.)]({{site.baseurl}}/user_guide/data_and_analytics/reporting/engagement_reports/#data-display) nos quais gostaria de ver a divisão dos seus dados.
9. Agende seu relatório para [enviar imediatamente]({{site.baseurl}}/user_guide/data_and_analytics/reporting/engagement_reports/#send-immediately) ou em um [momento futuro especificado]({{site.baseurl}}/user_guide/data_and_analytics/reporting/engagement_reports/#send-at-designated-time).
10. Execute o relatório, depois abra-o no seu e-mail quando ele chegar!

{% endapi %}
{% api %}

### Qual é a diferença entre Relatórios de Engajamento e o Construtor de Relatórios?

{% apitags %}
Análise de dados
{% endapitags %}

Relatórios de engajamento fornecem a você CSVs de estatísticas de engajamento para mensagens específicas de campanhas e canvas via um e-mail acionado. Certos dados são agregados no nível da campanha ou canva em comparação com o nível da variante individual ou etapa. Os relatórios não são salvos no dashboard, e reexecutar o relatório pode resultar em estatísticas atualizadas.

O Construtor de Relatórios permite que você compare os resultados de várias campanhas ou canvas em uma única visualização, para que você possa determinar facilmente quais estratégias de engajamento mais impactaram suas métricas principais. Para ambas as campanhas e canvas, você pode exportar seus dados e salvar seu relatório para visualizar no futuro.

Para saber mais sobre os usos de relatórios e análise de dados na Braze, consulte [visão geral dos relatórios]({{site.baseurl}}/user_guide/analytics/reporting/reports_overview/).

{% endapi %}

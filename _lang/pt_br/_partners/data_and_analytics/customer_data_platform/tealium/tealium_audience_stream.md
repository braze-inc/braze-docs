---
nav_title: Tealium AudienceStream
article_title: Tealium AudienceStream
page_order: 2
alias: /partners/tealium_audience_stream/
description: "Este artigo de referência descreve a parceria entre a Braze e a Tealium, um hub de dados universal que permite conectar dados móveis, da Web e de outros tipos a fontes de terceiros."
page_type: partner
search_tag: Partner

---

# Tealium AudienceStream

> O [Tealium AudienceStream](https://docs.tealium.com/server-side/getting-started/audiencestream-cdp/introduction/) é um mecanismo de segmentação de clientes omnicanal com atuação em tempo real. O AudienceStream utiliza os dados que fluem para o EventStream e cria perfis de visitantes que representam os atributos mais importantes do engajamento de seus clientes com sua marca. 

A integração do Braze e da Tealium utiliza os perfis de visitantes do AudienceStream. Os comportamentos compartilhados segmentam esses perfis para criar conjuntos de visitantes com características comuns, conhecidos como públicos. Esses públicos podem ajudar a alimentar sua stack de tecnologia de marketing em tempo real por meio de conectores. 

{% alert important %}
O Tealium AudienceStreams e o EventStream oferecem ações de conector com e sem lote. O conector sem lote deve ser usado quando as solicitações em tempo real forem importantes para o caso de uso e não houver preocupações quanto a atingir as especificações do limite de frequência da API do Braze. Entre em contato com [suporte]({{site.baseurl}}/braze_support/) da Braze ou com seu gerente de sucesso do cliente se tiver alguma dúvida.
{% endalert %}

## Pré-requisitos

| Nome | Descrição |
| ---- | ----------- |
| Conta Tealium | É necessária uma [conta Tealium](https://my.tealiumiq.com/) com acesso ao lado do servidor. Recomendamos que você também use as integrações do lado do cliente para aproveitar essa parceria. |
| Chave da API REST | Uma chave da API REST da Braze com as permissões `users.track`, `users.delete` e `subscription.status.set`.<br><br>Isso pode ser criado no **Dashboard do Braze > Console de desenvolvedor > Chave da API REST > Criar nova chave de API**|
| [Endpoint REST  do Braze]({{site.baseurl}}/api/basics/#endpoints) | Sua URL de endpoint REST. Seu endpoint dependerá da [URL do Braze para sua instância]({{site.baseurl}}/api/basics/#endpoints). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integração

### Etapa 1: configurar atributos e emblemas

#### Entendendo as atributos

A primeira etapa do uso do AudienceStream é a criação de atributos. As atribuições permitem que você defina as características importantes que representam os hábitos, as preferências, as ações e o engajamento de um visitante com a sua marca. 

**Atribuições da visita**: As atribuições de visita estão relacionadas à visita (ou sessão) atual do usuário. Os dados armazenados nessas atribuições persistem durante a duração da visita. Alguns exemplos de atribuições de visitas incluem:
- Duração da visita (número)
- Navegador atual (String)
- Dispositivo atual (String)
- Contagem de visualizações de página (número)

**Atribuições do visitante**: As atribuições do visitante estão relacionadas ao usuário atual. Os dados armazenados nesses atributos persistem por toda a vida do usuário. Alguns exemplos de atribuições de visitantes incluem: 
- Valor dos pedidos no tempo de vida (número)
- Nome (String)
- Data de nascimento (Data)
- Marcas de compras (registro)

Visite o [Tealium](https://docs.tealium.com/server-side/attributes/about/) para obter uma lista completa dos tipos de dados disponíveis.

##### Enriquecimento de atribuições

Depois de identificar as atribuições desejadas, você pode configurá-las com [enriquecimentos](https://docs.tealium.com/server-side/getting-started/audiencestream-cdp/attributes-enrichments/) \- regras de negócios que determinam quando e como atualizar os valores dos atributos. Cada tipo de dados oferece sua própria seleção de enriquecimentos para manipular o valor do atributo. Isso está associado à configuração "WHEN". As seguintes opções estão disponíveis para cada visita e atribuição de visitante:

- Novo visitante: ocorre na primeira vez que um visitante chega ao seu site.
- Nova visita: ocorre em uma nova visita de um visitante.
- Any Event: ocorre em qualquer evento.
- Visit Ended: ocorre quando uma visita termina.

Você também pode criar uma condição personalizada, chamada de regra, que determinará quando o enriquecimento ocorrerá.

#### Emblemas

Os emblemas são atribuições especiais do visitante que representam padrões de comportamento valiosos. Os crachás são atribuídos ou removidos dos visitantes com base na lógica de seus enriquecimentos. Essa lógica geralmente combina várias condições para capturar segmentos de visitantes ou define um limite para quando um determinado valor é atingido.

#### Exemplo de atributo e emblema

{% tabs local %}
{% tab Atribuição %}

Crie um atributo de visitante "Valor do tempo de vida do pedido" que calcule o valor cumulativo gasto (`order_total`) pelo cliente para todos os pedidos concluídos (evento de compra). Para configurar o valor dos pedidos no tempo de vida na sua conta Tealium, siga as instruções a seguir:

1. Navegue até **AudienceStream > Visitor/Visit Attributes** (AudienceStream > Atributos de visitante/visita) e clique em **Add Attribute** (Adicionar atributo).
2. Selecione o escopo como **Visitante** e clique em **Continuar**.
3. Selecione o tipo de dados **Número** e clique em **Continuar**.
4. Digite o nome do atributo, "Valor dos pedidos no tempo de vida".
5. Clique em **Add Enrichment** (Adicionar enriquecimento) e selecione **Increment or Decrement Number** (Aumentar ou diminuir número.
6. Selecione a atribuição que contém o valor a ser incrementado (`order_total`).
7. Deixe a opção "WHEN" (Quando) definida como "Any Event" (Qualquer evento) e clique em **Create a New Rule (Criar uma nova regra**).
8. Crie uma regra que identifique a ocorrência de um evento de compra.
9. Clique em **Save (Salvar**) e, em seguida, em **Finish (Concluir**).

Agora todos os clientes terão um atributo de valor dos pedidos no tempo de vida.

{% endtab %}
{% tab Badge %}

Você pode criar emblemas que o ajudem a classificar e direcionar seus usuários por determinadas atribuições que eles compartilham. No exemplo a seguir, criamos um emblema VIP para usuários com um "Valor dos pedidos no tempo de vida" superior a $ 500.

1. Navegue até **AudienceStream > Visitor/Visit Attributes** (AudienceStream > Atributos de visitante/visita) e clique em **Add Attribute** (Adicionar atributo).
2. Selecione o escopo como **Visitante** e clique em **Continuar**.
3. Selecione o tipo de dados **Badge** e clique em **Continue**.
4. Digite o nome do emblema, "VIP".
5. Clique em **Add Enrichment** e selecione **Atribuir crachá**.
6. Deixe a opção "WHEN" (quando) definida como "Any Event" (qualquer evento).
7. Crie uma regra para atribuição de crachá selecionando **Criar regra**. Atribua um título a essa regra e, usando o atributo criado anteriormente, defina a regra como "...tem atributo 'Valor dos pedidos no tempo de vida' maior que 500".
8. Clique em **Save (Salvar**) e, em seguida, em **Finish (Concluir**).

{% endtab %}
{% endtabs %}

### Etapa 2: Criar um público

Na página inicial do Tealium, selecione **Públicos** em **AudienceStream** na barra de navegação lateral. Aqui, você pode criar um público de usuários com atribuições comuns. A entrada ou saída de um usuário desse público será o disparo da ação do conector, configurada na próxima etapa, que passa essas informações para o perfil do usuário no Braze. 

Primeiro nomeie seu público e, em seguida, considere quais atributos se aplicariam ao tipo de público que está tentando criar. Por exemplo, para criar um público de usuários VIP, você pode criar um público de visitantes que tenham o **emblema VIP**.

Não se esqueça de **Salvar / Publicar** seu público quando terminar.

### Etapa 3: Criar um conector de eventos

Um conector é uma integração entre a Tealium e outro fornecedor usada para transmitir dados. Esses conectores contêm ações que representam as APIs suportadas por seus parceiros. 

1. Na barra lateral da Tealium, em **Server-Side** (Lado do servidor), navegue até **AudienceStream > Audience Connectors** (AudienceStream > Conectores de público).
2. Selecione o botão azul **\+ Add Connector** (+ Adicionar conector) para examinar o marketplace de conectores. Na nova caixa de diálogo que aparece, use a busca por holofotes para encontrar o conector **Braze**.
3. Para adicionar esse conector, clique no bloco do conector **Braze**. Em seguida, você verá o resumo da conexão e uma lista das informações necessárias, ações compatíveis e instruções de configuração. A configuração compreende três etapas: fonte, configuração e ação.

#### Origem

Na caixa de diálogo **Source (Fonte)** exibida, selecione o público criado na etapa anterior e um disparador que considere adequado à sua situação. Você também pode ativar o limite de frequência para controlar a frequência com que essa ação é disparada. 

![]({% image_buster /assets/img/tealium/create_source.png %}){: style="max-width:90%;"}

#### Configuração

Em seguida, será exibida a caixa de diálogo **Configuração** (Configuration). Selecione **Add Connector (Adicionar conector** ) na parte inferior da página. Dê um nome ao seu conector e forneça seu endpoint da API do Braze e a chave da API REST do Braze aqui.

![]({% image_buster /assets/img/tealium/create_configuration.png %}){: style="max-width:70%;"}

Se já tiver criado um conector anteriormente, você poderá usar um conector existente da lista de conectores disponíveis e modificá-lo para atender às suas necessidades com o ícone de lápis ou excluí-lo com o ícone de lixeira. 

Depois de criar ou selecionar um conector para vincular esse público, clique em Done (Concluído) para continuar.

#### Ação

Em seguida, nomeie sua ação de conector e selecione um tipo de ação que enviará dados de acordo com o mapeamento a ser configurado. Aqui, você mapeará as atribuições do Braze para os nomes de atributos do Tealium. Os campos exigidos pela Tealium variam de acordo com o tipo de ação escolhido. A seguir, exemplos e explicações sobre esses campos.

{% alert important %}
Nem todos os campos oferecidos são obrigatórios.

![]({% image_buster /assets/img/tealium/minimize.gif %}){: style="max-width:90%"}
{% endalert %}

{% tabs local %}
{% tab Rastreamento de usuário - lote e não lote %}

Essa ação permite rastrear atributos de usuário, evento e compra, tudo em uma única ação. Embora a ação "Rastrear usuário" seja a mesma para AudienceStream e EventStream, a Tealium recomenda definir mapeamentos de atributo de usuário com ações AudienceStream e mapeamentos de evento e compra com ações EventStream.

| Parâmetros | Descrição |
| ---------- | ----------- |
| ID de usuário | Use esse campo para mapear o campo de ID do usuário do Tealium para seu equivalente no Braze. Mapeie uma ou mais atribuições de ID de usuário. Quando várias IDs são especificadas, o primeiro valor não em branco é escolhido com base na seguinte ordem de prioridade: ID externo, ID da Braze, nome do alias e etiqueta do alias.<br><br>\- A ID externa e a ID Braze não devem ser especificadas se estiver importando tokens por push.<br>\- Se estiver especificando um alias de usuário, o nome do alias e o rótulo do alias devem ser definidos. <br><br>Para saber mais, confira o [endpoint `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) da Braze. |
| Atributos do usuário | Use os nomes de campo existentes do perfil de usuário do Braze para atualizar os valores do perfil de usuário no dashboard do Braze ou adicione seus próprios dados [de atributos]({{site.baseurl}}/api/objects_filters/user_attributes_object/) personalizados [de usuários]({{site.baseurl}}/api/objects_filters/user_attributes_object/) aos perfis de usuários.<br><br>\- Por padrão, novos usuários serão criados se não houver nenhum.<br>\- Ao definir **Update Existing Only** como `true`, somente os usuários existentes serão atualizados, e nenhum novo usuário será criado.<br>\- Se um atributo da Tealium estiver vazio, ele será convertido em nulo e removido do perfil de usuário da Braze. Os enriquecimentos devem ser usados se os valores nulos não devem ser enviados ao Braze para remover uma atribuição de usuário. |
| Modificar atributos do usuário | Use esse campo para incrementar ou decrementar certas atribuições do usuário<br><br>\- As atribuições de números inteiros podem ser incrementadas por números inteiros positivos ou negativos.<br>\- As atribuições das matrizes podem ser modificadas adicionando ou removendo valores das matrizes existentes. |
| Evento | Um evento representa uma única ocorrência de um evento personalizado por um usuário específico em um registro de data e hora. Use esse campo para rastrear e mapear atribuições de eventos como as do [objeto de evento]({{site.baseurl}}/api/objects_filters/event_object/) Braze. <br><br>\- O atributo de evento `Name` é necessário para cada evento mapeado.<br>\- O atributo de evento `Time` é automaticamente definido para a hora atual, a menos que seja explicitamente mapeado. <br>\- Por padrão, novos eventos serão criados se não houver nenhum. Ao definir `Update Existing Only` como `true`, somente os eventos existentes serão atualizados, e nenhum novo evento será criado.<br>\- Atribuições do tipo matriz de mapas para adicionar vários eventos. As atribuições do tipo matriz devem ter o mesmo comprimento.<br>\- Atributos de valor único podem ser usados e aplicados a cada evento. |
| Modelo de evento | Fornecer modelos de eventos a serem referenciados nos dados do corpo. Os modelos podem ser usados para transformar os dados antes de enviá-los ao Braze. Consulte o [Guia de modelos](https://docs.tealium.com/server-side/connectors/webhook-connectors/trimou-templating-engine/) da Tealium para saber mais. |
| Variável de modelo de evento | Forneça variáveis de modelo de evento como entrada de dados. Consulte o [Guia de variáveis de modelo](https://docs.tealium.com/server-side/connectors/webhook-connectors/template-variables/) da Tealium para saber mais. |
| Compra | Use esse campo para rastrear e mapear as atribuições de compra do usuário, como as do [objeto de compra]({{site.baseurl}}/api/objects_filters/purchase_object/) Braze.<br><br>\- Os atributos de compra `Product ID`, `Currency` e `Price` são necessários para cada compra mapeada.<br>\- O atributo de compra `Time` é automaticamente definido para a hora atual, a menos que seja explicitamente mapeado.<br>\- Por padrão, novas compras serão criadas se não houver uma. Ao definir `Update Existing Only` como `true`, somente as compras existentes serão atualizadas, e nenhuma nova compra será criada.<br>\- Mapeie atribuições do tipo matriz para adicionar vários itens de compra. As atribuições do tipo matriz devem ter o mesmo comprimento.<br>\- Os atributos de valor único podem ser usados e se aplicarão a cada item.|
| Modelo de compra | Os modelos podem ser usados para transformar os dados antes de serem enviados ao Braze.<br>\- Defina um modelo de compra se você precisar de suporte a objetos aninhados.<br>\- Quando um modelo de compra é definido, a configuração definida na seção de compras da sua ação será ignorada.<br>\- Consulte o [Guia de modelos](https://docs.tealium.com/server-side/connectors/webhook-connectors/trimou-templating-engine/) da Tealium para saber mais.|
| Variável do modelo de compra | Forneça variáveis de modelo de produto como entrada de dados. Consulte o [Guia de variáveis de modelo](https://docs.tealium.com/server-side/connectors/webhook-connectors/template-variables/) da Tealium para saber mais. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![]({% image_buster /assets/img/tealium/track_user_example2.png %}){: style="max-width:90%"}

{% endtab %}
{% tab Excluir usuário - Não lote %}

Essa ação permite excluir usuários do dashboard do Braze.

| Parâmetros | Descrição |
| ---------- | ----------- |
| ID de usuário | Use esse campo para mapear o campo de ID de usuário do Tealium para seu equivalente no Braze.<br><br>\- Mapeie uma ou mais atribuições de ID de usuário. Quando várias IDs são especificadas, o primeiro valor não em branco é escolhido com base na seguinte ordem de prioridade: ID externo, ID da Braze, nome do alias e etiqueta do alias.<br>\- Ao especificar um alias de usuário, o nome do alias e a etiqueta do alias devem ser definidos.<br><br>Para saber mais, consulte o [endpoint `/users/delete`]({{site.baseurl}}/api/endpoints/user_data/post_user_delete/) da Braze. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![]({% image_buster /assets/img/tealium/track_user_delete2.png %}){: style="max-width:90%"}

{% endtab %}
{% tab Atualizar Status do Grupo de Inscrições do Usuário - Não em Lote %}
Essa ação permite adicionar ou remover usuários dos grupos de inscrições para e-mail ou SMS do Braze.

| Parâmetros | Descrição |
| ---------- | ----------- |
| Tipo de grupo | Use esse campo para indicar se esse é um grupo de inscrições para SMS ou para e-mail. |
| Tipo de atualização | Mapeie essa ação para um evento de cancelamento de inscrição ou de inscrição 
| Atributos | \- ID do grupo de inscrições (obrigatório): O ID do grupo de inscrições relacionado ao tipo de grupo mapeado no campo anterior.<br>\- ID externa: A ID externa do usuário.<br><br>Grupo de e-mail específico:<br>\- E-mail: O endereço de e-mail do usuário.<br>**Se o ID externo não estiver definido, o e-mail será solicitado.**<br><br>Específico do grupo de SMS:<br>\- Telefone: O número de telefone no formato E.164. Por exemplo, +14155552671.<br>**Se o ID externo não estiver definido, o telefone será solicitado.** |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![]({% image_buster /assets/img/tealium/update_subscription.png %}){: style="max-width:90%"}

{% endtab %}
{% endtabs %}

Selecione **Finish (Acabamento**).

#### Resumo

Visualize o resumo do conector que você criou. Se quiser modificar as opções escolhidas, selecione **Back (Voltar** ) para editar ou **Finish (Concluir** ) para concluir.

Seu conector agora é exibido na lista de conectores na página inicial da Tealium.

Não se esqueça de salvar ou publicar seu conector quando terminar. As ações que você configurou passarão a ser acionadas acionadas quando as conexões do gatilho forem atendidas. 

### Etapa 4: Teste seu conector Tealium

Depois que o conector estiver instalado e funcionando, teste-o para garantir que esteja funcionando corretamente. A maneira mais simples de testar isso é usar a Tealium **Trace Tool**. Para começar a usar o Trace, confirme se adicionou a extensão de navegador Tealium Tools.

1. Para iniciar um novo rastreamento, encontre **Server-Side** (Lado do servidor) na barra lateral e selecione **Trace** (Rastrear). Clique em **Iniciar** e capture a ID do rastreamento.
2. Abra a extensão do navegador e insira a ID do rastreamento no AudienceStream Trace.
3. Examine o registro em tempo real.
4. Verifique a ação que deseja validar clicando na entrada **Actions Triggered (Ações disparadas)** para expandi-la.
5. Procure a ação que deseja validar e visualize o status do registro. 

Consulte a [documentação de rastreamento](https://docs.tealium.com/server-side/connectors/trace/about/) da Tealium para obter instruções mais detalhadas sobre a implementação da ferramenta de rastreamento da Tealium.

## Demonstração da integração

<div class="video-container">
  <iframe width="560" height="315" src="https://drive.google.com/file/d/1m2JI4vdFt3fDePBdVvVcQWEjbC82ApGA/preview" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

## Potenciais excedentes de pontos de dados

Há três maneiras principais que podem fazer você atingir acidentalmente o excedente de dados ao integrar a Braze pela Tealium:

#### Envio de dados duplicados - envie apenas deltas Braze de atribuições
O Tealium não envia ao Braze deltas de atribuições do usuário. Por exemplo, se você tiver uma ação EventStream que rastreia o nome, o e-mail e o número de telefone celular de um usuário, a Tealium enviará os três atributos à Braze sempre que a ação for disparada. A Tealium não procurará o que mudou ou foi atualizado e enviará apenas essas informações.<br><br> 
**Solução**: <br>Você pode verificar seu backend para avaliar se uma atribuição foi alterada ou não e, em caso afirmativo, chamar os métodos relevantes do Tealium para atualizar o perfil do usuário. **Isso é o que os usuários que integram o Braze diretamente costumam fazer.** <br>**OU**<br> Se você não armazenar sua própria versão de um perfil de usuário no backend e não puder saber se as atribuições mudam ou não, poderá usar o AudienceStream e [criar enriquecimentos](https://docs.tealium.com/server-side/attributes/manage-enrichments/add-enrichment/) para enviar atributos de usuário somente quando os valores forem alterados. 

#### Envio de dados irrelevantes ou substituição desnecessária de dados
Se você tiver vários EventStream que direcionam o mesmo feed de eventos, **todas as ações ativadas para esse conector** serão disparadas automaticamente sempre que uma única ação for disparada, **o que também pode resultar na substituição de dados no Braze.**<br><br>
**Solução**: <br>Configure uma especificação de evento ou feed separado para rastrear cada ação. <br>**OU**<br> Desative as ações (ou conectores) que você não deseja disparar usando os botões de alternância no dashboard do Tealium.

#### Inicialização do Braze muito cedo
Os usuários que se integram à Tealium usando a tag SDK para Web da Braze podem observar um aumento drástico no MAU. **Se for inicializada no carregamento da página, a Braze criará um perfil anônimo sempre que um usuário da Web navegar no site pela primeira vez.** Alguns podem querer rastrear o comportamento do usuário somente quando ele tiver concluído alguma ação, como "feito login" ou "assistido a um vídeo", para reduzir a contagem de MAU. <br><br>
**Solução**: <br>Configure [regras de carregamento](https://docs.tealium.com/iq-tag-management/load-rules/about/) para determinar exatamente quando e onde uma tag é carregada em seu site.


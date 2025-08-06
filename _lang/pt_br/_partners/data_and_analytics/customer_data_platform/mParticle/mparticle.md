---
nav_title: mParticle por Rokt
article_title: mParticle por Rokt
alias: /partners/mparticle/
description: "Este artigo de referência descreve a parceria entre o Braze e a mParticle, uma plataforma de dados do cliente que coleta e encaminha informações entre fontes em sua pilha de marketing."
page_type: partner
search_tag: Partner

---

# mParticle por Rokt

{% multi_lang_include video.html id="Njhqwd36gZM" align="right" %}

> A plataforma de dados de cliente da mParticle ajuda você a fazer mais com os dados existentes. Os melhores profissionais de marketing usam a mParticle para orquestrar dados entre todo o growth stack, para vencer em momentos importantes da jornada do cliente.

A integração entre a Braze e o mParticle permite que você controle com praticidade o fluxo de informações entre os dois sistemas:
- Sincronize os públicos do mParticle com a Braze para segmentação de campanhas e Canvas na Braze.
- Compartilhe dados entre as duas plataformas. Isso pode ser feito por meio da integração do kit mParticle e da integração de servidor a servidor.
- [Envie a interação do usuário da Braze para a mParticle por meio do Currents]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/mparticle/mparticle_for_currents/), tornando-a acionável em todo o growth stack. 

## Pré-requisitos

| Requisito | Descrição |
| ----------- | ----------- |
| Conta mParticle | É necessário ter uma [conta mParticle](https://app.mparticle.com/login) para usar essa parceria. |
| Instância do Braze | Sua instância do Braze pode ser encontrada na [página de visão geral da API]({{site.baseurl}}/api/basics/#endpoints) (por exemplo, `US-01` ou `US-02`). |
| Chave do identificador do app Braze | A chave do identificador de seu app. <br><br>Ela pode ser encontrada em **Dashboard da Braze > Gerenciar configurações > Chave de API**. |
| Chave da API REST do espaço de trabalho | (Servidor para servidor) Uma chave da API REST do Braze<br><br>Isso pode ser criado no **Dashboard da Braze > Console de desenvolvedor > Configurações de API > Chave de API**. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integração

### Públicos

Use a parceria entre o Braze e a mParticle para configurar sua integração e importar públicos da mParticle diretamente para o Braze para redirecionamento, criando um ciclo completo de dados de um sistema para outro. Qualquer integração que você configurar será contabilizada no volume de pontos de dados da sua conta.

#### Encaminhamento de públicos

O mParticle oferece três maneiras de definir atribuições de membros de coorte, controladas pela configuração [Send Segments As](#send_settings) (Enviar segmentos como). Consulte as seções a seguir para saber o processamento de cada opção:

- [Atribuição de string única](#string)
- [Atribuição de uma única matriz](#array)
- [Uma atribuição por segmento](#per-segment)
- [Atributo de matriz única e atributo de string única](#both-1)
- [Atributo de matriz única e um atributo por segmento](#both-2)
- [Atributo de string única e um atributo por segmento](#both-3)
- [Atributo de matriz única, atributo de string única e um atributo por segmento](#multi)

##### Atribuição de string única {#string}

A mParticle criará um único atributo personalizado chamado `SegmentMembership`. O valor dessa atribuição é uma string de IDs de público mParticle separados por vírgulas que correspondem ao usuário. Esses IDs de público podem ser encontrados no dashboard da mParticle, em **Audiences** (Públicos).

Por exemplo, se um público do mParticle "Ibiza dreamers" tiver um ID de público de "11036", você poderá segmentar esses usuários com o filtro `SegmentMembership` - `matches regex` - `11036`.

Embora essa seja a opção padrão no mParticle, a maioria dos usuários do Braze aceita usar [atribuições de matriz única](#array) para a experiência de filtragem ao criar segmentos no Braze.

{% alert important %}
Essa solução não é recomendada se você tiver mais do que alguns públicos porque os atributos personalizados podem ter até 255 caracteres, portanto, não será possível armazenar dezenas ou centenas de públicos em um perfil de usuário usando esse método. Se tiver um grande número de coortes por usuário, recomendamos fortemente a configuração "uma atributo por segmento".
{% endalert %}

![Associação do segmento mParticle]({% image_buster /assets/img_archive/mparticle1.png %})

##### Atribuição de uma única matriz {#array}

A mParticle cria um único atributo personalizado de matriz na Braze para cada usuário, chamado `SegmentMembershipArray`. O valor dessa atribuição é uma matriz de IDs de público do mParticle que correspondem ao usuário.

Por exemplo, se um usuário for membro de três públicos da mParticle com os IDs de público "13053", "13052" e "13051", você poderá segmentar os usuários que correspondem a um desses públicos com o filtro `SegmentMembershipArray` — `includes value` — `13051`.

{% alert note %}
As atribuições da matriz da Braze têm um comprimento máximo de 25. Se algum de seus usuários for membro de mais de 25 públicos, as informações de associação serão truncadas pelo Braze. Para contornar esse problema, entre em contato com o representante da Braze para aumentar o limite máximo de comprimento da matriz.
{% endalert %}

##### Uma atribuição por segmento {#per-segment}

O mParticle criará um atributo personalizado booleano para cada público ao qual o usuário pertence. Por exemplo, se um público da mParticle for chamado de "Possíveis parisienses", você poderá segmentar esses usuários com o filtro `In Possible Parisians` - `equals` - `true`.

![Atributo personalizado mParticle]({% image_buster /assets/img_archive/mparticle2.png %})

##### Atributo de matriz única e atributo de string única {#both-1}

A mParticle enviará atributos conforme descrito pelo atributo de matriz única e pelo atributo de string única.

##### Atributo de matriz única e um atributo por segmento {#both-2}

O mParticle enviará atribuições conforme descrito pelo atributo de matriz única e um atributo por segmento.

##### Atributo de string única e um atributo por segmento {#both-3}

O mParticle enviará atribuições conforme descrito pelo atributo de string única e um atributo por segmento.

##### Atributo de matriz única, atributo de string única e um atributo por segmento {#multi}

O mParticle enviará atribuições conforme descrito por um único atributo de matriz, um único atributo de string e um atributo por segmento.

#### Etapa 1: Criar um público no mParticle {#send_settings}

Para criar um público no mParticle:

1. Navegue até **Audiences** > **Single Workspace** > **\+ New Audience** (Públicos > Espaço de trabalho único > + Novo público).
2. Para conectar a Braze como uma saída para seu público, você deve fornecer os seguintes campos:

| Nome do campo               | Descrição                                                                                                                                                                   |
| ------------------------ | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Chave de API                  | Encontrado no dashboard do Braze em **Configurações** > **Chaves de API**.<br><br>Se estiver usando a navegação mais antiga, poderá encontrar as chaves de API em **Console do desenvolvedor** > **Configurações de API**. |
| Sistema operacional da chave de API | Selecione a qual sistema operacional sua chave de API da Braze corresponde. Essa seleção limitará os tipos de tokens por push encaminhados em uma atualização do público.                          |
| Enviar segmentos como         | O método de envio de públicos para o Braze. Consulte a seção [Encaminhamento de públicos](#forwarding-audiences) para obter detalhes.                                                          |
| Chave da API REST do espaço de trabalho   | Chave da API REST do Braze com permissões completas. Isso pode ser criado no dashboard do Braze em **Configurações** > **Chaves de API**.                                                        |
| Tipo de identidade externa   | O tipo de identidade do usuário mParticle a ser encaminhado como uma ID externa para o Braze. Recomendamos deixar esse valor como padrão, ID do cliente.                                          |
| Tipo de identidade de e-mail      | O tipo de identidade de usuário do mParticle a ser encaminhado como o e-mail para o Braze.                                                                                                            |
| Instâncias da Braze           | Especifique para qual cluster seus dados do Braze serão encaminhados.                                                                                                                   |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{:start="3"}
3\. Por fim, **salve** seu público.

Você deverá começar a ver os públicos sendo sincronizados com o Braze em alguns minutos. A inscrição do público só será atualizada para usuários com `external_ids` (ou seja, usuários não anônimos). Para saber mais sobre como criar o público da Braze mParticle, consulte a documentação da mParticle em [Configurações](https://docs.mparticle.com/integrations/braze/audience/#configuration-settings).

#### Etapa 2: Usuários do segmento no Braze

No Braze, para criar um segmento desses usuários, navegue até **Segments (Segmentos** ) em **Engagement (Engajamento)** e nomeie seu segmento. A seguir, dois exemplos de segmentos, dependendo da opção selecionada para **Enviar segmentos como**. Para obter mais detalhes sobre cada opção, consulte [Encaminhamento de públicos](#forwarding-audiences.)

- **Atribuição de matriz única:** Selecione `SegmentMembershipArray` como seu filtro. Em seguida, use a opção "includes value" e insira o ID do público desejado. ![mParticle segment filter "SegmentMembershipArray" set as "includes value" and audience ID.]({% image_buster /assets/img_archive/mparticle5.png %})<br><br>
- **Uma atribuição por segmento:** Selecione seu atributo personalizado como o filtro. Em seguida, use a opção "equals" e escolha a lógica apropriada. ![mParticle segment filter "in possible parisians" set as "equals" and "true".]({% image_buster /assets/img_archive/mparticle3.png %})

Depois de salvo, você pode fazer referência a esse segmento durante a criação do Canva ou da campanha na etapa de direcionamento de usuários.

#### Desativação e exclusão de conexões

Como o mParticle não mantém segmentos diretamente no Braze, ele não excluirá segmentos quando a conexão do público correspondente do mParticle for excluída ou desativada. Quando isso acontecer, o mParticle não atualizará as atribuições do usuário do público na Braze para remover o público de cada usuário.

Para remover o público de um usuário da Braze antes da exclusão, primeiro ajuste os filtros de público para forçar o tamanho do público a 0. Depois que o cálculo do público for concluído e retornar 0 usuário, exclua o público. Em seguida, a associação do público será atualizada na Braze para `false` para a opção de atribuição única ou removerá o ID do público do formato de matriz.

## Mapeamento de dados

Os dados podem ser mapeados para o Braze usando a [integração do kit incorporado](#embedded-kit-integration) se você quiser conectar seus aplicativos móveis e da Web ao Braze por meio do mParticle. Você também pode usar a [integração API de servidor para servidor](#server-api-integration) para encaminhar dados do lado do servidor para o Braze.

Independentemente da abordagem escolhida, configure a Braze como saída:

### Configure suas definições de saída do Braze

Na mParticle, navegue até **Setup > Outputs > Add Outputs** (Configuração > Saídas > Adicionar saídas) e selecione **Braze** para abrir a configuração do kit da Braze. **Salvar** quando concluído.

| Nome da configuração | Descrição |
| ------------ | ----------- |
| Chave do identificador do app Braze | Sua chave de identificador do app Braze pode ser encontrada no dashboard do Braze em **Configurações** > **Chaves de API**. Observe que as chaves de API serão diferentes para cada plataforma (iOS, Android e Web). |
| Tipo de identidade externa | O tipo de identidade do usuário mParticle a ser encaminhado como uma ID externa para o Braze. Recomendamos deixar esse valor como padrão, ID do cliente. |
| Tipo de identidade de e-mail | O tipo de identidade de usuário do mParticle a ser encaminhado como um e-mail para o Braze. Recomendamos deixar esse valor como padrão, E-mail, |
| Instâncias da Braze | O cluster para o qual seus dados do Braze serão encaminhados; esse deve ser o mesmo cluster em que seu dashboard está. |
| Ativar o encaminhamento de fluxo de eventos | (Servidor para servidor) Quando ativado, todos os eventos serão encaminhados em tempo real. Caso contrário, todos os eventos serão encaminhados em massa. Ao optar por ativar o encaminhamento do fluxo de dados de eventos, certifique-se de que os dados que você está enviando para o Braze respeitarão [os limites de frequência]({{site.baseurl}}/api/api_limits/). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![]({% image_buster /assets/img_archive/configure_settings.png %})

### Integração de kits incorporados

O SDK da mParticle e da Braze estará presente em seu aplicativo por meio da integração do kit incorporado. No entanto, ao contrário de uma integração direta da Braze, a mParticle se encarrega de chamar a maioria dos métodos do SDK da Braze para você. Os métodos do mParticle usados para rastrear dados de usuários serão automaticamente mapeados para os métodos do SDK do Braze. 

Esses mapeamentos do SDK da mParticle para [Android](https://github.com/mparticle-integrations/mparticle-android-integration-appboy), [iOS](https://github.com/mparticle-integrations/mparticle-apple-integration-appboy) e [Web](https://github.com/Appboy/integration-appboy) são de código aberto e podem ser encontrados na [página da mParticle no GitHub](https://github.com/mparticle-integrations). 

A integração do SDK do kit incorporado permite que você aproveite nosso conjunto completo de recursos (push, mensagens no app e todo o rastreamento de análise de dados de mensagens relevantes).

{% alert note %}
Para cartões de conteúdo e integrações personalizadas de mensagens no app, chame os métodos do SDK da Braze diretamente.
{% endalert %}

#### Etapa 1: Integrar os SDKs do mParticle

Integre os SDKs da mParticle apropriados em seu app com base nas necessidades de sua plataforma:

* [mParticle para Android](https://docs.mparticle.com/developers/sdk/android/getting-started/)
* [mParticle para iOS](https://docs.mparticle.com/developers/sdk/ios/getting-started/)
* [mParticle para Web](https://docs.mparticle.com/developers/sdk/web/getting-started/)

#### Etapa 2: Integração completa do kit de eventos Braze da mParticle

Embora o SDK da Braze não precise ser incluído diretamente em seu site ou aplicativo para essa integração da mParticle, o seguinte mParticle Appboy Kit deve ser instalado para encaminhar dados do seu aplicativo para a Braze.

O [Guia de integração do kit de eventos da Braze](https://docs.mparticle.com/integrations/braze/event/#kit-integration) elaborado pela mParticle oferece as instruções de alinhamento personalizado da mParticle e da Braze com base em suas necessidades de envio de mensagens (push, monitoramento de localização etc.).

#### Etapa 3: Configurações de conexões para sua saída do Braze

Na mParticle, navegue até **Connections > Connect > [Sua plataforma desejada] > Connect Output** (Conexões > Conectar > Nome da plataforma desejada > Conectar saída) para adicionar a Braze como saída. **Salvar** quando concluído.

![]({% image_buster /assets/img_archive/mParticle_event_config.png %})

Nem todas as configurações de conexão se aplicam a todas as plataformas e tipos de integração. Para obter um detalhamento das configurações de conexão e das plataformas às quais elas se aplicam, consulte [a documentação do mParticle](https://docs.mparticle.com/integrations/braze/event/#connection-settings).

### Integração da API do servidor

Esse é um complemento para rotear seus dados de backend para o Braze se estiver usando os SDKs do lado do servidor da mParticle (por exemplo, Ruby, Python, etc.). Para configurar essa integração de servidor para servidor com o Braze, siga [a documentação do mParticle](https://docs.mparticle.com/guides/platform-guide/connections/).

{% alert important %}
A integração servidor a servidor não oferece suporte aos recursos da interface do usuário do Braze, como envio de mensagens no app, cartões de conteúdo ou notificações por push. Também existem dados capturados automaticamente, como campos em nível de dispositivo, que não estão disponíveis por meio desse método. 

Considere uma integração lado a lado se quiser usar esses recursos.

Para que os dados do lado do servidor sejam encaminhados para a Braze, eles devem incluir um `external_id`; usuários anônimos não serão encaminhados.
{% endalert %}

#### Configurações de conexões para sua saída do Braze

Na mParticle, navegue até **Connections > Connect > [Sua plataforma desejada] > Connect Output** (Conexões > Conectar > Nome da plataforma desejada > Conectar saída) para adicionar a Braze como saída. **Salvar** quando concluído. 

![]({% image_buster /assets/img_archive/mParticle_connections.png %})

Nem todas as configurações de conexão se aplicam a todas as plataformas e tipos de integração. Para obter um detalhamento das configurações de conexão e das plataformas às quais elas se aplicam, consulte [a documentação do mParticle](https://docs.mparticle.com/integrations/braze/event/#connection-settings).

Antes de ativar "Enriched User Attributes" (Atributos enriquecidos de usuário) ou "Enriched User Identities" (Identidades enriquecidas de usuário), recomendamos revisar os [excedentes de pontos de dados](#potential-data-point-overages) para saber como essas configurações afetam o uso de pontos de dados.

### Detalhes do mapeamento de dados

#### Tipos de dados
Nem todos os tipos de dados são compatíveis entre as duas plataformas.
- As [propriedades de eventos personalizados]({{site.baseurl}}/user_guide/data/custom_data/custom_events/) são compatíveis com objetos dos tipos string, numérico, booleano ou data. Não oferece suporte a vetores de objetos ou objetos aninhados.
- Os [atributos personalizados]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/) suportam objetos dos tipos string, numérico, booleano, data e vetor, mas não suportam objetos ou objetos aninhados. 

{% alert note %}
O Braze não oferece suporte a registros de data e hora anteriores ao ano 0 ou posteriores ao ano 3000 nos atributos personalizados do tipo `Time`. A Braze fará a ingestão desses valores quando forem enviados pela mParticle, mas eles serão armazenados como string.
{% endalert %}

#### Mapeamento de dados

| Tipo de dados mParticle | Tipo de dados do Braze | Descrição |
| ------------------- | --------------- | ----------- |
| Atribuições do usuário (reservadas) | Atribuição padrão | Por exemplo, a chave de atributo de usuário reservada `$FirstName` da mParticle é mapeada para o campo de atributo padrão `first_name` da Braze. |
| Atribuições do usuário (outras) | Atributo personalizado | Quaisquer atributos de usuário passados para o mParticle que estejam fora de suas chaves de atributo de usuário reservadas são registrados no Braze como um atributo personalizado.<br><br>Os atributos de usuário suportam valores dos tipos string, numérico, booleano, data e vetor, mas não suportam objetos ou objetos aninhados. |
| Evento personalizado | Evento personalizado | Os eventos personalizados do mParticle são reconhecidos pelo Braze como um evento personalizado. Os atributos de eventos são encaminhados como propriedades de eventos personalizados.<br><br>Os atributos de eventos passados à Braze como propriedades de eventos suportam objetos dos tipos string, numéricos, booleanos ou data, mas não suportam vetores nem objetos aninhados. |
| Evento de compra comercial | Evento de compra | Os eventos de compra comercial são mapeados para eventos de compra da Braze. <br><br>Alterne o valor do agrupamento de dados de eventos comerciais para registrar as compras no nível do pedido ou do produto. Por exemplo, se `false`, um único evento de entrada com dois produtos, promoções ou impressões exclusivos resultaria em pelo menos dois eventos Braze de saída. Se definido como `true`, isso resultaria em um único evento de saída com uma matriz aninhada de produtos, promoções ou impressões, respectivamente.<br><br>Para saber mais sobre os campos de comércio adicionais que serão registrados, consulte a [documentação da mParticle](https://docs.mparticle.com/integrations/braze/event/#purchase-events). <br><br>Ao definir "bundle commerce event data" (agrupar dados de eventos comerciais) como `false`, os atributos do produto passados para a Braze como propriedades do evento de compra suportam objetos do tipo string, numérico, booleano ou data, mas não suportam vetores de objetos nem objetos aninhados.|
| Todos os outros eventos comerciais | Evento personalizado | Todos os outros eventos comerciais serão mapeados para eventos personalizados. <br><br>Alterne o valor do agrupamento de dados de eventos comerciais para registrar as compras no nível do pedido ou do produto. Por exemplo, se `false`, um único evento de entrada com dois produtos, promoções ou impressões exclusivos resultaria em pelo menos dois eventos Braze de saída. Se definido como `true`, isso resultaria em um único evento de saída com uma matriz aninhada de produtos, promoções ou impressões, respectivamente.<br><br>Além de certos valores comerciais padrão, as atribuições do produto serão registradas como propriedades do evento Braze. Para saber mais sobre os campos de comércio adicionais que serão registrados, consulte a [documentação da mParticle](https://docs.mparticle.com/integrations/braze/event/#other-commerce-events).<br><br>Ao definir "bundle commerce event data" (agrupar dados de eventos comerciais) como `false`, os atributos do produto passados para a Braze como propriedades do evento suportam objetos do tipo string, numérico, booleano ou data, mas não suportam vetores de objetos nem objetos aninhados. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

#### Mapeamento da identidade do usuário
Para cada saída do mParticle, você pode selecionar o tipo de identidade externa a ser enviada ao Braze como `external_id`. Embora o valor padrão seja o ID do cliente, você pode optar por mapear outro ID, como `MPID`, para enviar à Braze como `external_id`. Esteja ciente de que a escolha de um identificador diferente do ID do cliente pode influenciar a forma como os dados são enviados no Braze. 

Por exemplo, o mapeamento do MPID para seu `external_id` da Braze terá os seguintes efeitos:
- Devido à natureza de quando o MPID é atribuído, todos os usuários receberão um `external_id` no início da sessão.
- A configuração dos Currents pode exigir mapeamento adicional devido aos diferentes tipos de dados entre MPID e `external_id`.

### Encaminhamento de solicitações de exclusão (solicitações do titular dos dados)

Encaminhe solicitações de exclusão à Braze configurando uma saída de solicitação do titular dos dados para a Braze. Para encaminhar solicitações de exclusão à Braze, acesse a[documentação da mParticle](https://docs.mparticle.com/integrations/braze/forwarding-dsr/).

## Potenciais excedentes de pontos de dados

### Atribuições enriquecidas do usuário

#### Como ativar atributos e identidades enriquecidos de usuários (somente de servidor para servidor) {#enriched}

Nas configurações de conexão do mParticle, a Braze recomenda desativar a opção **Include Enriched User Attributes (Incluir atribuições enriquecidas do usuário**). Se ativada, a mParticle encaminhará todos os atributos de usuário disponíveis (como atributos padrão, atributos personalizados e atributos calculados) do perfil existente para o Braze em cada evento registrado. Isso resultará em um alto consumo de pontos de dados, pois a mParticle enviará à Braze os mesmos atributos inalterados em cada chamada.

Por exemplo, se um usuário adicionar nome, sobrenome e número de telefone durante a primeira sessão e, posteriormente, inscrever-se para receber um boletim informativo adicionando as mesmas informações, além do e-mail, disparando um evento de envio de e-mail:
- Se ativado (padrão), serão incorridos cinco pontos de dados. (evento de inscrição, endereço de e-mail, nome, sobrenome e número de telefone)
- Se desativado, dois pontos de dados serão incorridos (evento de inscrição e endereço de e-mail)

{% alert note %}
A desativação dessa configuração não verificará se há dados alterados. No entanto, isso impedirá que a integração envie todos os atributos de usuário no perfil do usuário que não foram recebidos no lote de entrada original ou explicitamente definidos como uma atribuição para o evento. É importante ainda verificar se apenas os deltas são passados para a Braze.
{% endalert %}

#### Considerações sobre a desativação de atribuições enriquecidas do usuário

Há algumas considerações que devem ser levadas em conta ao desativar **a opção Include Enriched User Attributes**:
1. A integração de servidor para servidor usa a API de eventos do mParticle para enviar eventos para o Braze. Cada solicitação é disparada por um evento. Quando uma atribuição do usuário é alterada, como a atualização de um endereço de e-mail, mas não está associada a um evento específico (por exemplo, um evento personalizado de atualização de perfil), o novo valor só é passado para uma saída como o Braze como um "atributo enriquecido" na carga útil do próximo evento disparado pelo usuário. Quando **Include Enriched User Attributes** estiver desativado, esse novo valor de atribuição não associado a um evento específico não será passado para o Braze.
  - Para resolver isso, recomendamos a criação de um evento separado de "atribuição de usuário atualizada" que envie apenas os atributos específicos do usuário que foram atualizados para o Braze. Note que, com essa abordagem, você ainda estará registrando um ponto de dados adicional para o evento "user attribute updated", mas o consumo de pontos de dados será muito menor do que o envio de todos os atributos de usuários em todas as chamadas com o recurso ativado.
2. Os atributos calculados são passados para o Braze como um atributo de usuário enriquecido, portanto, quando "Atributos de usuário enriquecidos" estiver desativado, eles não serão mais passados para o Braze. Para encaminhar atributos calculados para o Braze quando os "Atributos de usuário enriquecidos" estiverem desativados, um [feed de atributos calculados](https://docs.mparticle.com/guides/platform-guide/calculated-attributes/using-calculated-attributes/#forward-calculated-attributes-in-the-calculated-attributes-feed) poderia ajudar sem empurrar todos os atributos. O feed disparará uma atualização downstream para o Braze quando uma atribuição calculada for alterada. 

### Envio de dados desnecessários ou duplicados para o Braze
A Braze conta um ponto de dados toda vez que um atributo é passado para a Braze, mesmo que o valor não seja alterado. Por esse motivo, a Braze recomenda encaminhar apenas os dados necessários para a ação dentro da Braze e garantir que apenas deltas de atribuições estejam sendo passados.


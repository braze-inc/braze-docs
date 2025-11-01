---
nav_title: Pontuação de leads
article_title: Criação de um fluxo de trabalho de pontuação de leads
page_order: 1
page_type: reference
description: "Saiba como usar o Braze para fazer a pontuação simples de leads, a pontuação externa de leads e as transferências de leads."
---

# Criação de um fluxo de trabalho de pontuação de leads

> Este caso de uso demonstra como você pode usar o Braze para atualizar as pontuações de leads dos usuários em tempo real e entregar automaticamente os leads às suas equipes de vendas.

Há duas etapas principais para criar um fluxo de trabalho de pontuação de leads no Braze:

1. Crie um Canvas de pontuação de leads no Braze ou integre uma ferramenta externa de pontuação de leads:
- [Pontuação simples de leads](#simple-lead-scoring)
- [Pontuação externa de leads](#external-lead-scoring)

2. Crie uma campanha de webhook para enviar leads qualificados para sua equipe de vendas:
- [Transferência de liderança: Lead qualificado de marketing (MQL) para vendas](#lead-handoff)

## Pontuação simples de leads

### Etapa 1: Criar uma tela

1. Vá para **Messaging** > **Canvas** e selecione **Create Canvas** e, em seguida, preencha os dados básicos do Canvas.

2. Dê ao seu Canvas um nome relevante, como "Lead Scoring Canvas" e, para facilitar a localização, coloque uma tag como "Gerenciamento de leads".<br><br>\![Etapa 1 da criação de um Canvas com o nome "Lead Scoring Canvas" e a tag "Lead Management".]({% image_buster /assets/img/b2b/step_1_simple.png %}){: style="max-width:80%;"}

### Etapa 2: Configure seus critérios de entrada

1. Prossiga para a etapa **Entry Schedule (Programação de entrada** ) e selecione uma programação de entrada **baseada em ação**. Isso inserirá os usuários no Canvas quando eles realizarem ações específicas.

2. Em **Action-Based Options (Opções baseadas em ações**), adicione essas duas ações:
    - **Altere o valor do atributo personalizado** com o nome do atributo de pontuação de leads (como `lead score`). Se você ainda não criou um atributo de pontuação de leads, siga as etapas em [Atributos personalizados]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/). Isso inserirá os usuários no Canvas sempre que a pontuação do lead for alterada.
    - **Adicionar um endereço de e-mail**

Etapa 2 da criação de um Canvas com o cronograma de entrada "Baseado em ação" e opções baseadas em ação para alterar um atributo personalizado "pontuação de leads" e adicionar um endereço de e-mail.]({% image_buster /assets/img/b2b/step_2_simple.png %}){: style="max-width:80%;"}

### Etapa 3: Identifique seu público-alvo

#### Etapa 3a: Selecionar segmentos

Todos os usuários são qualificados para a pontuação de leads, portanto, você pode adicionar regras específicas da empresa sobre quem pontuar, selecionando os [segmentos]({{site.baseurl}}/user_guide/engagement_tools/segments/) de usuários a serem segmentados e aplicando [filtros]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/) adicionais. Por exemplo, você pode excluir funcionários, usuários que já são clientes e similares. 

Etapa 3 da criação de um Canvas com opções para selecionar segmentos e filtros para restringir o público-alvo de entrada.]({% image_buster /assets/img/b2b/step_3_simple.png %}){: style="max-width:80%;"}

#### Etapa 3b: Definir a reelegibilidade do Canvas

Um usuário passará por esse Canvas muitas vezes ao longo do ciclo de vida dele com você, portanto, certifique-se de que ele possa entrar novamente tão rapidamente quanto saiu da vez anterior. Isso pode ser feito por meio de configurações de reelegibilidade. 

Em **Controles de entrada**, faça o seguinte:
- Selecione **Permitir que os usuários entrem novamente neste Canvas**.
- Selecione **Specified Window (Janela especificada**).
- Defina a reelegibilidade como "0" **segundos**.

Seção "Controles de entrada" que tem seleções para "Permitir que os usuários entrem novamente neste Canvas" em uma "Janela especificada" de 0 segundos.]({% image_buster /assets/img/b2b/entry_controls_simple.png %}){: style="max-width:80%;"}

#### Etapa 3c: Atualizar configurações de envio

Dada a natureza operacional desse Canvas e o fato de que nenhuma mensagem será enviada a esses usuários, não é necessário aderir aos status de assinatura.

Em **Subscription Settings (Configurações de assinatura**), para **Send to these users (Enviar para esses usuários):** selecione **todos os usuários, inclusive os que não se inscreveram**. 

\![Etapa 4 da criação de um Canvas para definir as opções de envio de mensagens.]({% image_buster /assets/img/b2b/step_4_simple.png %}){: style="max-width:80%;"}

### Etapa 4: Crie seu Canvas

#### Etapa 4a: Adicionar um caminho de ação

Em sua variante, selecione o ícone de adição e, em seguida, selecione **Caminhos de ação**.

Canvas com "Action Paths" exibido no menu aberto pelo ícone de adição.]({% image_buster /assets/img/b2b/action_paths_simple.png %}){: style="max-width:60%;"}

#### Etapa 4b: Criar grupos de ação

Cada Action Group representará todas as ações que levam ao mesmo incremento ou decremento de pontos. Você pode definir até oito Action Groups. Nesse cenário, estaremos configurando quatro grupos.

Adicione os seguintes grupos ao seu Action Path:

- **Grupo 1:** Todos os eventos que contam para um incremento de 1 ponto.
- **Grupo 2:** Todos os eventos que contam para um incremento de 5 pontos.
- **Grupo 3:** Todos os eventos que contam para um decréscimo de 1 ponto.
- **Todos os demais:** Os caminhos de ação permitem que você defina a janela para esperar e ver se um usuário realiza uma ação, antes de colocá-lo em um grupo "todos os outros". Para a pontuação de leads, essa é uma oportunidade de diminuir a pontuação por "inatividade".

Caminho de ação contendo grupos de ação para adicionar um ponto, cinco pontos e dez pontos; subtrair um ponto e dez pontos; e "Todos os outros".]({% image_buster /assets/img/b2b/action_paths_selected_simple.png %}){: style="max-width:20%;"}

#### Etapa 4c: Configure cada grupo para incluir os eventos relevantes

Em cada Grupo de Ações, selecione **Selecionar acionador** e escolha o evento que adicionará o número de pontos para esse Grupo de Ações específico. Adicione mais acionadores para incluir todos os eventos que aumentarão a pontuação do lead em um. Por exemplo, um usuário pode aumentar sua pontuação em um quando iniciar uma sessão em qualquer aplicativo ou realizar um evento personalizado (como registrar-se ou participar de um webinar). 

Action Group para adicionar um ponto com os acionadores "Starting Session in Any App" (Iniciar sessão em qualquer aplicativo) e "Performing Custom Event" (Executar evento personalizado).]({% image_buster /assets/img/b2b/action_groups_simple.png %}){: style="max-width:80%;"}

#### Etapa 4d: Adicionar usuário Etapas de atualização

Adicione uma etapa de atualização do usuário a cada caminho do Canvas criado abaixo do seu caminho de ação. 

Tela exibindo o caminho da ação com caminhos ramificados de atualização do usuário para cada grupo de ações.]({% image_buster /assets/img/b2b/user_update_paths_simple.png %}){: style="max-width:80%;"}

{: start=”2”}
Na guia **Compose (Compor** ) de cada etapa do User Update, faça o seguinte para os respectivos campos:

| Campo | Ação |
| --- | --- |
| **Nome do atributo** | Selecione o atributo de pontuação do lead que você selecionou na etapa 2 (`lead score`).|
| **Ação** | Altere a ação para **Incrementar por** se o caminho aumentar a pontuação ou **Diminuir por** se o caminho diminuir a pontuação |
| **Incremento por** ou **Decremento por** | Insira o número de pontos que serão aumentados ou diminuídos da pontuação principal.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Etapa 5: Inicie seu Canvas

É isso aí! Seu Canvas de pontuação de leads está pronto para ser lançado.

## Pontuação externa de leads

Seja usando um de nossos [parceiros de tecnologia]({{site.baseurl}}/partners/home/), seu próprio modelo interno de pontuação de leads, aprendizado de máquina ou outra ferramenta de pontuação de leads, temos várias opções para você.

### Parceiros externos

Confira [Parceiros de tecnologia]({{site.baseurl}}/partners/home) para saber mais sobre nossos parceiros B2B que oferecem recursos de pontuação de leads. Não está vendo sua ferramenta lá? Você pode fazer a integração chamando nosso [`users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track#track-users) endpoint da API. 

### Modelos internos de dados de pontuação de leads

Você pode integrar o Braze aos seus modelos de dados internos, incluindo modelos de pontuação de leads, de várias maneiras. Veja abaixo alguns exemplos comuns de como nossos clientes se integraram ao Braze.

#### Armazém de dados na nuvem integrado

{% tabs %}
{% tab Braze as a data source %}

Como sua ferramenta de marketing, o Braze contém dados extremamente relevantes que podem complementar o modelo interno de pontuação de leads da sua equipe. 

Por exemplo, os dados de envolvimento de mensagens (como aberturas e cliques de e-mail, envolvimento da página de destino e outros) podem determinar o nível de envolvimento de um lead. Você pode passar esses dados de volta para seu data warehouse na nuvem e disponibilizá-los como entrada para seus modelos de pontuação de leads usando as soluções de exportação de dados de streaming da Braze:

- [Correntes de brasagem]({{site.baseurl}}/user_guide/data/braze_currents/)
- [Compartilhamento seguro de dados da Snowflake]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/)

{% endtab %}
{% tab Braze as a destination %}

Depois que suas equipes internas criarem e executarem seu modelo de pontuação de leads, você poderá puxar esses dados de volta para o Braze para poder segmentar e direcionar melhor os leads para mensagens relevantes. Você pode fazer isso com o [Braze Cloud Data Ingestion]({{site.baseurl}}/user_guide/data/cloud_ingestion/overview/). 

Com a ingestão de dados na nuvem, suas equipes internas criarão uma nova tabela ou exibição com os identificadores de usuário, as pontuações de leads mais recentes e os carimbos de data e hora em que as pontuações foram atualizadas. O Braze pegará a tabela ou visualização e adicionará as pontuações de leads aos perfis de usuário.

{% endtab %}
{% endtabs %}

## Transferência de liderança: Lead qualificado de marketing (MQL) para vendas {#lead-handoff}

Nossa abordagem recomendada para as transferências de leads é ter um lead ou contato correspondente anexado a cada usuário no Braze. Esses leads entrariam na fila de suas equipes de vendas quando seus status de lead mudassem para um estágio de MQL, momento em que o Salesforce daria início a um fluxo de trabalho de roteamento ou atribuição de leads. 

Para atualizar o registro do lead no Salesforce com o status do lead do Braze, recomendamos o uso de um modelo de webhook acionado.

### Etapa 1: Criar uma campanha de webhook

### Etapa 2: Configure seu webhook

#### Etapa 2a: Compor webhook

1. Dê um nome à sua campanha de webhook, como "Salesforce > Update lead to MQL".

2. Digite o URL do webhook no formato {% raw %}`https://YOUR_SALESFORCE_INSTANCE.my.salesforce.com/services/data/v60.0/sobjects/Lead/{{${user_id}}}`{% endraw %}. O ID de usuário do Braze de {% raw %}`{{$user_id}}}`{% endraw %} deve corresponder ao seu ID de contato do Salesforce. Caso contrário, use um alias em vez de {% raw %}`{{$user_id}}}`{% endraw %}.

3. Atualize o **método HTTP** para **PATCH**.

4. Configure seu payload para atualizar o registro do lead no Salesforce somente se a pontuação do lead ultrapassar o limite predefinido. Veja o exemplo de corpo de solicitação abaixo para uma pontuação de lead superior a 100.

{% raw %}
```liquid
{% assign threshold = 100%}
{% if custom_attribute.${lead score} > threshold %}
{
"lead_status": "MQL"
}
{% else %}{% abort_message('not at threshold')%}
{% endif %}
```
{% endraw %}

{: start="5"}
5\. Inclua os seguintes cabeçalhos:

| Cabeçalho | Conteúdo |
| --- | --- |
| Autorização | {% raw %}`Bearer {{result.access_token}}`{% endraw %}<br><br>Para recuperar um token, [configure um aplicativo conectado](https://help.salesforce.com/s/articleView?id=sf.connected_app_client_credentials_setup.htm&type=5) para o fluxo de credenciais do cliente OAuth 2.0 e, em seguida, use o Connected Content para recuperar o portador do Salesforce: <br><br>{% raw %}<code>{% connected_content https://[instance].my.salesforce.com/services/oauth2/token <br>:method post <br> :body client_id=[client_id]&client_secret=[client_secret]&grant_type=client_credentials <br>:save result %}{% endraw %} <br> Portador {% raw %}{{result.access_token}}</code>{% endraw %} |
| Content_Type | aplicativo/json |
{: .reset-td-br-1 reset-td-br-2}

Webhook sendo composto com um URL de webhook do Salesforce, método HTTP PATCH, corpo de solicitação de texto bruto e cabeçalhos de solicitação.]({% image_buster /assets/img/b2b/webhook.png %}){: style="max-width:80%;"}

#### Etapa 2b: Agendar envios de webhooks

A campanha deve ser acionada sempre que a pontuação de leads do usuário for alterada. Essa campanha será acionada para qualquer usuário cuja pontuação seja alterada, mas só afetará os usuários que não sejam atualmente um MQL e que tenham ultrapassado o limite definido na etapa anterior.

Na etapa **Schedule Delivery**, selecione o seguinte:
- Um tipo de entrega **baseado em ação** 
- Uma ação de gatilho de **Alterar valor de atributo personalizado** com o nome do seu atributo de pontuação de leads e uma ação de **qualquer novo valor**

#### Etapa 2c: Identificar o público-alvo

Na etapa **Target Audiences (Públicos-alvo** ), inclua um filtro que exclua os usuários cujos status de lead já estejam em MQL ou superior, como "`lead_status` `is none of` `MQL`".

\![As opções de direcionamento do webhook com o filtro de “lead_status” não são "MQL".]({% image_buster /assets/img/b2b/step_3_webhook.png %}){: style="max-width:80%;"}

### Etapa 3: Campanha de lançamento

Selecione **Launch (Iniciar** ) e observe o status do seu lead mudar no Salesforce à medida que seus clientes ultrapassam o limite de pontuação de lead MQL.


---
nav_title: Configurar orquestração
article_title: Configurar orquestração
page_order: 2
description: "Aprenda como conectar o BrazeAI Decisioning Studio Acessar sua plataforma de engajamento com clientes para ativar comunicações personalizadas."
toc_headers: h2
---

# Configurar orquestração

> O BrazeAI Decisioning Studio™ Go precisa se conectar à sua plataforma de engajamento com clientes (CEP) para orquestrar comunicações personalizadas. Este artigo explica como configurar a integração para cada CEP suportado.

## CEPs suportados

O Decisioning Studio Go suporta as seguintes plataformas de engajamento com clientes:

| CEP | Tipo de integração | Principais recursos |
|-----|-----------------|--------------|
| **Braze** | Campanhas disparadas por API | Integração nativa, disparo em tempo real |
| **Salesforce Marketing Cloud** | Journey Builder com eventos de API | Automação de consulta SQL, extensões de dados |
| **Klaviyo** | Fluxos com disparadores de métricas | Baseado em modelo, divisões de disparo |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

Selecione sua CEP abaixo para começar a configuração da integração.

{% tabs %}
{% tab Braze %}

## Configurando a integração do Braze

Para integrar o Decisioning Studio Go com o Braze, você criará uma chave de API, configurará uma campanha acionada por API e fornecerá os identificadores necessários para o portal do Decisioning Studio Go.

### Etapa 1: Criar uma chave de API REST

1. No dashboard do Braze, Acessar **Configurações** > **APIs e Identificadores** > **Chaves de API**.
2. Selecione **Create API Key (Criar chave de API**).
3. Digite um nome para sua chave de API. Um exemplo é "DecisioningStudioGoEmail".
4. Selecione as permissões com base nas seguintes categorias:
    - **Dados de Usuários:** selecione `users.track`, `users.delete`, `users.export.ids`, `users.export.segment`
    - **Mensagens:** selecione `messages.send`
    - **Campanhas:** selecione todas as permissões listadas
    - **Canva:** selecione todas as permissões listadas
    - **Segmentos:** selecione todas as permissões listadas
    - **Modelos:** selecione todas as permissões listadas

{: start="5"}
5\. Selecione **Criar chave de API**.
6\. Copie a chave de API e cole-a no seu portal BrazeAI Decisioning Studio™ Go.

### Etapa 2: Localize seu nome de exibição de e-mail

1. No painel do Braze, acesse **Configurações** > **Preferências de E-mail**.
2. Localize o nome de exibição a ser usado com o BrazeAI Decisioning Studio™ Go.
3. Copie e cole o **Nome de Exibição do Remetente** no portal BrazeAI Decisioning Studio™ Go como **Nome de Exibição do E-mail**.
4. Copie e cole o endereço de e-mail associado no seu portal BrazeAI Decisioning Studio™ Go como **Endereço de e-mail do remetente**, que combina a parte local e o domínio.

### Etapa 3: Encontre sua URL do Braze e ID do App

**Para encontrar sua URL do Braze:**
1. Acesse o painel do Braze.
2. Na janela do seu navegador, sua URL do Braze começa com `https://` e termina com `braze.com`. Um exemplo de URL do Braze é `https://dashboard-01.braze.com`.

**Para encontrar seu ID do App (Chave de API):**

{% alert note %}
O Braze oferece IDs de app (referidos como chaves de API no painel do Braze) que você pode usar para fins de rastreamento, como associar atividades a um app específico no seu espaço de trabalho. Se você usar IDs de aplicativo, o BrazeAI Decisioning Studio™ Go suporta a associação de um ID de aplicativo com cada experimentador.<br><br>Se você não usar IDs de aplicativo, pode inserir qualquer string de caracteres como um espaço reservado.
{% endalert %}

1. No painel do Braze, acesse **Configurações** > **Configurações do App**.
2. Acesse o aplicativo que você deseja rastrear.
3. Copie e cole a **chave de API** no seu portal do BrazeAI Decisioning Studio™ Go.

### Etapa 4: Crie uma campanha acionada por API

1. No painel do Braze, acesse **Envio de Mensagens** > **Campanhas**.
2. Selecione **Criar campanha**.
3. Para o tipo da sua campanha, selecione **campanha de API**.
4. Dê um nome à campanha. Um exemplo é "Decisioning Studio Go Email".

![Uma campanha de API chamada "Decisioning Studio Go Email".]({% image_buster /assets/img/decisioning_studio_go/api_campaign_name.png %})

{: start="5"}
5\. Para seu canal de envio de mensagens, selecione **e-mail**.

![Opção para selecionar seu canal de envio de mensagens para a campanha de API.]({% image_buster /assets/img/decisioning_studio_go/select_api_campaign.png %})

{: start="6"}
6\. Em **Opções Adicionais**, selecione a caixa de seleção **Permitir que os usuários se tornem re-elegíveis para receber a campanha**.
7\. Para o tempo para se tornar re-elegível, insira **1** e selecione **Horas** no menu suspenso.

![Re-elegibilidade para a campanha de API selecionada.]({% image_buster /assets/img/decisioning_studio_go/additional_options.png %})

{: start="8"}
8\. Selecione **Salvar Campanha**.

### Etapa 5: Copie seus IDs de campanha e mensagem

1. Na sua campanha de API, copie o **ID da Campanha**. Em seguida, acesse o portal do BrazeAI Decisioning Studio™ Go e cole o **ID da Campanha**.

![Um exemplo de ID de variação de mensagem para ser copiado e colado.]({% image_buster /assets/img/decisioning_studio_go/campaign_id.png %})

{: start="2"}
2\. Copie o **ID de Variação de Mensagem**. Em seguida, acesse o portal BrazeAI Decisioning Studio™ Go e cole o **ID de Variação de Mensagem**.

### Etapa 6: Localize um ID de usuário teste

Para testar sua integração, você precisará de um ID de usuário:

1. No dashboard do Braze, acesse **público** > **Buscar Usuários**.
2. Pesquise o usuário pelo ID de usuário externo, apelido, e-mail, número de telefone ou token por push.
3. Copie o ID do usuário para referência na sua configuração.

![Exemplo de perfil de usuário ao localizar um usuário pelo seu ID.]({% image_buster /assets/img/decisioning_studio_go/user_id.png %})

{% endtab %}
{% tab Salesforce Marketing Cloud %}

## Configurando a integração do SFMC

Para integrar o Decisioning Studio Go com o Salesforce Marketing Cloud, você configurará um pacote de app, criará uma automação de consulta de dados e construirá uma Jornada para gerenciar envios acionados.

### Parte 1: Configure um pacote de app do SFMC

1. Acesse a página inicial do Marketing Cloud.
2. Abra o menu no cabeçalho global e selecione **Configuração**.
3. Acesse **Apps** em **Ferramentas da Plataforma** na navegação do painel lateral, em seguida selecione **Pacotes Instalados**.
4. Selecione **Novo** para criar um pacote de app.
5. Dê um nome e uma descrição ao pacote de app.

![Um pacote de app com o nome "Experimentador 1 - Teste 5".]({% image_buster /assets/img/decisioning_studio_go/sfmc_app_package1.png %})

{: start="6"}
6\. Selecione **Adicionar Componente**.
7\. Para o **Tipo de Componente**, selecione **Integração de API**. Em seguida, selecione **Próximo**.
8\. Para o **Tipo de Integração**, selecione **Servidor para servidor**. Em seguida, selecione **Próximo**.
9\. Selecione os seguintes escopos recomendados apenas para o seu pacote de app:
    \- Canais > E-mail > Ler, Escrever, Enviar
    \- Canais > OTT > Ler
    \- Canais > Push > Ler
    \- Canais > SMS > Ler
    \- Canais > Social > Ler
    \- Canais > Web > Ler
    \- Ativos > Documentos e Imagens > Ler, Escrever
    \- Ativos > Conteúdo Salvo > Ler, Escrever
    \- Automação > Automizações > Ler, Escrever, Executar
    \- Automação > Jornadas > Ler, Escrever, Executar, Ativar/Parar/Pausar/Enviar/Agendar
    \- Contatos > Públicos > Ler
    \- Contatos > Lista e Assinantes > Ler, Escrever
    \- Plataforma Cross Cloud > Público de Mercado > Visualizar
    \- Plataforma Cross Cloud > Membro do Público de Mercado > Visualizar
    \- Plataforma Cross Cloud > Marketing Cloud Connect > Ler
    \- Dados > Extensões de Dados > Ler, Escrever
    \- Dados > Localizações de Arquivos > Ler
    \- Dados > Eventos de Rastreamento > Ler, Escrever
    \- Notificações de eventos > Callbacks > Ler
    \- Notificações de eventos > Assinaturas > Ler

{% details Show image of recommended scopes %}

![Os escopos recomendados para o pacote do app Salesforce Marketing Cloud.]({% image_buster /assets/img/decisioning_studio_go/app_package_scopes.png %})

{% enddetails %}

{: start="10"}
10\. Selecione **Salvar**.
11\. Copie e cole os seguintes campos no portal BrazeAI Decisioning Studio™ Go: **Id do Cliente**, **Segredo do Cliente**, **URI Base de Autenticação**, **URI Base REST**, **URI Base SOAP**.

### Parte 2: Configure uma automação de consulta de dados

#### Etapa 1: Crie uma nova automação

1. Na sua página inicial do Salesforce Marketing Cloud, acesse **Journey Builder** e selecione **Automation Studio**.

![Opção Automation Studio na navegação do Journey Builder.]({% image_buster /assets/img/decisioning_studio_go/query13.png %})

{: start="2"}
2\. Selecione **Nova Automação**.
3\. Arraste e solte um nó **Agendar** como a **Fonte Inicial**.

!["Agendar" como a fonte inicial de uma Jornada.]({% image_buster /assets/img/decisioning_studio_go/query14.png %})

{: start="4"}
4\. No nó **Agendar**, selecione **Configurar**.
5\. Defina o seguinte para o agendamento:
    - **Data de Início:** Dia do calendário de amanhã
    - **Hora:** **12:00 AM**
    - **Fuso Horário:** **(GMT-05:00) Leste (EUA & Canadá)**
6\. Para **Repetir**, selecione **Diariamente**.
7\. Defina este cronograma para nunca terminar.
8\. Selecione **Concluído** para salvar o cronograma.

![Um cronograma de exemplo definido para 25 de janeiro de 2024 às 12h ET, para repetir todos os dias.]({% image_buster /assets/img/decisioning_studio_go/query12.png %})

#### Etapa 2: Crie suas consultas de SQL

Em seguida, crie 2 consultas de SQL: uma consulta de assinantes e uma consulta de engajamento. Essas consultas permitem que o BrazeAI Decisioning Studio™ Acesse dados para preencher o público e ingerir eventos de engajamento.

**Consulta de Assinantes:**

1. Arraste e solte uma **Consulta SQL** no canva.
2. Selecione **Escolher**.
3. Selecione **Criar Nova Atividade de Consulta**.
4. Dê um nome e uma chave externa à consulta. Recomendamos usar o nome sugerido e a chave externa para a consulta de assinantes fornecidos em seu portal BrazeAI Decisioning Studio™ Acesse.

![Um exemplo "OFE_Subscribers_query_Test5" e a chave externa.]({% image_buster /assets/img/decisioning_studio_go/query11.png %})

{: start="5"}
5\. Selecione **Próximo**.
6\. Em seu portal BrazeAI Decisioning Studio™ Acesse, localize a consulta SQL de dados do Sistema em **Recursos de Consulta de Assinantes**.
7\. Copie e cole a consulta na caixa de texto e selecione **Próximo**.

![Um exemplo de consulta na seção de Consulta SQL.]({% image_buster /assets/img/decisioning_studio_go/query10.png %})

{: start="8"}
8\. No seu portal BrazeAI Decisioning Studio™ Go, na seção **Recursos a usar**, localize a chave externa da extensão de dados alvo. Em seguida, cole-a na barra de pesquisa para buscar.

![Uma chave externa colada na barra de pesquisa]({% image_buster /assets/img/decisioning_studio_go/query9.png %})

{: start="9"}
9\. Selecione a extensão de dados que corresponde à chave externa que você pesquisou. O nome da extensão de dados alvo também é fornecido no seu portal BrazeAI Decisioning Studio™ Go para referência cruzada. A **Extensão de Dados** para a consulta de assinantes deve terminar com um sufixo `BASE_AUDIENCE_DATA`.

![O nome da extensão de dados que corresponde à chave externa do exemplo.]({% image_buster /assets/img/decisioning_studio_go/query8.png %})

{: start="10"}
10\. Selecione **Substituir** e depois **Próximo**.

**Consulta de engajamento:**

1. Arraste e solte uma **Consulta SQL** no canva.

!["Consulta SQL" adicionada como uma atividade na Jornada.]({% image_buster /assets/img/decisioning_studio_go/query7.png %})

{: start="2"}
2\. Selecione **Escolher**.
3\. Selecione **Criar Nova Atividade de Consulta**.
4\. Dê um nome e uma chave externa à consulta. Recomendamos usar o nome sugerido e a chave externa para a consulta de engajamento fornecida no seu portal BrazeAI Decisioning Studio™ Go.

![Um exemplo "OFE_Engagement_query" e a chave externa.]({% image_buster /assets/img/decisioning_studio_go/query6.png %})

{: start="5"}
5\. Selecione **Próximo**.
6\. No seu portal BrazeAI Decisioning Studio™ Go, localize a consulta SQL de dados do sistema em **Recursos de Consulta de Engajamento**.
7\. Copie e cole a consulta na caixa de texto e selecione **Próximo**.

![Um exemplo de consulta na seção de Consulta SQL.]({% image_buster /assets/img/decisioning_studio_go/query5.png %})

{: start="8"}
8\. Localize e selecione a Extensão de Dados alvo para a Consulta de Engajamento especificada no seu portal BrazeAI Decisioning Studio™ Go.

{% alert tip %}
O nome da extensão de dados alvo também é fornecido no seu portal BrazeAI Decisioning Studio™ Go para referência cruzada. Certifique-se de que você está olhando para a Extensão de Dados alvo para a Consulta de Engajamento. A **Extensão de Dados** para a consulta de engajamento deve terminar com um sufixo ENGAGEMENT_DATA.
{% endalert %}

{: start="9"}
9\. Selecione **Substituir** e depois **Próximo**.

![O nome da extensão de dados que corresponde à chave externa do exemplo.]({% image_buster /assets/img/decisioning_studio_go/query4.png %})

#### Etapa 3: Execute a automação

1. Dê um nome à automação e selecione **Salvar**.

![Uma automação de exemplo "OFE_Experimenter_Test5_Automation".]({% image_buster /assets/img/decisioning_studio_go/query3.png %})

{: start="2"}
2\. Em seguida, selecione **Executar Uma Vez** para confirmar que tudo está funcionando como esperado.
3\. Selecione ambas as consultas e clique em **Executar**.

![Uma automação "OFE_Experimenter_Test5_Automation" com uma lista de atividades de consulta SQL selecionadas para executar.]({% image_buster /assets/img/decisioning_studio_go/query2.png %})

{: start="4"}
4\. Selecione **Executar Agora**.

![Uma atividade de Consulta SQL selecionada.]({% image_buster /assets/img/decisioning_studio_go/query1.png %})

Agora, você pode verificar se a automação está sendo executada com sucesso. Entre em contato com o Suporte da Braze para mais assistência se sua automação não estiver funcionando como esperado.

### Parte 3: Crie sua Jornada SFMC

#### Etapa 1: Configure a Jornada

1. No Salesforce Marketing Cloud, acesse **Construtor de Jornadas** > **Construtor de Jornadas**.
2. Selecione **Criar Nova Jornada**.
3. Para o tipo de jornada, selecione **Jornada de Múltiplas Etapas**, em seguida, selecione **Criar**.

![Uma fonte de entrada de Evento API conectada a um nó de Divisão de Decisão e múltiplos nós de E-mail.]({% image_buster /assets/img/decisioning_studio_go/journey1.png %})

#### Etapa 2: Construa a Jornada

**Criar uma fonte de entrada:**

1. Para sua fonte de entrada, arraste **Evento API** para o Construtor de Jornadas.

!["Evento API" selecionado como a fonte de entrada.]({% image_buster /assets/img/decisioning_studio_go/journey2.png %})

{: start="2"}
2\. No **Evento API**, selecione **Criar um evento**.

![A opção "criar um evento" no Evento API.]({% image_buster /assets/img/decisioning_studio_go/journey3.png %})

{: start="3"}
3\. Selecione **Selecionar Extensão de Dados**. Localize e selecione a extensão de dados que o BrazeAI Decisioning Studio™ Go usará para escrever recomendações.
4\. Selecione **Resumo** para salvar suas alterações.
5\. Selecione **Concluído** para salvar o evento da API.

![Resumo do evento da API.]({% image_buster /assets/img/decisioning_studio_go/journey4.png %}){: style="max-width:80%;"}

**Adicionar uma Divisão de Decisão:**

1. Arraste e solte uma **Divisão de Decisão** após o **Evento de Entrada da API**.
2. Nos detalhes da **Divisão de Decisão**, selecione **Editar** para o primeiro caminho.

![Detalhes da Divisão de Decisão com o botão "Editar".]({% image_buster /assets/img/decisioning_studio_go/journey5.png %})

{: start="3"}
3\. Atualize a **Divisão de Decisão** para usar o ID do modelo passado pela extensão de dados de recomendações. Localize o campo apropriado em **Dados da Jornada**.

![A seção de Dados da Jornada no Caminho 1 da Divisão de Decisão.]({% image_buster /assets/img/decisioning_studio_go/journey6.png %})

{: start="4"}
4\. Selecione seu evento de entrada e localize o campo de ID do modelo desejado, em seguida, arraste-o para o espaço de trabalho.

![O ID do modelo de e-mail a incluir.]({% image_buster /assets/img/decisioning_studio_go/journey7.png %})

{: start="5"}
5\. Insira o ID do modelo do seu primeiro modelo de e-mail, em seguida, selecione **Concluído**.
6\. Selecione **Resumo** para salvar este caminho.
7\. Adicione um caminho para cada um dos seus modelos de e-mail, em seguida, repita os passos 4-6 acima para definir os critérios de filtro para que o ID do modelo corresponda ao valor de ID de cada modelo.
8\. Selecione **Concluído** para salvar o nó da **Divisão de Decisão**.

![Dois caminhos em uma Divisão de Decisão para cada ID de modelo de e-mail.]({% image_buster /assets/img/decisioning_studio_go/journey10.png %}){: style="max-width:65%;"}

**Adicionar um E-mail para cada Divisão de Decisão:**

1. Arraste um **E-mail** para cada caminho da **Divisão de Decisão**.
2. Selecione **e-mail**, em seguida, selecione o modelo apropriado que deve ir em cada jornada (ou seja, o modelo com o valor de ID deve corresponder à lógica na sua divisão de decisão).

![Um nó de e-mail adicionado à jornada.]({% image_buster /assets/img/decisioning_studio_go/journey9.png %})

#### Etapa 3: Ative a jornada

Após configurar sua jornada, ative-a e compartilhe os seguintes detalhes com a equipe do BrazeAI Decisioning Studio™ Go:

* ID da jornada
* Nome da jornada
* chave de definição de evento da API
* chave externa da extensão de dados de recomendações

{% alert note %}
O portal do BrazeAI Decisioning Studio™ Go mostra a automação do SFMC que foi provisionada para exportar os assinantes e os dados de engajamento uma vez por dia. Se você abrir essa automação no SFMC, certifique-se de despausar e voltar a ativá-la.
{% endalert %}

1. No portal do BrazeAI Decisioning Studio™ Go, copie o **Nome da jornada**.
2. Em seguida, no Salesforce Marketing Cloud Journey Builder, cole o nome da jornada na barra de pesquisa.
3. Selecione o nome da jornada. Observe que a jornada está atualmente em status de rascunho.
4. Selecione **Validar**.

![A jornada concluída para ativar.]({% image_buster /assets/img/decisioning_studio_go/activate3.png %})

{: start="5"}
5\. Em seguida, revise os resultados da validação e selecione **Ativar**.

![Recomendações listadas na seção de Regras de Validação.]({% image_buster /assets/img/decisioning_studio_go/activate1.png %}){: style="max-width:60%;"}

{: start="6"}
6\. No resumo de **Ativar Jornada**, selecione **Ativar** novamente.

![Resumo para a jornada.]({% image_buster /assets/img/decisioning_studio_go/activate2.png %}){: style="max-width:85%;"}

Você está pronto! Agora você pode começar a acionar envios através do BrazeAI Decisioning Studio™ Go.

{% endtab %}
{% tab Klaviyo %}

## Configurando a integração com o Klaviyo

Para integrar o Decisioning Studio Go com o Klaviyo, você configurará uma chave de API, criará um fluxo de modelo de espaço reservado e construirá um fluxo para lidar com envios acionados.

### Parte 1: Configure as chaves de API do Klaviyo

1. No Klaviyo, acesse **Configurações** > **Chaves de API**.
2. Selecione **Criar Chave de API Privada**.
3. Digite um nome para a chave de API. Um exemplo é "Experimentadores do Decisioning Studio".
4. Selecione as seguintes permissões para a chave de API:
    - Campanhas: Acesso de Leitura
    - Privacidade de Dados: Acesso completo
    - Eventos: Acesso completo
    - Fluxos: Acesso completo
    - Imagens: Acesso de Leitura
    - Lista: Acesso completo
    - Métricas: Acesso completo
    - Perfis: Acesso completo
    - Segmentos: Acesso de Leitura
    - Modelos: Acesso completo
    - Webhooks: Acesso de Leitura

![Uma chave de API do Klaviyo com permissões selecionadas.]({% image_buster /assets/img/decisioning_studio_go/klaviyo_api_key.png %})

{: start="5"}
5\. Selecione **Criar**.
6\. Copie esta chave de API e cole-a no portal do BrazeAI Decisioning Studio™ Go onde solicitado.

### Parte 2: Crie um modelo de espaço reservado no Klaviyo

O BrazeAI Decisioning Studio™ Go importa modelos que estão associados a fluxos existentes na sua conta do Klaviyo. Para usar um modelo que não está associado a nenhum fluxo, você pode criar um fluxo de espaço reservado contendo os modelos que gostaria de usar. O fluxo pode ser deixado como um rascunho; não precisa estar ativo.

{% alert note %}
O objetivo deste fluxo de espaço reservado é importar o conteúdo desejado para o BrazeAI Decisioning Studio™ Go. Você deve criar um fluxo separado em um passo posterior, que o BrazeAI Decisioning Studio™ Go usará para disparar ativações uma vez que seu experimentador esteja ativo.
{% endalert %}

**Etapa 1: Configure seu fluxo**

1. No Klaviyo, selecione **Fluxos**.
2. Selecione **Criar fluxo** > **Criar do zero**.
3. Dê ao fluxo de espaço reservado um nome que você reconhecerá, então selecione **Criar fluxo**.

![Um fluxo chamado "Fluxo de espaço reservado OFE".]({% image_buster /assets/img/decisioning_studio_go/create_flow.png %})

{: start="4"}
4\. Selecione qualquer disparador, então salve o fluxo.
5\. Selecione **Confirmar e salvar**.

**Etapa 2: Crie o modelo de espaço reservado**

1. Arraste e solte um **e-mail** após o **Disparador**.

![Um fluxo com um nó de disparador seguido por um nó de e-mail.]({% image_buster /assets/img/decisioning_studio_go/set_up_email_node.png %})

{: start="2"}
2\. No nó **e-mail**, selecione **Selecionar modelo**.
3\. Então, escolha o modelo a ser usado e selecione **Usar modelo**.
4\. Selecione **Salvar** > **Concluído**.
5\. (Opcional) Para adicionar mais modelos a serem usados no BrazeAI Decisioning Studio™ Go, adicione outro **e-mail** e repita os passos 2–4.
6\. Deixe todos os e-mails em modo **Rascunho** e saia do Fluxo.

No portal BrazeAI Decisioning Studio™ Go, seus modelos devem ser selecionáveis sob seu fluxo de espaço reservado.

![Um exemplo de um modelo Klaviyo de espaço reservado no portal Decisioning Studio Go.]({% image_buster /assets/img/decisioning_studio_go/placeholder_flow.png %})

### Parte 3: Crie um fluxo no Klaviyo

{% alert important %}
Você deve criar um novo fluxo no Klaviyo para cada novo experimentador que configurar. Se você criou anteriormente um fluxo de espaço reservado para importar seus modelos, deve criar um novo fluxo e não pode reutilizar o fluxo de espaço reservado anterior.
{% endalert %}

Antes de criar um fluxo no Klaviyo, você deve ter os seguintes detalhes do seu portal BrazeAI Decisioning Studio™ Go para referência:

- Nome do fluxo
- Nome do evento de gatilho

#### Etapa 1: Configure o fluxo

1. No Klaviyo, selecione **Fluxos** > **Criar fluxo**.
2. Selecione **Crie seu próprio**.
3. Para **Nome**, insira o nome do fluxo do seu portal BrazeAI Decisioning Studio™ Go. Em seguida, selecione **Criar manualmente**.

![A opção "Criar manualmente" selecionada para um fluxo de exemplo.]({% image_buster /assets/img/decisioning_studio_go/flow1.png %}){: style="max-width:50%;"}

{: start="4"}
4\. Selecione o gatilho.
5\. Combine o nome da métrica com o nome do evento de gatilho do seu portal BrazeAI Decisioning Studio™ Go.

![Um exemplo de nome de métrica que corresponde ao nome do evento de gatilho "OFE_TEST_CASE_API_EVENT_TRIGGER".]({% image_buster /assets/img/decisioning_studio_go/flow2.png %})

{: start="6"}
6\. Selecione **Salvar**.

{% alert note %}
Se seu experimentador tiver um modelo base, prossiga para a Etapa 2. Se seu experimentador tiver dois ou mais modelos base, pule para [Etapa 3: Adicione uma divisão de disparo ao seu fluxo](#step-3-add-a-trigger-split-to-your-flow).
{% endalert %}

#### Etapa 2: Adicione um e-mail ao seu fluxo (modelo único)

1. Arraste e solte um **Email** após o nó **Disparar**.
2. Nos detalhes do **E-mail**, selecione **Selecionar modelo**.

![Opção "Selecionar modelo" na seção "Detalhes do E-mail".]({% image_buster /assets/img/decisioning_studio_go/flow3.png %})

{: start="3"}
3\. Encontre e selecione seu modelo base. Você pode procurar seu modelo pelo nome do modelo na seção **Recursos para usar** do portal BrazeAI Decisioning Studio™ Go.

![Um exemplo de modelo base no Klaviyo.]({% image_buster /assets/img/decisioning_studio_go/flow4.png %})

{: start="4"}
4\. Selecione **Usar modelo** > **Salvar**.
5\. Para a **Linha de assunto**, insira {% raw %}`{{event.SubjectLine}}`{% endraw %}.
6\. Para **Nome do remetente** e **Endereço de e-mail do remetente**, insira os detalhes que você gostaria de usar.

![Um exemplo de linha de assunto, nome do remetente e endereço de e-mail do remetente para "E-mail 1".]({% image_buster /assets/img/decisioning_studio_go/flow5.png %})

{: start="7"}
7\. Selecione **Concluído**.
8\. Desmarque a caixa **Pular perfis recentemente enviados**, depois selecione **Salvar**.
9\. No nó de e-mail, atualize o modo de **Rascunho** para **Ao vivo**.

![O editor de fluxo do Klaviyo mostrando um nó de Disparo conectado a um nó de E-mail.]({% image_buster /assets/img/decisioning_studio_go/flow6.png %})

Você está pronto! Agora você pode disparar ativações através do BrazeAI Decisioning Studio™ Go.

#### Etapa 3: Adicione uma divisão de disparo ao seu fluxo (múltiplos modelos)

1. Arraste e solte um nó de **Divisão de disparo** após o nó **Disparar**.
2. Selecione o nó **Divisão de disparo** e defina a **Dimensão** para **IDModeloEmail**.

![Diagrama de fluxo do Klaviyo mostrando um nó de Disparo alimentando uma divisão de disparo configurada com a Dimensão IDModeloEmail.]({% image_buster /assets/img/decisioning_studio_go/flow7.png %})

**Adicione seu modelo de e-mail:**

1. No portal BrazeAI Decisioning Studio™ Go, encontre o **ID do Modelo de E-mail** para seu primeiro modelo na seção **Recursos a usar**. Insira o **ID do Modelo de E-mail** no campo **Dimensão**, em seguida, selecione **Salvar**.
2. Arraste e solte um nó de **E-mail** para o ramo **Sim** do **divisor de Disparador**.

![Um fluxo Klaviyo com um nó de divisor de Disparador, que tem um ramo Sim levando a um nó de E-mail e um ramo Não conectando a outro divisor de Disparador.]({% image_buster /assets/img/decisioning_studio_go/flow8.png %})

{: start="3"}
3\. Na **detalhes do E-mail**, selecione **Selecionar modelo**.
4\. Encontre e selecione seu modelo base. Você pode procurar seu modelo pelo nome do modelo base na seção **Recursos a usar** do portal BrazeAI Decisioning Studio™ Go.
5\. Selecione **Usar modelo** > **Salvar**.
6\. Para a **linha de assunto**, insira {% raw %}`{{event.SubjectLine}}`{% endraw %}.
7\. Para **Nome do remetente** e **Endereço de e-mail do remetente**, insira os detalhes que você gostaria de usar.

![Um modelo de e-mail selecionado e campos para a linha de assunto, nome do remetente e endereço de e-mail do remetente.]({% image_buster /assets/img/decisioning_studio_go/flow5.png %})

{: start="8"}
8\. Selecione **Concluído**.
9\. Desmarque a caixa de seleção **Pular perfis recentemente enviados**, depois selecione **Salvar**.
10\. No nó de e-mail, atualize o modo de **Rascunho** para **Ao vivo**.

**Adicione uma nova divisão de disparo para cada modelo adicional:**

1. Arraste e solte outro nó **Divisão de disparo** na ramificação **Não** do nó de **Divisão de disparo** anterior.
2. Defina a **Dimensão** para **ID do Modelo de E-mail** e preencha o valor da **Dimensão** com o **ID do Modelo de E-mail** do modelo base que você está configurando.
3. Selecione **Salvar**.

![Diagrama de um editor de fluxo Klaviyo mostrando um nó de Disparo levando a uma divisão de Disparo. A divisão de Disparo tem uma ramificação Sim que leva a um nó de E-mail e uma ramificação Não que se conecta a outra divisão de Disparo que leva a nós de E-mail adicionais.]({% image_buster /assets/img/decisioning_studio_go/flow9.png %})

{: start="4"}
4\. Arraste e solte um nó **E-mail** na ramificação **Sim** da sua nova divisão de disparo.
5\. Repita as etapas de configuração do modelo de e-mail acima para selecionar o modelo correspondente.
6\. Defina a **Linha de assunto** para {% raw %}`{{event.SubjectLine}}`{% endraw %}, e desmarque a caixa de seleção **Pular perfis recentemente enviados**.
7\. Repita esse processo até que você tenha um nó **Divisão de disparo** e um nó **E-mail** para cada modelo base que seu experimentador está usando. Sua última divisão de disparo não deve ter nada na ramificação "Não".

![Um fluxo Klaviyo com múltiplos nós de divisão de disparo que ramificam para múltiplos nós de E-mail.]({% image_buster /assets/img/decisioning_studio_go/flow10.png %})

{: start="8"}
8\. Em cada um dos seus nós **E-mail**, atualize o modo de **Rascunho** para **Ao vivo**.

![A opção de atualizar o status do nó para "Ao vivo".]({% image_buster /assets/img/decisioning_studio_go/flow11.png %})

Você está pronto! Agora você pode acionar ativações através do BrazeAI Decisioning Studio™ Go.

{% endtab %}
{% endtabs %}

## Próximos passos

Agora que você configurou a orquestração, prossiga para projetar seu agente:

- [Crie seu agente]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/design_your_agent/)

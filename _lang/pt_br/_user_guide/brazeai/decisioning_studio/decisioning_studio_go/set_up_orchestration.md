---
nav_title: Configurar a orquestração
article_title: Configurar a orquestração
page_order: 2
description: "Saiba como conectar o BrazeAI Decisioning Studio Acessar sua plataforma de engajamento com clientes para ativar comunicações personalizadas."
toc_headers: h2
---

# Configurar a orquestração

> O BrazeAI Decisioning Studio™ Acessar precisa se conectar à sua plataforma de engajamento com clientes (CEP) para orquestrar comunicações personalizadas. Este artigo explica como configurar a integração para cada CEP compatível.

## CEPs com suporte

O Decisioning Studio Acessar é compatível com as seguintes plataformas de engajamento com clientes:

| CEP | Tipo de integração | Principais recursos |
|-----|-----------------|--------------|
| **Braze** | Campanhas disparadas por API | Integração nativa, disparo em tempo real |
| **Salesforce Marketing Cloud** | Journey Builder com eventos de API | Automação de consultas de SQL, extensões de dados |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

Selecione seu CEP abaixo para começar a configurar a integração.

{% tabs %}
{% tab Braze %}

## Configuração da integração com o Braze

Para integrar o Decisioning Studio Acessar o Braze, você criará uma chave de API, configurará uma campanha disparada por API e fornecerá os identificadores necessários ao portal do Decisioning Studio Acessar.

### Etapa 1: Criar uma chave de API REST

1. No dashboard do Braze, vá para **Configurações** > **APIs e Identificadores** > **Chaves de API**.
2. Selecione **Create API Key (Criar chave de API**).
3. Digite um nome para sua chave de API. Um exemplo é "DecisioningStudioGoEmail".
4. Selecione as permissões com base nas seguintes categorias:
    - **Dados de usuários:** selecione `users.track`, `users.delete`, `users.export.ids`, `users.export.segment`
    - **Envio de mensagens:** selecione `messages.send`
    - **Campanhas:** selecione todas as permissões listadas
    - **Canva:** selecione todas as permissões listadas
    - **Segmentos:** selecione todas as permissões listadas
    - **Modelos:** selecione todas as permissões listadas

{: start="5"}
5\. Selecione **Create API key (Criar chave de API**).
6\. Copie a chave de API e cole-a em seu portal BrazeAI Decisioning Studio™ Acessar.

### Etapa 2: Localize o nome de exibição de seu e-mail

1. No painel do Braze, acesse **Settings** > **Email Preferences**( **Configurações** > **Preferências de e-mail**).
2. Localize o nome de exibição a ser usado com o BrazeAI Decisioning Studio™ Acessar.
3. Copie e cole o **nome de exibição De** no portal do BrazeAI Decisioning Studio™ Acessar como o **nome de exibição do e-mail**.
4. Copie e cole o endereço de e-mail associado em seu portal BrazeAI Decisioning Studio™ Acessar como o **endereço de e-mail De**, que combina a parte de localização e o domínio.

### Etapa 3: Encontre seu URL do Braze e o ID do app

**Para encontrar seu URL do Braze:**
1. Acesse o dashboard do Braze.
2. Na janela de seu navegador, o URL do Braze começa com `https://` e termina com `braze.com`. Um exemplo de URL do Braze é `https://dashboard-01.braze.com`.

**Para encontrar seu App ID (chave de API):**

{% alert note %}
O Braze oferece IDs de aplicativos (chamados de chaves de API no dashboard do Braze) que você pode usar para fins de rastreamento, como para associar a atividade a um aplicativo específico em seu espaço de trabalho. Se você usar IDs de aplicativos, o BrazeAI Decisioning Studio™ Acessa a associação de um ID de aplicativo a cada experimentador.<br><br>Se você não usar IDs de app, poderá inserir qualquer string de caracteres como espaço reservado.
{% endalert %}

1. No dashboard do Braze, acesse **Settings** > **App Settings (Configurações**> **Configurações do app**).
2. Acesse o app que deseja rastrear.
3. Copie e cole a **chave de API** em seu portal BrazeAI Decisioning Studio™ Acessar.

### Etapa 4: Criar uma campanha disparada por API

1. No dashboard do Braze, acesse **Envio de mensagens** > Campanhas.
2. Selecione **Criar campanha**.
3. Para seu tipo de campanha, selecione **Campanha API**.
4. Dê um nome à campanha. Um exemplo é o "Decisioning Studio Go Email".

![Uma campanha da API chamada "Decisioning Studio Go Email".]({% image_buster /assets/img/decisioning_studio_go/api_campaign_name.png %})

{: start="5"}
5\. Para seu canal de envio de mensagens, selecione **E-mail**.

![Opção para selecionar seu canal de envio de mensagens para a campanha de mensagens da API.]({% image_buster /assets/img/decisioning_studio_go/select_api_campaign.png %})

{: start="6"}
6\. Em **Additional Options (Opções adicionais**), marque a caixa de seleção **Allow users to become re-eligible to receive campaign (Permitir que os usuários se tornem elegíveis para receber a campanha** ).
7\. Para o tempo para se tornar elegível novamente, digite **1** e selecione **Horas** no menu suspenso.

![Reelegível para a campanha da API selecionada.]({% image_buster /assets/img/decisioning_studio_go/additional_options.png %})

{: start="8"}
8\. Selecione **Save Campaign (Salvar campanha**).

### Etapa 5: Copie suas IDs de campanha e mensagem

1. Em sua campanha da API, copie o **ID da campanha**. Em seguida, acesse o portal do BrazeAI Decisioning Studio™ Acessar e cole o **ID da campanha**.

![Um exemplo de ID de variação de mensagem a ser copiado e colado.]({% image_buster /assets/img/decisioning_studio_go/campaign_id.png %})

{: start="2"}
2\. Copie o **ID da variação de mensagens**. Em seguida, acesse o portal do BrazeAI Decisioning Studio™ Acessar e cole o **ID da variação da mensagem**.

### Etapa 6: Localize um ID de usuário teste

Para testar sua integração, você precisará de um ID de usuário:

1. No dashboard do Braze, acesse **Público** > **Pesquisar usuários**.
2. Procure o usuário por sua ID de usuário externo, alias de usuário, e-mail, número de telefone ou token por push.
3. Copie o ID do usuário para fazer referência em sua configuração.

![Exemplo de perfil de usuário a partir da localização de um usuário com seu ID.]({% image_buster /assets/img/decisioning_studio_go/user_id.png %})

{% endtab %}
{% tab Salesforce Marketing Cloud %}

## Configuração da integração SFMC

Para integrar o Decisioning Studio Acessar com o Salesforce Marketing Cloud, você configurará um pacote de aplicativos, criará uma automação de consulta de dados e criará um Journey para lidar com envios disparados.

### Parte 1: Configure um pacote de aplicativos SFMC

1. Acesse a página inicial do Marketing Cloud.
2. Abra o menu no cabeçalho global e selecione **Setup (Configuração**).
3. Acesse **Apps** em **Platform Tools** na navegação do painel lateral e selecione **Installed Packages (Pacotes instalados**).
4. Selecione **Novo** para criar um pacote de aplicativos.
5. Dê um nome e uma descrição ao pacote do app.

![Um pacote de app com o nome "Experimenter 1 - Test 5".]({% image_buster /assets/img/decisioning_studio_go/sfmc_app_package1.png %})

{: start="6"}
6\. Selecione **Add Component (Adicionar componente**).
7\. Para o **tipo de componente**, selecione **Integração de API**. Em seguida, selecione **Next**.
8\. Para o **Tipo de integração**, selecione **Servidor para servidor**. Em seguida, selecione **Next**.
9\. Selecione os seguintes escopos recomendados apenas para seu pacote de aplicativos:
    \- Canais > E-mail > Ler, escrever, enviar
    \- Canais > OTT > Ler
    \- Canais > Push > Ler
    \- Canais > SMS > Ler
    \- Canais > Social > Ler
    \- Canais > Web > Ler
    \- Ativos > Documentos e imagens > Ler, escrever
    \- Ativos > Conteúdo salvo > Ler, escrever
    \- Automation > Automations > Read, Write, Execute
    \- Automation > Journeys > Ler, escrever, executar, ativar/interromper/pausar/enviar/agendar
    \- Contatos > Públicos > Ler
    \- Contatos > Lista e assinantes > Ler, escrever
    \- Plataforma Cross Cloud > Público do mercado > Visualizar
    \- Plataforma Cross Cloud > Membro do público do mercado > Visualizar
    \- Cross Cloud Platform > Marketing Cloud Connect > Ler
    \- Dados > Extensões de dados > Leitura, gravação
    \- Dados > Locais de arquivos > Ler
    \- Dados > Eventos de rastreamento > Leitura, gravação
    \- Notificações de eventos > Retornos de chamada > Ler
    \- Notificações de eventos > Inscrições > Ler

{% details Show image of recommended scopes %}

![Os escopos recomendados para o pacote do app Salesforce Marketing Cloud.]({% image_buster /assets/img/decisioning_studio_go/app_package_scopes.png %})

{% enddetails %}

{: start="10"}
10\. Selecione **Salvar**.
11\. Copie e cole os seguintes campos no portal do BrazeAI Decisioning Studio™ Acessar: **ID do cliente**, **segredo do cliente**, **URI da base de autenticação**, **URI da base REST**, **URI da base SOAP**.

### Parte 2: Configure uma automação de consulta de dados

#### Etapa 1: Criar uma nova automação

1. Na página inicial do Salesforce Marketing Cloud, acesse **o Journey Builder** e selecione **Automation Studio**.

![Opção Automation Studio na navegação do Journey Builder.]({% image_buster /assets/img/decisioning_studio_go/query13.png %})

{: start="2"}
2\. Selecione **Nova automação**.
3\. Arraste e solte um nó **Schedule** como **fonte inicial**.

!["Schedule" como a fonte inicial de uma Jornada.]({% image_buster /assets/img/decisioning_studio_go/query14.png %})

{: start="4"}
4\. No nó **Schedule**, selecione **Configure**.
5\. Defina o seguinte para a programação:
    - **Data de início:** Dia do calendário de amanhã
    - **Tempo:** **12:00 AM**
    - **Fuso horário:** **(GMT-05:00) Leste (EUA & Canadá)**
6\. Para **Repetir**, selecione **Diariamente**.
7\. Defina essa programação para nunca terminar.
8\. Selecione **Done (Concluído** ) para salvar a programação.

![Um exemplo de programação definida para 25 de janeiro de 2024 às 12 horas ET, a ser repetida todos os dias.]({% image_buster /assets/img/decisioning_studio_go/query12.png %})

#### Etapa 2: Crie suas consultas de SQL

Em seguida, crie duas consultas de SQL: uma consulta de assinantes e uma consulta de engajamento. Essas consultas permitem que o BrazeAI Decisioning Studio™ Acessar recupere dados para preencher o público e ingerir eventos de engajamento.

**Consulta dos assinantes:**

1. Arraste e solte uma **consulta de SQL** na tela.
2. Selecione **Selecionar**.
3. Selecione **Criar nova atividade de consulta**.
4. Dê um nome e uma chave externa à consulta. Recomendamos usar o nome sugerido e a chave externa para a consulta do assinante fornecida em seu portal BrazeAI Decisioning Studio™ Acessar.

![Um exemplo "OFE_Subscribers_query_Test5" e a chave externa.]({% image_buster /assets/img/decisioning_studio_go/query11.png %})

{: start="5"}
5\. Selecione **Próximo**.
6\. Em seu portal BrazeAI Decisioning Studio™ Acessar, localize a consulta de SQL de dados do sistema em **Recursos de consulta do assinante**.
7\. Copie e cole a consulta na caixa de texto e selecione **Next (Avançar**).

![Um exemplo de consulta na seção Consultas de SQL.]({% image_buster /assets/img/decisioning_studio_go/query10.png %})

{: start="8"}
8\. Em seu portal BrazeAI Decisioning Studio™ Acessar, na seção **Recursos a serem usados**, localize a chave externa da extensão de dados de direcionamento. Em seguida, cole-o na barra de pesquisa para pesquisar.

![Uma chave externa colada na barra de pesquisa]({% image_buster /assets/img/decisioning_studio_go/query9.png %})

{: start="9"}
9\. Selecione a extensão de dados que corresponde à chave externa que você pesquisou. O nome da extensão de dados de direcionamento também é fornecido em seu portal BrazeAI Decisioning Studio™ Acessar para referência cruzada. A **extensão de dados** para a consulta do assinante deve terminar com um sufixo `BASE_AUDIENCE_DATA`.

![O nome da extensão de dados que corresponde à chave externa de exemplo.]({% image_buster /assets/img/decisioning_studio_go/query8.png %})

{: start="10"}
10\. Selecione **Overwrite** e, em seguida, **Next**.

**Consulta sobre engajamento:**

1. Arraste e solte uma **consulta de SQL** na tela.

!["Consultas de SQL" adicionadas como uma atividade no Journey.]({% image_buster /assets/img/decisioning_studio_go/query7.png %})

{: start="2"}
2\. Selecione **Selecionar**.
3\. Selecione **Criar nova atividade de consulta**.
4\. Dê um nome e uma chave externa à consulta. Recomendamos usar o nome sugerido e a chave externa para a consulta de engajamento fornecida em seu portal BrazeAI Decisioning Studio™ Acessar.

![Um exemplo "OFE_Engagement_query" e a chave externa.]({% image_buster /assets/img/decisioning_studio_go/query6.png %})

{: start="5"}
5\. Selecione **Próximo**.
6\. Em seu portal BrazeAI Decisioning Studio™ Acessar, localize a consulta de SQL de dados do sistema em **Recursos de consulta de engajamento**.
7\. Copie e cole a consulta na caixa de texto e selecione **Next (Avançar**).

![Um exemplo de consulta na seção Consultas de SQL.]({% image_buster /assets/img/decisioning_studio_go/query5.png %})

{: start="8"}
8\. Localize e selecione a extensão de dados de direcionamento para a consulta de engajamento especificada em seu portal BrazeAI Decisioning Studio™ Acessar.

{% alert tip %}
O nome da extensão de dados de direcionamento também é fornecido em seu portal BrazeAI Decisioning Studio™ Acessar para referência cruzada. Certifique-se de que está olhando para a extensão de dados de destino da consulta de engajamento. A **extensão de dados** para a consulta de engajamento deve terminar com um sufixo ENGAGEMENT_DATA.
{% endalert %}

{: start="9"}
9\. Selecione **Overwrite** e, em seguida, **Next**.

![O nome da extensão de dados que corresponde à chave externa de exemplo.]({% image_buster /assets/img/decisioning_studio_go/query4.png %})

#### Etapa 3: Executar a automação

1. Dê um nome à automação e selecione **Salvar**.

![Um exemplo de automação "OFE_Experimenter_Test5_Automation".]({% image_buster /assets/img/decisioning_studio_go/query3.png %})

{: start="2"}
2\. Em seguida, selecione **Run Once** para confirmar que tudo está funcionando como esperado.
3\. Selecione ambas as consultas e selecione **Run (Executar**).

![Uma automação "OFE_Experimenter_Test5_Automation" com uma lista de atividades de consultas de SQL selecionadas a serem executadas.]({% image_buster /assets/img/decisioning_studio_go/query2.png %})

{: start="4"}
4\. Selecione **Run Now (Executar agora**).

![Uma atividade de consulta de SQL selecionada.]({% image_buster /assets/img/decisioning_studio_go/query1.png %})

Agora, você pode verificar se a automação está sendo executada com êxito. Entre em contato com o suporte da Braze para obter mais assistência se a sua automação não estiver funcionando como esperado.

### Parte 3: Crie sua jornada na SFMC

#### Etapa 1: Configurar a jornada

1. No Salesforce Marketing Cloud, acesse **Journey Builder** > **Journey Builder**.
2. Selecione **Create New Journey (Criar nova jornada**).
3. Para seu tipo de jornada, selecione **Multi-Step Journey (Jornada em várias etapas**) e, em seguida, selecione **Create (Criar**).

![Uma fonte de entrada de evento de API conectada a um nó de divisão de decisão e a vários nós de e-mail.]({% image_buster /assets/img/decisioning_studio_go/journey1.png %})

#### Etapa 2: Construir a jornada

**Criar uma fonte de entrada:**

1. Para sua fonte de entrada, arraste **API Event** para o Journey Builder.

!["Evento API" selecionado como a fonte de entrada.]({% image_buster /assets/img/decisioning_studio_go/journey2.png %})

{: start="2"}
2\. Em **API Event (Evento API**), selecione **Create an event (Criar um evento**).

![A opção "criar um evento" no evento da API.]({% image_buster /assets/img/decisioning_studio_go/journey3.png %})

{: start="3"}
3\. Selecione **Select Data Extension (Selecionar extensão de dados**). Localize e selecione a extensão de dados para a qual o BrazeAI Decisioning Studio™ Acessará as recomendações.
4\. Selecione **Summary (Resumo** ) para salvar suas alterações.
5\. Selecione **Concluído** para salvar o evento da API.

![Resumo do evento da API.]({% image_buster /assets/img/decisioning_studio_go/journey4.png %}){: style="max-width:80%;"}

**Adicionar uma divisão de decisão:**

1. Arraste e solte uma **divisão de decisão** após o **evento de entrada da API**.
2. Nos detalhes da **divisão de decisão**, selecione **Editar** para a primeira jornada.

![Detalhes da divisão de decisão com o botão "Edit" (Editar).]({% image_buster /assets/img/decisioning_studio_go/journey5.png %})

{: start="3"}
3\. Atualize a **divisão de decisão** para usar o ID do modelo passado pela extensão de dados de recomendações. Localize o campo apropriado em **Journey Data**.

![A seção Journey Data na jornada 1 da divisão de decisão.]({% image_buster /assets/img/decisioning_studio_go/journey6.png %})

{: start="4"}
4\. Selecione seu evento de entrada e localize o campo de ID do modelo desejado e, em seguida, arraste-o para o espaço de trabalho.

![O ID do modelo de e-mail a ser incluído.]({% image_buster /assets/img/decisioning_studio_go/journey7.png %})

{: start="5"}
5\. Digite o ID do modelo de seu primeiro modelo de e-mail e selecione **Concluído**.
6\. Selecione **Summary (Resumo** ) para salvar essa jornada.
7\. Adicione uma jornada para cada um de seus modelos de e-mail e, em seguida, repita as etapas 4 a 6 acima para definir os critérios de filtro de modo que o ID do modelo corresponda ao valor de ID de cada modelo.
8\. Selecione **Concluído** para salvar o nó **Divisão de decisão**.

![Duas jornadas em uma divisão de decisão para cada ID de modelo de e-mail.]({% image_buster /assets/img/decisioning_studio_go/journey10.png %}){: style="max-width:65%;"}

**Adicione um e-mail para cada divisão de decisão:**

1. Arraste um nó Envio **de e-mail** para cada jornada da **divisão de decisão**.
2. Selecione Envio **de e-mail** e, em seguida, selecione o modelo apropriado que deve ir em cada jornada (ou seja, o modelo com o valor de ID deve corresponder à lógica em sua divisão de decisão).

![Um nó de e-mail adicionado à Jornada.]({% image_buster /assets/img/decisioning_studio_go/journey9.png %})

#### Etapa 3: Ativar a jornada

Depois de configurar sua Journey, ative-a e compartilhe os seguintes detalhes com a equipe do BrazeAI Decisioning Studio™ Acessar:

* ID da viagem
* Nome da viagem
* Chave de definição de evento da API
* Recomendações chave externa de extensão de dados

{% alert note %}
O portal do BrazeAI Decisioning Studio™ Acessar mostra a automação SFMC que ele provisionou para exportar os dados de assinantes e engajamento uma vez por dia. Se você abrir essa automação no SFMC, certifique-se de cancelar a pausa e voltar a ativá-la.
{% endalert %}

1. No portal do BrazeAI Decisioning Studio™ Acessar, copie o **nome da Jornada**.
2. Em seguida, no Salesforce Marketing Cloud Journey Builder, cole o nome da jornada na barra de pesquisa.
3. Selecione o nome da viagem. Note que a Jornada está atualmente no status de Rascunho.
4. Selecione **Validate (Validar**).

![A jornada completa para ativar.]({% image_buster /assets/img/decisioning_studio_go/activate3.png %})

{: start="5"}
5\. Em seguida, revise os resultados da validação e selecione **Ativar**.

![Recomendações listadas na seção Regras de validação.]({% image_buster /assets/img/decisioning_studio_go/activate1.png %}){: style="max-width:60%;"}

{: start="6"}
6\. No resumo de **Activate Journey**, selecione **Activate** again ( **Ativar** novamente).

![Resumo para a jornada.]({% image_buster /assets/img/decisioning_studio_go/activate2.png %}){: style="max-width:85%;"}

Está tudo pronto! Agora você pode começar a disparar envios por meio do BrazeAI Decisioning Studio™ Acessar.

{% endtab %}
{% endtabs %}

## Próximos passos

Agora que você configurou a orquestração, prossiga para projetar seu agente:

- [Crie seu agente]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/design_your_agent/)

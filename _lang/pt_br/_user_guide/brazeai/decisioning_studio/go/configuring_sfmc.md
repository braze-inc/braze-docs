---
nav_title: Configurar com o Salesforce Marketing Cloud
article_title: Configurar com o Salesforce Marketing Cloud para o BrazeAI Decisioning Studio Acessar
page_order: 5
description: "Saiba como configurar uma automação de consulta de dados e o Journey no Salesforce Marketing Cloud para uso com o BrazeAI Decisioning <sup>StudioTM</sup> Acessar."
toc_headers: h2
---

# Configurar com o Salesforce Marketing Cloud para o BrazeAI Decisioning Studio™ Acessar

> Configure uma Jornada no Salesforce Marketing Cloud (SFMC) para começar a disparar envios por meio do BrazeAI Decisioning Studio™ Acessar.

## Configuração de uma automação de consulta de dados

### Etapa 1: Criar uma nova automação

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

### Etapa 2: Crie suas consultas de SQL

Em seguida, criaremos duas consultas de SQL: uma consulta de assinantes e uma consulta de engajamento. Essas consultas permitem que o BrazeAI Decisioning Studio™ Acessar recupere dados para preencher o público e ingerir eventos de engajamento.

{% tabs %}
{% tab Subscribers query %}
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
{% endtab %}
{% tab Engagement query %}
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
O nome da extensão de dados de direcionamento também é fornecido em seu portal BrazeAI Decisioning Studio™ Acessar para referência cruzada.  Certifique-se de que está olhando para a extensão de dados de destino da consulta de engajamento. A **extensão de dados** para a consulta de engajamento deve terminar com um sufixo ENGAGEMENT_DATA.
{% endalert %}

{: start="9"}
9\. Selecione **Overwrite** e, em seguida, **Next**.

![O nome da extensão de dados que corresponde à chave externa de exemplo.]({% image_buster /assets/img/decisioning_studio_go/query4.png %})

{% endtab %}
{% endtabs %}

### Etapa 3: Executar a automação

1. Dê um nome à automação e selecione **Salvar**.

![Um exemplo de automação "OFE_Experimenter_Test5_Automation".]({% image_buster /assets/img/decisioning_studio_go/query3.png %})

{: start="2"}
2\. Em seguida, selecione **Run Once** para confirmar que tudo está funcionando como esperado.
3\. Selecione ambas as consultas e selecione **Run (Executar**).

![Uma automação "OFE_Experimenter_Test5_Automation" com uma lista de atividades de consultas de SQL selecionadas para execução.]({% image_buster /assets/img/decisioning_studio_go/query2.png %})

{: start="4"}
4\. Selecione **Run Now (Executar agora**).

![Uma atividade de consulta de SQL selecionada.]({% image_buster /assets/img/decisioning_studio_go/query1.png %})

Agora, você pode verificar se a automação está sendo executada com êxito. Entre em contato com o suporte da Braze para obter mais assistência se a sua automação não estiver funcionando como esperado.

## Criando sua jornada na SFMC

### Etapa 1: Configurar a jornada

1. No Salesforce Marketing Cloud, acesse **Journey Builder** > **Journey Builder**.
2. Selecione **Create New Journey (Criar nova jornada**).
3. Para seu tipo de jornada, selecione **Multi-Step Journey (Jornada em várias etapas**) e, em seguida, selecione **Create (Criar**).

![Uma fonte de entrada de evento API conectada a um nó de divisão de decisão e a vários nós de e-mail.]({% image_buster /assets/img/decisioning_studio_go/journey1.png %})

### Etapa 2: Construir a jornada

#### Etapa 2.1: Criar uma fonte de entrada

1. Para sua fonte de entrada, arraste **API Event** para o Journey Builder.

!["Evento API" selecionado como a fonte de entrada.]({% image_buster /assets/img/decisioning_studio_go/journey2.png %})

2. Em **API Event (Evento API**), selecione **Create an event (Criar um evento**).

![A opção "criar um evento" no evento da API.]({% image_buster /assets/img/decisioning_studio_go/journey3.png %})

{: start="3"}
3\. Selecione **Select Data Extension (Selecionar extensão de dados**). Localize e selecione a extensão de dados para a qual o BrazeAI Decisioning Studio™ Acessará as recomendações.
4\. Selecione **Summary (Resumo** ) para salvar suas alterações.
5\. Selecione **Concluído** para salvar o evento da API.

![Resumo do evento da API.]({% image_buster /assets/img/decisioning_studio_go/journey4.png %}){: style="max-width:80%;"}

#### Etapa 2.2: Adicionar uma divisão de decisão

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

#### Etapa 2.3: Adicionar um e-mail para cada divisão de decisão

1. Arraste um nó Envio **de e-mail** para cada jornada da **divisão de decisão**.
2. Selecione Envio **de e-mail** e, em seguida, selecione o modelo apropriado que deve ir em cada jornada (ou seja, o modelo com o valor de ID deve corresponder à lógica em sua divisão de decisão).

![Um nó de e-mail adicionado à Jornada.]({% image_buster /assets/img/decisioning_studio_go/journey9.png %})

### Etapa 3: Ativar a jornada

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

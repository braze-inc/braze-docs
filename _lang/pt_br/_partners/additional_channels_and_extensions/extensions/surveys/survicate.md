---
nav_title: Survicate
article_title: Survicate
description: "Este artigo de referência descreve a parceria entre o Braze e a Survicate, uma plataforma de feedback do cliente que ajuda a coletar, analisar e agir com base nos insights do cliente em vários canais e durante toda a jornada do usuário."
alias: /partners/survicate/
page_type: partner
search_tag: Partner

---

# Survicate

> [A Survicate](https://survicate.com/integrations/braze-survey/?utm_source=braze&utm_medium=integrations&utm_campaign=helpcenter) é uma plataforma de feedback do cliente que coleta, analisa e age com base nos insights do cliente em vários canais e durante toda a jornada do usuário. [Assista a uma demonstração rápida](https://survicate.com/integrations/braze-survey/?utm_source=braze&utm_medium=integrations&utm_campaign=helpcenter)

_Essa integração é mantida pela Survicate._

## Sobre a integração

Use a integração nativa da Survicate e da Braze para sincronizar as respostas de pesquisas por e-mail, no aplicativo, no celular ou na Web com os perfis de clientes da Braze. As respostas da pesquisa são sincronizadas automaticamente com os perfis de usuário do Braze como atributos ou eventos personalizados. As percepções de feedback em tempo real facilitam o rastreamento e a análise do feedback juntamente com os dados de clientes e a criação de direcionamentos e segmentos hiperpersonalizados. 

## Casos de uso

A Braze e a Survicate trabalham juntas para cobrir uma série de casos de uso de feedback, ajudando-o a coletar insights práticos sobre o usuário e a melhorar a experiência do cliente:

- Melhore as taxas de resposta das pesquisas com pesquisas incorporadas que podem ser respondidas em uma caixa de entrada de e-mail. 
- Reúna insights em estágios críticos da jornada do cliente por meio do Braze In-App Message. 
- Use o feedback armazenado no Survicate para criar segmentos mais inteligentes no Braze. 
- Automatize campanhas de acompanhamento com base no feedback do cliente. 
- Use os insights dos clientes para disparar fluxos de trabalho personalizados. 
- Alcance um público mais amplo com pesquisas traduzidas automaticamente.
- Envie eventos para os perfis de contato do Braze quando alguém responder à sua pesquisa

## Pré-requisitos

| Requisito | Descrição |
| ----------- | ----------- |
| Conta Survicate | Você precisa de uma conta Survicate para ativar essa integração. |
| Chave da API REST do Braze | Uma chave da API REST do Braze com a permissão `users.track`. <br><br> Isso pode ser criado no dashboard do Braze em **Configurações** > **APIs e identificadores**. |
| Ponto de extremidade REST do Braze | [Sua URL de endpoint REST.]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints) Seu endpoint dependerá do URL do Braze para sua instância. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Principais recursos da integração

A integração entre a Survicate e a Braze oferece sincronização de dados em tempo real, de modo que as informações mais atualizadas das pesquisas da Survicate ficam imediatamente disponíveis na Braze. Com base nas respostas da pesquisa, você pode usar esses dados para tomar medidas oportunas e personalizadas.

- **Envie as respostas da pesquisa para o Braze como atributos personalizados do usuário**: Enriqueça os perfis de usuários do Braze com dados de respostas de pesquisas.
- **Disparar eventos personalizados no Braze**: Use eventos baseados nas respostas da pesquisa para direcionar grupos específicos ou iniciar campanhas de acompanhamento.
- **Crie segmentos detalhados**: Crie segmentos Braze usando dados das pesquisas Survicate para personalizar ainda mais seu alcance.

## Integração

### Criando suas pesquisas no Survicate

#### Incorpore sua pesquisa em um e-mail ou crie uma pesquisa com link compartilhável 

1.  No Survicate, clique em **\+ Criar nova pesquisa**, selecione qualquer método de criação (um modelo, usando a criação de pesquisa por IA ou adicionando suas próprias perguntas) e o tipo de pesquisa E-mail ou Link compartilhável:
![Braze é selecionado no criador da pesquisa.]({% image_buster /assets/img/survicate/survicate_1.gif %})

{: start="2"}
2\. Na guia Configure (Configurar) da pesquisa, selecione **Braze** como a ferramenta para identificar os entrevistados:
![Braze é selecionado na guia Configure (Configurar) do questionário.]({% image_buster /assets/img/survicate/survicate_2.png %})

{: start="3"}
3\. Depois de configurar o questionário, acesse a guia Compartilhar e decida como enviar o questionário por e-mail. Há duas opções: pode enviar a **pesquisa como um link** ou **incorporar a primeira pergunta no e-mail** para que os questionados comecem a responder à pesquisa diretamente do e-mail.

{% details Survey link option %}

1. Pegue um link para seu questionário no botão Copiar link do questionário:

![Pegue um link para seu questionário no botão Copiar link do questionário.]({% image_buster /assets/img/survicate/survicate_3.png %})

{: start="2"}
2\. Oculte o link da pesquisa atrás de um botão de CTA ou hiperlink em seu e-mail do Braze.

![Oculte o link da pesquisa atrás de um botão de CTA ou hiperlink em seu e-mail do Braze.]({% image_buster /assets/img/survicate/survicate_4.png %})

{% enddetails %}

{% details Email embed option %}

Exiba a primeira pergunta diretamente no corpo do e-mail para iniciar a pesquisa a partir do e-mail. Os entrevistados são então redirecionados para uma landing page para responder ao restante da pesquisa.

1. Clique em **Obter código de e-mail** e, em seguida, **Copie o código HTML**:

![Obter código de e-mail]({% image_buster /assets/img/survicate/survicate_5.gif %})

{: start="2"}
2\. Acesse a campanha do Braze que deseja usar para a pesquisa, clique em **Editar corpo do e-mail** e adicione um bloco HTML ao seu modelo:

![Obter código de bloco HTML]({% image_buster /assets/img/survicate/survicate_6.png %})

{: start="3"}
3\. Substitua o código pelo código que você copiou do questionário Survicate. Em seguida, você verá a primeira pergunta do questionário no modelo:

![Substitua o código pelo código que você copiou de sua pesquisa do Survicate]({% image_buster /assets/img/survicate/survicate_7.png %})

{: start="4"}
4\. Programe o envio do e-mail, escolha seu grupo-alvo e sua campanha estará pronta para ser enviada.

{% enddetails %}

### Pesquisa de mensagens no app do Braze

1. Clique em **\+ Criar nova pesquisa**, selecione qualquer método de criação (um modelo, usando a criação de pesquisa IA ou adicionando suas próprias perguntas) e, em seguida, escolha Pesquisas na plataforma e o tipo de pesquisa Mensagem no app do Braze:

![Clique em + Criar nova pesquisa, selecione qualquer método de criação]({% image_buster /assets/img/survicate/survicate_8.gif %})

{: start="2"}
2\. Inicie sua pesquisa de mensagem no app do Braze navegando até sua conta Braze e, em seguida, em Envio **de mensagens > Campanhas > Criar campanha > Mensagem no app:**
![Inicie sua pesquisa de mensagens no app do Braze]({% image_buster /assets/img/survicate/survicate_9.gif %})

### Inicie sua pesquisa no Braze In-App Messenger por meio do editor tradicional

1. Se você usar o editor tradicional, no Tipo de mensagem, selecione **Código personalizado**:

![escolha Código personalizado]({% image_buster /assets/img/survicate/survicate_10.gif %})

{: start="2"}
2\. Em seguida, cole o código da guia Launch (Iniciar) do seu questionário no campo HTML:

![cole o código da guia Launch de seu questionário no campo HTML]({% image_buster /assets/img/survicate/survicate_11.gif %})

{% alert note %}
Por padrão, o Braze exibe mensagens no app em um iframe enquanto o plano de fundo do app está bloqueado. Para permitir a interação com seu app, enquanto as pesquisas Survicate são exibidas, é necessário:<br><br>

- Adicione `opts.useBrazeIframeClipper = true` ao seu snippet Survicate-Braze.
- Instale o [pacote](https://www.npmjs.com/package/@survicate/braze-bridge-npm) `@survicate/braze-bridge-npm` no arquivo em que você inicializa o Braze e usa a função `initBrazeBridge`.

Você pode encontrar um snippet de amostra e a implementação do React [no site de desenvolvedores do Survicate](https://developers.survicate.com/javascript/installation/#braze).
{% endalert %}

{: start="3"}
3\. Em sua campanha no Braze, configure as etapas Target e Assign. Quando concluída, sua campanha estará pronta para ser lançada. Na etapa Review (Revisão), você pode ver a aparência da campanha. A pesquisa aparece em seu site no local especificado no painel Survicate, conforme descrito acima.

### Ativando a integração do Braze

1. Para ativar a integração do Braze, acesse **Integrações**, pesquise e selecione "Braze".

![Selecione Braze]({% image_buster /assets/img/survicate/survicate_12.gif %})

{: start="2"}
2\. Clique em **Connect (Conectar** ) para configurar a autorização.

3. Insira a chave de API do espaço de trabalho de sua conta Braze e o URL das instâncias da Braze:

![Insira a chave de API do espaço de trabalho de sua conta Braze e o URL das instâncias da Braze]({% image_buster /assets/img/survicate/survicate_13.png %})

{% alert important %}
Para conectar a Survicate ao Braze, a chave de API do Braze precisa ter as permissões `users.track`.
{% endalert %}

### Conectando suas pesquisas ao Braze

Agora que a integração do Braze está conectada, você pode definir configurações individuais para cada pesquisa. Acesse sua pesquisa, selecione a guia **Connect (Conectar** ) e escolha **Braze** na lista de integrações disponíveis.

![Acesse sua pesquisa, selecione a guia Connect (Conectar) e escolha Braze]({% image_buster /assets/img/survicate/survicate_14.png %})

### Envio de respostas ao Braze como atributos personalizados

Configure as respostas da pesquisa para fluir para o Braze como atributos personalizados, o que enriquece os perfis de usuários do Braze com os dados coletados.

1. Na guia Settings (Configurações) do Braze Integration, ajuste a seção **Update fields (Atualizar campos** ).

![Selecione a seção Atualizar campos]({% image_buster /assets/img/survicate/survicate_15.png %})

{: start="2"}
2\. Selecione a pergunta da qual você deseja atualizar os campos. Para evitar a inundação dos perfis de usuários do Braze com dados, é possível enviar respostas apenas para as perguntas escolhidas.

![Selecione a pergunta da qual você deseja atualizar os campos]({% image_buster /assets/img/survicate/survicate_16.png %})

{% alert note %}
As perguntas de classificação e de matriz não são compatíveis com essa integração do Braze.
{% endalert %}

{: start="3"}
3\. Adicione o nome do atributo personalizado que deseja atualizar no campo **Usuário**:

![Adicione o nome do atributo personalizado que deseja atualizar no campo Usuário]({% image_buster /assets/img/survicate/survicate_17.png %})

Por padrão, a Survicate envia o conteúdo de uma resposta de pesquisa como um valor de atribuição. Você pode alterar o rótulo para torná-lo mais curto ou ajustá-lo à sua estrutura de dados, clicando em **Edit mapping (Editar mapeamento** ) para modificar esses valores:

![Resposta da pesquisa como um valor de atribuição]({% image_buster /assets/img/survicate/survicate_18.png %})

![Clique em editar mapeamento para modificar esses valores]({% image_buster /assets/img/survicate/survicate_19.png %})

{% alert note %}
Para o NPS, a Survicate envia valores mapeados com base no grupo de resposta para a pergunta do NPS®. No entanto, se quiser receber valores numéricos, você pode ativar a opção Enviar respostas como valores de 0 a 10.
{% endalert %}

![O Survicate envia valores mapeados com base no grupo de resposta]({% image_buster /assets/img/survicate/survicate_20.png %})

{: start="4"}
4\. Conecte mais perguntas à sua integração clicando em **\+ Adicionar nova** e aplicando as mesmas etapas.

![Conecte mais perguntas à sua integração]({% image_buster /assets/img/survicate/survicate_21.png %})

### Envio de eventos para os perfis dos contatos do Braze

Além das configurações anteriores, cada vez que um entrevistado responde a uma pergunta da pesquisa, a Survicate pode enviar um evento personalizado no Braze chamado `survicate-question-answered`.
No painel Survicate, em Send responses as custom attributes (Enviar respostas como atributos personalizados), você pode escolher se deseja enviar o evento para todas as perguntas, para as perguntas escolhidas na guia Update fields (Atualizar campos) ou para nenhuma pergunta:

![você pode escolher se deseja enviar o evento para todas as perguntas]({% image_buster /assets/img/survicate/survicate_22.png %})

Se você optar por enviar os eventos, poderá ver nos perfis dos usuários quantas vezes eles responderam às pesquisas do Survicate e quando foi a última vez que responderam:

![Respostas ]({% image_buster /assets/img/survicate/survicate_23.png %})

O evento contém propriedades de evento com a resposta à pergunta e informações sobre a pesquisa, a pergunta e o respondente. Você pode usar esse evento para criar segmentos. Por exemplo, crie um segmento de usuários que responderam a uma pesquisa após uma determinada data ou um determinado número de vezes:

![O evento contém propriedades de evento com a resposta]({% image_buster /assets/img/survicate/survicate_24.png %})

Você também pode usar esses dados ao criar uma campanha no Braze.

![Você também pode usar esses dados ao criar uma campanha no Braze]({% image_buster /assets/img/survicate/survicate_25.png %})

### Teste a integração

Quando o questionário estiver pronto e a integração configurada, é possível testá-lo sem sair do Survicate, clicando no botão Testar integração ao lado de qualquer atribuição, tag ou configuração de novo contato que tenha sido criada. O Survicate cria um contato de teste (`braze-test@survicate.com`) na sua conta Braze. O perfil do contato inclui campos atualizados de acordo com a configuração.

![Clique no botão Testar integração]({% image_buster /assets/img/survicate/survicate_26.png %})

No Braze, você vê dados de amostra dos campos mapeados no contato fictício Survicate:

![Dados de amostra dos campos mapeados no contato fictício do Survicate]({% image_buster /assets/img/survicate/survicate_27.png %})

### Análise dos resultados da pesquisa

Depois de coletar as respostas por meio da pesquisa do Braze, é hora de analisar o feedback e os insights que os entrevistados compartilharam. O Survicate permite que você analise facilmente os resultados, as estatísticas e as tendências para tomar medidas adicionais.

### Feedback no Survicate

Depois que o questionário começar a coletar respostas, elas serão exibidas imediatamente na guia Análise do questionário.

![Respostas na guia Analisar]({% image_buster /assets/img/survicate/survicate_28.png %})

A guia Analisar mostra os resultados gerais com estatísticas e dados ao longo do tempo, bem como respostas individuais para examinar detalhadamente cada envio de pesquisa.

### Feedback em Braze

Se atualizar os campos de usuários com as respostas da pesquisa ou enviar respostas como eventos personalizados, poderá ver os dados da pesquisa sincronizados em tempo real. No Braze, acesse um contato específico que respondeu à sua pesquisa. Você vê os dados baseados em resposta e os eventos na visualização principal do contato.

![dados da pesquisa sincronizados em tempo real]({% image_buster /assets/img/survicate/survicate_29.png %}) 
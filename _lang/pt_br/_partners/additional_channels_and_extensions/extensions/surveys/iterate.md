---
nav_title: Iterate
article_title: Iterate
alias: /partners/iterate/
description: "Este artigo de referência descreve a parceria entre o Braze e a Iterate, permitindo que você enriqueça os dados de clientes usando pesquisas para acrescentar insights adicionais."
page_type: partner
search_tag: Partner

---

# Iterate

> [A Iterate](https://iteratehq.com) facilita o aprendizado com seus clientes, oferecendo ferramentas de pesquisa inteligentes e fáceis de usar que se parecem com a sua marca.

_Essa integração é mantida pela Iterate._

## Sobre a integração

A integração da Iterate com a Braze permite que você forneça pesquisas da Iterate de forma nativa e prática em seu produto ou campanhas. As respostas da pesquisa podem ser registradas como atributos personalizados do usuário no Braze, permitindo que você construa uma imagem completa dos seus usuários ou crie novos e poderosos públicos e segmentos.

Com o SDK do Braze instalado em seu aplicativo ou site, você pode usar as ferramentas de segmentação e direcionamento disponíveis no Braze para entregar pesquisas por meio de mensagens no app a uma parte específica do seu público com base em qualquer disparo ou segmento personalizado. As pesquisas da Iterate também podem ser incorporadas diretamente em suas campanhas de e-mail ou incluídas como links em seu push ou em outros tipos de campanha.

## Pré-requisitos

| Requisito | Origin |
|---|---|
|Conta da Iterate | É necessário ter uma [conta da Iterate](https://iteratehq.com) para usar a parceria. |
| chave da API REST Braze | Uma chave da API REST da Braze com `users.track` permissões. Para enviar pesquisas por meio de mensagens no app da Braze, você também precisará da permissão `kpi.mau.data_series`.<br><br> Isso pode ser criado no dashboard do Braze em **Configurações** > **Chaves de API**.|
| Ponto de extremidade REST do Braze  | Sua URL de endpoint REST. Seu endpoint dependerá da [URL do Braze para sua instância]({{site.baseurl}}/api/basics/#endpoints). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Casos de uso

Com a Iterate, você pode coletar praticamente qualquer tipo de dados. Desde informações pessoais (nome, idade, e-mail), dados de performance (NPS, satisfação do cliente, classificação por estrelas), preferências (dispositivo preferido, frequência preferida de comunicação) ou personalidade (livro favorito, cachorro ou gato). O que você pergunta depende inteiramente de você e do tipo de dados que deseja coletar ou do público que deseja construir.

## Integração

### Como começar: Conectar o Braze com o Iterate

Registre sua conta Iterate e adicione seu endpoint Braze REST e a chave da API REST na página **Company Settings (Configurações da empresa** ).

### Envie pesquisas como uma mensagem no app

#### Etapa 1: Crie sua pesquisa

Antes de criar sua pesquisa, ative a opção **Ativar pesquisas por mensagem no app** nas configurações do Iterate.

Em seguida, crie uma nova pesquisa na Iterate e adicione perguntas de pesquisa relevantes. Se apropriado, também é possível incluir uma mensagem de aviso a ser exibida antes da pesquisa. Selecione **Enviar via mensagem no app do Braze** como o tipo de pesquisa.

Quando a pesquisa estiver concluída, na guia **Publicar**, copie o snippet de código em **Copiar e cole o código de incorporação**.

#### Etapa 2: Compartilhe sua pesquisa

No Braze, crie uma nova campanha de mensagens no app com **código personalizado**, selecione-o como o tipo de mensagem e cole o snippet de código na mensagem. Em seguida, selecione **Wait for User to Dismiss** como o comportamento ao clicar na mensagem.

Continue configurando sua campanha como faria com qualquer outra campanha de mensagens no app, escolhendo um método de entrega e direcionando um público.

### Envie pesquisas por e-mail ou push

#### Etapa 1: Crie sua pesquisa

Crie uma nova pesquisa por e-mail ou link no Iterate e adicione perguntas de pesquisa relevantes. Depois que as perguntas tiverem sido escritas e você tiver personalizado o design, selecione **Send survey (Enviar pesquisa) > Integrations (Integrações) > Braze**.

Em seguida, você verá as opções de configuração para enviar respostas à Braze. Ative a integração para ativar o envio de respostas dessa pesquisa para o Braze. 

#### Etapa 2: Compartilhe sua pesquisa

Sua pesquisa pode ser compartilhada de duas maneiras: incorporando a primeira pergunta em sua mensagem ou incluindo um link direto para a pesquisa na plataforma Iterate.

![Iterar opções de links]({% image_buster /assets/img/iterate.png %})

- **Incorporar o código**
  - Copie o snippet de código em **Código de incorporação de e-mail** na seção de integração do Braze na guia **Enviar questionário**. Insira o código no HTML de seu e-mail do Braze onde deseja que o início da pesquisa apareça. 
  - Se estiver tendo dificuldades para renderizar as perguntas do questionário ou se elas parecerem formatadas incorretamente, será necessário acessar a guia **Informações de envio** no criador de mensagens e desmarcar **CSS em linha**.
- **Incluir um link**
  - Copie o link em **Survey Link** na seção de integração do Braze na guia **Enviar pesquisa**. Note que o Liquid incluído no link {% raw %}`?user_braze_id={{${braze_id}}}`{% endraw %} será automaticamente substituído para cada usuário após o envio.

### Próximos passos: criar campanhas de acompanhamento

À medida que os usuários respondem, você verá o preenchimento dos perfis deles com dados em tempo real. Esses dados podem ser usados para segmentar usuários e enviar campanhas de acompanhamento personalizadas. Por exemplo, se você enviar a pergunta "Você gosta dos nossos produtos?", poderá criar segmentos de usuários que tenham o atributo personalizado `Do you enjoy our products?` e que tenham respondido "Sim" ou "Não" e direcionar esses usuários.

## Eventos personalizados do Braze

Quando um usuário responde a uma pergunta da pesquisa, a Iterate dispara um evento personalizado na Braze chamado `survey-question-response`. Os eventos personalizados permitem que você dispare qualquer número e tipo de campanhas de acompanhamento.

## Personalizar nomes de atributos de usuários

Por padrão, o atributo de usuário criado para uma pergunta é o mesmo que o prompt.
Em alguns casos, você pode querer personalizar isso. Para fazer isso, clique no menu suspenso **Personalizar nomes de atributos de usuário** na etapa **Criar seu questionário** e insira os nomes personalizados que desejar.



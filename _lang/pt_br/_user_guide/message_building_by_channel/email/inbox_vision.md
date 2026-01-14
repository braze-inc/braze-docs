---
nav_title: Visão da caixa de entrada
article_title: Visão da caixa de entrada
page_order: 9
description: "Esta página aborda como configurar o Inbox Vision, um recurso que permite que os profissionais de marketing visualizem seus e-mails a partir da perspectiva de vários clientes de e-mail e dispositivos móveis."
tool:
  - Dashboard
channel:
  - email

---

# Visão da caixa de entrada

> O Inbox Vision permite que você visualize seus e-mails sob a perspectiva de vários clientes de e-mail e dispositivos móveis. Por exemplo, você pode usar o Inbox Vision para testar as diferenças entre os modos escuro e claro para confirmar que seus e-mails estão corretos.

{% alert important %}
Em geral, seu e-mail não funcionará com o Inbox Vision se o conteúdo do e-mail depender de informações de modelo, como informações de perfil de usuário. Isso ocorre porque os modelos do Braze em um usuário vazio quando enviamos e-mails usando esse recurso.<br><br>Verifique se você adicionou valores padrão a qualquer Liquid em sua mensagem de e-mail. Se nenhum valor padrão for fornecido, você poderá receber um falso positivo ou o teste poderá não ser executado.
{% endalert %}

## Testando seu e-mail no Inbox Vision

Seu e-mail deve incluir uma linha de assunto e um domínio de envio válido para que você possa ver essas visualizações. Lembre-se de como seu e-mail pode ser renderizado de forma diferente no desktop e nos dispositivos móveis. Ao visualizar essas prévias, você pode revisar o conteúdo e garantir que o e-mail esteja sendo exibido como pretendido.

Para testar sua mensagem de e-mail no Inbox Vision, faça o seguinte:

1. Vá para seu editor de arrastar e soltar ou editor de e-mail HTML.
2. Em seu editor, selecione **Preview & Test**.
3. Selecione **Visão da caixa de entrada**.
4. Selecione **Run Inbox Vision**. Isso pode levar de dois a dez minutos para ser concluído.
5. Em seguida, selecione um bloco para ver a visualização em mais detalhes. Essas visualizações estão agrupadas nas seguintes seções: **Clientes Web**, **clientes de aplicativos** e **clientes móveis**.

\![Visão geral do Inbox Vision para o editor HTML.]({% image_buster /assets/img_archive/inboxvision1.png %})

{: start="6"}
6\. Faça alterações em um modelo, se necessário.
7\. Selecione **Reexecutar teste** para ver as visualizações atualizadas.

{% alert note %}
O Inbox Vision não é compatível se sua mensagem de e-mail incluir [lógica de cancelamento,]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/aborting_messages) pois esses e-mails são renderizados como conteúdo estático.
{% endalert %}

### Pré-visualização como usuário

Quando você visualiza o e-mail como um usuário aleatório, quaisquer configurações ou atributos específicos associados a um usuário, como seu nome ou preferências, não são salvos para visualizações atuais ou futuras. Quando você seleciona um usuário personalizado, a visualização mostrada no Inbox Vision pode ser diferente da visualização da mensagem em outro lugar, pois essa opção usa dados específicos do usuário para criar a visualização

## Análise de código

A análise de código é uma maneira de o Braze destacar os problemas que podem existir em seu HTML, mostrando o número de ocorrências de cada problema e fornecendo informações sobre quais elementos HTML não são compatíveis.

### Exibição de informações de análise de código

Essas informações podem ser encontradas na guia **Inbox Vision**, selecionando <i class="fas fa-list"></i> **List view**. Esse modo de exibição de lista está disponível apenas para modelos de e-mail HTML. Se estiver usando modelos de e-mail do tipo arrastar e soltar, verifique as visualizações para resolver possíveis problemas.

\![Exemplo de análise de código na visualização do Inbox Vision.]({% image_buster /assets/img_archive/inboxvision2.png %})

{% alert note %}
Às vezes, a análise de código será exibida mais rapidamente do que a visualização para um cliente de e-mail específico. Isso ocorre porque o Braze aguarda até que o e-mail chegue à caixa de entrada antes de fazer a captura de tela.
{% endalert %}

## Teste de spam

Os testes de spam tentam prever se seu e-mail chegará às pastas de spam ou às caixas de entrada de seus clientes. Os testes de spam são executados nos principais filtros de spam, como IronPort, SpamAssassin e Barracuda, bem como nos principais filtros de provedores de serviços de Internet (ISP), como Gmail.com e Outlook.com.

### Exibição dos resultados do teste de spam

Para verificar os resultados do teste de spam, faça o seguinte:

1. Selecione a guia **Spam Testing (Teste de spam** ) na seção **Inbox Vision (Visão da caixa de entrada** ). A tabela **Spam Test Result (Resultado do teste de spam** ) lista o nome, o status e o tipo do filtro de spam.

\![Tabela de resultados do teste de spam com três colunas: Nome, status e tipo. Há uma lista de filtros de spam e filtros de ISP que foram aprovados no teste de spam, indicando que a campanha de e-mail não será enviada para a pasta de spam.]({% image_buster /assets/img_archive/email_spam_testing.png %})

{: start="2"}
2\. Analise esses resultados e faça os ajustes necessários em sua campanha de e-mail.
3\. Selecione **Re-run Test (Reexecutar teste** ) para recarregar os resultados do teste de spam.

## Teste de acessibilidade

O teste de acessibilidade no Inbox Vision destaca os problemas de acessibilidade que podem existir em seu e-mail para fornecer informações sobre quais elementos não estão atendendo aos padrões de acessibilidade. Ele analisa o conteúdo de seu e-mail em relação a algumas Diretrizes de Acessibilidade de Conteúdo da Web[(WCAG](https://www.w3.org/WAI/standards-guidelines/wcag/)). As WCAG são um conjunto de padrões técnicos reconhecidos internacionalmente e desenvolvidos pelo World Wide Web Consortium (W3C) para tornar o conteúdo da Web mais acessível a pessoas com deficiências. 

### Como funciona

Quando você executa um teste do Inbox Vision, a ferramenta verifica automaticamente se há problemas comuns de acessibilidade de e-mail no [conjunto de regras WCAG 2.2 AA](https://www.w3.org/WAI/WCAG22/quickref/?versions=2.2&currentsidebar=%23col_customize&levels=aaa), como texto alternativo ausente, contraste de cores insuficiente e estrutura de cabeçalho inadequada, e categoriza a gravidade de cada problema para ajudá-lo a priorizar as correções. 

{% alert important %}
Os Testes de Acessibilidade podem ser usados para apoiar os esforços de conformidade do Cliente com regulamentos ou leis, como a [Lei de Acessibilidade Europeia](https://www.braze.com/resources/articles/european-accessibility-at-what-it-means-for-marketers). No entanto, o Cliente reconhece que a Braze não faz representações ou garantias com relação ao fato de o uso dos Testes de Acessibilidade satisfazer ou não as obrigações de conformidade do Cliente e se isenta de qualquer responsabilidade com relação a isso.
{% endalert %}

### Visualização dos resultados dos testes de acessibilidade

O teste de acessibilidade gerará resultados para cada regra como aprovado, reprovado ou precisa de revisão na guia **Teste de acessibilidade**. Cada regra é categorizada usando POUR (Perceivable, Operable, Understandable, Robust), que são os quatro princípios principais por trás das WCAG.

#### Categorias POUR

Os problemas são categorizados de acordo com os quatro [princípios](https://www.w3.org/WAI/WCAG22/Understanding/intro#understanding-the-four-principles-of-accessibility) fundamentais [do POUR](https://www.w3.org/WAI/WCAG22/Understanding/intro#understanding-the-four-principles-of-accessibility): Perceptível, operável, compreensível e robusto. Cada princípio aborda um aspecto diferente do design acessível.

| Princípio | Definição |
| --- | --- |
| Perceptível | As informações e os componentes da interface do usuário devem ser apresentados aos usuários de forma que eles possam perceber.<br><br>Os usuários devem ser capazes de perceber as informações que estão sendo apresentadas (elas não podem ser invisíveis para todos os seus sentidos). |
| Operável | Os componentes da interface do usuário e a navegação devem ser operáveis.<br><br>Os usuários devem ser capazes de operar a interface (a interface não pode exigir uma interação que um usuário não possa realizar). |
| Compreensível | As informações e a operação da interface do usuário devem ser compreensíveis.<br><br>Os usuários devem ser capazes de entender as informações, bem como a operação da interface do usuário (o conteúdo ou a operação não podem estar além de sua compreensão). |
| Robusto | O conteúdo deve ser suficientemente robusto para que possa ser interpretado de forma confiável por uma ampla variedade de agentes de usuário, incluindo tecnologias assistivas.<br><br>Os usuários devem poder acessar o conteúdo à medida que as tecnologias avançam (à medida que as tecnologias e os agentes de usuário evoluem, o conteúdo deve permanecer acessível). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Níveis de gravidade

O Inbox Vision classifica os problemas de acessibilidade por gravidade para ajudá-lo a priorizar os esforços de correção.

| Status | Definição |
| --- | --- |
| Crítico | Problemas que podem bloquear o acesso ao conteúdo ou à funcionalidade para usuários com deficiências. Esses são os mais graves e devem ser priorizados para correção. |
| Sério | Problemas que podem causar barreiras significativas, mas não podem bloquear completamente o acesso. Elas devem ser tratadas prontamente. |
| Moderado | Problemas que podem causar alguma dificuldade para usuários com deficiências, mas que têm menos probabilidade de bloquear totalmente o acesso. |
| Menor | Problemas que têm um impacto relativamente baixo na acessibilidade e podem causar apenas pequenos inconvenientes. |
| Precisa de revisão | Não é possível detectar se há um problema ou não. Isso pode ocorrer quando não é possível determinar a taxa de contraste, pois o texto é colocado em uma imagem de fundo. Isso precisará ser revisado manualmente, pois não pode ser determinado automaticamente. |
| Aprovado | Aprovado nas WCAG A, AA ou nas práticas recomendadas de acessibilidade. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert important %}
Atualmente, o editor de arrastar e soltar e-mails não suporta a configuração de um elemento do documento `<title>`. Como resultado, o scanner de acessibilidade sempre falhará nessa verificação.<br><br>
Estamos monitorando essa limitação para melhorias futuras. Se isso afetar seus fluxos de trabalho ou seus usuários, [compartilhe seus comentários]({{site.baseurl}}/user_guide/administrative/access_braze/navigation/#sharing-feedback) para que possamos priorizar as correções mais impactantes.
{% endalert %}

### Compreensão dos testes automatizados de acessibilidade

{% multi_lang_include accessibility/automated_testing.md %}

## Precisão do teste

Todos os nossos testes são executados em clientes de e-mail reais. A Braze trabalha arduamente para verificar se todas as renderizações são as mais precisas possíveis. Se você sempre encontrar um problema com um cliente de e-mail, abra um [tíquete de suporte]({{site.baseurl}}/braze_support/).

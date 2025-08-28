---
nav_title: Inbox Vision
article_title: Inbox Vision
page_order: 9
description: "Esta página cobre como configurar o Inbox Vision, um recurso que permite aos profissionais de marketing visualizar seus e-mails a partir da perspectiva de vários clientes de e-mail e dispositivos móveis."
tool:
  - Dashboard
channel:
  - email

---

# Inbox Vision

> O Inbox Vision permite visualizar seus e-mails a partir da perspectiva de vários clientes de e-mail e dispositivos móveis. Por exemplo, você pode usar o Inbox Vision para testar as diferenças entre os modos escuro e claro para confirmar que seus e-mails estão exatamente certos.

{% alert important %}
Em geral, seu e-mail não funcionará com o Inbox Vision se o conteúdo do seu e-mail depender de informações de modelagem, como informações do perfil do usuário. Isso ocorre porque o Braze cria modelos em um usuário vazio quando enviamos e-mails usando esse recurso.<br><br>Certifique-se de ter adicionado valores padrão a qualquer Liquid em sua mensagem de e-mail. Se nenhum valor padrão for fornecido, você pode receber um falso positivo ou o teste pode falhar ao ser executado.
{% endalert %}

## Teste seu envio de e-mail no Inbox Vision

Seu e-mail deve incluir uma linha de assunto e um domínio de envio válido para que possa ver essas prévias. Lembre-se de como seu e-mail pode ser renderizado de forma diferente no desktop e nos dispositivos móveis. Ao visualizar essas prévias, é possível revisar o conteúdo e garantir que o e-mail esteja sendo exibido como pretendido.

Para testar sua mensagem de e-mail no Inbox Vision, faça o seguinte:

1. Acesse o editor de arrastar e soltar ou o editor de e-mail HTML.
2. No seu editor, selecione **Ver prévia e testar**.
3. Selecione **Inbox Vision**.
4. Selecione **Executar Inbox Vision**. Isso pode levar entre dois a dez minutos para ser concluído.
5. Em seguida, selecione um tile para visualizar a prévia com mais detalhes. Essas prévias estão agrupadas nessas seções: **Clientes Web**, **Clientes de Aplicativo** e **Clientes Móveis**.

![Visão geral do Inbox Vision para o editor de HTML.]({% image_buster /assets/img_archive/inboxvision1.png %})

{: start="6"}
6\. Faça alterações em um modelo, se necessário.
7\. Selecione **Refazer teste** para ver as prévias atualizadas.

{% alert note %}
O Inbox Vision não é suportado se sua mensagem de e-mail incluir [lógica de abortar]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/aborting_messages), pois esses e-mails são renderizados como conteúdo estático.
{% endalert %}

### Visualizando como um usuário

Quando você faz uma prévia do e-mail como um usuário aleatório, quaisquer configurações ou atributos específicos associados a um usuário, como seu nome ou preferências, não são salvos para prévias atuais ou futuras. Quando você seleciona um usuário personalizado, a prévia exibida no Inbox Vision pode diferir da prévia da mensagem em outros lugares, pois esta opção usa dados de usuários específicos para criar a prévia.

## Análise de código

A análise de código é uma maneira de o Braze destacar os problemas que podem existir em seu HTML, mostrando o número de ocorrências de cada problema e fornecendo insight sobre quais elementos HTML não são suportados.

### Exibição de informações de análise de código

Essas informações podem ser encontradas na guia **Inbox Vision**, selecionando <i class="fas fa-list"></i> **List view**. Esse modo de exibição de lista está disponível apenas para modelos de e-mail em HTML. Se estiver usando modelos de e-mail do tipo arrastar e soltar, verifique as prévias para resolver possíveis problemas.

![Análise de código de exemplo na prévia do Inbox Vision.]({% image_buster /assets/img_archive/inboxvision2.png %})

{% alert note %}
Às vezes, a análise de código será exibida mais rapidamente do que a prévia para um cliente de e-mail específico. Isso ocorre porque o Braze espera até que o e-mail chegue à caixa de entrada antes de fazer a captura de tela.
{% endalert %}

## Teste de spam

Os testes de spam tentam prever se seu e-mail chegará às pastas de spam ou às caixas de entrada de seus clientes. Os testes de spam são executados nos principais filtros de spam, como IronPort, SpamAssassin e Barracuda, bem como nos principais filtros de provedores de acesso à internet, como Gmail.com e Outlook.com.

### Exibição dos resultados do teste de spam

Para verificar os resultados do seu teste de spam, faça o seguinte:

1. Selecione a guia de **Teste de spam** na seção **Inbox Vision**. A tabela **Spam Test Result (Resultado do teste de spam** ) lista o nome, o status e o tipo do filtro de spam.

![Tabela "Spam Test Result" com três colunas: Nome, status e tipo. Há uma lista de filtros de spam e filtros de ISP que passaram no teste de spam, indicando que a campanha de e-mail não cairá na pasta de spam.]({% image_buster /assets/img_archive/email_spam_testing.png %})

{: start="2"}
2\. Revise esses resultados e faça os ajustes necessários na sua e-mail campanha.
3\. Selecione **Refazer teste** para recarregar os resultados do seu teste de spam.

## Teste de acessibilidade

O teste de acessibilidade no Inbox Vision destaca problemas de acessibilidade que podem existir em seu e-mail para fornecer insights sobre quais elementos não estão atendendo aos padrões de acessibilidade. Ele analisa o conteúdo do seu e-mail em relação a algumas Diretrizes de Acessibilidade de Conteúdo da Web ([WCAG](https://www.w3.org/WAI/standards-guidelines/wcag/)). WCAG é um conjunto de padrões técnicos reconhecidos internacionalmente desenvolvidos pelo World Wide Web Consortium (W3C) para tornar o conteúdo da web mais acessível a pessoas com deficiência. 

### Como funciona?

Quando você executa um teste do Inbox Vision, a ferramenta verifica automaticamente problemas comuns de acessibilidade em e-mails no [conjunto de regras WCAG 2.2 AA](https://www.w3.org/WAI/WCAG22/quickref/?versions=2.2&currentsidebar=%23col_customize&levels=aaa), como texto alternativo ausente, contraste de cores insuficiente e estrutura de cabeçalho inadequada, e então categoriza a gravidade de cada problema para ajudá-lo a priorizar as correções. 

{% alert important %}
O Teste de Acessibilidade pode ser usado para apoiar os esforços de conformidade do Cliente com regulamentos ou leis, como o [Atos de Acessibilidade da Europa](https://www.braze.com/resources/articles/european-accessibility-at-what-it-means-for-marketers), no entanto, o Cliente reconhece que a Braze não faz representações ou garantias com relação a se o uso do Teste de Acessibilidade satisfaz as obrigações de conformidade do Cliente e isenta-se de toda responsabilidade em relação a isso.
{% endalert %}

### Visualizando os resultados do teste de acessibilidade

O teste de acessibilidade gerará resultados para cada regra como aprovado, reprovado ou precisa de revisão na aba **Teste de Acessibilidade**. Cada regra é categorizada usando POUR (Perceptível, Operável, Compreensível, Robusto), que são os quatro princípios principais por trás do WCAG.

#### Categorias POUR

Os problemas são categorizados sob os quatro princípios fundamentais [POUR](https://www.w3.org/WAI/WCAG22/Understanding/intro#understanding-the-four-principles-of-accessibility): Perceptível, Operável, Compreensível e Robusto. Cada princípio aborda um aspecto diferente do design acessível.

| Princípio | Definição |
| --- | --- |
| Perceptível | Os componentes de informação e interface do usuário devem ser apresentáveis aos usuários de maneiras que eles possam perceber.<br><br>Os usuários devem ser capazes de perceber as informações apresentadas (não pode ser invisível a todos os seus sentidos). |
| Operável | Os componentes da interface do usuário e a navegação devem ser operáveis.<br><br>Os usuários devem ser capazes de operar a interface (a interface não pode exigir interação que um usuário não possa realizar). |
| Compreensível | As informações e a operação da interface do usuário devem ser compreensíveis.<br><br>Os usuários devem ser capazes de entender as informações, bem como a operação da interface do usuário (o conteúdo ou a operação não pode estar além de sua compreensão). |
| Robusto | O conteúdo deve ser robusto o suficiente para que possa ser interpretado de forma confiável por uma ampla variedade de agentes de usuário, incluindo tecnologias assistivas.<br><br>Os usuários devem ser capazes de acessar o conteúdo à medida que as tecnologias avançam (à medida que as tecnologias e os agentes de usuário evoluem, o conteúdo deve permanecer acessível). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Níveis de severidade

O Inbox Vision classifica problemas de acessibilidade por severidade para ajudar você a priorizar os esforços de remediação.

| Status | Definição |
| --- | --- |
| Crítico | Problemas que podem bloquear o acesso ao conteúdo ou funcionalidade para usuários com deficiência. Estes são os mais severos e devem ser priorizados para correção. |
| Sério | Problemas que podem causar barreiras significativas, mas podem não bloquear completamente o acesso. Estes devem ser tratados prontamente. |
| Moderado | Problemas que podem causar alguma dificuldade para usuários com deficiência, mas são menos propensos a bloquear completamente o acesso. |
| Leve | Problemas que têm um impacto relativamente baixo na acessibilidade e podem causar apenas pequenos inconvenientes. |
| Necessita de revisão | Incapaz de detectar se pode haver um problema ou não. Isso pode ocorrer quando não conseguimos determinar a razão de contraste, pois o texto está colocado em uma imagem de fundo. Isso precisará ser revisado manualmente porque não pode ser determinado automaticamente. |
| Aprovado | Aprovado WCAG A, AA ou melhores práticas de acessibilidade. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert important %}
O editor de arrastar e soltar de e-mail atualmente não suporta a configuração de um elemento `<title>`. Como resultado, o scanner de acessibilidade sempre falhará nesta verificação.<br><br>
Estamos rastreando essa limitação para melhorias futuras. Se isso afetar seus fluxos de trabalho ou seus usuários, [compartilhe seu feedback]({{site.baseurl}}/user_guide/administrative/access_braze/navigation/#sharing-feedback) para que possamos priorizar as correções mais impactantes.
{% endalert %}

### Entendendo testes de acessibilidade automatizados

{% multi_lang_include accessibility/automated_testing.md %}

## Precisão do teste

Todos os nossos testes são executados em clientes de e-mail reais. A Braze trabalha arduamente para verificar se todas as renderizações são as mais precisas possíveis. Se você sempre encontrar um problema com um cliente de e-mail, abra um [tíquete de suporte]({{site.baseurl}}/braze_support/).

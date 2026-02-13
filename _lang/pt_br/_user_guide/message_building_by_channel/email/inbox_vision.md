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

> O Inbox Vision permite visualizar seus e-mails sob a perspectiva de vários clientes de e-mail e dispositivos móveis. Por exemplo, você pode testar as diferenças entre os modos escuro e claro para confirmar que seus e-mails são renderizados conforme o esperado.

{% alert important %}
O Inbox Vision poderá não funcionar se o conteúdo do seu e-mail depender de informações de modelo, como dados de perfil de usuários. O Braze modela um usuário vazio ao enviar e-mails para esse recurso.<br><br>Adicione valores padrão a qualquer Liquid em sua mensagem de e-mail. Sem os padrões, você pode receber um falso positivo ou o teste pode falhar.
{% endalert %}

## Considerações

Em geral, seu e-mail não funcionará com o Inbox Vision se o conteúdo do e-mail depender de informações de modelo, como informações de perfil de usuário. Isso ocorre porque o Braze modela um usuário vazio quando enviamos e-mails usando esse recurso.

Você pode resolver isso adicionando valores padrão ou quaisquer valores do Liquid em sua mensagem de e-mail antes de executar o Inbox Vision. Quando você terminar o teste no Inbox Vision, a mensagem de e-mail original será exibida. Se nenhum valor for fornecido, o teste poderá falhar ao renderizar as prévias com êxito.

Sua empresa tem um limite para o número de e-mails que podem ser prévios com o Inbox Vision. Você pode monitorar isso na guia **Pré-visualizações de e-mail** do Inbox Vision.

Inclua uma linha de assunto e um domínio de envio válido para exibir prévias. Esteja atento às diferenças de renderização entre desktop e celular. Use as prévias para confirmar que o e-mail está sendo exibido como pretendido.

Para testar sua mensagem de e-mail no Inbox Vision:

1. Acesse o editor de arrastar e soltar ou o editor de e-mail HTML.
2. Em seu editor, selecione **Pré-visualização & Test**.
3. Selecione **Inbox Vision**.
4. Selecione **Executar Inbox Vision**. Isso leva até dez minutos.
5. Em seguida, selecione um tile para visualizar a prévia com mais detalhes. Essas prévias estão agrupadas nessas seções: **Clientes Web**, **Clientes de Aplicativo** e **Clientes Móveis**.

![A opção de selecionar clientes de e-mail para prévia.]({% image_buster /assets/img/select_email_preview_inbox_vision.png %}){: style="max-width:85%;"}

{:start="5"}
5\. Selecione **Executar Inbox Vision**. Isso pode levar entre dois a dez minutos para ser concluído.

{% alert note %}
O Inbox Vision não oferece suporte a mensagens de e-mail que incluem [lógica de abortar]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/aborting_messages) porque esses e-mails são renderizados como conteúdo estático.
{% endalert %}

### Visualizando como um usuário

Ao fazer uma prévia como um usuário aleatório, o Inbox Vision não salva configurações ou atribuições específicas do usuário (como nome ou preferências). Quando você seleciona um usuário personalizado, a visualização do Inbox Vision pode ser diferente de outras prévias porque usa dados de usuários específicos.

## Análise de código

A análise de código destaca possíveis problemas de HTML, mostra o número de ocorrências e indica elementos HTML sem suporte.

### Exibição de informações de análise de código

Encontre essas informações na guia **Inbox Vision**, selecionando <i class="fas fa-list"></i> **List view**. A exibição de lista está disponível apenas para modelos de e-mail em HTML. No caso de modelos do tipo arrastar e soltar, use prévias para resolver problemas.

![Exemplo de análise de código na prévia do Inbox Vision.]({% image_buster /assets/img_archive/inboxvision2.png %})

{% alert note %}
A análise do código pode aparecer mais rapidamente do que a prévia de um cliente específico porque o Braze aguarda a chegada do e-mail antes de fazer a captura de tela.
{% endalert %}

## Teste de spam

Os testes de spam preveem se seu e-mail vai parar nas pastas de spam ou nas caixas de entrada. O Braze executa testes nos principais filtros de spam (IronPort, SpamAssassin, Barracuda) e nos principais filtros de provedores de acesso à internet (Gmail.com, Outlook.com).

### Exibição dos resultados do teste de spam

Para verificar os resultados do teste de spam:

1. Selecione a guia de **Teste de spam** na seção **Inbox Vision**. A tabela **Spam Test Result (Resultado do teste de spam** ) lista o nome, o status e o tipo do filtro de spam.
2. Analise esses resultados e faça os ajustes necessários em sua campanha de e-mail.
3. Selecione **Refazer teste** para recarregar os resultados do seu teste de spam.

## Teste de acessibilidade

O teste de acessibilidade destaca possíveis problemas de acessibilidade em seu e-mail e mostra quais elementos não atendem aos padrões. O Braze analisa o conteúdo de acordo com as[WCAG (](https://www.w3.org/WAI/standards-guidelines/wcag/)Web Content Accessibility Guidelines, Diretrizes de Acessibilidade para Conteúdo da Web), um conjunto de padrões internacionalmente reconhecidos desenvolvidos pelo W3C para tornar o conteúdo da Web mais acessível.

### Como funciona?

Quando você executa o Inbox Vision, o Braze verifica automaticamente se há problemas comuns de acessibilidade no [conjunto de regras WCAG 2.2 AA](https://www.w3.org/WAI/WCAG22/quickref/?versions=2.2&currentsidebar=%23col_customize&levels=aaa) (como texto alternativo ausente, contraste de cor insuficiente, estrutura de cabeçalho inadequada) e categoriza a gravidade para ajudá-lo a priorizar as correções. 

{% alert important %}
Os Testes de Acessibilidade podem ser usados para apoiar os esforços de conformidade do Cliente com regulamentos ou leis, como a [Lei de Acessibilidade Europeia](https://www.braze.com/resources/articles/european-accessibility-at-what-it-means-for-marketers); no entanto, o Cliente reconhece que a Braze não faz representações ou garantias com relação ao fato de o uso dos Testes de Acessibilidade satisfazer ou não as obrigações de conformidade do Cliente e se isenta de qualquer responsabilidade com relação a isso.
{% endalert %}

### Visualização dos resultados dos testes de acessibilidade

O teste de acessibilidade gera resultados para cada regra como aprovado, reprovado ou precisa de revisão na guia **Teste de acessibilidade**. O Braze categoriza cada regra usando POUR (Perceivable, Operable, Understandable, Robust), os quatro princípios por trás das WCAG.

#### Categorias POUR

O Inbox Vision categoriza os problemas de acordo com os quatro [princípios](https://www.w3.org/WAI/WCAG22/Understanding/intro#understanding-the-four-principles-of-accessibility) fundamentais [do POUR](https://www.w3.org/WAI/WCAG22/Understanding/intro#understanding-the-four-principles-of-accessibility): Perceptível, operável, compreensível e robusto.

| Princípio | Definição |
| --- | --- |
| Perceptível | As informações e os componentes da interface do usuário devem ser apresentados aos usuários de forma que eles possam perceber.<br><br>Os usuários devem ser capazes de perceber as informações que estão sendo apresentadas (elas não podem ser invisíveis para todos os seus sentidos). |
| Operável | Os componentes da interface do usuário e a navegação devem ser operáveis.<br><br>Os usuários devem ser capazes de operar a interface (a interface não pode exigir interação que um usuário não possa realizar). |
| Compreensível | As informações e a operação da interface do usuário devem ser compreensíveis.<br><br>Os usuários devem ser capazes de entender as informações, bem como a operação da interface do usuário (o conteúdo ou a operação não podem estar além de sua compreensão). |
| Robusto | O conteúdo deve ser suficientemente robusto para que possa ser interpretado de forma confiável por uma ampla variedade de agentes de usuário, incluindo tecnologias assistivas.<br><br>Os usuários devem poder acessar o conteúdo à medida que as tecnologias avançam (à medida que as tecnologias e os agentes de usuário evoluem, o conteúdo deve permanecer acessível). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Níveis de gravidade

O Inbox Vision classifica os problemas de acessibilidade por gravidade para ajudá-lo a priorizar a correção.

| Status | Definição |
| --- | --- |
| Crítico | Problemas que podem bloquear o acesso a conteúdo ou funcionalidade para usuários com deficiência. Esses são os mais graves e devem ser priorizados para correção. |
| Sério | Problemas que podem causar barreiras significativas, mas não podem bloquear completamente o acesso. Elas devem ser tratadas prontamente. |
| Moderado | Problemas que podem causar alguma dificuldade para usuários com deficiências, mas que têm menos probabilidade de bloquear totalmente o acesso. |
| Leve | Problemas que têm um impacto relativamente baixo na acessibilidade e podem causar apenas pequenos inconvenientes. |
| Precisa de revisão | Não é possível detectar se há um problema ou não. Isso pode ocorrer quando não é possível determinar a taxa de contraste, pois o texto é colocado em uma imagem de fundo. Você deve revisar manualmente, pois isso não pode ser determinado automaticamente. |
| Aprovado | Aprovado nas WCAG A, AA ou nas práticas recomendadas de acessibilidade. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert important %}
O editor de arrastar e soltar não suporta a configuração de um elemento do documento `<title>`, portanto, o scanner de acessibilidade sempre falha nessa verificação.<br><br>Essa limitação é rastreada para melhorias futuras. Se isso afetar seus fluxos de trabalho ou seus usuários, [compartilhe seu feedback]({{site.baseurl}}/user_guide/administrative/access_braze/navigation/#sharing-feedback) para que possamos priorizar correções impactantes.
{% endalert %}

### Compreensão dos testes automatizados de acessibilidade

{% multi_lang_include accessibility/automated_testing.md %}

## Melhores práticas

### Analise sua lista de assinantes de e-mail

Consulte o [dashboard de insights de e-mail]({{site.baseurl}}/user_guide/analytics/dashboard/email_performance_dashboard#email-insights-dashboard) para determinar o tipo de dispositivo mais popular e os provedores de [e-mail]({{site.baseurl}}/user_guide/analytics/dashboard/email_performance_dashboard#email-insights-dashboard) com os quais seus assinantes estão se engajando. Se precisar de mais granularidade, como o navegador, o modelo do dispositivo e muito mais, poderá aproveitar os dados do [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents) ou o [Query Builder]({{site.baseurl}}/user_guide/analytics/query_builder) para recuperar esse nível de detalhe sobre o recente envio de e-mail dos usuários.

Caso contrário, o Braze usa como padrão as 20 principais prévias com base em dados gerais do setor e de especialistas, que abrangem a maioria dos locais onde seus assinantes estão se engajando com seus e-mails. Se sua análise de dados apontar para outras prévias mais populares, você poderá definir um conjunto padrão de prévias sempre que executar o Inbox Vision.

### Selecione prévias significativas e prévias afetadas

Se a sua empresa estiver sediada principalmente nos EUA, pode haver prévias específicas, como prévias internacionais como GMX.de, que são usadas apenas por um número nominal de usuários. Recomendamos priorizar e otimizar as caixas de entrada com um impacto considerável sobre os assinantes e reservar suas prévias para as caixas de entrada de maior impacto.

Ao fazer correções que afetam prévias específicas, certifique-se de selecionar apenas as prévias afetadas para evitar o consumo de prévias não utilizadas.

### Execute o Inbox Vision na versão final do e-mail

Sugerimos executar o Inbox Vision quando a mensagem de e-mail estiver pronta para produção ou próxima disso. Isso permite reduzir o número de prévias geradas, pois o e-mail passa por várias iterações antes de ser finalizado e estar pronto para ser enviado aos usuários.

A execução do Inbox Vision toda vez que você faz uma única edição ou alteração pode consumir rapidamente as prévias. Sugerimos que você faça todas as alterações necessárias no e-mail primeiro e, em seguida, execute o Inbox Vision para ter uma prévia de como todas as alterações podem afetar o envio de seu e-mail em todos os ambientes.

A Braze executa testes com clientes de e-mail reais e trabalha para garantir que as renderizações sejam precisas. Se você sempre encontrar um problema com um cliente, abra um [tíquete de suporte]({{site.baseurl}}/braze_support/).

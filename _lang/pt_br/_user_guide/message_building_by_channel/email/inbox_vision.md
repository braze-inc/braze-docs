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

> Inbox Vision permite que você visualize seus e-mails a partir da perspectiva de vários clientes de e-mail e dispositivos móveis. Por exemplo, você pode testar as diferenças entre o modo escuro e o modo claro para confirmar se seus e-mails são exibidos como pretendido.

{% alert important %}
O Inbox Vision pode não funcionar se o conteúdo do seu e-mail depender de informações de modelagem, como dados de perfil de usuário. O Braze modela um usuário vazio ao enviar e-mails para esse recurso.<br><br>Adicione valores padrão a qualquer Liquid na sua mensagem de e-mail. Sem valores padrão, você pode receber um falso positivo ou o teste pode falhar.
{% endalert %}

## Considerações

Em geral, seu e-mail não funcionará com o Inbox Vision se o conteúdo do seu e-mail depender de informações de modelagem, como informações de perfil de usuário. Isso ocorre porque o Braze modela um usuário vazio quando enviamos e-mails usando esse recurso.

Você pode resolver isso adicionando valores padrão ou quaisquer valores ao Liquid na sua mensagem de e-mail antes de executar o Inbox Vision. Quando você terminar de testar no Inbox Vision, a mensagem de e-mail original aparecerá. Se nenhum valor for fornecido, o teste pode falhar ao renderizar as prévias com sucesso.

Sua empresa tem um limite de quantos e-mails você pode visualizar com o Inbox Vision. Você pode monitorar isso na aba **Prévias de E-mail** do Inbox Vision.

Inclua uma linha de assunto e um domínio de envio válido para visualizar as prévias. Fique atento às diferenças de renderização entre desktop e mobile. Use as prévias para confirmar que o e-mail aparece como pretendido.

Para testar sua mensagem de e-mail no Inbox Vision:

1. Acesse o editor de arrastar e soltar ou o editor de e-mail HTML.
2. No seu editor, selecione **Prévia & Teste**.
3. Selecione **Inbox Vision**.
4. Selecione **Executar Inbox Vision**. Isso leva até dez minutos.
5. Em seguida, selecione um tile para visualizar a prévia com mais detalhes. Essas prévias estão agrupadas nessas seções: **Clientes Web**, **Clientes de Aplicativo** e **Clientes Móveis**.

![A opção de selecionar clientes de e-mail para visualizar prévias.]({% image_buster /assets/img/select_email_preview_inbox_vision.png %}){: style="max-width:85%;"}

{:start="5"}
5\. Selecione **Executar Inbox Vision**. Isso pode levar entre dois a dez minutos para ser concluído.

{% alert note %}
Inbox Vision não suporta mensagens de e-mail que incluem [abort logic]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/aborting_messages) porque esses e-mails são renderizados como conteúdo estático.
{% endalert %}

### Visualizando como um usuário

Quando você visualiza como um usuário aleatório, o Inbox Vision não salva configurações ou atributos específicos do usuário (como nome ou preferências). Quando você seleciona um usuário personalizado, a prévia do Inbox Vision pode diferir de outras prévias porque usa dados específicos do usuário.

## Análise de código

A análise de código destaca problemas potenciais de HTML, mostra o número de ocorrências e indica elementos HTML não suportados.

### Exibição de informações de análise de código

Encontre essas informações na guia **Inbox Vision** selecionando <i class="fas fa-list"></i> **Lista de visualização**. A lista de visualização está disponível apenas para modelos de e-mail em HTML. Para modelos de arrastar e soltar, use prévias para resolver problemas em vez disso.

![Exemplo de análise de código na prévia do Inbox Vision.]({% image_buster /assets/img_archive/inboxvision2.png %})

{% alert note %}
A análise de código pode aparecer mais rápida do que a prévia para um cliente específico porque o Braze espera até que o e-mail chegue antes de tirar a captura de tela.
{% endalert %}

## Teste de spam

O teste de spam prevê se seu e-mail vai parar em pastas de spam ou na caixa de entrada. O Braze realiza testes em principais filtros de spam (IronPort, SpamAssassin, Barracuda) e principais filtros de ISP (Gmail.com, Outlook.com).

### Exibição dos resultados do teste de spam

Para verificar os resultados do seu teste de spam:

1. Selecione a guia de **Teste de spam** na seção **Inbox Vision**. A tabela **Spam Test Result (Resultado do teste de spam** ) lista o nome, o status e o tipo do filtro de spam.
2. Revise esses resultados e faça quaisquer ajustes na sua campanha de e-mail.
3. Selecione **Refazer teste** para recarregar os resultados do seu teste de spam.

## Teste de acessibilidade

O teste de acessibilidade destaca problemas potenciais de acessibilidade em seu e-mail e mostra quais elementos não atendem aos padrões. O Braze analisa o conteúdo em relação às Diretrizes de Acessibilidade para Conteúdo da Web selecionadas ([WCAG](https://www.w3.org/WAI/standards-guidelines/wcag/)), um conjunto de padrões reconhecidos internacionalmente desenvolvidos pelo W3C para tornar o conteúdo da web mais acessível.

### Como funciona?

Quando você executa o Inbox Vision, o Braze verifica automaticamente problemas comuns de acessibilidade no conjunto de regras [WCAG 2.2 AA](https://www.w3.org/WAI/WCAG22/quickref/?versions=2.2&currentsidebar=%23col_customize&levels=aaa) (como texto alternativo ausente, contraste de cores insuficiente, estrutura de cabeçalho inadequada) e categoriza a gravidade para ajudá-lo a priorizar correções. 

{% alert important %}
O Teste de Acessibilidade pode ser usado para apoiar os esforços de conformidade do Cliente com regulamentos ou leis como a [Lei de Acessibilidade Europeia](https://www.braze.com/resources/articles/european-accessibility-at-what-it-means-for-marketers); no entanto, o Cliente reconhece que o Braze não faz representações ou garantias com relação a se o uso do Teste de Acessibilidade satisfaz as obrigações de conformidade do Cliente e isenta-se de toda responsabilidade em relação a isso.
{% endalert %}

### Visualizando os resultados do teste de acessibilidade

O teste de acessibilidade gera resultados para cada regra como aprovado, reprovado ou precisa de revisão na guia **Teste de Acessibilidade**. O Braze categoriza cada regra usando POUR (Perceptível, Operável, Compreensível, Robusto), os quatro princípios por trás do WCAG.

#### PRINCÍPIOS POUR

A Inbox Vision categoriza problemas sob os quatro princípios fundamentais [POUR](https://www.w3.org/WAI/WCAG22/Understanding/intro#understanding-the-four-principles-of-accessibility): Perceptível, Operável, Compreensível e Robusto.

| Princípio | Definição |
| --- | --- |
| Perceptível | Os componentes de informação e interface do usuário devem ser apresentáveis aos usuários de maneiras que eles possam perceber.<br><br>Os usuários devem ser capazes de perceber as informações que estão sendo apresentadas (não pode ser invisível a todos os seus sentidos). |
| Operável | Os componentes da interface do usuário e a navegação devem ser operáveis.<br><br>Os usuários devem ser capazes de operar a interface (a interface não pode exigir interações que um usuário não possa realizar). |
| Compreensível | As informações e a operação da interface do usuário devem ser compreensíveis.<br><br>Os usuários devem ser capazes de entender as informações, bem como a operação da interface do usuário (o conteúdo ou a operação não podem estar além de sua compreensão). |
| Robusto | O conteúdo deve ser robusto o suficiente para que possa ser interpretado de forma confiável por uma ampla variedade de agentes de usuário, incluindo tecnologias assistivas.<br><br>Os usuários devem ser capazes de acessar o conteúdo à medida que as tecnologias avançam (à medida que as tecnologias e os agentes de usuário evoluem, o conteúdo deve permanecer acessível). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Níveis de severidade

A Inbox Vision classifica problemas de acessibilidade por severidade para ajudar você a priorizar a remediação.

| Status | Definição |
| --- | --- |
| Crítico | Problemas que podem bloquear o acesso ao conteúdo ou funcionalidade para usuários com deficiência. Estes são os mais severos e devem ser priorizados para correção. |
| Sério | Problemas que podem causar barreiras significativas, mas podem não bloquear completamente o acesso. Estes devem ser tratados prontamente. |
| Moderado | Problemas que podem causar alguma dificuldade para usuários com deficiência, mas são menos propensos a bloquear completamente o acesso. |
| Leve | Problemas que têm um impacto relativamente baixo na acessibilidade e podem causar apenas pequenos inconvenientes. |
| Necessita de revisão | Não é possível detectar se pode haver um problema ou não. Isso pode ocorrer quando não conseguimos determinar a proporção de contraste, pois o texto está colocado em uma imagem de fundo. Você deve revisar manualmente, pois não pode ser determinado automaticamente. |
| Aprovado | Aprovado WCAG A, AA ou melhores práticas de acessibilidade. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert important %}
O editor de arrastar e soltar não suporta a configuração de um elemento `<title>`, então o scanner de acessibilidade sempre falha nesta verificação.<br><br>Essa limitação está sendo acompanhada para melhorias futuras. Se isso afetar seus fluxos de trabalho ou seus usuários, [compartilhe seu feedback]({{site.baseurl}}/user_guide/administrative/access_braze/navigation/#sharing-feedback) para que possamos priorizar correções impactantes.
{% endalert %}

### Entendendo testes automatizados de acessibilidade

{% multi_lang_include accessibility/automated_testing.md %}

## Melhores práticas

### Revise sua lista de assinantes de e-mail

Referencie o [painel de insights de e-mail]({{site.baseurl}}/user_guide/analytics/dashboard/email_performance_dashboard#email-insights-dashboard) para determinar o tipo de dispositivo e provedores mais populares onde seus assinantes estão se engajando. Se você precisar de mais granularidade, como o navegador, modelo de dispositivo e mais, pode aproveitar seus dados [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents) ou [Construtor de Consultas]({{site.baseurl}}/user_guide/analytics/query_builder) para recuperar esse nível de detalhe sobre o engajamento recente de e-mail de seus usuários.

Caso contrário, a Braze usa como padrão os 20 principais previews com base em dados gerais da indústria e de especialistas, que cobrem a maioria dos locais onde seus assinantes estão se engajando com seus e-mails. Se sua análise de dados apontar para outros previews mais populares, você pode definir um conjunto padrão de previews toda vez que executar o Inbox Vision.

### Selecione previews significativos e previews impactados

Se seu negócio estiver principalmente baseado nos EUA, pode haver previews específicos, como previews internacionais como GMX.de, que são usados apenas por um número nominal de usuários. Recomendamos priorizar e otimizar para caixas de entrada com um impacto considerável de assinantes e reservar seus previews para caixas de entrada de maior impacto.

Ao fazer correções que afetam previews específicos, certifique-se de selecionar apenas os previews impactados para evitar consumir previews não utilizados.

### Execute o Inbox Vision na versão final do e-mail

Sugerimos executar o Inbox Vision quando a mensagem de e-mail estiver pronta para produção ou próxima disso. Isso permite que você reduza o número de previews gerados, à medida que o e-mail passa por várias iterações antes de ser finalizado e pronto para ser enviado aos usuários.

Executar o Inbox Vision toda vez que você fizer uma única edição ou alteração pode consumir rapidamente as prévias. Sugerimos fazer todas as alterações necessárias no e-mail primeiro e, em seguida, executar o Inbox Vision para visualizar como todas as suas alterações podem afetar a renderização do seu e-mail em diferentes ambientes.

O Braze realiza testes através de clientes de e-mail reais e trabalha para garantir que as renderizações sejam precisas. Se você consistentemente ver um problema com um cliente, abra um [ticket de suporte]({{site.baseurl}}/braze_support/).

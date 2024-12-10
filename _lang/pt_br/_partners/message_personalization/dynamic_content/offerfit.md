---
nav_title: "OfferFit"
article_title: OfferFit
alias: /partners/offerfit/
description: "O OfferFit substitui os testes A/B manuais por testes IA. Os profissionais de marketing de ciclo de vida usam os testes de IA do OfferFit para tomar a melhor decisão 1:1 para cada cliente, testar todas as variáveis simultaneamente e detectar e se adaptar às mudanças do mercado."
page_type: partner
search_tag: OfferFit

---


# OfferFit

> [O OfferFit](https://www.offerfit.ai/) substitui os testes A/B manuais por testes IA. Os profissionais de marketing de ciclo de vida usam os testes de IA do OfferFit para tomar a melhor decisão 1:1 para cada cliente, testar todas as variáveis simultaneamente e detectar e se adaptar às mudanças do mercado.

A integração entre o OfferFit e o Braze permite que você descubra automaticamente a mensagem, o canal e o momento certos para cada cliente com base nos dados de seus clientes. Você pode otimizar suas campanhas para os clientes identificados existentes, com metas comerciais como venda cruzada, venda adicional, recompra, retenção, renovação, indicação e recuperação.

## Pré-requisitos

| Requisito | Descrição |
|-------------|-------------|
| Licença do OfferFit | É necessário ter uma licença ativa do OfferFit para aproveitar essa parceria. |
| chave da API REST Braze | Uma chave da API REST do Braze com as seguintes permissões: {::nomarkdown}<ul><li><code>users.export.ids</code></li><li><code>users.export.segment</code></li><li><code>messages.send</code></li><li><code>campaigns.trigger.send</code></li> <li><code>campaigns.list</code></li><li><code>campaigns.data_series</code></li><li><code>campaigns.details</code></li><li><code>canvas.trigger.send</code></li><li><code>canvas.list</code></li><li><code>canvas.data_series</code></li><li><code>canvas.details</code></li><li><code>segments.list</code></li><li><code>segments.data_series</code></li><li><code>segments.details</code></li><li><code>templates.create</code></li><li><code>templates.update</code></li><li><code>templates.info</code></li><li><code>templates.list</code></li></ul>{:/} Isso pode ser criado no dashboard do Braze em **Configurações** > **Chaves de API**. |
| Ponto de extremidade da API do Braze REST | [Seu URL do ponto de extremidade da API REST][1]. Seu endpoint depende do URL do Braze para sua instância. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert note %}
Se estiver usando a [navegação mais antiga]({{site.baseurl}}/navigation), poderá criar uma chave de API em **Console do desenvolvedor** > **Configurações de API**.
{% endalert %}

### Endpoints da API do Braze REST

Sua licença do OfferFit e o caso de uso determinarão os endpoints da Braze REST API que você usará. Abaixo estão vários endpoints de API que você pode usar.

| Ponto de extremidade da API do Braze REST | Uso do OfferFit |
|--------------|----------------|
| [POST /users/export/ids]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/)                          | Recupere a lista de clientes a serem direcionados por uma campanha ou Canva. Como o OfferFit não aceita dados de IPI, o atributo `fields_to_export` é usado apenas para recuperar os atributos de dados acordados com o usuário da plataforma. |
| [POST /users/export/segment]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment/)                         | Recupere todos os usuários que fazem parte de um segmento específico. Como o OfferFit não aceita dados de IPI, o atributo `fields_to_export` é usado para recuperar apenas os campos que não sejam de IPI acordados com o usuário da plataforma. |
| [POST /users/track]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)                                            | O OfferFit pode usar esse endpoint para atualizar os perfis de usuários com atributos de dados personalizados que podem ser usados para personalizar o envio de mensagens.                                                                                                                                            |
| [POST /messages/send]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/)                         | Disparar uma campanha API no Braze. |
| [POST /campaigns/trigger/send]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/)     | Disparar um envio para uma campanha que esteja configurada para entrega acionada por API. |
| [GET /campaigns/list]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaigns/)                                     | Recupera a lista de todas as campanhas configuradas no Braze e seus metadados associados. |
| [GET /campaigns/data_series]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_analytics/)                     | Recupere os dados de análises de uma campanha específica do Braze. |
| [GET /campaigns/details]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_details/)                           | Recupere os detalhes de uma campanha específica do Braze. |
| [POST /canvas/trigger/send]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/)         | Disparar um envio para um Canva que esteja configurado para entrega acionada por API. |
| [GET /canvas/list]({{site.baseurl}}/api/endpoints/export/canvas/get_canvases/)                                            | Recupera a lista de todas as Canvas configuradas no Braze e seus metadados associados. |
| [GET /canvas/data_series]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics/)                             | Recupere os dados de análises de um Canva específico. |
| [GET /canvas/details]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_details/)                                   | Recupere os detalhes de um Canva específico. |
| [GET /segments/list]({{site.baseurl}}/api/endpoints/export/segments/get_segment/)                                        | Recupera a lista de todos os segmentos configurados no Braze e seus metadados associados. |
| [GET /segments/data_series]({{site.baseurl}}/api/endpoints/export/segments/get_segment_analytics/)                        | Recupera o tamanho do segmento Braze. |
| [GET /segments/details]({{site.baseurl}}/api/endpoints/export/segments/get_segment_details/)                              | Recupere os detalhes de um segmento específico do Braze. |
| [POST /templates/email/create]({{site.baseurl}}/api/endpoints/templates/email_templates/post_create_email_template/)      | Crie um novo modelo de e-mail HTML do Braze. |
| [POST /templates/email/update]({{site.baseurl}}/api/endpoints/templates/email_templates/post_update_email_template/)      | Atualize um modelo de e-mail HTML existente do Braze. |
| [GET /templates/email/info]({{site.baseurl}}/api/endpoints/templates/email_templates/get_see_email_template_information/) | Recupere os detalhes de um modelo específico de e-mail HTML do Braze. |
| [GET /templates/email/list]({{site.baseurl}}/api/endpoints/templates/email_templates/get_list_email_templates/)           | Recupere a lista de todos os modelos de e-mail HTML do Braze configurados no Braze e seus respectivos `subject line` e `HTML content`. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Casos de uso

Depois de [integrar o OfferFit](#integration), você pode automatizar o processo de experimentação fazendo o seguinte:

1. Selecione uma **métrica de sucesso** para maximizar, como receita, conversões, ARPU ou qualquer outra
KPI que você pode medir a partir dos dados de seus clientes. Essa é a métrica que o OfferFit tentará maximizar com sua IA.
2. Selecione as **dimensões** a serem testadas (por exemplo, oferta, linha de assunto, criativo, canal, horário, dia, frequência etc.).
3. Selecione as **opções** disponíveis para cada dimensão. Por exemplo, você pode selecionar e-mail, SMS e push para a dimensão do canal e, em seguida, selecionar diariamente, duas vezes por semana e semanalmente para a dimensão de frequência.

![of_use_case_example][2]


Depois que o processo de experimentação for automatizado, o OfferFit começará a fazer recomendações diárias para cada cliente com o objetivo de maximizar a métrica de sucesso escolhida. 

A IA do OfferFit aprenderá com cada interação com o cliente e aplicará esses insights às recomendações do dia seguinte.


| Caso de uso | Objetivo | Abordagem prévia | Abordagem OfferFit |
|----------|------|----------------|-------------------|
| **Venda cruzada ou venda adicional** | Maximizar a receita média por usuário (ARPU) das inscrições na Internet. | Realizar campanhas anuais oferecendo a cada cliente o plano de nível mais alto. | Descubra empiricamente a melhor mensagem, horário de envio, desconto e plano a ser oferecido para cada cliente, aprendendo quais clientes são suscetíveis a ofertas de salto e quais clientes precisam de descontos ou outros incentivos para fazer upgrade. |
| **Renovação e retenção** | Garantir renovações de contratos, maximizando a duração do contrato e o valor presente líquido (VPL). | Faça testes A/B manualmente e ofereça descontos significativos para garantir renovações. | Use a experimentação automatizada para encontrar a melhor oferta de renovação para cada cliente e identifique os clientes que são menos sensíveis ao preço e precisam de descontos menos significativos para renovar. |
| **Compra recorrente** | Maximizar as taxas de compra e recompra. | Todos os clientes recebem a mesma jornada depois de criar uma conta no site (por exemplo, a mesma sequência de e-mails com a mesma cadência). | Automatize a experimentação para encontrar o melhor item do menu para oferecer a cada cliente, bem como a linha de assunto mais eficaz, o horário de envio e a frequência da comunicação. |
| **Reconquista** | Aumente a reativação incentivando os assinantes anteriores a se inscreverem novamente. | Testes A/B sofisticados e segmentação. | Aproveite a experimentação automatizada para testar milhares de variáveis de uma só vez, descobrindo o melhor criativo, mensagem, canal e cadência para cada indivíduo. |
| **Indicação** | Maximizar as novas contas abertas por meio de indicações de cartões de crédito comerciais de clientes existentes. | Sequência fixa de envio de e-mail para todos os clientes, com extensos Testes A/B para determinar os melhores horários de envio, cadência, etc. para a população de clientes. | Automatize a experimentação para determinar o e-mail, o criativo, o horário de envio e o cartão de crédito ideais para oferecer a clientes específicos. |
| **Nutrição e conversão de leads** | Aumente a receita e pague o valor certo para cada cliente. | À medida que as políticas de privacidade mudam no Facebook e em outras plataformas, as abordagens anteriores para anúncios pagos personalizados se tornam menos eficazes. | Aproveite os dados primários robustos para fazer experiências automáticas com segmentos de clientes, metodologia de lances, níveis de lances e criativos. |
| **Fidelidade e engajamento** | Maximizar as compras de novos inscritos no programa de fidelidade do cliente. | Os clientes receberam uma sequência fixa de e-mails em resposta às suas ações. Por exemplo, todos os novos inscritos no programa de fidelidade recebem a mesma viagem. | Faça experiências automáticas com diferentes ofertas de e-mail, criativos, horários de envio e frequências para maximizar a compra e a recompra de cada cliente. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }


## Integração

### Etapa 1: Definir o público-alvo no Braze

Defina seu público-alvo criando pelo menos um segmento no Braze. Esse segmento será usado para enviar sua campanha ou Canva para os usuários certos.

### Etapa 2: configure uma campanha ou uma tela da Braze disparada por API e crie ativos de campanha (por exemplo, modelos HTML, imagens) {#step-2}

1. Crie uma campanha ou uma tela no Braze. O OfferFit usará essa campanha ou Canva para enviar eventos de ativação personalizados 1:1 para os usuários certos do seu público definido. 
2. Não inclua um [grupo de controle]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/create_multivariate_campaign#including-a-control-group) Braze em sua campanha ou Canva. Isso permite que o grupo de controle do OfferFit seja o único ativo.
3. Dependendo de suas dimensões, é possível configurar Liquid tags em seu conteúdo criativo para preencher dinamicamente sua campanha ou Canva com recomendações do OfferFit. O OfferFit passará o conteúdo específico do cliente para as tags Liquid em seus modelos por meio da API do Braze.

### Etapa 3: Atualize sua configuração de caso de uso do OfferFit para orquestrar eventos de ativação do Braze

Você pode aproveitar a integração da ativação nativa do OfferFit com o Braze para orquestrar e programar recomendações personalizadas 1:1 para seu público-alvo.

## Personalização

Além de orquestrar os eventos de ativação no Braze, o OfferFit fornece recursos de integração de dados que permitem recuperar o perfil do cliente (não IPI) e os dados de engajamento do Braze por meio dos pontos de extremidade da API disponíveis.

## Usando esta integração

Depois que o OfferFit for configurado, a plataforma de experimentação automatizada enviará automaticamente ao Braze eventos de ativação personalizados 1:1 para cada usuário do seu público-alvo. Esses eventos de ativação serão disparados por meio das campanhas Braze ou Canvas que você configurou na [etapa 2](#step-2).

Além dos dados de análises disponíveis no Braze, o OfferFit fornece uma camada abrangente de relatórios que permite que os profissionais de marketing explorem os insights dos clientes descobertos pelo OfferFit por meio de seus recursos de IA de autoaprendizagem.




[1]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints
[2]: {% image_buster /assets/img/offerfit/of_use_case_example.png %}


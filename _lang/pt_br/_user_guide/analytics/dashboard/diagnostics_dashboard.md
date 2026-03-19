---
nav_title: Painel de diagnósticos de envio de mensagens
article_title: Painel de diagnósticos de envio de mensagens
description: "Este artigo de referência cobre o painel de diagnósticos de envio de mensagens, que ajuda você a entender por que as mensagens de suas campanhas ou canvases podem não ter sido enviadas como esperado."
alias: /ccdd/
page_order: 4.5
---

# Painel de diagnósticos de envio de mensagens

> O painel de **Diagnósticos de Envio de Mensagens** fornece uma visão geral dos resultados do envio de mensagens, permitindo que você identifique tendências e diagnostique problemas potenciais na sua configuração de envio de mensagens. Este painel pode ajudar você a entender por que as mensagens de suas campanhas ou canvases podem não ter sido enviadas como esperado.

{% alert important %}
O painel de **Diagnósticos de Envio de Mensagens** está atualmente em acesso antecipado. Entre em contato com seu gerente de sucesso do cliente se você estiver interessado em participar do acesso antecipado.
{% endalert %}

## Conceitos-chave

### Enviadas e entregues

É crucial entender que este painel relata como a Braze processou internamente uma mensagem, não o status final de entrega da mensagem.

Uma mensagem marcada como "enviada" neste painel significa que a Braze processou e despachou a mensagem com sucesso. Para a maioria dos canais, isso significa que a Braze entregou a mensagem ao parceiro de envio de terceiros relevante. No entanto, isso não garante a entrega final ao dispositivo do usuário. 

Quando a Braze "envia" uma mensagem, a entrega final pode depender de serviços externos. Considere os seguintes exemplos para cada canal.

| Canal | Exemplo de entrega final |
| --- | --- |
| Cartões de conteúdo | O cartão foi enviado e está elegível para visualização. |
| E-mail | A Braze entrega a mensagem a um prestador de serviços de e-mail (ESP). O ESP é então responsável pela entrega final. Esse ESP, por exemplo, pode relatar um "bounce" se o endereço de e-mail for inválido ou a caixa de entrada estiver cheia. |
| Mensagem no app | A mensagem foi apresentada ao usuário. |
| LINE | A mensagem foi entregue com sucesso a um parceiro de envio. |
| Push | Braze entrega a mensagem ao serviço de notificação por push apropriado (como o serviço de Notificações por Push da Apple para iOS ou o Firebase Cloud Messaging para Android). Esse serviço é responsável pela entrega final da notificação ao dispositivo. |
| SMS/MMS/RCS | Braze entrega a mensagem a um gateway de SMS (como o Twilio). Esse gateway é responsável pela entrega final à operadora móvel. |
| Webhooks | A solicitação do webhook foi feita com sucesso, retornando uma resposta `2xx`. |
| WhatsApp | A mensagem foi entregue com sucesso a um parceiro de envio. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" } 

### Atualização de dados

A frequência com que os dados neste dashboard são atualizados pode variar com base na carga do sistema. Embora a frequência de atualização não seja garantida, é provável que seja inferior a uma hora na maioria dos casos.

## Configurando o dashboard

Você pode acessar o dashboard de diagnósticos indo para **análise de dados** > **Construtor de Dashboard** e selecionando **Diagnósticos de Envio de Mensagens** na lista de dashboards criados pelo Braze.

Para executar o dashboard e visualizar seus dados:

1. Escolha **Campanhas** ou **Canvases** como a fonte para seus relatórios de dashboard. 
2. Selecione uma ou mais campanhas ou Canvases.
3. Selecione **Executar Dashboard** para carregar os dados para os filtros selecionados.

![Exemplo de diagnósticos de Campanha e Canvas de 25 de maio a 31 de maio de 2025 para uma campanha de série de boas-vindas.]({% image_buster /assets/img/campaign_canvas_dashboard_example.png %}){: style="max-width:90%;"}

## Interpretando os dados

{% alert note %}
O dashboard exibe apenas os dados dos últimos 7 dias.
{% endalert %}

### Blocos de resumo

Na parte superior da página, há blocos de resumo chave para o seu período selecionado que mostram:

- **Total Aborts:** A contagem total de mensagens que foram abortadas. Isso inclui membros do público do Canvas que não entraram no Canvas ou saíram do Canvas porque enfrentaram uma falha de etapa ou atenderam aos critérios de saída durante um evento de saída.
- **Envios de Mensagens:** A contagem total de mensagens que o Braze processou e enviou com sucesso. 
  - **Email, SMS/MMS/RCS, WhatsApp, LINE e push:** A mensagem foi entregue com sucesso a um parceiro de envio.  
  - **Webhooks:** A solicitação do webhook foi feita com sucesso, retornando uma resposta `2xx`.  
  - **Cartões de conteúdo:** O cartão foi enviado e está elegível para visualização.    
  - **Mensagens no app** A mensagem foi exibida para o usuário.

### Resultados das mensagens ao longo do tempo

Este gráfico de séries temporais mostra uma análise dia a dia dos diferentes motivos pelos quais uma mensagem foi abortada ou um usuário foi removido de um Canvas. Este gráfico não exibe o número de envios.  

{% alert note %}
Para manter o gráfico organizado, qualquer motivo de aborto ou remoção com zero ocorrências no intervalo de tempo selecionado não aparece no gráfico.
{% endalert %}

### Análise dos resultados das mensagens

Este gráfico mostra a análise de todos os resultados das mensagens dentro do intervalo de tempo selecionado. Ele fornece uma visão completa de:
- O número total de envios como uma proporção de todos os resultados.  
- A análise proporcional de cada motivo de aborto e remoção. Isso ajuda você a identificar rapidamente os motivos mais comuns pelos quais as mensagens não estão sendo enviadas.

### Resultados de aborto

As definições a seguir explicam os resultados de abortos mostrados no dashboard. Os resultados são agrupados por categoria para facilitar a localização do que você está investigando.

#### Conteúdo e renderização

| Resultado de aborto | Explicação |
| ---- | ---- |
| Cartão de conteúdo expirado | O cartão de conteúdo expirou antes que o usuário o visse. |
| Cartão de conteúdo inválido | O cartão de conteúdo teve erros e não foi enviado ao usuário. Algumas razões comuns para isso incluem: {::nomarkdown}<ul><li> Tamanho máximo excedido (2 KB) </li><li> A data de expiração é inválida </li><li> A mensagem contém caracteres inválidos </li></ul>{:/} |
| Conteúdo conectado falhou | A Braze tentou enviar a mensagem, mas o conteúdo conectado falhou após o número máximo de tentativas (o padrão é cinco). |
| Tempo limite de renderização de mensagem no aplicativo | Após várias tentativas de reenvio, o Liquid não pôde ser renderizado e atingiu o tempo limite. |
| Aborto do Liquid | A tag Liquid [abort_message]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/aborting_messages/#aborting-messages) foi chamada, então o envio foi cancelado. |
| Tempo limite de renderização do Liquid | Demorou muito para renderizar o modelo Liquid. Mais provável de ocorrer para Banners, mensagens no aplicativo e e-mail. |
| Erro de sintaxe do Liquid | O modelo Liquid teve um erro de análise, então a mensagem foi cancelada. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Estado da campanha e do Canvas

| Resultado de aborto | Explicação |
| ---- | ---- |
| Falha na etapa de postergação | A [etapa de postergação]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/delay_step/#personalized-delays) falhou, fazendo com que o usuário saísse do Canvas. Essa falha pode ocorrer quando: {::nomarkdown}<ul><li> A variável fornecida para a etapa de postergação personalizada estava vazia ou era de um tipo inválido </li><li> A postergação ultrapassou a duração máxima permitida dentro do Canvas</li></ul>{:/} |
| Exceção ou evento de saída | O usuário estava anteriormente elegível para receber a mensagem, mas {::nomarkdown}<ul><li> realizou um <a href="/docs/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/#step-3-select-exception-events">evento de exceção</a> para uma campanha baseada em ação, então a mensagem foi abortada, ou </li><li> atendeu aos <a href="/docs/user_guide/engagement_tools/canvas/create_a_canvas/exit_criteria/#setting-up-exit-criteria">critérios de saída</a> do Canvas, então foi descartado no meio da jornada.</li></ul>{:/} |
| Campanha inativa | A campanha foi interrompida enquanto a mensagem estava em andamento, então foi abortada. |
| Canvas inativo | O Canvas foi interrompido antes que o usuário entrasse na jornada. |
| Etapa do Canvas inativa | Isso pode ocorrer no Canvas se: {::nomarkdown}<ul><li> A etapa do Canvas foi excluída </li> <li>O Canvas foi interrompido, o que faz com que todas as etapas se tornem inativas. </li></ul>{:/} |
| Limite de volume | A campanha atingiu o limite de volume definido, então o envio foi cancelado. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Limitação de taxa e tempo

| Resultado de aborto | Explicação |
| ---- | ---- |
| Limite de frequência | O usuário já recebeu o número máximo de mensagens permitidas pelas regras de [limitação de frequência]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#about-frequency-capping) do seu espaço de trabalho, então o envio foi cancelado. |
| Abortar Horário de Silêncio | O Horário de Silêncio foi ativado para a campanha ou etapa do Canvas com o fallback definido para **Mensagem de Abort**. O usuário disparou a campanha ou entrou na etapa de mensagem do Canvas durante o Horário de Silêncio, então a mensagem foi abortada. No entanto, isso não retira o usuário do Canvas. |
| Limitação de taxa por mais de 72 horas | A mensagem foi limitada por mais de 72 horas devido a [limites de taxa de velocidade de entrega]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#delivery-speed-rate-limiting), então o envio foi abortado. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Elegibilidade e perfil do usuário

| Resultado de aborto | Explicação |
| ---- | ---- |
| Identificador de usuário duplicado | Vários usuários com um identificador correspondente (como ID externo, endereço de e-mail, número de telefone) eram elegíveis para receber esta mensagem. Para evitar envios duplicados para o mesmo usuário, esta mensagem foi abortada. |
| Usuário falhou na pré-verificação para a etapa de Mensagem | Esta pré-verificação é realizada antes das validações de entrega. Quando isso ocorre, o usuário não atendeu à pré-verificação básica para esta etapa de Mensagem (usuário não encontrado ou inelegível para o canal da etapa de Mensagem). **Nota:** Para uma etapa de Mensagem multicanal, isso significa que o usuário não foi encontrado; a elegibilidade do canal é verificada aqui apenas para etapas de Mensagem de canal único. |
| Usuário falhou na pré-verificação para mensagem disparada | Para uma mensagem disparada, a Braze realiza um conjunto inicial de pré-verificações básicas para elegibilidade do público, re-elegibilidade e elegibilidade do canal antes de criar uma mensagem para enviar a partir deste disparador. |
| Usuário não mais elegível | O usuário estava inicialmente no público-alvo, mas não corresponde mais aos critérios do público antes que o Braze enviasse a mensagem ou inserisse o usuário no canva. O tempo entre o usuário inicialmente atender aos critérios do público e sair do público pode ser devido a atrasos de: {::nomarkdown}<ul><li>Intelligent Timing</li><li>Horário de silêncio</li><li>Fuso local</li><li>Limites de taxa de velocidade de entrega (não aplicável para entrada no canva)</li><li>Atrasos no pipeline de envio de mensagens</li></ul>{:/} |
| Usuário não elegível para a etapa | O usuário saiu do canva porque não atendeu às [validações de entrega]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/#delivery-validations) definidas para a etapa da mensagem ou porque fazia parte de uma [lista de supressão]({{site.baseurl}}/user_guide/engagement_tools/segments/suppression_lists). |
| Usuário não re-elegível | O usuário estava elegível para receber a mensagem ou entrar no canva, mas o envio foi cancelado devido a configurações de re-elegibilidade ou reentrada. Isso pode acontecer se o usuário já recebeu a campanha ou entrou no canva muito recentemente, se outro envio para a mesma campanha já estiver em andamento para este usuário, ou se a re-elegibilidade ou reentrada estiver desativada. |
| Perfil do usuário não encontrado | O usuário nunca existiu ou não existe mais no Braze. Alguns casos comuns incluem: {::nomarkdown}<ul><li> O usuário foi segmentado usando envio de mensagens por API, mas nunca existiu no Braze. </li><li>O usuário foi excluído antes que a mensagem fosse enviada ou a etapa do canva fosse executada. </li><li>O usuário foi mesclado com outro perfil antes que a mensagem fosse enviada.</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Canal e entrega

| Resultado de aborto | Explicação |
| ---- | ---- |
| Tempo limite de entrega do parceiro | O Braze tentou enviar esta mensagem para seu parceiro de entrega por 24 horas, mas o parceiro retornou erros temporários durante toda a janela. |
| Credenciais de push inválidas | As [credenciais de push]({{site.baseurl}}/user_guide/message_building_by_channel/push/troubleshooting/#valid-push-token) para este app estão ausentes ou inválidas, portanto o envio foi cancelado. Atualize suas credenciais em **Configurações do App**. |
| Usuário não habilitado para push Android, app ou dispositivo | Push não pode ser enviado para este usuário. Algumas razões comuns: {::nomarkdown}<ul><li> O usuário não tem o app instalado.</li> <li> O usuário não possui um token de push válido. </li> <li>O usuário não tem o dispositivo necessário para esta notificação por push. </li> <li> O usuário desativou as notificações para este app nas configurações do dispositivo. </li> <li> O usuário não está inscrito ou optou por não receber notificações por push.</li></ul>{:/} |
| Usuário não habilitado para push iOS, app ou dispositivo | Mesma situação que Usuário não habilitado para push Android, app ou dispositivo (veja acima). |
| Usuário não habilitado para push Kindle, app ou dispositivo | Mesma situação que Usuário não habilitado para push Android, app ou dispositivo (veja acima). |
| Usuário não habilitado para push web, app ou dispositivo | Mesma situação que Usuário não habilitado para push Android, app ou dispositivo (veja acima). |
| Usuário não habilitado para Cartões de Conteúdo | O usuário não usou nenhum app que inclua este Cartão de Conteúdo. |
| Usuário não habilitado para e-mail | E-mails não podem ser enviados para este usuário. Algumas razões comuns: {::nomarkdown}<ul><li> O usuário não possui um endereço de e-mail em seu perfil. </li><li> O estado de inscrição do usuário o exclui de receber este e-mail. </li><li> O endereço de e-mail do usuário foi marcado como inválido anteriormente (hard bounce). </li><li> As mensagens enviadas para este endereço de e-mail são consistentemente marcadas como spam, então o envio foi cancelado.</li></ul>{:/} |
| Usuário não habilitado para LINE | Mensagens do LINE não podem ser enviadas para este usuário. Algumas razões comuns: {::nomarkdown}<ul><li> O usuário não possui um número de telefone em seu perfil. </li><li> O número de telefone do usuário foi marcado como inválido devido a falhas de entrega. </li><li> O estado de inscrição do usuário o exclui de receber esta mensagem. </li><li> O usuário não possui um ID do LINE.</li></ul>{:/} |
| Usuário não habilitado para SMS/MMS/RCS | Mensagens SMS não podem ser enviadas para este usuário. Algumas razões comuns: {::nomarkdown}<ul><li> O usuário não possui um número de telefone em seu perfil. </li><li> O número de telefone do usuário foi marcado como inválido devido a falhas de entrega. </li><li> O número de telefone do usuário não está no formato E.164 válido, e as tentativas de formatar o número automaticamente falharam. </li><li> O estado de inscrição do usuário o exclui de receber a mensagem SMS.</li><li>O número de telefone do usuário está em um país bloqueado.</li></ul>{:/} |
| Usuário não habilitado para WhatsApp | Mensagens do WhatsApp não podem ser enviadas para este usuário. Algumas razões comuns: {::nomarkdown}<ul><li> O usuário não possui um número de telefone em seu perfil. </li><li> O número de telefone do usuário foi marcado como inválido devido a falhas de entrega. </li><li> O estado de inscrição do usuário o exclui de receber esta mensagem. </li><li> O usuário não possui uma conta do WhatsApp.</li></ul>{:/} |
| Falha no webhook | O webhook recebeu um código de resposta não bem-sucedido (não `2xx`). Veja o [Registro de Atividade de Mensagens]({{site.baseurl}}/user_guide/administrative/app_settings/message_activity_log_tab#dev-console-troubleshooting) para mais detalhes. Logs que têm mais de 60 horas são limpos e não estão mais acessíveis; erros de webhook são amostrados até 20 logs por hora. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Perguntas frequentes

### O que significa uma falha de "pré-verificação"?

Uma "pré-verificação" refere-se a uma verificação de validação em alta velocidade e agrupada que é executada no início de uma etapa do pipeline (como uma mensagem sendo acionada ou o envio de uma etapa de mensagem do Canvas). Pense nisso como uma saída antecipada projetada para máxima velocidade. Em vez de executar muitas verificações separadas e que consomem muitos recursos (como validar cada detalhe do perfil de um usuário), a Braze agrupa várias validações básicas em uma "primeira passada".

Se um usuário falhar nesta única verificação agrupada, ele é descartado imediatamente. Essa abordagem agrupada permite que a Braze processe volumes massivos de mensagens em alta velocidade e pode contribuir para um desempenho mais rápido e estável para suas campanhas e Canvases, reduzindo a latência de processamento para cada mensagem.

### Por que a soma de _Total Aborts_ e _Message Sends_ é menor do que o tamanho esperado do público?

Isso pode acontecer por várias razões:

- **Critérios de público:** Menos usuários do que o esperado podem ter atendido aos critérios de público (por exemplo, eles não estavam no segmento ou não tinham os atributos necessários) quando a campanha ou Canvas foi lançada.
- **Processamento em andamento:** As mensagens ainda podem estar sendo processadas ativamente. Os usuários ainda podem estar em etapas anteriores do Canvas e não ter chegado a nenhuma etapa de Mensagem.
- **Atualização de dados:** Os dados do painel são atualizados aproximadamente a cada 15 minutos, mas isso não é uma garantia. Os dados mais recentes para esta campanha ou Canvas podem não ter chegado ao painel ainda.
- **Casos extremos:** Há uma pequena chance de você estar enfrentando um caso extremo que não está capturado neste painel neste momento. Se você suspeitar que este é o caso, entre em contato com [suporte da Braze]({{site.baseurl}}/user_guide/administrative/access_braze/support).

### Por que a soma de _Total Aborts_ e _Message Sends_ é maior do que o público para uma campanha e Canvas?

Isso pode ocorrer pelos seguintes motivos:

- **Mensagens multicanal:** A campanha ou etapa do Canva foi configurada para enviar em múltiplos canais (como SMS e e-mail). Um único usuário pode receber um resultado de "enviado" para um canal (como e-mail) e um resultado de "abortar" para outro (como "Usuário não habilitado para SMS/MMS/RCS"). Nesse caso, esse único usuário seria contado duas vezes no gráfico: uma vez como "enviado" e outra como "abortar."
  - **Exemplo:** Você envia uma campanha push para 100 usuários, direcionando tanto para iOS quanto para Android. Se um usuário tiver apenas um dispositivo iOS, ele recebe o push do iOS ("enviado"), mas também dispara um abortar para o push do Android ("Usuário não habilitado para push do Android, app ou dispositivo").
- **Várias etapas de Mensagem (apenas Canva):** Seu Canva pode ter mais de uma etapa de mensagem em um determinado caminho. Este dashboard agrega todos os resultados, então um único usuário pode ser contado várias vezes se passar por várias etapas de mensagem dentro do intervalo de tempo selecionado.
- **Mensagens de teste:** O envio de teste (que é contado no dashboard) está fazendo com que as contagens totais sejam maiores do que o tamanho do público. 

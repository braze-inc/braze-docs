---
nav_title: Perguntas frequentes
article_title: Perguntas frequentes sobre e-mail
page_order: 15
description: "Esta página fornece respostas a perguntas frequentes sobre envio de mensagens por e-mail."
channel: email

---

# Perguntas frequentes

> Este artigo fornece respostas a algumas perguntas frequentes sobre e-mails.

### O que acontece quando um e-mail é enviado e vários perfis têm o mesmo endereço de e-mail?

Se vários usuários com e-mails correspondentes estiverem em um segmento para receber uma campanha, um perfil de usuário aleatório com esse endereço de e-mail será escolhido no momento do envio. Dessa forma, o e-mail é enviado apenas uma vez e é deduplicado, garantindo que o e-mail não chegue ao mesmo endereço várias vezes.

Note que essa deduplicação ocorre quando os usuários direcionados estão incluídos no mesmo envio. As campanhas disparadas podem resultar em vários envios para o mesmo endereço de e-mail (mesmo dentro de um período em que os usuários poderiam ser excluídos devido à reelegibilidade) se diferentes usuários com endereços de e-mail correspondentes registrarem o evento de gatilho em momentos diferentes. Os usuários não são deduplicados por e-mail na entrada do Canvas, portanto, é possível que não sejam deduplicados além da primeira etapa de um Canvas se estiverem progredindo em momentos ligeiramente diferentes devido ao limite de frequência de entrada. Quando um usuário vinculado a um determinado endereço de e-mail abre ou clica em um e-mail, todos os perfis de usuário que compartilham esse endereço de e-mail são marcados como tendo aberto ou clicado na campanha.

#### Exceção: campanhas disparadas por API

As campanhas disparadas por API desduplicarão ou enviarão duplicatas, dependendo de onde o público estiver definido. E-mails duplicados devem ser direcionados separadamente na chamada da API usando `user_ids` distintos para receber vários detalhes. Aqui estão três cenários possíveis para campanhas disparadas por API:

- **Cenário 1: E-mails duplicados no segmento de destino:** Se o mesmo e-mail aparecer em vários perfis de usuário agrupados nos filtros de público do dashboard para uma campanha disparada por API, apenas um dos perfis receberá o e-mail.
- **Cenário 2: E-mails duplicados em diferentes `user_ids` dentro do objeto de destinatários:** Se o mesmo e-mail aparecer em múltiplos valores de `external_user_id` referenciados pelo objeto `recipients`, o e-mail será enviado duas vezes.
- **Cenário 3: E-mails duplicados devido a `user_ids` duplicados dentro do objeto de destinatários:** Se você tentar adicionar o mesmo perfil de usuário duas vezes, apenas um dos perfis receberá o e-mail.

### As atualizações das minhas configurações de envio de e-mail serão aplicadas retroativamente?

Não. As atualizações feitas nas configurações de e-mail de saída não afetam retroativamente os envios existentes. Por exemplo, a alteração do seu nome de exibição padrão nas configurações de e-mail não substituirá automaticamente o nome de exibição padrão existente em suas campanhas ativas ou canvas. 

### O que é uma "boa" taxa de entrega de e-mail?

Normalmente, o "número mágico" é cerca de 98% das mensagens entregues com uma taxa de bounce não superior a 3%. Se sua entrega cair abaixo disso, geralmente há motivo para preocupação.

No entanto, uma taxa acima de 98% ainda pode ter problemas de entregabilidade. Por exemplo, se todos os seus bounces forem provenientes de um único domínio, isso é um sinal claro de que há um problema de reputação com esse provedor.

Além disso, as mensagens podem estar sendo entregues e acabando em Spam, o que indica problemas de reputação potencialmente sérios. É importante monitorar não apenas o número de mensagens entregues, mas também as taxas de abertura e de cliques para determinar se os usuários estão realmente vendo as mensagens em suas caixas de entrada. Como os provedores geralmente não relatam todas as instâncias de spam, uma taxa de spam de até 1% pode ser motivo de preocupação e de análise adicional.

Por fim, sua empresa e os tipos de e-mail que você envia também podem afetar a entrega. Por exemplo, alguém que envia principalmente [e-mails de transação]({{site.baseurl}}/api/api_campaigns/transactional_api_campaign) deve esperar ver uma taxa melhor do que alguém que envia muitas mensagens de marketing.

### Por que minhas métricas de entrega de e-mail não estão chegando a 100%?

As métricas de entrega de e-mail (entregas, bounces e taxa de spam) podem não somar 100% devido aos e-mails que sofrem soft bounce e não são entregues após o período de nova tentativa de até 72 horas.

Soft bounces são e-mails que são devolvidos devido a um problema temporário ou transitório, como "caixa de correio cheia", "servidor temporariamente indisponível" e outros. Se um e-mail com soft bounce ainda não tiver sido entregue após 72 horas, esse e-mail não será contabilizado nas métricas de entrega da campanha.

### O que são pixels de rastreamento de abertura?

[Os pixels de rastreamento de abertura]({{site.baseurl}}/user_guide/administrative/app_settings/email_settings/#changing-location-of-tracking-pixel) aproveitam o domínio de rastreamento de cliques de e-mail de um remetente para rastrear eventos de abertura de e-mail. O pixel é uma tag de imagem anexada ao HTML do e-mail. É mais comumente o último elemento HTML dentro da tag body. Quando um usuário carrega seu e-mail, é feita uma solicitação para preencher a imagem do domínio de rastreamento da marca, que registra um evento de abertura.

### O que acontece quando uma campanha de e-mail ou um Canvas é interrompido?

Os usuários serão impedidos de entrar no Canvas e nenhuma outra mensagem será enviada. Para campanhas de e-mail e canvas, o botão Parar não significa que o envio será interrompido imediatamente. Isso ocorre porque, quando as solicitações de envio são enviadas, elas não podem ser impedidas de serem entregues ao usuário.

### Por que estou vendo mais cliques em e-mails do que aberturas?

Você pode estar vendo mais cliques do que aberturas por qualquer um dos seguintes motivos:
- Os usuários estão realizando vários cliques no corpo do e-mail em uma única abertura.
- Os usuários clicam em alguns links de e-mail no painel de prévia de seus telefones. Nesse caso, a Braze registra esse e-mail como tendo sido clicado, mas não aberto.
- Os usuários reabrem um e-mail cuja prévia já foi feita anteriormente.

### Por que estou vendo zero aberturas e cliques de e-mail?

Você pode estar vendo zero aberturas ou cliques de e-mail se houver uma configuração incorreta no seu domínio de rastreamento. Isso pode ser devido a qualquer uma das seguintes razões:
- Há um problema de SSL em que as URLs de rastreamento estão como `http` em vez de `https`.
- Há um problema com seu CDN em que a string do agente do usuário nos eventos de abertura, eventos de clique, ou ambos não está sendo preenchida.

### Quais são os possíveis riscos de disparar cliques no servidor?

Certos elementos de uma mensagem de e-mail, como mensagens muito longas ou muitos pontos de exclamação, podem disparar respostas de segurança de e-mail. Essas respostas podem afetar os relatórios, a reputação do IP e levar os usuários a cancelar inscrição.

Para obter práticas recomendadas sobre como lidar com essas respostas, consulte [Como lidar com aumentos nas taxas de cliques]({{site.baseurl}}/help/help_articles/email/open_rates/).

### A Braze pode rastrear links de cancelamento de inscrição contados para a métrica "Cancelamento de inscrição"?

A Braze rastreia links de cancelamento de inscrição se o seguinte Liquid for usado nos e-mails: {%raw%}`${set_user_to_unsubscribed_url}`{%endraw%}

### Posso adicionar um link "visualizar este e-mail em um navegador" aos meus e-mails?

Não, a Braze não oferece essa funcionalidade. Isso ocorre porque a maioria crescente dos e-mails é aberta em dispositivos móveis e clientes de e-mail modernos, que renderizam imagens e conteúdo sem problemas.

**Solução alternativa:** Para obter esse mesmo resultado, você pode hospedar o conteúdo do e-mail em uma landing page externa (como seu site), que pode ser vinculada à campanha de e-mail que você está criando usando a ferramenta **Link** ao editar o corpo do e-mail.

### Por que meus usuários estão sendo cancelados automaticamente por software de segurança de e-mail?

Algumas ferramentas de segurança de e-mail corporativas (como Barracuda, Proofpoint e serviços similares) pré-buscam ou escaneiam todas as URLs em e-mails recebidos, incluindo links de cancelamento de inscrição. Isso pode causar cancelamentos de inscrição não intencionais quando a ferramenta de segurança segue o link de cancelamento de inscrição de um clique.

Para mitigar isso:

- **Recomende que os destinatários coloquem seu domínio de envio na lista de permissões:** Trabalhe com as equipes de TI dos destinatários afetados para adicionar seu domínio de envio e os domínios de rastreamento da Braze à lista de permissões de segurança de e-mail deles.
- **Use uma Central de Preferências:** Em vez de um link direto de cancelamento de inscrição, use uma [Central de Preferências]({{site.baseurl}}/user_guide/message_building_by_channel/email/preference_center/overview/) que exija interação do usuário para confirmar a ação de cancelamento de inscrição. Scanners de segurança normalmente não completam formulários de múltiplas etapas.
- **Revise os registros de cancelamento de inscrição:** Verifique o cabeçalho `User-Agent` e o endereço IP nos dados do evento de cancelamento de inscrição do Currents para identificar padrões consistentes com escaneamento automatizado (como cabeçalhos `User-Agent` consistentes em múltiplos cancelamentos de inscrição).

Para mais detalhes sobre como o escaneamento do lado do servidor pode afetar as métricas de e-mail, consulte [Como lidar com aumentos nas taxas de cliques]({{site.baseurl}}/user_guide/message_building_by_channel/email/reporting_and_analytics/email_reporting/#handling-increases-in-click-rates).

### Por que minha taxa de abertura de máquina mudou inesperadamente?

[Aberturas de máquina]({{site.baseurl}}/user_guide/analytics/reporting/report_metrics/#machine-opens) são acionadas por recursos de segurança de e-mail, como a proteção de privacidade de e-mail da Apple (MPP), que pré-carrega o conteúdo do e-mail (incluindo o pixel de rastreamento) sem que o usuário abra fisicamente o e-mail. As taxas de abertura de máquina podem flutuar com base em:

- Mudanças na proporção do seu público usando o Apple Mail ou outros clientes de e-mail com recursos de privacidade.
- Atualizações nas funcionalidades de privacidade do provedor de e-mail ou comportamentos de detecção de bots.
- Mudanças na segmentação ou direcionamento do seu público.

As porcentagens de abertura de máquina não são uma medida confiável de engajamento real. Para uma visão mais precisa da performance do e-mail, concentre-se em *Outras Aberturas* (aberturas não-máquina) e *Cliques Únicos*. Você também pode comparar essas métricas ao longo do tempo usando o [Dashboard de Performance de E-mail]({{site.baseurl}}/user_guide/analytics/dashboard/email_performance_dashboard/).

### A métrica *Aberturas Únicas* inclui *Aberturas de Máquina*?

Sim. *Aberturas Únicas* inclui *Aberturas de Máquina*. Na página **Análise de dados da campanha** e no **Construtor de Relatórios**, você pode visualizar ambas as métricas.
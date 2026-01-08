---
nav_title: PERGUNTAS FREQUENTES
article_title: Perguntas frequentes sobre e-mail
page_order: 14
description: "Esta página fornece respostas a perguntas frequentes sobre mensagens de e-mail."
channel: email

---

# Perguntas frequentes

> Este artigo fornece respostas a algumas perguntas frequentes sobre e-mails.

### O que acontece quando um e-mail é enviado e vários perfis têm o mesmo endereço de e-mail?

Se vários usuários com e-mails correspondentes estiverem todos em um segmento para receber uma campanha, um perfil de usuário aleatório com esse endereço de e-mail será escolhido no momento do envio. Dessa forma, o e-mail é enviado apenas uma vez e é deduplicado, garantindo que o e-mail não chegue ao mesmo endereço de e-mail várias vezes.

Observe que essa deduplicação ocorre se os usuários visados estiverem incluídos no mesmo despacho. As campanhas acionadas podem resultar em vários envios para o mesmo endereço de e-mail (mesmo dentro de um período de tempo em que os usuários poderiam ser excluídos devido à reelegibilidade) se diferentes usuários com endereços de e-mail correspondentes registrarem o evento de acionamento em momentos diferentes. Os usuários não são deduzidos por e-mail na entrada do Canvas, portanto, é possível que os usuários não sejam deduzidos além da primeira etapa de um Canvas se estiverem progredindo em momentos ligeiramente diferentes devido à taxa de entrada limitada. Quando um usuário vinculado a um determinado endereço de e-mail abre ou clica em um e-mail, todos os perfis de usuário que compartilham o endereço de e-mail são marcados como tendo aberto e clicado na campanha.

#### Exceção: Campanhas acionadas por API

As campanhas acionadas pela API desduplicarão ou enviarão desduplicações, dependendo de onde o público-alvo estiver definido. Em resumo, os e-mails duplicados devem ser direcionados diretamente como `user_ids` separados na chamada de API para receber vários detalhes. Aqui estão três cenários possíveis para campanhas acionadas por API:

- **Cenário 1: E-mails duplicados no segmento-alvo:** Se o mesmo e-mail aparecer em vários perfis de usuário agrupados nos filtros de público-alvo do painel para uma campanha acionada por API, apenas um dos perfis receberá o e-mail.
- **Cenário 2: E-mails duplicados em diferentes `user_ids` dentro do objeto de destinatários:** Se o mesmo e-mail aparecer em vários `External_user_IDs` referenciados pelo objeto `recipients``, o e-mail será enviado duas vezes.
- **Cenário 3: E-mails duplicados devido à duplicação de user_ids no objeto de destinatários:** Se você tentar adicionar o mesmo perfil de usuário duas vezes, apenas um dos perfis receberá o e-mail.

### As atualizações das minhas configurações de e-mail de saída serão aplicadas retroativamente?

Não. As atualizações feitas nas configurações de e-mail de saída não afetam retroativamente os envios existentes. Por exemplo, alterar seu nome de exibição padrão nas configurações de e-mail não substituirá automaticamente o nome de exibição padrão existente em suas campanhas ativas ou Canvases. 

### O que é uma "boa" taxa de entrega de e-mail?

Normalmente, o "número mágico" é cerca de 98% das mensagens entregues com uma taxa de rejeição não superior a 3%. Se sua entrega cair abaixo disso, geralmente há motivo para preocupação.

No entanto, uma taxa pode ser superior a 98% e ainda assim ter problemas de capacidade de entrega. Por exemplo, se todas as devoluções forem provenientes de um domínio específico, isso é um sinal claro de que há um problema de reputação com esse provedor.

Além disso, as mensagens podem estar sendo entregues e acabando em Spam, o que indica problemas de reputação potencialmente graves. É importante monitorar não apenas o número de mensagens entregues, mas também as taxas de abertura e de cliques para determinar se os usuários estão realmente vendo as mensagens em suas caixas de entrada. Como os provedores geralmente não relatam todas as instâncias de spam, uma taxa de spam de até 1% pode ser motivo de preocupação e de análise adicional.

Por fim, sua empresa e os tipos de e-mails que você envia também podem afetar a entrega. Por exemplo, alguém que envia principalmente [e-mails transacionais]({{site.baseurl}}/api/api_campaigns/transactional_api_campaign) deve esperar ver uma taxa melhor do que alguém que envia muitas mensagens de marketing.

### Por que minhas métricas de entrega de e-mail não estão chegando a 100%?

As métricas de entrega de e-mail (entregas, rejeições e taxa de spam) podem não somar 100% devido aos e-mails que sofrem rejeição suave e não são entregues após o período de nova tentativa de até 72 horas.

Soft bounces são e-mails que são devolvidos devido a um problema temporário ou transitório, como "caixa de correio cheia", "servidor temporariamente indisponível" e outros. Se um e-mail com soft bounce ainda não tiver sido entregue após 72 horas, esse e-mail não será contabilizado nas métricas de entrega da campanha.

### O que são pixels de rastreamento abertos?

[Os pixels de rastreamento]({{site.baseurl}}/user_guide/administrative/app_settings/email_settings/#changing-location-of-tracking-pixel) de abertura aproveitam o domínio de rastreamento de cliques de e-mail de um remetente para rastrear eventos de abertura de e-mail. O pixel é uma tag de imagem anexada ao HTML do e-mail. Geralmente, é o último elemento HTML dentro da tag body. Quando um usuário carrega seu e-mail, é feita uma solicitação para preencher a imagem do domínio de rastreamento de marca, que registra um evento de abertura.

### O que acontece quando uma campanha de e-mail ou Canvas é interrompida?

Os usuários serão impedidos de entrar no Canvas e nenhuma outra mensagem será enviada. Para campanhas de e-mail e Canvases, o botão de parada não significa que o envio será interrompido imediatamente. Isso ocorre porque, quando as solicitações de envio são enviadas, elas não podem ser impedidas de serem entregues ao usuário.

### Por que estou vendo mais cliques em e-mails do que aberturas?

Você pode estar vendo mais cliques do que aberturas por qualquer um dos seguintes motivos:
- Os usuários estão realizando vários cliques no corpo do e-mail em uma única abertura.
- Os usuários clicam em alguns links de e-mail no painel de visualização de seus telefones. Nesse caso, o Braze registra esse e-mail como tendo sido clicado, mas não aberto.
- Os usuários reabrem um e-mail que visualizaram anteriormente.

### Por que não estou vendo nenhuma abertura e nenhum clique nos e-mails?

Você pode estar vendo zero aberturas e cliques de e-mail se houver uma configuração incorreta do seu domínio de rastreamento. Isso pode ser devido a qualquer um dos seguintes motivos:
- Há um problema de SSL em que os URLs de rastreamento são `http` em vez de `https`.
- Há um problema com a CDN em que a string do agente do usuário nos eventos de abertura, nos eventos de clique ou em ambos não está sendo preenchida.

### Quais são os possíveis riscos de acionar cliques no servidor?

Certos elementos de uma mensagem de e-mail, como mensagens muito longas ou muitos pontos de exclamação, têm o potencial de acionar respostas de segurança de e-mail. Essas respostas podem afetar os relatórios, a reputação do IP e podem resultar no cancelamento da assinatura dos usuários. 

Para obter as práticas recomendadas sobre como lidar com essas respostas, consulte [Como lidar com aumentos nas taxas de cliques]({{site.baseurl}}/help/help_articles/email/open_rates/).

### O Braze pode rastrear links de cancelamento de assinatura contados para a métrica "Cancelamento de assinatura"?

A Braze rastreia os links de cancelamento de assinatura se o seguinte Liquid for usado nos e-mails: {%raw%}`${set_user_to_unsubscribed_url}`{%endraw%}

### Posso adicionar um link "visualizar este e-mail em um navegador" aos meus e-mails?

Não, o Braze não oferece essa funcionalidade. Isso ocorre porque a maioria crescente dos e-mails é aberta em dispositivos móveis e clientes de e-mail modernos, que renderizam imagens e conteúdo sem problemas.

**Solução alternativa:** Para obter esse mesmo resultado, você pode hospedar o conteúdo do seu e-mail em uma página de destino externa (como o seu site), que pode ser vinculada à campanha de e-mail que você está criando usando a ferramenta **Link** ao editar o corpo do e-mail.


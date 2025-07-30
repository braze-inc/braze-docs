---
nav_title: Perguntas frequentes
article_title: Perguntas frequentes sobre e-mail
page_order: 14
description: "Esta página fornece respostas a perguntas frequentes sobre envio de mensagens por e-mail."
channel: email

---

# Perguntas frequentes

> Este artigo fornece respostas a algumas perguntas frequentes sobre e-mails.

### O que acontece quando um e-mail é enviado e vários perfis têm o mesmo endereço de e-mail?

Se vários usuários com e-mails correspondentes estiverem todos em um segmento para receber uma campanha, um perfil de usuário aleatório com esse endereço de e-mail será escolhido no momento do envio. Dessa forma, o e-mail é enviado apenas uma vez e é deduplicado, garantindo que o e-mail não chegue ao mesmo endereço eletrônico várias vezes.

Note que essa deduplicação ocorre se os usuários direcionados estiverem incluídos no mesmo envio. As campanhas disparadas podem resultar em vários envios para o mesmo endereço de e-mail (mesmo dentro de um período de tempo em que os usuários poderiam ser excluídos devido à reelegibilidade) se diferentes usuários com endereços de e-mail correspondentes registrarem o evento de gatilho em momentos diferentes. Os usuários não são deduzidos por e-mail na entrada do Canvas, portanto, é possível que os usuários não sejam deduzidos além da primeira etapa do Canva se estiverem progredindo em momentos ligeiramente diferentes devido ao limite de frequência de entrada. Quando um usuário vinculado a um determinado endereço de e-mail abre ou clica em um e-mail, todos os perfis de usuário que compartilham o endereço de e-mail são marcados como tendo aberto e clicado na campanha.

#### Exceção: Campanhas disparadas por API

As campanhas disparadas pela API desduplicarão ou enviarão desduplicações, dependendo de onde o público estiver definido. Em resumo, os e-mails duplicados devem ser direcionados diretamente como `user_ids` separados na chamada da API para receber vários detalhes. Aqui estão três cenários possíveis para campanhas disparadas por API:

- **Cenário 1: E-mails duplicados no segmento de destino:** Se o mesmo e-mail aparecer em vários perfis de usuário agrupados nos filtros de público do dashboard para uma campanha disparada por API, apenas um dos perfis receberá o e-mail.
- **Cenário 2: Envio de e-mails duplicados em diferentes `user_ids` dentro do objeto de destinatários:** Se o mesmo e-mail aparecer em vários `External_user_IDs` referenciados pelo objeto `recipients``, o e-mail será enviado duas vezes.
- **Cenário 3: Envio de e-mails duplicados devido a user_ids duplicados no objeto de destinatários:** Se você tentar adicionar o mesmo perfil de usuário duas vezes, apenas um dos perfis receberá o e-mail.

### Como posso verificar se um endereço de e-mail já está associado a um usuário?

Antes de criar um usuário por meio da API ou do SDK, chame o ponto de extremidade [`/users/export/ids`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/) e especifique o endereço do usuário `email_address`. Se retornar um perfil de usuário, esse usuário do Braze já está associado a esse endereço de e-mail.

Recomendamos enfaticamente que procure endereços de e-mail exclusivos quando novos usuários forem criados e evite enviar ou importar usuários com o mesmo endereço de e-mail. Caso contrário, você poderá ter consequências não intencionais que afetarão o envio de mensagens, o direcionamento, os relatórios e outros recursos.

Por exemplo, digamos que você tenha perfis duplicados, mas determinados atributos personalizados ou eventos residam em apenas um perfil. Quando você tenta disparar campanhas ou Canvas com vários critérios, o Braze não consegue identificar o usuário como elegível porque há dois perfis de usuário. Ou, se uma campanha direcionar um endereço de e-mail compartilhado por dois usuários, a página **Pesquisar usuários** mostrará ambos os perfis de usuário como tendo recebido a campanha.

### As atualizações das minhas configurações de envio de e-mail serão aplicadas retroativamente?

Não. As atualizações feitas nas configurações de e-mail de saída não afetam retroativamente os envios existentes. Por exemplo, a alteração de seu nome de exibição padrão nas configurações de e-mail não substituirá automaticamente o nome de exibição padrão existente em suas campanhas ativas ou Canvas. 

### O que é uma "boa" taxa de entrega de e-mail?

Normalmente, o "número mágico" é cerca de 98% das mensagens entregues com uma taxa de bounce não superior a 3%. Se sua entrega cair abaixo disso, geralmente há motivo para preocupação.

No entanto, uma taxa pode ser superior a 98% e ainda assim ter problemas de entregabilidade. Por exemplo, se todos os seus bounces forem provenientes de um determinado domínio, isso é um sinal claro de que há um problema de reputação com esse provedor.

Além disso, as mensagens podem estar sendo enviadas e acabando em Spam, o que indica problemas de reputação potencialmente sérios. É importante monitorar não apenas o número de mensagens enviadas, mas também as taxas de abertura e de cliques para determinar se os usuários estão realmente vendo as mensagens em suas caixas de entrada. Como os provedores geralmente não relatam todas as instâncias de spam, uma taxa de spam de até 1% pode ser motivo de preocupação e de análise adicional.

Por fim, sua empresa e os tipos de e-mail que você envia também podem afetar a entrega. Por exemplo, alguém que envia principalmente [e-mails de transação]({{site.baseurl}}/api/api_campaigns/transactional_api_campaign) deve esperar ver uma taxa melhor do que alguém que envia muitas mensagens de marketing.

### Por que minhas métricas de envio de e-mail não estão chegando a 100%?

As métricas de entrega de e-mail (entregas, bounces e taxa de spam) podem não somar 100% devido aos e-mails que são soft bounce e não são entregues após o período de nova tentativa de até 72 horas.

Soft bounces são e-mails que são devolvidos devido a um problema temporário ou transitório, como "caixa de correio cheia", "servidor temporariamente indisponível" e outros. Se um e-mail com soft bounce ainda não tiver sido entregue após 72 horas, esse e-mail não será contabilizado nas métricas de entrega da campanha.

### O que são pixels de rastreamento de abertura?

[Os pixels de rastreamento de abertura]({{site.baseurl}}/user_guide/administrative/app_settings/email_settings/#changing-location-of-tracking-pixel) aproveitam o domínio de rastreamento de cliques de e-mail de um remetente para rastrear eventos de abertura de e-mail. O pixel é uma tag de imagem anexada ao HTML do e-mail. É mais comumente o último elemento HTML dentro da tag body. Quando um usuário envia seu e-mail, é feita uma solicitação para preencher a imagem do domínio de rastreamento da marca, que registra um evento de abertura.

### O que acontece quando uma campanha de e-mail ou o Canva é interrompido?

Os usuários serão impedidos de entrar no Canva e nenhuma outra mensagem será enviada. Para campanhas de e-mail e canvas, o botão Parar não significa que o envio será interrompido imediatamente. Isso ocorre porque, quando as solicitações de envio são enviadas, elas não podem ser impedidas de serem entregues ao usuário.

### Por que estou vendo mais cliques em e-mails do que aberturas?

Você pode estar vendo mais cliques do que aberturas por qualquer um dos seguintes motivos:
- Os usuários estão realizando vários cliques no corpo do e-mail em uma única abertura.
- Os usuários clicam em alguns links de e-mail no painel de visualização de seus telefones. Nesse caso, a Braze registra esse e-mail como tendo sido clicado, mas não aberto.
- Os usuários reabrem um e-mail cuja prévia foi feita.

### Por que estou vendo zero aberturas e cliques em e-mails?

Você pode estar vendo zero aberturas e cliques de e-mail se houver uma configuração incorreta com seu domínio de rastreamento. Isso pode ser devido a qualquer um dos seguintes motivos:
- Há um problema de SSL em que os URLs de rastreamento são `http` em vez de `https`.
- Há um problema com a CDN em que a string do agente do usuário nos eventos de abertura, nos eventos de clique ou em ambos não está sendo preenchida.

### Quais são os possíveis riscos de disparar cliques no servidor?

Certos elementos de uma mensagem de e-mail, como mensagens muito longas ou muitos pontos de exclamação, têm o potencial de disparar respostas de segurança de e-mail. Essas respostas podem afetar os relatórios, a reputação do IP e podem resultar no cancelamento da inscrição dos usuários. 

Para obter práticas recomendadas sobre como lidar com essas respostas, consulte [Como lidar com aumentos nas taxas de cliques]({{site.baseurl}}/help/help_articles/email/open_rates/).

### Como posso remover um endereço de e-mail da lista de bounce ou de spam?

Você pode remover e-mails devolvidos e e-mails na lista de spam com os seguintes pontos de extremidade:
- [`/email/bounce/remove`]({{site.baseurl}}/api/endpoints/email/post_remove_hard_bounces)
- [`/email/spam/remove`]({{site.baseurl}}/api/endpoints/email/post_remove_spam)

### Como posso verificar o grupo de inscrições para e-mail de um usuário?

- **Perfil do usuário:** Os perfis de usuários individuais podem ser acessados por meio do dashboard do Braze na página [Pesquisar usuários]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/#access-profiles). Aqui, é possível procurar perfis de usuários por endereço de e-mail, número de telefone ou ID de usuário externo. Em um perfil de usuário, na guia Engajamento, é possível visualizar os grupos de inscrições para e-mail de um usuário.
- **API REST:** O grupo de inscrições de perfis de usuários individuais pode ser visualizado pelo [endpoint Listar grupos de inscrições do]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_groups/) usuário ou pelo [endpoint Listar status do grupo de inscrições do usuário]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_group_status/) usando a Braze REST API. 

### Como posso atualizar o grupo de inscrições para e-mail de um usuário?

Os usuários serão impedidos de entrar no Canva e nenhuma outra mensagem será enviada. Para campanhas de e-mail e canvas, o botão Parar não significa que o envio será interrompido imediatamente. Isso ocorre porque, depois que as solicitações de envio são enviadas, elas não podem ser impedidas de serem entregues ao usuário.

### O Braze pode rastrear os links de cancelamento de inscrição contados para a métrica "Unsubscribe" (Cancelamento de inscrição)?

A Braze rastreia os links de cancelamento de inscrição se o seguinte Liquid for usado nos e-mails: {%raw%}`${set_user_to_unsubscribed_url}`{%endraw%}

### Posso adicionar um link "visualizar este e-mail em um navegador" aos meus e-mails?

Não, o Braze não oferece essa funcionalidade. Isso ocorre porque a maioria crescente dos e-mails é aberta em dispositivos móveis e clientes de e-mail modernos, que renderizam imagens e conteúdo sem problemas.

**Solução alternativa:** Para obter esse mesmo resultado, é possível hospedar o conteúdo do e-mail em uma landing page externa (como seu site), que pode ser vinculada à campanha de e-mail que você está criando usando a ferramenta **Link** ao editar o corpo do e-mail.


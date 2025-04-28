---
nav_title: Perguntas frequentes
article_title: FAQ de e-mail e modelo de link
page_order: 10

page_type: FAQ
description: "Esta página contém perguntas frequentes sobre modelos de e-mail e modelos de link."
tool:
  - Templates
channel: email

---

# Perguntas frequentes

> Esta página fornece respostas para algumas perguntas frequentes sobre modelos de e-mail e modelos de link.

## Modelos de e-mail

### Posso adicionar um link "ver este e-mail no navegador" aos meus e-mails?

Não, o Braze não oferece essa funcionalidade. Isso ocorre porque a maioria crescente dos e-mails é aberta em dispositivos móveis e clientes de e-mail modernos, que renderizam imagens e conteúdo sem problemas.

**Solução alternativa:** Para alcançar esse mesmo resultado, você pode hospedar o conteúdo do seu e-mail em uma landing page externa (como o seu site), que pode ser vinculada a partir da campanha de e-mail que você está construindo usando a ferramenta **Link** ao editar o corpo do e-mail.

### Como crio um link de cancelamento de inscrição personalizado para meus modelos de e-mail?

Há uma opção de redirecionamento para a página de cancelar inscrição.

Você pode alterar o link de cancelamento de inscrição no rodapé personalizado de {% raw %} `{{${set_user_to_unsubscribed_url}}}` {% endraw %} para um link para seu próprio site com um parâmetro de consulta que inclua o ID do usuário. Um exemplo é:
{% raw %} 
> https://www.braze.com/unsubscribe?user_id={{${user_id}}}
{% endraw %}

Em seguida, você pode chamar o [endpoint `/email/status`]({{site.baseurl}}/api/endpoints/email/post_email_subscription_status/) para atualizar o status da inscrição do usuário. Para saber mais, consulte nossa documentação sobre como [alterar o status da inscrição de e-mail]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#changing-email-subscriptions).

Para salvar esse novo link, a tag de cancelar inscrição padrão da Braze {%raw%}(``${set_user_to_unsubscribed_url}``){%endraw%} deve estar no rodapé. Isso significa que você precisará incluir o link padrão "escondendo-o" colocando a tag em um comentário ou em uma tag oculta `<div>`.

- **Tag em exemplo de comentário:** colocando tag em exemplo de comentário: `<!-- ${set_user_to_unsubscribed_url} -->`
- **Comentário no exemplo de tag `<div>` oculta:** {%raw%}`<div style="display:none;max-height:0px;overflow:hidden;">${set_user_to_unsubscribed_url}</div>`{%endraw%}

### O que acontece se eu editar um modelo de e-mail que está sendo usado em uma campanha?

As edições feitas em um modelo existente não serão refletidas em campanhas que foram criadas usando versões anteriores desse modelo. Para campanhas de API que usam um modelo no corpo da API REST, o Braze usará a versão mais recente do modelo no momento do envio.  

## Modelos de links

### Posso fazer upload de vários modelos de link para o meu e-mail?

Sim, você pode inserir quantos modelos quiser em suas mensagens de e-mail. Como uma prática recomendada, você deve testar seus e-mails para garantir que os links não excedam 2.000 caracteres, pois a maioria dos navegadores irá encurtar ou cortar os links.

### Como faço para prévia meus links com todas as tags aplicadas?

Existem várias maneiras de abrir uma prévia de seus links. Depois de aplicar o [modelo de link]({{site.baseurl}}/user_guide/message_building_by_channel/email/templates/link_template/), você pode enviar um [e-mail de teste]({{site.baseurl}}/developer_guide/sending_test_messages/) para si mesmo para visualizar todos os links. 

No painel de prévia em uma nova guia, você também pode abrir os links para visualizar os links. Você também pode passar o mouse sobre os links no painel de prévia e vê-los na parte inferior do seu navegador.

### Como funciona a modelagem de links com Liquid?

Os modelos de link são expandidos e adicionados a cada URL antes de qualquer expansão de Liquid acontecer. Se parte de seu URL for gerada usando um snippet do Liquid, recomendamos que a base do URL e o ponto de interrogação (?) sejam codificados para que os modelos de link sejam expandidos corretamente. 

Evite adicionar o ponto de interrogação (?) ao Liquid, pois isso fará com que os modelos de link adicionem primeiro um ponto de interrogação (?), e depois o processo de expansão do Liquid adicionará um segundo ponto de interrogação (?).

## Apelidamento de link

### Como a habilitação de alias de link impactará meus blocos de conteúdo e modelos de link?

Para todos os novos Blocos de Conteúdo que são criados, o aliasing de links é aplicado em todos os espaços de trabalho, pois esta é uma funcionalidade a nível de empresa. 

Os Blocos de Conteúdo existentes não serão modificados quando a criação de alias de links estiver ativada. Embora os modelos de link existentes não sejam modificados, a seção de modelo de link existente em uma mensagem será removida. Para saber mais, consulte [Alias de link em blocos de conteúdo]({{site.baseurl}}/user_guide/message_building_by_channel/email/templates/link_aliasing/#link-aliasing-in-content-blocks).

### Posso usar a lógica condicional Liquid inteiramente dentro de uma tag de âncora HTML?

Não, o alias de link da Braze não reconhecerá o código HTML corretamente. 

Quando a lógica como essa é usada em conjunto com recursos que precisam analisar o HTML (como um pré-cabeçalho ou modelagem de link), a biblioteca usada para escanear o HTML pode modificar a tag de âncora de uma maneira que impedirá que o `href` adequado seja modelado. A biblioteca então determinará que o HTML é inválido porque é agnóstica ao código Liquid. 

Em vez disso, use a lógica Liquid que contém uma tag de âncora completa em cada estágio. Isso não interferirá na análise de HTML porque a lógica inclui várias instâncias de HTML válido. Você também pode simplificar sua lógica atribuindo e, em seguida, modelando uma variável na tag de âncora apropriada.

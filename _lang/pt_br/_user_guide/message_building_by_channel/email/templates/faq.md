---
nav_title: PERGUNTAS FREQUENTES
article_title: Perguntas frequentes sobre modelos de e-mail e links
page_order: 10

page_type: FAQ
description: "Esta página aborda as perguntas frequentes sobre modelos de e-mail e modelos de links."
tool:
  - Templates
channel: email

---

# Perguntas frequentes

> Esta página fornece respostas a algumas perguntas frequentes sobre modelos de e-mail e modelos de links.

## Modelos de e-mail

### Posso adicionar um link "visualizar este e-mail em um navegador" aos meus e-mails?

Não, o Braze não oferece essa funcionalidade. Isso ocorre porque a maioria crescente dos e-mails é aberta em dispositivos móveis e clientes de e-mail modernos, que renderizam imagens e conteúdo sem problemas.

**Solução alternativa:** Para obter esse mesmo resultado, você pode hospedar o conteúdo do seu e-mail em uma página de destino externa (como o seu site), que pode ser vinculada à campanha de e-mail que você está criando usando a ferramenta **Link** ao editar o corpo do e-mail.

### Como faço para criar um link de cancelamento de assinatura personalizado para meus modelos de e-mail?

Há uma opção de redirecionamento para a página de cancelamento de assinatura.

Você pode alterar o link de cancelamento de assinatura no rodapé personalizado de {% raw %} `{{${set_user_to_unsubscribed_url}}}` {% endraw %} para um link para seu próprio site com um parâmetro de consulta que inclua o ID do usuário. Um exemplo é:
{% raw %} 
> https://www.braze.com/unsubscribe?user_id={{${user_id}}}
{% endraw %}

Em seguida, você pode chamar o [endpoint`/email/status` ]({{site.baseurl}}/api/endpoints/email/post_email_subscription_status/) para atualizar o status da assinatura do usuário. Para obter mais detalhes, consulte nossa documentação sobre [como alterar o status da assinatura de e-mail]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#changing-email-subscriptions).

Para salvar esse novo link, a tag padrão de cancelamento de inscrição do Braze {%raw%}(``${set_user_to_unsubscribed_url}``){%endraw%} deve estar no rodapé. Isso significa que você precisará incluir o link padrão "ocultando-o" ao colocar a tag em um comentário ou em uma tag `<div>` oculta.

- **Exemplo de tag em comentário:** exemplo de colocação de tag em comentário: `<!-- ${set_user_to_unsubscribed_url} -->`
- **Comentário no exemplo de tag oculta `<div>`:** {%raw%}`<div style="display:none;max-height:0px;overflow:hidden;">${set_user_to_unsubscribed_url}</div>`{%endraw%}

### O que acontece se eu editar um modelo de e-mail que está sendo usado atualmente em uma campanha?

As edições feitas em um modelo existente não serão refletidas nas campanhas que foram criadas usando versões anteriores desse modelo. Para campanhas de API que usam um modelo no corpo da API REST, o Braze usará a versão mais recente do modelo no momento do envio.  

## Modelos de links

### Posso carregar vários modelos de links em meu e-mail?

Sim, você pode inserir quantos modelos quiser em suas mensagens de e-mail. Como prática recomendada, você deve testar seus e-mails para garantir que os links não excedam 2.000 caracteres, pois a maioria dos navegadores encurta ou corta os links.

### Como faço para visualizar meus links com todas as tags aplicadas?

Há várias maneiras de visualizar seus links. Depois de aplicar o [modelo de link]({{site.baseurl}}/user_guide/message_building_by_channel/email/templates/link_template/), você pode enviar um [e-mail de teste]({{site.baseurl}}/developer_guide/in_app_messages/sending_test_messages/) para si mesmo para visualizar todos os links. 

No painel de visualização em uma nova guia, você também pode abrir os links para visualizá-los. Você também pode passar o mouse sobre os links no painel de visualização e vê-los na parte inferior do navegador.

### Como o modelo de link funciona com o Liquid?

Os modelos de link são expandidos e adicionados a cada URL antes de ocorrer qualquer expansão do Liquid. Se parte do seu URL for gerada usando um snippet do Liquid, recomendamos que a base do URL e o ponto de interrogação (?) sejam codificados para que os modelos de link sejam expandidos corretamente. 

Evite adicionar o ponto de interrogação (?) ao seu Liquid, pois isso fará com que os modelos de link adicionem primeiro um ponto de interrogação (?) e, posteriormente, o processo de expansão do Liquid adicionará um segundo ponto de interrogação (?).

## Aliasing de links

### Como a ativação do aliasing de links afetará meus Content Blocks e modelos de links?

Para todos os novos blocos de conteúdo criados, o aliasing de links é aplicado em todos os espaços de trabalho, pois esse é um recurso em nível de empresa. 

Os blocos de conteúdo existentes não serão modificados quando o aliasing de links estiver ativado. Embora os modelos de link existentes não sejam modificados, a seção de modelo de link existente em uma mensagem será removida. Para obter mais informações, consulte [Aliasing de links em blocos de conteúdo]({{site.baseurl}}/user_guide/message_building_by_channel/email/templates/link_aliasing/#link-aliasing-in-content-blocks).

### Posso usar a lógica condicional do Liquid inteiramente em uma tag de âncora HTML?

Não, o aliasing de link do Braze não reconhecerá o HTML corretamente. 

Quando uma lógica como essa é usada em conjunto com recursos que precisam analisar o HTML (como um pré-cabeçalho ou modelo de link), a biblioteca usada para examinar o HTML pode modificar a tag de âncora de forma a impedir que o `href` adequado seja modelado. A biblioteca determinará que o HTML é inválido, pois é independente do código Liquid. 

Em vez disso, use a lógica Liquid que contém uma tag de âncora completa em cada estágio. Isso não interfere na análise de HTML porque a lógica inclui várias instâncias de HTML válido. Você também pode simplificar sua lógica atribuindo e, em seguida, modelando uma variável na tag de âncora apropriada.

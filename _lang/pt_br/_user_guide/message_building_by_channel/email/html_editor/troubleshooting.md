---
nav_title: Solução de problemas
article_title: Solução de problemas
page_order: 9
description: "Este artigo de ajuda o orienta sobre como solucionar problemas com e-mails em HTML."
channel: email
---

# Solução de problemas 

## O HTML é renderizado incorretamente em e-mails de teste

Se o [e-mail de teste]({{site.baseurl}}/developer_guide/platform_wide/sending_test_messages/#sending-a-test-push-notification-or-in-app-messages-a-classmargin-fix-namepush-inapp-testa) não parecer correto, recomendamos verificar primeiro a configuração do HTML. Em seguida, você pode verificar esses problemas:
* [Conflitos de extensão](#check-conflicts)
* [Prestação de serviços de e-mail](#check-rendering)
* [CSS inlining](#switch-css-inlining)

### Conflitos de extensão

Algumas extensões de navegador podem causar problemas com nosso editor de e-mail. Um exemplo é o [Grammarly](https://chrome.google.com/webstore/detail/grammarly-for-chrome/kbfnbcaeplbcioakkpcpgfkobkghlhen?hl=en) quando usado com o Google Chrome. Se estiver usando uma dessas extensões, você deve: 
- Editar e-mails do Braze em um navegador que não tenha o Grammarly como extensão
- Entre em contato com seu gerente de conta Braze e peça para mudar seus editores de e-mail para somente HTML ou texto simples. 

A visualização de texto simples remove o editor ```WYSIWYG``` (o que você vê é o que você obtém), portanto, primeiro confirme se todos os membros da equipe estão familiarizados com HTML antes de fazer essa solicitação.

### Prestação de serviços de e-mail

Os e-mails são renderizados de forma diferente dependendo dos navegadores e clientes de e-mail, portanto, observe com quais navegadores e clientes de e-mail você está tendo problemas.

- Visualize seus e-mails usando o [Inbox Vision]({{site.baseurl}}/user_guide/message_building_by_channel/email/inbox_vision/#inbox-vision/) para ver como eles se parecem em diferentes navegadores e clientes de e-mail.
- Depois de identificar quais navegadores ou clientes de e-mail estão causando problemas, informe à sua equipe de desenvolvedores que eles precisarão modificar o HTML e fazer edições para acomodar esses navegadores ou clientes de e-mail.

### CSS inlining

Há ocasiões em que as visualizações no Inbox Vision ainda não correspondem ao que é enviado com o Braze. Isso pode ser causado pela diferença no inlining de CSS realizado pelo Braze e por outras ferramentas. Se você suspeitar que esse é o caso, desative o inlining de CSS.

Ainda precisa de ajuda? Abra um [tíquete de suporte]({{site.baseurl}}/braze_support/).

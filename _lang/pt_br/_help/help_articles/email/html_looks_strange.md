---
nav_title: Envio de e-mail de teste com renderização de HTML
article_title: Envio de e-mail de teste com renderização de HTML
page_order: 2

page_type: solution
description: "Este artigo de ajuda orienta você sobre como solucionar problemas de envio de e-mail de teste com HTML."
channel: email
---

# Solução de problemas de renderização de HTML em e-mails de teste

Se o [e-mail de teste]({{site.baseurl}}/developer_guide/platform_wide/sending_test_messages/#sending-a-test-push-notification-or-in-app-messages-a-classmargin-fix-namepush-inapp-testa) não parecer correto, recomendamos verificar primeiro a configuração do HTML. Em seguida, você pode verificar esses problemas:
* [Conflitos de extensão](#check-conflicts)
* [Envio de e-mail](#check-rendering)
* [CSS inlining](#switch-css-inlining)

### Conflitos de extensão

Algumas extensões de navegador podem causar problemas com nosso editor de e-mail. Um exemplo é o [Grammarly](https://chrome.google.com/webstore/detail/grammarly-for-chrome/kbfnbcaeplbcioakkpcpgfkobkghlhen?hl=en)) quando usado com o Google Chrome. Se estiver usando uma dessas extensões, você deve: 
- Edite os e-mails do Braze em um navegador que não tenha o Grammarly como uma extensão do navegador
- Entre em contato com o gerente da sua conta Braze e peça para mudar seus editores de e-mail para somente HTML ou texto simples. 

A visualização de texto simples remove o editor ```WYSIWYG``` (what you see is what you get), portanto, confirme primeiro se todos os membros da equipe estão familiarizados com HTML antes de fazer essa solicitação.

### Envio de e-mail

Os e-mails são renderizados de forma diferente dependendo dos navegadores e clientes de e-mail, portanto, note com quais navegadores e clientes de e-mail você está tendo problemas.

- Faça uma prévia de seus e-mails usando o [Inbox Vision]({{site.baseurl}}/user_guide/message_building_by_channel/email/inbox_vision/#inbox-vision/) para ver a aparência de seus e-mails em diferentes navegadores e clientes de e-mail.
- Depois de identificar quais navegadores ou clientes de e-mail estão causando problemas, informe à sua equipe de desenvolvedores que eles precisarão modificar o HTML e fazer edições para acomodar esses navegadores ou clientes de e-mail.

### CSS inlining

Há ocasiões em que as prévias no Inbox Vision ainda não correspondem ao que é enviado com o Braze. Isso pode ser causado pela diferença no inlining de CSS realizado pela Braze e por outras ferramentas. Se suspeitar que esse é o caso, entre em contato com o gerente de conta do Braze para solicitar que o CSS inlining seja desativado.

Ainda precisa de ajuda? Abra um [tíquete de suporte]({{site.baseurl}}/braze_support/).

_Última atualização em 21 de dezembro de 2021_


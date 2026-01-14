---
nav_title: CSS inlining
article_title: CSS Inlining
page_order: 5.1
description: "Este artigo de referência aborda como ativar o inlining de CSS e algumas práticas recomendadas."
channel:
  - email

---

# CSS inlining

> O CSS inlining é uma forma de pré-processamento de e-mail que move estilos em uma folha de estilo CSS para o corpo de um e-mail HTML. O termo "inlining" refere-se ao fato de que os estilos são aplicados "inline" a elementos HTML individuais.

Para alguns clientes de e-mail, o CSS inlining pode melhorar a forma como os e-mails são renderizados e ajudar a confirmar que seus e-mails têm a aparência esperada. Se você já tiver a maior parte do CSS incorporado ou tiver certeza de que seu HTML e CSS são compatíveis com os requisitos da maioria dos clientes de e-mail, talvez não seja necessário ativar esse recurso. Isso pode fazer com que os estilos incorporados dinamicamente entrem em conflito com os estilos embutidos existentes e pode alterar a visualização esperada e a renderização do e-mail.

## Uso de CSS inlining

Você pode controlar se o CSS embutido está ativado ou desativado em qualquer mensagem de e-mail usando a opção **Ativar CSS embutido** na guia **Informações de envio** do editor de HTML.

Caixa de seleção para gerenciar o inlining de CSS no HTML Composer.]({% image_buster /assets/img_archive/css-inline2.png %}){: style="max-width:40%;"}

### Estado padrão de inlining

Você pode definir um estado padrão ligado ou desligado globalmente em **Configurações** > **Preferências de e-mail**. Localize a configuração para **CSS Inlining**. Essa configuração determina o valor padrão desejado com o qual todas as novas mensagens de e-mail começam. Observe que a alteração dessa configuração não afetará nenhuma de suas mensagens de e-mail existentes. Você também pode substituir esse padrão a qualquer momento ao redigir mensagens de e-mail.

Opção Inline CSS em novos e-mails por padrão localizada nas configurações de e-mail.]({% image_buster /assets/img_archive/css-inline1.png %})


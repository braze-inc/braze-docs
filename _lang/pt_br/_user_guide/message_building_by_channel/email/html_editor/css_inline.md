---
nav_title: CSS inline
article_title: CSS inline
page_order: 5.1
description: "Este artigo de referência aborda como ativar o CSS inlining e algumas práticas recomendadas."
channel:
  - email

---

# CSS inlining

> O CSS inlining é uma forma de pré-processamento de e-mail que move estilos em uma folha de estilo CSS para o corpo de um e-mail HTML. O termo "inlining" refere-se ao fato de que os estilos são aplicados "inline" a elementos HTML individuais.

Para alguns clientes de e-mail, o envio de e-mail com CSS inlining pode melhorar a forma como os e-mails são renderizados e ajudar a confirmar que seus e-mails têm a aparência esperada. Se você já tem a maior parte do CSS em linha ou está confiante de que seu HTML e CSS são compatíveis com os requisitos da maioria dos clientes de e-mail, pode não ser necessário ativar esse recurso. Isso pode causar conflitos entre estilos embutidos dinamicamente e seus estilos em linha existentes e pode alterar sua prévia e renderização de e-mail esperadas.

## Uso de CSS inlining

Você pode controlar se a ativação do CSS em linha está ligada ou desligada para qualquer mensagem de e-mail usando o **Ativar CSS em linha** alternar na **Informações de Envio** guia do editor de HTML.

![Caixa de seleção para gerenciar CSS em linha no criador de HTML.]({% image_buster /assets/img_archive/css-inline2.png %}){: style="max-width:40%;"}

### Estado padrão de inlining

Você pode definir um estado padrão ligado ou desligado globalmente em **Configurações** > **Preferências de e-mail**. Localize a configuração para **CSS Inlining**. Essa configuração determina o valor padrão desejado com o qual todas as novas mensagens de e-mail começam. Observe que a alteração dessa configuração não afetará nenhuma das mensagens de e-mail existentes. Você também pode substituir esse padrão a qualquer momento durante o envio de mensagens de e-mail.

![Opção de CSS em linha em novos e-mails por padrão localizada nas configurações de e-mail.]({% image_buster /assets/img_archive/css-inline1.png %})


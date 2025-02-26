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

Para alguns clientes de e-mail, o envio de e-mail com CSS inlining pode melhorar a forma como os e-mails são renderizados e ajudar a confirmar que seus e-mails têm a aparência esperada.

## Uso de CSS inlining

É possível controlar se o CSS inlining está ativado ou desativado para qualquer mensagem de e-mail por meio de uma caixa de seleção na guia **Informações de envio** do editor de HTML.

![Caixa de seleção para gerenciar o inlining de CSS no criador do HTML.][2]{: style="max-width:80%;"}

### Estado padrão de inlining

Você pode definir um estado padrão ligado ou desligado globalmente em **Configurações** > **Preferências de e-mail**. Localize a configuração para **CSS Inlining**. Essa configuração determina o valor padrão desejado com o qual todas as novas mensagens de e-mail começam. Observe que a alteração dessa configuração não afetará nenhuma das mensagens de e-mail existentes. Você também pode substituir esse padrão a qualquer momento durante o envio de mensagens de e-mail.

{% alert note %}
Se estiver usando a [navegação mais antiga]({{site.baseurl}}/navigation), essa página está localizada em **Gerenciar configurações** > **Configurações de e-mail**).
{% endalert %}

![Opção de CSS embutido em novos e-mails por padrão, localizada nas configurações de e-mail.][1]

[1]:{% image_buster /assets/img_archive/css-inline1.png %}
[2]:{% image_buster /assets/img_archive/css-inline2.png %}

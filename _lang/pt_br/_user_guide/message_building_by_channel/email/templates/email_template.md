---
nav_title: Criação de um modelo de e-mail
article_title: Criação de um modelo de e-mail
page_order: 0
description: "Este artigo de referência aborda como criar, personalizar e gerenciar modelos de e-mail."
tool:
  - Templates
channel:
  - email
alias: "/dnd/email_template/"
search_rank: 1
---

# Criação de um modelo de e-mail

> O painel de controle do Braze tem um editor de modelos de e-mail que permite que você crie e-mails personalizados e atraentes e os salve para uso posterior em campanhas. Você também pode carregar seu próprio [modelo de e-mail em HTML]({{site.baseurl}}/user_guide/message_building_by_channel/email/templates/html_email_template/).

## Etapa 1: Navegue até o editor de modelos de e-mail

Vá para **Templates** > **Email Templates**.

## Etapa 2: Selecione sua experiência de edição 

Selecione entre o **Drag-And-Drop Editor** ou **o HTML Editor** para sua experiência de edição. 

Em seguida, você pode escolher entre modelos Braze predefinidos, criar um novo modelo ou editar um modelo existente (simples ou [responsivo para dispositivos móveis]({{site.baseurl}}/help/release_notes/2018/may/#mobile-responsive-email-templates)).

\![Um modelo de e-mail para uma promoção de primavera de uma empresa com opções para selecionar o editor de arrastar e soltar ou o editor HTML, ou para selecionar modelos do Braze.]({% image_buster /assets/img/email_templates/template2.png %})

{% alert note %}
Todos os modelos HTML personalizados existentes precisarão ser recriados usando o editor de arrastar e soltar.
{% endalert %}

## Etapa 3: Personalize seu modelo

Depois de selecionar sua experiência de editor, esta é sua oportunidade de ser criativo ao personalizar seu modelo de e-mail. Você pode usar HTML para criar e emular sua marca no editor de HTML ou incluir uma variedade de [detalhes criativos]({{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/overview/#creative-details) no editor de arrastar e soltar.

### Inclusão de um link para cancelar a assinatura

Ao criar seu modelo de e-mail, se você não incluir um link de cancelamento de inscrição, o Braze solicitará que você o adicione em seu e-mail, pois isso é exigido por lei em todos os e-mails de marketing. Você pode adicionar esse link de cancelamento de assinatura como um rodapé na parte inferior de seus e-mails usando a tag Liquid {% raw %}``${email_footer}``{% endraw %} ou [personalizando o rodapé]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#custom-footer) em seu modelo.

## Etapa 4: Verifique se há erros de e-mail

Os erros de e-mail são apresentados na guia **Compor** do fluxo de trabalho da mensagem. Os erros impedem que você avance. "Avisos" indicam lembretes para ajudá-lo a seguir as práticas recomendadas. Dependendo do seu negócio, você pode optar por ignorá-los.

\![Lista de erros e avisos de um e-mail de exemplo.]({% image_buster /assets/img/dnd_compose_error.png %}){: style="float:right;max-width:40%;margin-left:15px;"}

Aqui está uma lista de erros que são contabilizados em nosso editor:

- Sintaxe incorreta do Liquid
- [Corpos de e-mail maiores que 400kb; é altamente recomendável que os corpos sejam menores que 102kb]({{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices/)
- Modelos sem um link de cancelamento de assinatura
- E-mails com um **corpo** ou **assunto** em branco
- E-mails sem link para cancelar a assinatura

## Etapa 5: Visualize e teste sua mensagem

Depois de concluir a composição do modelo, você pode testá-lo antes de enviá-lo.

Na parte inferior da tela de visão geral, selecione **Preview and Test**. Aqui, você pode visualizar como seu e-mail aparecerá na caixa de entrada de um cliente. Com a opção **Preview as User** selecionada, você pode visualizar seu e-mail como um usuário aleatório, selecionar um usuário específico ou criar um usuário personalizado. Isso permite que você teste se o Connected Content e as chamadas de personalização estão funcionando como deveriam. 

Em seguida, você pode **Copiar link de visualização** para gerar e copiar um link de visualização compartilhável que mostra como será o e-mail para um usuário aleatório. O link terá duração de sete dias antes de precisar ser regenerado.

Você também pode alternar entre as visualizações de desktop, celular e texto simples para ter uma ideia de como sua mensagem aparecerá em diferentes contextos.

{% alert tip %}
Está curioso para saber como é o seu e-mail para os usuários do modo escuro? Selecione o botão de alternância **Dark Mode Preview** ( **Visualização** **do modo escuro** ) localizado na seção **Preview and Test (Visualização e teste** ) (somente no editor de arrastar e soltar).
{% endalert %}

Quando estiver pronto para uma verificação final, selecione **Test Send (Enviar teste)** e envie uma mensagem de teste para você mesmo ou para um grupo de testadores de conteúdo para garantir que seu e-mail seja exibido corretamente em vários dispositivos e clientes de e-mail.

\![Exemplo de visualização de e-mail a ser enviado para teste.]({% image_buster /assets/img_archive/newEmailTest.png %})

Se você encontrar algum problema com o modelo ou quiser fazer alguma alteração, selecione **Edit Email (Editar e-mail)** para retornar ao editor.

## Etapa 6: Salvar seu modelo

Certifique-se de salvar seu modelo selecionando **Save Template (Salvar modelo**). Agora você está pronto para usar esse modelo em qualquer campanha ou componente do Canvas que escolher. Para acessar seu modelo, selecione a experiência de edição com a qual você o criou e, em seguida, selecione-o na lista de modelos disponíveis.

{% alert note %}
Se você fizer qualquer edição em um modelo existente, essas alterações não serão refletidas nas campanhas criadas usando versões anteriores desse modelo.
{% endalert %}

### Gerenciando seus modelos

À medida que você cria mais modelos de e-mail, é possível [duplicar]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/managing_templates/#duplicate-templates) e [arquivar]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/managing_templates/#archive-templates) modelos de e-mail. Saiba mais sobre como criar e gerenciar sua biblioteca de modelos e conteúdo criativo em [Modelos e mídia]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/).

### Uso de seus modelos em campanhas de API

Para usar seu e-mail para uma campanha de API, você precisa de um `email_template_id`, que pode ser encontrado na parte inferior de qualquer modelo de e-mail criado no Braze.

Identificador de API localizado na parte inferior de um modelo de e-mail.]({% image_buster /assets/img/email_templates/template5.png %})

### Comentários sobre modelos de e-mail

Você pode colaborar e comentar em modelos de e-mail no editor de arrastar e soltar. 

1. Selecione o bloco de conteúdo ou a linha no corpo do e-mail que você deseja comentar.
2. Selecione o ícone de comentário <i class="fas fa-comment"></i>.
3. Digite seu comentário na barra lateral e selecione **Submit (Enviar**).
4. Depois de inserir seus comentários, selecione **Concluído**.
5. Selecione **Save Template (Salvar modelo** ) para salvar seus comentários.

Depois que o modelo for salvo, os usuários poderão ver ícones sobre os comentários não abordados. Selecione **Resolver** para resolver esses comentários.

\![Um comentário de modelo de e-mail que diz "Parece bom para mim".]({% image_buster /assets/img/email_templates/template_comment.png %})

Para obter respostas às perguntas mais frequentes sobre modelos de e-mail, consulte nossas Perguntas [frequentes sobre modelos]({{site.baseurl}}/user_guide/message_building_by_channel/email/templates/faq/).


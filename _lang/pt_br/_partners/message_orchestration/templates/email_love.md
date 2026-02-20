---
nav_title: "Email Love"
article_title: Email Love
description: "Aprenda a integrar o Braze com o Email Love, um plugin do Figma que permite projetar e exportar e-mails HTML responsivos e acessíveis diretamente do Figma."
alias: /partners/email_love/
page_type: partner
search_tag: Partner

---

# Email Love

> [Email Love](https://emaillove.com/) é um plugin do Figma que permite projetar e exportar e-mails HTML responsivos e acessíveis diretamente do Figma. O recurso Exportar para Braze do Email Love utiliza a API do Braze para fazer upload de seus modelos de e-mail para o Braze de forma integrada.

## Pré-requisitos

| Requisito            | Descrição                                                      |
|------------------------|------------------------------------------------------------------|
| **Conta do Email Love** | Uma conta do Email Love é necessária para aproveitar esta parceria. |
| **Chave da API REST do Braze** | Uma chave da API REST do Braze com `Templates` permissão total habilitada. Isso pode ser criado no dashboard do Braze em **Configurações** > **Chaves de API**. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation}

## Usando o Email Love com o Braze

### Etapa 1: Execute o plugin

Para projetar seu modelo de e-mail, você precisará primeiro carregar o plugin. Para instruções mais detalhadas, consulte a documentação do Email Love para [fazer upload do seu e-mail para o Braze](https://help.emaillove.com/exporting-an-email-design/6rcR6LPWq6BoYseKZf41nS/uploading-your-email-to-braze-/3ZcmGaGz6a8azeZQxWgKzm).

### Etapa 2: Crie seu primeiro quadro

No plugin, selecione o botão **[+ Nenhum Modelo Selecionado]** para criar um novo quadro para o design do seu e-mail.

### Etapa 3: Projete o modelo com os componentes pré-construídos do Email Love

Selecione o quadro que você criou e comece a adicionar componentes (cabeçalhos, blocos de conteúdo, CTAs e rodapés) da biblioteca **Ativos** do plugin para estruturar seu e-mail.

![Componentes pré-construídos do Email Love.]({% image_buster /assets/img/email_love/emaillove1_content.png %})

### Etapa 4: Personalize os Componentes

Modifique os componentes usando as ferramentas do Figma para ajustar seu texto, imagens, cores e elementos de layout para alinhar o design do modelo com sua marca. Se você adicionar um componente de rodapé, um link de cancelamento de inscrição do Braze será incluído automaticamente quando você exportar.

![Personalize componentes no Figma.]({% image_buster /assets/img/email_love/emaillove2_components.png %})

### Etapa 5: Exporte seu modelo de e-mail para Braze

1. Quando terminar, selecione o quadro que deseja exportar. Observe que você precisará usar um rodapé do Email Love que contenha um link de cancelamento de inscrição para que a exportação funcione.
2. Selecione o botão **Exportar** no plugin e selecione **Braze** no menu suspenso.
3. Copie e cole sua chave de API na caixa **Chave de API do Braze** dentro do plugin Email Love Figma.
4. Selecione o botão **Definir Chave de API**.
5. Selecione **Alterar ID da Instância**, em seguida, selecione seu ID da instância Braze.

![Exportando um modelo para Braze a partir do plugin Email Love.]({% image_buster /assets/img/email_love/emaillove3_exportbraze.png %}){: style="max-width:50%;"}

### Etapa 6: Edite seu e-mail no Braze

No Braze, vá para **Modelos** > **Editar Modelos** > **Editar Mensagem**. Dentro do editor de modelos, você pode editar o HTML do seu e-mail ou usar o **editor de texto rico** na aba **Clássica**.

## Suporte e solução de problemas

Para instruções mais detalhadas, consulte a documentação do Email Love sobre [exportar um design de e-mail](https://help.emaillove.com/exporting-an-email-design/6rcR6LPWq6BoYseKZf41nS/uploading-your-email-to-braze-/3ZcmGaGz6a8azeZQxWgKzm). Para suporte adicional, entre em contato com a equipe de suporte do Email Love.

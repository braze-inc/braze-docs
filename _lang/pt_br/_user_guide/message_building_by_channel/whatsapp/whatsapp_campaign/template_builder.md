---
nav_title: Criador de Modelos do WhatsApp
article_title: Criador de Modelos do WhatsApp
description: "Saiba como criar, configurar e enviar modelos de mensagem do WhatsApp diretamente na Braze usando o Criador de Modelos do WhatsApp."
alias: /whatsapp_template_builder/
page_type: reference
channel:
  - WhatsApp
---

# Criador de Modelos do WhatsApp

> O Criador de Modelos do WhatsApp permite criar e enviar modelos de mensagem do WhatsApp diretamente na Braze, sem precisar alternar entre a Braze e o Meta Business Manager. Depois que a Meta aprovar seu modelo, use-o em quantas campanhas e Canvas você quiser.

{% alert note %}
O Criador de Modelos do WhatsApp está atualmente em acesso antecipado. Entre em contato com o gerente da sua conta Braze para obter acesso.
{% endalert %}

## Pré-requisitos

Antes de criar um modelo do WhatsApp na Braze, conclua a [configuração do WhatsApp]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/).

## Criar um modelo

### Etapa 1: Acessar os Modelos do WhatsApp

Acesse **Modelos** > **Modelos do WhatsApp** e selecione **Criar novo modelo**.

![Página de modelos do WhatsApp com botão para criar um novo modelo.]({% image_buster /assets/img/whatsapp/templates/create_whatsapp_template.png %})

### Etapa 2: Configurar as definições do modelo

Preencha os seguintes campos:

| Campo | Descrição |
| ----- | ----- |
| **Conta** | A conta do WhatsApp Business (WABA) para a qual você deseja enviar o modelo. Todos os grupos de inscrições e números de telefone dentro de uma WABA compartilham o acesso ao modelo. |
| **Idioma** | O idioma deste modelo. O WhatsApp exige um modelo separado para cada idioma. |
| **Nome do modelo** | Um nome exclusivo para o seu modelo. Os nomes de modelo podem conter apenas letras minúsculas, números e underscores. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Etapa 3: Escolher um layout

Em **Layout**, selecione o tipo de modelo:

- **Padrão:** Uma mensagem padrão do WhatsApp. Este é o layout abordado neste artigo.  
- **Carrossel:** Uma mensagem com cartões roláveis horizontalmente. Para saber mais, consulte [Modelos de carrossel]({{site.baseurl}}/whatsapp_carousel_templates/).

### Etapa 4: Construir seu modelo

#### Cabeçalho (opcional)

Adicione um cabeçalho para aparecer acima do corpo da mensagem. Você pode escolher:

- **Texto:** Um cabeçalho de texto curto.  
- **Mídia:** Uma imagem, vídeo ou documento (somente URL). A Braze armazena a referência de mídia e envia uma amostra para a Meta para aprovação.  
- **Nenhum:** Sem cabeçalho 

#### Corpo

Insira o conteúdo principal da sua mensagem e personalize o corpo conforme necessário usando Liquid ou variáveis genéricas:

{% raw %}
- Use Liquid tags (por exemplo, `{{${first_name}}}`). A Braze salva seu Liquid e o exibe quando você usa o modelo em uma campanha ou no criador de Canvas.  
- Use variáveis genéricas, como placeholders numerados (por exemplo, `{{1}}`), se preferir adicionar personalização depois, ao construir sua mensagem.
{% endraw %}

Você pode adicionar personalização onde o botão **+** (mais) aparecer. Nem todos os campos suportam personalização.

#### Rodapé (opcional)

Adicione um rodapé curto para aparecer abaixo do corpo da mensagem.

#### Botões (opcional)

Adicione até 10 botões ao seu modelo. Os tipos de botão têm diferentes categorias e especificações.

| Tipo de botão | Categoria | Especificações |
| --- | --- | --- |
| Resposta rápida | Botões de resposta rápida |{::nomarkdown}<ul><li><b>Quantidade máxima:</b> 10</li><li><b>Texto do botão:</b> Até 25 caracteres</li></ul> {:/}|
| Número de telefone | Botões de chamada para ação | {::nomarkdown}<ul><li><b>Quantidade máxima:</b> 1</li><li><b>Texto do botão:</b> Até 25 caracteres</li><li><b>Número de telefone:</b> Número de telefone válido com código do país, sem + (como "14155552671")</li></ul> {:/}|
| Visitar site | Botões de chamada para ação | {::nomarkdown}<ul><li><b>Quantidade máxima:</b> 2</li><li><b>Texto do botão:</b> Até 25 caracteres</li><li><b>URL do site:</b> Até 2.000 caracteres</li></ul> {:/}|
| Copiar código de oferta | Botões de chamada para ação | {::nomarkdown}<ul><li><b>Quantidade máxima:</b> 1</li><li><b>Texto do botão:</b> "Copy offer code" (não pode ser editado)</li><li><b>Código de oferta:</b> Até 15 caracteres</li></ul> {:/}|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

![Criador de modelos do WhatsApp com botões de resposta rápida e chamada para ação.]({% image_buster /assets/img/whatsapp/templates/buttons.png %})

### Etapa 5: Visualizar seu modelo

Antes de enviar, visualize como sua mensagem aparecerá para os destinatários:

- **Visualizar como um usuário:** Veja uma prévia genérica da mensagem.  
- **Visualizar como um usuário específico:** Selecione um perfil de usuário para visualizar como o modelo será renderizado com os dados desse usuário.

### Etapa 6: Enviar para revisão

Selecione **Enviar** para enviar seu modelo à Meta para revisão, que normalmente leva alguns minutos, mas pode levar até 24 horas. O modelo aparece na sua página de **Modelos do WhatsApp** quando é enviado, e o status é atualizado quando você atualiza a página de **Modelos do WhatsApp**.

## Categorias de modelo suportadas

Apenas modelos de Marketing são suportados atualmente no Criador de Modelos do WhatsApp.

## Usar um modelo aprovado em uma campanha

Depois que a Meta aprovar seu modelo, você pode usá-lo em uma campanha ou Canvas do WhatsApp.

1. Acesse **Campanhas** e selecione **Criar Campanha** > **WhatsApp**.  
2. No criador de mensagens, selecione seu modelo aprovado.  
3. A Braze preenche automaticamente o conteúdo do modelo, incluindo qualquer mídia e Liquid que você inseriu durante a criação do modelo, para que você não precise inseri-los novamente.  
4. Atualize qualquer conteúdo variável ou personalização conforme necessário. Os campos bloqueados pela Meta (exibidos em cinza) não podem ser editados. Para alterar conteúdo bloqueado, você deve editar e reenviar o modelo para aprovação.  
5. Use a guia **Teste** para visualizar a mensagem, atualizar as variáveis do corpo e confirmar que a mensagem está como esperado antes do lançamento.

Para saber mais sobre como criar campanhas do WhatsApp, consulte [Criar uma mensagem do WhatsApp]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/create/).

## Perguntas frequentes

### Quanto tempo leva a revisão de modelo pela Meta?

As revisões normalmente são concluídas em cinco minutos, mas podem levar até 24 horas.

### Posso editar um modelo depois que ele foi aprovado?

Qualquer alteração em conteúdo bloqueado (texto do corpo ou outros campos controlados pela Meta) exige o reenvio do modelo para aprovação, o que deve ser feito pelo WhatsApp Business Manager. Você pode atualizar conteúdo e personalização ao construir sua campanha ou Canvas.

### O que acontece com os modelos que enviei antes de o Criador de Modelos estar disponível?

Os modelos criados no Meta Business Manager ainda estão disponíveis para uso na Braze. O Criador de Modelos é uma forma adicional de criar e gerenciar modelos sem sair do dashboard da Braze.

### Por que não consigo adicionar personalização a todos os campos?

A Meta restringe quais partes de um modelo podem ser personalizadas. O botão **+** (mais) aparece apenas nos campos que suportam conteúdo variável.
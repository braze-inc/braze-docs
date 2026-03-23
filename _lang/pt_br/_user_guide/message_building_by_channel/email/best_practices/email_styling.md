---
nav_title: Aplicação de estilo em e-mails
article_title: Estilo de e-mail
page_order: 2
page_type: reference
description: "Este artigo descreve as práticas recomendadas de estilo de e-mail que devem ser consultadas ao criar suas campanhas de e-mail."
channel: email

---

# Aplicação de estilo em e-mails

## Estilo de endereço

A **Linha de Assunto** é uma das primeiras coisas que os destinatários verão ao receber sua mensagem. O uso de 6 a 10 palavras produzirá as taxas de abertura mais altas. 

Há também diferentes abordagens para criar uma boa linha de assunto, desde fazer uma pergunta para despertar o interesse do leitor ou ser mais direto, até personalizá-la para engajar sua clientela. Não se limite a uma única linha de assunto, aproveite os [Testes A/B]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/#what-are-multivariate-and-ab-testing/) para experimentar novas linhas e avaliar sua eficácia. As linhas de assunto não devem ter mais de 35 caracteres para serem exibidas adequadamente no celular.

O campo "De" deve mostrar claramente quem é o remetente. Tente não usar o nome de uma pessoa ou uma abreviação incomum. Em vez disso, use um nome reconhecível, como o nome da sua marca. Se o uso do nome de uma pessoa for adequado aos métodos de personalização de e-mail da sua marca, mantenha a consistência para desenvolver um relacionamento com o destinatário. O nome "De" não deve ter mais de 25 caracteres para ser exibido adequadamente no celular.

### Endereços sem resposta

Endereços de e-mail sem resposta geralmente não são recomendados por vários motivos, pois eles desengajam seus leitores. Muitos destinatários respondem ao e-mail para cancelar inscrição, portanto, se não tiverem permissão para fazer isso, o próximo curso de ação é, na maioria das vezes, marcar o e-mail como spam.

Obter respostas de ausência do escritório pode, na verdade, fornecer informações valiosas, aumentando as taxas de abertura e diminuindo os relatórios de spam (removendo aqueles que não querem receber e-mails). Em um nível pessoal, uma ausência de resposta pode parecer impessoal para os destinatários e pode fazer com que eles deixem de receber mais e-mails da sua empresa.

## Texto do pré-cabeçalho

O texto do pré-cabeçalho em um e-mail comunica o ponto principal da mensagem de forma eficiente para atrair o interesse do leitor e incentivar a abertura. O texto do pré-cabeçalho também é frequentemente usado por profissionais de marketing de e-mail para fornecer informações adicionais sobre o conteúdo de um e-mail. Um pré-cabeçalho é o texto de prévia exibido imediatamente após o assunto de um e-mail. No exemplo a seguir, o pré-cabeçalho é `- Brand. New. Lounge Shorts`.

![Texto de pré-cabeçalho em uma caixa de entrada do Gmail com o texto "Brand. New. Lounge Shorts".]({% image_buster /assets/img_archive/preheader_example.png %})

A quantidade de texto visível do pré-cabeçalho depende do cliente de e-mail do usuário e do tamanho da linha de assunto do e-mail. Em geral, sugerimos que os pré-cabeçalhos de e-mail tenham entre 50 e 100 caracteres.

{% alert note %}
O pré-cabeçalho pode fazer referência ao Liquid no corpo do e-mail, e o corpo do e-mail pode fazer referência ao Liquid no pré-cabeçalho. Isso ocorre porque o texto do pré-cabeçalho é parte do corpo do e-mail quando você envia mensagens para os destinatários.
{% endalert %}

Aqui estão algumas práticas recomendadas que você deve ter em mente ao escrever seus pré-cabeçalhos:

1. As chamadas para ação entram em jogo depois que os leitores abrem seu e-mail.
  - Direcione seus leitores para a direção certa, seja para que eles se inscrevam, comprem um produto ou visitem seu site.
  - Use palavras fortes para que o leitor saiba exatamente o que você está pedindo, mas certifique-se de que isso reflita a voz da marca da sua empresa e que cada chamada para ação apresente algum tipo de valor para o consumidor.
  - O pré-cabeçalho não deve ter mais de 85 caracteres e deve ter algum tipo de chamada para ação descritiva que apoie a linha de assunto.

2. Os e-mails e sites de destino para os quais você direciona seus usuários devem ser otimizados para dispositivos móveis:
  - Sem caixas intersticiais
  - Campos de formulário grandes
  - Fácil navegação
  - Texto grande
  - Espaço em branco generoso
  - Texto do corpo curto e conciso
  - Chamadas para ação claras

### Limites de caracteres do pré-cabeçalho

  |   Cliente de e-mail móvel  |  Limite  |
  |:----------------------:|:-------:|
  | iOS Outlook            | 74      |
  | Android nativo         | 43      |
  | Android Gmail          | 24      |
  | iOS nativo             | 82      |
  | iOS Gmail              | 30      |
  {: .reset-td-br-1 .reset-td-br-2 role="presentation" }

  |  Cliente de e-mail para desktop  |  Limite  |
  |:----------------------:|:-------:|
  | Apple Mail             | 33      |
  | Outlook '13            | 38      |
  | Outlook para Mac '15   | 53      |
  | Outlook '16            | 50      |
  {: .reset-td-br-1 .reset-td-br-2 role="presentation" }


  |  Cliente de e-mail Webmail  |  Limite  |
  |:----------------------:|:-------:|
  | AOL Mail               | 81      |
  | Gmail                  | 119     |
  | Outlook.com            | 49      |
  | Office 365             | 40      |
  | Mail.ru                | 64      |
  {: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Tamanho do e-mail

Certifique-se de limitar o tamanho do seu e-mail. Corpos de e-mail maiores que 102&nbsp;KB não apenas sobrecarregam os servidores da Braze, mas também são cortados pelo Gmail e outros clientes de e-mail. Tente manter o tamanho do seu e-mail abaixo de 25&nbsp;KB apenas para texto ou 60&nbsp;KB com imagens. Recomendamos enfaticamente que você use nosso carregador de imagens para hospedar imagens e faça referência a essas imagens pelo `href`.

|   Apenas texto   | Texto com imagens |     Largura do e-mail    |
|:-------------:|:----------------:|:------------------:|
| Máximo de 25&nbsp;KB |   Máximo de 60&nbsp;KB   | Máximo de 600 pixels |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% alert note %}
Para salvar sua campanha de e-mail ou modelo, certifique-se de que o corpo do e-mail não exceda 400&nbsp;KB.
{% endalert %}

## Comprimento do texto

Consulte a tabela a seguir para ver os comprimentos de texto recomendados.

| Especificações de texto | Propriedades recomendadas |
| --- | --- |
| Comprimento da linha de assunto | Máximo de 35 caracteres (para otimizar a exibição em dispositivos móveis) (6 a 10 palavras) |
| Comprimento do nome do remetente | Máximo de 25 caracteres (para otimizar a exibição em dispositivos móveis) |
| Comprimento do pré-cabeçalho | Máximo de 85 caracteres |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Tamanho da imagem

Consulte a tabela a seguir para ver os tamanhos de imagem recomendados. Imagens menores e de alta qualidade serão carregadas mais rapidamente, portanto, use o menor ativo possível para obter o resultado desejado.

|     Tamanho    | Largura da imagem do cabeçalho |  Largura da imagem do corpo  |   Tipos de arquivos  |
|:-----------:|:------------------:|:------------------:|:-------------:|
| Máximo de 5&nbsp;MB | Máximo de 600 pixels | Máximo de 480 pixels | PNG, JPEG, GIF |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Deep links

Com notificações por push e mensagens no app, um [deep link]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/deep_linking_to_in-app_content/) leva os usuários diretamente a um destino específico dentro de um app. No entanto, deep links exigem que o app esteja instalado, e os e-mails não oferecem uma forma de saber se os destinatários têm o app. Isso significa que deep links em e-mails podem resultar em erros para destinatários que não têm o app instalado.

Em vez disso, use [links universais e App Links]({{site.baseurl}}/user_guide/message_building_by_channel/email/universal_links), que funcionam como URLs padrão. Você pode configurá-los para abrir o app ou direcionar os usuários a uma página específica. Eles também podem redirecionar para a loja de apps ou voltar para uma página da web quando o app não está instalado.
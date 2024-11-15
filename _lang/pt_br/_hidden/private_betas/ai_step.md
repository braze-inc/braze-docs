---
nav_title: Etapa de IA
article_title: Etapa de IA
permalink: /ai_step/
description: "Este artigo de referência aborda a etapa de IA no canva."
Tool:
  - Canvas
hidden: true
---

# Etapa IA

> A etapa de IA dentro do canva utiliza o ChatGPT para automatizar marketing personalizado, interpretando entradas geradas pelo usuário (como feedback de pesquisas), determinando a resposta adequada e disparando mensagens — tudo dentro da Braze. O ChatGPT é alimentado pela OpenAI, uma empresa terceira.

{% alert note %}
A etapa IA está atualmente disponível como um recurso beta. Entre em contato com seu gerente de sucesso do cliente se estiver interessado em participar dessa avaliação beta.
{% endalert %}

## Criação de uma etapa de IA {#create-ai-step}
 
1. Adicione uma nova etapa ao canva e selecione **Etapa de IA**. <br><br>![Etapa do IA no Criador de canvas][1]{: style="max-width: 30%;"}<br><br>
2. Crie um prompt que informe à IA como responder a várias ações do usuário. As respostas podem incluir a atualização de um atributo personalizado ou o envio de uma mensagem. Esse prompt pode usar o Liquid para atribuir diferentes saídas de resposta com base em diferentes atribuições ou entradas do usuário. <br><br>Para atribuir resultados que possam ser usados para personalizar mensagens futuras no mesmo Canva, crie um prompt que salve variáveis com nomes específicos (por exemplo, "mensagem" e "pontuação de sentimento"). <br><br> ![Exemplo de prompt de IA usado nas configurações da etapa de IA para enviar uma mensagem personalizada com base em uma pontuação de sentimento gerada. Esse exemplo é apresentado na seção "Respostas de sentimento do cliente".][2] <br><br>
3. Use a guia **Preview (Prévia** ) para testar o que a IA pode produzir para usuários específicos.<br><br> ![A guia Pré-visualização das configurações da etapa de IA mostra uma mensagem personalizada gerada por IA com três parâmetros: o primeiro nome "Cameron", o nome do produto "sapatos", e o texto "confortáveis, mas meu cadarço já estragou"][3]

## Referência à saída de IA usando Liquid
Faça referência à saída de IA nas etapas seguintes inserindo a lógica Liquid `{% raw %}{{ai_step_output.${key_name}}}{% endraw %}`. Você pode definir o endereço `key_name` dentro do prompt na etapa IA.

Por exemplo, se você usar as variáveis "message" (mensagem) e "sentiment score" (pontuação de sentimento), poderá usar `{% raw %}{{ai_step_output.${message}}}{% endraw %}` para personalizar uma mensagem subsequente no mesmo Canva.

Você também pode registrar a saída de qualquer etapa de IA como um atributo personalizado usando a etapa de atualização do usuário no canva, onde você lê a saída da etapa de IA (por exemplo, `{% raw %}{{ai_step_output.${sentiment_score}}}{% endraw %}`). Se a saída não for armazenada como um atributo personalizado, ela não poderá ser usada em nenhum outro lugar além das etapas subsequentes do mesmo Canva.

## Estatísticas de etapas da IA

As etapas de IA têm as seguintes estatísticas em nível de etapa:

- **Avançou para a próxima etapa:** Número de usuários que prosseguiram para a(s) etapa(s) seguinte(s) do Canva
- **Canva encerrado:** Número de usuários que saíram do Canva porque sua etapa do IA era a última etapa
- **Saída foi bem-sucedida:** Número de usuários para os quais a etapa de IA gerou resultados com sucesso
- **Falha na saída:** Número de usuários para os quais a etapa de IA não gerou saída; nesse caso, os usuários ainda prosseguirão para as etapas subsequentes.

### Compreensão dos resultados de suas etapas de IA

Há alguns cenários em que a Braze descartará a saída da etapa IA e enviará o cliente para a próxima etapa:
- Se a saída exceder 1.024 caracteres
- Se a saída não estiver em JSON
- Se o prompt não atender aos requisitos [de moderação](https://platform.openai.com/docs/guides/moderation/overview) da OpenAI, que sinaliza conteúdo inadequado gerado pelo usuário

## Casos de uso de etapas de IA

### Respostas ao sentimento do cliente

Conforme demonstrado pelo exemplo em [Criar uma etapa de IA](#create-ai-step), você pode solicitar que a IA envie mensagens de acompanhamento com base em pontuações de sentimento geradas a partir do feedback do cliente.
- Pontuações de sentimento positivo - Dispare uma notificação por push que peça aos usuários para deixar uma avaliação
- Pontuações médias de sentimento - Disparar um e-mail que pergunta aos usuários se eles gostariam de ajuda adicional
- Pontuações de sentimento baixas - disparam um webhook que notifica o Help Desk do usuário, para que um representante do suporte possa criar um acompanhamento diferenciado

#### Exemplo de prompt de IA

Esse exemplo foi usado na [etapa Criando uma IA](#create-ai-step).

Um cliente comprou "`{% raw %}{{canvas_entry_properties.${product_name}}}{% endraw %}`" e deu o feedback do produto: "`{% raw %}{{canvas_entry_properties.${text}}}{% endraw %}`". Crie uma pontuação de sentimento como um número inteiro entre 0 e 100. Em seguida, crie uma mensagem personalizada. Isso deve retornar duas variáveis, "message" (mensagem) e "sentiment score" (pontuação de sentimento).

### Acompanhamento de pesquisas

Se você executar uma pesquisa no app ou no navegador com uma seção de resposta livre, poderá usar as etapas de IA para analisar as respostas livres e fazer o acompanhamento adequado. 

Por exemplo, se um varejista de maquiagem tiver uma pesquisa perguntando: "Quais produtos você gostaria de indicar para os prêmios de beleza deste ano?", ele poderá usar um prompt que identifique e associe uma atribuição para os tipos e marcas de produtos favoritos do usuário e, em seguida, personalizar o conteúdo futuro com base nesses dados.

#### Exemplo de prompt de IA

Identifique a marca favorita do usuário usando a resposta dele. Em seguida, crie uma mensagem que agradeça aos usuários por preencherem a pesquisa e mencione como os especialistas em beleza também adoram sua marca favorita. Isso deve retornar duas variáveis, "message" (mensagem) e "favorite brand" (marca favorita).

![Guia Pré-visualização das configurações da etapa de IA mostrando uma mensagem personalizada gerada por IA para o parâmetro de resposta da pesquisa "Eu adoro os cremes faciais da Estee Lauder", que agradece ao usuário por preencher a pesquisa e, em seguida, recomenda um creme facial.][4]

### Recomendações orientadas por comportamento

Os clientes podem solicitar que a IA analise o comportamento do usuário e envie mensagens de recomendação. 

Por exemplo, é possível criar um prompt para analisar as 50 compras mais recentes dos usuários e definir a categoria mais comprada como um novo atributo personalizado. Em seguida, é possível enviar recomendações personalizadas por e-mail para a categoria favorita de cada usuário.

#### Exemplo de prompt de IA

Um cliente adquiriu os seguintes produtos: "`{% raw %}{{custom_attribute.${Products Purchased}}}{% endraw %}`". Identifique a categoria de produto mais comprada pelo usuário. Isso deve retornar uma nova variável para "categoria mais comprada".

![Guia Pré-visualização das configurações da etapa de IA mostrando a variável gerada pela IA de "livro" para o parâmetro da categoria mais comprada.][5]

## Limites de frequência

Há um limite de 10 solicitações por minuto (RPM) por empresa. Isso significa que, para qualquer etapa da IA, até 10 usuários podem receber essa etapa durante um determinado minuto e qualquer usuário além dos 10 avançará automaticamente para a próxima etapa. Quando o próximo minuto começar, os usuários poderão receber novamente a etapa IA, mas os usuários anteriores que dispararam o limite de frequência não serão tentados novamente.

## Limitações das etapas de IA

- Esse recurso utiliza o GPT-3.5.
- Esse recurso usa a chave de API da OpenAI da Braze. Não é possível usar sua própria chave de API da OpenAI.
- Há um limite de 5 solicitações por minuto (RPM) por espaço de trabalho e 10 RPM por empresa.
- Esse recurso não está em conformidade com a HIPAA e os clientes não devem enviar nenhuma informação de identificação pessoal (IPI) ou informações de integridade protegida (PHI).

## Como meus dados são usados e enviados para a OpenAI?

Para analisar e criar o conteúdo de suas mensagens, o Braze enviará seus prompts para a plataforma API da OpenAI. Todas as consultas enviadas à OpenAI pela Braze são anônimas, o que significa que a OpenAI não poderá identificar de quem a consulta foi enviada, a menos que você inclua informações exclusivamente identificáveis no conteúdo da mensagem que fornecer. Conforme detalhado nos [Compromissos da Plataforma de API da OpenAI](https://openai.com/policies/api-data-usage-policies), os dados enviados à API da OpenAI via Braze não são usados para treinar ou melhorar seus modelos e serão excluídos após 30 dias. Siga às políticas da OpenAI relevantes para você, incluindo a [Política de Uso](https://openai.com/policies/usage-policies). A Braze não oferece nenhuma garantia de qualquer tipo com relação a qualquer conteúdo gerado por IA. 

[1]: {% image_buster /assets/img/ai_step1.png %}
[2]: {% image_buster /assets/img/ai_step2.png %}
[3]: {% image_buster /assets/img/ai_step3.png %}
[4]: {% image_buster /assets/img/ai_step4.png %}
[5]: {% image_buster /assets/img/ai_step5.png %} 
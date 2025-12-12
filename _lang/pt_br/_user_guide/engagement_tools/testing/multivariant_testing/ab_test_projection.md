---
nav_title: Projeção de teste A/B
article_title: Projeção de teste A/B
page_order: 20
hidden: true
page_type: reference
description: "Este artigo explica como funciona a projeção de teste A/B, como executar uma projeção e como o Braze usa seus dados."
---

# Projeção de teste A/B

> A projeção de teste A/B usa redes neurais para prever quais linhas de assunto têm melhor desempenho. Nosso modelo extrai recursos linguísticos dos testes A/B vencedores realizados no Braze e usa esses padrões linguísticos estatísticos para ensinar à nossa IA o que torna as linhas de assunto melhores.

{% alert important %}
Esse recurso está atualmente em acesso antecipado. Entre em contato com o gerente de contas ou de sucesso do cliente Braze se estiver interessado em participar do acesso antecipado.
{% endalert %}

## Execução de uma projeção

Na composição da campanha, insira suas variantes de mensagem e suas linhas de assunto no editor. Quando estiver pronto, vá para a etapa **Target Audience (Público-alvo** ) do fluxo de criação da campanha. No painel **A/B Testing (Teste A/B** ), selecione **Run Projection (Executar projeção**).

<img width="518" alt="imagem" src="https://github.com/braze-inc/braze-docs/assets/17167198/8e74835c-76e4-4241-9763-c4f86a622c75">

Um modal será aberto com as linhas de assunto de quaisquer variantes de mensagem que você já tenha criado. Opcionalmente, você pode inserir linhas de assunto adicionais (até um máximo de dez) inserindo manualmente uma na caixa e executando a projeção. Selecione **Run Projection (Executar projeção**).

<img width="722" alt="imagem" src="https://github.com/braze-inc/braze-docs/assets/17167198/f9ad45a3-6565-467b-a7f6-35277bef7699">

A linha de assunto que nossa IA prevê ser a melhor será destacada com um rótulo de **Vencedor Projetado**.

{% alert note %}
Para [campanhas de envio rápido]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/quick_push/), há suporte para testes A/B quando você seleciona várias plataformas.
{% endalert %}

### Qual é a precisão das projeções?

Nos testes, descobrimos que as projeções são cerca de 70% precisas ao escolher entre pares de mensagens em testes A/B reais. Considere isso ao interpretar as mensagens que o modelo projeta para vencer.

### Como usamos seus dados?

Esse recurso aprende com os testes A/B anteriores realizados no Braze. A cópia real de suas mensagens ou das mensagens de qualquer cliente Braze nunca é fornecida ao modelo. Primeiro, extraímos os padrões de linguagem de alto nível que preveem mensagens vencedoras em testes A/B. Em seguida, fornecemos esses padrões à nossa IA para ensiná-la a discernir quais recursos linguísticos constituem linhas de assunto superiores.
---
nav_title: Informações de contato
article_title: Informações de contato
page_order: 0
page_type: reference
description: "Este artigo de referência aborda informações importantes para administradores sobre como gerenciar as informações de contato e o fuso horário da sua empresa no Braze."

---

# Informações de contato

> Como administrador, você pode usar a página **Informações de Contato** para gerenciar as informações de contato e o fuso horário da sua empresa no Braze.

Para acessar essa página, acesse **Configurações** > **Configurações administrativas** > **Informações de contato**. Certifique-se de selecionar **Salvar** para aplicar quaisquer alterações antes de sair da página.

## Consequências da mudança de fuso horário

{% alert warning %}
Mudar de fuso horário pode causar discrepâncias de dados em torno do período em que o fuso horário foi alterado. Se você mudar seu fuso horário, o Braze faz um esforço de boa-fé para converter as informações com precisão, mas não garante uma conversão perfeita. Você pode notar uma descontinuidade em seus dados, onde eles podem alternar entre fusos horários.
{% endalert %}

Se você optar por mudar de fuso horário, poderá sofrer uma série de consequências, inclusive:

- Embora as campanhas programadas para horários específicos em locais específicos (como 21h, horário da costa leste dos EUA) sejam executadas adequadamente dentro do cronograma até serem editadas, a análise de dados da campanha e as programações de campanhas futuras serão afetadas pela alteração.
- Qualquer programação de cartão que não seja atribuída ao fuso local pode ser afetada, com cartões ativos potencialmente aparecendo como finalizados ou o contrário.
- Os filtros de segmentação da forma "Fez X antes/depois `Date`" terão o tempo ajustado porque a data inicial agora será localizada no fuso horário padrão do seu espaço de trabalho (por exemplo, Horário do Pacífico).

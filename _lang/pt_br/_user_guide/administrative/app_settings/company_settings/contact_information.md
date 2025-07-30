---
nav_title: Informações de contato
article_title: Informações de contato
page_order: 0
page_type: reference
description: "Este artigo de referência aborda informações importantes para administradores sobre como gerenciar as informações de contato e o fuso horário da sua empresa no Braze."

---

# Informações de contato

<style>
.fa-crown {
  color: gold;
}
</style>

> Esta página contém informações importantes para administradores sobre como gerenciar as informações de contato e o fuso horário da sua empresa no Braze.

Para acessar essa página, acesse **Configurações** > **Configurações administrativas** > **Informações de contato**.

É nessa página que você pode gerenciar as informações de contato e o fuso horário da sua empresa. Não se esqueça de clicar em **Salvar** antes de sair da página!

## Consequências da mudança de fuso horário

{% alert warning %}

A mudança de fuso horário pode causar algumas discrepâncias de dados em torno do ponto em que o fuso horário foi alterado. Se alguém muda de fuso horário, fazemos um esforço de boa fé para converter as coisas com precisão, mas nem sempre a conversão é perfeita. Você pode notar uma descontinuidade em seus dados, onde eles podem alternar entre fusos horários.

{% endalert %}

Se você optar por mudar de fuso horário, poderá sofrer uma série de consequências, inclusive:

- Embora as campanhas programadas para horários específicos em locais específicos (como 21h, horário da costa leste dos EUA) sejam executadas adequadamente dentro do cronograma até serem editadas, a análise de dados da campanha e as programações de campanhas futuras serão afetadas pela alteração.
- Qualquer programação de cartão que não seja atribuída ao fuso local pode ser afetada, com cartões ativos potencialmente aparecendo como finalizados ou o contrário.
- Os filtros de segmentação do formulário "Has done X before/after `Date`" terão a hora ajustada porque a data inicial agora será localizada no horário do Pacífico.
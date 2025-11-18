{% if include.section == "Plan-specific features" %}

## Recursos de IA específicos do plano

A tabela a seguir descreve as diferenças entre a versão gratuita e a versão profissional dos tipos de recomendação IA Personalized, Popular e Trending:

| Área                   | Versão gratuita                          | Versão Pro            |
| :---------------------- | ------------------------------------- | :--------------------------------------- |
| <sup>Frequência</sup> de atualização do usuário1   | Semanalmente                                | Diariamente                                    |
| Frequência de retreinamento do modelo  | Mensalmente                               | Semanalmente                                   |
| Modelos de recomendação máxima | 1 modelo por <sup>tipo2</sup> | 100 modelos por <sup>tipo2</sup> |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

<sup>1\. Essa é a frequência com que as recomendações de itens específicos do usuário são atualizadas (todos os modelos, exceto os itens Mais populares, que são atualizados quando o modelo é retreinado). Por exemplo, se um usuário comprar um item recomendado com base nas recomendações de itens da IA, seus itens recomendados serão atualizados de acordo com essa frequência</sup><br>
<sup>2\. Os tipos de recomendação disponíveis são IA Personalizada, Mais recente, Mais popular e Tendências.</sup>

{% endif %}

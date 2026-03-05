---
nav_title: Transformação de dados
hidden: true
---

# Transformação de dados do Braze

> O Braze [Data Transformation]({{site.baseurl}}/data_transformation/) pode ingerir um webhook de uma plataforma parceira e permitir que um cliente defina um mapeamento para converter a carga útil desse webhook nos dados de usuários desejados, como atributos, eventos ou compras nos perfis de usuários do Braze.

## Como seria uma integração baseada em transformação de dados

Uma integração com parceiros baseada no recurso Data Transformation poderia ser um modelo de código de transformação compartilhado com os clientes por meio de documentação pública.

Para clientes mútuos, seria algo parecido assim:

1. Eles registram-se em sua plataforma e configuram webhooks.
2. Eles trabalham com a equipe do Braze para obter acesso à transformação de dados do Braze e criar uma nova transformação no dashboard do Braze.
3. O URL gerado pela transformação é copiado.
4. De volta à Braze, eles enviam um webhook de teste para o URL de transformação copiado.
5. Na Braze, eles copiam e colam o modelo do código de transformação.
6. Eles ativam a transformação.
7. Quando ativada, eles podem verificar, por meio da ferramenta de pesquisa de usuários do Braze, se o perfil do usuário é atualizado com base no webhook e editar o código de transformação conforme desejado.

{% alert tip %}
Recomenda-se a criação de uma transformação por tipo de webhook enviado ao Braze ao criar exemplos de código de transformação.
{% endalert %}

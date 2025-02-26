---
nav_title: Solução de problemas de exportação
article_title: Solução de problemas de exportação
page_order: 10
page_type: reference
description: "Este artigo de referência cobre alguns cenários comuns de solução de problemas para API e exportações CSV."

---

# Exportação de solução de problemas

> Esta página lista as mensagens de erro que você pode encontrar ao exportar dados por meio de CSV ou API do Braze.

## Erros comuns

### AcessoNegado 

#### Ao usar seu próprio bucket S3

Se estiver usando **seu próprio bucket S3**, isso pode acontecer porque:

- O objeto esperado não está mais no bucket S3; verifique com seus engenheiros.
- As credenciais S3 configuradas no dashboard do Braze não têm as permissões corretas; confirme as credenciais adequadas com sua equipe.

#### Ao usar um bucket S3 da Braze

Se estiver usando um **bucket S3 do Braze**, isso pode acontecer porque:

- O objeto não está mais lá. Isso pode ocorrer se você clicar em um link para uma exportação que foi executada há mais de 4 horas. Se for esse o caso, execute sua exportação novamente.
- Você selecionou o link para baixar imediatamente, antes que o S3 estivesse pronto para servir o objeto. Aguarde alguns minutos e tente novamente. Relatórios maiores geralmente demoram mais. 
- A exportação é muito grande, então nosso servidor ficou sem memória ao tentar criar este arquivo zip. Enviaremos automaticamente um e-mail ao usuário que estiver tentando fazer esta exportação, caso isso ocorra. Se o problema persistir, recomendamos que use seus próprios buckets S3.

### TokenExpirado

Isso acontece se o e-mail tiver sido enviado há mais de 4 horas. Execute novamente a exportação e baixe-a dentro de 4 horas.

Isso também pode ser causado por que a Braze não tem mais acesso ao bucket S3 para o qual você está baixando os dados. Atualize suas credenciais S3 usando estas etapas.

### Parece que o arquivo não existe mais, por favor verifique para garantir que nada esteja excluindo objetos do seu bucket

Pode haver um pequeno atraso entre o momento em que o e-mail da Braze com a exportação é enviado e quando o S3 está realmente pronto para servir o objeto. Caso veja esse erro, aguarde alguns minutos antes de tentar novamente.

### Apóstrofos adicionados aos campos

Braze adicionará automaticamente um apóstrofo a um campo na exportação CSV se o campo começar com qualquer um dos seguintes caracteres:

- -
- =
- +
- @

Por exemplo, o campo "-1943" será exportado como "'-1943". Isso não se aplica a exportações JSON, como as retornadas pelo [endpoint `/users/export/segment` ]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment/).
---
nav_title: Exportar solução de problemas
article_title: Exportar Solução de Problemas
page_order: 10
page_type: reference
description: "Este artigo de referência cobre alguns cenários comuns de solução de problemas para exportações de API e CSV."

---

# Exportar solução de problemas

> Esta página lista mensagens de erro que você pode encontrar ao exportar dados através de CSV ou API do Braze.

## Erros comuns

### 'AcessoNegado' 

#### Ao usar seu próprio bucket S3

Se você estiver usando **seu próprio bucket S3**, isso pode acontecer porque:

- O objeto esperado não está mais no bucket S3; verifique com seus engenheiros.
- As credenciais S3 configuradas no painel do Braze não têm as permissões corretas; confirme as credenciais adequadas com sua equipe.

#### Ao usar um bucket S3 do Braze

Se você estiver usando um **bucket S3 do Braze**, isso pode acontecer porque:

- O objeto não está mais lá. Isso pode ocorrer se você clicou em um link para uma exportação que expirou, pois os arquivos são automaticamente excluídos do S3 quando o link de download expira. Salvo indicação em contrário, os arquivos são removidos após quatro horas. Se este for o caso, execute sua exportação novamente.
- Você selecionou o link de download imediatamente, antes que o S3 estivesse pronto para servir o objeto. Aguarde alguns minutos e tente novamente. Relatórios maiores geralmente levarão mais tempo. 
- A exportação é muito grande, então nosso servidor ficou sem memória ao tentar criar este arquivo zip. Nós enviaremos automaticamente um e-mail para o usuário que está tentando esta exportação se isso ocorrer. Se você encontrar consistentemente esse problema, recomendamos que você use seus próprios buckets S3 no futuro.

### 'TokenExpirado'

Isso acontece se o e-mail foi enviado há tempo suficiente para que o arquivo S3 tenha expirado. Salvo indicação em contrário, os arquivos são removidos após quatro horas. Reexecute a exportação e faça o download antes que o arquivo expire.

Isso também pode ser causado pelo Braze não ter mais acesso ao bucket S3 para o qual você está baixando os dados. Certifique-se de que você atualizou suas credenciais S3 seguindo estas etapas.

### "Parece que o arquivo não existe mais, por favor verifique se nada está excluindo objetos do seu bucket"

Pode haver um pequeno atraso entre quando o e-mail do Braze com a exportação é enviado e quando o S3 está realmente pronto para servir o objeto. Se você ver este erro, aguarde alguns minutos antes de tentar novamente.

### Apóstrofos adicionados aos campos

O Braze automaticamente adicionará um apóstrofo a um campo na exportação CSV se o campo começar com qualquer um dos seguintes caracteres:

- -
- =
- +
- @

Por exemplo, o campo "-1943" será exportado como "'-1943". Isso não se aplica a exportações JSON, como aquelas retornadas pelo [`/users/export/segment` endpoint]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment/).
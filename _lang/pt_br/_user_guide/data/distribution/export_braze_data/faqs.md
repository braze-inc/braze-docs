---
nav_title: PERGUNTAS FREQUENTES
article_title: Perguntas frequentes sobre exportação
page_order: 11
page_type: FAQ
description: "Este artigo aborda algumas perguntas frequentes sobre exportações de API e CSV."

---

# Perguntas frequentes

> Esta página fornece respostas a algumas perguntas frequentes sobre exportações de API e CSV.

### Você pode fazer com que determinadas exportações apareçam em seu bucket S3 e outras não?

Não. Se você tiver fornecido credenciais do S3, todas as suas exportações aparecerão em seu bucket do S3; caso contrário, se nenhuma credencial for fornecida, todas as exportações aparecerão em um bucket do S3 pertencente ao Braze.

### Preciso adicionar credenciais S3 ao Braze para exportar dados?

Não. Se você não adicionar credenciais do S3, suas exportações aparecerão em um bucket do S3 pertencente ao Braze.

### O que acontece se você configurar as credenciais do S3 no painel, mas não selecionar "Tornar este o destino padrão de exportação de dados"?

A caixa de seleção **Tornar este o destino padrão de exportação de dados** afeta o fato de as exportações irem para o S3 ou para o Azure, supondo que você tenha adicionado credenciais para ambos.

### Por que recebi vários arquivos ao exportar perfis de usuário para o S3?

Esse é o comportamento esperado para espaços de trabalho com muitos usuários. O Braze dividirá sua exportação em vários arquivos com base no número de usuários em seu espaço de trabalho. Em geral, há uma saída de arquivo para cada 5.000 usuários. Observe que, se estiver exportando um pequeno segmento dentro de um espaço de trabalho grande, você ainda poderá receber vários arquivos.

### Por que vejo duplicatas quando exporto usuários por segmento por meio da API REST?

Essa é uma ocorrência muito rara causada pela arquitetura subjacente do provedor de banco de dados. As duplicatas são limpas toda semana; no entanto, na maioria das semanas, nenhuma duplicata é limpa.

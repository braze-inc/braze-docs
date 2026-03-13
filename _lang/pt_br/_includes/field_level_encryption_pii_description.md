{% comment %}
  Descrição da criptografia em nível de campo de identificador e IPI. Uso no documento de criptografia em nível de campo e notas de lançamento.
  Parâmetros:
  - link (opcional): Se definido, "a criptografia em nível de campo de identificador" será envolvida neste link (e.g. {{site.baseurl}}/user_guide/analytics/field_level_encryption/).
{% endcomment %}
{% if include.link %}
Usando [criptografia em nível de campo de identificador]({{ site.baseurl }}/{{ include.link }}), você pode criptografar endereços de e-mail com o AWS Key Management Service (KMS) para minimizar as informações pessoalmente identificáveis (IPI) compartilhadas no Braze. A criptografia substitui dados confidenciais por texto cifrado, que é uma informação criptografada ilegível.
{% else %}
Usando a criptografia em nível de campo do identificador, é possível criptografar perfeitamente os endereços de e-mail com o AWS Key Management Service (KMS) para minimizar as informações de identificação pessoal (IPI) compartilhadas no Braze. A criptografia substitui dados confidenciais por texto cifrado, que é uma informação criptografada ilegível.
{% endif %}

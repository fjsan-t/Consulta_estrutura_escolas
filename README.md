<h1>Análise de Dados das Escolas da Bahia</h1>

<p>Aplicação web full-stack em desenvolvimento para consulta e filtragem de dados sobre a infraestrutura das escolas públicas no estado da Bahia. O projeto conta com uma API RESTful em FastAPI hospedada no Render e uma interface em HTML e JavaScript hospedada no GitHub Pages.</p>

<h2>Links do Projeto</h2>

<ul>
  <li><strong>Frontend:</strong> <a href="https://fjsan-t.github.io/Consulta_estrutura_escolas/">https://fjsan-t.github.io/Consulta_estrutura_escolas/</a></li>
  <li><strong>Backend API:</strong> https://anallise-dados-escolas-bahia.onrender.com/api</li>
</ul>

<h2>Tecnologias Utilizadas</h2>

<h3>Análise de Dados</h3>
<ul>
  <li>Google Colab</li>
  <li>Python & Pandas</li>
</ul>

<h3>Backend</h3>
<ul>
  <li>Python</li>
  <li>FastAPI</li>
  <li>Pandas/ SQLite</li>

</ul>

<h3>Frontend</h3>
<ul>
  <li>HTML5/ CSS3</li>
  <li>JavaScript </li>
</ul>

<h2>Funcionalidades</h2>

<ul>
  <li>Filtro por município</li>
  <li>Filtro por rede de ensino (Estadual / Municipal)</li>
  <li>Filtro por presença de laboratório de informática</li>
  <li>Busca por nome da escola</li>
  <li>Contador de escolas encontradas</li>
</ul>

<h2>Endpoints da API</h2>

<table border="1">
  <thead>
    <tr>
      <th>Método</th>
      <th>Rota</th>
      <th>Descrição</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>GET</td>
      <td>/api/municipios</td>
      <td>Retorna a lista de municípios da Bahia.</td>
    </tr>
    <tr>
      <td>GET</td>
      <td>/api/escolas</td>
      <td>Retorna a lista de escolas filtradas.</td>
    </tr>
  </tbody>
</table>

<h2>Como Rodar o Projetos Localmente</h2>

<h3>1. Clonar o repositório</h3>
<pre>git clone https://github.com/fjsan-t/anallise-dados-escolas-bahia.git
cd anallise-dados-escolas-bahia</pre>

<h3>2. Instalar dependências e rodar a API</h3>
<pre>pip install -r requirements.txt
uvicorn main:app --reload</pre>


<h2>Próximos passos</h2>

<p>Implementação de dashboards para visualização de dados </p>
<p>Inserir informações como contato e localização das escolas. </p>

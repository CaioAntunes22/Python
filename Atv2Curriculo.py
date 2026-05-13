from flask import Flask

app = Flask(__name__)  # inicio o flask


@app.route(
    "/"
)  # Isso é o decorator, ele é usado para mapear a função abaixo para a rota '/'
def curriculo():
    return """
    
<!DOCTYPE html>
<html lang="pt-br">
<head>
<meta charset="UTF-8">
<title>Currículo Online</title>

<style>
*{
margin:0;
padding:0;
box-sizing:border-box;
}

body{
font-family: Arial, sans-serif;
background: #1e1e2f;
color: white;
padding: 40px;
}

.curriculo{
max-width: 900px;
margin:auto;
background:#2b2b40;
border-radius:15px;
overflow:hidden;
box-shadow:0 0 20px rgba(0,0,0,0.5);
}

.topo{
background:#6c63ff;
padding:30px;
text-align:center;
}

.topo h1{
font-size:40px;
}

.topo p{
margin-top:10px;
}

.conteudo{
padding:30px;
}

h2{
color:#6c63ff;
margin-bottom:10px;
margin-top:25px;
}

ul{
margin-left:20px;
}

.card{
background:#3a3a55;
padding:15px;
border-radius:10px;
margin-bottom:15px;
}

.idiomas{
display:flex;
gap:20px;
}

.idioma-box{
background:#6c63ff;
padding:15px;
border-radius:10px;
width:200px;
text-align:center;
}
</style>

</head>
<body>

<div class="curriculo">

<div class="topo">
<h1> Caio Antunes </h1>
<p> (31) 99999-9999 </p>
<p> caio@gmail.com </p>
</div>

<div class="conteudo">

<h2>Objetivo</h2>
<p> Emprego </p>

<h2>Formação</h2>
<ul>
Ensino Tecnico
</ul>

<h2>Experiência Profissional</h2>


<div class="card">
<h3> nenhum </h3>
<p> nenhum </p>
<small> 0 </small>
</div>


<h2>Cursos</h2>
<ul>
<li>TI</li>

</ul>

<h2>Idiomas</h2>

<div class="idiomas">
<div class="idioma-box">
<h3>Inglês</h3>
<p> Ingles </p>
</div>

<div class="idioma-box">
<h3>Espanhol</h3>
<p> Ingles </p>
</div>
</div>

</div>

</div>

</body>
</html> """


if __name__ == "__main__":
    app.run(
        debug=True
    )  # Isso inicia o servidor Flask em modo de depuração, o que é útil para desenvolvimento

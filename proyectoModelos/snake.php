<?php
//VISTA
      session_start();
     $name = $_SESSION['name'];
     $clave=$_SESSION['clave'];
      if(!isset($name)){
          header("location: index.php");
        }else{
?>
	<html>
		<head>
			<title>Snake</title>
			<link rel="stylesheet" type="text/css" href="static/css/estilos.css">
            <link rel="stylesheet" type="text/css" href="static/css/estilo1.css">
            <link rel="stylesheet" type="text/css" href="static/css/style.css">

        </head>
		<body>
        <header>
		<div class="logo">JuegosXmonton</div>
		<div>
        <nav>
        <a href="inicio.php"> Inicio</a>
        <a href="puntajesj.php"> &#127918;<?php
            echo "  $name ";
            $_SESSION['name'] = $name; 
        }       
        ?></a>
            <a href="salir.php"> Salir</a>
		</nav>
	</div>
	</header>  
		<br>
		<center><b>________________________________<img src="static/imagenes/snakegif.gif" width="100" height="100">
		<input type="checkbox" id="chec">
		<label for="chec">
			<img src="static/imagenes/menu.png" width="80" height="90">
		</label>
		<nav>
			<ul>
				<li><b></b></li>
				<li><h5>INSTRUCCIONES</h5></li>
				<br>
				<li><h3>Snake es el famoso juego que todos jugamos en un NOKIA de la serpiente que va creciendo y crecioendo mientras se va alimentando.</h3></li>
				<li><h3>Ayuda a la serpiente a conseguir mas puntos para que siga creciendo moviendola con las flechas del teclado.</h3></li>
				<li><h3>___________________________</h3></li>
				<li><center><h3>BUENA SUERTE</h3></li>
				<li><b><center><img src="static/imagenes/snakeInst.png" width="150" height="120"></b></li>
			</ul>
		</nav>
		<center><h4 id="Puntaje">Puntaje: 0</h4>
		<center><h4 id="Puntajem">Maximo puntaje: 0</h4>
			<canvas id="c" width="450" height="450"></canvas>
		<script type="text/javascript" src="funcsnake.js"></script>
		</center>
		<div class="social-bar">
			<a href="index.html" class="icon icon-frUDiv" target="_blank"></a>
			<a href="https://www.youtube.com/watch?v=v26_pOpZDw0" class="icon icon-youtube" target="_blank"></a>
		</body>
	</html>
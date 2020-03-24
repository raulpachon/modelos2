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
    <meta charset="utf-8">
    <title>JuegosXmonton</title>
    <link href="static/css/estilo1.css" rel="stylesheet">
    <script src="http://code.jquery.com/jquery-latest.js"></script>
    <script src="header.js"></script>
</head>

<body>

    <header>
        <div class="logo">JuegosXmonton</div>
        <nav>
        <a href="inicio.php"> Inicio</a>
        <a href="#"> &#127918;<?php
            echo "  $name ";
            $_SESSION['name'] = $name;        
        ?></a>
            <a href="salir.php"> Salir</a>
        </nav>
    </header>
    <div class="contenedor">
<p>Hola <?php echo "  $name "; ?> estos son tus puntajes:</p><br>
    <table style="margin: auto; width: 800px; border-collapse: separate; border-spacing: 10px 5px;">
            <thead>
              <th>juego.</th>
              <th>puntaje</th>
            </thead>

            <?php
            include "conexion.php";
            $sql =<<<EOF
            SELECT * FROM puntajes WHERE nomJugador = '$name';
EOF;
            $ret = $db->query($sql);
            while($row = $ret->fetchArray(SQLITE3_ASSOC) ) {
            
              echo "<tr>";
                echo "<td>".$row['nomJuego']."</td>";
                echo "<td>"; echo $row['puntos']; echo "</td>";
     
              echo "</tr>";
            }
        }
            ?>
          </table>
        </div>
    </body>

</html>
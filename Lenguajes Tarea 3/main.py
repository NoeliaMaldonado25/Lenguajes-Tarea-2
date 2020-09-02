import webbrowser

funcion = open('Reporte.html','w')

mensaje = """<html>
<head>
<title>REPORTE</title>
<link rel="stylesheet" href="./archivo css/style.css">
</head>

<body> 
<h1> Reporte</h1>
<h2> Reporte de empleados</h2>
<ol>
    <li>
        <object>
        Noelia Raquel Yoc Maldonado, 25 años, activa, Q. 200
        </object>
    </li>
    <li>
        <object>
        Andrea Magali Cifuente Ortega, 22 años, activa, Q. 150
        </object>
    </li>
    <li>
        <object>
        Javier Alejandro Lopez Tuyun, 50 años, inactivo, Q. 350
        </object>
    </li>
    <li>
        <object>
        Armando Eddi Menzadosa Solarez, 32 años, inactivo, Q. 00
        </object>
    </li>
    <li>
        <object>
        Beatriz Camila Pinzon Solano, 29 años, activa, Q. 200
        </object>
    </li>
    <li>
        <object>
        Patricia Eugenia Fernadez Chocoy, 23 años, activa, Q. 35
        </object>
    </li>
    <li>
        <object>
        Harry Andres Potter Valdez, 45 años, activo, Q. 100
        </object>
    </li>
    <li>
        <object>
        Wison Estuardo Jimenez Duran, 28 años, inactivo, Q. 00
        </object>
    </li>
    <li>
        <object>
        Francisco Pedro Torres Catu, 25 años, activo, Q. 50
        </object>
    </li>
    <li>
        <object>
        Helen Abigail Barrera Godinez, 25 años, activa, Q. 550
        </object>
    </li>

</ol>


</body>
</html>"""

funcion.write(mensaje)
funcion.close()

webbrowser.open_new_tab('Reporte.html')

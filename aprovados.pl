estudiante("camilo").
estudiante("maria").
asignatura("modelos_2").
inscrito("camilo", "modelos_2").
nota_aprueba(35).
asistencia("camilo",45).
asistencia("maria",20).
notapc("camilo","modelos_2",30).
notapc("maria","modelos_2",20).
notasc("camilo","modelos_2",45).
notasc("maria","modelos_2",20).
notatc("camilo","modelos_2",47).
notatc("maria","modelos_2",47).
notafn(A,B,Y):-notapc(A,B,C),notasc(A,B,D),notatc(A,B,E), Y is ((C+D+E)/3).
aprueba(A,B,Y):-notafn(A,B,Y),nota_aprueba(X),Y>X.
no_aprueba(A,B,Y):-notafn(A,B,Y),nota_aprueba(X),Y<X.
no_aprueba_asis(A,B):-asistencia(A,B), B<32.
aprueba_asis(A,B):-asistencia(A,B),B>32.
aprobados(A,B,Y,D):-aprueba(A,B,Y),asistencia(A,D),Y>35,D>32.
no_aprobados(A,B,Y,D):-aprueba(A,B,Y),asistencia(A,D),Y<35,D<32.

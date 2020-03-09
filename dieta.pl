alimento(a,posillo_zucaritas,110).
alimento(b,vegetal,155).
alimento(c,posillo_de_leche,660).
alimento(c,huevo_frito,110).
alimento(c,bife_de_vaca,185).
alimento(c,pechuga_de_pollo,185).
alimento(d,helado,330).

plato([1,B,C]):-alimento(A,B,C).

calorias([A,B,C],C):-!.

pertenece(B,[X|L]):- pertenece1(B,X).
pertenece(B,[X|L]):-pertenece(B,L).

pertenece1([V,B,M],[A,B,C]):-!.

suma([],0):-!.
suma([X|L],S):- suma(L,T), calorias(X,R), S is R+T.

insertar(X,[],[X]):-!.
insertar(X,L,[X|L]):-not pertenece(X,L),!.
insertar(X,L,R):-suma_c(X,L,R).

suma_c(X,[R|L],T):-pertenece1(X,R),suma_caloria(X,R,U),concatenar([U],L,T).
suma_c(X,[R|L],[R|T]):-suma_c(X,L,T).

suma_caloria([A,B,C],[R,B,V],[X,B,N]):-N is V+C, X is R+A.

concatenar([],L,L):-!.
concatenar([X|R],L,[X|T]):-concatenar(R,L,T).

arma_dieta(L,L):-suma(L,T),T>2400,T<2800,!.
arma_dieta(L,L1):-suma(L,T),T<2400,plato(X),insertar(X,L,L2),arma_dieta(L2,L1).

arma_dieta1(L,N):-arma_dieta([],L),suma(L,N).

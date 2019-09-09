-- esta es la funcionn recursiva de potenciacion 2 3  ==  8

potencia :: Integer -> Integer -> Integer
potencia m 0 = 1
potencia m n = m*(potencia m (n-1))
 
--esta es la funcionn recursiva de fibonacci 8 ---> 21
fibonacci :: Int -> Int
fibonacci 0 = 0
fibonacci 1 = 1
fibonacci (n+2) = fibonacci n + fibonacci (n+1)

--esta es la funcionn recursiva de division 8 2== 4
division :: Integer -> Integer -> Integer
division m > n  = 0
division m <= n = 1+(division m (n-1))

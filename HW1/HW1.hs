-- CptS 355 - Fall 2020  : 09/06/2020

module HW1
     where
import Data.Char ()



-- 1.a. biggerDate and maxDate
biggerDate :: (Ord a1,Ord a2,Ord a3) => (a3,a2,a1) -> (a3,a2,a1) -> (a3,a2,a1)
biggerDate (a,b,c) (d,e,f) | c > f = (a,b,c)
                         | c < f = (d,e,f)
                         | c == f && b > e = (a,b,c)
                         | c == f && b < e = (d,e,f)
                         | c == f && b == e && a > d = (a,b,c)
                         | c == f && b == e && a < d = (d,e,f)
                         | otherwise = (a,b,c)
-- 1.b. maxDate
-- Dont know why it just not work --Done
-- need maxDate [(a,b,c)] = (a,b,c)
maxDate :: (Ord a1, Ord a2, Ord a3) => [(a3, a2, a1)] -> (a3, a2, a1)
maxDate [(a,b,c)] = (a,b,c)
maxDate [] = error "wrong"
maxDate ((a,b,c):lessList) = biggerDate (a,b,c) (maxDate lessList)

-- 2. ascending
ascending :: Ord a => [a] -> Bool
ascending [] = True
ascending [_] = True
ascending (x:y:zs)  | x <= y = ascending (y:zs)
                    | otherwise = False

-- 3.a. insert
insert :: Int -> t2 -> [t2] -> [t2]
insert 0 b xs = b:xs
insert _ _ [] = []
--insert i b (x:xs) = x : insert (i-1) b xs
insert i b (x:xs)   | i > (length (x:xs)) = x:xs
                    | otherwise = x : insert (i-1) b xs

-- 3.b. insertEvery
insertEvery :: (Eq t, Num t) => t -> a -> [a] -> [a]
insertEvery n b xs = helper n xs where
     helper 0 xs = b:helper n xs
     helper _ [] = []
     helper j (x:xs) = x:helper (j-1) xs



-- 4.a. getHours
-- not done sum when repeated --Done
getSales :: (Num p, Eq t) => t -> [(t, p)] -> p
getSales _ [] = 0
getSales x ((a,b):xs)    | x == a = b + getSales x xs
                         | otherwise = getSales x xs


-- 4.b. sumSales
-- sum of repeated not work here --Done
sumSales:: (Num p)=> String -> String -> [(String,[(String,p)])] -> p
sumSales _ _ [] = 0
sumSales y x ((s,(a,b):xs):ss)     | y == s = getSales x ((a,b):xs) + sumSales y x ss
                                   | otherwise = sumSales y x ss

-- 5.a. split
split :: Eq a => a -> [a] -> [[a]]
split _ [] = []
split m iL =   let
          helper2 [] buf = (reverse buf):[]
          helper2 (x:xs) buf =     if x /= m then (helper2 (xs) (x:buf))
                                   else (reverse buf):(helper2 (xs) [])
               in helper2 iL []


-- 5.b. nSplit
nSplit :: (Ord a1, Num a1, Eq a2) => a2 -> a1 -> [a2] -> [[a2]]
nSplit _ _ [] = []
nSplit m n iL =     let 
               helper3 xs buf 0 = filter (not . null) ((reverse buf) : [xs])
               helper3 [] buf n = reverse buf : []
               helper3 (x:xs) buf n =   if x /= m then (helper3 xs (x:buf) n)
                                        else (reverse buf):(helper3 (xs) [] (n-1))
                    in helper3 iL [] n
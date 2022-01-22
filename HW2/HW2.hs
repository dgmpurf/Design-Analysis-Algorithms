module HW2
     where
import Data.Char ()



-- 1
{- (a) merge2 5%-}
merge2 :: [a] -> [a] -> [a]
merge2 [] [] = []
merge2 xs [] = xs
merge2 [] ys = ys
merge2 (x:xs) (y:ys) = x : y : (merge2 xs ys)
                         

{- (b) merge2Tail 10% -}
-- need helper function for tail, parameter only 2 not 3
merge2Tail :: [a] -> [a] -> [a]
merge2Tail l1 l2 = let
                         helper acc [] [] = reverse acc
                         helper acc xs [] = acc ++ xs
                         helper acc [] ys = acc ++ ys
                         helper acc (x:xs) (y:ys) = (helper (y:x:acc) xs ys)
                    in
                         helper [] l1 l2



{- (c) mergeN 5%-}
mergeN:: [[a]] -> [a]
mergeN [] =[]
--foldr f right to left, foldl f left to right
{-
     debug_foldr (map show [1..10]) "0"
     (1+(2+(3+(4+(5+(6+(7+(8+(9+(10+0))))))))))
     debug_foldl (map show [1..10]) "0"
     ((((((((((0+1)+2)+3)+4)+5)+6)+7)+8)+9)+10)
-}
mergeN (x:xs) = foldl merge2 x xs



-- 2
{- (a) removDuplicates 10% -}
removeDuplicates:: Eq a => [a] -> [a]
removeDuplicates iL = foldr (\x xs -> if x `elem` xs then xs else x:xs) [] iL


{- (b) count 5% -}
count :: Eq a => a -> [a] -> Int
count x xL = (length.filter (==x)) xL

{- (c) histogram 10% -}
histogram :: Eq a => [a] -> [(a, Int)]
histogram _ = []
--histogram il | x:(removeDuplicates il) /= [] = (x, count x (removeDuplicates il))


-- 3                
{- (a) concatAll 4% -}
concatAll :: [[String]] -> String
concatAll [] = ""
concatAll xL = foldr (++) "" (foldr (++) [] xL)



{- (b) concat2Either 9% -}               
data AnEither  = AString String | AnInt Int
                deriving (Show, Read, Eq)

concat2Either:: [[AnEither]] -> AnEither
concat2Either il =  foldr helper2 (AString []) (map (foldr helper2 (AString [])) il)
                    where helper2 (AnInt x) (AnInt y) = (AString ((show x) ++ (show y)))
                          helper2 (AnInt x) (AString y) = (AString ((show x) ++ y))
                          helper2 (AString x) (AString y) = (AString (x ++ y))



{- (c) concat2Str 6% -}  
concat2Str:: [[AnEither]] -> String             
concat2Str _ = ""
--concat2Str il =     foldr helper3 (AString []) (map (foldr helper3 (AString [])) il)
--                    where helper3 (AString x) y = (x ++ y)



-- 4 

data Op = Add | Sub | Mul | Pow
          deriving (Show, Read, Eq)

evaluate:: Op -> Int -> Int -> Int
evaluate Add x y =  x+y
evaluate Sub   x y =  x-y
evaluate Mul x y =  x*y
evaluate Pow x y = x^y

data ExprTree a = ELEAF a | ENODE Op (ExprTree a) (ExprTree a)
                  deriving (Show, Read, Eq)

{- (a) evaluateTree - 10% -}
evaluateTree :: ExprTree Int -> Int
evaluateTree (ELEAF x) = x
evaluateTree (ENODE op l r) = evaluate op (evaluateTree l) (evaluateTree r)




{- (b) printInfix - 10% -}
printInfix:: Show a => ExprTree a -> String
printInfix (ELEAF x) = show x
--printInfix (ENODE op l r) = ENODE (evaluate op (evaluateTree l) (evaluateTree r)) (printInfix l) (printInfix r)
--printInfix (ENODE op le ri) = ENODE (evaluate (show op) (show (evaluateTree le)) (show (evaluateTree ri))) (printInfix le) (printInfix ri)





{- (c) createRTree 12% -}
data ResultTree a  = RLEAF a | RNODE a (ResultTree a) (ResultTree a)
                     deriving (Show, Read, Eq)

createRTree :: ExprTree Int -> ResultTree Int
createRTree (ELEAF v) = RLEAF v
createRTree (ENODE op le ri) = RNODE (evaluate op (evaluateTree le) (evaluateTree ri)) (createRTree le) (createRTree ri)





-- 5
{-Sample trees 4% -}
-- createRTree
myTree1 = (ENODE Sub (ENODE Sub (ENODE Mul (ELEAF 6) (ELEAF 7)) (ELEAF 8)) (ENODE Sub (ELEAF 12) (ELEAF 8)))

-- evaluateTree
myTree2 = (RNODE 30 (RNODE 34 (RNODE 42 (RLEAF 6) (RLEAF 7)) (RLEAF 8)) (RNODE 4 (RLEAF 12) (RLEAF 8)))



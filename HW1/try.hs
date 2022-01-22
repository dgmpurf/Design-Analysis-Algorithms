x = 2
y = 3
main =  let z = x + y
        in print z

average a b = (a + b) / 2.0
f1 = average 3.0
result = f1 4.0

average2 a b = (a + b) / 2.0
a = average 3.0 4.0

myTuple = (True,1,"one")

nestedTuple = (True, (2,"two"), 2.0)

swap (x,y) = (y,x)

--mytuple1 = (1,2,3)
--(a,b,c) = mytuple1

max x y = if x >= y then x else y


signum x = if x < 0 then -1 else if x == 0 then 0 else 1

signum1 x    | x < 0 = -1
             | x == 0 = 0
             | otherwise = 1

-- 5.a. split
split :: Eq a => a -> [a] -> [[a]]
split _ [] = [[]]
split ch (strl:strlist)  | strl /= ch = split ch strlist
                         | strl == ch = [strl]:(split ch strlist)

-- 5.a. split
split' :: (Eq x) => [x] -> [x] -> [[x]]
split' _ [] = [[]]
split' del (front_list:rear_list) =
                                   if front_list `elem` del
                                   then []:rear_divide
                                   else (front_list:(head rear_divide)):(tail rear_divide)
                                   where rear_divide = split' del rear_list

biggerDate date1 date2 = if (date2 > date1) then date2 else date1

search :: (Eq a) => a -> [(a,b)] -> b
search _ [] = error "element not found"
search x ((a,b):xs) = if x == a then b else search x xs

-- 1.b. maxDate
maxDate :: (Ord a1, Ord a2, Ord a3) => [(a3, a2, a1)] -> (a3, a2, a1)
maxDate (x:xs) = (biggerDate x (maxDate xs))

-- 5.a. split
split :: Eq a => a -> [a] -> [[a]]
split _ [] = [[]]
split ch str = helper2 ch str where
     helper2 _ [] = [[]]

-- 3.b. insertEvery
insertEvery :: (Eq t, Num t) => t -> a -> [a] -> [a]
insertEvery n b xs = helper n xs where
     helper 0 xs = b:helper n xs
     helper _ [] = []
     helper j (x:xs) = x:helper (j-1) xs
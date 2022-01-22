tailallSquares acc [] = (reverse acc)
tailallSquares acc (x:xs) = (tailallSqueares (x*x):acc)xs)
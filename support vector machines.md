put a hyperplane to cut your data points in half. Things on one side are one class, things on the other side are the other.

But what if the data can't be easily split with a hyperplane? (for example, one category is 5 < x < 10, and the other category is y < 5,y > 10) Then use a kernel function to map the data to a higher dimension, where it can be split with some hyperplane (for example, you can map the above problem from value -> value squared, at which point the line f(x) = 15x - 50 will split it.)

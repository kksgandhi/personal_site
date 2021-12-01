NB(r, p) is the number of times you do thing with success probability p until you get r successes. (Sometimes p is probability of failure? Just depends on the package you are using)

So NB(5, 1/6) is the distribution of times you have to roll a 6 sided die before you get 5 6s

General case of the [[geometric distribution]] (geom(p) = NB(1, p))

to do [[hypothesis testing]] and see if two negative binomial distributions are different, I suggest generalized linear models in R, specifically glm.nb
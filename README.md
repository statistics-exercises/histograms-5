# Poisson random variable

Now that you know how to generate a multinomial trial using a while statement we can use this idea to do something more complicated.  In particular we can use what you just learned about using a while statement to generate a multinomial trial to write a function that generates Poisson random variables.  The probability mass function for a poisson random variable is:

![](https://render.githubusercontent.com/render/math?math=P(X=x)=\frac{\lambda^x}{x!}e^{-\lambda})

The poisson random variable can thus take any integer value between 0 and infinity.  Your task is to modify the function called `poisson` that takes the parameter `lam` so that this function returns a Poisson random variable.  To do this you will need to use an approach that is similar to the approach that you just used with the while statement to generate the multinomial trial. 

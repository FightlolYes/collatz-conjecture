Just trying to do some research regarding the Collatz Conjecture problem and using a Machine Learning algorithm to predict accurate patterns (I have no hope to make any groundbreaking discovery)

Still in Development stage :)

# What is Collatz Conjecture?

Collatz conjecture says that if you start with any positive integer, you’ll always end up in this loop. And you’ll probably ignore my warning about trying to solve it: It just seems too simple and too orderly to resist understanding. In fact, it would be hard to find a mathematician who hasn’t played around with this problem.

# How does it work?

Take 10 for example: 10 is even, so we cut it in half to get 5. Since 5 is odd, we triple it and add 1. Now we have 16, which is even, so we halve it to get 8, then halve that to get 4, then halve it again to get 2, and once more to get 1. Since 1 is odd, we triple it and add 1. Now we’re back at 4, and we know where this goes: 4 goes to 2 which goes to 1 which goes to 4, and so on. We’re stuck in a loop.

Here is a [video](https://www.youtube.com/watch?v=094y1Z2wpJg) about it :), or this [article](https://www.quantamagazine.org/why-mathematicians-still-cant-solve-the-collatz-conjecture-20200922/)
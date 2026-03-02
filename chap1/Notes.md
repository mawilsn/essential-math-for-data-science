# Chapter 1: Basic Math and Calculus Review


- Cartesian Systems

- Exponents and Logarithms

- Calculus:

	- Derivatives and Integers

  
## Number Theory

- Natural Numbers: 1, 2, 3. Positive 1 to infinity. No Zero

- Whole Numbers: Natural Numbers and Zero

- Integers: Positive, Negative numbers, and anything to do with whole numbers.

- Rational: Integers and numbers that can be expressed as a fraction

Natural --> Whole --> Integers --> Rational
Rational contains integers
Integers contains Whole
Whole Contains Natural
- Irrational: Cannot be expresses as fraction: $\sqrt{2}$, $\pi$, $e$
- Real Numbers: Rational and Irrational Numbers
- Complex and Imaginary: Negative Square Root

## Order of operations:
PEDMAS
Parenthesis, Exponents, Multiply, Divide, Add, Subtract

## Functions
- Define: Expressions that define a Relationship between two or more variables.
	- Input Variable
	- Output Variable also known as dependent Variable
When Dealing with real numbers ask yourself, how many _x_ values can we put through a function? and what type of step to take?

- Continuous Function: Every value of _x_ there is a _y_
- Cartesian Plane: A X-Y plane or coordinate plane
-  Curvilinear Function: continuous but curvy function.
![[media/Pasted image 20260301142953 1.png]]

How many independent Varialbes can you have?
- one or more 
How many Dependent Variables can you have?
- one

## Summations
$\sum_{i=1}^5(2i)$
this is just: $2(1) + 2(2) +  2(3)  + 2(4) + 2(5$)
## Exponents
- Multiplies a number a specific amount of times
$2^3 = 2*2*2=8$
- Product Rule: $y^a * y^b =$ y<sup>a+b</sup>
$x^2 +x^3 = x^{2+3} = x^5$
$x^2/x^5 = x^2 *x^{-5} = x^{2-5}= x^-3 = 1/x^3$

- Power Rule: When exponents are brought to a power you can multiply: $(x^a)^b = x^{a*b}$
$(x^2)^3 = x^6$

## Logarithms
- A functions that finds a power for a specific number and base
- "2 raise to what power gives you 8"
	- $2^x=8$
	- or $log_2(8)=x$
- MOst of the time whne no base is provided 10 is assumed.
- Data science mostly uses Euler's number



| Property            | equation                           |
| ------------------- | ---------------------------------- |
| Multiplication      | $log(a*b) = log(a) + log(b)$       |
| Division            | $log(a/b) = log(a)-log(b)$         |
| Exponentiation      | $log(a^n) = n*log(a)$              |
| Zero Exponentiation | $log(1)=0$                         |
| Inverse             | $log(x^{-1}) = log(1/x) = -log(x)$ |
## Euler's Number
$e$ or approx. 2.71828. Will talk more in other chapters
### Natural Logaritm
- When $e$ is used as a base it is called a natural logarithm

## Limits
Approaches a but never becomes the number
As the line approaches 0, it never reaches 0

![[media/Pasted image 20260301171837.png]]
$lim_{x->\infty}{1/x}=0$
As x approaches infinity, the funciton $1/x$ approaches 0, but never reach

- Euler's Number is like this to
- $lim_{x->\infty}(1+{1/n})^n=e$

## Derivatives
- Tells the slope of a funciton
-  useful to tell the rate of change at any point in a function
- Tangent Line: a straight line that touches the curve at any point
- Tangent line can be ywhere as long as it touches

![[media/Pasted image 20260301173136.png]]

How to estimate the tangent line at given X Value by create a line intersectio that x-value and a really close neighboring x-value.
Example

$f(x) = x^2; x_1=2 and x_2=2.1$
|x|f(x)|
|-|-|
|2|4|
|2.1|4.41|
$(4.41-4)/(2.1-2)=.41/.2=4.1$
If we keep going smaller, We will see $f(x)$ approaches 4.
We can also use derivative

- $\frac{d}{dx}x^n = nx^{n-1}$
- Example: $(\frac{d}{dx})x^2=2*x^{2-1}=2x$
- Derivate with respect to x is....

### Partial Derivative
- Derivate of functions that have multiple input variables
- Instead of a slope on one dimension, slopes with respect to multiple variables
 Example:
$f(x,y) = 2x^3 +3y^3$
$\frac{d}{dx}* \frac{d}{dy}$
$\frac{d}{dx}2x^3+3y^3=6x^2$
$\frac{d}{dy}2x^3+3y^3=9y^2$
Notice how the derivative denominator is the one that changes
Slopes are called "gradients" when dealing with multiple slopes.
## Chain Rule
Given function $y$ (with input variable $x$) composed into antoher function $z$ (with input from variable $y$). We can find the derivative of $z$ with respect to $x$ by multiplying the respective derivatives togethers
- $\frac{dz}{dx}=\frac{dz}{dy}*\frac{dy}{dx}$
- $y=x^2+1; z=y^3-2$
- $y=x^2+1$ What is $\frac{dy}{dx}$ (derivative of y with respect to x)
	- $\frac{dy}{dx}(x^2+1)= 2x$
- $z=y^3-2$ What is $\frac{dz}{dy}$ (derivative of z with respect to y).
	- $\frac{dz}{dy}(y^3-2)= 3y^2$
-  $\frac{dz}{dx}=\frac{dz}{dy}*\frac{dy}{dx}$
- $\frac{dz}{dx} = 2x*3y^2=6xy^2$
## Integrals
- opposite of derivatives
- Area under the curve for a given range
  
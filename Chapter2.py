Statistical Learning

X(inputs) is usually denoted by a subscript to distinguish them and they
go by many different names; predictors, independent variables,
features, or sometimes just variables.

often denoted as Y(output) are more called as output, ['response and dependent variables.']

Y = ƒ(X) + ε

ƒ(X) ; a fixed but unknown function of X1,...Xp, 
ε ; the random error term, which is independent of X and has a mean of 0.

∴ ƒ represents the systematic information that X provides about Y.

refer to page 17; fig 2.2

ƒ which is generally unknown (can be known when simulated)
- is the function of X and the line that shows the connection
  between X and Y. ( line)

ε is represented by the vertical lines between the  lines and 
point, also known as the error term.

['note: some errors are positive/negative depending on where they lie in ƒ']

```Statistical Learning refers to a set of approaches for estimating ƒ```

    > Why Estimate ƒ? <
    two main reasons; prediction and inference


----------------------------------------------------------------------------------
Prediction

'''
X(inputs) are available, but Y(output) cannot be easily obtained.
Since the error term averages to zero, we can predict Y using
'''

            Ŷ = f̂(X)

'''
where f̂ represents the estimate for ƒ and Ŷ represents the resulting 
prediction for Y.
'''

f̂ is often treated as a black box, in the sense that one is not 
typically concerned with the exact form of f̂, provided that
it yields the accurate predictions for Y.

f̂ ; represents estimate of ƒ -  line
Ŷ ; predicted values and represents the actual predictions from Y

Predictions have two errors namely; reducible & irreducible errors

['REDUCIBLE'] because you can improve the accuracy using f̂,
and ['IRREDUCIBLE'] where ε(error term) cannot be predicted using X
which therefore affects the accuracy of our predictions.

E(Y - Ŷ)^2 = E[ƒ(X) + ε - f̂(X)]^2
         = [ƒ(X) - f̂(X)]^2 + Var(ε)


E(Y - Ŷ)^2 ; Expected Value or average of the squared difference between the 
actual value of Y,
and Var(ε) represents the variance in association with the error term ε.

'''
note: keep in mind that the irreducible error will always provide and upper bound
on the accuracy of our prediction for Y. THE BOUND IS ALMOST ALWAYS UNKNOWN
'''

in short it is how accurate the prediction of the line is, whereas we use X
as basis for the line itself keeping in mind the error which comes from Y
and the data set. 

--------------------------------------------------------------------------------
`Interference`

understanding that way that Y is affected as X1, ... Xp change.(subscript 1, ..., p),
where we wish to estimate f(the line), but not necessarily with the predictions Y(Ŷ).

instead we want to understand the relatioship between X and Y, more specifically 
to understand how Y changes based on the function(X1,...,Xp).

['ƒ cannot be treated as a black box anymore, because we need to know its exact form']

in this section, we may want to ask the following questions:


    1Which predictors are associated with the response?
    2What is the relationship between the response and each predictor?
    3Can the relationship between Y and each predictor be adequately summarized using a 
      linear equation, or is the relationship more complicated?
    4Can the relationship between Y and each predictor be adequately summarized using a linear
      equation, or is the relationship more complicated?
    
  1 Attribute/Variable Selection due to its connection/association and relativity with Y.
  2 Some values of X may have an association with the increasing or decreasing of the value Y,
    depending on the complexity of the data itself.
  3 In some situations, it is desirable. but often the true relationship is more complicated
    that a linear model cant fit with an accurate representation of the relationship between
    the input and output variables.

  pg.20 `e.q.
  
  A company is interested in conducting a direct-marketing campaign
    to identify individuals who will respond positively to a mailing
    the demographic variables measures are served as the predictors X
    the response will serve as the outcome(positive or negative). Y

  1Which media contributed to sales?
  2Which media generated the biggest boost in sales?
  3How much increase in sales is associated with a given increase in TV ads?
  > `This situation falls into the interference paradigm.

  The modeling the brand of a product that a customer might purchase based on the variables 
    such as;
      price, store location, discount levels, competition price, and so forth.
    
  in this instance one might be really interested in how each of the individual variables
    affects the probability of purchase.

  1What effect will changing the price of a product have on sales?
  >  `This is an example of a modeling inteference.

  for both prediction and interference.
  In a real estate setting, one may seek to relate values of homes to inputs
  such as;
    crime rate, zoning, distance from a river, air quality, schools, income level of community,
    size of houses and so forth.
  
  in this instance one might be interested in how the individual input variables affect the prices
  
  1How much extra will a house be worth if it has a view of the river?
  > `This is an interference problem.`
  2Is this house under- or over-valued? 
  > `This is a prediction problem. `

  Interference; results pinning an independent variable
  Prediction; results are of continuous values e.q. price


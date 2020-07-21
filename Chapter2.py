Statistical Learning

X(inputs) is usually denoted by a subscript to destinguish them and they
go by many different names; predictors, independent variables,
features, or sometimes just variables.

often denoted as Y(output) are more often called as output, response and 
dependent variables.

Y = ƒ(X) + ε

ƒ(X) ; a fixed but unknown function of X1,...Xp, 
ε ; the random error term, which is independent of X and has a mean of 0.

∴ ƒ represents the systematic information that X provides about Y.

refer to page 17; fig 2.2
ƒ which is generally unknown (can be known when simulated)
- is the function of X and the line that shows the connection
  between X and Y.

ε is represented by the vertical lines, also known as the error term.

['note: some errors are positive/negative depending on where they lie in ƒ']


`Statistical Learning refers to a set of approaches for estimating ƒ`

    > Why Estimate ƒ? <
    two main reasons; prediction and inference

Prediction
'''
X(inputs) are available,but Y(output) cannot be easily obtained.
Since the error term averages to zero, we can predict Y using
'''
ŷ = f̂(X)

"""
where f̂ represents the estimate for ƒ and ŷ represents the resulting 
prediction for Y.
"""
f̂ is often treated as a black box, in the sense that one is not 
typically concerned with the exact form of f̂, provided that
it yields the accurate predictions for Y.

Predictions have two errors namely; reducible & irreducible errors

reducible because you can improve the accuracy using f̂,
and irreducible where ε(error term) cannot be predicted using X
which therefore affects the accuracy of our predictions.


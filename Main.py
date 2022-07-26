class Evaluate:
  """This class validates and evaluate postfix expression.
  Attributes:
      top: An integer which denotes the index of the element at the top of the stack currently.
      size_of_stack: An integer which represents the size of stack.
      stack: A List which acts as a Stack.
  """
    # Write your code here


  def __init__(self, size):
    """Inits Evaluate with top, size_of_stack and stack.
    Arguments:
      top:An integer which points to the top most element in the stack.
      size_of_stack: An integer which represents size of stack.
      stack: A list which maintians the elements of stack.
    """
    self.top = -1
    self.size_of_stack = size
    self.stack = []


  def isEmpty(self):
    
    """
    Check whether the stack is empty.
    Returns:
      True if it is empty, else returns False.
    """
    if set.top == -1:
      return True
    else:
      return False


  def pop(self):
    """
    Do pop operation if the stack is not empty.
    Returns:
      The data which is popped out if the stack is not empty.
    """
    if not self.isEmpty():
      self.stack.pop()


  def push(self, operand):
    """
    Push the operand to stack if the stack is not full.
    Arguments:
      operand: The operand to be pushed.
    """
    if self.top!= self.size_of_stack-1:
      self.stack.append(operand)


  def validate_postfix_expression(self, expression):
    """
    Check whether the expression is a valid postfix expression.
    Arguments:
      expression: A String which represents the expression to be validated.
    Returns:
      True if the expression is valid, else returns False.
    """
    number = 0
    operations = 0
    for el in expression:
      if el.isnumeric():
        number+=1
      else:
        operations +=1
    if operations == number - 1:
      return True
    else:
      return False


  def evaluate_postfix_expression(self, expression):
    """
    Evaluate the postfix expression
    Arguments:
      expression: A String which represents the the expression to be evaluated
    Returns:
      The result of evaluated postfix expression.
    """
    stack = []
    for i in expression:
      if i.isnumeric():
        stack.append(int(i))
      if len(stack)>=2:
        if i=='+':
          stack[-2] = stack[-2] + stack[-1]
          stack.pop()
        elif i=='-':
          stack[-2] = stack[-2] - stack[-1]
          stack.pop()
        elif i=='*':
          stack[-2] = stack[-2] * stack[-1]
          stack.pop()
        elif i=='/':
          stack[-2] = stack[-2] / stack[-1]
          stack.pop()
        elif i=='^':
          stack[-2] = stack[-2] ** stack[-1]
          stack.pop()
      return int(stack[-1])



# Do not change the following code
postfix_expression = input()  # Read postfix expression
tokens = postfix_expression.split()
evaluate = Evaluate(len(tokens))
if evaluate.validate_postfix_expression(tokens):
    print(evaluate.evaluate_postfix_expression(tokens))
else:
    print('Invalid postfix expression')

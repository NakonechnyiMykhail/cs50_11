# pip3 install sympy

#####################################################################
## example 1
#####################################################################
# from sympy import * 
  
# x = symbols('x') 
# expr = sin(x)/x; 
    
# print("Expression : {}".format(expr))  
      
# # Use sympy.limit() method  
# limit_expr = limit(expr, x, 0)   
      
# print("Limit of the expression tends to 0 : {}".format(limit_expr))

#####################################################################
## example 2
#####################################################################
# import sympy 
# from sympy import *

# x = symbols('x') 
# expr = sin(3 * x)/x; 
	
# print("Expression : {}".format(expr)) 
	
# # Use sympy.limit() method 
# limit_expr = limit(expr, x, 0) 
	
# print("Limit of the expression tends to 0 : {}".format(limit_expr)) 

#####################################################################
## example 3
#####################################################################
# from sympy import *

# x = symbols('x') 
# expr = 1 / x; 
	
# print("Expression : {}".format(expr)) 
	
# # Use sympy.limit() method 
# limit_expr = limit(expr, x, 0) 
	
# print("Limit of the expression tends to 0 : {}".format(limit_expr)) 

#####################################################################
## example 4
#####################################################################
# from sympy import *

# x = symbols('x') 
# expr = sqrt(x) 
	
# print("Expression : {}".format(expr)) 
	
# # Use sympy.limit() method 
# limit_expr = limit(expr, x, 0) 
	
# print("Limit of the expression tends to 0 : {}".format(limit_expr)) 

#####################################################################
## example 5
#####################################################################
# from sympy import *

# x = symbols('x') 
# expr = exp(-x); 
	
# print("Expression : {}".format(expr)) 
	
# # Use sympy.limit() method 
# limit_expr = limit(expr, x, 0) 
	
# print("Limit of the expression tends to 0 : {}".format(limit_expr)) 

#####################################################################
## example 6
#####################################################################
# from sympy import *

# x = symbols('x') 
# expr = 1 / x**2; 
	
# print("Expression : {}".format(expr)) 
	
# # Use sympy.limit() method 
# limit_expr = limit(expr, x, 0) 
	
# print("Limit of the expression tends to 0 : {}".format(limit_expr)) 

#####################################################################
## example 7
#####################################################################
# from sympy import *

# x = symbols('x') 
# expr = exp(x); 
	
# print("Expression : {}".format(expr)) 
	
# # Use sympy.limit() method 
# limit_expr = limit(expr, x, 0) 
	
# print("Limit of the expression tends to 0 : {}".format(limit_expr)) 


#####################################################################
## example 8
#####################################################################
# from sympy import *

# x = symbols('x') 
# expr = log(x) 
	
# print("Expression : {}".format(expr)) 
	
# # Use sympy.limit() method 
# limit_expr = limit(expr, x, 0) 
	
# print("Limit of the expression tends to 0 : {}".format(limit_expr)) 

#####################################################################
## example 9
#####################################################################
# from sympy import *

# x = symbols('x') 
# expr = (4 * (x**3) - 2 * x - 6) / (-x**3 + x**2 + 1) ;
	
# print("Expression : {}".format(expr)) 
	
# # Use sympy.limit() method 
# limit_expr = limit(expr, x, 2) # 0 -> 1 | or other a | oo
	
# print("Limit of the expression tends to 0 : {}".format(limit_expr)) 


#####################################################################
## example 10 ### as x tends to Zero
#####################################################################
# import numpy as np # pip3 install numpy
# from sympy import *
# import matplotlib.pyplot as plt # pip3 install matplotlib

# x = symbols('x')
# init_printing(use_unicode=True)

# expr = 1 / x; 
	
# print("Expression : {}".format(expr)) 
	
# # Use sympy.limit() method 
# limit_expr_plus = limit(expr, x, 0, '+') 
# limit_expr_minus = limit(expr, x, 0, '-') 
# print("Limit of the expression tends to +0 : {}".format(limit_expr_plus))
# print("Limit of the expression tends to -0 : {}".format(limit_expr_minus))
# plot(expr) 

#######
# t = np.linspace(0, 0.01, 0.5)
# plt.plot(t, expr, 'g^')  
# plt.xlabel('x')
# plt.ylabel('y')
# plt.title("Expression : {}".format(expr))
# plt.legend(["{}".format(expr)],    # список легенды
#             loc='upper left')    # положение легенды
# plt.show()

#####################################################################
## example 11 ### as x tends to Zero
#####################################################################
# import numpy as np # pip3 install numpy
# from sympy import *
# import matplotlib.pyplot as plt # pip3 install matplotlib

# x = symbols('x')
# init_printing(use_unicode=True)

# expr = sin(1 / x); 
	
# print("Expression : {}".format(expr)) 
	
# # Use sympy.limit() method 
# limit_expr_plus = limit(expr, x, 0, '+') 
# limit_expr_minus = limit(expr, x, 0, '-') 
# print("Limit of the expression tends to +0 : {}".format(limit_expr_plus))
# print("Limit of the expression tends to -0 : {}".format(limit_expr_minus))
# plot(expr) 

#####################################################################
## example 12 ### as x tends to Zero
#####################################################################
# import numpy as np # pip3 install numpy
# from sympy import *
# import matplotlib.pyplot as plt # pip3 install matplotlib

# x = symbols('x')
# init_printing(use_unicode=True)

# expr = cos(1 / x); 
	
# print("Expression : {}".format(expr)) 
	
# # Use sympy.limit() method 
# limit_expr_plus = limit(expr, x, 0, '+') 
# limit_expr_minus = limit(expr, x, 0, '-') 
# print("Limit of the expression tends to +0 : {}".format(limit_expr_plus))
# print("Limit of the expression tends to -0 : {}".format(limit_expr_minus))
# plot(expr) 

#####################################################################
## example 13 ### as x tends to Zero
#####################################################################
# import numpy as np # pip3 install numpy
# from sympy import *
# import matplotlib.pyplot as plt # pip3 install matplotlib

# x = symbols('x')
# init_printing(use_unicode=True)

# expr = x * sin(1 / x); 
	
# print("Expression : {}".format(expr)) 
	
# # Use sympy.limit() method 
# limit_expr_plus = limit(expr, x, 0, '+') 
# limit_expr_minus = limit(expr, x, 0, '-') 
# print("Limit of the expression tends to +0 : {}".format(limit_expr_plus))
# print("Limit of the expression tends to -0 : {}".format(limit_expr_minus))
# plot(expr) 

#####################################################################
## example 14 ### as x tends to Zero
#####################################################################
# import numpy as np # pip3 install numpy
# from sympy import *
# import matplotlib.pyplot as plt # pip3 install matplotlib

# x = symbols('x')
# init_printing(use_unicode=True)

# expr = x * cos(1 / x); 
	
# print("Expression : {}".format(expr)) 
	
# # Use sympy.limit() method 
# limit_expr_plus = limit(expr, x, 0, '+') 
# limit_expr_minus = limit(expr, x, 0, '-') 
# print("Limit of the expression tends to +0 : {}".format(limit_expr_plus))
# print("Limit of the expression tends to -0 : {}".format(limit_expr_minus))
# plot(expr) 


#####################################################################
## example 15 ### as x tends to Zero
#####################################################################
# import numpy as np # pip3 install numpy
# from sympy import *
# import matplotlib.pyplot as plt # pip3 install matplotlib

# x = symbols('x')
# init_printing(use_unicode=True)

# expr = x**2 * sin(1 / x); 
	
# print("Expression : {}".format(expr)) 
	
# # Use sympy.limit() method 
# limit_expr_plus = limit(expr, x, 0, '+') 
# limit_expr_minus = limit(expr, x, 0, '-') 
# print("Limit of the expression tends to +0 : {}".format(limit_expr_plus))
# print("Limit of the expression tends to -0 : {}".format(limit_expr_minus))
# plot(expr) 


#####################################################################
## example 16 ### as x tends to Zero
#####################################################################
# import numpy as np # pip3 install numpy
# from sympy import *
# import matplotlib.pyplot as plt # pip3 install matplotlib

# x = symbols('x')
# init_printing(use_unicode=True)

# expr = x**2 * cos(1 / x); 
	
# print("Expression : {}".format(expr)) 
	
# # Use sympy.limit() method 
# limit_expr_plus = limit(expr, x, 0, '+') 
# limit_expr_minus = limit(expr, x, 0, '-') 
# print("Limit of the expression tends to +0 : {}".format(limit_expr_plus))
# print("Limit of the expression tends to -0 : {}".format(limit_expr_minus))
# plot(expr) 

#####################################################################
## example 17 ### as x tends to Zero
#####################################################################
# import numpy as np # pip3 install numpy
# from sympy import *
# import matplotlib.pyplot as plt # pip3 install matplotlib

# x = symbols('x')
# init_printing(use_unicode=True)

# expr = sin(1 / x); 
	
# print("Expression : {}".format(expr)) 
	
# # Use sympy.limit() method 
# limit_expr_plus = limit(expr, x, 0, '+') 
# limit_expr_minus = limit(expr, x, 0, '-') 
# print("Limit of the expression tends to +0 : {}".format(limit_expr_plus))
# print("Limit of the expression tends to -0 : {}".format(limit_expr_minus))
# plot(expr) 


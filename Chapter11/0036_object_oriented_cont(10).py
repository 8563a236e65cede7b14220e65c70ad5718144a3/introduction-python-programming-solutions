"""
Operator Overloading and Magic Methods
    Operator Overloading is a specific case of polymorphism,
    where different operators have different implementations depending
    on their arguments.
    A class can implement certain operations that are invoked by special
    syntax (such as arithmetic operations or subscripting and slicing) by
    defining methods with special names called "Magic Methods"
    This is Python's solution to operator overloading, allowing classes
    to define their own behaviour.
    Magic Methods start with double underscores and end with double
    underscores.
    Provides a simple way to make objects behave like built-in types.
    Basic rule of operator overloading
        Whenever the meaning of an operator is not obviously clear and
        undisputed, it should not be overloaded and always stick to the
        operator's well-known semantics.

-------------------------------------------------------------------------
Binary Operators
-------------------------------------------------------------------------
+   __add__(self, other)            Invoked for Addition Operations
-   __sub__(self, other)            Invoked for Subtraction Operations
*   __mul__(self, other)            Invoked for Multiplication Operations
/   __truediv__(self, other)        Invoked for Division Operations
//  __floordiv__(self, other)       Invoked for Floor Division Operations
%   __mod__(self, other)            Invoked for Modulus Operations
**  __pow__(self, other[,modulo])   Invoked for Power Operations
<<  __lshift__(self, other)         Invoked for Left-Shift Operations
>>  __rshift__(self, other)         Invoked for Right-Shift Operations
&   __and__(self, other)            Invoked for Binary AND Operations
^   __xor__(self, other)            Invoked for Binary Exclusive-OR Operations
|   __or__(self, other)             Invoked for Binary OR Operations
-------------------------------------------------------------------------
Extended Operators
-------------------------------------------------------------------------
+=  __iadd__(self, other)            Invoked for Addition Assignment Operations
-=  __isub__(self, other)            Invoked for Subtraction Assignment Operations
*=  __imul__(self, other)            Invoked for Multiplication Assignment Operations
/=  __idiv__(self, other)            Invoked for Division Assignment Operations
//= __ifloordiv__(self, other)       Invoked for Floor Division Assignment Operations
%=  __imod__(self, other)            Invoked for Modulus Assignment Operations
**= __ipow__(self, other[,modulo])   Invoked for Power Assignment Operations
<<= __ilshift__(self, other)         Invoked for Left-Shift Assignment Operations
>>= __irshift__(self, other)         Invoked for Right-Shift Assignment Operations
&=  __iand__(self, other)            Invoked for Binary AND Assignment Operations
^=  __ixor__(self, other)            Invoked for Binary Exclusive-OR Assignment Operations
|=  __ior__(self, other)             Invoked for Binary OR Assignment Operations
-------------------------------------------------------------------------
Unary Operators
-------------------------------------------------------------------------
-       __neg__(self)       Invoked for Unary Negation Operator
+       __pos__(self)       Invoked for Unary Plus Operator
abs()   __abs__()           Invoked for built-in function abs()
~       __invert__(self)    Invoked for Unary Invert Operator
-------------------------------------------------------------------------
Conversion Operators
-------------------------------------------------------------------------
complex()   __complex__(self)   Invoked for built-in complex() function
int()       __int__(self)       Invoked for built-in int() function
long()      __long__(self)      Invoked for built-in long() function
float()     __float__(self)     Invoked for built-in float() function
oct()       __oct__()           Invoked for built-in oct() function
hex()       __hex__()           Invoked for built-in hex() function
-------------------------------------------------------------------------
Comparison Operators
-------------------------------------------------------------------------
<   __lt__(self, other)     Invoked for Less-Than Operations
<=  __le__(self, other)     Invoked for Less-Than or Equal-To Operations
==  __eq__(self, other)     Invoked for Equality Operations
!=  __ne__(self, other)     Invoked for Inequality Operations
>=  __ge__(self, other)     Invoked for Greater-Than or Equal-To Operations
>   __gt__(self, other)     Invoked for Greater-Than Operations
-------------------------------------------------------------------------

"""
    Nestor Ingles Jr
    CSC 121 (Python Programming) Notes


    x = input('Please enter a number')
    name = input('What is your name?')
    temperature = float(input('What is the temperature?'))

    print('Hello', first_name, last_name)
    
    print('The profit is $', format(profit, ',.2f')
    
    Faranheit to Celsius
    
    F = (9/5)*C + 32

    Compound Interest
    
    A = P(
    
    int(item)       You pass an argument to the int() function and it returns the argument's value converted to an int.

    float(item)     You pass an argument to the float() function and it returns the argument's value converted to a float.

    Ex.
    string_value = input('How many hours did you work? ')
    hours = int(string_value)
    
    Vs. (Better/Simpler)
    hours = int(input('How many hours did you work? '))
    
 
    pay_rate = float(input('What is your hourly pay rate? '))
    
    
    k = int(input())
    d = float(input())
    s = input()
    
    print(s, d, k)
    print(k, d, s)
    
    //  integer division    - Divides one number byanother and gives the result as a whole number
    %   Remainder           - Divides one number byanother and gives the remainder  
    **  Exponent            - Raises a number bya power
    
    Line continuation character     \
        
        result =    var1 * 2 + var2 * 3 + \
                    var3 * 4 + var4 * 5
    
    
    Instead of new line character:
    
        print('one', end=' ')
        
        print('one', 'two', 'three', sep='*')
        one*two*three
    
    Escape Characters
    
        \n  Causes output to be advanced tothe next line.
        \t  Causes output to skip over to the next horizontal tab position.
        \'  Causes a single quote mark to be printed
        \"  Causes a double quote mark to be printed
        \\  Causes a backlash charater to be printed
        
    Formating long floating point numbers
        
        print(format(12345.6789, '.2f'))
        
        12345.68
        
    Comma separators in numbers
        
        print(format(123456789.456, ',.2f'))
        
        123,456,789.46
        
    Field width
        
        print('The number is ', format(12345.6789, '12.2f'))
        
           The number is     12345.68
                    
    Formatting a floating-point numberas a percentage
        
        print(format(0.5, '%'))
        50.000000
        
        print(format(0.5, '.0%'))
        50%
        
    Turtle Graphics
    
        import turtle
        turtle.showturtle()
        turtle.forward(200)
        turtle.right(90)
        turtle.setheading(270)
        turtle.heading()    'Get turtles heading'
        turtle.circle(radius)
        turtle.dot()
        turtle.pensize(5)
        turtle.pencolor('red')
        turtle.bgcolor('gray')
        turtle.reset()
        turtle.clear()
        turtle.clearscreen()
        turtle.setup(640, 480)
        turtle.goto(0, 100)
        turtle.pos()    '(100.00, 150.00)'
        turtle.xcor()   '100'
        turtle.ycor()   '150'
        turtle.speed(0) 'disables speed/draws instantly'
        turtle.speed()  'Displays current speed'
        turtle.hideturtle()
        turtle.showturtle()
        turtle.write('text')
        turtle.begin_fill()
        turtle.end_fill()
        turtle.fillcolor('red')
        turtle.done() 'Prevents window fromclosing after the programend drawing'
        turtle.isdown() 'Deterines if pen is down or not'
        turtle.penup()
        turtle.isvisible()
        turtle.hideturtle()
        
        
        numCookies = int(input("Enter number of cookies:"))

#1.5 cups sugar/48 cookies = x cups sugar/numCookies
#1 cup butter/48 cookies = x cups butter/numCookies
# 2.75 cups flour/48 cookies = x cups flour/numCookies

cupsSugar = 1.5*numCookies/48
cupsButter = numCookies/48
cupsFlour = 2.75*numCookies/48

#You need x cups of sugar, x cups of butter, and x cups of flour.

print("You need %s cups of sugar, %s cups of butter, and %s cups of flour." % (cupsSugar, cupsButter, cupsFlour))


The if Statement

        if sales > 50000:
            bonus = 500
            commission_rate = 0.12
            print('You met your sales quota!')
        statement
        statement

        age = int(input('What is your age?'))
        
        x = 1
        y = 0
        x > y "True"
        y > x "False"
        
        if x > y:
            max = x
        else:
            max = y
            
        
        if age >= 65:
            senior_citizens = senior_citizens + 1
        else:
            non_seniors = non_seniors + 1
            
            
        if temperature > 98.6:
            fever = True
        else:
            fever = False
            
        Logical Operators
        and or not
            

        
        
        

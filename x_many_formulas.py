import sys

def main():
    # strip() to remove the new line char
    numbers = sys.stdin.readline().strip()
    total = 0
    for i in range(1 << (len(numbers) - 1)):
        remainders = ""
        for f in range(len(numbers)):
            remainders += numbers[f]
            if i & (1 << f) and f < len(numbers) - 1:
                remainders += '+'
        total += eval(remainders)   
    print(total)
           
main()

# Certainly! `eval()` is a built-in Python function that allows you to evaluate and execute Python expressions dynamically at runtime. It takes a string as input, interprets it as a Python expression, and then executes the expression, returning the result.

# Syntax:
# ```
# eval(expression, globals=None, locals=None)
# ```

# Parameters:
# - `expression`: A string containing a valid Python expression or statement.
# - `globals` (optional): A dictionary representing the global namespace. If provided, the evaluation will be done in this namespace. If not provided, the evaluation will be done in the current global namespace.
# - `locals` (optional): A dictionary representing the local namespace. If provided, the evaluation will be done in this namespace. If not provided, the evaluation will be done in the current local namespace.

# Working Principle:
# When you pass a string containing a Python expression to `eval()`, Python internally parses the string, compiles it into bytecode, and then executes the bytecode in the specified namespace (global or local). The result of the expression is returned as the return value of `eval()`.

# Example:
# ```python
# result = eval("3 + 5")
# print(result)  # Output: 8
# ```

# In this example, the string `"3 + 5"` is a valid Python expression. When `eval()` is called with this string, it evaluates the expression and returns the result, which is `8`.

# Use Cases and Caveats:
# 1. Arithmetic and Mathematical Expressions: You can use `eval()` to evaluate arithmetic expressions, mathematical functions, and complex calculations. However, be cautious with user inputs as `eval()` can execute arbitrary code, making it a potential security risk.

# 2. Simple Calculations: It can be useful for quick and simple calculations or when working with small-scale dynamic expressions in your code.

# Caveats and Security Concerns:
# Using `eval()` should be done with great caution, especially when dealing with user inputs or untrusted sources. Here are some considerations:

# 1. Security Risk: Since `eval()` executes any valid Python code, it can be exploited by malicious users to execute harmful or unintended code. Avoid using `eval()` with untrusted input to prevent code injection attacks.

# 2. Performance: `eval()` can be slower than other methods for evaluating expressions because it involves parsing and compiling the input string.

# 3. Debugging: It can be challenging to debug errors or exceptions that arise from using `eval()` since the code being executed is not directly visible in the source code.

# Alternative Approach:
# Instead of using `eval()`, consider using safer alternatives, such as parsing the input string manually or using specialized libraries for expression evaluation. For simple arithmetic calculations, Python provides built-in functions like `eval()` and `exec()`. However, for more complex use cases, you may want to explore dedicated libraries or safer parsing methods tailored to your specific needs.
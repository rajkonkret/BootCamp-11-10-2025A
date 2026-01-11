# niebezpieczne działania z kodem
x = 10
print(eval("x + 5"))  # 15

print(eval("sum([1,2,3])"))  # 6

print(eval("print('Hello from eval!')"))  # Hello from eval!

# nie uruchamiamy tego
# odpowiednik format c:
user_input = "__import_-('os').system('rm -rf /')"
# eval(user_input)

code = """
def greet(name):
    print(f'Hello: {name}!')
greet('Jan')
"""
exec(code)  # Hello: Jan!

# bezpieczniejsze podejscie - uzycie ast
import ast

user_input = "[1,2, {'a':3}]"
# tylko literały Pythona:
# str, bytes, numeryczne, tuple, list, dict, bool, None
result = ast.literal_eval(user_input)
print(result)  # [1, 2, {'a': 3}]

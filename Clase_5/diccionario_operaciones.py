operaciones = {
    "suma": lambda x, y: x + y,
    "resta": lambda x, y: x - y,
}

print(operaciones["suma"](10, 5))  # Debería imprimir 15
print(operaciones["resta"](20, 15)) # Deberia imprimir 5

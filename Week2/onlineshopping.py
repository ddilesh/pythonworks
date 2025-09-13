def calculate_bill(item_cost,quantity,tax=0.05,discount=0):
    total = (item_cost * quantity) + (item_cost * quantity * tax) - discount
    return total
if __name__ == "__main__":
  tpositionalargs=calculate_bill(500, 2)
  print(tpositionalargs)

  tkeyargs=calculate_bill(500, 2,tax=0.01,discount=5)
  print(tkeyargs)
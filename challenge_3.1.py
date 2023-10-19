def linear_search_product(productlist,target):
  indices=[]
  for index,product in enumerate(productlist):
    if product==target:
      indices.append(index)

  return indices


#product list
productlist=["cake","pizza","donuts","cake","pastery","chocolate","cake"]

#target item
target="cake"
result=linear_search_product(productlist,target)
print("The product indices are:",result)

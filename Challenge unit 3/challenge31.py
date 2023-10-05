def linear_search_product(product_list, target_product):
    indices = []
    
    for index, product in enumerate(product_list):
        if product == target_product:
            indices.append(index)
    
    return indices

# Example usage:
products = ["apple", "banana", "apple", "orange", "apple", "grape"]
target_product = "apple"
result = linear_search_product(products, target_product)

if result:
    print(f"{target_product} found at indices: {result}")
else:
    print(f"{target_product} not found in the list.")

def print_models(unprinted_designs, completed_models):
    while unprinted_designes:
        current_design = unprinted_designes.pop()
        print("Printing model: " + current_design)
        completed_models.append(current_design)

def show_completed(completed_models):
    print("\nThe following models have been printed: ")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designes = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designes, completed_models)
show_completed(completed_models)
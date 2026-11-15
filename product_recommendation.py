
# Product Recommendation System

customers = {
    "Amit": ["Laptop", "Mouse", "Keyboard"],
    "Bina": ["Laptop", "Mouse", "Headphones"],
    "Chetan": ["Phone", "Charger"],
    "Divya": ["Laptop", "Keyboard", "Monitor", "Webcam"]
}


# Function to find similarity between two customers
def similarity(p1, p2):

    s1 = set(p1)
    s2 = set(p2)

    common = len(s1 & s2)
    total = len(s1 | s2)

    if total == 0:
        return 0

    return common / total


# Function to find popular product
def find_popular():

    product_count = {}

    for items in customers.values():
        for item in items:

            if item in product_count:
                product_count[item] += 1
            else:
                product_count[item] = 1

    popular = max(product_count, key=product_count.get)

    return popular


# Main recommendation function
def recommend(name):

    if name == "":
        print("Name cannot be empty.")
        return

    if name not in customers:
        print("Customer not found.")
        return

    scores = {}

    for other in customers:

        if other != name:
            result = similarity(customers[name], customers[other])
            scores[other] = result

    # Display similarity scores
    print("\nSimilarity scores:")

    for person in sorted(scores, key=scores.get, reverse=True):
        print(person, ":", format(scores[person], ".2f"))

    # Find most similar customer
    best = max(scores, key=scores.get)

    if scores[best] == 0:
        print("No similar customers found.")
        print("Popular product:", find_popular())
        return

    print("Most similar customer:", best)

    # Recommend products not already purchased
    recommendation = []

    for item in customers[best]:

        if item not in customers[name]:
            recommendation.append(item)

    if recommendation:
        print("Recommended:", ", ".join(recommendation))
    else:
        print("No new products to recommend.")


# Taking customer name from user
customer_name = input("Recommend for: ").strip().title()

recommend(customer_name)

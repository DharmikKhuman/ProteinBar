from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/customize', methods=['GET', 'POST'])
def customize():
    if request.method == 'POST':
        data = request.form
        # Handle customization logic here
    return render_template('customize_products.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # Save feedback or inquiries
        pass
    return render_template('contact.html')



# In-memory cart (reset on server restart)
cart = []

@app.route('/')
@app.route('/customize_products', methods=['GET', 'POST'])
def customize_products():
    # Example list of ready-made protein bars
    protein_bars = [
        {
            "name": "Quest Nutrition Protein Bar",
            "protein": "20g",
            "carbs": "5g",
            "fats": "7g",
            "price": "$2.99",
            "flavor": "Chocolate Chip",
            "ingredients": "Whey Protein, Almonds, Stevia, Cocoa Butter",
            "image": "cat1.jpg"
        },
        {
            "name": "RXBAR Protein Bar",
            "protein": "12g",
            "carbs": "23g",
            "fats": "8g",
            "price": "$2.50",
            "flavor": "Peanut Butter",
            "ingredients": "Egg Whites, Dates, Peanuts, Sea Salt",
            "image": "cat2.jpg"
        },
        {
            "name": "Clif Bar",
            "protein": "10g",
            "carbs": "42g",
            "fats": "6g",
            "price": "$1.99",
            "flavor": "Oatmeal Raisin",
            "ingredients": "Rolled Oats, Raisins, Soy Protein, Brown Rice Syrup",
            "image": "cat3.jpg"
        },
        {
            "name": "ONE Protein Bar",
            "protein": "20g",
            "carbs": "8g",
            "fats": "7g",
            "price": "$2.75",
            "flavor": "Birthday Cake",
            "ingredients": "Milk Protein, Tapioca, Almonds, Natural Flavors",
            "image": "cat4.jpg"
        },
    ]

    if request.method == 'POST':
        # Add customized product to cart
        customized_bar = {
            "name": "Customized Protein Bar",
            "flour": request.form.get('flour'),
            "protein": request.form.get('protein') + "g",
            "flavor": request.form.get('flavor'),
            "sweetener": request.form.get('sweetener'),
            "price": "Custom"
        }
        cart.append(customized_bar)
        return redirect(url_for('customize_products'))

    return render_template('customize_products.html', protein_bars=protein_bars, cart=cart)

@app.route('/add_to_cart', methods=['POST'])
def add_to_cart():
    # Get the product details from the form submission
    product = {
        "name": request.form.get('name'),
        "flavor": request.form.get('flavor'),
        "protein": request.form.get('protein'),
        "carbs": request.form.get('carbs'),
        "fats": request.form.get('fats'),
        "price": request.form.get('price'),
        "ingredients": request.form.get('ingredients'),
    }
    # Add the product to the in-memory cart
    cart.append(product)
    return redirect(url_for('customize_products'))


@app.route('/cart')
def view_cart():
    return render_template('cart.html', cart=cart)


if __name__ == '__main__':
    app.run(debug=True)

from product import Product
from payment import Payment
from policyholder import Policyholder

print("=== PRODUCT DEMO ===")
product1 = Product(product_id=501, name="Galactic Shield Plan", price=599.99)
product1.display_product()

# Update product details
product1.update(new_name="Quantum Shield Plan", new_price=749.99)
product1.display_product()

# Suspend product
product1.suspend()
product1.display_product()

print("\n=== POLICYHOLDER DEMO ===")
policyholder1 = Policyholder(name="Leia Organa", policy_id="REB-1138")
policyholder1.display_details()

# Suspend and reactivate policyholder
policyholder1.suspend()
policyholder1.display_details()
policyholder1.reactivate()
policyholder1.display_details()

print("\n=== PAYMENT DEMO ===")
payment1 = Payment(amount=749.99, due_date="2125-06-01")
payment2 = Payment(amount=749.99, due_date="2125-07-01")

# Add payments to policyholder
policyholder1.payments.append(payment1)
policyholder1.payments.append(payment2)

# Display updated policyholder details with payments
policyholder1.display_details()

# Send reminder and apply penalty for unpaid payments
payment1.reminder()
payment1.penalty()

# Make a payment
payment1.pay()
print(f"Payment status: {payment1}")

# Check remaining unpaid payment
payment2.reminder()
payment2.penalty()

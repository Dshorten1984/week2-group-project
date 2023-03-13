class RentalProperty:
    def __init__(self, purchase_price, rental_income, operating_expenses):
        self.purchase_price = purchase_price
        self.rental_income = rental_income
        self.operating_expenses = operating_expenses
    
    def calculate_roi(self, holding_period, selling_price):
        total_income = sum(self.rental_income) * holding_period
        total_expenses = self.operating_expenses * holding_period
        net_income = total_income - total_expenses + selling_price - self.purchase_price
        roi = (net_income / self.purchase_price) * 100 / holding_period
        return roi


# Create a RentalProperty object
rp = RentalProperty(100000, [1000, 1200, 1300], 500)

# Calculate the ROI for a holding period of 5 years and a selling price of 120000
roi = rp.calculate_roi(5, 120000)

# Print the ROI
print(f"ROI: {roi:.2f}%")

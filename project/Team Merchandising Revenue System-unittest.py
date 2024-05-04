class Merchandise:
    def __init__(self, item_id, name, team_id, revenue, description):
        self.item_id = item_id
        self.name = name
        self.team_id = team_id
        self.revenue = revenue
        self.description = description

    def __str__(self):
        return f"Item ID: {self.item_id}, Name: {self.name}, Team ID: {self.team_id}, Revenue: {self.revenue}, Description: {self.description}"

class RevenueReport:
    def __init__(self):
        self.merchandise = {}

    def create(self, item_id, name, team_id, revenue, description):
        if item_id in self.merchandise:
            raise ValueError("Item ID already exists")
        self.merchandise[item_id] = Merchandise(item_id, name, team_id, revenue, description)

    def read(self, item_id):
        if item_id not in self.merchandise:
            raise ValueError("Item ID does not exist")
        return self.merchandise[item_id]

    def update(self, item_id, name=None, team_id=None, revenue=None, description=None):
        if item_id not in self.merchandise:
            raise ValueError("Item ID does not exist")
        item = self.merchandise[item_id]
        if name:
            item.name = name
        if team_id:
            item.team_id = team_id
        if revenue:
            item.revenue = revenue
        if description:
            item.description = description

    def delete(self, item_id):
        if item_id not in self.merchandise:
            raise ValueError("Item ID does not exist")
        del self.merchandise[item_id]

    def track_team_merchandise_sales(self, team_id):
        total_sales = 0
        for item in self.merchandise.values():
            if item.team_id == team_id:
                total_sales += item.revenue
        return total_sales

    def analyze_revenue_streams(self, revenue_data):
        total_revenue = sum(revenue_data)
        average_revenue = total_revenue / len(revenue_data) if revenue_data else 0
        max_revenue = max(revenue_data) if revenue_data else 0
        min_revenue = min(revenue_data) if revenue_data else 0
        return total_revenue, average_revenue, max_revenue, min_revenue

def create_team1_merchandise(db):
    db.create(1, "Computer", 1, 40000, "12th Gen computer")
    db.create(2, "Smartphone", 1, 30000, "100 megapixel camera")
    db.create(3, "Earbuds", 1, 2500, "Noise cancelation")
    db.create(4, "Television", 1, 60000, "4k HD display")

def create_team2_merchandise(db):
    db.create(5, "Cricket kit", 2, 15000, "MRF-Company")
    db.create(6, "Furniture", 2, 30000, "Wooden sofa set")
    db.create(7, "Bag", 2, 1800, "Flexible and lightweight")
    db.create(8, "Smart Watch", 2, 3000, "Health tracking")

# Unit tests
import unittest

class TestMerchandiseManager(unittest.TestCase):
    def setUp(self):
        self.db = RevenueReport()
        create_team1_merchandise(self.db)
        create_team2_merchandise(self.db)

    def test_create(self):
        self.db.create(9, "FootBall", 1, 3000, "Rubberized moulded")
        self.assertIn(9, self.db.merchandise)

    def test_read(self):
        item = self.db.read(1)
        self.assertEqual(item.name, "Computer")

    def test_update(self):
        self.db.update(1, name="Updated Computer", revenue=50000, description="Improved Generation")
        item = self.db.read(1)
        self.assertEqual(item.name, "Updated Computer")
        self.assertEqual(item.revenue, 50000)
        self.assertEqual(item.description, "Improved Generation")

    def test_delete(self):
        self.db.delete(2)
        self.assertNotIn(2, self.db.merchandise)

    def test_track_team_merchandise_sales(self):
        total_sales_team1 = self.db.track_team_merchandise_sales(1)
        print("\nCalculated total sales for team 1:", total_sales_team1)
        for item in self.db.merchandise.values():
            if item.team_id == 1:
                print(f"Item: {item.name}, Revenue: {item.revenue}")           
        self.assertEqual(total_sales_team1, 132500)  

    def test_analyze_revenue_streams(self):
        revenue_data = [item.revenue for item in self.db.merchandise.values()]
        total_revenue, average_revenue, max_revenue, min_revenue = self.db.analyze_revenue_streams(revenue_data)
        self.assertEqual(total_revenue, sum(revenue_data))
        self.assertEqual(average_revenue, sum(revenue_data) / len(revenue_data))
        self.assertEqual(max_revenue, max(revenue_data))
        self.assertEqual(min_revenue, min(revenue_data))

if __name__ == '__main__':
    unittest.main(verbosity=10)


class Merchandise:
    def __init__(self, item_id, item_name, description, team_id, revenue):
        self.item_id = item_id
        self.item_name = item_name
        self.description = description
        self.team_id = team_id
        self.revenue = revenue

    def __str__(self):
        return f"Item ID: {self.item_id}, Name: {self.item_name}, Description: {self.description}, Team ID: {self.team_id}, Revenue: {self.revenue}"

class RevenueReport:
    def __init__(self, revenue_data):
        self.revenue_data = revenue_data

    def track_team_merchandise_sales(self, team_id):
        team_sales = [item for item in self.revenue_data if item.team_id == team_id]
        total_sales = sum(item.revenue for item in team_sales)
        return total_sales

    def analyze_revenue_streams(self):
        revenue_streams = {}
        for item in self.revenue_data:
            if item.item_name in revenue_streams:
                revenue_streams[item.item_name] += item.revenue
            else:
                revenue_streams[item.item_name] = item.revenue
        return revenue_streams

class MerchandiseManager:
    def __init__(self):
        self.revenue_data = []

    def add_revenue(self, item_id, item_name, description, team_id, revenue):
        merchandise_item = Merchandise(item_id, item_name, description, team_id, revenue)
        self.revenue_data.append(merchandise_item)

    def update_revenue(self, item_id, new_revenue):
        for item in self.revenue_data:
            if item.item_id == item_id:
                item.revenue = new_revenue
                break

    def update_item_info(self, item_id, new_item_name, new_description):
        for item in self.revenue_data:
            if item.item_id == item_id:
                item.item_name = new_item_name
                item.description = new_description
                break

    def delete_revenue(self, item_id):
        self.revenue_data = [item for item in self.revenue_data if item.item_id != item_id]

    def get_revenue_data(self):
        return self.revenue_data


manager = MerchandiseManager()
def add_revenue_data():
    item_id = int(input("Enter item ID: "))
    item_name = input("Enter item name: ")
    description = input("Enter item description: ")
    team_id = int(input("Enter team ID: "))
    revenue = float(input("Enter revenue: "))
    manager.add_revenue(item_id, item_name, description, team_id, revenue)
    print("Revenue data added successfully.")

def update_item_info_and_revenue():
    item_id = int(input("Enter item ID to update name, description, and revenue: "))
    new_item_name = input("Enter new item name: ")
    new_description = input("Enter new item description: ")
    new_revenue = float(input("Enter new revenue: "))
       
    manager.update_item_info(item_id, new_item_name, new_description)
    manager.update_revenue(item_id, new_revenue)
    print("Item name, description, and revenue updated successfully.")

def delete_item():
    item_id = int(input("Enter item ID to delete: "))
    manager.delete_revenue(item_id)
    print("Item deleted successfully.")

add_more = input("Do you want to add revenue data? (yes/no): ").lower()
while add_more == "yes":
    add_revenue_data()
    add_more = input("Do you want to add more revenue data? (yes/no): ").lower()

update_info_revenue_more = input("Do you want to update any item name, description, and revenue? (yes/no): ").lower()
while update_info_revenue_more == "yes":
    update_item_info_and_revenue()
    update_info_revenue_more = input("Do you want to update more item name, description, and revenue? (yes/no): ").lower()

delete_more = input("Do you want to delete any item? (yes/no): ").lower()
while delete_more == "yes":
    delete_item()
    delete_more = input("Do you want to delete more items? (yes/no): ").lower()

report = RevenueReport(manager.get_revenue_data())
team1_sales = report.track_team_merchandise_sales(1)
team2_sales = report.track_team_merchandise_sales(2)
total_sales = team1_sales + team2_sales
revenue_streams = report.analyze_revenue_streams()

if team1_sales > team2_sales:
    winning_team = "Team 1"
    winning_sales = team1_sales
else:
    winning_team = "Team 2"
    winning_sales = team2_sales

with open("team_revenue_report.txt", "w") as file:
    file.write("Team 1 Total Sales: $%d\n" % team1_sales)
    file.write("Team 2 Total Sales: $%d\n" % team2_sales)
    file.write("Total Revenue Generated: $%d\n" % total_sales)
    file.write("Winning Team: %s\n" % winning_team)
    file.write("\nRevenue Streams for Team 1:\n")
    team1_revenue_streams = [item for item in manager.get_revenue_data() if item.team_id == 1]
    for item in team1_revenue_streams:
        file.write("%s: $%d\n" % (item.description, item.revenue))

    file.write("\nRevenue Streams for Team 2:\n")
    team2_revenue_streams = [item for item in manager.get_revenue_data() if item.team_id == 2]
    for item in team2_revenue_streams:
        file.write("%s: $%d\n" % (item.description, item.revenue))

print("Report has been updated and saved to 'team_revenue_report.txt'")

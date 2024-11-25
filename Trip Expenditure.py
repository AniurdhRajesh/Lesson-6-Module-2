def calculate_total_trip_expenditure():
    hotel_cost_per_day = float(input("Enter the hotel cost per day: "))
    number_of_days = int(input("Enter the number of days stayed: "))
    plane_cost = float(input("Enter the plane ticket cost: "))
    vehicle_rental_cost = float(input("Enter the vehicle rental cost: "))
    
    total_hotel_cost = hotel_cost_per_day * number_of_days
    total_expenditure = total_hotel_cost + plane_cost + vehicle_rental_cost
    
    print("Total trip expenditure: $", total_expenditure)

calculate_total_trip_expenditure()

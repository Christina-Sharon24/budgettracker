def allocate_monthly_expenses(monthly_income, expense_categories):
    """
    Allocates a given monthly income across a list of expense categories, 
    returning a dictionary with each category and its allocated amount. 
    
    Args:
        monthly_income: The total monthly income. 
        expense_categories: A list of dictionaries, where each dictionary contains 
                            an expense category name and its desired percentage allocation. 
    
    Returns:
        A dictionary where keys are expense categories and values are allocated amounts. 
    """
    
    allocated_expenses = {}
    total_allocation = 0  
    
    # Calculate total percentage allocation 
    for category in expense_categories:
        total_allocation += category["percentage"] 
    
    # Allocate funds based on percentages 
    for category in expense_categories:
        allocated_amount = (category["percentage"] / total_allocation) * monthly_income
        allocated_expenses[category["name"]] = allocated_amount
    
    return allocated_expenses 

# Example usage
income = 3000 
expenses = [
    {"name": "Housing", "percentage": 35}, 
    {"name": "Food", "percentage": 20}, 
    {"name": "Transportation", "percentage": 15}, 
    {"name": "Utilities", "percentage": 10}, 
    {"name": "Entertainment", "percentage": 20}
]

allocated_budget = allocate_monthly_expenses(income, expenses) 
print(allocated_budget) 
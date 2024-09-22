# Dictionary comprehensions - Практика

employee_projects = {
    "Alice": {"project_1", "project_3"},
    "Bob": {"project_2"},
    "Charlie": {"project_1", "project_2", "project_3"},
    "David": set(),  # Незагруженный сотрудник
    "Eve": {"project_3"}
}


employee_projects_quantity = {
    employee: len(projects)
    for employee, projects in employee_projects.items()
}
print(employee_projects_quantity)


employee_projects_mates = {
    employee: {
        mate
        for mate, mate_projects in employee_projects.items()
        if mate != employee and mate_projects.intersection(projects)
    }
    for employee, projects in employee_projects.items()
}
print(employee_projects_mates)


employee_without_work = {
    employee: projects
    for employee, projects in employee_projects.items()
    if not projects
}
print(employee_without_work)


unique_projects = {
    project
    for projects in employee_projects.values()
    for project in projects
}
print(unique_projects)
project_employees = {
    project: {
        employee
        for employee, projects in employee_projects.items()
        if project in projects
    }
    for project in unique_projects
}
print(project_employees)

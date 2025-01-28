import requests

BASE_URL = "http://localhost:8080/courses"

def list_courses():
    """Fetch all courses from the API."""
    response = requests.get(BASE_URL)
    if response.status_code == 200:
        courses = response.json()
        for course in courses:
            print(f"ID: {course['id']}, Title: {course['title']}, Price: ${course['price']}")
    else:
        print("Failed to fetch courses. Status code:", response.status_code)

def get_course(course_id):
    """Fetch a specific course by ID."""
    response = requests.get(f"{BASE_URL}/{course_id}")
    if response.status_code == 200:
        course = response.json()
        print(f"ID: {course['id']}")
        print(f"Title: {course['title']}")
        print(f"Description: {course['description']}")
        print(f"Price: ${course['price']}")
        print(f"Instructor: {course['instructor']}")
    else:
        print("Course not found. Status code:", response.status_code)

def create_course(title, description, workload, price, instructor, published, category, image_url):
    """Create a new course."""
    course_data = {
        "title": title,
        "description": description,
        "workload": workload,
        "price": price,
        "instructor": instructor,
        "published": published,
        "category": category,
        "imageUrl": image_url
    }
    response = requests.post(BASE_URL, json=course_data)
    if response.status_code == 200:
        print("Course created successfully:", response.json())
    else:
        print("Failed to create course. Status code:", response.status_code)

def update_course(course_id, title, description, workload, price, instructor, published, category, image_url):
    """Update an existing course."""
    course_data = {
        "title": title,
        "description": description,
        "workload": workload,
        "price": price,
        "instructor": instructor,
        "published": published,
        "category": category,
        "imageUrl": image_url
    }
    response = requests.put(f"{BASE_URL}/{course_id}", json=course_data)
    if response.status_code == 200:
        print("Course updated successfully:", response.json())
    else:
        print("Failed to update course. Status code:", response.status_code)

def delete_course(course_id):
    """Delete a course."""
    response = requests.delete(f"{BASE_URL}/{course_id}")
    if response.status_code == 204:
        print("Course deleted successfully.")
    else:
        print("Failed to delete course. Status code:", response.status_code)

if __name__ == "__main__":
    while True:
        print("\nCourse Management Client")
        print("1. List all courses")
        print("2. Get course by ID")
        print("3. Create a new course")
        print("4. Update a course")
        print("5. Delete a course")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            list_courses()
        elif choice == "2":
            course_id = input("Enter course ID: ")
            get_course(course_id)
        elif choice == "3":
            title = input("Title: ")
            description = input("Description: ")
            workload = int(input("Workload (hours): "))
            price = float(input("Price: "))
            instructor = input("Instructor: ")
            published = input("Published (true/false): ").lower() == "true"
            category = input("Category: ")
            image_url = input("Image URL: ")
            create_course(title, description, workload, price, instructor, published, category, image_url)
        elif choice == "4":
            course_id = input("Enter course ID to update: ")
            title = input("Title: ")
            description = input("Description: ")
            workload = int(input("Workload (hours): "))
            price = float(input("Price: "))
            instructor = input("Instructor: ")
            published = input("Published (true/false): ").lower() == "true"
            category = input("Category: ")
            image_url = input("Image URL: ")
            update_course(course_id, title, description, workload, price, instructor, published, category, image_url)
        elif choice == "5":
            course_id = input("Enter course ID to delete: ")
            delete_course(course_id)
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid option. Please try again.")

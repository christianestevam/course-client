## Client - Course Management Client

### **Description**
This is a Python-based client to interact with the Course Management API. It provides a command-line interface for performing CRUD operations on courses.

---

### **Features**
- List all courses.
- View details of a specific course.
- Add a new course.
- Update an existing course.
- Delete a course.

---

### **Requirements**
- Python 3.8+
- `requests` library

---

### **Setup Instructions**

#### **1. Clone the Repository**
```bash
git clone <git@github.com:christianestevam/course-client.git>
cd client
```

#### **2. Install Dependencies**
Install the required Python packages:
```bash
pip install -r requirements.txt
```

The `requirements.txt` file should contain:
```plaintext
requests
```

---

### **Usage**
Run the Python client using:
```bash
python client.py
```

You will see a menu with the following options:
1. List all courses
2. Get course by ID
3. Create a new course
4. Update a course
5. Delete a course
6. Exit

---

### **API Configuration**
Ensure the `base_url` in `client.py` matches your backend URL:
```python
base_url = 'http://localhost:8080/courses'
```

---
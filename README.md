

````markdown
# Donations Portal

The **Donations Portal** is a web-based application designed to streamline the donation process between **donors**, **administrators**, and **recipients** in a transparent and organized manner. It allows users to make and manage donations across categories like **education**, **infrastructure**, and **food**.

---

## 🌐 Features

### 🔹 Donor Module

* Browse and contribute to verified donation campaigns.
* Choose donation categories (education, food, infrastructure, etc.).
* Track donation status.
* Get email notifications on request approvals.
* Raise and resolve queries with admin support.

### 🔹 Admin Module

* Approve or reject donor and recipient requests.
* Manage and publish donation campaigns.
* Respond to donor queries.
* Ensure verification using Aadhaar and ration card uploads.

### 🔹 Recipient Module

* Submit help requests via a detailed form.
* Upload required documents (Aadhaar, ration card).
* Get email updates on approval/rejection of the request.

---

## 💻 Tech Stack

* **Frontend**: HTML, CSS, JavaScript, Bootstrap
* **Backend**: Python, Django
* **Database**: SQLite
* **Email Support**: SMTP (Django Email Backend)

---

## 🚀 Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Mounika9929/Donations-Portal.git
   cd Donations-Portal
````

2. Create a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install Django (if not already installed):

   ```bash
   pip install django
   ```

4. Apply migrations:

   ```bash
   python manage.py migrate
   ```

5. Run the server:

   ```bash
   python manage.py runserver
   ```

6. Open in browser:
   `http://127.0.0.1:8000/`

---

## 📁 File Structure

```
DonationsProject/
├── DonationsApp/
│   ├── templates/
│   ├── static/
│   ├── forms.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
├── DonationsProject/
│   ├── settings.py
│   ├── urls.py
├── db.sqlite3
├── manage.py
```

---

## 📧 Email Configuration

In `settings.py`, configure your email settings:

```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your-email@gmail.com'
EMAIL_HOST_PASSWORD = 'your-email-password'
```

> ⚠️ **Note:** For production, store credentials securely using environment variables or a `.env` file.

---

## 📜 License

This project is open-source and available under the [MIT License](LICENSE).

---

## 🙋‍♀️ Contact

For queries, contact the developer: **[mounikaundela999@gmail.com](mailto:mounikaundela999@gmail.com)**
GitHub Repo: [https://github.com/Mounika9929/Donations-Portal](https://github.com/Mounika9929/Donations-Portal)

---

```

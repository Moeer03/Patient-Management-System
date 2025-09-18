# 🩺 Patient Management System (FastAPI + Streamlit)

A **simple yet powerful Patient Management System** built with:
- **FastAPI** → for backend APIs  
- **Streamlit** → for interactive frontend UI  
- **Pydantic** → for data validation and computed fields  
- **JSON storage** → for simplicity (no database required)

This project allows you to **view, create, update, sort, and delete patient records** — all from a clean web UI.

---

## 🚀 Features

✅ **Backend (FastAPI)**
- CRUD APIs for patients (Create, Read, Update, Delete)
- BMI and health verdict computed dynamically
- Data stored in `patients.json`
- Validation using Pydantic models

✅ **Frontend (Streamlit)**
- Simple, user-friendly UI
- Sidebar navigation for all actions
- JSON response viewer for quick debugging
- Error handling + success notifications

✅ **Single-Command Run**
- A `run_app.py` script launches **both backend and frontend together** — no need to manually run two terminals.

---

## 📂 Project Structure

```
📦 patient-management-system
 ┣ 📜 main.py           # FastAPI backend
 ┣ 📜 frontend.py       # Streamlit frontend
 ┣ 📜 run_app.py        # Launcher for backend + frontend
 ┣ 📜 patients.json     # JSON "database"
 ┣ 📜 requirements.txt  # Dependencies
 ┣ 📜 LICENSE           # MIT License
 ┗ 📜 README.md         # This file
```

---

## 🛠️ Installation & Setup

### 1️⃣ Clone the Repo
```bash
git clone https://github.com/your-username/patient-management-system.git
cd patient-management-system
```

### 2️⃣ Create & Activate Virtual Environment
**Windows (PowerShell):**
```powershell
python -m venv venv
.env\Scriptsctivate
```

**Linux / Mac:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Run the App (Backend + Frontend Together 🚀)
```bash
python run_app.py
```

Streamlit will open automatically in your browser at `http://localhost:8501`.

---

## 🖼️ Screenshots

| Homepage | Create Patient |
|---------|---------------|
| ![Home](https://via.placeholder.com/400x200?text=Home+Page) | ![Create](https://via.placeholder.com/400x200?text=Create+Patient) |

*(Replace placeholders with actual screenshots of your running app)*

---

## 📡 API Endpoints (Backend)

| Method | Endpoint | Description |
|-------|----------|-------------|
| `GET` | `/` | Health check |
| `GET` | `/view` | View all patients |
| `GET` | `/patient/{patient_id}` | Get details of a patient |
| `GET` | `/sort?sort_by=bmi&order=asc` | Sort patients by `height`, `weight`, or `bmi` |
| `POST` | `/create` | Create a new patient |
| `PUT` | `/edit/{patient_id}` | Update existing patient |
| `DELETE` | `/delete/{patient_id}` | Delete patient |

---

## 📦 Requirements

Add this to your `requirements.txt`:

```
fastapi
uvicorn
streamlit
pydantic
requests
```

Then install with:
```bash
pip install -r requirements.txt
```

---

## 📝 License

This project is licensed under the **MIT License** – see the [LICENSE](LICENSE) file for details.

---

## 🙌 Contributing

PRs are welcome! If you have ideas to improve this project (UI, data validation, performance), feel free to fork and submit a pull request.

---

## ⭐ Support

If you find this helpful, **star ⭐ this repo** to support the project!

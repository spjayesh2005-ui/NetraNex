# NetraNexAI

Explainable AI prototype for Diabetic Retinopathy Screening in Rural India.

> **Important:** This repository is a demonstration/prototype. The included prediction service is a mock/demo classifier and must not be used for medical diagnosis or clinical decisions.

## Features
- Fundus image upload
- Image preview
- Demo DR severity classification
- Risk level display
- Explainability/heatmap placeholder
- Rural/low-bandwidth friendly UI
- Python Flask API
- GitHub-ready project structure

## Run locally

### Backend
```bash
cd backend
python -m venv venv
# Windows:
venv\Scripts\activate
# macOS/Linux:
# source venv/bin/activate

pip install -r requirements.txt
python app.py
```

Backend runs at `http://127.0.0.1:5000`.

### Frontend
Open `frontend/index.html` directly, or serve it with a local static server.

The frontend expects the backend at `http://127.0.0.1:5000`.

## Project structure
```text
NetraNexAI/
├── frontend/
├── backend/
├── model/
├── docs/
├── .gitignore
└── README.md
```

## Replacing the demo model
Put your trained model inside `model/` and replace the demo logic in `backend/services/prediction.py` with your validated inference pipeline.

## GitHub
```bash
git init
git add .
git commit -m "Initial commit - NetraNexAI"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/NetraNexAI.git
git push -u origin main
```

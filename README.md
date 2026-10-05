# Apple Sports & Apple Apps/Services Dashboard Clone <img src="https://ibb.co" width="20" height="20" style="vertical-align: middle;"> <img src="https://ibb.co" width="20" height="20" style="vertical-align: middle;"> <img src="https://ibb.co" width="20" height="20" style="vertical-align: middle;">
---

An interactive web dashboard clone inspired by [dieterich-lab/AppleDashboard](https://github.com/dieterich-lab/AppleDashboard) to parse and visualize workout telemetry and physical sports data exported from the Apple Watch and Apple Health ecosystem.

## 📁 Repository Structure
* `app.py`: Main interactive Dash application and layout.
* `parser.py`: Service backend script responsible for parsing `export.xml`.
* `Pipfile`: Strict dependency management configuration.
* `Dockerfile` & `docker-compose.yml`: Containerized production and dev environment setup.
* `.import/`: Folder destination where your `export.xml` file should be placed.

---

## 🚀 Getting Started

### Option 1: Running with Docker (Recommended)
Make sure you have Docker and Docker Compose installed, then execute:
```bash
docker-compose up --build
```
Once initialized, open your browser and navigate to `http://localhost:8050`.

### Option 2: Running Locally with Pipenv
If you prefer running natively on your machine:
```bash
# Install pipenv if you haven't already
pip install pipenv

# Install project dependencies
pipenv install

# Spawn the virtual environment shell
pipenv shell

# Execute the application
python app.py
```

## 📊 Importing Your Apple Watch Data
1. Open the **Health** app on your iPhone.
2. Tap your profile picture in the top right corner.
3. Select **"Export Health Data"** at the bottom.
4. Unzip the file and move `export.xml` into the `.import/` directory of this project.

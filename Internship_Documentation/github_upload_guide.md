# Step-by-Step GitHub Upload & Sharing Guide

**Project**: ShadowFox Data Analyst Internship  
**Repository Name**: `ShadowFox_Data_Analyst_Internship`  
**Location**: `C:\Users\keert\.gemini\antigravity-ide\scratch\ShadowFox_Data_Analyst_Internship`  

---

## 1. Prerequisites
- A free **GitHub account** ([github.com](https://github.com)).
- **Git** installed on your Windows machine. (If not installed, download from [git-scm.com](https://git-scm.com)).

---

## 2. Step-by-Step Git Commands

Open **PowerShell** or **Command Prompt**, and run the following exact sequence of commands:

### Step 1: Navigate to the Internship Workspace
```powershell
cd "C:\Users\keert\.gemini\antigravity-ide\scratch\ShadowFox_Data_Analyst_Internship"
```

### Step 2: Initialize Git Repository
```powershell
git init
```

### Step 3: Configure Your Git Identity (If Not Already Done)
```powershell
git config user.name "Your Name"
git config user.email "your.email@example.com"
```

### Step 4: Stage All Files
```powershell
git add .
```

### Step 5: Verify Staged Files
```powershell
git status
```
*(You will see all three project folders, data files, scripts, SQL, DAX, charts, and READMEs staged in green.)*

### Step 6: Create the Initial Commit
```powershell
git commit -m "Complete ShadowFox Data Analyst Internship: Beginner, Intermediate, and Advanced Projects"
```

---

## 3. Creating & Linking the Remote Repository on GitHub

1. Log in to [GitHub](https://github.com).
2. Click the **+** (plus icon) in the top-right corner > select **New repository**.
3. **Repository Settings**:
   - **Repository Name**: `ShadowFox_Data_Analyst_Internship`
   - **Description**: `Official ShadowFox Data Analyst Internship Portfolio: Small Business Sales (Excel), Customer Analytics & RFM (SQL/Python), and Executive BI Dashboard (Power BI/DAX).`
   - **Visibility**: Select **Public** (Crucial: ShadowFox mentors must be able to view your repo).
   - **Do NOT check** "Add a README file", ".gitignore", or "license" (we have already created all of them).
4. Click **Create repository**.
5. Copy the remote URL displayed on the next screen: `https://github.com/Keerthanagowda42/ShadowFox_Data_Analyst_Internship.git`.

---

## 4. Pushing Local Code to GitHub

Run the following commands in your PowerShell terminal:

```powershell
# Rename default branch to main
git branch -M main

# Link your local repo to GitHub
git remote add origin https://github.com/Keerthanagowda42/ShadowFox_Data_Analyst_Internship.git

# Push the code
git push -u origin main
```

---

## 5. Google Drive Video Sharing Instructions

1. Record your 3–5 minute presentation using Loom, Zoom, or OBS following `Internship_Documentation/video_presentation_script.md`.
2. Save the final `.mp4` video on your computer.
3. Open [Google Drive](https://drive.google.com).
4. Drag and drop your video file into Google Drive.
5. Once uploaded:
   - Right-click the video file > Select **Share** > **Share**.
   - Under **General access**, change from *Restricted* to **"Anyone with the link"**.
   - Ensure the permission dropdown on the right is set to **"Viewer"**.
   - Click **Copy link**.
6. Test the copied link in an **Incognito / Private browser window** to ensure anyone can view it without needing login approval.

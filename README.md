# 🚀 Smart File Automator (GUI Version)

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GitHub Stars](https://img.shields.io/github/stars/vthish/smart-file-automator?style=social)](https://github.com/vthish/smart-file-automator)
[![Release](https://img.shields.io/github/v/release/vthish/smart-file-automator?include_prereleases)](https://github.com/vthish/smart-file-automator/releases)

A lightweight and efficient Python-based desktop application that automatically organizes your messy folders. It sorts files and sub-folders into categorized directories based on their extensions.

---

## 🛠️ New Features
* **🖥️ User-Friendly GUI:** No more terminal commands! Use the interactive interface to select folders.
* **📂 Full Organization:** Now handles both **Files** and **Sub-folders**.
* **⚡ Portable Executable (.exe):** Run it directly on Windows without installing Python.
* **🛡️ Error Handling:** Smoothly skips locked files (like those syncing with OneDrive).
* **🗂️ Categorization:** Groups items into Images, Documents (including .sql), Videos, Audio, and Archives. Unknown types move to "Others".

---

## 📂 How It Works
Select any directory (like your Downloads or Desktop), and with one click, it transforms from a mess into this:

```text
📁 Selected Folder
 ┣ 📁 Images (.jpg, .png, .gif, .webp)
 ┣ 📁 Documents (.pdf, .docx, .txt, .xlsx, .sql)
 ┣ 📁 Videos (.mp4, .mkv, .mov)
 ┣ 📁 Audio (.mp3, .wav)
 ┣ 📁 Archives (.zip, .rar, .7z)
 ┗ 📁 Others (Folders & unidentified files)

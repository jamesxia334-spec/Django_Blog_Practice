# 🧠 Django Blog Practice

This is a small Django practice project based on exercises from *Python Crash Course*.

Exercise: 19-3 Protected Blog

Current progress:

- corrected the "edit entry" button text to "edit post"
- fixed a bug where logging in would always redirect to the homepage instead of the originally requested page
- modified the database schema by adding an `owner` field to protect user data, restricting access so users can only view their own data

## 🛠️ Tech Stack

- Python
- Django
- SQLite


## 🔗 Account Routes

- `/accounts/register/`
- `/accounts/login/`
- `/accounts/logout/`

## 📘 Learning Notes

- reinforced Django's `MTV` structure: `Model`, `Template`, and `View`
- how Django manages (collect and store username and password) user accounts
- data protection by associating data with specific users via foreign keys (`owner`)
- handling access control to restrict users from viewing or modifying others' data

## ⚠️ Note

This project is still in progress and is mainly for learning Django basics.

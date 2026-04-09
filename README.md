# 🧠 Django Blog Practice

This is a small Django practice project based on exercises from *Python Crash Course*.

Exercise: 19-3 Protected Blog

Current progress:

- corrected the "edit entry" button text to "edit post"
- fixed a bug where logging in would always redirect to the homepage instead of the originally requested page
- modified the database schema by adding an `owner` field to protect user data, restricting access so users can only view their own data
## ✨ Extra Features (Beyond the Book)

The following advanced features were independently developed and added **on top of the original author's codebase** to significantly enhance user experience and data safety:

- **Edit Blog Metadata**: Added an `edit_blog` page, enabling users to modify the titles and subtitles of their existing blogs.
- **Dynamic Post Categorization**: Implemented a dynamic dropdown feature allowing users to seamlessly reassign a post to a different blog while editing.
- **Asynchronous Blog Creation**: Added the ability to create a brand new blog on the fly via a seamless asynchronous (AJAX) popup mechanism, without ever leaving the post editor.
- **Secure Deletion Mechanism**: Added deletion functionality for both Blogs and Posts, incorporating a strong anti-accidental deletion safeguard (requiring users to explicitly type 'DELETE') to manage cascading data destruction safely.

## 🛠️ Tech Stack

- Python
- Django
- SQLite
- Vanilla JavaScript (for asynchronous interactions)

## 🔗 Account Routes

- `/accounts/register/`
- `/accounts/login/`
- `/accounts/logout/`

## 📘 Learning Notes

- reinforced Django's `MTV` structure: `Model`, `Template`, and `View`
- how Django manages (collect and store username and password) user accounts
- data protection by associating data with specific users via foreign keys (`owner`)
- handling access control to restrict users from viewing, modifying, or deleting others' data
- integrating JavaScript's `fetch` API with Django for asynchronous data submissions and seamless UI updates without page reloads
- implementing strict POST-only constraints and multi-level user-confirmation dialogues to prevent CSRF vulnerabilities and accidental data loss

## 🚀 Future Enhancements (Scalability & Security)

While the current system implements robust ownership-based access control, the following enhancements are considered for a production-grade deployment:

*   **Rate Limiting**: To prevent authenticated users from spamming the `new_blog` API (which could lead to resource exhaustion and database pollution), I would implement rate limiting using tools like `django-ratelimit` or a Web Application Firewall (WAF) such as Cloudflare.
*   **Advanced Validation**: Implementing more granular field-level validation (e.g., minimum character counts, profanity filters) in `forms.py` to ensure only high-quality data enters the database.

## ⚠️ Note

This project is still in progress and is mainly for learning Django basics.

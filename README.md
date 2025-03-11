# Todo List Application

This application helps users manage their daily tasks efficiently with a clean and intuitive interface.

## Features

- ✅ Create, read, update, and delete todos
- 📱 Responsive design that works on desktop and mobile
- 🎨 Clean user interface
- 💾 Local storage persistence

## Getting Started

### Installation

1. Clone the repository:
```bash
git clone https://github.com/nrjss67/Todo_list.git
```

2. Navigate to the project directory:
```bash
cd todo_list
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Make migrations:
```bash
python manage.py migrate
```

5. Start the development server:
```bash
python manage.py runserver
```

5. Open your browser and visit `http://localhost:8000`

## Project Structure

```
todo_list/
|-- todo 
|-- todo_list/ # Django app
|-- templates/ # HTML templates
|-- manage.py # Django management script
|-- requirements.txt # Project dependencies
|-- README.md # Project documentation
```

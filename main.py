from fastapi import FastAPI, Request, Form
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
from datetime import datetime


app = FastAPI(title="Yugendar Portfolio")

app.mount(
    "/static",
    StaticFiles(directory="static"),
    name="static"
)

templates = Jinja2Templates(directory="templates")


name = "Gadicherla Yugendar"
email = "yugendargadicherla566@gmail.com"

github_url = "https://github.com/yugendar123"

linkedin_url = (
    "https://www.linkedin.com/in/"
    "gadicherla-yugendar-b97b71394/"
)


skills = {
    "Programming": ["Python", "OOP", "SQL"],
    "Backend Development": ["FastAPI", "Flask", "REST APIs"],
    "Frontend": ["HTML5", "CSS3", "Jinja2"],
    "Database": ["MySQL", "SQLite"],
    "AI & ML": ["Machine Learning", "Computer Vision"],
    "Tools": ["Git", "GitHub", "Uvicorn"]
}


projects = [
    {
        "number": "01",
        "title": "Student-portal",
        "category": " /full-stack",
        "description": (
            "Student Portal is a web-based application developed using FastAPI that provides a centralized platform for students to manage their accounts and access student-related information. It includes user authentication, role-based access control, student dashboards, and an admin panel for managing student records"
        ),
        "technologies": [
            "Python",
            "Fastapi",
            "Role based access control"
        ],
        "github": "#"
    },
    {
        "number": "02",
        "title": "Crowd Detection System",
        "category": "MACHINE LEARNING / COMPUTER VISION",
        "description": (
            "A computer vision project focused on identifying "
            "and monitoring crowds using machine learning "
            "techniques."
        ),
        "technologies": [
            "Python",
            "Machine Learning",
            "Computer Vision"
        ],
        "github": "#"
    },
    {
        "number": "03",
        "title": "Product Management Application",
        "category": "WEB DEVELOPMENT / BACKEND",
        "description": (
            "A web application built using FastAPI, database "
            "integration and Jinja2 templates for product "
            "management and displaying product information."
        ),
        "technologies": [
            "FastAPI",
            "MySQL",
            "Jinja2"
        ],
        "github": (
            "https://github.com/yugendar123/"
            "fastapijinja2project"
        )
    }
]


@app.get("/")
async def home(request: Request):

    theme = request.cookies.get("theme", "dark")

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "theme": theme,
            "name": name,
            "email": email,
            "github_url": github_url,
            "linkedin_url": linkedin_url,
            "skills": skills,
            "projects": projects,
            "year": datetime.now().year
        }
    )


@app.post("/set-theme")
async def set_theme(request: Request):

    current_theme = request.cookies.get("theme", "dark")

    new_theme = (
        "light"
        if current_theme == "dark"
        else "dark"
    )

    response = RedirectResponse(
        url="/",
        status_code=303
    )

    response.set_cookie(
        key="theme",
        value=new_theme,
        max_age=60 * 60 * 24 * 30,
        httponly=True,
        samesite="lax"
    )

    return response


@app.post("/contact")
async def contact(
    name: str = Form(...),
    email: str = Form(...),
    message: str = Form(...)
):

    

    response = RedirectResponse(
        url="/?contact=success#contact",
        status_code=303
    )

    return response

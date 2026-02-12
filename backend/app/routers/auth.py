from sqlalchemy.exc import IntegrityError

@router.post("/register")
def register_user(
    request: Request,
    first_name: str = Form(...),
    last_name: str = Form(...),
    username: str = Form(...),
    birth_date: date = Form(...),
    password: str = Form(...),
    db: Session = Depends(get_db)
):
    try:
        user = User(
            first_name=first_name,
            last_name=last_name,
            username=username,
            birth_date=birth_date,
            password_hash=hash_password(password)
        )

        db.add(user)
        db.commit()

    except IntegrityError:
        db.rollback()
        return templates.TemplateResponse(
            "register.html",
            {
                "request": request,
                "error": "Ce nom d’utilisateur existe déjà."
            }
        )

    except Exception as e:
        db.rollback()
        return templates.TemplateResponse(
            "register.html",
            {
                "request": request,
                "error": "Erreur interne. Veuillez réessayer."
            }
        )

    return RedirectResponse("/login", status_code=303)

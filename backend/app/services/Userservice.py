from app.models.user import User
class UserService:
    def __init__(self,db,a):
        self.db = db
        self.a = a

    def create_user(self):
        user=User(
            name=self.a.name,
            email=self.a.email,
            password=self.a.password,
            dob=self.a.dob,
            exp=self.a.experience
        )
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)

        return user


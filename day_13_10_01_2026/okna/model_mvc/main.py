from models.user_model import UserModel
from controllers.user_controller import UserController
from views.main_view import MainView

model = UserModel()
controller = UserController(model)
view = MainView(controller)

view.mainloop()

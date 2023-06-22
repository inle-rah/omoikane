from django.urls import path
from .import views #app内のviewsファイルから取得
from .views import TaskList, TaskDetail, TaskCreate, TaskUpdate, TaskDelete, TaskListLoginView, RegisterOmoikaneApp
from django.contrib.auth.views import LogoutView

# viewsで新しいクラスを作成→urlsでアクセスするURLを都度用意する
urlpatterns = [
    path("", TaskList.as_view(), name="tasks"),
    path("task/<int:pk>/", TaskDetail.as_view(), name="task") ,
    #pk:プライマリキー name:nameを選択すると該当pathに飛ぶ
    path("create-task/", TaskCreate.as_view(), name="create-task"),
    path("edit-task/<int:pk>/", TaskUpdate.as_view(), name="edit-task") ,
    path("delete-task/<int:pk>/", TaskDelete.as_view(), name="delete-task") ,
    path("login/", TaskListLoginView.as_view(), name="login") ,
    path("logout/", LogoutView.as_view(next_page="login"), name="logout"),
    path("register/", RegisterOmoikaneApp.as_view(), name="register")  
]

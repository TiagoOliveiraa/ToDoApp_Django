from django.urls import path
from .views import taskList, taskDetail, taskCreate, taskDelete, taskUpdate, CustomLogin, RegisterPage
from .views import teamList,teamTaskList, teamTaskCreate, teamCreate, teamEdit
from .views import teamInvite, inviteList, accept_invite, accept_invite_home, deny_invite, deny_invite_home
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', taskList.as_view(), name='tasks'),
    path('team-task-list/<int:id>/',teamTaskList.as_view(),name="team-task-list"),
    path('task/<int:pk>/', taskDetail.as_view(), name='tasks'),
    path('task-create/',taskCreate.as_view(), name='task-create'),
    path('task-update/<int:pk>/', taskUpdate.as_view(), name="task-update"),
    path('task-delete/<int:pk>/', taskDelete.as_view(), name='task-delete'),
    path('login/',CustomLogin.as_view(),name='login'),
    path('logout/',LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', RegisterPage.as_view(), name='register'),
    path('team-list/',teamList.as_view(),name="team-list"),
    path('team-task-create/<int:id>/',teamTaskCreate.as_view(), name="team-task-create"),
    path('team-create/',teamCreate.as_view(), name="team-create"),
    path('team-invitation/<int:id>/', teamInvite.as_view(), name="team-invite"),
    path('invite-list/', inviteList.as_view(), name="invite-list"),
    path('accept-invite-home/<int:id>/', accept_invite_home, name="accept-invite-home"),
    path('deny-invite-home/<int:id>/', deny_invite_home, name="deny-invite-home"),
    path('accept-invite/<int:id>/', accept_invite, name="accept-invite"),
    path('deny-invite/<int:id>/', deny_invite, name="deny-invite"),
    path('team-detail/<int:pk>',teamEdit.as_view(), name="team-detail")
]
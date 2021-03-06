from django.urls import include, path
from . import views
from rest_framework_nested import routers

router = routers.DefaultRouter()

router.register(r'projects',
                views.ProjectViewSet,
                basename='projects')

contributors_router = routers.NestedDefaultRouter(router,
                                                  r'projects',
                                                  lookup='project')
contributors_router.register(r'users',
                             views.ContributorViewSet,
                             basename='project-contributors')

issues_router = routers.NestedDefaultRouter(router,
                                            r'projects',
                                            lookup='project')
issues_router.register(r'issues',
                       views.IssueViewSet,
                       basename='project-issues')

comments_router = routers.NestedDefaultRouter(issues_router,
                                              r'issues',
                                              lookup='issue')
comments_router.register(r'comments', views.CommentViewSet,
                         basename='issues-comments')

urlpatterns = [
    path(r'', include(router.urls)),
    path(r'', include(contributors_router.urls)),
    path(r'', include(issues_router.urls)),
    path(r'', include(comments_router.urls)),
]

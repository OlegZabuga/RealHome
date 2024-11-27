from .dataclasses import ProjectData
from realty.models.project import Project


class ProjectRepository:
    @staticmethod
    def get_all_projects():
        projects = Project.objects.all()
        return [
            ProjectData(
                id=project.id,
                name=project.name,
                description=project.description,
                amount_floors=project.amount_floors,
                rating=project.rating,
                image_url=project.image,
            )
            for project in projects
        ]

    @staticmethod
    def get_project_by_id(project_id):
        try:
            project = Project.objects.get(id=project_id)
            return ProjectData(
                id=project.id,
                name=project.name,
                description=project.description,
                amount_floors=project.amount_floors,
                rating=project.rating,
                image_url=project.image
            )
        except Exception:
            raise ValueError(f'Ошибка! Проект с id {project_id} не существует')
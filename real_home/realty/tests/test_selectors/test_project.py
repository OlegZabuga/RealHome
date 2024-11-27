from django.test import TestCase
from realty.domain.project.selectors import ProjectRepository
from realty.models import Project


class ProjectRepositoryTest(TestCase):
    def setUp(self):
        self.project1 = Project.objects.create(
            name='first',
            description='first',
            amount_floors=9,
            rating='A',
            image='image.jpg',
        )

        self.project2 = Project.objects.create(
            name='second',
            description='second',
            amount_floors=9,
            rating='A',
            image='image2.jpg',
        )

    def test_get_all_projects(self):
        projects = ProjectRepository.get_all_projects()
        self.assertEqual(len(projects), 2)

        project_data = projects[0]
        self.assertEqual(project_data.id, self.project1.id)
        self.assertEqual(project_data.name, self.project1.name)
        self.assertEqual(project_data.description, self.project1.description)
        self.assertEqual(project_data.amount_floors, self.project1.amount_floors)
        self.assertEqual(project_data.rating, self.project1.rating)
        self.assertEqual(project_data.image_url, self.project1.image)

    def test_get_project_by_id_success(self):
        project_data = ProjectRepository.get_project_by_id(self.project1.id)

        self.assertEqual(project_data.id, self.project1.id)
        self.assertEqual(project_data.name, self.project1.name)
        self.assertEqual(project_data.description, self.project1.description)
        self.assertEqual(project_data.amount_floors, self.project1.amount_floors)
        self.assertEqual(project_data.rating, self.project1.rating)
        self.assertEqual(project_data.image_url, self.project1.image)

    def test_get_project_by_id_fail(self):
        with self.assertRaises(ValueError) as context:
            ProjectRepository.get_project_by_id(10)
        self.assertEqual(str(context.exception), 'Ошибка! Проект с id 10 не существует')
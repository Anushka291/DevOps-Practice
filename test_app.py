import unittest
from app import app, contents

class FlaskTest(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

        # backup original data
        self.original = contents.copy()

        # clear data before each test
        contents.clear()

    def tearDown(self):
        # restore original data
        contents.clear()
        contents.extend(self.original)

    # ✅ HOME
    def test_home(self):
        res = self.app.get('/')
        self.assertEqual(res.status_code, 200)

    # ✅ ADD
    def test_add(self):
        res = self.app.post('/', data={
            "title": "Test",
            "description": "Desc"
        }, follow_redirects=True)

        self.assertEqual(res.status_code, 200)

        self.assertIn(["Test", "Desc"], contents)

    # ✅ EDIT
    def test_edit(self):
        contents.append(["Old", "Data"])

        res = self.app.post('/edit/0', data={
            "title": "New",
            "description": "Updated"
        }, follow_redirects=True)

        self.assertEqual(res.status_code, 200)

        self.assertIn(["New", "Updated"], contents)

    # ✅ DELETE
    def test_delete(self):
        contents.append(["Delete", "Me"])

        res = self.app.post('/delete/0', follow_redirects=True)

        self.assertEqual(res.status_code, 200)

        self.assertNotIn(["Delete", "Me"], contents)


if __name__ == "__main__":
    unittest.main()